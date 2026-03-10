import os

VISITED_DEEP_DETAILS = {
    "Istanbul": {
        "hikmet": "İstanbul, iki denizin birleştiği gibi, Doğu'nun mistisizmi ile Batı'nın rasyonalizminin kucaklaştığı evrensel bir tapınaktır.",
        "quote": "\"İmparatorlukların doğup battığı, hem Roma'nın düzeninin hem de Sufi'nin aşkının yankılandığı yedi tepeli şehir.\"",
        "description": "Dünyanın gözbebeği, asırlık payitaht. Topraklarında barındırdığı sayısız medeniyetin iziyle ayakta duran bu kadim şehir, her sokağında farklı bir inancın ve felsefenin sırrını fısıldar. Ayasofya'nın kubbesinden süzülen ışıkta antik Hristiyan felsefesini, Galata'nın dar sokaklarında zamanın akışını, Mevlevihanede ise Mevlana'nın kozmik dönüşünü (sema) duyarsınız. Gündüzü telaşla geçerken, gecesi derin bir panteist sükunete erer.",
        "sufi_notes": "İstanbul'u layıkıyla gezmek, sadece taşını toprağını görmek değil, üzerine sinmiş felsefi tarihi hissetmektir. Tarihi yarımadada yürürken, stoacı Marcus Aurelius'un kabullenişini ve Yunus Emre'nin ilahi sevgisini aynı anda tefekkür etmektir.",
        "landmarks": ["Ayasofya", "Topkapı Sarayı", "Galata Kulesi", "Süleymaniye Camii", "Galata Mevlevihanesi"]
    },
    "Konya": {
        "hikmet": "Evren (Logos) daima hareket halindedir; dönen sadece derviş değil, tüm galaksilerdir.",
        "quote": "\"Felsefenin ve hoşgörünün harmanlandığı, antik bilgelik ile tasavvufi aşkın toprakla buluştuğu yer.\"",
        "description": "Hoşgörünün merkezi, bilgelerin yurdu. Çöllerin ortasında bir vaha gibi, entelektüel ve ruhani kuraklığı çeken zihinleri serinleten bir havzadır. Geçmişten fısıldanan evrensel sevgi, Taoist 'Akış' (Dao) felsefesiyle ve Rumi'nin ilahi aşkıyla birleşerek asırlardır bu şehrin sokaklarına yayılmıştır.",
        "sufi_notes": "Mevleviliğin 'sema' töreni, aslında antik atom teorisinde ya da evrenin kozmik dönüşünde görülen makro-mikro dengesinin estetik ve ruhani bir tezahürüdür (Logos ile Vahdet-i Vücud sentezi).",
        "landmarks": ["Mevlana Müzesi", "Şems-i Tebrizi Anıtı", "Karatay Medresesi", "İnce Minareli Medrese"]
    },
    "Bursa": {
        "hikmet": "Dağın (Uludağ/Olympos) zirvesindeki sessizlik, doğanın insana anlattığı en kadim felsefedir.",
        "quote": "\"İmparatorlukların doğuşuna tanıklık etmiş, hem antik tanrıların hem de ulu evliyaların gölgesini taşıyan topraklar.\"",
        "description": "Antik Çağ'da Keşiş Dağı (Olympos) olarak bilinen Uludağ'ın eteklerindeki asil şehir. Yeşil dokusu, panteist bir doğa anlayışına kucak açarken, ulu çınarların kökleri Osmanlı'nın kuruluş iradesini simgeler. Ulu Cami'deki sükunet, doğanın ve mimarinin insan ruhunu ne kadar yüceltebileceğinin mimari formudur.",
        "sufi_notes": "Bursa sokaklarında yürümek, doğanın döngüsel tarihine şahitlik etmektir. Su sesleriyle uyanıp rüzgara kulak vermek, insanın doğa ile (Tao) uyum içinde yaşamasının ne kadar zaruri olduğunu öğretir.",
        "landmarks": ["Ulu Cami", "Tarihi Çınar", "Yeşil Türbe", "Koza Han", "Muradiye Külliyesi"]
    },
    "Ankara": {
        "hikmet": "Zorluklar ve yıkımlar, küllerinden doğan rasyonel bir iradenin (Logos) habercisidir.",
        "quote": "\"Taşın ve toprağın, stoacı bir direnişle yepyeni bir ülkeye dönüştüğü o kararlı merkez.\"",
        "description": "Anadolu'nun kalbi, Friglerden, Romalılara ve sonrasında Cumhuriyet'e uzanan güçlü bir iradenin başkenti. Augustus Tapınağı'nın antik paganizmi ile Hacı Bayram-ı Veli'nin tasavvufi gölgesi yan yana durarak Anadolu'nun dinsel ve felsefi hoşgörüsünü özetler.",
        "sufi_notes": "Ankara, zorluklardan nasıl yeni bir başlangıç çıkarılabileceğinin yeryüzündeki kanıtıdır. Stoacı felsefenin 'Sana ne olduğu değil, senin ona nasıl tepki verdiğin önemlidir' görüşü, bu yorgun bozkırdan doğan milletin özeti gibidir.",
        "landmarks": ["Anıtkabir", "Ankara Kalesi", "Augustus Tapınağı", "Hacı Bayram Cami", "Anadolu Medeniyetleri Müzesi"]
    },
    "Amasya": {
        "hikmet": "Maddenin (Kayanın) direnci, insanın yaratıcı iradesi karşısında her zaman boyun eğer.",
        "quote": "\"Pontus krallarının izleri, Ferhat'ın dağı delen arzusu ve suyun sessiz zikriyle örülü vadi.\"",
        "description": "Elmanın, Ferhat ile Şirin'in, Strabon'un (Antik Coğrafyacı) memleketi. Yeşilırmak'ın aynasında farklı inançları izleyen kent. Amasya vadinin içine gizlenmiş, sırlarını hem antik kaya mezarlarıyla hem de Osmanlı mimarisiyle anlatan devasa bir felsefi tablodur.",
        "sufi_notes": "Amasya'da Ferhat'ın Şirin'e duyduğu aşk, insanın bir gaye uğruna maddesel dünyayı nasıl aşabileceğinin öyküsüdür. Pontus krallarının mezarları, gücün geçiciliğine (Memento Mori) dikkat çeker.",
        "landmarks": ["Kral Kaya Mezarları", "Amasya Kalesi", "II. Bayezid Külliyesi", "Yalıboyu Evleri"]
    },
    "Corum": {
        "hikmet": "Toprağın altındaki binlerce yıllık tabletler, zamanın (Kronos) her şeyi nasıl eşitlediğini gösterir.",
        "quote": "\"Tarihin en eski barış antlaşmalarının doğduğu, Hitit güneşinin kadim izlerini taşıyan il.\"",
        "description": "Hititlerin kadim diyarı, dünyanın ilk yazılı barış antlaşmasının ev sahibi. Hattuşaş'ın yıkıntıları arasında yürürken insan, çok tanrılı pagan inanışlarından, bugünün tektanrılı felsefelerine uzanan o uzun yolculuğu tefekkür eder. Güçlü krallıklar bile zamanın rüzgarında savrulmuştur.",
        "sufi_notes": "Bu şehir bize saltanatın geçici olduğunu, elde kalan tek şeyin kültür, barış ve insanlık mirası olduğunu fısıldar. Geçmişin Hitit tanrılarına yapılan ritüeller, bugün insanın kendi iç barışını (Nirvana/Mutmain) bulma çabasına evrilmiştir.",
        "landmarks": ["Hattuşaş Antik Kenti", "Alacahöyük", "Çorum Müzesi", "Şapinuva"]
    },
    "Samsun": {
        "hikmet": "Deniz ne kadar hırçınsa, kurtuluş fenerinin ışığı o kadar parlaktır.",
        "quote": "\"Amazon savaşçılarından, Milli Mücadele'nin ilk ateşine kadar hep direncin limanı olmuştur.\"",
        "description": "Tarih boyunca Amazon efsanelerinden bağımsızlık mücadelelerine kadar birçok kırılma noktasına şahitlik etmiş Karadeniz limanı. Hırçın dalgaların umuda dönüştüğü, eylemselliğin ve iradenin merkezidir.",
        "sufi_notes": "Hayatın zorluklarına karşı atılacak o 'ilk adım', varoluşçu (eksistansiyalist) bir sıçramadır. İnsanın kendi kaderini eline alması, Samsun'un dalgalı kıyılarından öğrenilebilir.",
        "landmarks": ["Onur Anıtı", "Bandırma Vapuru Müzesi", "Amisos Tepesi", "Amazon Köyü"]
    },
    "Sinop": {
        "hikmet": "Gölge etme, başka ihsan istemem. En büyük zenginlik, kendine yetebilmektir.",
        "quote": "\"Sinoplu Diyojen'in fıçısında bulduğu hakikatin, dalgaların hüznüyle buluştuğu sükunet şehri.\"",
        "description": "Antik çağın ünlü kinik filozofu Diyojen'in memleketi. Dünya malına ve hırslara sırt çevirip doğayla uyumu arayan bu felsefe, Sinop'un coğrafyasına sirayet etmiştir. Tarihi cezaevi, insanın fiziksel ve zihinsel esaretini sorgulatır.",
        "sufi_notes": "Tasavvuftaki 'terk' makamı ile Diyojen'in kinik felsefesi buralarda birbirine karışır. Cezaevinin soğuk duvarlarına bakıp, insanın kendi zihnine inşa ettiği görünmez hapishaneleri (Platon'un Mağarası) tefekkür etmek gerekir.",
        "landmarks": ["Tarihi Sinop Cezaevi", "Sinop Kalesi", "Hamsilos Tabiat Parkı", "Erfelek Şelaleleri", "Diyojen Heykeli"]
    },
    "Giresun": {
        "hikmet": "Ağaç (Doğa) meyve verdikçe dalını eğer; bilgelik de böyledir.",
        "quote": "\"Amazonlardan Altın Post efsanelerine, doğanın tüm zenginliklerini sunan Karadeniz yurdu.\"",
        "description": "Antik çağda Kerasus adıyla bilinen, Argonotların Altın Post'u ararken uğradığı efsanevi şehir. Mavi ile yeşilin kucaklaştığı bu nokta, mitolojinin ve doğa felsefesinin (Animizm) iç içe geçtiği bir nefes alanıdır.",
        "sufi_notes": "Çetin arazide gösterilen emek ve doğaya entegre yaşam, insanın evrenin sadece bir parçası olduğunu öğreten derin bir Şamanist/Doğa kökenli tefekkür sunar.",
        "landmarks": ["Giresun Kalesi", "Zeytinlik Semti", "Giresun Adası", "Kuzalan Şelalesi"]
    },
    "Ordu": {
        "hikmet": "Göğe uzanamayan, ufku ve bütünü kavrayamaz.",
        "quote": "\"Altın Post'un izinde, eşsiz koyların yemyeşil tepelerle buluştuğu yükseklerin sığınağı.\"",
        "description": "Antik dönem efsanelerinin ve Karadeniz'in tabiatla iç içe geçmiş modern yüzü. Yason Burnu, Argonotların efsanelerinde adından söz ettiren erken Hristiyanlığın ve pagan kültürün izlerini taşıyan evrensel bir duraktır.",
        "sufi_notes": "Boztepe'den uçsuz bucaksız denize bakmak, insanın yeryüzündeki yerini (makrokozmosta mikrokozmos) sorgulamasına sebep olur. Yason burnunda batan güneşi izlemek saf bir Nirvana/Vahdet anıdır.",
        "landmarks": ["Boztepe", "Yason Burnu", "Kurul Kalesi", "Perşembe Yaylası"]
    },
    "Kocaeli": {
        "hikmet": "Maddeye şekil veren emek, insanlığın ortak şuurunu inşa eder.",
        "quote": "\"Taşın terlediği, demirin şekil bulduğu, sanayinin ve üretimin başkenti.\"",
        "description": "Antik dönemde Nikomedia olarak bilinen ve bir zamanlar Roma'nın Doğu başkenti olan bu şehir, şimdilerde modern endüstrinin kalbi. Geçmişin ihtişamlı imparatorlukları yerini dev bacalara ve alın terine bırakmıştır.",
        "sufi_notes": "Kocaeli'de insan aklının sınırlarını ve doğayı dönüştürme potansiyelini (Homo Faber) görürüz. Üreten insanın teri, evrensel yaratım sürecinin dünyevi bir yansımasıdır.",
        "landmarks": ["İzmit Saat Kulesi", "Osman Hamdi Bey Evi", "Kartepe", "Sekapark"]
    },
    "Antalya": {
        "hikmet": "Zaman her taşı aşındırır, ama düşünce mermere kazınır ve yaşar.",
        "quote": "\"Lidyalılardan Romalılara, Selçuklulardan günümüze felsefeyi denizin mavisiyle harmanlayan diyar.\"",
        "description": "Akdeniz'in vitrini ve antik dünyanın en değerli liman ve yerleşim ağlarından (Likya) biri. Olympos'un hiç sönmeyen ateşi (Chimaera), insanın içindeki kutsal arayışın pagan bir yansıması gibidir. Romalı amfitiyatrolar, sanatın ve trajedinin beşiği olarak bize duygularımızı hatırlatır.",
        "sufi_notes": "Hadrian Kapısı'ndan geçerken, imparatorluk çökse de sanatın ve taşın hafızasının (Kolektif Bilinçdışı) kaldığını fark edersiniz. Akdeniz'in sonsuz mavisi, insana ruhani bir dinginlik (Ataraksiya) verir.",
        "landmarks": ["Kaleiçi", "Hadrian Kapısı", "Antalya Müzesi", "Olympos Antik Kenti", "Phaselis"]
    },
    "Denizli": {
        "hikmet": "Su taşa, sabır zihne şekil verir; gerçek güzellik doğanın yavaş işçiliğinde yatar.",
        "quote": "\"Apollon rahiplerinin şifa bulduğu, beyaz kayaların içinden sızan doğanın sanatı.\"",
        "description": "Hierapolis antik kentiyle iç içe geçmiş bembeyaz travertenlerin şehri. Antik çağlarda kutsal şifa ve kehanet merkezi olan bu bölge, Laodikeia'daki erken Hristiyan cemaatlerine de ev sahipliği yapmış, inanç sistemlerinin dönüşümüne tanıklık etmiştir.",
        "sufi_notes": "Termal suların kayaları beyaza boyaması gibi, gezgin de karşılaştığı inanç, kültür ve tecrübelerle kendi zihnini şekillendirir. Denizli, çok katmanlı felsefenin ve doğa tapınımının modern bir şahididir.",
        "landmarks": ["Pamukkale Travertenleri", "Hierapolis Antik Kenti", "Laodikeia", "Karahayıt Suları"]
    }
}

