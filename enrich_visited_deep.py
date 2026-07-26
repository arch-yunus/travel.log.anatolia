import os

VISITED_DEEP_DETAILS = {
    "Istanbul": {
        "library": "Şemsipaşa İlçe Halk Kütüphanesi (Üsküdar) - Denize sıfır konumuyla tefekküre değer, internet hızı yüksek, priz imkanı sınırlı ama atmosferi büyüleyici.",
        "hikmet": "İstanbul bir ayna gibidir; ona yüzünü dönen, zamanın ve tarihin kalbinde kendi yansımasını görür.",
        "quote": "\"İmparatorlukların ebediyete karıştığı, taşın ve denizin şiir yazdığı yedi tepeli masal.\"",
        "description": "Dünyanın gözbebeği, iki kıtayı birbirine diken asırlık payitaht. Topraklarında barındırdığı üç büyük imparatorluğun kültürel ve mimari nefesini her sokağında hissettiren bu kadim şehir, asla uyumayan devasa bir deryadır.\n\nAyasofya'nın kubbesinden süzülen solgun bir ışık, Galata'nın rutubetli taşlarına sinmiş anılar, Boğaz'ın hırçın rüzgarına karışan eski zaman fısıltıları... İstanbul, dar vakitlerde aceleyle 'gezilecek' değil; durup uzun uzadıya kulak verilecek, derin bir nefesle içe çekilecek, insanın kendi varoluşunu sorgulayabileceği uçsuz bucaksız bir romandır.\n\nYedi tepesine nakış gibi işlenmiş ulu camileri, yüzyılların hüznünü taşıyan surları, erguvan mevsiminde alev alev yanan Boğaz kıyıları ile İstanbul, başlı başına bir kainattır. Pierre Loti'den Haliç'e bakarken, ya da Üsküdar'da Kız Kulesi'ne karşı çay yudumlarken hissedilen o eşsiz bütünlük duygusu, başka hiçbir coğrafyada bulunmaz. Tarih, bu şehirde kitapların arasında değil, kaldırım taşlarının, cumbalı ahşap evlerin ve asırlık çınarların gölgesinde yaşamaya devam eder.",
        "sufi_notes": "İstanbul'un karmaşık sokaklarında kaybolmak, aslında kendini bulmanın, içindeki kaosu dindirmenin bir yoludur. Buradaki her yıkık dökük kalıntı, bize zamanın ne kadar hızlı aktığını ve insan ömrünün ne denli kısa olduğunu hatırlatırken; aynı zamanda yaşanmışlıkların, estetiğin ve inancın nesiller boyu kalplere nasıl dokunabildiğini gösterir.\n\nFatih'in fethindeki azim, Mimar Sinan'ın taşa üflediği ruh, Süleymaniye'nin avlusundaki sükunet... İstanbul, madde ile mananın en görkemli biçimde iç içe geçtiği yerdir. Boğaz'ın sularına vuran mehtap, insanın kendi karanlık köşelerine de ışık tutar; bu devasa kalabalığın içinde aslında herkesin ne kadar yalnız, ama en nihayetinde ne kadar büyük bir bütünün parçası olduğunu fısıldar.",
        "gastronomi": "- **Tarihi Süleymaniye Kurufasulyeci:** Çınar altında, bakır taslarda sunulan asırlık gelenek.\n- **Eminönü Balık Ekmek:** Boğaz esintisi ve martı sesleri eşliğinde hızlı ama unutulmaz bir klasik.\n- **Vefa Bozacısı:** Soğuk akşamlarda tarçın kokusuyla ısınan tarihi muhabbetler.",
        "landmarks": ["Ayasofya-i Kebir Cami-i Şerifi", "Topkapı Sarayı", "Galata Kulesi", "Süleymaniye Camii", "Yerebatan Sarnıcı", "Kapalıçarşı", "Sultanahmet Meydanı", "Eyüp Sultan Türbesi"]
    },
    "Konya": {
        "library": "Konya İl Halk Kütüphanesi - Geniş ve ferah salonları var, Selçuklu mimarisinin esintilerini taşıyor, çalışma disiplini yüksek.",
        "hikmet": "Susuzluktan kuruyan bozkırı yeşerten yağmur değil, gönülden kopan sevginin ve hoşgörünün pınarıdır.",
        "quote": "\"Rüzgârın en hafif estiği, sarı buğday başakları arasında evrensel sükunetin demlendiği Selçuklu diyarı.\"",
        "description": "Çöllerin ve uçsuz bucaksız ovaların ortasında bir vaha gibi duran, yalnızlığın ve dinginliğin başkenti. Dışarıdan bakıldığında sessiz, sert ve kurak görünen bu bozkır, içine girildiğinde eşsiz bir hoşgörü, tasavvuf ve estetik barındırır.\n\nMevlana'nın yüzyılları aşan 'Ne olursan ol gel' çağrısının yankılandığı sokaklarında gezinirken, sarının ve toprağın her tonu güneşte parlar. Konya, insanın dış dünyadaki karmaşayı geride bırakıp içselliğine uzandığı mistik bir kervansaraydır.\n\nAlaeddin Tepesi'ndeki ulu ağaçların dibinde Selçuklu sancağının ihtişamını, Karatay Medresesi'nin yıldızlı çinilerinde evrenin sonsuzluğunu hissedersiniz. Sille'nin kireç badanalı dar sokakları ve zamana direnen kiliseleri, bu topraklardaki çok kültürlü hoşgörünün ve derin sevginin taşa kazınmış en zarif halidir.",
        "sufi_notes": "Konya'da bozkır rüzgârını dinlemek, insanın kendi gürültüsünden kaçıp sükunetini bulması gibidir. Burada göğe uzanan sadece yeşil çinili minareler değil; sevgiyle, estetikle ve tevazuyla yükselen ulu bir düşünce sisteminin kökleridir. Her semazen dönüşünde kainatın sırrını fısıldar.\n\nİnsan, Mevlana türbesinin loş ve mistik atmosferinde durduğunda, 'hiç' olmanın aslında 'hep' olmak demek olduğunu, makamın ve kibrin eriyip bir damla gözyaşına dönüştüğünü idrak eder. Bozkırın kuraklığı, aslında içimizdeki sönmeyen ilahi aşk ateşinin yanabilmesi için hazırlanmış manevi bir fırın gibidir.",
        "gastronomi": "- **Etliekmek:** İnce hamur, ustalık ve odun ateşinin harika buluşması (özellikle Havzan veya Meram bölgesinde).\n- **Fırın Kebabı:** Saatlerce bakır tepsilerde ağır ağır pişen Selçuklu mirası et yemeği.\n- **Bamya Çorbası:** Düğünlerin ve özel günlerin ekşi-tatlı eşsiz başlangıcı.",
        "landmarks": ["Mevlana Müzesi", "Alaeddin Tepesi", "Karatay Medresesi", "Sille Köyü", "Kelebekler Vadisi", "İnce Minareli Medrese"]
    },
    "Bursa": {
        "library": "Bursa İl Halk Kütüphanesi - Sakin ve geniş çalışma alanları mevcut, araştırma kaynakları zengin, bahçesi mola için ideal.",
        "hikmet": "Dağın yüceliği sadece zirvesindeki karlardan değil, eteklerindeki çınarlara verdiği can suyundan gelir.",
        "quote": "\"Suyun sesine karışan ulu çınar yapraklarının, bir imparatorluğun doğuşuna beşiklik ettiği yeşil başkent.\"",
        "description": "Uludağ'ın eteklerine şefkatle yaslanmış, yeşiliyle ve suyuyla her nefeste hayat bulan asil Osmanlı şehri. Her köşebaşındaki tarihi bir şadırvandan su sesi gelir; dar sokaklarında ahşap ve taşlarla ilmek ilmek işlenmiş, asırlara meydan okuyan bir sükunet vardır.\n\nBursa, doğa ile insanın, yeşil ile mimarinin en zarif şekilde uyumlandığı kadim bir huzur yuvasıdır. Hanlar bölgesindeki çay molaları, zamanın burada daha yavaş aktığının en büyük kanıtıdır.\n\nUlu Cami'nin o bitimsiz, iç içe geçmiş yirmi kubbesi altında duyulan yankı, Yeşil Türbe'nin sır kaplı çinilerindeki ince işçilik ve Kozahan'da ipek tezgâhlarından yükselen o kadim şıkırtılar... Bursa, sadece eski bir başkent değil, toprağın suyla, sanatın inançla buluşup mayalandığı, ruhu hiçbir zaman eskimemiş yeşil bir cennettir.",
        "sufi_notes": "Tarihi İnkaya çınarının altında kök salmak ve göğe yükselmek üzerine düşünmek, insana sabrın gücünü öğretir. Bursa, ne kadar büyürse büyüsün, o ilk toprağa düşen Osman Gazi tohumunun tevazusunu hep koruması gerektiğini sessizce anlatır.\n\nUlu Cami'nin şadırvanından dökülen her damla su, insanın kendi günahlarından ve kibrinden arınması, berraklaşması için yapılmış bir çağrıdır. Emir Sultan'ın tepesinden şehre bakıldığında, hayatın ne kadar da gelip geçici, dünyevi telaşların ne kadar beyhude olduğu bir kez daha, suyun ve yeşilin fısıltısıyla ruhun en derinliklerine kazınır.",
        "gastronomi": "- **Tarihi İskender Kebap:** Pide, tereyağı, enfes döner ve salçanın 1800'lerden gelen büyük buluşması.\n- **Pideli Köfte:** Kayhan çarşısında esnafın en sevdiği, iskenderin mütevazı ama bir o kadar lezzetli kardeşi.\n- **Tahinli Pide:** Sabahın erken saatlerinde fırından yeni çıkmış, çayın en büyük yoldaşı.",
        "landmarks": ["Ulu Cami", "Tarihi İnkaya Çınarı", "Yeşil Türbe", "Koza Han", "Cumalıkızık", "Tophane", "Osman Gazi ve Orhan Gazi Türbeleri"]
    },
    "Ankara": {
        "library": "Milli Kütüphane (Bahçelievler) - Türkiye'nin en büyük araştırma kütüphanesi, 24 saat açık salonları, sınırsız kaynak ve üst düzey çalışma disiplini ile kod yazmak için eşsiz bir mabet.",
        "hikmet": "Taşa ve yokluğa karşı dikilen bir Cumhuriyet iradesi, dünyadaki en güçlü çelikten daha aşılmazdır.",
        "quote": "\"Yorgun bir bozkırda imkansızın nasıl başarıldığını haykıran, vakur, kararlı ve devrimci başkent.\"",
        "description": "Anadolu'nun kalbi, Friglerden Cumhuriyetin kuruluş yıllarına kadar uzanan, daima ayakta kalmanın direncini simgeleyen şehir. Güçlü ayazı insanın tenini sıyırsa da, sokaklarındaki ciddiyet ve kararlılık devletin ve milletin ruhunu ateşler.\n\nAnkara, görkemli sarayların veya boğaz parıltısının değil; emeğin, kararlılığın, diplomasinin ve 'kendi küllerinden doğma' inancının merkezidir. Ulus meydanındaki her kaldırım taşı Cumhuriyetin ilk adımlarını şahididir.\n\nAnıtkabir'in aslanlı yolundan yürürken hissedilen o devasa ağırlık ve minnet duygusu, Kurtuluş Savaşı müzesindeki yırtık çarıklara bakınca boğaza düğümlenen o hüzünlü saygı... Ankara, pes etmemenin, küllerinden bir Anka kuşu gibi yeniden doğmanın adıdır. Eymir'in sonbahar yapraklarında dahi bu şehrin o vakur ve ketum melankolisinden bir parça bulabilirsiniz.",
        "sufi_notes": "Ankara bize en büyük zorluklara karşı dik durmayı öğretir. Hiçbir şeyin altın tepside sunulmadığı, aksine tırnaklarla kazınarak kazanıldığı bu topraklarda atılan her sağlam temel, inancın imkansızlıkları nasıl yarıp geçtiğine dair bir belgeseldir.\n\nBu gri şehir insana gösterişin ve ihtişamın aslında çok ucuz, ancak çalışmanın, liyakatin ve çabanın paha biçilemez olduğunu hissettirir. Sade bir memur şehrinin ardında yatan o güçlü karakter, inancın her türlü yokluğu ve sarı bozkırı nasıl aydınlık bir geleceğe ve yemyeşil umutlara çevirebileceğinin en somut manevi şahididir.",
        "gastronomi": "- **Ankara Simidi:** Pekmezi bol, dışı çıtır, içi tel tel dökülen vazgeçilmez sabah lezzeti.\n- **Ankara Tava:** Arpa şehriye ve ağır ateşte pişmiş kuzu etinin doyurucu senfonisi.\n- **Beypazarı Kurusu:** Çay masalarının aylarca bayatlamayan, tarçın kokulu yoldaşı.",
        "landmarks": ["Anıtkabir", "Ankara Kalesi", "Anadolu Medeniyetleri Müzesi", "I. ve II. Meclis Binaları", "Atakule", "Eymir Gölü", "Hamamönü"]
    },
    "Amasya": {
        "library": "Amasya İl Halk Kütüphanesi - Yeşilırmak kıyısında, nehrin şırıltısı eşliğinde kod yazma deneyimi sunan eşsiz bir çalışma alanı.",
        "hikmet": "Kayaya kazınan en büyük iz kralların gücü değil, vadiden usulca akan suların getirdiği yaşamdır.",
        "quote": "\"Nehrin ikiye böldüğü, Ferhat'ın gölgesiyle dağların şarkısının rüzgarda birbirine karıştığı elma kokulu vadi.\"",
        "description": "Yeşilırmak'ın nazlı nazlı aktığı dar ve sarp bir vadiye gizlenmiş masal şehri. Nehrin iki yakasını süsleyen ince işçilikli yalıboyu evleri, onların üstüne heybetle yükselen hırçın kayalar ve bu kayalara kazınmış iki bin yıllık Pontus antik Kral Kaya mezarları...\n\nAmasya, nehrin ritmiyle tarihin donup kaldığı bir seyir terasıdır. Şehzadelerin devlet yönetmeyi öğrendikleri bu topraklar, küçük yüzölçümüne rağmen kültürel olarak bir imparatorluk büyüklüğündedir.\n\nHarşena Dağı'nın eteklerine serpiştirilmiş medreseler, köprüler ve camiler, sanki nehirle bir uyum anlaşması imzalamış gibidir. Geceleri Yeşilırmak'ın üzerine düşen o yumuşak yalı ışıkları, şehri adeta altın tozu serpilmiş efsunlu bir Ortaçağ masalına çevirir.",
        "sufi_notes": "Bir dağın sinesine kibre kapılarak kazınmış o kocaman kral mezarları bile zamanın karşısında ufalanır; fakat o mütevazı görünümlü ırmak asırlardır hep aynı türküyü söyler. Amasya insana kalıcı olanın güç değil, doğanın akışına uyum sağlamak olduğunu öğretir.\n\nFerhat'ın Şirin için dağları deldiği bu sarp kayalıklar, mecazi aşkın nasıl ilahi bir gayrete ve sebatkarlığa dönüşebileceğini anlatır. Vadinin dar ve basık yapısı aslında bir sığınak gibi insanı dünyanın şerrinden uzaklaştırıp, kendi kalbinin en korunaklı köşesinde tefekküre daldırır.",
        "gastronomi": "- **Amasya Çöreği:** Haşhaş ve cevizin odun ateşinde buluştuğu efsane lezzet.\n- **Keşkek:** Özel günlerin ve bayramların büyük bakır kazanlarda dövülerek yapılan baştacı yemeği.\n- **Misket Elması:** Sulu, kokulu ve şehrin simgesi olan enfes meyve.",
        "landmarks": ["Kral Kaya Mezarları", "Amasya Kalesi", "Amasya Yalıboyu Evleri", "Hazeranlar Konağı", "Ferhat ile Şirin Aşıklar Müzesi", "II. Bayezid Külliyesi", "Sabuncuoğlu Şerefeddin Tıp Müzesi"]
    },
    "Corum": {
        "library": "Çorum İl Halk Kütüphanesi - Sessiz ve düzenli çalışma odalarıyla odaklanmayı kolaylaştıran sakin bir Anadolu kütüphanesi.",
        "hikmet": "Medeniyetler kılıçla veya kanla kurulsa da, yalnızca masaya barışın mührü basıldığında yarına kalır.",
        "quote": "\"Çivi yazılı taş tabletlerin arasında yankılanan ilk barışın, bereketli topraklardaki unutulmaz izi.\"",
        "description": "Hititlerin kadim güneşi altında yıkanan, bereketin, tarihin ve Anadolu uygarlıklarının beşiği. Çorum, gösterişten uzak tepelerinde binlerce yıllık bir imparatorluk mirasını saklar.\n\nHattuşaş'ın yıkıntıları arasında, Aslanlı Kapı'dan içeri doğru yürürken duyulan tek ses, toprağın ve rüzgarın binlerce yıllık şahitliğinin ninnisine benzer. Şehir, leblebicilerinin burna dolan o güzel kavrulmuş kokusu ile samimi, mütevazı ama derin bir karakter sergiler.\n\nAlacahöyük'te bulunan Sfenksli Kapı ve kral mezarlarından çıkarılan güneş kursları, insanoğlunun tunç çağındaki o olağanüstü sanat yeteneğine hayran bırakır. Çorum, gösterişsiz bozkır örtüsünün altında, antik dünyanın en büyük askeri ve diplomatik dehalarından birinin izlerini gururla taşır.",
        "sufi_notes": "Krallar unutulup gider, aşılamaz denen devasa surlar yıkılır. Ancak insanlık tarihine düşülen 'Kadeş Barış Antlaşması' notu sonsuza kadar toprağın hafızasında kalır. Gücün ardındaki asıl zarafet ve barışın kıymeti, bu bozkır harabelerinde yatar.\n\nZamanın acımasız dişlileri arasında kaybolmamak için taşa kazınan o hiyeroglifler bile yavaş yavaş silinir. Çorum'un sessiz harabeleri bize, dünyada bıraktığımız en kalıcı izin taş binalar değil, kalplere ektiğimiz sevgi, dürüstlük ve erdem tohumları olduğunu hatırlatır.",
        "gastronomi": "- **Taze Kavrulmuş Çorum Leblebisi:** Sokakları saran sıcacık, odun ateşi tadında nohutun sanata dönüşmüş hali.\n- **İskilip Dolması:** Ağzı mühürlenmiş kazanlarda saatlerce pişen destansı ziyafet yemeği.\n- **Kuru Mantı:** Genellikle fırınlanıp kurutularak saklanan ve kışın yoğurtla şölene dönüşen lezzet.",
        "landmarks": ["Hattuşaş Antik Kenti (Boğazkale)", "Alacahöyük", "Çorum Müzesi", "Yazılıkaya Açık Hava Tapınağı", "Şapinuva", "Saat Kulesi"]
    },
    "Samsun": {
        "library": "Samsun İl Halk Kütüphanesi - Karadeniz'in en modern kütüphanelerinden biri, priz ve internet altyapısı mükemmel.",
        "hikmet": "En hırçın fırtınalarda uyanan irade, coşkulu dalgaları uysallaştıran ve rotayı çizen tek pusuladır.",
        "quote": "\"Kurtuluşa atılan o tarifsiz ilk sağlam adımın, denizin tuzuna karışıp bir milleti dirilttiği özgürlük limanı.\"",
        "description": "Karadeniz'in deli dalgalarına karşı hep bir fener gibi aydınlık ve dik durmuş umudun şehri. Dağlardan denize doğru uzanan yemyeşil tepelerin ve hırçın Karadeniz sahilinin tam ortasında, medeniyet ve doğanın büyük kucaklaşmasıdır.\n\nAtatürk'ün Bandırma Vapuru ile ufukta göründüğü o tarihi anın ruhunu tütünde, denizde ve rüzgarda her an hissedebilirsiniz. Karadeniz'in en modern şehirlerinden biri olarak ticareti, tarihi ve gençliği aynı sokaklarda barındırır.\n\nKızılırmak ve Yeşilırmak'ın denize kavuştuğu devasa deltalarındaki kuş cennetleri, Amazon savaşçılarının efsunlu tepeleri ve bağımsızlık meşalesinin yandığı tütün kokulu iskeleleri ile Samsun, Karadeniz'in göz ardı edilemez başkenti rolünü üstlenir.",
        "sufi_notes": "Bazen pasif kalıp beklemek değil, tam aksine dalgaların üzerine doğru inançla o 'ilk adımı' atmak gerekir. Hayattaki tüm korkular, umutsuzluklar ve engeller, insanın karar verip Bandırma misali yola çıkmasıyla küçülmeye başlar.\n\nZorlu koşulların, bitmek bilmeyen fırtınaların ve imkansızlıkların ortasında zafere ulaşmanın anahtarı silahlarda değil, tam kalpteki sarsılmaz inanctatır. Bu topraklara atılan her bir adım, sabrın, cesaretin ve vazgeçmeyişin ruha attığı büyük ebediyet tohumlarıdır.",
        "gastronomi": "- **Bafra Pidesi:** İncecik, kapalı hamurun içinde bol tereyağı ile harmanlanmış kıymalı şaheser.\n- **Terme Pidesi:** Daha yumuşak, açık ve sucuk/kaşar varyasyonlarıyla zengin lezzet.\n- **Çakallı Menemeni:** Suyunu çektirip peynirle karamelleşen, ekmek bandırmalık efsanevi yol üstü kahvaltısı.",
        "landmarks": ["Onur Anıtı (Atatürk Heykeli)", "Bandırma Vapuru ve Milli Mücadele Parkı", "Amisos Tepesi", "Amazon Köyü", "Kurtuluş Yolu", "Kızılırmak Deltası Kuş Cenneti"]
    },
    "Sinop": {
        "library": "Sinop Rıza Nur İl Halk Kütüphanesi - Tarihi ve nostaljik ahşap binasıyla zamanda yolculuk hissi veriyor, huzurlu bir çalışma noktası.",
        "hikmet": "En karanlık zindan kalın dört duvar arası ve demir parmaklıklar değil, insanın kendi kafasında ördüğü sınırlardır.",
        "quote": "\"Hırçın Karadeniz ile huzurlu limanın buluştuğu, deniz kokulu yalnızlığıyla baş başa kalan filozof yarımada.\"",
        "description": "Gölgelerin, sükunetin ve en kuzeyin şehri. Anadolu'nun denize bir mızrak ucu gibi uzanan en uç noktası. Dalgaların yüzlerce yıllık kale duvarlarını dövdüğü, ormanın adeta denize döküldüğü ve insanın doğayla baş başa kaldığı efsanevi bir liman!\n\nDar sokaklarında deniz kokusu evlerin pencerelerinden içeri dolar. Hem inziva köşesi arayan bir bilge kadar huzurlu, hem de asırlık tarihi cezaevinin ürpertici havasını taşıyan acılı bir hafıza mekanıdır. Diogenes'in fenerle gündüz vakti insan aradığı bu topraklar, tefekkürün tam merkezidir.\n\nErfelek şelalelerinde ormanın içlerine doğru suyun peşinden giderken hissettiğiniz o gizem, İnceburun'un o rüzgarlı kayalıklarında yerini hudutsuz bir Sonsuzluk hissine bırakır. Sinop, coğrafyanın kader, doğanın ise bir öğretmen olduğunun en net tablosudur.",
        "sufi_notes": "Tarihi cezaevinin nemli, ürpertici havası ve soğuk duvarları bize dışarıdaki özgürlüğün, bir nefes almanın değerini hatırlatırken; duvarın hemen dibindeki uçsuz bucaksız deniz, insanın kalbindeki sınır tanımaz umudu ve sonsuzluk tutkusunu temsil eder.\n\nDüşünceleri, duyguları yahut bedeni hapsedeceklerini sananların, insanın ruhundaki o uçsuz bucaksız maviliği asla demir parmaklıklar ardına koyamayacağı bu şehirde daha iyi anlaşılır. Fırtına ne kadar sert eserse essin, dalgalar ne kadar yükselirse yükselsin, içimizdeki sükunet limanı hep oradadır.",
        "gastronomi": "- **Sinop Mantısı (Cevizli Mantı):** Yarısı yoğurtlu, yarısı bol cevizli olarak sunulan sıradışı bir hamur işi vizyonu.\n- **Nokul:** Üzümlü ve cevizli, çay saatlerinin başrol oyuncusu, kıyır kıyır bir yöresel börek/çörek.\n- **Taze Karadeniz Balıkları:** Özellikle kış aylarında İnceburun açıklarından tutulan hamsi ve istavrit.",
        "landmarks": ["Tarihi Sinop Cezaevi", "Sinop Kalesi", "Hamsilos Tabiat Parkı", "Erfelek Tatlıca Şelaleleri", "İnceburun Deniz Feneri", "Diyojen Heykeli"]
    },
    "Giresun": {
        "library": "Giresun İl Halk Kütüphanesi - Harşit Vadisi esintileriyle serin, sakin çalışma masaları mevcut.",
        "hikmet": "Karadeniz'in dalgalarının dövdüğü kayalar ne kadar sarp ise, zorluklarla bezenmiş o dalların verdiği fındıklar o kadar tatlıdır.",
        "quote": "\"Yeşilin en koyusunun, denizin en mavisinin ve zorlu yamaçlardaki emeğin sonsuz bir memleket hasretiyle kucaklaştığı yer.\"",
        "description": "Ormanın denize paralel bir sükunet ve inatla uzandığı, sislerin ardında gizli kalmış muazzam tabiat. Yaylalarındaki serin rüzgarlar insanın kalbine yaşama sevinci pompalarken, o sarp yamaçlarda yeşeren doğa insan emeğinin en dürüst karşılığını sunar.\n\nSadece adasındaki Amazon efsaneleri değil, yaylarındaki uçsuz bucaksız yeşil dalgalar da Giresun'u Karadeniz'in en otantik ve dokusu bozulmamış incilerinden biri yapar.\n\nKuzalan Şelalesi'nin o efsunlu, mistik turkuaz rengi suları ve Kümbet yaylasının o oksijen deposu çam ormanları arasında insan, şehir hayatının ne kadar sentetik, doğanın ise ne kadar hakiki ve anaç olduğunu hisseder. Giresun'da zaman, çay bahçelerinden denize inen dik patikalarda asuman bir huzurla ağır ağır akar.",
        "sufi_notes": "Doğadaki her türlü zorluk ve ulaşılamazlık, sabır ve emekle yoğrulduğunda en tatlı meyvelerini (örneğin fındığı) cömertçe sunar. İnsan doğanın bu inatçı ama verimli karakterine bakıp kendi içindeki çetin mücadelelerin de eninde sonunda çiçek açacağını idrak edebilir.\n\nGiresun Adasındaki o suskun Amazon yıkıntıları ve Karadeniz'in hırçın esintisi, bir zamanların en yenilmez komutanlarının bile nasıl doğanın döngüsü içinde silinip gittiğini, elimizde kalanın sadece tabiata olan saygı ve yeryüzüne bıraktığımız iyilikler olduğunu kulağımıza fısıldar.",
        "gastronomi": "- **Giresun Kalite Fındık:** Dünyanın en iyi, en yağlı ve lezzetli tombul fındığı.\n- **Pancarlı Karalahana Çorbası:** Karalahana, mısır yarması ve fasulyenin oluşturduğu tam bir şifa deposu.\n- **Görele Pidesi:** Özel hamuru ve mis gibi köy tereyağıyla taçlandırılmış çıtır Karadeniz pidesi.",
        "landmarks": ["Giresun Kalesi", "Kuzalan Şelalesi", "Mavi Göl", "Giresun Adası (Aretias)", "Kümbet Yaylası", "Sis Dağı"]
    },
    "Ordu": {
        "library": "Ordu İl Halk Kütüphanesi - Teleferik hattına yakın konumuyla mola vermeye uygun, çalışma salonları geniş.",
        "hikmet": "Göğe ne kadar yükselir ve aşağıya kibirle değil de şefkatle bakarsan, önündeki yollar ve denizler o kadar aydınlanır.",
        "quote": "\"Bulutların üzerine kurulan tahtından, Karadeniz'in ince dantel gibi örülmüş muazzam kıyılarını izleyen zarif şehir.\"",
        "description": "Boztepe'ye çıkıp teleferikten bakıldığında, ayağınızın altında uzanan o muazzam yeşil ve mavi uçurumun şehri. Yaylalarının (Perşembe, Çambaşı) uçsuz bucaksız sisli tepeleri, mendereslerin muazzam kıvrımları ve kıyıların eşsiz sükuneti birleşir.\n\nBurası, insanın metropol gürültüsünden kaçıp kafa dinlemek için haritadan gözü kapalı seçeceği, doğanın merhametli kollarında kurulu, Karadeniz'in en nazlı çocuklarından biridir.\n\nYason Burnu'nda güneşi batırırken Argonotların altın post efsanesini iliklerinize kadar hissedersiniz. Kurul Kalesi'nde Kibele heykeline dokunup, Karadeniz'in sadece deniz ve orman değil, aynı zamanda çok köklü bir antik miras barındırdığına şahit olursunuz. Ordu, modern bir sahil şehri ile antik bir dağ köyünün birleşim noktasıdır.",
        "sufi_notes": "Yüksek bir tepeden o uçsuz bucaksız denize ve ucu bucağı görünmeyen ormanlara bakmak; insanın evrenin ne kadar devasa, kendisinin ve dertlerinin ise ne kadar narin bir zerreden ibaret olduğunu anlaması için ruhsal bir aynadır.\n\nPerşembe yaylasının o bitmek tükenmek bilmeyen kıvrımlı menderesleri, hayat yolculuğumuzun aslında hiçbir zaman dümdüz olmadığını, engeller ve virajlarla dolup taştığını, fakat tüm o kıvrımlara rağmen suyun eninde sonunda denize varacağını öğretir.",
        "gastronomi": "- **Ordu Tostu:** İki kalın ekmek dilimi arasına konulan özel sucuk ezmesinin preslenmesiyle yapılan kült sokak lezzeti.\n- **Yalıköy Köftesi:** Baharatsız, sadece etin kendi muazzam lezzetiyle şekillendirilen Karadeniz köftesi.\n- **Melocan (Diken Ucu) Kavurması:** Doğadan toplanan narin bitkilerin yöresel bir kavurmayla şölene dönüşmesi.",
        "landmarks": ["Boztepe ve Teleferik", "Yason Burnu ve Kilisesi", "Perşembe Yaylası (Menderesler)", "Kurul Kalesi", "Gölköy Ulugöl"]
    },
    "Kocaeli": {
        "library": "Kocaeli İl Halk Kütüphanesi - Modern iç tasarımı ve güçlü internet altyapısıyla kodlama mesaileri için son derece konforlu.",
        "hikmet": "Emeğin teriyle işlediği demir pas tutmaz; yorgunluk, yeni bir inşanın umut kıvılcımıdır.",
        "quote": "\"Fabrika bacalarından tüten isli umutlarla, bitinya krallığından kalma mirasın beraber yeşerdiği üretim diyarı.\"",
        "description": "Denizin kıyısında, körfez köprülerinin ağzında, demirin, plastiğin ve ateşin şekillendiği Türkiye'nin devasa endüstri başkenti. Dışarıdan veya otobandan bakıldığında sadece sanayi bacaları ve duman görünse de, şehrin biraz içine sızınca Kartepe'nin karlarına ve Kandıra'nın yemyeşil koylarına ulaşırsınız.\n\nKocaeli, gece gündüz uyumayan bir üretim arzusuyla, dağların arkasındaki gizli doğanın sürekli bir mücadele ve denge içinde yaşadığı, dinamik bir şehirdir.\n\nEskihisar sahilinden Yalova'ya doğru uzanan vapur rotasında martılara simit atarken, bir tarafınızda Osman Hamdi Bey'in Kaplumbağa Terbiyecisi'ni çizdiği tarihi konağı, diğer tarafınızda yüzlerce metre boyunda devasa lojistik gemilerini görürsünüz. Bu şehir, sanayi ile kültürün, beton ile doğanın o garip, bitirim ve eşsiz sarmalıdır.",
        "sufi_notes": "Çarkların, çekiçlerin ve koca fabrikaların geceyi aydınlatan ateşli sesi, aslında insan aklının, hayatta kalma refleksinin ve emeğinin birer senfonisidir. Hiçbir şey durduk yere şekillenmez; demir bile işe yaramak için önce ateşe sabırla dayanmalıdır.\n\nBu isli ve dumanlı fabrikaların gölgesinde bile insanın umuda olan inancından hiçbir şey kaybetmemesi, üretmenin ve alın terinin ne kadar kutsal bir arınma yöntemi olduğunu anlatır. Tüketimin çılgınlığına karşı, Kocaeli usulca 'gerçek zafer, bir şeyler üretebildiğinde başlar' mesajını verir.",
        "gastronomi": "- **Pişmaniye:** Çekildikçe incelen, ustalık isteyen ve damakta eriyen tatlı tel tel Kar demeti.\n- **Değirmendere Fındığı / Yarımca Kirazı:** Endüstrinin tam kalbinden fışkıran yöresel doğa mucizeleri.\n- **Kandıra Yoğurdu:** Manda sütünden yapılan, bıçakla kesilebilecek kadar kıvamlı ve doğal yoğurt.",
        "landmarks": ["Sekapark (Eski Kağıt Fabrikası Dönüşümü)", "Kartepe Kayak Merkezi", "İzmit Tarihi Saat Kulesi", "Osman Hamdi Bey Evi (Eskihisar)", "Kefken ve Kerpe Kayalıkları", "Ormanya Doğal Yaşam Parkı"]
    },
    "Antalya": {
        "library": "Antalya İl Halk Kütüphanesi - Yeşillikler içindeki bahçesi ve geniş okuma salonlarıyla Akdeniz sıcağında serin bir çalışma limanı.",
        "hikmet": "Sonsuz maviliğin ufku, geçmişi derinliklerinde hatırlar ancak daima doğacak yeni güne daha büyük umutla bakar.",
        "quote": "\"Kayalıklarına gürültüyle çarpıp geri çekilen suların, asırların mirasını şefkatle yıkadığı sıcak Akdeniz cenneti.\"",
        "description": "Akdeniz'in şüphesiz vitrini; güneşi, Likya ve Pamfilya antik kentlerini ve turkuaz doğayı cömertçe kucaklayan o sıcak coğrafya. Bir yanda Torosların kar kaplı heybeti dururken, diğer yanda insanın ruhunu yatıştıran engin mavi plajlar uzanır.\n\nKaleiçi'nin begonvillerle süslenmiş, dar ve nostaljik sokaklarında yürürken, antik krallıkların ayak seslerini ve yorgun kalyoncuların kalkanlara vuran mızrak seslerini bir film şeridi gibi hissedersiniz.\n\nAspendos'un o muazzam akustiğinde binlerce yıl önceki trajedilerin yankılandığını hayal edebilir, Kurşunlu ve Düden şelalelerinin ferahlığında cehennem sıcağından bir vaha serinliğine kaçabilirsiniz. Antalya sadece bir yaz rotası değil, derinlere inen kanyonları ve sedir ormanlarıyla başlı başına bir yaşam felsefesi mekanıdır.",
        "sufi_notes": "Güneyin bu kızgın Akdeniz güneşi ve şifalı tatlı-tuzlu suyu, bedeni yorarken zihni tazeler. Karşınıza çıkan her amfi tiyatro ve kalıntı, geçmiş zamanın dünya telaşının ne denli boş olduğunu, asıl gerçeğin o anı en güzel şekilde yaşamak olduğunu fısıldar.\n\nTorosların zirvelerinden Akdeniz'e karışan o coşkulu sular, aslında ruhun en yüksek zirvelerinden koptuktan sonra bedenin denizinde kayboluşunu ve en nihayetinde kaynağa, yani büyük sonsuzluğa geri dönüşünü simgeler.",
        "gastronomi": "- **Piyaz (Antalya Usulü):** Tahinli, sirkeli sosuyla alışılagelmiş piyazları unutturan, kendi başına harika bir öğün.\n- **Hibeş:** Tahin, sarımsak, limon ve baharatların harmanından doğan muazzam yerel meze.\n- **Yanık Dondurma (Keçi Sütlü):** İsli, yanık kokulu ve sakızlı eşsiz bir serinletici.",
        "landmarks": ["Tarihi Kaleiçi ve Yivli Minare", "Hadrian Kapısı (Üç Kapılar)", "Olympos ve Phaselis Antik Kentleri", "Düden ve Kurşunlu Şelaleleri", "Aspendos Antik Tiyatrosu", "Termessos Antik Kenti"]
    },
    "Denizli": {
        "library": "Denizli İl Halk Kütüphanesi - Şehir merkezinde, sessiz çalışma salonları geniş, öğleden sonra kalabalık olabiliyor.",
        "hikmet": "Sabırla süzülen küçük ısrarlı su damlaları, asırlar içinde en sert ve karanlık kayaları bile bembeyaz bir pamuk tarlasına döndürür.",
        "quote": "\"Yeraltından fokurdayarak fışkıran sıcağın sanata, antik zamanların ve gladyatörlerin ise derin bir sessizliğe dönüştüğü o eşsiz coğrafya.\"",
        "description": "Uzaktan pamuk tarlaları gibi görünen travertenlerin bembeyaz şefkati ve hemen yanı başındaki Hierapolis'in büyüleyici, devasa lahit kalıntıları. Toprağın altında kaynayan ve efsanelere konu olan şifalı sular, yeryüzüne çıktığında muazzam bir doğa heykeli inşa eder.\n\nDenizli, tekstilin, dokumanın ve tabiatın en zarif işçiliğini birleştirerek yeryüzü tuvalinde sergilediği inanılmaz bir sanat atölyesi gibidir.\n\nLaodikeia'da gezinirken İncil'de geçen yedi kiliseden birinde durduğunuzu farz ederken, antik havuzun içinde gladyatör sutunlarına dokunarak yüzmenin o olağanüstü mitolojik aurasına kapılabilirsiniz. Dokuma tezgahlarının o ritmik 'tık tık' sesleri, ezelden beri süre gelen bir bereketin kalp atışı gibidir.",
        "sufi_notes": "Travertenleri adım adım, milim milim oluşturan o incecik damlalar bize sadece 'damlaya damlaya göl olur' demez; 'israr ederek, damlaya damlaya imkansız doğa mucizeleri yaratılır' der. Dünyadaki her büyük güzelliğin ardında asırlık sessiz bir sabır ve yavaş ama tükenmez bir gayret yatar.\n\nHierapolis'in o büyüleyici mezarlık alanı (Nekropol), ölümün bile bir sanat, bir saygı ve bir huzur sükuneti içinde ele alınabileceğini gösterir. Pamuk gibi bembeyaz kalkerlerin altında yatan o fokurdayan kırmızı termal sular, insanın en dingin dış görünüşünün ardında bile sönmeyen, tutkulu bir ateş barındırdığının nişanesidir.",
        "gastronomi": "- **Denizli Kebabı (Fırın Kebabı):** Elle yenmesi adet olan, sakız odunu ateşinde taş fırınlarda pişen kuzu şöleni.\n- **Zafer Gazozu:** Bölgenin retro ve popüler serinleticisi.\n- **Yanık Yoğurt:** Bakır kazanlarda bilerek dibi tutturularak elde edilen özel isli lezzet.",
        "landmarks": ["Pamukkale Travertenleri", "Hierapolis Antik Kenti ve Antik Havuz", "Laodikeia Antik Kenti", "Karahayıt Kırmızı Su Suları", "Teleferik ve Bağbaşı Yaylası", "Güney Şelalesi"]
    },
    "Adana": {
        "library": "Adana İl Halk Kütüphanesi - Şehir merkezinde yer alıyor, klimaları yaz sıcağında can kurtarıyor, priz imkanları iyi.",
        "hikmet": "Seyhan ve Ceyhan'ın bereketiyle yıkanan bu sıcak topraklar, sadece bedeni değil, cömertliğiyle ruhu da doyurur.",
        "quote": "\"Güneşin en dik açıyla vurduğu, pamuk tarlalarının beyazlığında alın terinin ve samimiyetin harmanlandığı sıcak Akdeniz kapısı.\"",
        "description": "Toroslar'ın eteklerinden Akdeniz'e süzülen nehirlerin suladığı bereketli Çukurova'nın kalbi. Adana, enerjisi yüksek, insanı sıcak ve yaşam ritmi son derece canlı bir şehirdir. Tarihi Taşköprü'nün üzerinden geçen rüzgar, antik çağlardan bu yana kim bilir kaç medeniyetin hikayesini Seyhan'ın sularına fısıldamıştır. Kentin sokaklarında yürürken burnunuza çalınan o nefis kebap kokuları, esnafın sıcak selamlamaları ve portakal çiçeği mevsiminde şehri saran o büyüleyici koku, Adana'yı sadece bir coğrafya değil, bir yaşam coşkusu haline getirir.",
        "sufi_notes": "Adana'nın yakıcı sıcağı, sabrın ve tahammülün bir imtihanı gibidir. Seyhan Nehri'nin kenarında oturup suların akışını izlemek, hayatın da bu nehir gibi durmaksızın akıp gittiğini, insana düşenin ise bu akışa ayak uydururken etrafına bereket saçmak olduğunu hatırlatır. Taşköprü'nün asırlık kemerleri, zamanın geçiciliğine karşı dik duran sarsılmaz birer şahit gibidir; tıpkı bu toprakların insanının her türlü zorluğa karşı gösterdiği o dirençli ve dik duruş gibi.",
        "gastronomi": "- **Adana Kebabı:** Zırhla çekilmiş erkek koyun eti, kuyruk yağı ve pul biberin köz ateşindeki kusursuz dansı.\n- **Şalgam Suyu:** Kebap sofralarının acılı, mor mayalı ve asil eşlikçisi.\n- **Bici Bici:** Yaz sıcağında nişasta, buz ve şerbetin buz gibi serinleten ferahlığı.",
        "landmarks": ["Tarihi Taşköprü", "Sabancı Merkez Camii", "Ulu Cami ve Ramazanoğulları Külliyesi", "Büyük Saat Kulesi", "Seyhan Baraj Gölü", "Varda Köprüsü (Alman Köprüsü)"]
    },
    "Hatay": {
        "library": "Hatay İl Halk Kütüphanesi - Tarihi dokusuyla ilham verici, sessiz çalışma odaları tefekkür ve kodlama için çok uygun.",
        "hikmet": "Medeniyetlerin ve inançların ortak sofrasında buluşan Hatay, barışın ve kardeşliğin ebedi yurdudur.",
        "quote": "\"Tarihin en eski caddelerinde farklı ezan, çan ve hazzan seslerinin birbirine karıştığı hoşgörü bahçesi.\"",
        "description": "Tarih boyunca 'Doğu'nun Kraliçesi' olarak anılan, Asi Nehri'nin tersine akışıyla nam saldığı kadim Antakya toprakları. Hatay, Hristiyanlığın ilk kiliselerinden St. Pierre'e, Anadolu'nun ilk camilerinden Habib-i Neccar'a ev sahipliği yapan, inançların ve kültürlerin binlerce yıldır barış içinde yan yana yaşadığı eşsiz bir mozaiktir. Sokaklarında yürürken Roma döneminden kalma taş sütunların izlerine rastlayabilir, dünyanın en zengin mozaik müzelerinden birinde zaman yolculuğuna çıkabilirsiniz. Hatay, her kültürden, her dilden ve her inançtan insanın ortak bir çatı altında kardeşçe yaşayabileceğinin en somut ve asil kanıtıdır.",
        "sufi_notes": "Habib-i Neccar Camii'nin sessizliğinde oturup, hakikati haykıran o ilk inananların hikayesini düşünmek, ruha derin bir teslimiyet ve huzur aşılar. Farklı dinlerin tapınaklarının neredeyse sırt sırta verdiği bu şehir, insana 'yaradılanı severim Yaradan'dan ötürü' felsefesinin en somut halini gösterir. Asi Nehri'nin tersine akması gibi, buradaki manevi iklim de insana dünyanın bencil ve maddeci akışına karşı durmayı, sevgi ve barış yolunda tersine kürek çekmeyi öğretir.",
        "gastronomi": "- **Antakya Künefesi:** Tuzsuz özel künefe peyniri, tel kadayıf ve sıcacık şerbetin közde pişen efsanesi.\n- **Tepsi Kebabı:** Zırh kıymasının baharatlar ve sosla fırın tepsisinde ağır ağır pişmesiyle oluşan şaheser.\n- **Humus:** Bol tahin, kimyon ve zeytinyağıyla sunulan, ılık ve enfes bir Akdeniz klasiği.",
        "landmarks": ["Habib-i Neccar Camii", "St. Pierre Kilisesi", "Hatay Arkeoloji Müzesi", "Titus Tüneli ve Beşikli Mağara", "Tarihi Antakya Sokakları", "Harbiye Şelaleleri"]
    },
    "Mugla": {
        "library": "Muğla İl Halk Kütüphanesi - Üniversite bölgesine yakın, çalışma ortamı sessiz ve ferah, priz sayısı yeterli.",
        "hikmet": "Mavinin yeşille kavuştuğu bu kıyılar, ruhunu dinlendirmek isteyen her seyyah için bir sığınaktır.",
        "quote": "\"Antik Likya ve Karia medeniyetlerinin gölgesinde, turkuaz suların zümrüt ormanlarla seviştiği ebedi mavi yolculuk.\"",
        "description": "Ege ve Akdeniz'in kucaklaştığı, her koyunda başka bir efsanenin saklandığı Muğla. Antik kalıntıları, el değmemiş doğası ve uçsuz bucaksız koyları ile burası sadece bir yaz tatili rotası değil; tarihin ve doğanın en cömert birleşimidir. Fethiye'deki Ölüdeniz'in o kıpırtısız sakinliğinden, Kayaköy'ün hüzünlü hayalet sokaklarına uzanan bu yolculuk, insanın iç dünyasında da yeni kapılar aralar.",
        "sufi_notes": "Kayaköy'ün terk edilmiş taş evleri arasında rüzgarın uğultusunu dinlemek, insan yapımı her şeyin geçiciliğini ve sessizliğin sesini öğretir. Doğanın insan elinin çekildiği yerleri nasıl yavaşça geri aldığını görmek, kibirden uzaklaşmak için muhteşem bir derstir. Muğla'nın turkuaz suları ise ruhu arındıran, berraklaştıran manevi bir ayna gibidir.",
        "gastronomi": "- **Muğla Köftesi:** İçi sulu, az baharatlı, yanında közlenmiş biber ve domatesle sunulan lezzet.\n- **Çökertme Kebabı:** İncecik çıtır patatesler üzerinde yoğurt ve sosla sunulan et şöleni.\n- **Kabak Çiçeği Dolması:** Sabahın ilk ışıklarında toplanan taze kabak çiçeklerinin pirinçle buluştuğu Ege başyapıtı.",
        "landmarks": ["Ölüdeniz", "Kayaköy", "Saklıkent Kanyonu", "Kral Kaya Mezarları (Dalyan)", "Sedir Adası (Kleopatra Plajı)", "Bodrum Kalesi"]
    },
    "Nevsehir": {
        "library": "Nevşehir İl Halk Kütüphanesi - Taş mimarisiyle huzurlu, sessiz odaları odağı artırmak için ideal.",
        "hikmet": "Yerin altındaki gizli sığınaklar ve göğe uzanan peri bacaları, insana hem yerin altını hem de gökleri tefekkür ettirir.",
        "quote": "\"Milyonlarca yıllık lavların ve rüzgarın taşa fısıldadığı, masalsı balonların gökyüzünü süslediği güzel atlar ülkesi.\"",
        "description": "Erciyes and Hasan Dağı'nın lavlarıyla şekillenen, rüzgarın sabırla oymasıyla oluşan masalsı coğrafya: Kapadokya. Nevşehir, peri bacalarının mistik görüntüsü, kayalara oyulmuş bin yıllık kiliseleri ve yerin altına kat kat inen devasa yeraltı şehirleriyle adeta başka bir gezegendir. Sabahın ilk ışıklarıyla gökyüzüne yükselen yüzlerce rengarenk balon, bu antik vadileri gökyüzünden izleme şansı sunarak insanı büyüler.",
        "sufi_notes": "Karanlık Kilise'nin loş duvarlarındaki fresklere bakmak, yüzyıllar boyu burada saklanan inananların adanmışlığını hissettirir. Derinkuyu Yeraltı Şehri'nin dar tünellerinde ilerlerken insan kendi içsel derinliklerine iner; dar geçitler sabrı ve nefsi terbiye etmeyi simgeler. Peri bacalarının zamanla aşınan gövdeleri ise dünyanın gelip geçici şekillerden ibaret olduğunu sessizce anlatır.",
        "gastronomi": "- **Testi Kebabı:** Güveç testisi içinde közde saatlerce pişen ve masada kırılarak sunulan et yemeği.\n- **Nevşehir Tava:** Sarımsak, biber ve kuzu etinin fırında ağır ağır pişirilmesiyle yapılan lezzet.\n- **Köftür:** Üzüm şırasından yapılan nişastalı, doğal Kapadokya lokumu.",
        "landmarks": ["Göreme Açık Hava Müzesi", "Uçhisar Kalesi", "Derinkuyu Yeraltı Şehri", "Ihlara Vadisi", "Aşk Vadisi", "Devrent Vadisi (Hayal Vadisi)"]
    },
    "Trabzon": {
        "library": "Trabzon İl Halk Kütüphanesi - Şehir merkezinde vakur bir bina, araştırma ve geliştirme için sessiz odalar sunuyor.",
        "hikmet": "Sarp kayalıkların sinesine kurulan mabetler, inancın hiçbir engel tanımadığının en somut nişanesidir.",
        "quote": "\"Hırçın dalgaların vurduğu kıyılardan, sisler altındaki yemyeşil yaylalara uzanan, tarihin vakur limanı.\"",
        "description": "Karadeniz'in hırçın suları ile sarp dağlarının arasında kurulmuş kadim liman şehri. Trabzon, Zigana Dağları'nın sisli geçitlerinden süzülen Karadeniz kültürünün, kemençe sesinin ve horon coşkusunun merkezidir. Karadağ'ın dik yamaçlarına adeta bir kartal yuvası gibi kondurulmuş bin 600 yıllık Sümela Manastırı, inancın sarp dağları nasıl aşabileceğinin en büyüleyici kanıtıdır. Hamsi kokan sokakları, yemyeşil yaylaları ve tarihi yapılarıyla Trabzon, Karadeniz'in ruhunu en derin hissettiren kentidir.",
        "sufi_notes": "Sümela Manastırı'nın Karadağ yamaçlarındaki o dik, sarp ve sisli yolunu adımlamak, hakikate giden yolun da meşakkatli ama ulaşıldığında o derece ferahlatıcı olduğunu hissettirir. Doğu Karadeniz'in geçit vermez dağları, insana tabiat karşısındaki acziyetini hatırlatarak tevazuyu öğretir. Kemençenin o kıvrak, hırçın ama bir o kadar da dertli sesi, bu toprakların insanının neşesini ve hüznünü aynı anda içinde barındıran kalbinin yansımasıdır.",
        "gastronomi": "- **Trabzon Akçaabat Köftesi:** Bol sarımsaklı ve özel dana kıymasıyla yapılan, ızgarada pişen efsane köfte.\n- **Kuymak (Muhlama):** Kolot peyniri, mısır unu ve tereyağının uzayıp giden o nefis lezzet senfonisi.\n- **Hamsili Pilav:** Fırında nar gibi kızarmış hamsilerin mısır ekmeği ve baharatlı pilavla buluşması.",
        "landmarks": ["Sümela Manastırı", "Trabzon Ayasofya Camii", "Uzungöl", "Atatürk Köşkü", "Hıdırnebi Yaylası", "Boztepe Seyir Terası"]
    },
    "Mardin": {
        "library": "Mardin İl Halk Kütüphanesi - Taş mimarisi ve Mezopotamya ovasına bakan avlusuyla seyyah yazılımcıya ilham kaynağı.",
        "hikmet": "Gecesi gerdanlık, gündüzü mezarlık olan bu taş şehir, ölüm ile yaşamın en estetik buluşma noktasıdır.",
        "quote": "\"Mezopotamya ovasına tepeden bakan, sarı kalker taşından oyulmuş masalsı ve kadim bir medeniyet kalesi.\"",
        "description": "Tarihin ve dinlerin harmanlandığı, taşın dile geldiği kadim Mezopotamya şehri. Mardin, daracık abbaraları (tünelli geçitler), göğe yükselen minareleri ve manastır kuleleri ile zamana meydan okuyan sarı taş bir masaldır. Kasımiye Medresesi'nin avlusundaki havuzda akan suyun hikayesi, insan ömrünün aşamalarını (doğum, gençlik, yaşlılık ve ölüm sonrası) sembolize eder. Akşamları ovaya çöken karanlıkla birlikte ışıldayan şehir, Mezopotamya ovasının üzerinde parıldayan asil bir gerdanlık gibi görünür.",
        "sufi_notes": "Kasımiye Medresesi'ndeki su akan çeşmenin başında oturup suyun akışını izlemek, hayatın geçiciliğini ve en sonunda dingin bir havuzda (ahirette) toplanacağını tefekkür etmek için muazzam bir fırsattır. Süryani manastırı Deyrulzafaran'ın bin yıllık taşlarında yankılanan dualar, inancın dilleri ve zamanı aşan ortak tınısını hatırlatır. Mardin'in dar sokaklarında kaybolmak, aslında insan yapımı sınırların anlamsızlığını ve insanlığın kadim ortak kökenini kavramaktır.",
        "gastronomi": "- **Mardin İçli Köftesi (İrok):** Baharatlı kıyma ve ceviz dolgulu, dışı çıtır bulgurlu kızartma başyapıtı.\n- **Kaburga Dolması:** Kuzu kaburgasının iç pilavla doldurularak saatlerce buharda pişirilen bayram yemeği.\n- **Süryani Çöreği:** Mahlep, zencefil ve tarçın kokulu, hurma dolgulu nefis çörek.",
        "landmarks": ["Eski Mardin Sokakları ve Abbaralar", "Deyrulzafaran Manastırı", "Kasımiye Medresesi", "Dara Antik Kenti", "Mardin Ulu Camii", "Zinciriye Medresesi"]
    },
    "Mersin": {
        "library": "Mersin İl Halk Kütüphanesi - Sahile yakın, ferah çalışma masaları ve deniz manzaralı dinlenme alanlarıyla motivasyon verici.",
        "hikmet": "Denizin ortasındaki kaleler ve derin obruklar, insanın hem içindeki derin dehlizleri hem de dış dünyadaki sığınakları aramasıdır.",
        "quote": "\"Toroslar'ın gölgesinde, Akdeniz'in tuzuyla yıkanan, antik Likya'dan bugüne uzanan narenciye kokulu sahil diyarı.\"",
        "description": "Akdeniz'in en uzun kıyı şeritlerinden birine sahip, palmiyeler ve portakal bahçeleriyle süslü liman şehri. Mersin, denizin ortasında yükselen efsanevi Kızkalesi, yerin yüzlerce metre altına inen Cennet ve Cehennem obrukları ve tarihin en eski mağara sığınaklarından Eshab-ı Kehf (Yedi Uyurlar) ile gizemli ve zengin bir mirasa sahiptir. Limanının getirdiği kozmopolit hava ile Akdeniz sıcaklığını harmanlayan bu şehir, her adımda yeni bir antik kent kalıntısıyla gezginleri selamlar.",
        "sufi_notes": "Cennet Obruğu'nun yüzlerce basamakla inilen o serin derinliğinde akan yeraltı nehrinin sesini dinlemek, insanın kendi bilinçaltının derinliklerine inmesi gibidir. Eshab-ı Kehf mağarasında zamanın nasıl büküldüğünü ve teslimiyetin gücünü düşünmek, ruha derin bir huşu verir. Kızkalesi'nin kıyıdan uzakta, suların ortasındaki yalnızlığı, insanın dünyadaki yalnız ama bir o kadar da asil duruşunu simgeler.",
        "gastronomi": "- **Tantuni:** İnce kıyılmış dana etinin sacda pamuk yağıyla pişip, lavaş arasında limon ve sumakla buluşması.\n- **Kerebiç:** İrmiğin ceviz veya fıstıkla doldurulup, çöven otu kökünden elde edilen beyaz köpükle sunumu.\n- **Cezerye:** Havuç, şeker ve kuruyemişlerin saatlerce kaynatılıp hindistan ceviziyle kaplanan enerji deposu.",
        "landmarks": ["Kızkalesi (Deniz Kalesi)", "Cennet ve Cehennem Obrukları", "Eshab-ı Kehf Mağarası", "Kanlıdivane Antik Kenti", "Soloi Pompeipolis Antik Kenti", "Tarsus Ulu Camii ve Danyal Peygamber Kabri"]
    },
    "Isparta": {
        "library": "Isparta Halil Hamit Paşa İl Halk Kütüphanesi - Şehir merkezinde, sessiz çalışma alanları geniş ve ferah.",
        "hikmet": "Gülün kokusu geçicidir ama onun ruhumuza üflediği zarafet ve saflık baki kalır.",
        "quote": "\"Göller yöresinin serin esintisinde, lavanta ve gül kokulu sokakların asırlık tarihle buluştuğu sakin şehir.\"",
        "description": "Göller Yöresi'nin kalbinde yer alan, Türkiye'nin gül bahçesi Isparta. Eğirdir Gölü'nün göz alıcı turkuazı, lavanta kokulu Kuyucak köyü ve antik çağların izlerini taşıyan Sagalassos ile burası doğanın ve tarihin en huzurlu köşelerinden biridir. Şehir, sakin yaşamı ve mis kokulu tarım arazileriyle insana huzur verir.",
        "sufi_notes": "Eğirdir Gölü'nün kenarında durup gün batımını izlemek, hayatın karmaşasından sıyrılıp sakinleşmek için harika bir tefekkür anıdır. Gül hasadı yapan işçilerin alın terini görmek, emeğin ve doğanın cömertliğinin kutsallığını hatırlatır. Sagalassos'un yüksek zirvelerinde yükselen sütunlar, insan yapımı görkemin doğanın büyüklüğü karşısındaki yerini gösterir.",
        "gastronomi": "- **Isparta Fırın Kebabı:** Kuzu etinin taş fırınlarda kendi yağıyla saatlerce pişmesiyle oluşan enfes lezzet.\n- **Kabune Pilavı:** Düğünlerin vazgeçilmezi olan nohutlu, etli ve baharatlı geleneksel pilav.\n- **Gül Şerbeti:** Taze gül yapraklarından yapılan mis kokulu, serinletici şerbet.",
        "landmarks": ["Eğirdir Gölü ve Can Ada", "Sagalassos Antik Kenti", "Kuyucak Lavanta Köyü", "Yazılı Kanyon Tabiat Parkı", "Isparta Ulu Camii", "Davraz Dağı Kayak Merkezi"]
    },
    "Aksaray": {
        "library": "Aksaray İl Halk Kütüphanesi - Bozkırın ortasında modern ve sessiz bir çalışma alanı.",
        "hikmet": "Bozkırın ortasındaki derin vadiler, hayatın en kurak anlarında bile sığınabileceğimiz gizli vahaların olduğunu fısıldar.",
        "quote": "\"Ihlara Vadisi'nin yeşil sükûnetinde akan suların, Hasan Dağı'nın heybetli gölgesiyle buluştuğu kadim geçit.\"",
        "description": "Kapadokya'nın batı kapısı olan, Hasan Dağı'nın eteklerindeki Aksaray. Melendiz Çayı'nın binlerce yılda oyduğu muazzam Ihlara Vadisi, kayalara oyulmuş kiliseleri ve Selçuklu mirası kervansaraylarıyla burası adeta bir tarih and doğa müzesidir. Bozkırın ortasında yükselen bu antik kent, kervanların ve dervişlerin asırlar boyu sığındığı bir menzildir.",
        "sufi_notes": "Ihlara Vadisi'ne inen yüzlerce basamağı adımlarken insan gürültülü dünyayı geride bırakıp nehrin ve kuşların sesine odaklanır. Selime Katedrali'nin devasa kaya oyuklarında yankılanan rüzgar, geçmiş yüzyıllardaki insanların manevi arayışlarını hissettirir. Eğri Minare'nin eğikliğine rağmen asırlardır ayakta durması, inancın ve sağlam temellerin gücünü sembolize eder.",
        "gastronomi": "- **Aksaray Tava:** Kuzu eti, sarımsak ve domatesin fırında ağır ağır pişmesiyle yapılan nefis yemek.\n- **Şeker Pancarı Pekmezi:** Bölgenin verimli topraklarından elde edilen doğal ve şifalı pekmez.\n- **Sıkma:** Sıcak sac ekmeği arasına yerel tulum peyniri konularak yapılan pratik lezzet.",
        "landmarks": ["Ihlara Vadisi", "Selime Katedrali", "Hasan Dağı", "Eğri Minare (Kızıl Minare)", "Sultanhanı Kervansarayı", "Narlıgöl (Krater Gölü)"]
    },
    "Eskisehir": {
        "library": "Eskişehir İl Halk Kütüphanesi - Genç nüfusun yoğun olduğu, dinamik, internet hızı yüksek ve priz imkanı bol olan modern kütüphane.",
        "hikmet": "Porsuk Çayı'nın şehri ikiye bölen dingin akışı, modern yaşamın ritmiyle tarihin zarafetinin uyumudur.",
        "quote": "\"Odunpazarı'nın renkli cumbalı evlerinde geçmişin fısıldadığı, gençliğin ve sanatın coşkuyla yaşandığı modern vaha.\"",
        "description": "İç Anadolu'nun parlayan yıldızı, kültür, sanat ve üniversite şehri Eskişehir. Tarihi Odunpazarı evlerinin nostaljik sokaklarından, Porsuk Çayı kenarındaki modern kafelere; lüle taşı işçiliğinden devasa parklarına kadar burası Türkiye'nin en yaşanabilir ve estetik şehirlerinden biridir. Kent, geçmişi korurken geleceğe umutla bakan aydınlık bir karaktere sahiptir.",
        "sufi_notes": "Kurşunlu Külliyesi'nin sessiz avlusunda oturup lüle taşı ustalarının sabırlı ellerini izlemek, sabrın ve sanatın manevi değerini anlamak için güzel bir fırsattır. Şehrin içinden geçen Porsuk Çayı, hayatın da böyle berrak ve akıcı olması gerektiğini fısıldar. Balmumu müzesindeki heykellere bakmak, tariye yön veren insanların bıraktığı kalıcı izler üzerine tefekküre sevk eder.",
        "gastronomi": "- **Çibörek:** İnce açılmış hamur içine kıyma konularak yağda kızartılan Kırım Tatar mirası efsane lezzet.\n- **Balaban Köfte:** Soslu pide parçaları üzerine dizilen köfte, yoğurt ve tereyağı kombinasyonu.\n- **Met Helvası:** Un, yağ ve şekerden yapılan, pişmaniyeye benzeyen geleneksel Eskişehir helvası.",
        "landmarks": ["Tarihi Odunpazarı Evleri", "Porsuk Çayı ve Adalar Bölgesi", "Kurşunlu Külliyesi ve Camii", "Sazova Parkı (Bilim Sanat ve Kültür Parkı)", "Eskişehir Balmumu Heykeller Müzesi", "Kentpark"]
    },
    "Sivas": {
        "library": "Sivas Şems-i Sivasî İl Halk Kütüphanesi - Selçuklu esintileriyle bezeli geniş ve düzenli çalışma salonları.",
        "hikmet": "Selçuklu çinilerindeki geometrik nizam, evrendeki kusursuz matematiksel ve manevi düzenin taştaki yansımasıdır.",
        "quote": "\"Ulu medreselerin göğe yükselen çifte minarelerinde, Cumhuriyet'in ilk kongre kararlarının yankılandığı vakur bozkır kalesi.\"",
        "description": "Tarih boyunca Selçuklu'nun en önemli merkezlerinden biri olan, Cumhuriyet'in temellerinin atıldığı Sivas. Gök Medrese ve Çifte Minareli Medrese'nin muazzam taş oyma işçilikleri, Sivas Kongre Binası'nın tarihi önemi ve Divriği Ulu Camii'nin UNESCO miras listesindeki eşsiz mimarisi ile bu şehir adeta bir açık hava müzesidir. Soğuk ayazı meşhur olsa da insanının sıcaklığıyla gönülleri ısıtır.",
        "sufi_notes": "Şifaiye Medresesi'nin darüşşifa avlusunda geçmişteki şifa yöntemlerini ve su sesinin ruha olan etkilerini düşünmek derin bir içsel huzur verir. Çifte Minare'nin göğe uzanan kolları, duanın ve yükselişin sembolü gibidir. Sivas Kongre Binası'nda alınan 'Manda ve himaye kabul olunamaz' kararı, bağımsızlık ruhunun bu coğrafyadaki sarsılmaz duruşunu hatırlatır.",
        "gastronomi": "- **Sivas Köftesi:** Katkısız, sadece kıyma ve tuzla yoğrularak yapılan, etin saf lezzetini sunan tescilli köfte.\n- **Sivas Katmeri:** Tereyağlı, çıtır çıtır kat kat açılan nefis fırın işi.\n- **Madımak Yemeği:** Bozkırdan toplanan şifalı madımak otunun pastırma ve bulgurla pişirilmesi.",
        "landmarks": ["Çifte Minareli Medrese", "Gök Medrese", "Sivas Kongre Müzesi", "Şifaiye Medresesi", "Divriği Ulu Camii ve Darüşşifası", "Kangal Balıklı Kaplıcası"]
    },
    "Artvin": {
        "library": "Artvin İl Halk Kütüphanesi - Yamaçta kurulu, manzaralı, dik yokuşlardan sonra dinlenip kod yazmak için ideal sessiz sığınak.",
        "hikmet": "Bulutların üzerine kurulan bu dik yamaçlar, insanın doğa karşısındaki sınırlarını ve sabrını sınayan muazzam bir okuldur.",
        "quote": "\"Karadeniz'in göğe komşu topraklarında, geçit geçmez vadilerin ve zümrüt yeşili milli parkların gizemli cenneti.\"",
        "description": "Türkiye'nin en engebeli ve vahşi doğasına sahip, yeşilin binbir tonunu barındıran sınır şehri Artvin. Çoruh Nehri'nin derin vadileri, Karagöl'ün büyüleyici yansıması, Macahel'in bakir ormanları ve göğe yükselen yaylalarıyla burası macera ve huzur arayan gezginlerin rüyasıdır. Coğrafyanın zorluğu, insanının direncini ve doğaya olan derin saygısını şekillendirmiştir.",
        "sufi_notes": "Borçka Karagöl'ün kıyısında sislerin göl yüzeyine inişini izlemek, ilahi sanatın yeryüzündeki en zarif tablolarından birine şahit olmaktır. Macahel'in el değmemiş ormanlarında rüzgarın uğultusu, dünyanın ilk günlerindeki o saf ve temiz sükuneti fısıldar. Dik yamaçlardaki ahşap evlerin doğayla uyumu, insanın tabiata meydan okumak yerine onunla dost olması gerektiğini öğretir.",
        "gastronomi": "- **Artvin Döneri:** Yayla otlarıyla beslenen hayvanların etinden yapılan, yatık olarak odun ateşinde pişen nefis döner.\n- **Kalaco:** Süt, süzme yoğurt ve mısır unuyla yapılan geleneksel bir Artvin kahvaltılığı.\n- **Hinkal:** Kafkas esintili, içi kıymalı ve sulu devasa mantı.",
        "landmarks": ["Borçka Karagöl Tabiat Parkı", "Şavşat Karagöl", "Macahel (Camili) Havzası", "Hatila Vadisi Cam Teras", "Çoruh Kanyonu", "Atatepe (Dev Atatürk Heykeli)"]
    },
    "Bayburt": {
        "library": "Bayburt İl Halk Kütüphanesi - Çoruh Nehri kıyısında, sessiz ve sakin bir çalışma ortamı.",
        "hikmet": "Yalnızlık ve sessizlik, bozkırın ortasında kurulan bu kalede insanın kendi iç dünyasıyla yüzleşmesini sağlar.",
        "quote": "\"Çoruh Nehri'nin kıvrılarak geçtiği, bozkırın sessizliğinde yükselen kadim kale ve modern sanatın buluştuğu sıradışı diyar.\"",
        "description": "Doğu Karadeniz'i Doğu Anadolu'ya bağlayan geçitlerin üzerinde yer alan, Çoruh Nehri'nin ikiye böldüğü Bayburt. Bayburt Kalesi'nin heybetli surları, yerin altındaki gizemli Aydıntepe Yeraltı Şehri and Baksı Müzesi ile burası şaşırtıcı detaylarla doludur. Sakin, gösterişsiz ama derin bir ruha sahiptir.",
        "sufi_notes": "Bayburt Kalesi'nden şehri ve Çoruh'un akışını izlemek, imparatorlukların geçip gidişini ve kalıcı olanın sadece nehrin kendisi olduğunu tefekkür ettirir. Aydıntepe Yeraltı Şehri'nin tüf kayalara oyulmuş galerilerinde yürümek, sığınma ve korunma refleksinin manevi boyutunu düşündürür. Baksı Müzesi'nin bozkırın tepesindeki yalnızlığı, sanatın ve düşüncenin en ücra köşelerde bile nasıl çiçek açabileceğini gösterir.",
        "gastronomi": "- **Bayburt Ketesi:** Un, tereyağı ve ceviz içiyle yapılan, fırından yeni çıkmış çıtır kete.\n- **Galacoş:** Mercimek, kıyma ve süzme yoğurdun kuru ekmek parçalarıyla buluştuğu yöresel yemek.\n- **Tatlı Çorba:** Kurutulmuş kuşburnu, kayısı ve incir gibi meyvelerin aşure kıvamında pişirilmesiyle yapılan tatlı.",
        "landmarks": ["Bayburt Kalesi", "Baksı Müzesi", "Aydıntepe Yeraltı Şehri", "Çoruh Nehri Rekreasyon Alanı", "Kop Dağı Müdafaası Tarihi Milli Parkı", "Kenan Yavuz Etnografya Müzesi"]
    },
    "Gumushane": {
        "library": "Gümüşhane İl Halk Kütüphanesi - Vadinin serinliğinde, odaklanmayı kolaylaştıran butik ve huzurlu çalışma alanı.",
        "hikmet": "Kayaların arasındaki altın ve gümüş madenleri gibi, insanın içindeki cevher de ancak zorlu sınavlardan geçtikten sonra parıldar.",
        "quote": "\"Harşit Vadisi'nin sarp kayalıkları arasına gizlenmiş antik kentlerin, elma bahçelerinin ve gizemli mağaraların yurdu.\"",
        "description": "Adını asırlarca işletilen gümüş madenlerinden alan, sarp vadilerin ve yemyeşil yaylaların şehri Gümüşhane. Karaca Mağarası'nın büyüleyici sarkıt ve dikitleri, antik dönemden kalan Süleymaniye Mahallesi (Eski Gümüşhane) ve vadi yamaçlarında kurulu kiliseleriyle burası saklı bir hazinedir. Şehir, cevizli pestil ve kömesinin kokusuyla tatlı bir Karadeniz havası sunar.",
        "sufi_notes": "Karaca Mağarası'nın milyonlarca yılda şekillenen damlataş sütunları altında durmak, zamanın ne kadar yavaş aktığını ve sabrın ilahi tecellisini kavramak için eşsiz bir andır. Eski Süleymaniye Mahallesi'nin sessiz harabeleri ve yan yana duran cami ile kilise kalıntıları, geçmişteki ortak yaşam kültürünün manevi zenginliğini hatırlatır.",
        "gastronomi": "- **Gümüşhane Pestili ve Kömesi:** Dut şırası, un, süt ve ceviz/fındıkla yapılan, tüm Türkiye'de ün salmış şifalı tatlı.\n- **Siron:** Fırınlanmış yufkaların rulo yapılıp üzerine yoğurt, sarımsak ve tereyağı dökülerek sunulması.\n- **Gümüşhane Ekmeği:** Ekşi mayalı, taş fırında pişen ve günlerce taze kalan devasa ekmek.",
        "landmarks": ["Karaca Mağarası", "Süleymaniye Mahallesi (Antik Gümüşhane)", "Krom Vadisi", "Limni Gölü Tabiat Parkı", "Santa Harabeleri", "Kürtün Örümcek Ormanları"]
    },
    "Rize": {
        "library": "Rize İl Halk Kütüphanesi - Çay tarlalarının yeşili eşliğinde, modern altyapısı ve güçlü internetiyle kodlama için ideal.",
        "hikmet": "Bulutların yamaçları kucakladığı bu coğrafya, her an değişen havasıyla hayatın beklenmedik iniş çıkışlarını öğretir.",
        "quote": "\"Yemyeşil çay tarlalarının dik yamaçları süslediği, coşkulu derelerin gürültüsüyle yankılanan yaylalar diyarı.\"",
        "description": "Türkiye'nin en çok yağış alan, yeşilin en canlı yaşandığı, çayın başkenti Rize. Kaçkar Dağları'nın sis altındaki yaylaları (Ayder, Pokut, Anzer), Fırtına Deresi üzerinde yükselen asırlık taş kemer köprüler ve dik yamaçlara serpilmiş ahşap konaklar Rize'yi masalsı kılar. Hırçın derelerinin sesi, insanın içindeki tüm dinginliği harekete geçiren coşkulu bir ritme sahiptir.",
        "sufi_notes": "Pokut Yaylası'nda bulut denizinin üzerinde gün doğumunu izlemek, gökler ile yerin birleştiği o sınırda ilahi kudret karşısında secdeye varmak gibidir. Fırtına Deresi'nin azgın sularını izlemek, hayatın da bu nehir gibi engelleri yıkarak coşkuyla akması gerektiğini hatırlatır. Taş köprülerin asırlardır sellere karşı direnmesi, sağlam bir inancın fırtınalara karşı nasıl durabileceğinin simgesidir.",
        "gastronomi": "- **Rize Kavurması:** Kendi yağıyla ağır ateşte pişen, lokum kıvamındaki tescilli et yemeği.\n- **Muhlama:** Kolot peyniri, mısır unu ve tereyağının sacda pişen Karadeniz klasiği.\n- **Laz Böreği:** İnce yufkalar arasına muhallebi konulup şerbet dökülerek yapılan sıradışı tatlı.",
        "landmarks": ["Ayder Yaylası", "Pokut ve Sal Yaylaları", "Fırtına Vadisi ve Taş Kemer Köprüler", "Zil Kale", "Anzer Yaylası", "Palovit Şelalesi"]
    },
    "Ardahan": {
        "library": "Ardahan İl Halk Kütüphanesi - Kışın sıcacık soba sıcaklığında, dışarıdaki dondurucu soğuğa inat sessizce kod yazma imkanı.",
        "hikmet": "En kuzey sınırda esen dondurucu rüzgar, insanın içindeki yaşama azmini ve kardeşlik sıcaklığını daha da kurutmaz, tam aksine artırır.",
        "quote": "\"Yalnızçam Dağları'nın beyaz örtüsü altında, Çıldır Gölü'nün buz tutmuş yüzeyinde atlı kızakların kaydığı sınır boyu.\"",
        "description": "Türkiye'nin en soğuk ve en kuzeydoğu illerinden biri olan, Kafkasya geçidindeki Ardahan. Kış aylarında tamamen buz tutan devasa Çıldır Gölü, üzerindeki atlı kızakları ve eskimo usulü balıkçılığıyla masalsı bir kış diyarı sunar. Ardahan Kalesi'nin Kura Nehri'ne bakan surları ve Yalnızçam yaylaları, bu sınır kentinin vakur ve dayanıklı karakterini yansıtır.",
        "sufi_notes": "Tamamen donmuş Çıldır Gölü'nün üzerinde yürümek, suyun katılaşarak nasıl güvenli bir yola dönüştüğünü görmek, zor şartların bile inançla aşılabileceğini tefekkür ettirir. Kura Nehri'nin kıvrılarak ovayı sulaması, hayatın en sert iklimlerde bile bir yol bulup yeşereceğinin kanıtıdır. Sınır boylarındaki yalnızlık, insanın dünyadaki misafirliğini daha net hissettirir.",
        "gastronomi": "- **Ardahan Kaz Eti:** Kış aylarında kar yiyen kazların kurutulup bulgur pilavı üzerinde sunulan efsanevi lezzeti.\n- **Ardahan Kaşarı ve Çeçil Peyniri:** Yayla çiçekleriyle beslenen ineklerin sütünden yapılan peynirler.\n- **Feselli:** Tereyağlı yufkaların sac üzerinde pişirilmesiyle yapılan sıcak hamur işi.",
        "landmarks": ["Çıldır Gölü", "Ardahan Kalesi", "Yalnızçam Kayak Merkezi", "Şeytan Kalesi (Çıldır)", "Kura Nehri Vadisi", "Posof Vadisi"]
    },
    "Elazig": {
        "library": "Elazığ İl Halk Kütüphanesi - Gakgoşlar diyarında modern ve konforlu çalışma odalarıyla geniş bir kütüphane.",
        "hikmet": "Harput'un bin yıllık taş surları, medeniyetlerin yükselip alçaldığı ama maneviyatın hep ayakta kaldığı bir kaledir.",
        "quote": "\"Tarihi Harput Kalesi'nin gölgesinde, Hazar Gölü'nün batık şehrine bakan köklü medeniyetlerin ve gakgoşların yurdu.\"",
        "description": "Kadim Harput kentinin mirasçısı, baraj gölleriyle çevrili Doğu Anadolu kenti Elazığ. Harput Kalesi'nin eğik minaresi, Hazar Gölü'nün suları altındaki antik Batık Şehir ve şifalı Buzluk Mağarası ile burası tarihi ve doğal sürprizlerle doludur. Kendine has musikisi (kürsübaşı sohbetleri) ve 'gakgoş' kültürüyle son derece misafirperverdir.",
        "sufi_notes": "Harput Ulu Camii'nin İtalya'daki Pisa Kulesi'nden daha eğik olan minaresinin altında durup onun yüzyıllardır yıkılmadan duran dengesini izlemek, ilahi korumanın ve dengenin manevi bir sembolüdür. Hazar Gölü'nün berrak sularına gömülmüş o antik şehrin kalıntıları, suların altındaki geçip gitmiş hayatlar üzerine hüzünlü bir tefekkür sunar.",
        "gastronomi": "- **Harput Köftesi:** İnce bulgur, kıyma ve reyhan otunun yoğrularak salçalı suda pişirilmesiyle yapılan yemek.\n- **Orcik:** İpe dizilen cevizlerin sıcak üzüm şırasına batırılarak kurutulmasıyla yapılan şifalı tatlı.\n- **Gömme:** Fırında kömür ateşinde pişen, içi kıymalı ve tereyağlı geleneksel ekmek yemeği.",
        "landmarks": ["Harput Kalesi ve Harput Ulu Camii", "Hazar Gölü ve Batık Şehir", "Buzluk Mağarası", "Kömürhan Köprüsü", "Kürsübaşı Kultur Evi", "Hazarbaba Kayak Merkezi"]
    },
    "Erzincan": {
        "library": "Erzincan İl Halk Kütüphanesi - Deprem sonrası yenilenen geniş caddelerin ortasında modern ve ferah bir kütüphane.",
        "hikmet": "Depremlerle defalarca yıkılan bu şehrin küllerinden yeniden doğması, sabrın ve yeniden inşa iradesinin en büyük zaferidir.",
        "quote": "\"Munzur Dağları'nın gölgesinde, Fırat Nehri'nin coşkulu kollarında rafting yapılan, küllerinden doğmuş dirençli şehir.\"",
        "description": "Tarih boyunca büyük depremler atlatmış ama her seferinde daha planlı ve güzel bir şekilde yeniden kurulmuş olan Erzincan. Karanlık Kanyon'un dik yamaçları, Girlevik Şelalesi'nin donmuş buz sütunları ve tulum peynirinin eşsiz aroması ile burası Doğu Anadolu'nun düzenli ve huzurlu bir merkezidir. Fırat Nehri (Karasu) boyunca uzanan vadiler doğa sporları için biçilmiş kaftandır.",
        "sufi_notes": "Girlevik Şelalesi'nin gürül gürül akan sularının kışın devasa buz sütunlarına dönüşmesi, doğanın form değiştiren ilahi sanatını gösterir. Karanlık Kanyon'un dik kayalıklarını el oyması tünellerle aşan insanların azmi, zorluklar karşısında yılmayan insan iradesinin tecellisidir. Şehrin geniş caddelerindeki nizam, düzenin ruha verdiği dinginliği hissettirir.",
        "gastronomi": "- **Erzincan Tulum Peyniri:** Şavak aşiretinin yaylalarda koyun sütünden yapıp deri tulumlarda olgunlaştırdığı peynir.\n- **Erzincan Döneri:** Kuzu eti ağırlıklı, incecik kesilmiş ve odun ateşinde pişmiş lezzet bombası.\n- **Ketesi:** İçi unlu kavurmalı veya sade olarak fırınlanan Erzincan ketesi.",
        "landmarks": ["Karanlık Kanyon (Kemaliye)", "Girlevik Şelalesi", "Kemaliye Tarihi Evleri ve Taş Yolu", "Ergan Dağı Kayak Merkezi", "Ekşisu Mesire Alanı", "Terzibaba Türbesi ve Camii"]
    },
    "Erzurum": {
        "library": "Erzurum Erzurumlu Emrah İl Halk Kütüphanesi - Tarihi dokusuyla dadaşların vakur çalışma disiplinini yansıtan sessiz çalışma limanı.",
        "hikmet": "Çifte Minareli Medrese'nin taş kemerleri, tarihin vakur soğuğuna inançla meydan okuyan sarsılmaz birer kaledir.",
        "quote": "\"Palandöken'in karlı zirvelerinden, ulu medreselerin taş oymalarına uzanan, bozkırın vakur ve yiğit dadaşlar diyarı.\"",
        "description": "Anadolu'nun en yüksek ve köklü kentlerinden biri, dadaşlık kültürünün ve kış sporlarının merkezi Erzurum. Çifte Minareli Medrese, Yakutiye Medresesi, Ulu Camii ve Erzurum Kongre Binası ile burası Türk-İslam mimarisinin zirve noktasıdır. Palandöken Dağı'nın eteklerinde kurulu şehir, kışın kar beyazı, yazın ise serin bozkır havasıyla gezginleri karşılar.",
        "sufi_notes": "Çifte Minareli Medrese'nin taç kapısındaki hayat ağacı ve çift başlı kartal kabartmalarını incelemek, Türk mitolojisiyle İslam tasavvufunun taşta birleşen derin manasını düşünmeye sevk eder. Palandöken'in karlı yamaçlarından şehre bakarken çöken soğuk ayaz, insanın içindeki manevi sıcaklığı daha çok hissetmesini sağlar. Cağ kebabının ocaktaki ateşi, sabırla pişen nefsin simgesidir.",
        "gastronomi": "- **Cağ Kebabı:** Kuzu etinin soğan ve reyhanla marine edilip yatık şişte odun ateşinde pişirilmesi.\n- **Kadayıf Dolması:** Kadayıf tellerinin ceviz dolgusuyla sarılıp kızartılarak şerbetlenmesi.\n- **Erzurum Ketesi:** Kat kat yağlanmış hamurun fırınlanmasıyla yapılan unlu kete.",
        "landmarks": ["Çifte Minareli Medrese", "Yakutiye Medresesi", "Palandöken Kayak Merkezi", "Erzurum Kalesi ve Üç Kümbetler", "Erzurum Kongre Binası", "Tarihi Erzurum Evleri"]
    },
    "Kars": {
        "library": "Kars İl Halk Kütüphanesi - Rus döneminden kalma taş binaların mistik havasında, karlar altında kodlama mesaisi yapabileceğiniz sıcak sığınak.",
        "hikmet": "Ani Harabeleri'nin sessizliği, yan yana yıkılmış cami ve kiliselerin asırlar boyu süren ortak insanlık tefekkürüdür.",
        "quote": "\"Rus mimarisinin taş sokaklarından, Ani Harabeleri'nin sınır çizen yalnızlığına uzanan, karlar altındaki sınır masalı.\"",
        "description": "Türkiye'nin en doğusunda, çok kültürlü yapısıyla ve Rus döneminden kalma ızgara planlı taş binalarıyla ünlü Kars. Ermenistan sınırında yer alan görkemli Ani Harabeleri, Kars Kalesi ve aşıklık geleneği ile burası gizemli bir sınır masalıdır. Kış aylarında Doğu Ekspresi ile gelen gezginlerin karla kaplı sokaklarında kaybolduğu eşsiz bir destinasyondur.",
        "sufi_notes": "Ani Harabeleri'nde, Arpaçay nehrinin sınır çizdiği kanyonda durup Ebul Manuçihr Camii ile katedral kalıntılarını izlemek, sınırların yapaylığını ve inancın kalıcılığını hissettirir. Ebü'l-Hasan Harakānî Hazretleri'nin türbesinin mistik havası, bu soğuk sınır şehrini ısıtan manevi bir ocaktır. Kar altında parıldayan taş binalar, sabrın ve estetiğin simgesidir.",
        "gastronomi": "- **Kars Gravyeri ve Kaşarı:** Aylarca olgunlaştırılan, gözenekli and yoğun aromalı peynir sanatı.\n- **Kars Kazı:** Kışın kesilip kurutulan kaz etinin bulgur pilavı üzerindeki nefis sunumu.\n- **Piti Kebabı:** Nohut, kuzu eti ve safranın fırınlanıp yufka üzerine dökülerek yendiği lezzet.",
        "landmarks": ["Ani Harabeleri (UNESCO)", "Kars Kalesi ve Taş Köprü", "Ebü'l-Hasan Harakānî Türbesi ve Evliya Camii", "Rus Dönemi Taş Binalar", "Sarıkamış Allahuekber Dağları Şehitliği", "Kars Peynir Müzesi"]
    },
    "Malatya": {
        "library": "Malatya İl Halk Kütüphanesi - Şehir merkezinde yer alan, geniş araştırma kaynakları ve rahat çalışma alanları sunan yerleşke.",
        "hikmet": "Toprağın sinesinden fışkıran kayısılar, sabırla açan çiçeklerin en tatlı meyveye dönüşen ilahi mükafatıdır.",
        "quote": "\"Fırat Vadisi'nin bereketli topraklarında, kayısı bahçelerinin turuncusunda parıldayan antik Arslantepe'nin kadim yurdu.\"",
        "description": "Dünya kayısı üretiminin merkezi, Fırat Nehri'nin suladığı verimli ovaların şehri Malatya. Tarihin en eski bürokratik devlet yapısının bulunduğu Arslantepe Höyüğü, Somuncu Baba Külliyesi ve Levent Vadisi'nin devasa kanyonları ile burası köklü bir geçmişe sahiptir. İnsanının samimiyeti ve çalışkanlığı, topraklarının bereketiyle birleşmiştir.",
        "sufi_notes": "Darende'deki Somuncu Baba Külliyesi'nin avlusunda, Tohma Çayı'nın kanyon kayaları arasından süzülen aktığı nehrin kenarında oturmak, ruhu dünyevi tüm karmaşadan arındıran manevi bir vahadır. Arslantepe'deki kerpiç saray kalıntıları, gücün ve devlet yapılarının geçiciliğini tefekkür ettirir. Kayısı ağaçlarının baharda beyaza, yazın turuncuya boyanması, tabiatın diriliş ve bereket döngüsüdür.",
        "gastronomi": "- **Analı Kızlı Çorba:** İçi kıymalı küçük içli köfteler ve nohutlu salçalı sosun uyumu.\n- **Kağıt Kebabı:** Kuzu etinin sebzelerle fırın kağıdında saatlerce fırınlanmasıyla yapılan lokum lezzet.\n- **Kayısı Tatlısı:** Taze veya kuru kayısıların tereyağında kavrulup tereyağıyla sunulması.",
        "landmarks": ["Arslantepe Höyüğü (UNESCO)", "Somuncu Baba Külliyesi ve Tohma Kanyonu", "Levent Vadisi Cam Teras", "Malatya Ulu Camii", "Karakaya Baraj Gölü", "Şire Pazarı"]
    },
    "Tunceli": {
        "library": "Tunceli İl Halk Kütüphanesi - Munzur nehrinin esintisiyle serinleyen, sessiz çalışma ortamı ve güler yüzlü çalışanlarıyla butik kütüphane.",
        "hikmet": "Munzur'un hırçın köpüklü suları, dağların derinliklerinden gelen en saf ve temiz yaşam energisidir.",
        "quote": "\"Munzur Dağları'nın geçit vermez zirvelerinde, hırçın nehirlerin ve kutsal gözelerin sarmaladığı gizemli coğrafya.\"",
        "description": "Tunceli, sarp dağların, kanyonların ve akarsuların çevrelediği, doğanın en bakir kaldığı Doğu Anadolu ilidir. Kutsal kabul edilen Munzur Gözeleri, Munzur Vadisi Milli Parkı ve Munzur Çayı rafting parkurları ile burası doğa severler için eşsizdir. Alevi-Bektaşi kültürünün en yoğun yaşandığı, doğaya ve canlıya derin bir saygının hakim olduğu mistik bir atmosfere sahiptir.",
        "sufi_notes": "Munzur Gözeleri'nde kayaların arasından fışkıran buz gibi suların sesini dinlemek, yaşam pınarının ve ilahi yaratılışın durmaksızın fışkıran enerjisini hissetmektir. Yöre halkının dağ keçilerini kutsal sayması, doğadaki tüm canlılarla barış içinde yaşama felsefesinin en asil tezahürüdür. Dağların doruklarına çöken sis, insanın içsel dünyasındaki sır perdelerini aralaması için tefekkür imkanı sunar.",
        "gastronomi": "- **Munzur Sarımsaklı Tunceli Kavurması:** Munzur dağlarından toplanan yabani sarımsaklarla tatlandırılan kuzu eti.\n- **Zerefet (Babuko):** Fırında pişen sert hamurun içinin oyulup, tereyağı ve sarımsaklı yoğurt dökülerek yendiği yemek.\n- **Dut Pekmezi ve Pülümür Balı:** Tamamen organik çiçeklerden elde edilen şifalı bal.",
        "landmarks": ["Munzur Gözeleri", "Munzur Vadisi Milli Parkı", "Pülümür Çayı ve Kanyonu", "Kutudere Mesire Alanı", "Halbori Gözeleri", "Pertek Kalesi"]
    },
    "Canakkale": {
        "library": "Çanakkale Mehmet Akif Ersoy İl Halk Kütüphanesi - Boğaz manzaralı terası ve geniş çalışma alanlarıyla seyyah yazılımcılar için mükemmel bir durak.",
        "hikmet": "Tarihin en büyük savaşlarının yaşandığı bu topraklar, barışın ve kardeşliğin en kalıcı anıtıdır.",
        "quote": "\"Boğazın serin rüzgarında destanların yankılandığı, Truva'dan Çanakkale Geçilmez destanına uzanan köprü.\"",
        "description": "Marmara ile Ege'nin birleştiği, tarihin seyrini değiştiren savaşların yaşandığı kahraman şehir Çanakkale. Truva'nın binlerce yıllık mitolojik surlarından, Çanakkale Savaşı'nın yaşandığı Gelibolu Yarımadası'ndaki şehitliklere kadar burası tam bir destanlar coğrafyasıdır. Şehir, boğazın iki yakasında uzanan tarihi kaleleri, Aynalı Çarşısı ve kordon boyundaki huzurlu yürüyüş yollarıyla ziyaretçilerini kendine hayran bırakır.",
        "sufi_notes": "Gelibolu Şehitliği'nde yatan binlerce vatan evladının ve yabancı askerin mezarları arasında yürürken, hayatın ne kadar kıymetli olduğunu ve savaşın acımasızlığını derinden tefekkür edersiniz. Truva atının gölgesinde ise güç ve hilenin geçici olduğunu, sadece hakikatin ve adaletin yarına kaldığını anlarsınız. Boğazın sularına vuran gün batımı, ruhu sakinleştiren ve içsel bir dinginliğe sevk eden eşsiz bir manzaradır.",
        "gastronomi": "- **Peynir Helvası:** Fırınlanmış veya sade, tuzsuz peynirden yapılan Çanakkale'nin en meşhur tatlısı.\n- **Sardalya:** Boğazdan taze tutulan, asma yaprağında veya ızgarada sunulan nefis balık.\n- **Ezine Peyniri:** Kaz Dağları'nın esintisiyle beslenen koyun/keçi sütünden yapılan dünyaca ünlü peynir.",
        "landmarks": ["Aynalı Çarşı", "Çanakkale Şehitler Abidesi", "Truva Antik Kenti", "Kilitbahir Kalesi", "Çanakkale Deniz Müzesi", "Asos Antik Kenti (Behramkale)"]
    },
    "Izmir": {
        "library": "İzmir Atatürk İl Halk Kütüphanesi - Konak'ta yer alan, İzmir'in en köklü kütüphanelerinden biri. Çalışma alanları ferah, internet bağlantısı hızlı.",
        "hikmet": "Ege'nin özgür rüzgarı ve parıldayan güneşi, insana hayatın her anını coşkuyla ve sevgiyle yaşamayı fısıldar.",
        "quote": "\"Mavi denizin kıyısında, antik kütüphanelerin ve kordon boyundaki cıvıl cıvıl hayatın harmanlandığı Ege'nin incisi.\"",
        "description": "Ege'nin kalbi, Türkiye'nin batıya açılan en aydınlık penceresi İzmir. Kordon boyundaki palmiyeleri, Tarihi Saat Kulesi, cıvıl cıvıl Kemeraltı Çarşısı ve hemen yanı başındaki antik dünyanın en büyük kenti Efes ile İzmir, hem modern bir metropol hem de devasa bir tarih hazinesidir. Şehir, insanının sıcaklığı, özgür ruhu ve körfezin getirdiği huzurla seyyahların vazgeçilmez duraklarından biridir.",
        "sufi_notes": "Efes Antik Kenti'nin mermer caddelerinde yürürken, bir zamanlar binlerce insanın yaşadığı bu devasa şehrin şimdi sessiz harabelerden ibaret olmasını tefekkür edersiniz. Celsus Kütüphanesi'nin önünde durup insan aklının ve bilgisinin kalıcılığını hissedersiniz. Şirince'nin yeşil tepeleri arasındaki eski Rum evlerinin sessizliği, geçmişteki ortak yaşamın ve kültürlerin manevi zenginliğini ruhunuza fısıldar.",
        "gastronomi": "- **Boyoz:** İzmir'in simgesi olan, sabahları fırından sıcak çıkan, haşlanmış yumurta eşliğindeki çıtır hamur işi.\n- **İzmir Kumrusu:** Nohut mayalı özel ekmek arasına şarküteri ürünleri ve İzmir tulumu konarak yapılan sandviç.\n- **Şambali:** İrmikli, şerbetli, üzeri fıstıklı ve tarçınlı geleneksel sokak tatlısı.",
        "landmarks": ["Tarihi Saat Kulesi", "Efes Antik Kenti (Selçuk)", "Kemeraltı Çarşısı", "Kordon Boyu", "Tarihi Asansör", "Şirince Köyü"]
    },
    "Agri": {
        "library": "Ağrı İl Halk Kütüphanesi - Soğuk Doğu ikliminde sıcak bir çalışma ortamı sunan, modern donanımlı kütüphane.",
        "hikmet": "Ağrı Dağı'nın bulutları aşan heybeti, insana kendi küçüklüğünü ve yaratıcının büyüklüğünü hatırlatan sessiz bir mabettir.",
        "quote": "\"Doğunun sınır çizgisinde, İshak Paşa Sarayı'nın masalsı silüetinin Ağrı Dağı'nın karlarıyla buluştuğu yüksek diyar.\"",
        "description": "Türkiye'nin ve Avrupa'nın en yüksek zirvesi olan Ağrı Dağı'nın adını taşıyan, sınırlerin ve karlı dağların şehri Ağrı. Doğubayazıt ilçesinde, sarp kayalıkların üzerine adeta bir kartal yuvası gibi kurulmuş olan 18. yüzyıl Osmanlı şaheseri İshak Paşa Sarayı, Türk mimarlık tarihinin en görkemli yapılarından biridir. Şehir, sert iklimine rağmen misafirperver insanları ve kadim tarihiyle dikkat çeker.",
        "sufi_notes": "İshak Paşa Sarayı'nın avlusunda durup aşağıdaki ovayı izlemek, dünyadaki krallıkların ve sarayların geçiciliğini, asıl kalıcı olanın ise sadece yaradanın yüceliği olduğunu derinden hissettirir. Ağrı Dağı'nın dumanlı zirvesine bakmak, dervişlerin manevi basamakları aşarak ulaştıkları o yüksek mertebeleri ve içsel zirveleri sembolize eder. Soğuk bozkır havası, zihni berraklaştıran ve içsel bir tefekküre davet eden bir atmosfere sahiptir.",
        "gastronomi": "- **Abdigör Köftesi:** Doğubayazıt yöresine ait, taş üzerinde tokmakla dövülerek yapılan çok lezzetli ve hafif köfte.\n- **Ağrı Halisesi:** Tandırda uzun süre pişen buğday ve kemiksiz etin dövülerek bulamaç haline getirilmesi.\n- **Kete:** Doğu Anadolu'nun geleneksel içli veya sade fırınlanmış hamur işi lezzeti.",
        "landmarks": ["İshak Paşa Sarayı", "Ağrı Dağı Milli Parkı", "Doğubayazıt Kalesi", "Meteor Çukuru", "Nuh'un Gemisi İzleri", "Diyadin Kaplıcaları"]
    },
    "Van": {
        "library": "Van İl Halk Kütüphanesi - Van Gölü'nün maviliği yakınlarında, ferah ve geniş çalışma salonlarıyla seyyah yazılımcılar için ideal.",
        "hikmet": "Van Gölü'nün turkuaz sularındaki Akdamar Kilisesi, farklı inançların aynı coğrafyada bıraktığı barışçıl izlerin nişanesidir.",
        "quote": "\"Urartuların kadim başkentinde, Van Denizi'nin turkuaz maviliğinde süzülen Akdamar Adası'nın efsunlu hikayesi.\"",
        "description": "Doğu Anadolu'nun en büyük gölü olan Van Gölü'nün (halk arasındaki adıyla Van Denizi) kıyısında kurulu, Urartuların tarihi başkenti Van. Akdamar Adası'ndaki tarihi kilisesi, sarp kayalıklar üzerine kurulu görkemli Van Kalesi, dünyaca ünlü Van Kedisi ve eşsiz kahvaltı kültürüyle Van, bölgenin en canlı ve kültürel açıdan en zengin şehridir.",
        "sufi_notes": "Akdamar Kilisesi'nin dış duvarlarındaki Tevrat ve İncil hikayelerini anlatan kabartmaları incelerken, insan elinin ve inancının taşa işlediği o asırlık estetiği tefekkür edersiniz. Van Gölü'nün sodalı, turkuaz sularında batan güneşi Van Kalesi'nden izlemek, Urartu krallarından bugüne geçen binlerce yıllık zamanın akıp gidişini ve insanoğlunun yeryüzündeki kısa yolculuğunu hissettirir.",
        "gastronomi": "- **Van Kahvaltısı:** Otlu peynirden murtuğaya, kavuttan süzme bala kadar onlarca çeşidin sunulduğu dünyaca ünlü kahvaltı.\n- **Sengser:** Kurutulmuş süzme yoğurt (kurut), yeşil mercimek ve kuzu etiyle yapılan yöresel lezzet.\n- **Keledoş:** Baklagiller, buğday, et ve kurut sosunun karıştırılarak yapıldığı tescilli Van yemeği.",
        "landmarks": ["Van Kalesi (Tuşpa)", "Akdamar Adası ve Kilisesi", "Van Kedisi Evi", "Muradiye Şelalesi", "Hoşap Kalesi", "Van Müzesi"]
    }
}

