# -*- coding: utf-8 -*-
"""
Farmakoloji Pulse — ayarlar.

EN ÇOK BURAYI DÜZENLEYECEKSİN. Skorlamanın "gizli sosu" bu dosyadır:
hangi dergi kaç puan, hangi makale tipi öne çıkar, hangi bölüme düşer.

Dergi anahtarları PubMed'in NLM kısaltmalarıdır (ISOAbbreviation ile eşleşir).
"""

# --------------------------------------------------------------------------
# DERGİLER ve TIER'LARI  (farmakoloji / farmasötik bilimler)
# Tier 1 = bayrak/üst düzey, Tier 2 = güçlü uzmanlık, Tier 3 = geniş/bölgesel
# --------------------------------------------------------------------------
JOURNAL_TIERS = {
    # --- Tier 1 ---
    "Nat Rev Drug Discov": 1,
    "Pharmacol Rev": 1,
    "Pharmacol Ther": 1,
    "Trends Pharmacol Sci": 1,
    "Acta Pharm Sin B": 1,
    "Drug Resist Updat": 1,
    "Adv Drug Deliv Rev": 1,
    "Br J Pharmacol": 1,
    "Pharmacol Res": 1,
    "Clin Pharmacol Ther": 1,
    "J Control Release": 1,
    "Phytomedicine": 1,
    "Drugs": 1,
    "Arch Toxicol": 1,

    # --- Tier 2 ---
    "Eur J Pharmacol": 2,
    "Biochem Pharmacol": 2,
    "Br J Clin Pharmacol": 2,
    "Clin Pharmacokinet": 2,
    "Drug Metab Dispos": 2,
    "Mol Pharmacol": 2,
    "J Pharmacol Exp Ther": 2,
    "Eur J Pharm Sci": 2,
    "Int J Pharm": 2,
    "Pharmaceutics": 2,
    "Pharmaceuticals (Basel)": 2,
    "J Pharm Sci": 2,
    "Toxicol Appl Pharmacol": 2,
    "J Ethnopharmacol": 2,
    "Front Pharmacol": 2,
    "Naunyn Schmiedebergs Arch Pharmacol": 2,
    "Basic Clin Pharmacol Toxicol": 2,
    "Expert Opin Drug Deliv": 2,
    "Expert Opin Drug Metab Toxicol": 2,
    "Drug Deliv": 2,
    "Eur J Pharm Biopharm": 2,
    "Neuropharmacology": 2,
    "Psychopharmacology (Berl)": 2,
    "Biomed Pharmacother": 2,
    "Chem Biol Interact": 2,
    "Life Sci": 2,

    # --- Tier 3 ---
    "Fundam Clin Pharmacol": 3,
    "Regul Toxicol Pharmacol": 3,
    "CPT Pharmacometrics Syst Pharmacol": 3,
    "Pharmacol Biochem Behav": 3,
    "Pharmacol Rep": 3,
    "Curr Pharm Des": 3,
    "Drug Dev Ind Pharm": 3,
    "AAPS PharmSciTech": 3,
    "Daru": 3,
    "Turk J Pharm Sci": 3,
    "Saudi Pharm J": 3,
    "BMC Pharmacol Toxicol": 3,
    "J Clin Pharm Ther": 3,
    "Ann Pharmacother": 3,
    "Pharmacotherapy": 3,
    "Toxicol Lett": 3,
    "Xenobiotica": 3,
    "Iran J Pharm Res": 3,
}

# Tier başına temel puan
JOURNAL_TIER_WEIGHT = {1: 100, 2: 60, 3: 35}
DEFAULT_TIER = 3

