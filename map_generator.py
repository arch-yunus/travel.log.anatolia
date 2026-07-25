import json
import os
import folium
import re

class MapGenerator:
    def __init__(self, data_file="travel_data.json", output_file="travel_map.html"):
        self.data_file = data_file
        self.output_file = output_file
        
        # Approximate coordinates for the 81 provinces to plot them exactly
        self.city_coords = {
            "Adana": [37.0000, 35.3213], "Adıyaman": [37.7648, 38.2786], "Afyonkarahisar": [38.7507, 30.5567],
            "Ağrı": [39.7191, 43.0503], "Aksaray": [38.3687, 34.0370], "Amasya": [40.6500, 35.8333],
            "Ankara": [39.9208, 32.8541], "Antalya": [36.8841, 30.7056], "Ardahan": [41.1105, 42.7022],
            "Artvin": [41.1828, 41.8183], "Aydın": [37.8444, 27.8458], "Balıkesir": [39.6484, 27.8826],
            "Bartın": [41.6344, 32.3375], "Batman": [37.8812, 41.1351], "Bayburt": [40.2552, 40.2249],
            "Bilecik": [40.1451, 29.9798], "Bingöl": [38.8847, 40.4939], "Bitlis": [38.4011, 42.1078],
            "Bolu": [40.7392, 31.6111], "Burdur": [37.7204, 30.2908], "Bursa": [40.1828, 29.0667],
            "Çanakkale": [40.1553, 26.4142], "Çankırı": [40.6013, 33.6134], "Çorum": [40.5506, 34.9556],
            "Denizli": [37.7765, 29.0864], "Diyarbakır": [37.9144, 40.2306], "Düzce": [40.8438, 31.1565],
            "Edirne": [41.6771, 26.5557], "Elazığ": [38.6810, 39.2264], "Erzincan": [39.7500, 39.5000],
            "Erzurum": [39.9043, 41.2679], "Eskişehir": [39.7767, 30.5206], "Gaziantep": [37.0662, 37.3833],
            "Giresun": [40.9128, 38.3895], "Gümüşhane": [40.4597, 39.4745], "Hakkari": [37.5833, 43.7333],
            "Hatay": [36.2000, 36.1667], "Iğdır": [39.9237, 44.0450], "Isparta": [37.7648, 30.5566],
            "İstanbul": [41.0082, 28.9784], "İzmir": [38.4192, 27.1287], "Kahramanmaraş": [37.5847, 36.9339],
            "Karabük": [41.2061, 32.6226], "Karaman": [37.1811, 33.2222], "Kars": [40.6013, 43.0975],
            "Kastamonu": [41.3766, 33.7765], "Kayseri": [38.7312, 35.4787], "Kilis": [36.7161, 37.1150],
            "Kırıkkale": [39.8468, 33.5153], "Kırklareli": [41.7333, 27.2167], "Kırşehir": [39.1425, 34.1709],
            "Kocaeli": [40.7654, 29.9408], "Konya": [37.8667, 32.4833], "Kütahya": [39.4167, 29.9833],
            "Malatya": [38.3552, 38.3095], "Manisa": [38.6191, 27.4289], "Mardin": [37.3122, 40.7339],
            "Mersin": [36.8000, 34.6333], "Muğla": [37.2153, 28.3636], "Muş": [38.7304, 41.4910],
            "Nevşehir": [38.6244, 34.7144], "Niğde": [37.9667, 34.6833], "Ordu": [40.9839, 37.8764],
            "Osmaniye": [37.0742, 36.2472], "Rize": [41.0201, 40.5234], "Sakarya": [40.6940, 30.4358],
            "Samsun": [41.2867, 36.3300], "Şanlıurfa": [37.1500, 38.8000], "Siirt": [37.9333, 41.9500],
            "Sinop": [42.0231, 35.1531], "Şırnak": [37.5164, 42.4611], "Sivas": [39.7477, 37.0179],
            "Tekirdağ": [40.9833, 27.5167], "Tokat": [40.3167, 36.5500], "Trabzon": [41.0015, 39.7178],
            "Tunceli": [39.1079, 39.5401], "Uşak": [38.6823, 29.4082], "Van": [38.4891, 43.3853],
            "Yalova": [40.6500, 29.2833], "Yozgat": [39.8181, 34.8147], "Zonguldak": [41.4564, 31.7987],
            # Aliases
            "Afyon": [38.7507, 30.5567], "Urfa": [37.1500, 38.8000], "Maras": [37.5847, 36.9339]
        }
        
    def _normalize(self, name):
        tr_to_en = {
            'ı': 'i', 'I': 'I', 'İ': 'I', 'i': 'i',
            'ğ': 'g', 'Ğ': 'G',
            'ü': 'u', 'Ü': 'U',
            'ş': 's', 'Ş': 'S',
            'ö': 'o', 'Ö': 'O',
            'ç': 'c', 'Ç': 'C'
        }
        name = name.translate(str.maketrans(tr_to_en))
        return name.lower().strip()

    def _find_city_path(self, city_name):
        regions = ["01_Marmara", "02_Ege", "03_Akdeniz", "04_IcAnadolu", "05_Karadeniz", "06_DoguAnadolu", "07_GuneydoguAnadolu"]
        norm_target = self._normalize(city_name)
        
        for r in regions:
            if os.path.exists(r):
                for folder in os.listdir(r):
                    if self._normalize(folder) == norm_target:
                        return os.path.join(r, folder)
        return None

    def generate_map(self):
        # We find visited checking README actual list
        visited_cities = set()
        if os.path.exists("README.md"):
            with open("README.md", "r", encoding="utf-8") as f:
                content = f.read()
                matches = re.findall(r"✅ \*\*([^\*]+)\*\*", content)
                for m in matches:
                    visited_cities.add(m.strip())

        # Load deep details from script if possible
        try:
            from enrich_visited_deep import VISITED_DEEP_DETAILS
        except ImportError:
            VISITED_DEEP_DETAILS = {}

        # Center of Turkey approx: 38.9637, 35.2433
        m = folium.Map(location=[38.9637, 35.2433], zoom_start=6, tiles='CartoDB dark_matter', control_scale=True)
        
        total_cities = 81
        visited_count = len(visited_cities)
        pct = (visited_count / total_cities) * 100
        
        # UI Styling Tokens (CSS)
        css_style = """
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&family=Inter:wght@300;400;500;600&display=swap');
        
        .map-title-panel {
            position: absolute;
            top: 20px;
            left: 70px;
            z-index: 1000;
            background: rgba(15, 23, 42, 0.85);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            padding: 20px 24px;
            border-radius: 16px;
            color: #fff;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
            max-width: 320px;
            transition: all 0.3s ease;
        }
        .map-title-panel:hover {
            border-color: rgba(255, 255, 255, 0.15);
            box-shadow: 0 12px 40px rgba(0, 0, 0, 0.6);
        }
        .map-title-panel h1 {
            font-family: 'Outfit', sans-serif;
            font-size: 18px;
            font-weight: 700;
            margin: 0 0 6px 0;
            background: linear-gradient(135deg, #2ecc71, #00f2fe);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            letter-spacing: 0.5px;
        }
        .map-title-panel p.subtitle {
            font-size: 11px;
            color: #94a3b8;
            margin: 0 0 16px 0;
            line-height: 1.4;
        }
        .progress-container {
            margin-bottom: 12px;
        }
        .progress-info {
            display: flex;
            justify-content: space-between;
            font-size: 11px;
            color: #cbd5e1;
            margin-bottom: 6px;
            font-weight: 500;
        }
        .progress-bar-bg {
            width: 100%;
            height: 6px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 3px;
            overflow: hidden;
        }
        .progress-bar-fill {
            height: 100%;
            background: linear-gradient(90deg, #2ecc71, #00f2fe);
            box-shadow: 0 0 8px rgba(46, 204, 113, 0.5);
            border-radius: 3px;
        }
        .panel-quote {
            font-style: italic;
            font-size: 10.5px;
            color: #64748b;
            border-left: 2px solid #2ecc71;
            padding-left: 8px;
            margin: 12px 0 0 0;
        }
        .pulsing-marker {
            position: relative;
            width: 16px;
            height: 16px;
        }
        .pulsing-marker .dot {
            width: 10px;
            height: 10px;
            border-radius: 50%;
            background: #2ecc71;
            box-shadow: 0 0 10px #2ecc71;
            position: absolute;
            top: 3px;
            left: 3px;
            cursor: pointer;
            border: 2px solid #ffffff;
            transition: all 0.2s ease;
        }
        .pulsing-marker:hover .dot {
            transform: scale(1.3);
            background: #00f2fe;
            box-shadow: 0 0 15px #00f2fe;
        }
        .pulsing-marker .pulse {
            position: absolute;
            top: -5px;
            left: -5px;
            height: 26px;
            width: 26px;
            border-radius: 50%;
            background: rgba(46, 204, 113, 0.35);
            animation: pulse-ring 2s cubic-bezier(0.455, 0.03, 0.515, 0.955) infinite;
            pointer-events: none;
        }
        @keyframes pulse-ring {
            0% { transform: scale(0.3); opacity: 1; }
            80%, 100% { transform: scale(1.6); opacity: 0; }
        }
        .leaflet-popup-content-wrapper {
            background: rgba(15, 23, 42, 0.9) !important;
            backdrop-filter: blur(12px) !important;
            -webkit-backdrop-filter: blur(12px) !important;
            border: 1px solid rgba(255, 255, 255, 0.08) !important;
            border-radius: 16px !important;
            padding: 0 !important;
            overflow: hidden;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.6) !important;
            color: #fff !important;
        }
        .leaflet-popup-content {
            margin: 0 !important;
            width: 260px !important;
        }
        .leaflet-popup-tip {
            background: rgba(15, 23, 42, 0.9) !important;
            border: 1px solid rgba(255, 255, 255, 0.08) !important;
        }
        .custom-popup-card {
            display: flex;
            flex-direction: column;
            width: 260px;
        }
        .popup-image-header {
            height: 120px;
            background-size: cover;
            background-position: center;
            position: relative;
        }
        .popup-image-overlay {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(0deg, rgba(15, 23, 42, 0.95) 0%, rgba(15, 23, 42, 0.1) 100%);
        }
        .popup-city-title {
            position: absolute;
            bottom: 8px;
            left: 16px;
            font-family: 'Outfit', sans-serif;
            font-size: 16px;
            font-weight: 700;
            color: #fff;
            margin: 0;
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.6);
        }
        .popup-body-content {
            padding: 14px 16px;
        }
        .popup-excerpt {
            font-size: 11px;
            color: #cbd5e1;
            line-height: 1.5;
            margin: 0 0 8px 0;
            font-style: italic;
        }
        .popup-desc {
            font-size: 10px;
            color: #94a3b8;
            line-height: 1.4;
            margin: 0 0 12px 0;
        }
        .popup-action-btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 100%;
            padding: 8px 0;
            background: linear-gradient(135deg, #2ecc71, #27ae60);
            color: #fff !important;
            font-size: 11px;
            font-weight: 600;
            text-decoration: none !important;
            border-radius: 8px;
            transition: all 0.2s ease;
            box-shadow: 0 4px 12px rgba(46, 204, 113, 0.2);
            border: none;
            cursor: pointer;
            box-sizing: border-box;
        }
        .popup-action-btn:hover {
            background: linear-gradient(135deg, #2ecc71, #00f2fe);
            box-shadow: 0 4px 16px rgba(0, 242, 254, 0.35);
            transform: translateY(-1px);
        }
        .custom-tooltip {
            background: rgba(15, 23, 42, 0.9) !important;
            backdrop-filter: blur(8px) !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            color: #fff !important;
            border-radius: 6px !important;
            font-family: 'Inter', sans-serif !important;
            font-size: 10.5px !important;
            font-weight: 500 !important;
            padding: 4px 8px !important;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3) !important;
        }
        .unvisited-marker {
            transition: all 0.3s ease;
            cursor: pointer;
        }
        .unvisited-marker:hover {
            stroke: #00f2fe !important;
            fill: #00f2fe !important;
            r: 5px !important;
        }
        .visited-cities-list {
            margin-top: 14px;
            border-top: 1px solid rgba(255, 255, 255, 0.08);
            padding-top: 10px;
            max-height: 120px;
            overflow-y: auto;
            margin-bottom: 10px;
        }
        .visited-cities-list h3 {
            font-family: 'Outfit', sans-serif;
            font-size: 11px;
            font-weight: 600;
            color: #2ecc71;
            margin: 0 0 6px 0;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        .visited-cities-item {
            font-family: 'Inter', sans-serif;
            font-size: 11px;
            color: #cbd5e1;
            padding: 3px 0;
            border-bottom: 1px solid rgba(255, 255, 255, 0.03);
            display: flex;
            align-items: center;
        }
        .visited-cities-item::before {
            content: '✓';
            color: #2ecc71;
            margin-right: 6px;
            font-weight: bold;
        }
        .visited-cities-list::-webkit-scrollbar {
            width: 4px;
        }
        .visited-cities-list::-webkit-scrollbar-track {
            background: rgba(255, 255, 255, 0.02);
            border-radius: 2px;
        }
        .visited-cities-list::-webkit-scrollbar-thumb {
            background: rgba(255, 255, 255, 0.12);
            border-radius: 2px;
        }
        .visited-cities-list::-webkit-scrollbar-thumb:hover {
            background: #2ecc71;
        }
        """

        m.get_root().header.add_child(folium.Element(f"<style>{css_style}</style>"))
        
        # Build visited cities vertical list
        sorted_visited = sorted(list(visited_cities))
        cities_list_html = ""
        for city in sorted_visited:
            cities_list_html += f'<div class="visited-cities-item">{city}</div>'

        # Add the floating title panel
        progress_bar_fill = f'<div class="progress-bar-fill" style="width: {pct:.1f}%"></div>'
        title_panel_html = f'''
        <div class="map-title-panel">
            <h1>🇹🇷 ANADOLU SEYAHATNAMESİ</h1>
            <p class="subtitle">Bir seyyahın adımladığı kadim topraklar ve dijital gezi günlüğü.</p>
            <div class="progress-container">
                <div class="progress-info">
                    <span>Keşif İlerlemesi</span>
                    <span>%{pct:.1f} ({visited_count}/{total_cities})</span>
                </div>
                <div class="progress-bar-bg">
                    {progress_bar_fill}
                </div>
            </div>
            
            <div class="visited-cities-list">
                <h3>Ziyaret Edilen İller</h3>
                {cities_list_html}
            </div>
            
            <p class="panel-quote">"İyi bir gezginin sabit planları ve varmak gibi bir amacı yoktur."</p>
        </div>
        '''
        m.get_root().html.add_child(folium.Element(title_panel_html))

        plotted = 0
        for city_raw in visited_cities:
            # find coords
            for c_name, coords in self.city_coords.items():
                if self._normalize(c_name) == self._normalize(city_raw):
                    
                    # Find city path and banner
                    city_dir = self._find_city_path(city_raw)
                    banner_rel_path = "assets/banner.png"
                    quote_text = "Keşfedilen ve tefekkür edilen seyahat noktası."
                    readme_link = "#"
                    
                    if city_dir:
                        city_dir_html = city_dir.replace("\\", "/")
                        readme_link = f"{city_dir_html}/README.md"
                        if os.path.exists(os.path.join(city_dir, "banner.jpg")):
                            banner_rel_path = f"{city_dir_html}/banner.jpg"
                    
                    # Lookup deep details
                    lookup_key = city_raw
                    if city_raw == "İstanbul": lookup_key = "Istanbul"
                    if city_raw == "Çorum": lookup_key = "Corum"
                    
                    desc_text = ""
                    if lookup_key in VISITED_DEEP_DETAILS:
                        quote_text = VISITED_DEEP_DETAILS[lookup_key].get("quote", quote_text).strip('"')
                        full_desc = VISITED_DEEP_DETAILS[lookup_key].get("description", "")
                        # Take the first 2 sentences
                        sentences = [s.strip() for s in full_desc.split('. ') if s.strip()]
                        if len(sentences) > 0:
                            s1 = sentences[0]
                            if not s1.endswith('.'): s1 += '.'
                            desc_text = s1
                            if len(sentences) > 1:
                                s2 = sentences[1]
                                if not s2.endswith('.'): s2 += '.'
                                desc_text += " " + s2
                    
                    desc_html = f'<p class="popup-desc">{desc_text}</p>' if desc_text else ""
                    
                    popup_html = f'''
                    <div class="custom-popup-card">
                        <div class="popup-image-header" style="background-image: url('{banner_rel_path}')">
                            <div class="popup-image-overlay"></div>
                            <h3 class="popup-city-title">📍 {city_raw}</h3>
                        </div>
                        <div class="popup-body-content">
                            <p class="popup-excerpt">"{quote_text}"</p>
                            {desc_html}
                            <a href="{readme_link}" target="_blank" class="popup-action-btn">Gezi Günlüğünü Oku ➔</a>
                        </div>
                    </div>
                    '''
                    
                    popup = folium.Popup(popup_html, max_width=260)
                    
                    marker_html = f'''
                    <div class="pulsing-marker">
                        <div class="pulse"></div>
                        <div class="dot"></div>
                    </div>
                    '''
                    
                    folium.Marker(
                        location=coords,
                        popup=popup,
                        tooltip=folium.Tooltip(city_raw, class_name="custom-tooltip"),
                        icon=folium.DivIcon(
                            html=marker_html,
                            class_name="custom-pulsing-icon",
                            icon_size=(16, 16),
                            icon_anchor=(8, 8)
                        )
                    ).add_to(m)
                    
                    plotted += 1
                    break
        
        # Add unvisited as small dots
        for c_name, coords in self.city_coords.items():
            if c_name in ["Afyon", "Urfa", "Maras"]: continue # skip aliases
            
            is_visited = False
            for v in visited_cities:
                if self._normalize(c_name) == self._normalize(v):
                    is_visited = True
                    break
            
            if not is_visited:
                folium.CircleMarker(
                    location=coords,
                    radius=3,
                    color="#475569",
                    fill=True,
                    fill_color="#1e293b",
                    fill_opacity=0.8,
                    weight=1.5,
                    tooltip=folium.Tooltip(f"Keşfedilmeyi bekliyor: {c_name}", class_name="custom-tooltip"),
                    class_name="unvisited-marker"
                ).add_to(m)

        m.save(self.output_file)
        return plotted

if __name__ == "__main__":
    mg = MapGenerator()
    mg.generate_map()
    print("Map generated.")
