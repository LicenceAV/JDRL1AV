#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# File Name :
# Creation Date : mer. 11 oct. 2017 09:30:55 CEST
# Last Modified : mer. 11 oct. 2017 13:34:05 CEST
# Created By : Cyril Desjouy
#
# Copyright © 2016-2017 Cyril Desjouy <ipselium@free.fr>
# Distributed under terms of the BSD license.
"""

DESCRIPTION

Iterator ot genererate ascii Hangman pictures

@author: Cyril Desjouy
"""

### Ajout d'un titre en français
### Ajout de l'affichage du nombre d'erreur dans la liste asciipics

class Hangman:
    '''
    Hangman iterator
    '''

    def __init__(self):
        self.title2='''\n''' + \
        '''                                888          \n'''+ \
        '''88888b.   .d88b.  88888b        888 888  888 \n''' + \
        '''d88 "88b d88  d8b 888 "88b "888 888 888  888 \n''' + \
        '''888  888 8888888" 888  888 888  888 888  888 \n'''+ \
        '''888 888" d88      888  888 d88" 888 888 "88b \n'''+ \
        '''888       "d8888  888  888  .d88888 888888b. \n'''+ \
        '''888 '''
        '''888 '''
        self.title = '''\n''' + \
            '''888\n''' + \
            '''888\n''' + \
            '''888\n''' + \
            '''88888b.  8888b. 88888b.  .d88b. 88888b.d88b.  8888b. 88888b.\n''' + \
            '''888 "88b    "88b888 "88bd88P"88b888 "888 "88b    "88b888 "88b\n''' + \
            '''888  888.d888888888  888888  888888  888  888.d888888888  888\n''' + \
            '''888  888888  888888  888Y88b 888888  888  888888  888888  888\n''' + \
            '''888  888"Y888888888  888 "Y88888888  888  888"Y888888888  888\n''' + \
            '''                             888\n''' + \
            '''                        Y8b d88P\n''' + \
            '''                         "Y88P"\n'''
        self.loss = '''___________.._______\n''' + \
            '''| .__________))______|\n''' + \
            '''| | / /      ||\n''' + \
            '''| |/ /       ||\n''' + \
            '''| | /        ||.-''.\n''' + \
            '''| |/         |/  _  \\\n''' + \
            '''| |          ||  `/,|\n''' + \
            '''| |          (\\\\`_.\n''' + \
            '''| |         .-`--'.\n''' + \
            '''| |        /Y . . Y\\\n''' + \
            '''| |       // |   | \\\\\n''' + \
            '''| |      //  | . |  \\\\\n''' + \
            '''| |     ')   |   |   (`\n''' + \
            '''| |          ||'||\n''' + \
            '''| |          || ||\n''' + \
            '''| |          || ||\n''' + \
            '''| |         / | | \\\n''' + \
            '''""""""""""|_`-' `-' |"""|\n''' + \
            '''|"|"""""""\ \       '"|"|\n''' + \
            '''| |        \ \        | |\n''' + \
            ''': :         \ \       : :\n''' + \
            '''. .          `'       . .\n''' + \
            '''. .                   . .\n'''
        self.win = '''      .   ,      .\n''' + \
            '''          L\  o    .-""-.\n''' + \
            '''           |\_    / (--> \\\n''' + \
            '''       o  .\ \'--.)_>_=/_(   __\n''' + \
            '''     .      \ )`-._/|_,(    (==)\n''' + \
            '''         o   |_\ (_   ( \  /|~~|\n''' + \
            '''       o . _.' `\ ) \_/\ \/ |  |\n''' + \
            '''      _ _.','\ _/\   (__'._/|()|\n''' + \
            '''     |=/=/====\======/==|  /`  `\\\n''' + \
            '''     \ ' . o . '-..-' o / /      \\\n''' + \
            '''      `'-.__  o'  __.-'` ;  _/\_  ;\n''' + \
            '''            `'..'`       ||`    `||\n''' + \
            '''              ||         || You  ||\n''' + \
            '''              ||         || WIN! ||\n''' + \
            '''              ||         | \____/ |\n''' + \
            '''           _.'  '._      |        |\n''' + \
            '''          <        >     \_.-""-._/\n''' + \
            '''           `""""""`       `""""""`\n'''
        self.asciipics = [
            '\n\t  _____' +
            '\n\t |    \|' +
            '\n\t       |' +
            '\n\t       |' +
            '\n\t       |' +
            '\n\t       |' +
            '\n\t       |' +
            '\n\t===========' +
            '\nRaté : 1/8',
            '\n\t  _____' +
            '\n\t |    \|' +
            '\n\t O     |' +
            '\n\t       |' +
            '\n\t       |' +
            '\n\t       |' +
            '\n\t       |' +
            '\n\t===========' +
            '\nEncore une erreur... : 2/8',
            '\n\t  _____' +
            '\n\t |    \|' +
            '\n\t O     |' +
            '\n\t |     |' +
            '\n\t       |' +
            '\n\t       |' +
            '\n\t       |' +
            '\n\t===========' +
            '\nConcentrez-vous : 3/8',
            '\n\t  _____' +
            '\n\t |    \|' +
            '\n\t O     |' +
            '\n\t/|     |' +
            '\n\t       |' +
            '\n\t       |' +
            '\n\t       |' +
            '\n\t===========' +
            "\nVous n'avez plus beaucoup d'essai : 4/8",
            '\n\t  _____' +
            '\n\t |    \|' +
            '\n\t O/    |' +
            '\n\t/|     |' +
            '\n\t       |' +
            '\n\t       |' +
            '\n\t       |' +
            '\n\t===========' +
            '\nLa fin se rapproche : 5/8',
            '\n\t  _____' +
            '\n\t |    \|' +
            '\n\t\O/    |' +
            '\n\t |     |' +
            '\n\t/      |' +
            '\n\t       |' +
            '\n\t       |' +
            '\n\t==========='
            '\n6 fautes...',
            '\n\t  _____' +
            '\n\t |    \|' +
            '\n\t\@/    |' +
            '\n\t |     |' +
            '\n\t/ \    |' +
            '\n\t       |' +
            '\n\t       |' +
            '\n\t==========='
            '\nVous allez y passer : 7/8',
            '\n\t  _____' +
            '\n\t |    \|' +
            '\n\t Q' +
            '     |' +
            '\n\t/|\ ' +
            '   |' +
            '\n\t/ \ ' +
            '   |' +
            '\n\t       |' +
            '\n\t       |' +
            '\n\t===========' +
            '\nPlus de seconde chance...']

        self.max = len(self.asciipics)
        self.level = -1
        
    def __iter__(self):
        return self

    def __next__(self):
        self.level += 1
        if self.level < self.max:
            return self.asciipics[self.level]
        else:
            raise StopIteration
    
    def __str__(self):
        return self.title
    def title2(self):
        return self.title2


if __name__ == '__main__':

    pics = Hangman()
    for i in pics:
        print(i)
