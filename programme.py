from employe import Employe
from technicien import Technicien

class Programme:
    def __init__(self):  
        self.listing_employe = []
        
    def ajouter_employe(self):    
        add = input("Souhaitez-vous ajouter un employé ? (O/N) : ")
        if add.upper() == "O":
            while True:
                nom = input("Saisir le nom du contact : ").casefold()      #demander à l'utilisateur de saisir le nom du contact
                if nom.isalpha():        #si le nom contient que des lettres 
                    print ("Nom valide : ", nom)        #afficher le nom valide
                    break
                else:
                    print("Nom invalide")       #si le nom ne contient pas que des lettres, ça affichera nom invalide 
            
            while True:        
                age = input("Saisir l'âge du contact : ")        #demander à l'utilisateur de saisir l'age de l'employé.
                if age.isdigit():         #si l'age de l'employé contient que des chiffres
                    print (f"{nom} a : {age} ans.")      #afficher le nom valide
                    break
                else:
                    print("Âge invalide")         #si le prénom ne contient pas que des lettres, ça affichera nom invalide 
            
            while True:
                salaire = int(input("Saisir le montant du salaire (annuel) : ")) #demander à l'utilisateur de saisir le salaire de l'employé.
                if int(salaire): # Verifie si c'est des chiffres uniquement
                    print(f"Le salaire de {nom} est de : {salaire} €")
                    break
                else:
                    print("Saisie du salaire invalide") 
            
            while True:
                n_secu = input("Saisir le numéro de sécurité sociale de l'employé : ") #demander à l'utilisateur de saisir le numéro de sécurité sociale de l'employé.
                if n_secu.isdigit() and len(n_secu) == 15: # Verifie si c'est des chiffres uniquement et si le numéro ne contient les 15 chiffres.
                    print(f"Le numéro de sécurité sociale de {nom} est : {n_secu} ")
                    break
                else:
                    print("Saisie du numéro de sécurité sociale doit contenir 15 chiffres.") 
                     
            mon_employe = Employe(nom, age, salaire, n_secu)
            
            rang = input(f"{nom} est également un technicien ? (O/N) : ").upper().strip()
            if rang == "O":
                while True:
                    grade = input("Saisir le grade du technicien : ").casefold()      #demander à l'utilisateur de saisir le nom du contact
                    if grade.isalpha():        #si le nom contient que des lettres 
                        print ("Grade valide : ", grade)        #afficher le nom valide
                        break
                    else:
                        print("Grade invalide") 
                        
                technicien = Technicien(nom, age, salaire, n_secu, grade) 
                self.listing_employe.append(technicien)
                print(f"L'employé {nom} a été ajouté à la liste des techniciens") 
                  
            else:
                print("Cet employé n'est pas un technicien.")
                self.listing_employe.append(mon_employe) #Ajoute l'employé à la liste
                print(f"L'employé {nom} a été ajouté avec succès à la liste des employés.") #afficher un message de confirmation
            
            self.afficher_listing()
        
    def supprimer_employe(self): #supprime un contact de la liste s'il est présent
        self.afficher_listing()
        delete_employe = input("Saisir le nom de l'employé à supprimer de la liste : ").strip()
        trouve = False
        for emp in self.listing_employe:
            if emp.nom == delete_employe:
                reponse = input("Souhaitez-vous supprimer définitivement l'employé ? (O/N): ").upper()
                if reponse == "O":
                    self.listing_employe.remove(emp)
                    trouve = True
                    print(f"Le contact {delete_employe} a été supprimé.")
                    break
        
    
    def afficher_listing(self): #affiche la liste des employés et techniciens
        if not self.listing_employe:
            print("Aucun employé n'est enregistré")
        else:
            for i, employe in enumerate(self.listing_employe):
                print(f"{i + 1}. {employe.afficher()}" , "")
                
    def augmentation(self):
        if len(self.listing_employe) <= 0:
            print("Il n'y a aucun employé dans la liste")    
        else:
            aug = input("Souhaites-tu attribuer une augmentation à un employé ? (O/N) : ") #demander à l'utilisateur s'il veut modifier un contact
            if aug.upper() == "O":
                self.afficher_listing()       
                try:
                    select_employe = int(input("Quel employé souhaites-tu augmenter ? : "))-1
                    
                    if select_employe < 0 or select_employe >= len(self.listing_employe): #Si le nb saisi par l'utilisateur n'est pas entre  et la longueur de la liste
                        print(f"La selection est invalide, la selection est comprise entre 0 et", len(self.listing_employe))
                        return
                    else:
                        employe_choisi = self.listing_employe[select_employe]
                        employe_choisi.augmentation()
                        
                
                except ValueError: #Si la saisie inclue une erreur
                    print("Merci de saisir un element valide!")                  
            else:
                print("Pas de modification souhaitée")
            
                return self.menu
    
    def menu(self): #definir la fonction menu
        print("///// MENU /////") # affiche le menu 
        while True:
            try:
                choix = int(input("Quel choix souhaitez-vous faire ? 1. Ajouter un employé, 2. Afficher la liste des employés, 3. Augmenter un employé ,  4. Supprimer un employé : "))
                if choix <= 0 or choix >= 4:
                    print("Le choix est incorrect. Veuillez saisir une des 4 options proposées")          
                if choix == 1:
                    self.ajouter_employe()        
                if choix == 2:
                    self.afficher_listing()                     
                if choix == 3:
                    self.augmentation()
                if choix == 4:
                  self.supprimer_employe()
                    
            except ValueError:
                print("Saisie invalide. Veuillez reessayer")    
                
                
programme = Programme()
programme.menu()