# --------------------------------------------------------------------------
# DERGİ ETKİ FAKTÖRLERİ (yaklaşık JCR — "Best of 2026" sıralaması için, düzenlenebilir)
# --------------------------------------------------------------------------
JOURNAL_IF = {
    "Nat Rev Drug Discov": 60.8, "Pharmacol Rev": 19.3, "Drug Resist Updat": 15.0,
    "Acta Pharm Sin B": 14.0, "Drugs": 13.4, "Adv Drug Deliv Rev": 13.3,
    "Pharmacol Ther": 12.0, "Trends Pharmacol Sci": 11.0, "J Control Release": 10.5,
    "Pharmacol Res": 9.1, "Br J Pharmacol": 6.8, "Phytomedicine": 6.7,
    "Biomed Pharmacother": 6.5, "Clin Pharmacol Ther": 6.3, "Arch Toxicol": 6.1,
    "Drug Deliv": 6.0, "J Ethnopharmacol": 5.4, "Int J Pharm": 5.3,
    "Biochem Pharmacol": 5.3, "Pharmaceutics": 5.4, "Life Sci": 5.2,
    "Eur J Pharmacol": 5.0, "Expert Opin Drug Deliv": 5.0, "Pharmaceuticals (Basel)": 4.6,
    "Clin Pharmacokinet": 4.6, "Neuropharmacology": 4.6, "Eur J Pharm Sci": 4.5,
    "Eur J Pharm Biopharm": 4.5, "Front Pharmacol": 4.4, "Chem Biol Interact": 4.4,
    "Drug Metab Dispos": 4.0, "Expert Opin Drug Metab Toxicol": 4.0,
    "J Pharmacol Exp Ther": 3.9, "Toxicol Appl Pharmacol": 3.8, "CPT Pharmacometrics Syst Pharmacol": 3.7,
    "Mol Pharmacol": 3.5, "Psychopharmacology (Berl)": 3.5, "Br J Clin Pharmacol": 3.5,
    "J Pharm Sci": 3.3, "Pharmacol Biochem Behav": 3.3, "Naunyn Schmiedebergs Arch Pharmacol": 3.2,
    "Regul Toxicol Pharmacol": 3.2, "Pharmacol Rep": 3.0, "Curr Pharm Des": 3.0,
    "AAPS PharmSciTech": 3.0, "Ann Pharmacother": 3.0, "Pharmacotherapy": 3.0,
    "Toxicol Lett": 3.0, "Basic Clin Pharmacol Toxicol": 2.9, "Drug Dev Ind Pharm": 2.9,
    "BMC Pharmacol Toxicol": 2.7, "Daru": 2.5, "Fundam Clin Pharmacol": 2.4,
    "J Clin Pharm Ther": 2.1, "Turk J Pharm Sci": 1.8, "Saudi Pharm J": 3.5,
    "Xenobiotica": 1.5, "Iran J Pharm Res": 1.9,
}
DEFAULT_IF = 1.5
BEST_KEEP = 60

# --------------------------------------------------------------------------
# BÖLÜMLER (alt konu) — makaleler konuya göre gruplanır.
# Başlık + özet + dergi metninde anahtar kelime aramasıyla, SECTION_ORDER
# sırasıyla ilk eşleşen bölüm atanır (eşleşme yoksa "diger").
# --------------------------------------------------------------------------
SECTION_ORDER = [
    "klinik", "noro", "kardiyometabolik", "onko", "immuno",
    "antimikrobiyal", "toksikoloji", "dogal", "formulasyon", "kesif", "diger",
]

SECTION_LABELS = {
    "klinik": "Klinik Farmakoloji & Farmasötik Bakım",
    "noro": "Nöropsikofarmakoloji",
    "kardiyometabolik": "Kardiyovasküler & Metabolik",
    "onko": "Onkoloji & Antikanser",
    "immuno": "İmmün & İnflamasyon",
    "antimikrobiyal": "Antimikrobiyal & Enfeksiyon",
    "toksikoloji": "Toksikoloji",
    "dogal": "Doğal Ürünler & Fitoterapi",
    "formulasyon": "Farmasötik Teknoloji & İlaç Taşıma",
    "kesif": "İlaç Keşfi & Medisinal Kimya",
    "diger": "Diğer",
}

