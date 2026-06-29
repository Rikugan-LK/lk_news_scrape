import os
import glob
import re

NEWSPAPERS = [
    ("ColomboGazetteCom", "http://colombogazette.com/"),
    ("CounterpointLk", "http://counterpoint.lk/"),
    ("DeshayaLk", "http://deshaya.lk/"),
    ("EnglishLankaviewsCom", "http://english.lankaviews.com/"),
    ("KottuOrg", "http://kottu.org/"),
    ("LankacnewsCom", "http://lankacnews.com/english/"),
    ("LankahqNet", "http://lankahq.net/"),
    ("LankatnewsCom", "http://lankatnews.com/"),
    ("NeruppuCom", "http://neruppu.com/"),
    ("OnlineuthayanCom", "http://onlineuthayan.com/"),
    ("RedfmLk", "http://redfm.lk/"),
    ("SathhandaLk", "http://sathhanda.lk/"),
    ("SirasatvLk", "http://sirasatv.lk/"),
    ("SithafmLk", "http://sithafm.lk/"),
    ("ThesamnetCoUk", "http://thesamnet.co.uk/"),
    ("ArmyLk", "http://www.army.lk/"),
    ("ArunaLk", "http://www.aruna.lk/"),
    ("AsianmirrorLk", "http://www.asianmirror.lk/"),
    ("BbcCoUkTamil", "http://www.bbc.co.uk/tamil/"),
    ("Col3negoriginalCom", "http://www.col3negoriginal.com/"),
    ("ColomboxnewsCom", "http://www.colomboxnews.com/"),
    ("DefenceLk", "http://www.defence.lk/"),
    ("DeranaLk", "http://www.derana.lk/"),
    ("DinaminaLk", "http://www.dinamina.lk/"),
    ("ElukathirLk", "http://www.elukathir.lk/"),
    ("EuthayanCom", "http://www.euthayan.com/"),
    ("EyesrilankaCom", "http://www.eyesrilanka.com/"),
    ("FmderanaLk", "http://www.fmderana.lk/"),
    ("FrontpageLk", "http://www.frontpage.lk/"),
    ("GoldfmLk", "http://www.goldfm.lk/"),
    ("GroundviewsOrg", "http://www.groundviews.org/"),
    ("HirufmLk", "http://www.hirufm.lk/"),
    ("HirunewsLk", "http://www.hirunews.lk/"),
    ("HirutvLk", "http://www.hirutv.lk/"),
    ("IlankainetCom", "http://www.ilankainet.com/"),
    ("ItnLk", "http://www.itn.lk/"),
    ("JaffnamuslimCom", "http://www.jaffnamuslim.com/"),
    ("LakhandaLk", "http://www.lakhanda.lk/"),
    ("LakresaNet", "http://www.lakresa.net/"),
    ("LankabusinessonlineCom", "http://www.lankabusinessonline.com/"),
    ("LankaenewsCom", "http://www.lankaenews.com/English/"),
    ("LankanewspapersCom", "http://www.lankanewspapers.com/"),
    ("LankanewswebCom", "http://www.lankanewsweb.com/"),
    ("LankapuvathLk", "http://www.lankapuvath.lk/"),
    ("LankasrinewsCom", "http://www.lankasrinews.com/"),
    ("LankatruthCom", "http://www.lankatruth.com/home/"),
    ("LankawebCom", "http://www.lankaweb.com/"),
    ("LmdLk", "http://www.lmd.lk/"),
    ("MawbimaLk", "http://www.mawbima.lk/"),
    ("NavaliyaCom", "http://www.navaliya.com/"),
    ("NewsLk", "http://www.news.lk/"),
    ("RangiriCom", "http://www.rangiri.com/site/"),
    ("RiviraLk", "http://www.rivira.lk/"),
    ("RupavahiniLk", "http://www.rupavahini.lk/"),
    ("SannasaNet", "http://www.sannasa.net/"),
    ("SarasaviyaLk", "http://www.sarasaviya.lk/"),
    ("SiluminaLk", "http://www.silumina.lk/"),
    ("SiyathafmLk", "http://www.siyathafm.lk/"),
    ("SlbcLk", "http://www.slbc.lk/"),
    ("SlguardianOrg", "http://www.slguardian.org/"),
    ("SooriyanfmLk", "http://www.sooriyanfm.lk/"),
    ("SrilankamirrorCom", "http://www.srilankamirror.com/"),
    ("SundayobserverLk", "http://www.sundayobserver.lk/"),
    ("SundaytimesLk", "http://www.sundaytimes.lk/"),
    ("SunfmLk", "http://www.sunfm.lk/"),
    ("SwarnavahiniLk", "http://www.swarnavahini.lk/"),
    ("ThemorningLk", "http://www.themorning.lk/"),
    ("TheneeCom", "http://www.thenee.com/"),
    ("ThinakaranLk", "http://www.thinakaran.lk/"),
    ("ThinakkuralLk", "http://www.thinakkural.lk/"),
    ("TnlrocksCom", "http://www.tnlrocks.com/"),
    ("VikalpaOrg", "http://www.vikalpa.org/"),
    ("VimasumaCom", "http://www.vimasuma.com/"),
    ("VivalankaCom", "http://www.vivalanka.com/"),
    ("YesfmonlineCom", "http://www.yesfmonline.com/"),
    ("YfmLk", "http://www.yfm.lk/"),
    ("DivesanewsCom", "https://divesanews.com/"),
    ("MonaraCom", "https://monara.com/"),
    ("NethfmLk", "https://nethfm.lk/"),
    ("NewsradioLk", "https://newsradio.lk/"),
    ("RhythmfmLk", "https://rhythmfm.lk/"),
    ("RoarMedia", "https://roar.media/english/"),
    ("ShakthifmCom", "https://shakthifm.com/"),
    ("SiyathanewsLk", "https://siyathanews.lk/"),
    ("TheleaderLk", "https://theleader.lk/"),
    ("BudusaranaLk", "https://www.budusarana.lk/"),
    ("NewswireLk", "https://www.newswire.lk/"),
    ("ShaafmLk", "https://www.shaafm.lk/"),
    ("VfmLk", "https://www.vfm.lk/"),
]

