import concurrent.futures
import subprocess

DOMAINS = [
    "colombogazette.com",
    "counterpoint.lk",
    "dbsjeyaraj.com",
    "deshaya.lk",
    "english.lankaviews.com",
    "kottu.org",
    "lankacnews.com",
    "lankahq.net",
    "lankatnews.com",
    "neruppu.com",
    "news.yahoo.com",
    "onlineuthayan.com",
    "redfm.lk",
    "sathhanda.lk",
    "sirasatv.lk",
    "sithafm.lk",
    "thesamnet.co.uk",
    "ada.lk",
    "adaderana.lk",
    "army.lk",
    "aruna.lk",
    "asianmirror.lk",
    "bbc.co.uk",
    "col3negoriginal.com",
    "colomboxnews.com",
    "dailymirror.lk",
    "dailynews.lk",
    "defence.lk",
    "derana.lk",
    "dinamina.lk",
    "divaina.com",
    "elukathir.lk",
    "euthayan.com",
    "eyesrilanka.com",
    "fmderana.lk",
    "frontpage.lk",
    "ft.lk",
    "goldfm.lk",
    "groundviews.org",
    "hirufm.lk",
    "hirunews.lk",
    "hirutv.lk",
    "ilankainet.com",
    "island.lk",
    "itn.lk",
    "jaffnamuslim.com",
    "lakhanda.lk",
    "lakresa.net",
    "lankabusinessonline.com",
    "lankadeepa.lk",
    "lankaenews.com",
    "lankanewspapers.com",
    "lankanewsweb.com",
    "lankapuvath.lk",
    "lankasrinews.com",
    "lankatruth.com",
    "lankaweb.com",
    "lmd.lk",
    "mawbima.lk",
    "navaliya.com",
    "news.lk",
    "newsfirst.lk",
    "rangiri.com",
    "rivira.lk",
    "rupavahini.lk",
    "sannasa.net",
    "sarasaviya.lk",
    "silumina.lk",
    "siyathafm.lk",
    "slbc.lk",
    "slguardian.org",
    "sooriyanfm.lk",
    "srilankamirror.com",
    "sundayobserver.lk",
    "sundaytimes.lk",
    "sunfm.lk",
    "swarnavahini.lk",
    "tamilmirror.lk",
    "tamilnet.com",
    "themorning.lk",
    "thenee.com",
    "thinakaran.lk",
    "thinakkural.lk",
    "tnlrocks.com",
    "vikalpa.org",
    "vimasuma.com",
    "virakesari.lk",
    "vivalanka.com",
    "yesfmonline.com",
    "yfm.lk",
    "youtube.com",
    "ceylontoday.lk",
    "colombotelegraph.com",
    "divesanews.com",
    "economynext.com",
    "monara.com",
    "nethfm.lk",
    "newsradio.lk",
    "radio.com.lk",
    "rhythmfm.lk",
    "roar.media",
    "shakthifm.com",
    "siyathanews.lk",
    "theleader.lk",
    "budusarana.lk",
    "espncricinfo.com",
    "infolanka.com",
    "newswire.lk",
    "shaafm.lk",
    "vfm.lk"
]

def check_domain(domain):
    # Try HTTPS then HTTP using curl via subprocess
    url = f"https://{domain}/"
    cmd = [
        "curl", "-s", "-o", "/dev/null", "-I", 
        "-w", "%{http_code}", "--max-time", "3", 
        "-L", "--connect-timeout", "2",
        "-k",  # Insecure ssl verify
        "-A", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        url
    ]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True)
        code = res.stdout.strip()
        if code and code != "000" and code != "00":
            return domain, True, int(code)
    except:
        pass
    
    url_http = f"http://{domain}/"
    cmd[-1] = url_http
    try:
        res = subprocess.run(cmd, capture_output=True, text=True)
        code = res.stdout.strip()
        if code and code != "000" and code != "00":
            return domain, True, int(code)
    except:
        pass
        
    return domain, False, "offline"

def main():
    unique_domains = sorted(list(set(DOMAINS)))
    print(f"Checking {len(unique_domains)} unique domains using curl subprocesses...")
    
    online = []
    offline = []
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=40) as executor:
        results = executor.map(check_domain, unique_domains)
        for domain, is_online, status in results:
            if is_online:
                online.append((domain, status))
            else:
                offline.append((domain, status))
                
    print(f"\n--- ONLINE ({len(online)}) ---")
    for d, s in sorted(online):
        print(f"  {d} (HTTP {s})")
        
    print(f"\n--- OFFLINE / TIMEOUT ({len(offline)}) ---")
    for d, err in sorted(offline):
        print(f"  {d} ({err})")

if __name__ == "__main__":
    main()
