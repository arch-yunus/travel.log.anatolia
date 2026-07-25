import os

LIBRARIES = {
    "Istanbul": "Şemsipaşa İlçe Halk Kütüphanesi (Üsküdar) - Denize sıfır konumuyla tefekküre değer, internet hızı yüksek, priz imkanı sınırlı ama atmosferi büyüleyici.",
    "Bursa": "Bursa İl Halk Kütüphanesi - Sakin ve geniş çalışma alanları mevcut, araştırma kaynakları zengin, bahçesi mola için ideal.",
    "Kocaeli": "Kocaeli İl Halk Kütüphanesi - Modern iç tasarımı ve güçlü internet altyapısıyla kodlama mesaileri için son derece konforlu.",
    "Denizli": "Denizli İl Halk Kütüphanesi - Şehir merkezinde, sessiz çalışma salonları geniş, öğleden sonra kalabalık olabiliyor.",
    "Mugla": "Muğla İl Halk Kütüphanesi - Üniversite bölgesine yakın, çalışma ortamı sessiz ve ferah, priz sayısı yeterli.",
    "Antalya": "Antalya İl Halk Kütüphanesi - Yeşillikler içindeki bahçesi ve geniş okuma salonlarıyla Akdeniz sıcağında serin bir çalışma limanı.",
    "Mersin": "Mersin İl Halk Kütüphanesi - Sahile yakın, ferah çalışma masaları ve deniz manzaralı dinlenme alanlarıyla motivasyon verici.",
    "Adana": "Adana İl Halk Kütüphanesi - Şehir merkezinde yer alıyor, klimaları yaz sıcağında can kurtarıyor, priz imkanları iyi.",
    "Hatay": "Hatay İl Halk Kütüphanesi - Tarihi dokusuyla ilham verici, sessiz çalışma odaları tefekkür ve kodlama için çok uygun.",
    "Ankara": "Milli Kütüphane (Bahçelievler) - Türkiye'nin en büyük araştırma kütüphanesi, 24 saat açık salonları, sınırsız kaynak ve üst düzey çalışma disiplini ile kod yazmak için eşsiz bir mabet.",
    "Nevsehir": "Nevşehir İl Halk Kütüphanesi - Taş mimarisiyle huzurlu, sessiz odaları odağı artırmak için ideal.",
    "Konya": "Konya İl Halk Kütüphanesi - Geniş ve ferah salonları var, Selçuklu mimarisinin esintilerini taşıyor, çalışma disiplini yüksek.",
    "Samsun": "Samsun İl Halk Kütüphanesi - Karadeniz'in en modern kütüphanelerinden biri, priz ve internet altyapısı mükemmel.",
    "Sinop": "Sinop Rıza Nur İl Halk Kütüphanesi - Tarihi ve nostaljik ahşap binasıyla zamanda yolculuk hissi veriyor, huzurlu bir çalışma noktası.",
    "Giresun": "Giresun İl Halk Kütüphanesi - Harşit Vadisi esintileriyle serin, sakin çalışma masaları mevcut.",
    "Ordu": "Ordu İl Halk Kütüphanesi - Teleferik hattına yakın konumuyla mola vermeye uygun, çalışma salonları geniş.",
    "Trabzon": "Trabzon İl Halk Kütüphanesi - Şehir merkezinde vakur bir bina, araştırma ve geliştirme için sessiz odalar sunuyor.",
    "Amasya": "Amasya İl Halk Kütüphanesi - Yeşilırmak kıyısında, nehrin şırıltısı eşliğinde kod yazma deneyimi sunan eşsiz bir çalışma alanı.",
    "Corum": "Çorum İl Halk Kütüphanesi - Sessiz ve düzenli çalışma odalarıyla odaklanmayı kolaylaştıran sakin bir Anadolu kütüphanesi.",
    "Mardin": "Mardin İl Halk Kütüphanesi - Taş mimarisi ve Mezopotamya ovasına bakan avlusuyla seyyah yazılımcıya ilham kaynağı.",
    "Isparta": "Isparta Halil Hamit Paşa İl Halk Kütüphanesi - Şehir merkezinde, sessiz çalışma alanları geniş ve ferah.",
    "Aksaray": "Aksaray İl Halk Kütüphanesi - Bozkırın ortasında modern ve sessiz bir çalışma alanı.",
    "Eskisehir": "Eskişehir İl Halk Kütüphanesi - Genç nüfusun yoğun olduğu, dinamik, internet hızı yüksek ve priz imkanı bol olan modern kütüphane.",
    "Sivas": "Sivas Şems-i Sivasî İl Halk Kütüphanesi - Selçuklu esintileriyle bezeli geniş ve düzenli çalışma salonları.",
    "Artvin": "Artvin İl Halk Kütüphanesi - Yamaçta kurulu, manzaralı, dik yokuşlardan sonra dinlenip kod yazmak için ideal sessiz sığınak.",
    "Bayburt": "Bayburt İl Halk Kütüphanesi - Çoruh Nehri kıyısında, sessiz ve sakin bir çalışma ortamı.",
    "Gumushane": "Gümüşhane İl Halk Kütüphanesi - Vadinin serinliğinde, odaklanmayı kolaylaştıran butik ve huzurlu çalışma alanı.",
    "Rize": "Rize İl Halk Kütüphanesi - Çay tarlalarının yeşili eşliğinde, modern altyapısı ve güçlü internetiyle kodlama için ideal.",
    "Ardahan": "Ardahan İl Halk Kütüphanesi - Kışın sıcacık soba sıcaklığında, dışarıdaki dondurucu soğuğa inat sessizce kod yazma imkanı.",
    "Elazig": "Elazığ İl Halk Kütüphanesi - Gakgoşlar diyarında modern ve konforlu çalışma odalarıyla geniş bir kütüphane.",
    "Erzincan": "Erzincan İl Halk Kütüphanesi - Deprem sonrası yenilenen geniş caddelerin ortasında modern ve ferah bir kütüphane.",
    "Erzurum": "Erzurum Erzurumlu Emrah İl Halk Kütüphanesi - Tarihi dokusuyla dadaşların vakur çalışma disiplinini yansıtan sessiz çalışma limanı.",
    "Kars": "Kars İl Halk Kütüphanesi - Rus döneminden kalma taş binaların mistik havasında, karlar altında kodlama mesaisi yapabileceğiniz sıcak sığınak.",
    "Malatya": "Malatya İl Halk Kütüphanesi - Şehir merkezinde yer alan, geniş araştırma kaynakları ve rahat çalışma alanları sunan yerleşke.",
    "Tunceli": "Tunceli İl Halk Kütüphanesi - Munzur nehrinin esintisiyle serinleyen, sessiz çalışma ortamı ve güler yüzlü çalışanlarıyla butik kütüphane."
}

with open("enrich_visited_deep.py", "r", encoding="utf-8") as f:
    code = f.read()

for city, lib in LIBRARIES.items():
    target = f'    "{city}": {{'
    replacement = f'    "{city}": {{\n        "library": "{lib}",'
    if target in code and f'"library": "{lib}"' not in code:
        code = code.replace(target, replacement)
        print(f"Added library to {city}")

with open("enrich_visited_deep.py", "w", encoding="utf-8") as f:
    f.write(code)
