# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mbenjell <mbenjell@42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/19 11:07:51 by mbenjell          #+#    #+#              #
#    Updated: 2020/04/21 04:16:53 by mbenjell         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import re 
import operator
from solver import *
from parsing import *

class Polynome:

    def __init__(self, expr):
        self.poly = expr

    def __repr__(self):
        seq = sorted(self.poly.items())

        res = 'Reduced form: '
        if len(seq) == 0:
            res += '0 = 0'
            return(res)
        else:
            coef = seq[0][1]
            power = seq[0][0]
            if coef - int(coef) != 0:
                res += '{} * X^{}'.format(coef, int(power))
            else:
                res += '{} * X^{}'.format(int(coef), int(power))

        for k, v in seq[1:]:
            if v < 0:
                if -v - int(v) != 0:
                    res += ' - {} * X^{}'.format(-v, int(k))
                else:
                    res += ' - {} * X^{}'.format(int(-v), int(k))
            else:
                if v - int(v) != 0:
                    res += ' + {} * X^{}'.format(v, int(k))
                else:
                    res += ' + {} * X^{}'.format(int(v), int(k))
        
        res += ' = 0'
        res += '\nPolynomial degree: {}'.format(int(max(seq)[0]))
        return str(res)

    def __add__(self, right):
        return Polynome(merge_dict(self.poly, right.poly, operator.add))

    def __neg__(self):
        return Polynome(dict((k, -v) for k, v in self.poly.items()))

    def __sub__(self, right):
        return self + -right

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('usage : python3.7 main.py [formule]')
        exit()

    parser = Parser()
    expr_1, expr_2 = parser.parse_formula(str(sys.argv[1]))
    poly_1 = Polynome(expr_1)
    poly_2 = Polynome(expr_2)

    reduced_poly = poly_1 - poly_2
    reduced_poly.poly = {k:v for k, v in reduced_poly.poly.items() if v != 0}

    if len(reduced_poly.poly) != 0:
        reduced_poly.degree = max(reduced_poly.poly.items())[0]

    print(reduced_poly)
    solution = Solver(reduced_poly)
    print(solution.solve())
