import os
import re
from icrawler.builtin import BingImageCrawler

data_marques = {
    "BMW": {
        "Série 1": [
            "E81/E82/E87/E88",
            "F20/F21",
            "F40",
            "F70"
        ],
        "Série 3": [
            "E21",
            "E30",
            "E36",
            "E46",
            "E90/E91/E92/E93",
            "F30/F31/F34",
            "G20/G21"
        ],
        "Série 5": [
            "E12",
            "E28",
            "E34",
            "E39",
            "E60/E61",
            "F10/F11/F07",
            "G30/G31",
            "G60/G61"
        ],
        "Série 7": [
            "E23",
            "E32",
            "E38",
            "E65/E66",
            "F01/F02",
            "G11/G12",
            "G70"
        ],
        "X3": [
            "E83",
            "F25",
            "G01",
            "G45"
        ],
        "X5": [
            "E53",
            "E70",
            "F15",
            "G05"
        ],
        "Z4": [
            "E85/E86",
            "E89",
            "G29"
        ]
    },
    "Mercedes-Benz": {
        "Classe A": [
            "W168",
            "W169",
            "W176",
            "W177"
        ],
        "Classe C": [
            "W201 - 190",
            "W202",
            "W203",
            "W204",
            "W205",
            "W206"
        ],
        "Classe E": [
            "W123",
            "W124",
            "W210",
            "W211",
            "W212",
            "W213",
            "W214"
        ],
        "Classe S": [
            "W116",
            "W126",
            "W140",
            "W220",
            "W221",
            "W222",
            "W223"
        ],
        "Classe G": [
            "W460 / W461",
            "W463",
            "W463 Type 464"
        ],
        "Classe SL": [
            "R107",
            "R129",
            "R230",
            "R231",
            "R232"
        ],
        "GLC": [
            "X253",
            "X254"
        ]
    }
}

NOMBRE_IMAGES_MAX = 300
DOSSIER_RACINE = "dataset_voitures"

VARIANTES_REQUETES = [
    "{marque} {modele} {gen} car exterior",
    "{marque} {modele} {gen} front view",
    "{marque} {modele} {gen} side view",
]

def scraper_images():
    for marque, modeles in data_marques.items():
        for modele, generations in modeles.items():
            for gen in generations:
                nom_brut = f"{marque}_{modele}_{gen}"
                dossier_classe = re.sub(r'[\s/\\:*?"<>|]+', '_', nom_brut)
                chemin_complet = os.path.join(DOSSIER_RACINE, dossier_classe)
                os.makedirs(chemin_complet, exist_ok=True)

                print(f"\nLancement du scraping : {marque} {modele} {gen}")
                print(f"Dossier : {chemin_complet}")

                for template in VARIANTES_REQUETES:
                    requete = template.format(marque=marque, modele=modele, gen=gen)
                    print(f"  Requete : {requete}")
                    try:
                        crawler = BingImageCrawler(storage={'root_dir': chemin_complet})
                        crawler.crawl(keyword=requete, max_num=NOMBRE_IMAGES_MAX // len(VARIANTES_REQUETES))
                    except Exception as e:
                        print(f"  Erreur pour '{requete}' : {e}")

if __name__ == "__main__":
    print("Demarrage de la collecte du dataset...")
    scraper_images()
    print("\nScraping termine.")