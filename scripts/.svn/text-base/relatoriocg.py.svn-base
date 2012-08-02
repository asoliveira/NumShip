# -*- coding: iso-8859-1 -*-

################################################
##
##   Relatório
##
################################################
temp= scgarq + '/relcg.tex' 
try:
  f= open(temp, 'w')
except NameError:
  print 'houve algum problema na criação do diretório' + temp
del temp

f.write('\chapter{Relatório da Curva Giro Navio '+ nome +' }\n\n ')




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

f.write('Diâmetro tático   &' +
'%.f'.rjust(6)%(listacg[0]['taticalDiameter']) + '&')
f.write(2 * '\\' + '\n  ')

f.write('Avanço   & ' + '%.f'.rjust(4)%(listacg[0]['advance']) + '&')
f.write(2 * '\\' + '\n  ')

f.write('Transferência   & '+ '%.f'.rjust(4)%(listacg[0]['transfer']) + '&')
f.write(2 * '\\' + '\n  ')

f.write('Raio da curva de equilíbrio  & '+
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

f.write('\subsection{Acelerações}')
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

f.write('\subsection{Forças e Momentos}')
f.write('\n ')

f.write('\\begin{figure}[H]')
f.write('\n  ')
f.write('\includegraphics[scale=' + escala + ']{'+dircg + TipoModelo +
'ForMom.' + formato + '}')
f.write('\n ')
f.write('\caption{\ extit{Curva de Giro}. As forças e os mometos estão \
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
