import random 

def word_to_guess():
    return random.choice(["Accueillir", "Fraise", "Myrtille", "Pomme"]).lower()

word = word_to_guess()

mot_devine = ["_"] * len(word)

# Permet d'afficher le résultat

def afficher_underscore(lettre:str, word:str):
    for i in range(len(word)):
        if word[i] == lettre:
            mot_devine[i] = lettre
    print(" ".join(mot_devine))

# Recupère lettre utilisateur
def letter():
    return input("Choisissez une lettre à deviner ").lower() 


# Défini si une lettre est présente dans le mot
def presence_lettre(lettre, word):
    if lettre in word:
        return True
    return False

def play():
    isfinish = False
    nombre_essai_maximal = 10
    while not isfinish and nombre_essai_maximal > 0:
        lettre = letter()
        estPresent = presence_lettre(lettre, word)
        if estPresent:
            if "_" not in mot_devine or lettre == word:
                isfinish = True
                print('Bravo ! tu as trouvé ', word)
                break 
        else: 
            nombre_essai_maximal -= 1
            print("\n" f"Il vous reste {nombre_essai_maximal} essais")
        afficher_underscore(lettre, word)
    if not isfinish: print(f"Vous avez perdu. Le mot était {word}")
        
play()