REGIONS_MAP = {
    "01_Marmara": ["Istanbul", "Kocaeli", "Bursa", "Canakkale"],
    "02_Ege": ["Denizli", "Mugla", "Izmir"],
    "03_Akdeniz": ["Antalya", "Adana", "Hatay", "Mersin", "Isparta"],
    "04_IcAnadolu": ["Ankara", "Konya", "Nevsehir", "Aksaray", "Eskisehir", "Sivas"],
    "05_Karadeniz": ["Amasya", "Corum", "Samsun", "Sinop", "Giresun", "Ordu", "Trabzon", "Artvin", "Bayburt", "Gumushane", "Rize"],
    "06_DoguAnadolu": ["Ardahan", "Elazig", "Erzincan", "Erzurum", "Kars", "Malatya", "Tunceli", "Agri", "Van"],
    "07_GuneydoguAnadolu": ["Mardin"]
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
            if clean_city == "Eskişehir": lookup_key = "Eskisehir"
            if clean_city == "Gümüşhane": lookup_key = "Gumushane"
            if clean_city == "Elazığ": lookup_key = "Elazig"
            
            if lookup_key in VISITED_DEEP_DETAILS:
                
                details = VISITED_DEEP_DETAILS[lookup_key]
                file_path = os.path.join(region, folder, "README.md")
                
                content = f"# 📍 {clean_city} - Seyahat ve Tefekkür Notları\n\n"
                
                banner_path = os.path.join(region, folder, "banner.jpg")
                if os.path.exists(banner_path):
                    content += f"![{clean_city} Manzarası](banner.jpg)\n\n"
                    
                content += f"## 📜 Şehrin Ruhu\n> \"{details['hikmet']}\"\n"
                content += f"> {details['quote']}\n\n"
                content += f"### 🌍 Şehrin Dokusu ve Hatırası\n{details['description']}\n\n"
                content += f"### 🕊️ Gezginin Not Defterinden (İçsel Düşünceler)\n{details['sufi_notes']}\n\n"
                
                if 'gastronomi' in details:
                    content += f"### 🍽️ Yöresel Lezzet Tavsiyeleri\n{details['gastronomi']}\n\n"
                
                content += "### ⛺ Konaklama ve Bütçe Stratejisi\n"
                content += "- **Sıfır Konaklama Maliyeti:** GSB Seyahatsever projesi kapsamında şehirdeki KYK yurtlarında 5 gün ücretsiz konaklanmıştır.\n"
                content += "- **Ulaşım Optimizasyonu:** Bir önceki ilden rotaya devam edilerek yol masrafı minimize edilmiştir.\n\n"
                content += "### 💻 Yarı Göçebe Mesaisi (Upskilling)\n"
                content += "- **Kütüphane Rutini:** Gündüzleri İl Halk Kütüphanesinde zaman geçirilerek yazılım projeleri geliştirilmiş ve eğitimlere devam edilmiştir.\n"
                if 'library' in details:
                    content += f"  * *Seyyahın Kütüphane Notu:* {details['library']}\n"
                content += "- **Şehri Sindirme:** Kalan vakitlerde şehrin tarihi ve kültürel dokusu acele etmeden, derinlemesine keşfedilmiştir.\n\n"
                content += "### ✨ Keşfedilesi Duraklar\nBu şehrin havasını solumak, ruhuna dokunmak için mutlaka adımlanması gereken köşe taşları:\n"
                
                for loc in details['landmarks']:
                    content += f"- [ ] **{loc}**\n"
                    
                content += "\n---\n*Bu il bizzat deneyimlenmiş, yolları aşındırılmış ve seyahatnameye sevgiyle işlenmiştir.* ✅\n"
                
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"Deeply enriched: {file_path}")

if __name__ == "__main__":
    enrich_visited()
