def card(kk, ru, en):
    return {"kk": kk, "ru": ru, "en": en}


def base_card(title_kk, title_ru, title_en, sample_type_kk, sample_type_ru, sample_type_en,
              formula, color_kk, color_ru, color_en, hardness, luster_kk, luster_ru, luster_en,
              cleavage_kk, cleavage_ru, cleavage_en, fracture_kk, fracture_ru, fracture_en,
              system_kk, system_ru, system_en, desc_kk, desc_ru, desc_en):
    return card(
        {
            "title": title_kk,
            "type": sample_type_kk,
            "color": color_kk,
            "formula": formula,
            "luster": luster_kk,
            "hardness": hardness,
            "cleavage": cleavage_kk,
            "fracture": fracture_kk,
            "crystal_system": system_kk,
            "description": desc_kk,
            "origin": "Табиғи геологиялық процестер нәтижесінде түзіледі.",
            "uses": "Музей коллекцияларында, оқу және ғылыми мақсатта қолданылады.",
            "deposits": ["Қазақстан", "Ресей", "Қытай", "АҚШ"],
            "interesting_facts": ["Әр үлгінің түсі мен құрылымы түзілу жағдайына байланысты өзгереді."]
        },
        {
            "title": title_ru,
            "type": sample_type_ru,
            "color": color_ru,
            "formula": formula,
            "luster": luster_ru,
            "hardness": hardness,
            "cleavage": cleavage_ru,
            "fracture": fracture_ru,
            "crystal_system": system_ru,
            "description": desc_ru,
            "origin": "Образуется в результате природных геологических процессов.",
            "uses": "Используется в музейных коллекциях, обучении и научных целях.",
            "deposits": ["Казахстан", "Россия", "Китай", "США"],
            "interesting_facts": ["Цвет и структура образца зависят от условий его образования."]
        },
        {
            "title": title_en,
            "type": sample_type_en,
            "color": color_en,
            "formula": formula,
            "luster": luster_en,
            "hardness": hardness,
            "cleavage": cleavage_en,
            "fracture": fracture_en,
            "crystal_system": system_en,
            "description": desc_en,
            "origin": "Forms through natural geological processes.",
            "uses": "Used in museum collections, education, and scientific study.",
            "deposits": ["Kazakhstan", "Russia", "China", "USA"],
            "interesting_facts": ["Colour and texture depend on formation conditions."]
        },
    )


