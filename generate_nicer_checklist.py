import re
import math

provinces = {
    '🏰 Marmara Bölgesi': ['Balıkesir', 'Bilecik', 'Bursa', 'Çanakkale', 'Edirne', 'İstanbul', 'Kırklareli', 'Kocaeli', 'Sakarya', 'Tekirdağ', 'Yalova'],
    '🌊 Ege Bölgesi': ['Afyonkarahisar', 'Aydın', 'Denizli', 'İzmir', 'Kütahya', 'Manisa', 'Muğla', 'Uşak'],
    '☀️ Akdeniz Bölgesi': ['Adana', 'Antalya', 'Burdur', 'Hatay', 'Isparta', 'Kahramanmaraş', 'Mersin', 'Osmaniye'],
    '🌾 İç Anadolu Bölgesi': ['Aksaray', 'Ankara', 'Çankırı', 'Eskişehir', 'Karaman', 'Kayseri', 'Kırıkkale', 'Kırşehir', 'Konya', 'Nevşehir', 'Niğde', 'Sivas', 'Yozgat'],
    '🌲 Karadeniz Bölgesi': ['Amasya', 'Artvin', 'Bartın', 'Bayburt', 'Bolu', 'Çorum', 'Düzce', 'Giresun', 'Gümüşhane', 'Karabük', 'Kastamonu', 'Ordu', 'Rize', 'Samsun', 'Sinop', 'Tokat', 'Trabzon', 'Zonguldak'],
    '🏔️ Doğu Anadolu Bölgesi': ['Ağrı', 'Ardahan', 'Bingöl', 'Bitlis', 'Elazığ', 'Erzincan', 'Erzurum', 'Hakkari', 'Iğdır', 'Kars', 'Malatya', 'Muş', 'Tunceli', 'Van'],
    '🏜️ G.Doğu Anadolu Bölgesi': ['Adıyaman', 'Batman', 'Diyarbakır', 'Gaziantep', 'Kilis', 'Mardin', 'Siirt', 'Şanlıurfa', 'Şırnak']
}

def normalize_city(c):
    return c.strip().lower().replace(" ", "")

def extract_visited_from_readme(readme_path="README.md"):
    visited = set()
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract the visited cities using the ✅ **City** pattern
    matches = re.findall(r"✅ \*\*([^\*]+)\*\*", content)
    for m in matches:
        visited.add(normalize_city(m))
        
    return visited

def generate_visual_checklist(visited_normalized):
    total_cities = 81
    visited_actual = set()
    
    lines = ["## ✅ 81 İl Keşif Haritası", ""]
    
    # We will build the regions text while counting visited
    regions_text = []
    
    for region, cities in provinces.items():
        sorted_cities = sorted(cities)
        visited_in_region = 0
        city_strings = []
        for city in sorted_cities:
            if normalize_city(city) in visited_normalized:
                visited_in_region += 1
                visited_actual.add(city)
                city_strings.append(f"- ✅ **{city}**")
            else:
                city_strings.append(f"- ❌ {city}")
                
        regions_text.append(f"**{region} ({visited_in_region}/{len(cities)})**")
        regions_text.append("\n".join(city_strings))
        regions_text.append("")

    v_count = len(visited_actual)
    pct = (v_count / total_cities) * 100
    
    # Build progress bar
    bar_length = 20
    filled = math.floor((v_count / total_cities) * bar_length)
    empty = bar_length - filled
    bar = "🟩" * filled + "⬜" * empty

    lines.append(f"**🏆 Genel İlerleme:** %{pct:.1f} ({v_count} / {total_cities} İl)")
    lines.append(f"{bar}")
    lines.append("")
    lines.append("> *Sürücü koltuğunda bizzat geçilen ve anı biriktirilen eşsiz rotalar...*")
    lines.append("")
    
    lines.extend(regions_text)
    
    return "\n".join(lines)

def update_readme():
    visited = extract_visited_from_readme("README.md")
    checklist_md = generate_visual_checklist(visited)
    
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()
        
    # Replace existing checklist
    # from "## ✅ 81 İl Keşif Haritası" until "## 🧬 Kavramsal ve Teknik Mimari"
    new_content = re.sub(r"## ✅ 81 İl Keşif Haritası.*?(?=## 🧬 Kavramsal ve Teknik Mimari)", checklist_md + "\n", content, flags=re.DOTALL)
    
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)
        
    print(f"Updated README with nicer checklist! Total visited real cities: {len(visited)}")

if __name__ == "__main__":
    update_readme()
