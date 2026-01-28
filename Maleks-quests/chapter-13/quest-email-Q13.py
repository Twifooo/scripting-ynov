import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


email_expediteur = "votre_email@gmail.com"
mot_de_passe = "votre_mot_de_passe"
email_destinataire = "destinataire@example.com"

message = MIMEMultipart()
message['From'] = email_expediteur
message['To'] = email_destinataire
message['Subject'] = "Test Email Python"

corps = "Bonjour, ceci est un email de test envoye avec Python et smtplib."
message.attach(MIMEText(corps, 'plain'))

serveur = smtplib.SMTP('smtp.gmail.com', 587)
serveur.starttls()
serveur.login(email_expediteur, mot_de_passe)

texte = message.as_string()
serveur.sendmail(email_expediteur, email_destinataire, texte)

serveur.quit()

print("Email envoye avec succes!")
