# -*- coding: iso-8859-1 -*-

################################################
##
##   Relatório
##
################################################

f = open('./saida/relteste.tex', 'w')

f.write('\chapter{Relatório de Simulação de testes '+ nome +' }\n\n\t')




#####################################################
##
##   testes
##
#####################################################

##

f.write('\subsection{Forças}')
f.write('\n\t')

f.write('\\begin{figure}[H]')
f.write('\n\t\t')
f.write('\includegraphics[scale=' + escala + ']{'+ dir + TipoModelo +'Fxbeta.' + formato + '}')
f.write('\n\t')
f.write('\caption{\\textit{}}')
f.write('\n\t')
f.write('\end{figure}')
f.write('\n\n\t')

f.write('\\begin{figure}[H]')
f.write('\n\t\t')
f.write('\includegraphics[scale=' + escala + ']{'+ dir + TipoModelo +'Fybeta.' + formato + '}')
f.write('\n\t')
f.write('\caption{\\textit{}}')
f.write('\n\t')
f.write('\end{figure}')
f.write('\n\n\t')

f.write('\\begin{figure}[H]')
f.write('\n\t\t')
f.write('\includegraphics[scale=' + escala + ']{'+ dir + TipoModelo +'Kbeta.' + formato + '}')
f.write('\n\t')
f.write('\caption{\\textit{}}')
f.write('\n\t')
f.write('\end{figure}')
f.write('\n\n\t')

f.write('\\begin{figure}[H]')
f.write('\n\t\t')
f.write('\includegraphics[scale=' + escala + ']{'+ dir + TipoModelo +'Nbeta.' + formato + '}')
f.write('\n\t')
f.write('\caption{\\textit{}}')
f.write('\n\t')
f.write('\end{figure}')
f.write('\n\n\t')

f.close()
