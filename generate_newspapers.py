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

CUSTOM_DIR = "src/news_lk3/custom_newspapers"
FACTORY_PATH = "src/lk_news/NewspaperFactory.py"

def generate():
    # 1. Create missing custom newspapers
    for name, url in NEWSPAPERS:
        filepath = os.path.join(CUSTOM_DIR, f"{name}.py")
        if not os.path.exists(filepath):
            print(f"Creating newspaper: {name} -> {url}")
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

    # 2. Re-generate __init__.py
    py_files = sorted(glob.glob(os.path.join(CUSTOM_DIR, "*.py")))
    classes = []
    
    init_content = ["# news_lk3.custom_newspapers (auto generated)", "# flake8: noqa: F401", ""]
    
    for filepath in py_files:
        filename = os.path.basename(filepath)
        if filename == "__init__.py":
            continue
        classname = filename[:-3] # Remove .py
        classes.append(classname)
        init_content.append(f"from news_lk3.custom_newspapers.{classname} import {classname}")
        
    init_path = os.path.join(CUSTOM_DIR, "__init__.py")
    with open(init_path, "w") as f:
        f.write("\n".join(init_content) + "\n")
    print(f"Updated {init_path}")

    # 3. Re-generate NewspaperFactory.py
    imports = ", ".join(classes)
    # Format with nice lines
    imports_formatted = ",\n                                         ".join(classes)
    
    factory_content = f"""from news_lk3.custom_newspapers import (
    {",\n    ".join(classes)}
)


class NewspaperFactory:
    @staticmethod
    def list_all():
        return [
            {",\n            ".join(classes)}
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
