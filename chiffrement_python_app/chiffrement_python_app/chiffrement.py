"""
Module de chiffrement César et Vernam
"""

def chiffrer_chaine_cesar(chaine, clef):
    """Chiffre une chaîne avec l'algorithme César"""
    chainechiffre = ''
    etapes = []
    
    for eachcar in chaine:
        cipherd = int(((ord(eachcar) - 65 + int(clef)) % 26) + 65)
        lettre = chr(cipherd)
        etapes.append(f'{eachcar} → {lettre}')
        chainechiffre += lettre
    
    return chainechiffre, etapes


def dechiffrer_chaine_cesar(chaine, clef):
    """Déchiffre une chaîne avec l'algorithme César"""
    chainechiffre = ''
    etapes = []
    
    for eachcar in chaine:
        cipherd = int(((ord(eachcar) - 65 - int(clef)) % 26) + 65)
        lettre = chr(cipherd)
        etapes.append(f'{eachcar} → {lettre}')
        chainechiffre += lettre
    
    return chainechiffre, etapes


def vernam_chiffrement(texte, cle):
    """Chiffre une chaîne avec l'algorithme Vernam"""
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    texte_chiffre = ""
    etapes = []
    
    for i in range(len(texte)):
        lettre = texte[i]
        lettre_cle = cle[i]
        index_chiffre = alphabet.index(lettre)
        index_cle = alphabet.index(lettre_cle)
        index_resultat = (index_chiffre + index_cle) % 26
        resultat = alphabet[index_resultat]
        etapes.append(f'{lettre} + {lettre_cle} → {resultat}')
        texte_chiffre += resultat
    
    return texte_chiffre, etapes


def vernam_dechiffrement(texte_chiffre, cle):
    """Déchiffre une chaîne avec l'algorithme Vernam"""
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    texte_dechiffre = ""
    etapes = []
    
    for i in range(len(texte_chiffre)):
        lettre_chiffree = texte_chiffre[i]
        lettre_cle = cle[i]
        index_chiffre = alphabet.index(lettre_chiffree)
        index_cle = alphabet.index(lettre_cle)
        index_dechiffre = (index_chiffre - index_cle) % 26
        resultat = alphabet[index_dechiffre]
        etapes.append(f'{lettre_chiffree} - {lettre_cle} → {resultat}')
        texte_dechiffre += resultat
    
    return texte_dechiffre, etapes
