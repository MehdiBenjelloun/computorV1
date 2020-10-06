# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    tools.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mbenjell <mbenjell@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/24 20:26:21 by mbenjell          #+#    #+#              #
#    Updated: 2020/02/25 18:19:28 by mbenjell         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def merge_dict(dict_1, dict_2, op):
   
    res = {**dict_1, **dict_2}

    for k, v in res.items():
        if k in dict_1 and k in dict_2:
            res[k] = op(dict_1[k], dict_2[k])

    return res

def ft_sqrt(nb):
    
    a = nb
    b = 0
    e = 0.00001

    if nb == 0:
        return(0)
    else:
        while True:
            b = 0.5 * (a + nb / a)
            diff = a - b
            if diff < 0:
                diff = -diff
            if diff < e:
                return b
            a = b
    return (nb)
