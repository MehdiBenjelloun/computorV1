# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    parsing.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mbenjell <mbenjell@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/19 11:08:47 by mbenjell          #+#    #+#              #
#    Updated: 2020/04/21 03:10:30 by mbenjell         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import re

class Parser:
    
    dict_left = {}
    dict_right = {}

    def check_pattern(self, liste):
        for e in liste:
            index = liste.index(e)
            if len(e) == 3:
                elt = liste[index]
                a = elt[0]
                b = elt[1]
                c = elt[2]
                liste[index] = [a + '.' + b, c]
            elif len(e) != 2:
                exit('Error parsing')
 
    def parse_formula(self, chaine):
        chaine = re.sub(r'\s+', r'', chaine)
        regex = r'([-]?([0-9]+(\.[0-9]+)?)[*]X\^([0-9]+))+'
        pattern = re.compile(regex)
        liste = chaine.split('=')
 
        if len(liste) is not 2:
            sys.exit('Error parsing')
 
        str_left = liste[0]
        str_right = liste[1]
 
        str_left = re.sub(r'-', r'+-', str_left)
        str_right = re.sub(r'-', r'+-', str_right)
 
        liste_left = re.split(r'[+]', str_left)
        liste_right = re.split(r'[+]', str_right)
 
        liste_left = [i for i in liste_left if len(i) is not 0]
        liste_right = [i for i in liste_right if len(i) is not 0]

        for i in liste_left:
            if re.match(pattern, i) is None:
                exit('Error parsing')
        for i in liste_right:
            if re.match(pattern, i) is None:
                exit('Error parsing')
 
        simple_pattern = r'([-]?[0-9]+)'

        liste_left = [re.findall(simple_pattern, i) for i in liste_left]
        liste_right = [re.findall(simple_pattern, i) for i in liste_right]
 
        self.check_pattern(liste_left)
        self.check_pattern(liste_right)

        for l in liste_left:
             l.reverse()
 
        for l in liste_right:
             l.reverse()
 
        self.dict_left = dict(liste_left)
        self.dict_right = dict(liste_right)

        self.dict_left = {float(k):float(v) for k, v in self.dict_left.items()}
        self.dict_right = {float(k):float(v) for k, v in self.dict_right.items()}

        return self.dict_left, self.dict_right
