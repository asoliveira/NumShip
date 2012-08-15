# - * - coding: utf-8 - * -

#
#This file is part of a program called NumShip

#Copyright (C) 2011,2012  Alex Sandro Oliveira

#NumShip is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.


import scipy as sp
import numpy  as np

from LemeMarAd import * 
from LemeGen import * 

class leme1(lemeMarAd):
    """Classe com o modelo matemático de leme do 1"""

      def MudaLeme(self, dt):
        """Muda o leme avançando um passo 'dt' no tempo"""

        self.leme = self.leme + (self.lemeCom - self.leme) * (1 -
            sp.exp(-self.dic['lambdaleme'] * dt))        


if __name__ == "__main__":
    import doctest
    doctest.testmod() 