class Employe:
    def __init__(self, nom, age, salaire, n_secu):
        self.nom = nom
        self.age = age
        self.salaire = salaire
        self.n_secu = n_secu
            
    def afficher(self):
        return(f"Nom : {self.nom}, Age : {self.age}, Salaire : {self.salaire}€, Numero Securité Sociale : {self.n_secu}")
        
    def augmentation(self):
        combien = int(input("De combien souhaitez-vous augmenter votre employé ? : ").strip())
        if int(combien) <= 0:
            print("Merci de saisir un montant valide")
        else:    
            self.salaire += combien
            print(f"Le salaire a été augmenté de {combien} € ")
            print(f"Le nouveau salaire est maintenant à {self.salaire} €")
            return
        
        
        
    def calcul_salaire(self): 
        return self.salaire 
            