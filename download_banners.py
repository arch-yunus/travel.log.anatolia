import os
import json
import urllib.request
import urllib.parse
from urllib.error import URLError
import time

REGIONS_MAP = {
    "01_Marmara": ["Istanbul", "Kocaeli", "Bursa"],
    "02_Ege": ["Denizli", "Mugla"],
    "03_Akdeniz": ["Antalya", "Adana", "Hatay", "Mersin", "Isparta"],
    "04_IcAnadolu": ["Ankara", "Konya", "Nevsehir", "Aksaray", "Eskisehir", "Sivas", "Kayseri", "Kirikkale"],
    "05_Karadeniz": ["Amasya", "Corum", "Samsun", "Sinop", "Giresun", "Ordu", "Trabzon", "Artvin", "Bayburt", "Gumushane", "Rize"],
    "06_DoguAnadolu": ["Ardahan", "Elazig", "Erzincan", "Erzurum", "Kars", "Malatya", "Tunceli", "Agri"],
    "07_GuneydoguAnadolu": []
}

USER_AGENT = 'Mozilla/5.0 (compatible; TravelLogBot/2.0; +https://github.com/bahattinyunus/travel.log)'

def get_city_image_url(city_name):
    tr_names = {
        'Adana': 'Adana', 'Adiyaman': 'Adıyaman', 'Afyonkarahisar': 'Afyonkarahisar', 'Agri': 'Ağrı',
        'Aksaray': 'Aksaray', 'Amasya': 'Amasya', 'Ankara': 'Ankara', 'Antalya': 'Antalya', 'Ardahan': 'Ardahan',
        'Artvin': 'Artvin', 'Aydin': 'Aydın', 'Balikesir': 'Balıkesir', 'Bartin': 'Bartın', 'Batman': 'Batman',
        'Bayburt': 'Bayburt', 'Bilecik': 'Bilecik', 'Bingol': 'Bingöl', 'Bitlis': 'Bitlis', 'Bolu': 'Bolu',
        'Burdur': 'Burdur', 'Bursa': 'Bursa', 'Canakkale': 'Çanakkale', 'Cankiri': 'Çankırı', 'Corum': 'Çorum',
        'Denizli': 'Denizli', 'Diyarbakir': 'Diyarbakır', 'Duzce': 'Düzce', 'Edirne': 'Edirne', 'Elazig': 'Elazığ',
        'Erzincan': 'Erzincan', 'Erzurum': 'Erzurum', 'Eskisehir': 'Eskişehir', 'Gaziantep': 'Gaziantep',
        'Giresun': 'Giresun', 'Gumushane': 'Gümüşhane', 'Hakkari': 'Hakkari', 'Hatay': 'Hatay', 'Igdir': 'Iğdır',
        'Isparta': 'Isparta', 'Istanbul': 'İstanbul', 'Izmir': 'İzmir', 'Kahramanmaras': 'Kahramanmaraş', 'Karabuk': 'Karabük',
        'Karaman': 'Karaman', 'Kars': 'Kars', 'Kastamonu': 'Kastamonu', 'Kayseri': 'Kayseri', 'Kilis': 'Kilis',
        'Kirikkale': 'Kırıkkale', 'Kirklareli': 'Kırklareli', 'Kirsehir': 'Kırşehir', 'Kocaeli': 'Kocaeli', 'Konya': 'Konya',
        'Kutahya': 'Kütahya', 'Malatya': 'Malatya', 'Manisa': 'Manisa', 'Mardin': 'Mardin', 'Mersin': 'Mersin',
        'Mugla': 'Muğla', 'Mus': 'Muş', 'Nevsehir': 'Nevşehir', 'Nigde': 'Niğde', 'Ordu': 'Ordu', 'Osmaniye': 'Osmaniye',
        'Rize': 'Rize', 'Sakarya': 'Sakarya', 'Samsun': 'Samsun', 'Sanliurfa': 'Şanlıurfa', 'Siirt': 'Siirt',
        'Sinop': 'Sinop', 'Sirnak': 'Şırnak', 'Sivas': 'Sivas', 'Tekirdag': 'Tekirdağ', 'Tokat': 'Tokat',
        'Trabzon': 'Trabzon', 'Tunceli': 'Tunceli', 'Usak': 'Uşak', 'Van': 'Van', 'Yalova': 'Yalova', 'Yozgat': 'Yozgat',
        'Zonguldak': 'Zonguldak'
    }
    query_city = tr_names.get(city_name, city_name)
    encoded_city = urllib.parse.quote(query_city)
    url = f"https://tr.wikipedia.org/w/api.php?action=query&titles={encoded_city}&prop=pageimages&format=json&pithumbsize=1200"
    
    req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
    try:
        time.sleep(1.0) # sleep 1 second before API request to avoid rate limit
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            pages = data.get('query', {}).get('pages', {})
            for page_id, page_data in pages.items():
                if 'thumbnail' in page_data:
                    return page_data['thumbnail']['source']
    except Exception as e:
        print(f"Error fetching URL for {city_name}: {e}")
    return None

def download_image(url, save_path):
    url = url.split('?')[0]
    req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
    for attempt in range(3):
        try:
            time.sleep(2.0 + attempt * 3.0)
            with urllib.request.urlopen(req) as response, open(save_path, 'wb') as out_file:
                data = response.read()
                out_file.write(data)
            return True
        except Exception as e:
            print(f"Error downloading {url} (attempt {attempt+1}): {e}")
    return False

def main():
    for region, cities in REGIONS_MAP.items():
        if not os.path.exists(region):
            print(f"Directory {region} not found, skipping.")
            continue
            
        actual_folders = os.listdir(region)
        for folder in actual_folders:
            clean_city = folder.strip()
            lookup_key = clean_city
            if clean_city == "İstanbul": lookup_key = "Istanbul"
            if clean_city == "Çorum": lookup_key = "Corum"
            
            # Verify if this is one of our target cities mapped
            all_cities = [c for lst in REGIONS_MAP.values() for c in lst]
            if lookup_key in all_cities:
                target_path = os.path.join(region, folder, "banner.jpg")
                # Skip if banner already exists and has non-zero size
                if os.path.exists(target_path) and os.path.getsize(target_path) > 0:
                    print(f"Banner already exists for {clean_city}, skipping.")
                    continue
                    
                print(f"Processing {clean_city}...")
                img_url = get_city_image_url(lookup_key)
                
                if img_url:
                    print(f"  -> Found image: {img_url}")
                    success = download_image(img_url, target_path)
                    print(f"  -> Saved to {target_path}: {success}")
                else:
                    print(f"  -> No Wikipedia page image found for {clean_city}.")

if __name__ == "__main__":
    main()
