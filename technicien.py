from employe import Employe 

class Technicien(Employe):
    def __init__(self, nom, age, salaire, n_secu, grade):
          super().__init__(nom, age, salaire, n_secu)
          self.grade = grade.upper()
          
          
    def grade(self):
        add_grade = input("Merci de saisir un grade (A/B/C) : ").strip().upper()
        if add_grade == ("A", "B", "C") and len(add_grade) < 2:
            self.grade = add_grade
        else:
            print("Saisie invalide. Le grade doit correspondre à A, B ou C")
        
    def primes(self):
            prime = {"A" : 300, "B" : 200, "C" : 100}
            return prime.get(self.grade, 0)
           
            # if self.grade == "A":
            #         primes = 300
            #         break
            # elif self.grade == "B":
            #         primes = 200
            #         return
            #         break
            # elif self.grade == "C":
            #         primes = 100
            #         break
            # else:
            #     print("Saisie invalide. Le grade doit correspondre à A, B ou C")
        
        # print(f"Primes : {primes} €")
    
    def afficher_grade(self):
        return(f"Grade : {self.grade}")
      
    def afficher(self):
        return Employe.afficher(self) + ", " + self.afficher_grade() +", Primes : " + str(self.primes()) + "€"
          
        
    # def calcul_salaire(self): 
    #     Employe.calcul_salaire()
        
        

    
            
    
        
        


        