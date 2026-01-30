import pandas as pd
import matplotlib.pyplot as plt
import glob

fichiers = glob.glob("/var/log/sysstat/sar*") or glob.glob("/var/log/sa/sa*")
if not fichiers:
    print("Aucun fichier SAR trouvé")
    exit()

donnees = []
for f in sorted(fichiers):
    with open(f) as lignes:
        for ligne in lignes:
            champs = ligne.split()
            if len(champs) > 6 and ":" in champs[0] and "." in champs[-1]:
                try:
                    heure = champs[0]
                    idle = float(champs[-1])
                    donnees.append({"heure": heure, "idle": idle, "util": 100 - idle})
                except:
                    pass

if not donnees:
    print("Aucune donnée trouvée")
    exit()

df = pd.DataFrame(donnees)
df = df.groupby("heure").mean().reset_index()

plt.plot(df["heure"], df["util"], color="red", label="% utilisé")
plt.plot(df["heure"], df["idle"], color="green", label="% idle")
plt.title("Activité CPU")
plt.xlabel("Heure")
plt.ylabel("%")
plt.grid(True)
plt.legend()
plt.show()