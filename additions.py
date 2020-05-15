#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 15:45:58 2020

@author: rcoppe
"""
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import random as rd

class additions:
    
    """
    La classe additions regroupe les éléments d'amélioration du JDR non nécéssaires.
        - méthode dice
        - méthode images
        - méthode sacados
        - méthode barre
    """
    
    def dice(nb=2, start=1, end=6):
        
        """
        Méthode définissant un lancé de dé sans affichage.
            - Arguments : nombre de dés, numéro de la première face, numéro de la dernière
            - Exécution : Tirage au sort d'un nombre compris entre les deux faces 
                          autant de fois qu'il y a de dés, et addition des résultats.
        """
        
        tot = 0                                         
        for i in range(nb):                           
            a = rd.randint(start, end)                 
            tot += a                                  
        return tot 
    
    def images(x):
        
        """
        Lecture d'image avec matplotlib
            - Arguments : nom de l'image.png
        """
        
        img = mpimg.imread(x)
        fig= plt.imshow(img)
        fig.axes.get_xaxis().set_visible(False)
        fig.axes.get_yaxis().set_visible(False)
        plt.show()
        
    def sacados(self):
        
        """
        Méthode définissant l'affichage des objets que possède le joueur au travers d'un tableau
        
        Print pour chaque objet : son nom, combien il y en a dans la liste obj (méthode count())
        """
        
        print('Voici ce que tu possède dans tes affaires :\n')
        print(" "*20,'-'*52)
        print(" "*20,'|', 7*" ","{}".format('Objets'), 8*" ", "|", 8*" ", "Nombre",6*' ', "|")
        print(" "*20,'-'*52)
        print(" "*20,'|', 7*" ","{}".format('Bombe'), 9*" ", "|", 10*" ", "{}".format(self.obj.count('bombe')),9*' ', "|")
        print(" "*20,'-'*52)
        print(" "*20,'|', 6*" ","{}".format('Explosif'), 7*" ", "|", 10*" ", "{}".format(self.obj.count('explosif')),9*' ', "|")
        print(" "*20,'-'*52)
        print(" "*20,'|', 4*" ","{}".format('Potion de soin'), 3*" ", "|", 10*" ", "{}".format(self.obj.count('potion de soin')),9*' ', "|")
        print(" "*20,'-'*52)
        print(" "*20,'|', 2*" ","{}".format("Potion d'endurance"), " ", "|", 10*" ", "{}".format(self.obj.count("potion d'endurance")),9*' ', "|")
        print(" "*20,'-'*52)
        print(" "*20,'|', 3*" ","{}".format('Potion de force'), 3*" ", "|", 10*" ", "{}".format(self.obj.count('potion de force')),9*' ', "|")
        print(" "*20,'-'*52)
        print(" "*20,'|', 3*" ","{}".format('couteau de lancer'), 1*" ", "|", 10*" ", "{}".format(self.obj.count('couteau de lancer')),9*' ', "|")
        print(" "*20,'-'*52)
        print(" "*20,'|', 8*" ","{}".format('Surin'), 8*" ", "|", 10*" ", "{}".format(self.obj.count('surin')),9*' ', "|")
        print(" "*20,'-'*52)
        print(" "*20,'|', 5*" ","{}".format('Bibelot magique'), 1*" ", "|", 10*" ", "{}".format(self.obj.count('bibelot magique')),9*' ', "|")
        print(" "*20,'-'*52)
        input("Appuyez sur 'Entrée' pour continuer")
        
    def barre(self,x,y):
        
        """
        Méthode définissant l'affichage d'une 'barre de chargement' (visualisation de l'expérience, etc...)
            - Arguments : Valeur variable, valeur fixe
            - Exécution : Valeur variable / valeur fixe 
                          Résultat multiplié à la longueur de la barre voulue (ici 50 caractères)
                          Affichage du nombre de caractère correspondant, ainsi que du reste en caractère vide
                          Pour plus de précision nous avons rajouté le pourcentage à côté.
            - Return : Une barre 'de chargement' évolutive pour aider à la visualisation de certaines statistiques.
        """
        
        percent=x/y
        used=percent*50
        presque= "[{}{}]".format('='*int(used),' '*(50-int(used))), '{}%'.format(int(percent*100))
        return ''.join(presque)

#if __name__ == "__main__" :
#    A=additions()
#    additions.tuto1()  
