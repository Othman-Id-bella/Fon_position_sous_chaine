def position_sous_chaine(chaine, sous_chaine):
    return chaine.find(sous_chaine)

chaine = "Hello, world!"
sous_chaine = "world"
resultat = position_sous_chaine(chaine, sous_chaine)
print("Position de la sous-chaîne:", resultat)

