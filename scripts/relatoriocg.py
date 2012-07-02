# -*- coding: iso-8859-1 -*-

################################################
##
##   Relat�rio
##
################################################
temp= scgarq + '/relcg.tex' 
try:
  f= open(temp, 'w')
except NameError:
  print 'houve algum problema na cria��o do diret�rio' + temp
del temp

f.write('\chapter{Relat�rio da Curva Giro Navio '+ nome +' }\n\n\t')




#####################################################
##
##   Curva De Giro
##
#####################################################

##
f.write('\section{Curva de Giro}')
f.write('\n\t')



f.write('\subsection{Dados}')
f.write('\n\t')

f.write('\\begin{center}')
f.write('\n\t')
f.write('\\begin{tabular}{ll}')
f.write('\\ \n\t\t')

f.write('Di�metro t�tico  = & ' +
'%.f'.rjust(6)%(listacg[0]['taticalDiameter']))
f.write('\\\ \n\t\t')

f.write('Avan�o  = & ' + '%.f'.rjust(4)%(listacg[0]['advance']) )
f.write('\\\ \n\t\t')

f.write('Transfer�ncia  = & '+ '%.f'.rjust(4)%(listacg[0]['transfer']))
f.write('\\\ \n\t\t')

f.write('Raio da curva de equil�brio = & '+
'%.f'.rjust(4)%(listacg[0]['steadytr']))
f.write('\\\ \n\t')

f.write('\end{tabular}')
f.write('\n\t')
f.write('\end{center}')






f.write('\\begin{figure}[H]')
f.write('\n\t\t')
f.write('\includegraphics[scale=' + escala + ']{'+dircg + TipoModelo + 'PosOri.' + formato + '}')
f.write('\n\t')
f.write('\caption{\\textit{Curva de Giro}}')
f.write('\n\t')
f.write('\end{figure}')
f.write('\n\t')


if GrausDeLib==4:
    f.write('\\begin{figure}[H]')
    f.write('\n\t\t')
    f.write('\includegraphics[scale=' + escala + ']{'+dircg + TipoModelo + 'Roll.' + formato + '}')
    f.write('\n\t')
    f.write('\caption{\\textit{Curva de Giro}}')
    f.write('\n\t')
    f.write('\end{figure}')
    f.write('\n\t')

f.write('\subsection{Velocidades}')
f.write('\n\n\t')

f.write('\\begin{figure}[H]')
f.write('\n\t\t')
f.write('\includegraphics[scale=' + escala + ']{'+dircg + TipoModelo + 'Velo.' + formato + '}')
f.write('\n\t')
f.write('\caption{\\textit{Curva de Giro}}')
f.write('\n\t')
f.write('\end{figure}')
f.write('\n\n\t')

f.write('\subsection{Acelera��es}')
f.write('\n\t')

f.write('\\begin{figure}[H]')
f.write('\n\t\t')
f.write('\includegraphics[scale=' + escala + ']{'+dircg + TipoModelo + 'Acel.' + formato + '}')
f.write('\n\t')
f.write('\caption{\\textit{Curva de Giro}}')
f.write('\n\t')
f.write('\end{figure}')
f.write('\n\n\t')

f.write('\subsection{For�as e Momentos}')
f.write('\n\t')

f.write('\\begin{figure}[H]')
f.write('\n\t\t')
f.write('\includegraphics[scale=' + escala + ']{'+dircg + TipoModelo + 'ForMom.' + formato + '}')
f.write('\n\t')
f.write('\caption{\\textit{Curva de Giro}. As for�as e os mometos est�o multiplicados por '+ str(ForEs) + '}')
f.write('\n\t')
f.write('\end{figure}')

f.write('\n\n\t')

f.write('\subsection{Eta}')
f.write('\n\t')

f.write('\\begin{figure}[H]')
f.write('\n\t\t')
f.write('\includegraphics[scale=' + escala + ']{'+ dircg + TipoModelo +'pltetat.' + formato + '}')
f.write('\n\t')
f.write('\caption{\\textit{Curva de Giro '  +'}}')
f.write('\n\t')
f.write('\end{figure}')

f.write('\n\n\t')


f.close()
