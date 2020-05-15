#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 20:01:23 2020

@author: rcoppe
"""

from Character import character, enemies, nymphess
from tuto import tuto
from additions import additions 
import random as rd
from fight import fight
import time

class JDR:
    """
    La classe JDR assemble toutes les classes et les méthodes créées autour du jeu,
    dans le but de construire l'histoire finale
    """
    
    def __init__(self):
        
        '''
        L'initialisation de ma classe JDR présente simplement le titre de ce dernier en ASCII
        '''
        
        character.__init__(self)
        print("""
                        888
                      888
                      
888         88   88888888888  888888d.   88888888888 88888888888     888888888b.  88888888888  .d8888b.
888         8    888          888   88b. 888         888             888    888b  888         d88b  Y88b 
888              888          888    888 888         888             888     888  888         Y88b
888              88888888     888   d88P 88888888    88888888        888     888  88888888    "Y888b.
888              888          888888P"   888         888             888     888  888            "Y88b.
888              888          888        888         888             888     888  888              "888
888b             888          888        888         888             888    888P  888         Y88b  d88P
88888888888      88888888888  888        88888888888 88888888888     888888888P"  88888888888  "Y8888P"


     Y888888888888Y   d8888  88888888b  Y888888888888Y   d8888  88888888b   88888888888  .d8888b.
          888        d88888  888    Y88b     888        d88888  888    Y88b 888         d88b  Y88b
          888       d88P888  888     888     888       d88P888  888     888 888         Y88b
          888      d88P 888  888    d88P     888      d88P 888  888    d88P 88888888     "Y888b.
          888     d88P  888  88888888P"      888     d88P  888  88888888P"  888            "Y88b.
          888    d88P   888  888  T88b       888    d88P   888  888  T88b   888              "888
          888   d8888888888  888   T88b      888   d8888888888  888   T88b  888         Y88b  d88P
          888  d88P     888  888    T88b     888  d88P     888  888    T88b 88888888888  "Y8888P""""")
    
    def menu(self):
        
        """
        Cette méthode est utile pour l'affichage du menu principal du jeu
        """
        
        print("\n\n"," "*16,'-'*70)
        print(" "*17,'|', 7*" ","{}".format('Tuto de combat'), 8*" ", "|", 8*" ", "Tuto du marchand",6*' ', "|")
        print(" "*17,'-'*70)
        print(" "*17,'|', 12*" ","{}".format('Jouer'), 12*" ", "|", 14*" ", "{}".format("Exit"),12*' ', "|")
        print(" "*17,'-'*70)
        p=input("Que voulez-vous faire ? ")
        if p.lower()=='tuto de combat':
            tuto.tuto1(self)
            JDR.menu(self)
        elif p.lower()=='tuto du marchand':
            tuto.tuto2(self)
            JDR.menu(self)
        elif p.lower()=='jouer':
            self.primer=time.time()
            JDR.histoire(self)
        elif p.lower()=='exit':
            print("\nA bientôt pour une nouvelle partie")
    
    def endloose(self):
        
        """
        methode définissant ce qu'il se passe en cas de défaite.
            - Affichage du temps de jeu au cours de la partie tout juste finie
            - Message de fin
            - Retour au menu
        """
        
        ti=time.time()
        globaal=ti-self.primer
        print("\nC'est la fin de l'aventure pur toi"+\
              "\nTu auras tout de même essayé de défendre le monde."
              "\nEt ce pendant {} minutes.".format(round(globaal/60,0))+\
              "\n\nReposes en paix.")
        JDR.menu(self)
        
    def endwin(self):
        
        """
        methode définissant ce qu'il se passe en cas de victoire.
            - Affichage du temps de jeu au cours de la partie tout juste finie
            - Retour au menu
        """
        
        ti=time.time()
        globaal=ti-self.primer
        print("\nTon combat aura duré {} minutes.".format(round(globaal/60,0)))
        JDR.menu(self)
        
    def histoire(self):
        
        """
        Ici, le but est de développer l'intrigue.
        Cette méthode se compose principalement d'affichage de texte.
        On y trouve aussi l'ensemble des méthodes venant d'autres classes mises dasn l'ordre afin de correspondre au jeu.
        """
        
        self.c=1
        while self.c>0:
            
            print("\n\nComme tous les matins, la jeune Lucie prépare le repas pour sa famille. Une corvée qu'elle réalise avec joie.\n"+\
                  "Mais ce matin là, le lait venait à manquer, elle due donc aller au marché.")
            
            print("\nAu coueur des stands de la ville de Lorcéis, au nord de la Grèce, elle se ballade."+\
                  "\nPour rentrer chez elle, elle doit emprunter un chemin terreux entre les grands chênes de la fôret."+\
                  "\nSes lourds sabots de bois taillé la ralentissent dans sa marche; elle aime penser que les Dieux lui demande d'observer le monde.")
            
            input("Appuyez sur 'Entrée' pour continuer")
            
            print("\nMais au loin elle entend une douce mélodie se perdant dans le vent.")
            
    
            print("\nQuand elle chercha d'ou vint le bruit, elle vit au pied d'un arbre un être très étrange, mi-Homme, mi-bête"+\
                  "\nMais qui était-il ..?")
            
            additions.images('satyre.jpeg')
            
            print("\nLa créature, consciente de la présence de Lucie, bondie sur ses deux pattes et voulu se cacher !"+\
                  "\nMais il était bien trop tard, elle était démasquée."+\
                  "\nIl fallut peut de temps à Lucie pour retrouver le monstre qui est bêtement tombé sur le sol.\n"+\
                  "\n\nQui êtes vous ? -Demanda vivement Lucie-")
            
            input("Appuyez sur 'Entrée' pour continuer")
            
            character.difficulty(self)
            
            print("Elle resta plantée là, bouche bée, ne sachant que dire.\n"+\
                  "\n!!!!!!! BOUUUUUM !!!!!!!")
            
            input("Appuyez sur 'Entrée' pour continuer")
                  
            print("\nUn bruit d'explosion vous abassourdi."+\
                  "\n{}: - C'était donc ça, ce que je ressentais...".format(self.name)+\
                  "\nLucie: - QUE SE PASSE-T-IL ?\n"+\
                  "\nSans perdre plus de temps, la créature prit ses affaires et courru vers le village"+\
                  "\nDans la panique, aucun mot ne se fit entendre sur le trajet, seul vos pas hâtés lessairent une trace dans ce lourd silence.\n"+\
                  "\nEn arrivant aux porte de Lorcéis, vous voyez une ville ravagée, en ruine. Un énorme cratère s'est creusé entre deux maisons."+\
                  "\nMais cela n'était pas le pire... Un Homme sortit du cratère...")
            
            enemies.Ixion(self)
            fight.fight(self)
            if self.stat[0]>0:
                input("Appuyez sur 'Entrée' pour continuer")
                print("\nTu as maintenant vaincu Ixion. Il était connu pour avoir tué sa belle-mère en la brûlant vive."+\
                      "\nMais ce qui semble étrange, c'est qu'il est mort il y a bien longtemps..."+\
                      "\nComment diable est-ce possible de revenir des tart..."+\
                      "\n\nLucie: {} ! Tu as battu Ixion ! Comment-ce fait-il qu'il soit revenu à la vie ?".format(self.name)+\
                      "\n{} : J'ai bien peut que la réponse ne plaise à personne ici bas...\n".format(self.name))
                nymphess.premiere(self)
                
                print("Lucie : A vrai dire, maintenant que je t'ai vu nous défendre, je me rend bien compte que tu es quelqu'un d'humain."+\
                      "\n{} : Ca me touche sincèrement... Mais je n'ai pas de temps à perdre, une faille vers les Tartares à été ouvertes et je me dois de combattre pour l'avenir de cette Terre.".format(self.name)+\
                      "\nLucie : Mais, nous n'avons aucune informations. Comment allons nous nous en sortir sortir ?"+\
                      "\n{} : Ne t'en fait pas, tu ne ferras pas partie de cette aventure, je ne peux me permettre de risquer une vie inocente.".format(self.name)+\
                      "\nLucie : Mais je ne veux plus retourner chez moi, ma vie ne me convient pas... Laisse moi venir..."+\
                      "\n{} : Il en est hors de question, tu ne peux pas. Tu devrais mieux penser à tes enfants si tu en as. Pars maintenant.\n".format(self.name))
                print("\nA contre coeur Lucie s'enfonce dans la fôret de Lorcéis, sans même dire aurevoir, une rivière de tristesse coulant sur ses joues.")
                input("Appuyez sur 'Entrée' pour continuer.")
                print("\nUne porte physique à donc été ouverte... Il faut impérativement la trouver et la refermer avant que les morts ne reviennent."+\
                      "\nMais comment trouver son emplacement ?"+\
                      "\n\nCommence par voyager, tu en apprendras certainement plus sur cette histoire."+\
                      "\n\nAinsi démarre ton voyage, de la ville de Lorcéis, direction Athène."+\
                      "\nLe soleil, haut dans ce ciel d'été commence à te rendre malade, il faut que tu t'arrrête."
                      "\nSur le bord de la route tu te pose contre un arbre. Au loin tu peux apercevoir la silouhète d'un Homme, grand, trop grand."+\
                      "\nCette vision te térifie et tu reste sur tes gardes."+\
                      "\nC'est un Cyclope ! Il ne faut pas perdre de temps, il est l'heure de se battre !")
                enemies.myenemi(self)
                fight.fight(self)
                if self.stat[0]<=0:
                    self.c=0
                else:
                    print("\nCe n'est ni le premier, ni le dernier d'une longue liste d'énemies et de dangers qui t'anttendent sur la route."+\
                          "\nPrépare toi ! d'autres arrivent plus vite que tu ne le penses.")
                    for i in range(rd.randint(6,8)):
                        ransentence=['Lève ton épée guerrier, un énemi te barre la route !','Tu dois forcer le passage !',"Oh non, tu vois un énemi au loin, il a l'air fort !",'Aux armes {} !'.format(self.name),'Un nouveau round se prépare !']
                        enemies.myenemi(self)
                        g=input("\nVeux-tu te reposer avant de partir ? (O/n) ")
                        if g=='O':
                            fight.repos(self)
                        print(rd.choice(ransentence))
                        fight.fight(self)
                        if self.stat[0]<=0:
                            break
                        else:
                            a=rd.randint(100)
                            if a>=33:
                                nymphess.yes(self)
                    if self.stat[0]<=0: 
                        self.c=0
                    else:
                        print("\n{} : La route à été longue mais enfin, Athène, te voilà.".format(self.name))
                        input("Appuyez sur 'Entrée' pour continuer.")
                        print("\nLa ville d'Athènes regorge de gens heureux dans les rues. Ces rues qui se multiplient à chaque croisement, un dédalle sans fin."+\
                              "\nComment donc compte tu trouver ou se trouve la faille ?"+\
                              "\nInstinctivement tu t'es dirigé vers cette cité, et plus tu avançais, plus tu pouvais trouver d'énemis... Tes intuissions ont l'air vraiment bonnes."+\
                              "\nMais n'était-ce vraiement qu'une simple intuission ?"+\
                              "\nTa condition de {} doit y être reliée... Mais comment ?".format(self.classe)+\
                              "\nPour le moment tu n'as rien de mieux à faire que te reposer dans le bois le plus proche pour éviter de te faire surprendre par des Humains.")
                        input("Appuyez sur 'Entrée' pour continuer.")
                        print("\nAprès une bonne nuit de sommeil te voilà bien remit"+\
                              "\nAthène est une mine d'informations, il te faut y pénétrer."+\
                              "\nPour se faire tu cache tes pâtes dans une longue toge salie par le voyage."+\
                              "\nA force de conversation tu sais désormais que la Sibylle Libyque se trouve en Ville il te faut donc la trouver.")
                        self.stat[3]=self.save[3]
                        if self.stat[0]<0.5*self.save[0]:
                            self.stat[0]=int(0.5*self.save[0])
                        else:
                            self.stat[0]=self.stat[0]+int(0.15*self.save[0])
                        print("\nAprès 5 jours de recherche, tu la trouve sur un chemin non loin de la cité..."+\
                              "\nLa Sibylle : Je savais que tu finirais par me trouver, mais es vraiment lent."+\
                              "\n{} : Où se trouve la porte ?".format(self.name)+\
                              "\nLa sibylle : Ne soit pas si préssé, je ne connais moi-même pas la réponse. Mais toi tu l'as."+\
                              "\n{} : Qu'entends-tu par là ?".format(self.name)+\
                              "\nLa Sibylle : Tu vas devoir chercher toi même ta réponse, sonde ton âme guérrier."+\
                              "\n{} : Je ne sais pas commet m'y prendre...".format(self.name)+\
                              "\nLa Sibylle : Tu trouveras si tu le veux vraiment.")
                        input("Appuyez sur 'Entrée' pour continuer.")
                        print("\nAprès cette conversation courte mais intense, tu décide de méditer afin de trouver cette réponse que tu cherches tant.")
                        fight.méditation(self)
                        if self.stat[0]<=0: 
                            self.c=0
                        else:
                            print("\n{} : J'ai réussi à développer mes sens, je sais désormais que faire.".format(self.name)+\
                                  "\nSans perdre de temps, tu regroupes toutes tes affaires."+\
                                  "\nPlus tu avances dans la fôret, plus tu es sûr de toi."+\
                                  "\nEnfin tu arrives, après de longues minutes de marches,"+\
                                  "derrière le Pnyx, la colline la plus majestueuse d'Athène."+\
                                  "\nIci se cache un grand secret."+\
                                  "\n\nC'est là que tu retrouve la faille vers les enfers, grande ouverte. "+\
                                  "\nSans même réfléchir tu t'y enfonces, il est trop tard pour faire machine arrière.")
                            input("Appuyez sur 'Entrée' pour continuer.")
                            print("\nEn penetrant dans la faille une odeur putride te parvient."+\
                                  "\nUne odeur de mort envahissait les lieux."+\
                                  "\nEt ce n'est qu'à deux de pas de là, en avançant,"+\
                                  "que tu trouve cerbère, entièrement étêté."+\
                                  "\nC'est d'ici que vient cette effluve."+\
                                  "\nLe pauvre chien n'a certainement pas pu lutter face à l'invasion"+\
                                  "d'hécatonchires et de géants."+\
                                  "\nMais tu n'as pas le temps de lui préparer une cérémonie,"+\
                                  "tu dois faire vite et trouver comment fermer la faille.")
                            input("Appuyez sur 'Entrée' pour continuer.")
                            print("\nAprès avoir passé les portes des enfers c'est une nouvelle surprise qui t'attend."+\
                                  "\nLa barque de Charon est vide. "+\
                                  "Serait-il mort lui aussi ?"+\
                                  "\nPeu importe, sa barque se trouve sur la rive,"+\
                                  "il comprendra que tu as traversé le Styx sans lui pour une bonne raison."+\
                                  "\nLa traversée est calme, c'est comme si l'enfer s'était vidé."+\
                                  "\nDans les récits il en est tout autrement."+\
                                  "\nAu loin tu aperçoit une chose flottante dans l'eau."+\
                                  " En te rapprochant tu discernes une forme humaine."+\
                                  "\nCharon était bien mort, noyé dans le Styx.")
                            input("Appuyez sur 'Entrée' pour continuer.")
                            print("\nIl faut encore faire des efforts, la réponse à toutes tes questions se trouve de l'autre côté."+\
                                  "\nMais pas le temps de te reposer, un Echatonchyre vient vers toi, il à l'air carriace.")
                            for i in range(rd.randint(6,8)):
                                ransentence=['Lève ton épée guerrier, un énemi te barre la route !','Tu dois forcer le passage !',"Oh non, tu vois un énemi au loin, il a l'air fort !",'Aux armes {} !'.format(self.name),'Un nouveau round se prépare !']
                                enemies.myenemi(self)
                                g=input("\nVeux-tu te reposer avant de partir ? (O/n) ")
                                if g=='O':
                                    fight.repos(self)
                                print(rd.choice(ransentence))
                                fight.fight(self)
                                if self.stat[0]<=0:
                                    break
                                else:
                                    a=rd.randint(100)
                                    if a>=33:
                                        nymphess.yes(self)
                            if self.stat[0]<=0: 
                                self.c=0
                            else:
                                print("\nBien. Maintenant que tu as la paix, il te faut explorer les enfers."+\
                                      "\nAprès de longues minutes de marche, tu trouves un énome palace."+\
                                      " Mais que peux-tu y trouver ?"+\
                                      "\nLes enfers sont relativement vides en ce moment..."+\
                                      "\nAinsi tu pousses les portes pour vérifier."+\
                                      "\nEt quelle ne fut pas ta surprise...")
                                enemies.Chronos(self)
                                qe=input("Es-tu prêt ? (O/n) ")
                                if qe=="n":
                                    print("\nChronos: Retourne dans ta campagne, mortel, tu n'es pas digne de te battre avec moi."+\
                                          "\n\n\n Ainsi s'achève ton aventure, par une peur incontrolable qui offre le monde aux enfers.")
                                    self.c=0
                                    self.stat[0]=0
                                else:
                                    zer=time.time()
                                    print("Le chronomètre est lancé !")
                                    fight.fight(self)
                                    ert=time.time()
                                    rty=zer-ert
                                    if rty<60:
                                        print("Le combat a duré {} secondes".format(int(rty)))
                                    elif rty>=60:
                                        print("Le combat a duré {} minutes et {} secondes".format(round(rty/60),int(rty-60*round(rty/60))))
                                    if self.stat[0]<=0:
                                        self.c=0
                                    elif self.stat>0 and rty>180:
                                        print("Chronos: il est déjà trop tard pour toi, même si je meurs, les enfers snt déjà vides."+\
                                              "Tous mes pairs attaquent les Dieux à cette heure, et leur fin et proche. La tienne va etre lente et douloureuse ici bas, Sans moi..."+\
                                              "Tu es enfermé dasn les enfers, mais rien ne peut te tuer. "+\
                                              "La vie t'es éternelle, alors que tu es seul dans ce monde hostile. Et tu vas peux à peux sombrer dans la folie. Adieu {}.")
                                        self.c=0
                                    elif self.stat>0 and rty<=180:
                                        print("Tu cours pour sortir des enfers, trop de choses s'y sont passées."+\
                                              "Le styx et la porte des enfers, avec leur cadavres tristement célébres ne te ralentissent pas."+\
                                              "Tu as vaincu et compte bien retrouver ta vie normale."+\
                                              "En sortant de la faille tu sens un vent puissant dans ton dos,"+\
                                              "et une fois retourné, tu ne vois plus rien, la faille a disparue.")
                                        input("Appuyez sur 'Entrée' pour continuer.")
                                        print("Lucie: {} ! Tu l'as fait ! ".format(self.name)+\
                                              "{}: Que fais tu là Lucie ??".format(self.name)+\
                                              "Lucie: Je t'ai suivie tout ce temps, mais il est bien dommage que je ne puisse rentrer dans les enfers."+\
                                              "{}: Folle que tu es ! Et ta famille ?".format(self.name)+\
                                              "Lucie : Ils sont morts, tués par un Cyclope."+\
                                              "{}: Je suis désolé...".format(self.name)+\
                                              "Lucie: Ce n'est pas grave, suis moi, j'ai une surprise.")
                                        input("Appuyez sur 'Entrée' pour continuer.")
                                        print("Lucie te prend par la mais et vous courrez, sans que tu saches ou vous allez."+\
                                              "C'est en haut du Pnyx que se trouve un Homme d'une étrange beaute."+\
                                              "Sans dire un mot il fit apparaitre un escalier dasn le ciel."+\
                                              "Une fois en haut de ce dernier tu comprend,"+\
                                              "Le mont olympe.")
                                        input("Appuyez sur 'Entrée' pour continuer.")
                                        print("Zeus: Bonjour {}, coment te sens tu ?".format(self.name)+\
                                              "{}: PAs très bien pour être honnête.".format(self.name)+\
                                              "Zeus, ce n'est pas grave, tu serras vite remit."+\
                                              "Je tenias à te remercier pour tout ce que tu as fait pour nous Pendant que tu affrontais tous les énemis inimaginables,"+\
                                              "nous étions confronté à des vagues gigantesques de monstres."+\
                                              "{}: Je n'ai fait que ce qui me paraissais bon.".format(self.name)+\
                                              "Zeus: C'est pour ça qu'au nom de tous mes pairs, je te fait Dieux Majeur de notre cour. "+\
                                              "*tu pleures sasn pouvoir faire me moindre bruit*"+\
                                              "Zeus: Tu pourras ainsi regner sur le ont olympe. "+\
                                              ".......")
                                        input("Appuyez sur 'Entrée' pour continuer.")
                                        print("Et c'est ainsi que toute cette histoire se termine, par une quête que tu as mené à bien."+\
                                              "Bravo, {}.".format(self.name))
                                        self.c=0
            else:
                self.c=0
        
        if self.stat[0]<=0:
            JDR.endloose(self)
        else:
            JDR.endwin(self)

if __name__ == "__main__" :
    A=JDR()
    A.menu()    