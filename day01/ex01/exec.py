# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: esafar <marvin@42.fr>                      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/11/08 11:14:26 by esafar            #+#    #+#              #
#    Updated: 2021/11/08 14:08:02 by esafar           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

str = '';
#len = len(sys.argv);
#if len > 1:
for i in sys.argv:
    str = str + i + ' ';
str = str[8:len(str)-1];                     
str = str[::-1];                     
str = str.swapcase();
print(str);                  
