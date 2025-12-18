import argparse

def traiter_resultats(resultats):
    print("Traitement en cours avec les arguments :")
    print(f"Entrée : {resultats['fichier']}")
    print(f"Mode verbeux : {resultats['verbeux']}")
    print(f"Nombre magique : {resultats['nombre']}")
    print("→ Tout est prêt !")


def main():
    # 1. Création du parser
    parser = argparse.ArgumentParser()

    # 2. Au moins 3 arguments différents avec aide
    parser.add_argument('fichier', type=str)
    parser.add_argument('-v', '--verbeux', action='store_true')
    parser.add_argument('--nombre', type=int, default=42)

    args = parser.parse_args()

    # 3. Stockage dans une variable + transmission à une autre fonction
    resultats_analyses = {
        'fichier': args.fichier,
        'verbeux': args.verbeux,
        'nombre': args.nombre
    }
    traiter_resultats(resultats_analyses)

if __name__ == "__main__":
    main()