# List of offline/timeout domains to move to the fallback folder
OFFLINE_CLASSES = {
    "ArmyLk", "EnglishLankaviewsCom", "EuthayanCom",
    "LankasrinewsCom", "LmdLk", "MawbimaLk", "NeruppuCom", "NewsradioLk",
    "RedfmLk", "RiviraLk", "RupavahiniLk", "SannasaNet", "SarasaviyaLk", "SathhandaLk",
    "SithafmLk", "SiyathafmLk",
    "SlbcLk", "SlguardianOrg", "SooriyanfmLk", "SrilankamirrorCom",
    "TamilnetCom", "TheleaderLk", "ThemorningLk", "TheneeCom", "ThesamnetCoUk",
    "ThinakaranLk", "ThinakkuralLk", "TnlrocksCom", "VfmLk", "VikalpaOrg", "VimasumaCom",
    "VirakesariLk", "VivalankaCom", "YesfmonlineCom", "YfmLk", "YoutubeCom"
}

CUSTOM_DIR = "src/news_lk3/custom_newspapers"
FALLBACK_DIR = "src/news_lk3/custom_newspapers/fallback"
FACTORY_PATH = "src/lk_news/NewspaperFactory.py"

def generate():
    # Make sure fallback directory exists
    os.makedirs(FALLBACK_DIR, exist_ok=True)

    # 1. Create custom newspapers (regular or fallback)
    for name, url in NEWSPAPERS:
        # Determine target folder
        is_fallback = name in OFFLINE_CLASSES
        target_dir = FALLBACK_DIR if is_fallback else CUSTOM_DIR
        filepath = os.path.join(target_dir, f"{name}.py")
        
        # Remove it from old regular folder if it was moved to fallback
        if is_fallback:
            old_path = os.path.join(CUSTOM_DIR, f"{name}.py")
            if os.path.exists(old_path):
                os.remove(old_path)
                print(f"Moved regular file to fallback: {name}")
        else:
            old_path = os.path.join(FALLBACK_DIR, f"{name}.py")
            if os.path.exists(old_path):
                os.remove(old_path)
                print(f"Moved fallback file to regular: {name}")
        
        if not os.path.exists(filepath):
            print(f"Creating newspaper: {name} -> {url} (fallback={is_fallback})")
            content = f"""from news_lk3.core import AbstractNewsPaper


class {name}(AbstractNewsPaper):
    @classmethod
    def get_index_urls(cls):
        return [
            '{url}',
        ]
"""
            with open(filepath, "w") as f:
                f.write(content)

    # 2. Get list of all py files in CUSTOM_DIR and FALLBACK_DIR
    reg_py_files = sorted(glob.glob(os.path.join(CUSTOM_DIR, "*.py")))
    fb_py_files = sorted(glob.glob(os.path.join(FALLBACK_DIR, "*.py")))
    
    classes_reg = []
    classes_fb = []
    
    init_content = ["# news_lk3.custom_newspapers (auto generated)", "# flake8: noqa: F401", ""]
    
    for filepath in reg_py_files:
        filename = os.path.basename(filepath)
        if filename == "__init__.py":
            continue
        classname = filename[:-3]
        classes_reg.append(classname)
        init_content.append(f"from news_lk3.custom_newspapers.{classname} import {classname}")
        
    for filepath in fb_py_files:
        filename = os.path.basename(filepath)
        if filename == "__init__.py":
            continue
        classname = filename[:-3]
        classes_fb.append(classname)
        init_content.append(f"from news_lk3.custom_newspapers.fallback.{classname} import {classname}")
        
    init_path = os.path.join(CUSTOM_DIR, "__init__.py")
    with open(init_path, "w") as f:
        f.write("\n".join(init_content) + "\n")
    print(f"Updated {init_path}")

    # Generate fallback/__init__.py
    fb_init_content = ["# news_lk3.custom_newspapers.fallback (auto generated)", "# flake8: noqa: F401", ""]
    for classname in classes_fb:
        fb_init_content.append(f"from news_lk3.custom_newspapers.fallback.{classname} import {classname}")
    fb_init_path = os.path.join(FALLBACK_DIR, "__init__.py")
    with open(fb_init_path, "w") as f:
        f.write("\n".join(fb_init_content) + "\n")
    print(f"Updated {fb_init_path}")

    # 3. Re-generate NewspaperFactory.py
    imports_list = []
    if classes_reg:
        imports_list.append(f"from news_lk3.custom_newspapers import (\n    " + ",\n    ".join(classes_reg) + "\n)")
    if classes_fb:
        imports_list.append(f"from news_lk3.custom_newspapers.fallback import (\n    " + ",\n    ".join(classes_fb) + "\n)")
        
    all_classes = sorted(classes_reg + classes_fb)
    
    factory_content = f"""{chr(10).join(imports_list)}


class NewspaperFactory:
    @staticmethod
    def list_all():
        return [
            {",\n            ".join(all_classes)}
        ]

    @staticmethod
    def list_all_testing():
        return [
            CeylonTodayLk,
        ]
"""
    with open(FACTORY_PATH, "w") as f:
        f.write(factory_content)
    print(f"Updated {FACTORY_PATH}")

if __name__ == "__main__":
    generate()
