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

f.write('\chapter{Relat�rio da Curva Giro Navio '+ nome +' }\n\n ')




#####################################################
##
##   Curva De Giro
##
#####################################################

##
f.write('\section{Curva de Giro}')
f.write('\n ')



f.write('\subsection{Dados}')
f.write('\n ')

f.write('\\begin{center}')
f.write('\n ')
f.write('\\begin{tabular}{lll}')
f.write('\n')
f.write('Dados &Simulado &MarAd')
f.write(2 * '\\' + ' \hline' + ' \n' + 2 * ' ')

f.write('Di�metro t�tico   &' +
'%.f'.rjust(6)%(listacg[0]['taticalDiameter']) + '&')
f.write(2 * '\\' + '\n  ')

f.write('Avan�o   & ' + '%.f'.rjust(4)%(listacg[0]['advance']) + '&')
f.write(2 * '\\' + '\n  ')

f.write('Transfer�ncia   & '+ '%.f'.rjust(4)%(listacg[0]['transfer']) + '&')
f.write(2 * '\\' + '\n  ')

f.write('Raio da curva de equil�brio  & '+
'%.f'.rjust(4)%(listacg[0]['steadytr']) + '&')
f.write(2 * '\\' + '\n ')

f.write('\end{tabular}')
f.write('\n ')
f.write('\end{center}')






f.write('\\begin{figure}[H]')
f.write('\n  ')
f.write('\includegraphics[scale=' + escala + ']{'+dircg + TipoModelo +
'PosOri.' + formato + '}')
f.write('\n ')
f.write('\caption{\ extit{Curva de Giro}}')
f.write('\n ')
f.write('\end{figure}')
f.write('\n ')


if GrausDeLib==4:
    f.write('\\begin{figure}[H]')
    f.write('\n  ')
    f.write('\includegraphics[scale=' + escala + ']{'+dircg + TipoModelo +
'Roll.' + formato + '}')
    f.write('\n ')
    f.write('\caption{\ extit{Curva de Giro}}')
    f.write('\n ')
    f.write('\end{figure}')
    f.write('\n ')

f.write('\subsection{Velocidades}')
f.write('\n\n ')

f.write('\\begin{figure}[H]')
f.write('\n  ')
f.write('\includegraphics[scale=' + escala + ']{'+dircg + TipoModelo + 'Velo.'
+ formato + '}')
f.write('\n ')
f.write('\caption{\ extit{Curva de Giro}}')
f.write('\n ')
f.write('\end{figure}')
f.write('\n\n ')

f.write('\subsection{Acelera��es}')
f.write('\n ')

f.write('\\begin{figure}[H]')
f.write('\n  ')
f.write('\includegraphics[scale=' + escala + ']{'+dircg + TipoModelo + 'Acel.'
+ formato + '}')
f.write('\n ')
f.write('\caption{\ extit{Curva de Giro}}')
f.write('\n ')
f.write('\end{figure}')
f.write('\n\n ')

f.write('\subsection{For�as e Momentos}')
f.write('\n ')

f.write('\\begin{figure}[H]')
f.write('\n  ')
f.write('\includegraphics[scale=' + escala + ']{'+dircg + TipoModelo +
'ForMom.' + formato + '}')
f.write('\n ')
f.write('\caption{\ extit{Curva de Giro}. As for�as e os mometos est�o \
multiplicados por '+ str(ForEs) + '}')
f.write('\n ')
f.write('\end{figure}')

f.write('\n\n ')

f.write('\subsection{Eta}')
f.write('\n ')

f.write('\\begin{figure}[H]')
f.write('\n  ')
f.write('\includegraphics[scale=' + escala + ']{'+ dircg + TipoModelo
+'pltetat.' + formato + '}')
f.write('\n ')
f.write('\caption{\ extit{Curva de Giro '  +'}}')
f.write('\n ')
f.write('\end{figure}')

f.write('\n\n ')


f.close()
