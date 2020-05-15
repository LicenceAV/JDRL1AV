from Character import character,enemies,nymphess
from fight import fight
import time

class tuto:
    def tuto1(self):
        time.sleep(2)
        print("\nBienvenue dans le tutoriel spécialisé pour le combat."+\
               "\nTu apprendras ici comment te battre, ce qu'il se passe quand tu te bats,"
               "et tous les rouages utiles au jeu.")
        input("Appuyez sur 'Entrée' pour commencer.")
        self.ename=enemies.randname(self)
        self.estat=[100,10,15]
        self.stat=[100,10,15,100]
        self.save=self.stat.copy()
        print("Lors de ton aventure tu seras amené à combatre des énemis, toujours plus corriaces"
              "\nVoici ton énnemi:", self.ename)
        enemies.affstat(self)
        
        print("\nTon but est de l'éliminer pour continuer ton aventure."+\
              "\nPour ce faire, tu peux l'attaquer !")
        input("Attaque ! (a) ")
        print("\nBravo, tu retire 10pv à ton adversaire. Mais il t'attaque aussi !"+\
              "\nTu perds 5pv."+\
              "\nToute attaque que tu portes te fais perdre de l'endurance, veille à ne pas être trop bas,"+\
              "tu risques de ne plus pouvoir attaquer.")
        self.estat=[85,10,15]
        self.stat=[90,10,15,95]
        character.affstat(self)
        enemies.affstat(self)
        input("Appuyez sur 'Entrée' pour continuer.")

        
        print("\nTu te débrouille bien, mais il faut que tu saches que tes dégats sont variables."+\
              "\nTu as, dans tes statistiques, un dés à 12 faces représentant ton attaque."+\
              "\nTes dégats sont le résultat de l'addition de ta valeur d'attaque et du résultat du dès." )
        input("Attaque de nouveau ! (a) ")
        print("\nC'est un coup critique ! Tu lances ton dés d'attaque deux fois, pour plus de dégats potentiels."+\
              "\nCa te permet de faire 25 de dégats."+\
              "\nMais ton énnemi se défend, il ne te fais pas de dégats et réduits les coups que tu lui portes."+\
              "\nTu lui enlèves donc 10pv.")
        self.estat=[75,10,15]
        self.stat=[90,10,15,85]
        character.affstat(self)
        enemies.affstat(self)
        input("Appuyez sur 'Entrée' pour continuer.")
        
        print("Toi aussi tu peux te défendre, essaye donc :")
        input("Défend-toi (d) ")
        print("Peu importe ce que ferra ton adversaire, les dommages subit seront dimminués."+\
              "Mais dans ce cas, il se  défend aussi."+\
              "Le fait de ne pas avoir attaqué te fait reprendre de l'énergie.")
        self.estat=[75,10,15]
        self.stat=[90,10,15,100]
        character.affstat(self)
        enemies.affstat(self)
        input("Appuyez sur 'Entrée' pour continuer.")
        
        print("Tu ne sais jamais ce que peux faire l'énnemi à l'avance, tiens toi prêt à tout."
              "\nDe plus, tu peux également louper ton coup...")
        input("Attaque donc ton adversaire pour gagner (a) ")
        print("\nVous faites tous les deux la même chose, mais tu rates ton coup..."
              " En plus de te louper tu tombe et te fait mal."
              "\nIl faudra apprendre à faire plus attention.")
        self.estat=[75,10,15]
        self.stat=[75,10,15,85]
        character.affstat(self)
        enemies.affstat(self)
        input("Appuyez sur 'Entrée' pour continuer.")
        
        print("\nAu cours de l'histoire tu pourras posséder des objets diverses, voici leurs caractéristiques:"
              "\n  - Bombe / explosif : Tue l'énnemi mais te fait des dégats"
              "\n  - Potion de vie: Redonne 35pv"
              "\n  - Potion d'endurance: restore ton endurance"
              "\n  - Potion de force: Double ta force pour le combat en cours"
              "\n  - Couteau de lancer / surin: fait 30 points de dégats sur l'adversaire à coup sûr"
              "\n  - Bibelot magique: peut ne rien faire, restaurer ton énergie ou restaurer tes pv")
        
        input("Tu as actuellement un surin, utilise le !"
               "\nUtilise ton objet : (o) ")
        
        print("Ton énnemi perds donc 30pv."
              "\nMais il t'attaque, tu perds donc 21pv.")

        self.estat=[45,10,15]
        self.stat=[54,10,15,85]
        character.affstat(self)
        enemies.affstat(self)
        input("Appuyez sur 'Entrée' pour continuer.")
         
        input("\nTu dois encore apprendre une chose, tu auras un pouvoir spécial, reçu des Dieux. "
               "Mais fais attention, tu n'en as que 3..."
               "\nEssaye de le maîtriser. (spe) ")
        print("\nCette attaque réduit en poussière ton adveraire en fonction de la difficulté de jeu choisie."
              "\n\nTon adversaire est donc mort." )
        input("Appuyez sur 'Entrée' pour continuer.")
        
        print("\nBien ! Maintenant que tu as compris, essaye de t'en sortir face à un vrai adversaire.")
        
        character.__init__(self, pv=100, attack=20, armor=15, endurance=100,xp=0,lvl=0,obj=['surin','bibelot magique', "potion d'endurance"],aface=12,spe=' ',credit=1500)
        enemies.myenemi(self)
        self.tech=['crochet du droit','crochet du gauche','uppercut','gifle']
        self.stat=[100,20,15,100]
        self.name='Joueur 1'
        fight.fight(self)
        
        print("\nVoilà, tu as désormais fini le tutoriel."
              "\nJe te souhaite une agréable expérience de jeu.")
    
    def tuto2(self):
        time.sleep(2)
        print("\nBienvenue dans ce tutoriel réservé aux marchands, dénommés nymphes.")
        input("Appuyez sur 'Entrée' pour commencer.")
        
        print("\nLes nymphes apparaiteront aléatoirement après les combats, et il en existe plusieurs types:"
              "\n    - L'herboriste : vend des potions en tout genres"
              "\n    - Le voyageur : t'offre un objet aléatoire"
              "\n    - La forgeronne : vend des armes et des objets offensifs"
              "\n    - La magicienne : te vend quelques potions et objets magiques"
              "\n    - La joueuse : te proposera de jouer à un jeu, si tu gagnes, tu seras récompensé.")
        
        character.__init__(self, pv=100, attack=20, armor=15, endurance=100,xp=0,lvl=0,obj=['surin','bibelot magique', "potion d'endurance"],aface=12,spe=' ',credit=1500)
        
        input("Appuyez sur 'Entrée' pour continuer.")
        print("\nEn début de partie tu as directement {} crédits".format(self.credits)+\
              "\nCes crédits sont a monaie du Jeu, et tu en gagne pour chaque énnemi vaincu."
              "\n\nPour lui acheter un objet il te suffiera de lui demander en toute lettre quand tu y serras convié."
              " Mais si tu ne veux rien lui acheter il te suffit de lui répondre 'rien'."
              "\nVoici un exemple de nymphes :")
        input("Es-tu prêt ?")
        nymphess.yes(self)
        
        input("\nJ'espère que tu as bien compris le fonctionnement de cette partie du gameplay !"
              "Amuse-toi bien sur ce JDR."
              "\n\nAppuyez sur 'Entrée' pour terminer ce tutoriel.")

if __name__=='__main__':
    A=pif()