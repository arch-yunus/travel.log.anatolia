import os
import json
import re

def _find_city_path(city_name):
    regions = ["01_Marmara", "02_Ege", "03_Akdeniz", "04_IcAnadolu", "05_Karadeniz", "06_DoguAnadolu", "07_GuneydoguAnadolu"]
    tr_to_en = {
        'ı': 'i', 'İ': 'I', 'ş': 's', 'Ş': 'S', 'ğ': 'g', 'Ğ': 'G',
        'ü': 'u', 'Ü': 'U', 'ö': 'o', 'Ö': 'O', 'ç': 'c', 'Ç': 'C'
    }
    norm_target = city_name.translate(str.maketrans(tr_to_en)).lower().strip()
    
    for r in regions:
        if os.path.exists(r):
            for folder in os.listdir(r):
                folder_norm = folder.translate(str.maketrans(tr_to_en)).lower().strip()
                if folder_norm == norm_target:
                    return r, folder
    return None, None

def main():
    try:
        from enrich_visited_deep import VISITED_DEEP_DETAILS, REGIONS_MAP
    except ImportError:
        print("Could not import enrich_visited_deep.")
        return
        
    web_cities = {}
    
    # We find visited checking README actual list
    visited_cities = set()
    if os.path.exists("README.md"):
        with open("README.md", "r", encoding="utf-8") as f:
            content = f.read()
            matches = re.findall(r"✅ \*\*([^\*]+)\*\*", content)
            for m in matches:
                visited_cities.add(m.strip())

    REGIONS_INFO = {
        "01_Marmara": "Marmara Bölgesi",
        "02_Ege": "Ege Bölgesi",
        "03_Akdeniz": "Akdeniz Bölgesi",
        "04_IcAnadolu": "İç Anadolu Bölgesi",
        "05_Karadeniz": "Karadeniz Bölgesi",
        "06_DoguAnadolu": "Doğu Anadolu Bölgesi",
        "07_GuneydoguAnadolu": "Güneydoğu Anadolu Bölgesi"
    }

    for city_name in sorted(list(visited_cities)):
        lookup_key = city_name
        if city_name == "İstanbul": lookup_key = "Istanbul"
        if city_name == "Çorum": lookup_key = "Corum"
        if city_name == "Eskişehir": lookup_key = "Eskisehir"
        if city_name == "Gümüşhane": lookup_key = "Gumushane"
        if city_name == "Elazığ": lookup_key = "Elazig"
        
        region_dir, folder_name = _find_city_path(city_name)
        if not region_dir:
            continue
            
        banner_path = "assets/banner.png"
        city_banner = os.path.join(region_dir, folder_name, "banner.jpg")
        if os.path.exists(city_banner):
            banner_path = f"{region_dir}/{folder_name}/banner.jpg"
            
        details = VISITED_DEEP_DETAILS.get(lookup_key, {})
        
        web_cities[city_name] = {
            "name": folder_name,
            "region": REGIONS_INFO.get(region_dir, "Bilinmeyen Bölge"),
            "banner": banner_path,
            "hikmet": details.get("hikmet", "Henüz bir bilge sözü eklenmedi."),
            "quote": details.get("quote", "Seyahat, yeni gözlerle bakmaktır."),
            "description": details.get("description", "Açıklama mevcut değil."),
            "sufi_notes": details.get("sufi_notes", "İçsel not mevcut değil."),
            "gastronomi": details.get("gastronomi", ""),
            "landmarks": details.get("landmarks", []),
            "library": details.get("library", "")
        }
        
    js_content = f"const TRAVEL_DATA = {json.dumps(web_cities, ensure_ascii=False, indent=4)};\n"
    
    with open("web_data.js", "w", encoding="utf-8") as f:
        f.write(js_content)
        
    print("Generated web_data.js successfully with", len(web_cities), "cities.")

if __name__ == "__main__":
    main()