SECTION_KEYWORDS = {
    "klinik": ["clinical pharmacy", "klinik eczacılık", "pharmacokinet", "farmakokinet",
               "pharmacodynam", "pharmacovigilance", "farmakovijilans", "drug interaction",
               "ilaç etkileşim", "adherence", "uyunç", "therapeutic drug monitoring",
               "bioequivalence", "biyoeşdeğer", "dose optim", "prescrib", "reçete",
               "medication", "rational drug", "akılcı ilaç", "polypharmacy"],
    "noro": ["antidepress", "antipsychotic", "antipsikotik", "anxiolytic", "anksiyolitik",
             "depression", "depresyon", "anxiety", "anksiyete", "schizophren", "epilep",
             "seizure", "nöbet", "analgesi", "analjezi", " pain", "ağrı", "neuropath",
             "nöropati", "parkinson", "alzheimer", "dementia", "demans", "antinocicept",
             "morphine", "morfin", "opioid", "opiyat", "serotonin", "dopamin", "gaba",
             "migraine", "migren", "neuroprotect", "nöroprotekt", "antiepilept", "sedati"],
    "kardiyometabolik": ["cardiovascular", "kardiyovasküler", "hypertension", "hipertansiyon",
                         "antihypertens", "cardiac", "kardiyak", "myocard", "miyokard",
                         "atheroscler", "ateroskler", "diabet", "diyabet", "insulin", "insülin",
                         "antidiabet", "antidiyabet", "obesity", "obezite", "lipid", "cholesterol",
                         "kolesterol", "glucose", "glikoz", "heart failure", "kalp yetmez",
                         "coronary", "koroner", "vascular", "vasküler"],
    "onko": ["cancer", "kanser", "tumor", "tümör", "tumour", "antitumor", "anticancer",
             "antikanser", "antineoplastic", "carcinoma", "karsinom", "chemotherap", "kemoterapi",
             "cytotoxic", "sitotoksik", "apoptos", "apoptoz", "leukemia", "lösemi", "melanoma",
             "glioblastoma", "antiproliferat", "oncolog", "onkoloji"],
    "immuno": ["immun", "immün", "inflammat", "inflamas", "anti-inflammat", "antiinflamatuar",
               "autoimmune", "otoimmün", "cytokine", "sitokin", "arthritis", "artrit",
               "rheumatoid", "romatoid", "psorias", "colitis", "kolit", "allerg", "alerji",
               "macrophage", "makrofaj"],
    "antimikrobiyal": ["antibiotic", "antibiyotik", "antimicrobial", "antimikrobiyal",
                       "antibacterial", "antibakteriyel", "antiviral", "antifungal", "antifungic",
                       "infection", "enfeksiyon", "bacteri", "bakteri", "virus", "virüs",
                       "fungal", "mantar", "antiparasit", "antimalarial", "sepsis", "biofilm",
                       "biyofilm", "wound healing", "yara iyileş"],
    "toksikoloji": ["toxicity", "toksisite", "toxicolog", "toksikoloji", "hepatotoxic",
                    "hepatotoksik", "nephrotoxic", "nefrotoksik", "cardiotoxic", "kardiyotoksik",
                    "neurotoxic", "nörotoksik", "genotoxic", "genotoksik", "poisoning", "zehirlen",
                    "oxidative stress", "oksidatif stres", "ischemia", "iskemi", "reperfusion",
                    "reperfüzyon", "toxic effect"],
    "dogal": ["natural product", "doğal ürün", "herbal", "plant extract", "bitki ekstre",
              "phytochem", "fitokim", "ethnopharmacol", "etnofarmakol", "essential oil", "uçucu yağ",
              "flavonoid", "polyphenol", "polifenol", "medicinal plant", "tıbbi bitki",
              "phytotherap", "fitoterapi", "alkaloid", "saponin", "farmakognozi", "pharmacognos",
              "extract of", "hypericum", "berberis", "curcumin", "kurkumin"],
    "formulasyon": ["formulation", "formülasyon", "nanoparticle", "nanopartikül", "nanoemul",
                    "nanoemül", "drug delivery", "ilaç taşı", "controlled release", "kontrollü salım",
                    "sustained release", "bioavailability", "biyoyararlanım", "solubility",
                    "çözünürlük", "liposome", "lipozom", "microsphere", "mikroküre", "hydrogel",
                    "hidrojel", "transdermal", "buccal", "bukkal", "dissolution", "dissolüsyon",
                    "nanocarrier", "plga", "niosome", "spanlastic", "emulgel", "emüljel",
                    "nanostructured", "in vitro release"],
    "kesif": ["synthesis", "sentez", "derivative", "türev", "molecular docking", "moleküler doking",
              "in silico", "structure-activity", "yapı-etki", "qsar", "novel compound",
              "yeni bileşik", "schiff base", "schiff bazı", "pyrazol", "pirazol", "chalcone",
              "şalkon", "azole", "azol", "piperazin", "admet", "inhibitor design", "docking"],
}

# --------------------------------------------------------------------------
# MAKALE TİPİ AĞIRLIKLARI
# --------------------------------------------------------------------------
PUBTYPE_WEIGHTS = {
    "Meta-Analysis": 45,
    "Systematic Review": 40,
    "Practice Guideline": 38,
    "Guideline": 35,
    "Randomized Controlled Trial": 35,
    "Clinical Trial, Phase III": 30,
    "Multicenter Study": 18,
    "Clinical Trial": 15,
    "Validation Study": 12,
    "Review": 10,
    # cezalar
    "Case Reports": -15,
    "Editorial": -25,
    "Letter": -30,
    "Comment": -30,
    "Published Erratum": -100,
    "Retraction of Publication": -200,
}

RECENCY_PER_DAY = 2.0

# --------------------------------------------------------------------------
# ARAMA AYARLARI
# --------------------------------------------------------------------------
RELDATE_DAYS = 1
DATETYPE = "edat"
RETMAX = 300
EXTRA_TERMS = ""

TIER1_THRESHOLD = 110
TIER2_THRESHOLD = 80

# Dergi listesini sorgu için düz liste olarak çıkar
JOURNALS = list(JOURNAL_TIERS.keys())