REGIONS_MAP = {
    "01_Marmara": ["Istanbul", "Kocaeli", "Bursa"],
    "02_Ege": ["Denizli"],
    "03_Akdeniz": ["Antalya"],
    "04_IcAnadolu": ["Ankara", "Konya"],
    "05_Karadeniz": ["Amasya", "Corum", "Samsun", "Sinop", "Giresun", "Ordu"]
}

def enrich_visited():
    for region, cities in REGIONS_MAP.items():
        if not os.path.exists(region):
            continue
        
        # Match exact folder names in the directory
        actual_folders = os.listdir(region)
        
        for folder in actual_folders:
            clean_city = folder.strip()
            # If standard ascii matching
            lookup_key = clean_city
            if clean_city == "İstanbul": lookup_key = "Istanbul"
            if clean_city == "Çorum": lookup_key = "Corum"
            
            if lookup_key in VISITED_DEEP_DETAILS:
                
                details = VISITED_DEEP_DETAILS[lookup_key]
                file_path = os.path.join(region, folder, "README.md")
                
                content = f"# 📍 {clean_city} - Evrensel Keşif ve Felsefe Notları\n\n"
                content += f"## 📜 Şehrin Kadim Hikmeti\n> \"{details['hikmet']}\"\n"
                content += f"> {details['quote']}\n\n"
                content += f"### 🌍 Şehrin Antik Ruhu ve Çok Kültürlü Dokusu\n{details['description']}\n\n"
                content += f"### 🕊️ Felsefi ve Bâtıni Notlar (Arkeolojik & Ruhani Perspektif)\n{details['sufi_notes']}\n\n"
                content += "### ✨ Tarihi, Antik ve Kutsal Duraklar\nArayıcının adımlaması ve ibret alması tavsiye edilen mukaddes ve tarihi mekanlar:\n"
                
                for loc in details['landmarks']:
                    content += f"- [ ] **{loc}**\n"
                    
                content += "\n---\n*Bu il bizzat evrensel bir arayıcı tarafından ziyaret edilmiş, tarihsel ve felsefi katmanları idrak edilmiştir.* ✅\n"
                
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"Deeply enriched: {file_path}")

if __name__ == "__main__":
    enrich_visited()
