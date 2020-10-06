# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mbenjell <mbenjell@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/14 13:14:41 by mbenjell          #+#    #+#              #
#    Updated: 2020/02/24 22:44:23 by mbenjell         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from math import *
from tools import *

class Solver:

    solution = ''
    def __init__(self, poly):
        self.poly = poly

    def solve(self):
        a = self.poly.poly.get(2)
        b = self.poly.poly.get(1)
        c = self.poly.poly.get(0)

        if len(self.poly.poly) == 0:
            return('All real numbers are solutions')
        if self.poly.degree == 0 and c != 0:
            return('Impossible solution')
        if self.poly.degree == 1 and b == 0:
            return('Impossible solution')

        if a == None: a = 0
        if b == None: b = 0
        if c == None: c = 0

        if self.poly.degree == 1 and b != 0:
            return('The solution is:\n{}'.format(-c/b))
        elif self.poly.degree > 2:
            return("The polynomial degree is stricly greater than 2, I can't solve.")

        delta = b * b - 4 * a * c

        if delta < 0:
            solution = 'Discriminant is strictly negative, '
            solution += 'the two complex solutions are:\n'
            x = -b / (2 * a)
            y = ft_sqrt(-delta) / (2 * a)
            solution += '{} + i * {}\n'.format(x, y)
            solution += '{} - i * {}'.format(x, y)
            return(solution)
        else:
            s1 = (-b + ft_sqrt(delta)) / (2 * a)
            s2 = (-b - ft_sqrt(delta)) / (2 * a)

        if delta == 0:
            solution = 'The solution is:\n{}'.format(s1)
            return(solution)
        else:
            solution = 'Discriminant is strictly positive, the two solutions are:\n'
            solution += '{}\n{}'.format(s1, s2)
            return(solution)

