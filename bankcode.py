
message="""Cet script vous permet de faire la conversion de pource en cm et vise-versa.\n"""
def convertir_pource_vers_cm(pources):
    """Convertir des pource en centimètre"""
    return pources*2.54
def convertir_cm_vers_pource(cm):
    """Conversion de cm en pource"""
    return cm*0.394
def demande_de_choisir_conversion():
    """Demande à utilisateur de choisir"""
    print("Choisir le type de conversion: ")
    print("1 - Pouces vers Centimètres (pouces → cm)")
    print("2 - Centimètres vers Pouces (cm → pouces)")
    print("Votre choix :")
    choix = int(input())
    return choix
def demande_la_valeur_de_conversion(unite_actuel,unite_final):
    """ Demander l'utilisateur d'entrer la valeur à convertie """
    valeur = float(input(f" Entrer la valeur en {unite_actuel} à convertie en {unite_final} :"))
    return valeur

def aficher_resultat(valeur_convertir,unite_final):
    """Afficher le resultat de la conversion """
    print(f"Le resultat de la conversion est :{valeur_convertir:.2f} {unite_final}")

def main():

    #Demande le type de conversion
    print(f"\n{message}")
    choix = demande_de_choisir_conversion()
    if choix == 1:
        pouces_vers_cm = demande_la_valeur_de_conversion("pources", "cm")
        cm=convertir_pource_vers_cm(pouces_vers_cm)
        aficher_resultat(cm,"cm")
    elif choix == 2:
        cm_ver_pource=demande_la_valeur_de_conversion("cm", "pources")
        pource=convertir_cm_vers_pource(cm_ver_pource)
        aficher_resultat(pource,"pources")
    else :
        print("Choix invalide, Veuillez entrer 1 ou 2 ")

if __name__ == "__main__":

    main()

