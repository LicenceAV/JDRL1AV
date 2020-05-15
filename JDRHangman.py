#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 23:13:08 2020

@author: rcoppe
"""

import random as rd
import io
from hangman import Hangman
import time
from additions import additions

aaccent = ["é", "è", "ê", "à", "ù", "û", "ç", "ô", "î", "ï", "â"]
saccent = ["e", "e", "e", "a", "u", "u", "c", "o", "i", "i", "a"]

class Hangman_game(Hangman):
    """
    Cette classe est une reprise de la classe Hangman, codé en projet secondaire ce semestre.
    Elle a été simplifiée et adaptée au JDR afin de proposer une expérience cohérente.
    
    Maintenant cette classe permet de faire fonctionner un jeu du "Pendu" simplement, avec une récompense en cas de victoire.
    Le choix de la récompense se fait en tirant un dè. Jusqu'à 4 propositions peuvent être faites, mais le joueur ne pourra en choisir qu'une.
    """
    
    def __init__(self, langue="fr"):
        
        """
        Cette méthode initialise le jeu.
        On y ouvre notamment le dictionnaire français.
        """
        
        self.mistakes=0             # Sert dans l'affichage des différents dessins en ascii lorsque le joueur se trompe de lettre (self.game())
        self.al=[]                  # Liste dans la quelle on va implémenter les lettres déjà essayées (voir self.already())
        self.streak=[]              # Liste pour implémenter tous les mots déjà trouvés en cas de série de victoire
        self.all=[0]                # Liste pour enregistrer les points de chaque mots trouvés
        self.allstreak=[0]          # Liste pour enregistrer les maximums de points globaux en une série de victoire
        self.allwords=['']          # Liste pour enregistrer tous les mots joués
        self.d=0                    # Instanciation des points de base, soit 0
        Hangman.__init__(self)      # Instanciation du module Hangman joint au TP
        
        #Début du jeu:
        print('Bien, que le pendu commence !')
        time.sleep(2)
        
        # Ici on choisit le dictionnaire (la langue du jeu):
        with io.open('fr_dic.txt', encoding='utf8') as f:
            self.content=f.readlines()
        print(self.title2)                      # Utilisation des titres en ascii du fichier annexe
        
        Hangman_game.word_choice(self)
        Hangman_game.game(self)
    #fonction pour retirer les accents du mot à deviner
    def g(self,x):
        
        """
        La méthode g prend en argument un mot et en retire les accent.
        Ce grâce au listes aaccent et saccent, qui permettent de jouer avec l'indexation des caractères.
        """
        for i in aaccent:
            if i in x:
                a=aaccent.index(i)
                x=x.replace(i,saccent[a])
            else:
                x=x
        return(x)     
                
    #fonction pour choisir le mot que l'on va faire deviner
    def word_choice(self):
        
        """
        La méthode word_choice est utilisée pour choisir un mot parmis le dictionnaire francais.
        """
        
        for x in self.content:
            if len(x)<=6:                   # Suppression des éléments pas assez long (<4 + \n donc <6)
                self.content.remove(x)
        word=rd.choice(self.content)        # Choix aléatoire du mot dans tous les mots restant du dictionnaire
        self.word=word.replace('\n','')     # Remplacement du retour à la ligne
        self.word=self.g(self.word)              # Utilisation de la fonction précédente (g(x))
        self.find='*'*len(self.word)        # Création du mot caché que l'on nomme 'Find'
        
        ## Les deux listes suivantes seront utiles dans l'affichage de find avec les lettres déjà trouvées
        # Le mot et le mot caché sonttransformés en liste (voir utilité dans: 'self.already()')
        self.lword=[i for i in self.word]
        self.lfind=[t for t in self.find]            
    

    def end(self):
        
        """
        Méthode décrivant ce qu'il se passe si le joueur ne veux pas continuer la partie
        """
        
        print("\nTu veux donc partir... Bien. Tu n'auras donc aucune récompense.")
        self.lfind=self.find.replace('*','')
    
    def loser(self):
        
        """
        Méthode s'éxecutant en cas de défaite, ce qui signifie : pas de récompense pour le joueur.
        """
        
        self.find=self.find.replace('*','')
        print('\nT as perdu.','\n',self.loss,'\nVotre mot était : {}'.format(self.word))
        print('Tu perds donc toutes tes récompenses. Aurevoir guerrier.')
        self.allstreak.append(int(self.d))  # Voir doc string ligne 148-159
        self.streak=[]                 # Réinitialisation du win streak
        self.d=0                       # Réinitialisation des points
    
    # Fonction listant les lettres déjà essayées par le joueur
    def already(self):
        
        """
        Méthode utile dans le jeu pour afficher les lettres déjà utilisées.
        """
        
        self.al.append(self.lettre+'-')
        v=''.join(self.al)
        print('\nTu as essayé : {}'.format(v.upper()))
    
    def game(self):
        
        """
        Cette méthode correspond au coeur du mini jeu, elle met les fonctions en place pour permettre une bonne expérience.
        
        Si le joueur gagne, il peut prendre 1 objet parmis ceux proposés (1 à 4 aléatoires)
        """
        
        print('\nLe mot à de deviner se compose de {} lettres.'.format(len(self.word)))
        print('\n'+ self.find)
        
        # Tant que la personne n'a pas deviné le mot complet: 
        while self.find.count('*')>0:
            lettre=input('Quelle lettre veux-tu tester ? ')
            
            self.lettre=lettre.lower()      # Permet de jouer en majuscule et en minuscule
            
            # Si il rentre un mot:
            if len(lettre)>1:
                
                # Si c'est le bon mot, il gagne
                if self.lettre == self.word:
                    print("\nBravo, je ne m'attendais pas à cela de ta part",'\n','\n',self.win)
                    input("Appuyez sur 'Entrée' pour continuer")
                    print("Comme je te l'avais promis, tu as maintenant le droit à une récompense. Que veux tu donc ?")
                    g=additions.dice(1,1,4)
                    objects=['bombe','explosif','potion de soin',"potion d'endurance","potion de force","couteau de lancer","surin","bibelot magique"]
                    ob=[]
                    for i in range(g):
                        q=rd.choice(objects)
                        ob.append(q)
                        print('-', ob[i])
                    w=input('Que comptes tu prendre ? (écris le en entier)')
                    if w.lower()=='bombe':
                        self.obj.append('bombe')
                    elif w.lower()=='explosif':
                        self.obj.append('explosif')
                    elif w.lower()=='potion de soin':
                        self.obj.append('potion de soin')
                    elif w.lower()=="potion d'endurance":
                        self.obj.append("potion d'endurance")
                    elif w.lower()=='potion de force':
                        self.obj.append('potion de force')
                    elif w.lower()=='couteau de lancer':
                        self.obj.append('couteau de lancer')
                    elif w.lower()=='surin':
                        self.obj.append('surin')
                    elif w.lower()=='bibelot magique':
                        self.obj.append('bibelot magique')
                    self.credits=self.credits+1000
                    print("Bien. Je dois maintenant y aller, je te laisse te concentrer sur ta quête. Aurevoir.")
                    self.find=self.find.replace('*','')
                
                # Si le joueur veut arrêter son expérience
                elif self.lettre in ['end','fin','exit','stop']:    # Ces mots étant trop courts pour être des mots a trouver, ça ne pose pas de problème
                    self.end()
                    
                    self.find=self.find.replace('*','')
                    
                # Sinon il perd
                else:
                    self.loser()
            
            ## Si le joueur se trompe et appuis sur entré sans rien essayer ('miss click')
            # Cela évite de compter cette mégarde comme une erreur
            elif len(lettre)==0:
                print("\nIl semblerait qu'il y ait un problème, avez vous entré une lettre ?" )
            
            # Si il joue une lettre simple:
            else:
                
                # Pour demander les règles, le joueur tape '?'
                if lettre == '?':
                    print('\nLes règles sont les suivantes :','\n    - Il faut trouver le mot caché, pour cela, propose des lettres quand on te le demandera.' + \
                          "\n    - si ta lettre et dans le mot le jeu continue normalement."+\
                          "\n    - si ta lettre n'est pas dans le mot, tu commencera la mise a mort du pendu."+\
                          "\n    - si tu n'entre pas de lettre, cela ne comptera pas."+\
                          "\n      Il moura après la 8ème faute, mais tout te serra indiqué au fur et à mesure."+\
                          "\n    - Si tu as une idée du mot caché, il te suffit de l'écrire lorsque l'on demande une lettre."+\
                          "\n      Tu sauras alors si c'est le bon ou non "+\
                          "\n      Attention à bien entrer un mot complet pour que ton essai soit valide."+\
                          "\n    - Si tu le souhaite, tu peux sortir du jeu en tappant 'exit','end','fin', ou encore 'stop'. Mais tu n'auras pas ta récompense.")
                
                # Dans tout autre cas, le joueur entre une lettre
                else:
                    
                    # Si la lettre est dans le mot, on remplace le bon astérisque par la lettre en question
                    if lettre in self.lword:
                        for i,e in enumerate(self.lword):
                            if e==lettre:
                               self.lfind[i]=lettre
                            else:
                                pass
                        self.find=''.join(self.lfind)
                        print('\n',self.find)
                        self.already()
                        
                    # Si il se trompe:
                    else:
                        self.mistakes=self.mistakes + 1
                        
                        # Trop d'erreur = perte de la partie
                        if self.mistakes>8:
                            self.loser()
                            
                        # Sinon, on rajoute la lettre aux lettres déjà testée et on affiche le pendu étape par étape
                        else:
                            print(self.asciipics[self.mistakes-1])
                            self.already()
                            print('\n'+''.join(self.lfind))

#if __name__ == "__main__" :
#    A=Hangman_game()
#    A.word_choice()
#    A.game()