import requests

response = requests.get("https://www.youtube.com")

if response.status_code == 200:
    print("Succès ! Connexion établie avec YouTube (code 200)")

    print("\nType de contenu reçu :", response.headers['Content-Type'])
    print("\nExtrait des premiers 500 caractères de la page (HTML) :")
    print(response.text[:500])
    if "YouTube" in response.text:
        print("\n✓ La page contient bien le mot 'YouTube'")

else:
    print("Erreur :", response.status_code)
    print("Raison :", response.reason)