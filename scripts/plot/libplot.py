# -*- coding: utf-8 -*-

import scipy as sp

def somep(v, num=100):
  import pdb
  inds = 0
  inde = 0
  dis = len(v)/num
  s = sp.zeros(num)
  for cont in s:
    try:
      s[inds] = v[inde]
    except IndexError:
      print 'inds = ' + str(inds) + ' inde = ' + str(inde)
      print 's = ' + str(s.shape) + ' v = ' + str(v.shape), ' dis = ', str(dis)
  
    if (inde + dis) <= (v.shape[0]) and (inds <= (s.shape[0] - 1)):
      inde += dis
      inds += 1
    else:
      return s
        
  return s
