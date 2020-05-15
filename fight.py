#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 14:05:38 2020

@author: rcoppe
"""
from Character import character,enemies,nymphess
from additions import additions
import random as rd

class fight:
    
    """
    Cette classe comprend toutes les méthode utile au combat ou à certaines actions du joueur.
        - méthode méditation
        - méthode fight
        - méthode endurancelimit
        - méthode repos
    """
    
    def méditation(self):
        
        """
        La méthode méditation est activée à un moment précis de l'histoire. 
        Le joueur doit méditer certain nombre d'heure. Et aléatoirement il se réveille à cause d'un énnemi. 
        """
        
        print("Une fois de retour à ton camps tu entres en méditation.")
        time=0
        while time<=96:
            add=15+additions.dice(3,2,5)
            time=time+add
            print("\nTu as pu méditer {} heures.".format(add)+\
                  "Mais un énemi te dérange, il faut te défendre !")
            enemies.myenemi(self)
            fight.fight(self)
            if self.stat[0]<=0:
                break
            else:
                a=additions.dice(1,1,3)
                if a<3:
                    nymphess()
            
    def fight(self):
        
        """
        Ici on créé une boucle qui définit le déroulement des combats, 
        qui s'arrêtent lorsque un des deux opposants n'a plus de vie.
        
        Ce que fait l'énnemi est choisit aléatoirement parmis :
            - Attaquer (69%)
            - Se défendre (30%)
            - Fuir (1%)
        
        Le joueur à le droit entre:
            - Attaquer
            - Se défendre
            - Utiliser un objet 
            - Uiliser son attaque spéciale (3 utilisations mais pas contre Ixion)
        
        Dans chaque situations il y a différents scénarios possibles. 
        
            Le joueur, si il attaque, peut faire:
                - un coup critique (utilisation de deux dés de combat)
                - un coup normal (un seul dés de combat)
                - louper son coup
                - louper son coup et se blésser 
            Ensuite il se prendra des dégats si l'ennemi attaque. Si ce dernier se défend, il prendra moins de dégats.
            
            En cas de défense:
                - Récupération d'énergie
                - Minimisation des dégats subit 
            
            Utilisation d'un objet: 
                - Bombe / explosif : Tue l'énnemi mais fait des dégats au joueur
                - Potion de vie: Redonne 35pv au joueur
                - Potion d'endurance: restore l'endurance du joueur
                - Potion de force: Double la force du joueur pour le combat en cours
                - Couteau de lancer / surin: fait 30 points de dégats sur l'adversaire à coup sûr
                - Bibelot magique: peut ne rien faire (50%), restaurer l'énergie du joueur (40%), restaurer la vie du joueur (10%)
            
            L'attaque spéciale fait des dégats basés sur la difficulté du jeu :
                - Facile: 100
                - Moyen: 75
                - Extrème: 50
                
        La fonction est assez longue à cause de tous les éléments à gérer lors des combats.
        """
        end=1
        additions.sacados(self)
        while end==1:
            
            character.affstat(self)
            enemies.affstat(self)
            
            if self.ename=='Ixion' or self.uses==0:
                v=input("Veux-tu attaquer (a), te défendre (d), ou utiliser un objet (o) ? ")                     # Demande au joueur ce qu'il veut faire
            
            else:
                v=input("Veux-tu attaquer (a), te défendre (d), utiliser un objet (o), ou utiliser ta compétence spéciale (spe) ? ")
                
            lchoice=rd.randint(0,100) 
            damagea=self.estat[1]+additions.dice(1,0,4)                                                                  # De la ligne 31 à 37 on a un choix aléatoire d'action pour l'adversaire
            if lchoice<=69:
                l='a'                                                                                   # a symbolise l'attaque avec 69% de chance 
                
            elif lchoice>69 and lchoice<=99:
                l='d'                                                                                   # d symbolise la défense avec 29% de chance
            else:
                l='r'                                                                                   # r pour run symbolise la fuite avec 2% de chance
                print("\n{} s'enfuit en courant vite, on dirait qu'il a eu peur!".format(self.ename))
                self.xp=self.xp-100
                self.estat[0]=0

            if v.lower()=="a": 
                miss=rd.randint(0,100)                                                                                 # Si le joueur attaque, alors :
                if l=='a':
                    
                    edamage=damagea + additions.dice(1,0,2)
                    self.stat[0]=self.stat[0]-edamage
                    print("\nTon ennemi t'attaque aussi et tu perds {} PV".format(edamage))
                    if self.stat[3]==0:                                                                 # Il se peux qu'il n'ai plus d'endurance, au quel cas cela l'empêche d'attaquer et passe son tour
                        print("\nTu n'as plus d'énergie, tu ne peux donc pas attaquer !" )
                        
                    elif self.stat[3]>0:                                                                # Toutefois si il a assez d'énergie alors:
                        qc=rd.randint(0,3)
                        print(self.name, 'utilise : ', self.tech[qc])                                   # Le hasard choisit le nom de la technique utilisée
                        
                       
                        if miss<=85 and miss>70:
                            damage=self.stat[1]+additions.dice(2,0,self.aface)                         # L'attaque a 95% de chance de toucher la cible, dont 20% de chance de faire un coup critique
                            self.estat[0]=self.estat[0]-damage                                         # Coup critique = 2dés au lieu de un seul
                            self.stat[3]=self.stat[3]-additions.dice(1,1,3)
                            fight.endurancelimit(self)
                            print("\nC'est un coup critique !"+\
                                  "\nCette attaque fait perdre {} PV à ton adversaire".format(damage))
                                
                        elif miss<=70:                                                                   # Ici on définie l'attaque classique
                            damage=self.stat[1]+additions.dice(1,0,self.aface)
                            self.estat[0]=self.estat[0]-damage
                            self.stat[3]=self.stat[3]-additions.dice(1,1,3)
                            fight.endurancelimit(self)
                            print("\nJoli coup !"+\
                                  "\nCette attaque fait perdre {} PV à {}".format(damage,self.ename))
                                
                        elif miss>85 and miss<=99:                                                        # Il y a cependant 4% d'echec dans les attaques
                            print("\nTu n'as pas réussi à toucher ton adversaire ! Fais attention !")
                            self.stat[3]=self.stat[3]-additions.dice(1,1,3)
                            fight.endurancelimit(self)
                                
                        elif miss==100:                                                                   # Et 1% d'echec grave qui provoque une blessure chez le joueur
                            print("En voulant attaquer tu chute et te blesse !")
                            self.stat[0]=self.stat[0]-additions.dice(1,1,3)
                            self.stat[3]=self.stat[3]-additions.dice(1,1,3)
                            fight.endurancelimit(self)
                                
                elif l=='d':
                    if self.stat[3]==0:                                                                 # Il se peux qu'il n'ai plus d'endurance, au quel cas cela l'empêche d'attaquer et passe son tour
                        print("Tu n'as plus d'énergie, tu ne peux donc pas attaquer !" )
                    
                    elif self.stat[3]>0:                                                                # Toutefois si il a assez d'énergie alors:
                        qc=rd.randint(0,3)
                        print(self.name, 'utilise : ', self.tech[qc])
                        
                        if miss<=95 and miss>75:
                            damage=self.stat[1]-additions.dice(1,0,self.estat[2])+additions.dice(1,0,self.aface)
                            self.estat[0]=self.estat[0]-damage
                            self.stat[3]=self.stat[3]-additions.dice(1,1,3)
                            fight.endurancelimit(self)
                            print("\nC'est un coup critique, mais ton énnemi se défend !"+\
                                  "\nCette attaque fait perdre {} PV à ton adversaire".format(damage))
                            
                        elif miss<=75:                                                                    # Ici on définie l'attaque classique
                            damage=self.stat[1]+additions.dice(1,0,self.aface)-additions.dice(1,0,self.estat[2])
                            self.estat[0]=self.estat[0]-damage
                            self.stat[3]=self.stat[3]-additions.dice(1,1,3)
                            fight.endurancelimit(self)
                            print("\nJoli coup, mais ton énnemi se défend !"+\
                                  "\nCette attaque fait perdre {} PV à {}".format(damage,self.ename))
                        
                        elif miss>95 and miss<=99:                                                        # Il y a cependant 4% d'echec dans les attaques
                            print("Tu n'as pas réussi à toucher ton adversaire ! Fais attention !")
                            self.stat[3]=self.stat[3]-additions.dice(1,1,3)
                            fight.endurancelimit(self)
                            
                        elif miss==100:                                                                   # Et 1% d'echec grave qui provoque une blessure chez le joueur
                            print("En voulant attaquer tu chute et te blesse !")
                            self.stat[0]=self.stat[0]-additions.dice(1,1,3)
                            self.stat[3]=self.stat[3]-additions.dice(1,1,3)
                            fight.endurancelimit(self)
                                
                            
            elif v.lower()=='d':
                
                if l=='a':
                    self.stat[0]=self.stat[0]-damagea + additions.dice(1,0)
                    self.stat[3]=self.stat[3]+additions.dice(4,0,4)
                    print("Tu te défend mais ton énnemi attaque, ça fait mal !")
                    
                elif l=='d':
                    print("Vous vous défendez au même moment ! Auriez-vous peur ?")
                    self.stat[3]=self.stat[3]+additions.dice(3,0,3)
                    
                    
            elif v.lower()=='o':
                
                if len(self.obj)==0:
                    print("Tu n'as pas d'objet dans ton sac, tu perds votre temps !")
                    self.stat[0]=self.stat[0]-damagea + additions.dice(1,0,2)
                    damage=damagea - additions.dice(1,0,2)
                    print("Votre énnemi en profite, tu perds {} PV".format(damage))
                elif len(self.obj)>0:
                    self.stat[0]=self.stat[0]-damagea + additions.dice(1,0,2)
                    self.stat[3]=self.stat[3]+additions.dice(2,2,5)
                    additions.sacados(self)
                    w=input('Que veux-tu utiliser {}'.format(self.name))
                    if w.lower()=='bombe' or w.lower()=='explosif':
                        self.estat[0]= 0
                        self.stat[0]=self.stat[0]-additions.dice(2,0,5)
                        print("Une explosion retentit, {} n'est plus, mais vous y avez laissé des plumes...".format(self.ename))
                    elif w.lower()=='potion de soin':
                        self.stat[0]=self.stat[0]+35
                        print("Tu te sens beaucoup mieux d'un coup, tu regagnes des PV.")
                    elif w.lower()=="potion d'endurance":
                        self.stat[3]=self.save[3]
                        print("La potion a restauré toute ton énergie !")
                    elif w.lower()=='potion de force':
                        self.stat[1]=2*self.stat[1]
                        print("Tu te sens deux fois plus fort maintenant !" )
                    elif w.lower()=='couteau de lancer' or w.lower()=='surin':
                        self.estat[0]=self.estat[0]-30
                        print("Le tranchant de ton objet blesse ton adversaire !")
                    elif w.lower()=='bibelot magique':
                        effet=rd.randint(0,100)
                        if effet<80:
                            print("Rien ne se passe, cette nymphe m'a bien eu")
                        elif effet>=80 and effet<95:
                            print("C'est comme si tu n'avais pas encore combatu, ton énergie est comme neuve !")
                            self.stat[3]=self.save[3]
                        else:
                            print("Tes blessures ont disparues !")
                            self.stat[0]=self.save[0]
                    else:
                        print("Fais attention, l'erreur n'est pas permise en plein combat ! Tu t'es trompé dans l'écriture !")
                        
            elif v.lower()=='spe' and self.uses>0:
                self.uses=self.uses-1
                print("{} utilise : {}".format(self.name,self.spe))
                if self.diff=='1':
                    self.estat[0]=self.estat[0]-100
                elif self.diff=='2':
                    self.estat[0]=self.estat[0]-75
                elif self.diff=='3':
                    self.estat[0]=self.estat[0]-50
                    
                if self.spe=='le pouvoir de la Terre':
                    print('Une colonne de Terre sort du sol et projette {} dans les airs !'.format(self.ename))
                elif self.spe=="le pouvoir de l'Eau":
                    print("L'eau se condense autour de vos doigts et des gouttes, comme des balles, vont toucher ton adversaire")
                elif self.spe=="le pouvoir de l'Air":
                    print("L'air semble fuir ton énnemi, il s'étouffe !")
                elif self.spe=="le pouvoir du Feu":
                    print("Un feu ardent consume la toge de {}".format(self.ename))
            for i in range(0,len(self.stat)):
                #Changer pour rendre utile la potion de force
                if self.stat[i]>self.save[i] and i!=2:
                    self.stat[i]=self.save[i]
        
            if self.stat[0]<=0 and self.estat[0]>0:
                print('\n',self.name,": Je vais donc mourir aujourd'hui ? Comme cela ?"+\
                      "\n",self.ename,": Goutte une dernière fois au plaisir de la souffrance, misérable !")
                print("\nC'est la fin de l'aventure pour toi, tu es mort au combat."+\
                      "\nLes âmes damnées vont concquérir notre monde et en faire un enfer, mais tu te serra battu vaillamment, repose en paix.")
                additions.images('enferici.jpg')
                end=0
            elif self.stat[0]<=0 and self.estat[0]<=0:
                print("Dans ce combat acharné, les deux énnemis se donnent la mort, mais l'enfer reste ouvert...")
                additions.images('enferici.jpg')
                end=0
            elif self.estat[0]<=0:
                print("\nQuel combat spectaculaire et rude tu viens de mener, mais ne repose pas trop longtemps tes énemis prendraient l'avantage.")
                if self.stat[2]>self.save[2]:
                    self.stat[2]=self.save[2]
                end=0
                self.xp=self.xp+100
                self.credits=self.credits+500+additions.dice(2,15,50)
                character.lvl_up(self)
            
    def endurancelimit(self):
        
        """
        Cette méthode est utile pour éviter de dépasser le niveau d'endurance donné par les statistiques
        du joueur lorsque ce dernier se défend notamment.
        """
        
        if self.stat[3]<=0:
            self.stat[3]=0
            
    def repos(self):
        
        """
        Dans cette méthode, on définit ce qu'il se passe lorsque le joueur décide de se reposer avant un combat.
            Il regagne 1/3 de sa vie
            Il regagne toute son endurance
            Les énnemies deviennent plus forts
        """
        
        print("Tu attends un peu avant de reprendre ton chemin, c'est une décision sage, bien que tes énemis se renforcent...")
        self.stat[0]=self.stat[0]+int(0.3*self.save[0])
        self.stat[3]=self.save[3]
        if self.stat[0]>self.save[0]:
            self.stat[0]=self.save[0]
        self.estat[0]=self.estat[0]+20
        self.estat[1]= self.estat[1]+5
    
    def tuto1(self):
        
        self.stat=[100,20,15,100]
        print("Lors de ton aventure tu seras amené à combatre. des énemis, tjr plus corriaces"+\
              "Voici ton énemi:")
        
        self.ename=enemies.randname(self)
        self.estat=[100,20,15]
        print(self.ename,':')
        enemies.affstat(self)
        
        print("Ton but est de l'éliminer pour continuer ton aventure."+\
              "Pour ce faire, tu peux l'attaquer !")
        input("Attaque ! (a) ")
        print("Bravo")

