#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 10:11:30 2020

@author: rcoppe
"""
"""
Voir pour mettre plusieures armes a disposition du joueur dans chaque classe (class_)
Faire des boucles if dasn mes input en autorisant le caractère '?' pour donner au joueuru plus d'info sur ce que ça va engendrer
"""
### JDR

from additions import additions
from JDRHangman import Hangman_game
import random as rd


class character(additions):
    
    """
    Cette classe comporte toutes les méthodes utile à la création du personnage principal.
        - méthode difficulty
        - méthode class_
        - méthode affstat
        - méthode lvl_up
    """
    
    def __init__(self, pv=100, attack=20, armor=15, endurance=100,xp=0,lvl=0,obj=[],aface=12,spe=' ',credit=1500):
        
        """
        Initialisation des statistique du personnage principal, qui seront amenées à évoluer.
            - Arguments : statistiques (pv, endurance, attaque, défense)
                          expérience (par défaut à 0)
                          Niveau (par défaut à 0)
                          Liste d'objet (par défaut vide)
                          Face de dés d'attaque (par défaut à 12)
                          Une attaque spéciale (par défaut vide)
                          Des crédits qui font office de monaie (par défaut à 1500)
        """
        
        additions.__init__(self)
        self.spe=spe
        self.uses=3
        self.pv=pv
        self.attack=attack
        self.armor=armor
        self.endurance=endurance
        self.xp=xp
        self.lvl=lvl
        self.obj=obj
        self.aface=aface
        self.graph=[]
        self.credits=credit
        
    def difficulty(self):
        
        """
        Méthode pour définir la difficulté du jeu en fonction du choix du joueur.
        Les statistiques initiales du joueur en seront modifiées.
        Il a 3 choix de difficultés : extrème (il est vraiment difficile de terminer le jeu)
                                      moyenne (Difficulté de jeu équilibrée)
                                      facile (Le jeu est assez facile à terminer)
        
        En cas de difficulté moyenne ou extrème, le joueur peut choisir son nom.
        """
        
        self.diff=input("\n1) Pan : Dieu de la nature, protecteur des bergers, en choisissant ce personnage le jeu serra en sa difficulté minimale.\n" +\
                   "\n2) Un Faune: Version Romaine des satyres, les Faunes sont bien plus adroits et malins que leurs comparses. La difficulté en choisissznt ce personnage serra définie comme moyenne.\n"+\
                   "\n3) Un Satyre: Bons à rien, les satyres sont des être très maladroits, la difficulté sera donc bien plus grande.\n" )
        if self.diff=='1':
            print("\nJe suis Pan, Dieu de la nature. Enchanté.")
            self.stat=[150,25,25,100]
            self.name='Pan'
            self.classe='Dieu mineur'
        elif self.diff=='2':
            self.name=input("Quel serra ton nom, jeune Faune ? ")
            print("\nJe suis un Faune, {}. Enchanté.".format(self.name))
            self.stat=[110,15,15,65]
            self.classe='Faune'
        else:
            self.name=input("Quel serra ton nom, jeune Satyre ? ")
            print("\nJe suis un Satyre, {}. Enchanté.".format(self.name))
            self.stat=[90,10,10,50]
            self.classe='Satyre'
            
    def class_(self):
        
        """
        Méthode définissant la classe du joueur et ses attaques possibles en fonction de sont choix d'arme.
        Les statistiques dépendent de l'arme choisie: 
            - L'arc : moins de vie / légère augmentation de l'attaque / un peu moins de défense / plus endurant
            - L'épée : plus de vie / plus d'attaque / moins d'armure / endurance moyenne
            - La relique : Beaucoup de vie / moins de défense / beaucoup d'endurance / attaque moyenne
        
        Pour chaque arme est définit des attaques (coup de corne et coup de sabot sont 2 attaques communes)
            - Flèche dans la poitrine, dans la jambe
            - Taille, estoc
            - Magie, coup de sceptre
        
        Une fois le choix fait on montre une image de l'arme voulue.
        """
        
        self.cl=input("Quelle arme t'est la plus familière ?\n"+\
              "\n1) L'arc"+\
              "\n2) L'épée"+\
              "\n3) La relique\n")
        
        if self.cl=='1': 
            self.stat[0]=self.stat[0]-15
            self.stat[1]=self.stat[1]+5
            self.stat[2]=self.stat[2]-5
            self.stat[3]=self.stat[3]+10
            self.tech=['Coup de sabot', 'Coup de corne','flèche dans la poitrine','flèche dans la jambe']
            print("\nVoici ton arme")
            additions.images('arc1.jpg')
            
            
        elif self.cl=='2':
            self.stat[2]=self.stat[2]-5
            self.stat[1]=self.stat[1]+10
            self.stat[0]=self.stat[0]+15
            self.tech=['Coup de sabot', 'Coup de corne', 'Taille', 'Estoc']
            print("\nVoici ton arme")
            additions.images('jdrepee3.jpg')
            
        else:
            self.stat[0]=self.stat[0]+20
            self.stat[2]=self.stat[2]-5
            self.stat[3]=self.stat[3]+20
            self.tech=['Coup de sabot', 'Coup de corne', 'Magie', 'Coup de sceptre']
            print("\nVoici ton arme")
            additions.images('magic2.jpg')
        self.save=self.stat.copy()
    
    def affstat(self):
        
        """
        Méthode d'affichage des statistiques du joueur.
        Utilisation de la fonction additions.barre() afin de visualiser la vie et l'endurance
        """
        print("\nTes statistiques actuelles sont :\n"+\
              "\n PV: {}".format(additions.barre(self,self.stat[0],self.save[0]))+\
              "\n Endurance: {}".format(additions.barre(self,self.stat[3], self.save[3]))+\
              "\n Attaque: {}".format(self.stat[1])+\
              "\n Défense: {}".format(self.stat[2]))
            
    def lvl_up(self):
        
        """
        Méthode définissant la succession d'affichage et d'action en cas d'augmentation de niveau.
        Ainsi que l'affichage d'une barre d'expérience si le joueur n'a pas assez d'expérience. 
        
        En cas d'augmentation de niveau, le joueur peut choisir d'augenter ses statistiques avec 10points:
            - Attaque : l'augmentation est limitée à 3 points pour l'équilibrage du jeu
            - PV : l'augmentation n'est pas limitée 
            - Défense : limité à 5 points
            - Endurance : Non limité
        Il est important de noter que le joueur ne peut augmenter chaque statistiques qu'une seule fois.
        Et cela pour éviter qu'il ne veuille augenter plusieur fois de 3 points sont attaque par exemple.
        Si il ne dépense pas tout ses points, il les perd.
        """
        
        if self.xp>500:
            self.xp=500
        print("\nRegarde, ton niveau d'expérience :")
        print(additions.barre(self,self.xp,500))
        if self.xp>=500:
            print("\nBravo ! Tu viens de passer du niveau {} à {} !".format(self.lvl, self.lvl+1))
            self.xp=0
            self.lvl=self.lvl+1
            x=10
            p=m=n=k=h=e=j=1
            while x>0 and j==1:
                a=input("Vous avez {} points de statistiques suppémentaires, que voulez vous augmenter ? \n".format(x)+\
                      "L'attaque (a), la défense (d), ton endurance (e), ou tes points de vie (pv)")
                if p==0 and m==0 and n==0 and k==0:
                    j=0
                if a=='a' and p==1:
                    while e==1:
                        b=int(input("Combien de points veux-tu y attribuer ?"))
                        if b<=3:
                            self.stat[1]=self.stat[1]+b
                            self.save[1]=self.save[1]+b
                            e=p=0
                            x=x-b
                        else:
                            print("Tu ne peux pas devenir si fort si vite, le maximum attribuable est de 3")
                    
                elif a=='d' and m==1:
                    while h==1:
                        b=int(input("Combien de points veux-tu y attribuer ?"))
                        if b<=5:
                            self.stat[2]=self.stat[2]+b
                            self.save[2]=self.save[2]+b
                            h=m=0
                            x=x-b
                        else:
                            print("Tu ne peux pas apprendre à te défendre en si peu de temps, le maximum attribuable est de 5")
                            
                    
                elif a=='e' and n==1:
                    b=int(input("Combien de points veux-tu y attribuer ?"))
                    self.stat[3]=self.stat[3]+b
                    self.save[3]=self.save[3]+b
                    x=x-b
                    n=0
                elif a=='pv' and k==1:
                    b=int(input("Combien de points veux-tu y attribuer ?"))
                    self.stat[0]=self.stat[0]+b
                    self.save[0]=self.save[0]+b
                    x=x-b
                    k=0
                character.affstat(self)
            
            
class enemies(character):
    """
    Classe de création de toutes sortes d'énnemis.
    """
    def __init__(self,pv=0, attack=0, armor=0):
        
        """
        Initialisation des statistiques de l'énnemi commun:
            - Pv
            - attaque
            - armure
        
        Ces stats sont amenées à changer au cours du jeu grâce à la fonction myenemi()
        """
        
        self.pv=pv
        self.attack=attack
        self.armor=armor
        self.estat=[self.pv,self.attack,self.armor]
        additions.__init__(self)
        
    def randname(self):
        
        """
        Méthode de création d'un nom de manière aléatoire pour mon énnemi.
        Pour se faire on alterne entre une consonne et une voyelle tout deux aléatoire,
        afin de construire un mot d'une longueur aléatoire aussi.
        """
        
        a=additions.dice(1,2,7)
        name=[]
        voyelles=['a','e','i','o','u','y']
        consonnes=['z','r','t','p','q','s','d','f','g','h','j','k','l','m','w','x','c','v','b','n']
        for i in range(1,a+1):
            if (i%2)==0:
                name.append(rd.choice(voyelles))
            else:
                name.append(rd.choice(consonnes))
        self.ename=''.join(name)
        return self.ename
    
    def affstat(self):
        
        """
        Méthode d'affichage des statistiques de l'énnemi. Cette fois sans la méthode additions.barre()
        """
        
        print("\nLes statistiques de ton énnemi sont les suivantes :\n"+\
              "\n PV: {}".format(self.estat[0])+\
              "\n Attaque: {}".format(self.estat[1])+\
              "\n Défense: {}".format(self.estat[2]))
        
    def myenemi(self):
        
        """
        Création définitive des statistiques de l'énnemi commun en fonction des statistiques du joueur.
        Même si il est, par définition, moins fort. 
        (C'est également ici qu'on lui donne un nom aléatoire avec enemies.randname())
        """
        
        self.ename=enemies.randname(self)
        self.estat=[i for i in self.stat]
        self.estat[0]=self.save[0]-15
        self.estat[1]= self.estat[1]-5
            
    
    
    def Ixion(self):
        
        """
        La méthode Ixion définit un Boss, accessoirement premier énnemi du jeu.
            Affichage d'un peu de texte et d'image.
            Initialisation des statistique sous la même variable q'un énnemi classique.
            Le nom n'est pas aléatoire ('Ixion')
            C'est ici qu'est définie la classe du joueur (character.class_())
        """
        
        print(self.name,": C'est terrible... Ixion ! Vient te battre ! Lucie, éloigne toi !"+\
              "\nIxion: Comment compte tu me battre sans arme, pauvre monstre ?"+\
              "\n{} : *Je dois prendre une de ces armes autour.*".format(self.name))
        character.class_(self)
        input("Appuyer sur 'Entrée' pour continuer")
        additions.images('ixion2.jpg')
        print("Ixion: J'ai subi un tel supplice en enfer, vous allez tous payer !")
        self.estat=[1,10,15]
        self.ename='Ixion'
        self.xp=500
        
    def Chronos(self):
        
        """
        La méthode Chronos définit un Boss, Dernier énnemi du joueur.
            Affichage de beaucoup de texte pour l'histoire.
            Définition de ses statistiques et de son nom.
        """
        print("\nChronos: Bonsoir, {}, bienvenue chez moi!".format(self.name)+\
              "\nTérifié, tu restes bouche bée"+\
              "\nChronos: Alors, parle petit garnement, tu n'es pas arrivé là pour rien ?"+\
              "\n{}: Qu'à tu fais pour en arriver là ?".format(self.name)+\
              "\nChronos: Ce que j'ai fait ? C'est pourtant bien simple."+\
              "n'as tu pas vu que les enfers et le monde réel sont reliés maintenant ?"+\
              "\n{}: Merci de cette précision. Dis moi comment arrêter cela ?".format(self.name)+\
              "\nChronos: Espères-tu vraiment une réponse de ma part ? Je suis le créateur de cette faille."+\
              "Elle est faite de mon énérgie vitale, je ne vais donc pas te dévoiler tous ses secrets."+\
              "\n{}: Si tu dis vrai, alors ta mort entraînera la disparition de la faille.".format(self.name)+\
              "\nhChronos: *eclate de rire* Et que compte tu faire gringalet ?"+\
              "\n{}: Te tuer.".format(self.name)+\
              "\nChronos: Il faut que tu saches une chose, je veux bien t'accorder un combat."+\
              "Et si, par chance, tu parviens à me battre, tu devras le faire rapidement."+\
              "\nLes règles sont simples, tu as 3 minutes pour me vaincre. Si tu y arrives, tout redeviendra comme avant."+\
              "Mais, si tu n'y arrives pas, tu serras enfermé ici à jamais, avec moi, pour finir notre combat.")
        self.estat=[250,20,20]
        self.ename='Chronos'
        
class nymphess(character):
    
    """
    Cette classe regroupe les marchands du jeu, qui sont des nymphes: 
        - méthode yes
        - méthode prmière
        - méthode gambler
        - méthode blacksmith
        - méthode traveler
        - méthode herboriste
        - méthode magicien
    """
    
    def yes(self):
        
        """
        Cette méthode agit comme un début de conversation avec le marchand trés général 
        pour ensuite chosir au hasard quel marchand va être exécuté.
        """
        
        phrases=["Comme on se retrouve {}".format(self.name),'Bonjour mon grand bouc !', 'Comment vas-tu {}'.format(self.name), "Aurais-tu besoin d'aide ?", "De quoi aurra tu besoin aujourd'hui ?"]
        print(rd.choice(phrases)+\
              "\n{} : Qui es-tu ?".format(self.name))
        nymphes=['Érope','Agnodice','Agnodice','Wilhelmine','Basilisse','Glycère','Déô','Esther','Théodosie','Jeanne','Cyra','Xène','Flora','Chariclée','Chrysanthe','Horéozèle','Polymnie']
        self.nymphe=rd.choice(nymphes)
        y=rd.randint(0,4)
        if y==0:
            nymphess.gambler(self)
        elif y==1:
            nymphess.traveler(self)
        elif y==2:
            nymphess.herboriste(self)
        elif y==3:
            nymphess.blacksmith(self)
        elif y==4:
            nymphess.magician(self)

    def premiere(self):
        
        """
        La méthode première représente le premier marchad que le joueur croise.
        Avec beaucoup de texte pour l'histoire.
        
        Cette nymphes offre un pouvoir spécial au joueur (ce dernier aura le droit entre les 4 éléments),
        elle le soigne et lui redonne toute son endurance.
        """
        
        print("Comment vas-tu {} ?".format(self.name)+\
              "\n{} : Qui es-tu pour me connaître ?".format(self.name)+\
              "\nTu t'es bien battu, ça m'impressione... Mais ne te souviens-tu pas de moi ? Je suis Amphitrite, femme de Poséïdon."+\
              "\n{} : Et pourquoi te promène-tu ici, maintenant ? N'es-tu pas censée être au-près de ton Homme ?".format(self.name)+\
              "\nAmphitrite : Peut-être, mais nous faisons face à de grands problèmes comme tu as pu le remarquer."+\
              "\n{} : Pour être franc je n'ai pas bien compris, je n'ai que des soupçons...".format(self.name)+\
              "\nAmphitrite : Les bêtes comme toi sont vraiment sôtes, ce n'est pas qu'une légende... Ne sens-tu pas cette porte au Nord d'ici ?"+\
              "\n{} : J'ai de mauvais présentiments mais je ne peux rien affirmer.".format(self.name))
        input("Appuyez sur 'Entrée' pour continuer")
        print("\nAmphitrite: La porte des enfers s'est ouverte, mais personne ne s'y attendait. Ils nous ont prit au dépourvu." +\
              "\n{} : C'était donc bien ça... mais pourquoi les Dieux n'y sont pas ?".format(self.name)+\
              "\nAmphitrite : Ils ne peuvent pas, c'est pourquoi ils se reposent sur les gens come toi pour les aider."+\
              "\n{} : Cela risque d'être compliqué.".format(self.name)+\
              "\nAmphitrite : Certes, mais vous avez la bénédiction divine, et je suis là pour une bonne raison"+\
              "\n{} : Dis moi tout.".format(self.name)+\
              "\nAmphitrite : Si tu devais choisir un des 4 éléments, lequel serais-tu ?")
        
        special=input("L'Eau (e), le Feu (f), la Terre (t), ou l'Air (a) ?")
        if special.lower() == 'e':
            self.spe.replace(' ',"le pouvoir de l'Eau")
            dieu='Poséïdon'
        elif special.lower()=="f":
            self.spe.replace(' ',"le pouvoir du Feu")
            dieu= 'Héphaïstos'
        elif special.lower()=='t':
            self.spe.replace(' ','le pouvoir de la Terre')
            dieu='Gaïa'
        elif special.lower()=='a':
            dieu='Zéphir'
            self.spe.replace(' ',"le pouvoir de l'Air")
        
        print("\nAmphitrite : Ainsi tu possède donc le pouvoir de {} désormais.".format(dieu)+\
              "\n{} : Pourquoi devrais-je te croire ?".format(self.name)+\
              "\nAmphitrite : Ne suis-je pas l'épouse d'un Dieu. Au passage, je vais te soigner, tu en auras besoin.")
        self.stat[0]=self.save[0]
        self.stat[3]=self.save[3]
        
        input("Appuyez sur 'Entrée pour continuer")
        
        print("\n{} : Quelle bénédiction ! Merc... Elle est déjà partie...".format(self.name)+\
              "\nLucie : tu la connaissais ?"+\
              "\n{} : Oui de nom, elle est très connue de nous autres 'Monstres'.".format(self.name))
    
    def gambler(self):
        
        """
        Le gambler est un marchand orienté jeu. En d'autre termes c'est un joueur qui propose une partie au passant.
        Ainsi le héro prindcipal peut choisir si il veut joueur ou non.
        Si il décide de jouer, cela éxécute Hangman_game() du fichier JDRHangman.
        """        
        
        print("Je suis {}, enchantée. Tout le monde parle de toi en ce moment !".format(self.nymphe)+\
              "{} : Et que me veux tu ?".format(self.name)+\
              "{} : Veux tu jouer à un jeu, si tu gagne tu auras une récompense ?".format(self.nymphe)+\
              "{} : Laisse moi réfléchir...".format(self.name))
        
        a=input("Veux tu jouer à ce jeu ? (O/n) ")
        if a=='O':
            Hangman_game()
        elif a=='n':
            print("\n{} :Bien, c'est dommage pour toi, tu aurrai pu gagner gros sur ce coup...".format(self.nymphe))
            
    def traveler(self):
        
        """
        La méthode Traveler créé un 'marchand' qui offre un objet au hasard au joueur.
            - 75% de chance d'avoir au hasard: un bibelot magique, un couteau de lancer ou un surin.
            - 15% de chance d'avoir au hasard: des explosifs, une potion de force ou une potion d'endurance.
            - 10% de chance d'avoir au hasard: une bombe ou une potion de soin.
        """
        
        print('{} : Je suis {}. Enchantée !'.format(self.nymphe,self.nymphe)+\
              "\n{} : Bonjour, que me veux tu ?".format(self.name))
        just=["Sois un peu gentlemen tout de même je ne te veux que du bien.","Simplement t'aider dans ta quête","Je souhaite te donner un bien"]
        print("{} :".format(self.nymphe),rd.choice(just)+\
              "\n{} : Il faut faire vite s'il te plaît.".format(self.name))
        a=rd.randint(0,100)
        if a<=75:
            ob=['bibelot magique','couteau de lancer','surin']
        elif a>75 and a<=90:
            ob=['explosif','potion de force',"potion d'endurance"]
        else:
            ob=['bombe','potion de soin']
        v=rd.choice(ob)
        self.obj.append(v)
        print("{} : Voici mon présent.".format(self.nymphe)+\
              "\nTu obtiens : {}.".format(v)+\
              "\n{} : Merci infiniement, mais je dois reprendre ma route, aurevoir belle voyageuse !".format(self.name))
        
    def herboriste(self):
        
        """
        Cette méthode créé un marchand spécialisé dans les herbes médicinales et les potions.
        Le stock du marchand est aléatoire, allant de 1 à 4 objets.
            En fonction du nombre d'objet et de l'objet en lui même un tableau est affiché avec l'objet et son prix.
            Le joueur choisit ensuite ce qu'il veut.
            Il paiera avec ses crédits. 
        """
        
        print("{} :Je m'appelle {} et je suis spécialisée dans les herbes médicinales. Voudrais-tu m'acheter quelque chose ?".format(self.nymphe,self.nymphe)+\
              "\n\nTu as actuellement {} crédits.".format(self.credits))
        ob=['potion de force','potion de soin',"potion d'endurance"]
        a=rd.randint(1,4)
        b=input("Veu-tu acheter quelque chose à cette nymphe ? (O/n))")
        if b=='O':
            for i in range(0,a):
                v=rd.choice(ob)
                if v=='potion de force':
                    print(" "*20,'-'*52)
                    print(" "*20,'|', 3*" ","{}".format('Potion de force'), 3*" ", "|", 4*" ", "{}".format('2000 crédits'),4*' ', "|")
                    print(" "*20,'-'*52)
                elif v=='potion de soin':
                    print(" "*20,'-'*52)
                    print(" "*20,'|', 4*" ","{}".format('Potion de soin'), 3*" ", "|", 4*" ", "{}".format('3000 crédits'),4*' ', "|")
                    print(" "*20,'-'*52)
                else:
                    print(" "*20,'-'*52)
                    print(" "*20,'|', 2*" ","{}".format("Potion d'endurance"), " ", "|", 4*" ", "{}".format('1000 crédits'),4*' ', "|")
                    print(" "*20,'-'*52)
                    
            d=0
            while d==0:
                g=input("Que veux-tu lui acheter ? (si rien tappe 'rien')")
                if g.lower()=='potion de soin':
                    obje='potion de soin'
                    prix=3000
                    self.credits=self.credits-prix
                elif g.lower() =='potion de force':
                    prix=2000
                    obje='potiont de force'
                    self.credits=self.credits-prix
                elif g.lower()=="potion d'endurance":
                    obje="potion d'endurance"
                    prix=1000
                    self.credits=self.credits-prix
                elif g.lower()=='rien':
                    d=1
                
                if self.credits<0:
                    self.credits=self.credits+prix
                    print("Tu n'as pas assez de crédits pour te payer cela.")
                elif self.credits>=0 and g.lower()!='rien':
                    self.obj.append(obje)
                    print('Transaction effectuée')
                else:
                    print("\n{} : C'est dommage, bonne continuation à toi.".format(self.nymphe)+\
                          "\n{} : Merci, à toi aussi.".format(self.name))
                    
        else:
            print("{} : Alors je te dis aurevoir voyageur, je te souhaite le meilleur.".format(self.nymphe)+\
                  "\n{} : Au plaisir !".format(self.name))
            
    def blacksmith(self):
        """
        Cette méthode créé un marchand spécialisé dans la métalurgie.
        Le stock du marchand est aléatoire, allant de 1 à 4 objets.
            En fonction du nombre d'objet et de l'objet en lui même un tableau est affiché avec l'objet et son prix.
            Le joueur choisit ensuite ce qu'il veut.
            Il paiera avec ses crédits. 
        """
        print("{} :Je suis {}. Je vois que tu as du beau matériel, mais j'ai mieux à te proposer. Tu veux quelque chose ?".format(self.nymphe,self.nymphe)+\
              "\n\nTu as actuellement {} crédits.".format(self.credits))
        b=input("Veu-tu acheter quelque chose à cette nymphe ? (O/n)")
        a=rd.randint(1,3)
        obje=['nouvelle arme','couteau de lancer','surin']
        if b=='O':
            for i in range(0,a): 
                v=rd.choice(obje)
                print("\n")
                if v=='nouvelle arme':
                    print(" "*20,'-'*52)
                    print(" "*20,'|', 5*" ","{}".format("Arme neuve"), 5*" ", "|", 9*" ", "{}".format('9000'),8*' ', "|")
                    print(" "*20,'-'*52)
                elif v=='couteau de lancer':
                    print(" "*20,'-'*52)
                    print(" "*20,'|', 2*" ","{}".format('Couteau de lancer'), 1*" ", "|", 9*" ", "{}".format('800'),9*' ', "|")
                    print(" "*20,'-'*52)
                elif v=='surin':
                    print(" "*20,'-'*52)
                    print(" "*20,'|', 8*" ","{}".format('Surin'), 7*" ", "|", 9*" ", "{}".format('750'),9*' ', "|")
                    print(" "*20,'-'*52)
            d=0
            while d==0:
                g=input("Que veux-tu lui acheter ? (si rien tappe 'rien')")
                if g.lower()=='arme neuve':
                    prix=9000
                    self.credits=self.credits-prix
                elif g.lower() =='couteau de lancer':
                    prix=800
                    obje='couteau de lancer'
                    self.credits=self.credits-prix
                elif g.lower()=="surin":
                    obje="surin"
                    prix=750
                    self.credits=self.credits-prix
                elif g.lower()=='rien':
                    d=1
                
                if self.credits<0:
                    self.credits=self.credits+prix
                    print("Tu n'as pas assez de crédits pour te payer cela.")
                elif g.lower()=='':
                    print('{} : Je ne suis pas bien sur de comprendre ce que tu veux.'.format(self.nymphe))
                elif self.credits>=0 and g.lower()!='rien':
                    if g.lower()=='arme neuve':
                        print('Transaction effectuée'+\
                              '\n{} : Voici donc ta nouvelle arme guerrier.'.format(self.nymphe))
                        if self.cl=='1':
                            additions.images('arc2.jpg')
                        elif self.cl=='2':
                            additions.images('epeerandom.jpg')
                        elif self.cl=='3':
                            additions.images('magic3.jpg')
                        self.aface=self.aface+8
                    else:
                        self.obj.append(obje)
                        print('Transaction effectuée')
                else:
                    print("\n{} : Tu loupes des occasions en Or, tant pis.".format(self.nymphe)+\
                          "\n{} : Aurevoir belle forgeronne .".format(self.name))
        else:
            print("{} : Alors je te dis aurevoir voyageur, je te souhaite le meilleur.".format(self.nymphe)+\
                  "\n{} : Bon vent l'amie !".format(self.name))
            
    def magician(self):
        """
        Cette méthode créé un marchand spécialisé dans la magie et certaines potions.
        Le stock du marchand est aléatoire, allant de 1 à 4 objets.
            En fonction du nombre d'objet et de l'objet en lui même un tableau est affiché avec l'objet et son prix.
            Le joueur choisit ensuite ce qu'il veut.
            Il paiera avec ses crédits. 
        """
        
        print("{} :Je suis {}.Veux-tu pouvoir toucher au bonheur que je ressent en maitrisant la nature ?".format(self.nymphe,self.nymphe)+\
              "\n\nTu as actuellement {} crédits.".format(self.credits))
        b=input("Veu-tu acheter quelque chose à cette nymphe ? (O/n))")
        a=rd.randint(1,3)
        obje=['bibelot magique','bibelot magique',"potion d'endurance","potion de soin"]
        if b=='O':
            for i in range(0,a):
                v=rd.choice(obje)
                if v=='bibelot magique':
                    print(" "*20,'-'*52)
                    print(" "*20,'|', 5*" ","{}".format('Bibelot magique'), 1*" ", "|", 4*" ", "{}".format('1000 crédits'),4*' ', "|")
                    print(" "*20,'-'*52)
                elif v=='potion de soin':
                    print(" "*20,'-'*52)
                    print(" "*20,'|', 4*" ","{}".format('Potion de soin'), 3*" ", "|", 4*" ", "{}".format('3000 crédits'),4*' ', "|")
                    print(" "*20,'-'*52)
                else:
                    print(" "*20,'-'*52)
                    print(" "*20,'|', 2*" ","{}".format("Potion d'endurance"), " ", "|", 4*" ", "{}".format('1000 crédits'),4*' ', "|")
                    print(" "*20,'-'*52)
            d=0
            while d<a:
                g=input("Que veux-tu lui acheter ? (si rien tappe 'rien')")
                if g.lower()=='potion de soin':
                    obje='potion de soin'
                    prix=3000
                    self.credits=self.credits-prix
                    d=d+1
                elif g.lower() =='bibelot magique':
                    prix=2000
                    obje='bibelot magique'
                    self.credits=self.credits-prix
                    d=d+1
                elif g.lower()=="bibelot magique":
                    obje="potion d'endurance"
                    prix=1000
                    self.credits=self.credits-prix
                    d=d+1
                elif g.lower()=='rien':
                    d=d+10
                
                if self.credits<0:
                    self.credits=self.credits+prix
                    print("Tu n'as pas assez de crédits pour te payer cela.")
                elif self.credits>=0 and g.lower()!='rien':
                    self.obj.append(obje)
                    print('Transaction effectuée')
                
                print("\n{} : Bonne continuation à toi.".format(self.nymphe)+\
                      "\n{} : Merci, à toi aussi.".format(self.name))
            
                
#if __name__ == "__main__" :
#    nymphess().magician()  