MINERALS = {
    "biotite": base_card(
        "Биотит", "Биотит", "Biotite",
        "Слюда минералы", "Минерал группы слюд", "Mica group mineral",
        "K(Mg,Fe)₃AlSi₃O₁₀(F,OH)₂",
        "қара, қоңыр, қою жасыл", "чёрный, коричневый, тёмно-зелёный", "black, brown, dark green",
        "2.5–3", "шыны, інжу тәрізді", "стеклянный, перламутровый", "vitreous, pearly",
        "өте жақсы", "совершенная", "perfect",
        "тегіс емес", "неровный", "uneven",
        "моноклиндік", "моноклинная", "monoclinic",
        "Биотит — магмалық және метаморфтық жыныстарда жиі кездесетін қара түсті слюда.",
        "Биотит — тёмная слюда, распространённая в магматических и метаморфических породах.",
        "Biotite is a dark mica common in igneous and metamorphic rocks."
    ),

    "granite": base_card(
        "Гранит", "Гранит", "Granite",
        "Магмалық тау жынысы", "Магматическая горная порода", "Igneous rock",
        "Кварц + дала шпаты + слюда",
        "сұр, қызғылт, ақ", "серый, розовый, белый", "gray, pink, white",
        "6–7", "әлсіз шыны тәрізді", "слабый стеклянный", "weak vitreous",
        "жоқ", "отсутствует", "none",
        "түйіршікті", "зернистый", "granular",
        "аралас кристалдық құрылым", "смешанная структура", "mixed crystalline structure",
        "Гранит — жер қыртысында кең таралған берік магмалық тау жынысы.",
        "Гранит — широко распространённая прочная магматическая горная порода.",
        "Granite is a common durable igneous rock."
    ),

    "obsidian": base_card(
        "Обсидиан", "Обсидиан", "Obsidian",
        "Вулкандық шыны", "Вулканическое стекло", "Volcanic glass",
        "SiO₂-ге бай табиғи вулкандық шыны",
        "қара, қоңыр, қою сұр", "чёрный, коричневый, тёмно-серый", "black, brown, dark gray",
        "5–5.5", "шыны тәрізді", "стеклянный", "vitreous",
        "жоқ", "отсутствует", "none",
        "қабыршақты, конхоидальды", "раковистый", "conchoidal",
        "аморфты", "аморфная", "amorphous",
        "Обсидиан — лаваның тез суынуынан түзілетін табиғи вулкандық шыны.",
        "Обсидиан — природное вулканическое стекло, образующееся при быстром охлаждении лавы.",
        "Obsidian is natural volcanic glass formed by rapid cooling of lava."
    ),

    "agate": base_card(
        "Агат", "Агат", "Agate",
        "Халцедон түрі", "Разновидность халцедона", "Variety of chalcedony",
        "SiO₂",
        "жолақты, сұр, ақ, қоңыр, қызыл", "полосчатый, серый, белый, бурый, красный", "banded, gray, white, brown, red",
        "6.5–7", "балауыз тәрізді", "восковой", "waxy",
        "жоқ", "отсутствует", "none",
        "қабыршақты", "раковистый", "conchoidal",
        "тригональды", "тригональная", "trigonal",
        "Агат — түрлі түсті қабаттарымен ерекшеленетін халцедон түрі.",
        "Агат — разновидность халцедона, отличающаяся полосчатым рисунком.",
        "Agate is a banded variety of chalcedony."
    ),

    "fluorite": base_card(
        "Флюорит", "Флюорит", "Fluorite",
        "Минерал", "Минерал", "Mineral",
        "CaF₂",
        "күлгін, жасыл, сары, түссіз", "фиолетовый, зелёный, жёлтый, бесцветный", "purple, green, yellow, colourless",
        "4", "шыны тәрізді", "стеклянный", "vitreous",
        "өте жақсы", "совершенная", "perfect",
        "тегіс емес", "неровный", "uneven",
        "кубтық", "кубическая", "cubic",
        "Флюорит — түсі әртүрлі кальций фториді минералы.",
        "Флюорит — цветной минерал фторида кальция.",
        "Fluorite is a colourful calcium fluoride mineral."
    ),

    "pyrite": base_card(
        "Пирит", "Пирит", "Pyrite",
        "Сульфид минералы", "Сульфидный минерал", "Sulfide mineral",
        "FeS₂",
        "жез-сары", "латунно-жёлтый", "brass-yellow",
        "6–6.5", "металдық", "металлический", "metallic",
        "нашар", "несовершенная", "poor",
        "тегіс емес", "неровный", "uneven",
        "кубтық", "кубическая", "cubic",
        "Пирит — алтынға ұқсас жылтыр сульфид минералы.",
        "Пирит — блестящий сульфидный минерал, похожий на золото.",
        "Pyrite is a shiny sulfide mineral often mistaken for gold."
    ),

    "azurite": base_card(
        "Азурит", "Азурит", "Azurite",
        "Карбонат минералы", "Карбонатный минерал", "Carbonate mineral",
        "Cu₃(CO₃)₂(OH)₂",
        "көк, қою көк", "синий, тёмно-синий", "blue, deep blue",
        "3.5–4", "шыны тәрізді", "стеклянный", "vitreous",
        "жақсы", "хорошая", "good",
        "қабыршақты", "раковистый", "conchoidal",
        "моноклиндік", "моноклинная", "monoclinic",
        "Азурит — мыс кен орындарында кездесетін ашық көк минерал.",
        "Азурит — ярко-синий минерал, встречающийся в медных месторождениях.",
        "Azurite is a deep blue copper carbonate mineral."
    ),

    "chalcopyrite": base_card(
        "Халькопирит", "Халькопирит", "Chalcopyrite",
        "Сульфид минералы", "Сульфидный минерал", "Sulfide mineral",
        "CuFeS₂",
        "жез-сары", "латунно-жёлтый", "brass-yellow",
        "3.5–4", "металдық", "металлический", "metallic",
        "нашар", "несовершенная", "poor",
        "тегіс емес", "неровный", "uneven",
        "тетрагональды", "тетрагональная", "tetragonal",
        "Халькопирит — мыс өндіруде маңызды минерал.",
        "Халькопирит — важный минерал медных руд.",
        "Chalcopyrite is an important copper ore mineral."
    ),

    "basalt": base_card(
        "Базальт", "Базальт", "Basalt",
        "Вулкандық тау жынысы", "Вулканическая горная порода", "Volcanic rock",
        "Негізгі құрам: плагиоклаз + пироксен",
        "қара, қою сұр", "чёрный, тёмно-серый", "black, dark gray",
        "5–6", "күңгірт", "матовый", "dull",
        "жоқ", "отсутствует", "none",
        "тегіс емес", "неровный", "uneven",
        "ұсақ түйірлі құрылым", "мелкозернистая структура", "fine-grained structure",
        "Базальт — лаваның жер бетінде суынуынан түзілетін тау жынысы.",
        "Базальт — вулканическая порода, образующаяся при застывании лавы.",
        "Basalt is a volcanic rock formed from cooled lava."
    ),

    "opal": base_card(
        "Опал", "Опал", "Opal",
        "Аморфты кремнезем", "Аморфный кремнезём", "Amorphous silica",
        "SiO₂·nH₂O",
        "ақ, көкшіл, сары, түрлі түсті", "белый, голубоватый, жёлтый, разноцветный", "white, bluish, yellow, multicolour",
        "5.5–6.5", "шыны, балауыз тәрізді", "стеклянный, восковой", "vitreous, waxy",
        "жоқ", "отсутствует", "none",
        "қабыршақты", "раковистый", "conchoidal",
        "аморфты", "аморфная", "amorphous",
        "Опал — құрамында суы бар аморфты кремнезем.",
        "Опал — аморфный кремнезём с содержанием воды.",
        "Opal is hydrated amorphous silica."
    ),

    "hematite": base_card(
        "Гематит", "Гематит", "Hematite",
        "Темір оксиді", "Оксид железа", "Iron oxide",
        "Fe₂O₃",
        "қызыл-қоңыр, қара, болат-сұр", "красно-бурый, чёрный, стально-серый", "reddish brown, black, steel gray",
        "5.5–6.5", "металдық, күңгірт", "металлический, матовый", "metallic, dull",
        "жоқ", "отсутствует", "none",
        "тегіс емес", "неровный", "uneven",
        "тригональды", "тригональная", "trigonal",
        "Гематит — темірдің маңызды кен минералы.",
        "Гематит — важный рудный минерал железа.",
        "Hematite is an important iron ore mineral."
    ),

    "jadeite": base_card(
        "Жадеит", "Жадеит", "Jadeite",
        "Пироксен минералы", "Минерал группы пироксенов", "Pyroxene mineral",
        "NaAlSi₂O₆",
        "жасыл, ақ, сұр", "зелёный, белый, серый", "green, white, gray",
        "6.5–7", "шыны тәрізді", "стеклянный", "vitreous",
        "жақсы", "хорошая", "good",
        "түйіршікті", "занозистый, неровный", "splintery, uneven",
        "моноклиндік", "моноклинная", "monoclinic",
        "Жадеит — нефритпен бірге «жад» тастарына жататын бағалы минерал.",
        "Жадеит — ценный минерал, относящийся к группе жадовых камней.",
        "Jadeite is a valuable jade mineral."
    ),

    "native_copper": base_card(
        "Таза мыс", "Самородная медь", "Native copper",
        "Таза элемент", "Самородный элемент", "Native element",
        "Cu",
        "мыс-қызыл", "медно-красный", "copper-red",
        "2.5–3", "металдық", "металлический", "metallic",
        "жоқ", "отсутствует", "none",
        "иілімді", "ковкий", "malleable",
        "кубтық", "кубическая", "cubic",
        "Таза мыс табиғатта металл күйінде кездеседі.",
        "Самородная медь встречается в природе в металлическом состоянии.",
        "Native copper occurs naturally as metallic copper."
    ),

    "sphalerite_chalcopyrite": base_card(
        "Сфалерит-халькопирит кені", "Сфалерит-халькопиритовая руда", "Sphalerite-chalcopyrite ore",
        "Полиметалл кен ассоциациясы", "Полиметаллическая рудная ассоциация", "Polymetallic ore association",
        "ZnS + CuFeS₂",
        "қою сұр, жез-сары, қоңыр", "тёмно-серый, латунно-жёлтый, бурый", "dark gray, brass-yellow, brown",
        "3.5–4", "металдық, шайыр тәрізді", "металлический, смоляной", "metallic, resinous",
        "жақсы/нашар", "хорошая/слабая", "good/poor",
        "тегіс емес", "неровный", "uneven",
        "аралас", "смешанная", "mixed",
        "Сфалерит пен халькопириттің полиметалл кендеріндегі ассоциациясы.",
        "Ассоциация сфалерита и халькопирита в полиметаллических рудах.",
        "Association of sphalerite and chalcopyrite in polymetallic ores."
    ),
}