import smtplib
from email.mime.text import MIMEText

exp = "votre.email@gmail.com"
mdp = "votre-mot-de-passe-ou-app-password"
dest = "destinataire@example.com"

msg = MIMEText("Ceci est un test d'envoi depuis Python.")
msg["Subject"] = "Test email Python"
msg["From"] = exp
msg["To"] = dest

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as serveur:
    serveur.login(exp, mdp)
    serveur.send_message(msg)

print("Email envoyé")