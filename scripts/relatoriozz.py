# -*- coding: iso-8859-1 -*-

################################################
##
##   Relatório
##
################################################

f = open(scgarq + '/relzz.tex', 'w')

f.write('\chapter{Relatório da Curva Zig-Zag Navio '+ nome +' }\n\n ')

##
##   Primeira Execução
##
f.write('\section{Primera Execução}')
f.write('\n ')
f.write('\\begin{center}')
f.write('\n ')
f.write('\\begin{tabular}{l|l|l}')
f.write('\n  ')
f.write('&Simulado &MarAd' + 2 * '\\' + ' \hline')
f.write('\n  ')
f.write('Execução' + 2*(' &' +'%.0f'.rjust(4)%(listaz[0]['exeNumber']))  + 
2 * '\\')
f.write('\n' + 2 * ' ')

f.write('Tempo até a execução (segundos) &' +
'%.2e'.rjust(4)%(listaz[0]['time']) +' &' + 2 * '\\')
f.write('\n' + 2 * ' ')

f.write('Ângulo de overshoot (graus) &'+
'%.2f'.rjust(4)%(listaz[0]['osangle']*(180/sp.pi)) +' &' + 2 * '\\')
f.write('\n' + 2 * ' ')

f.write('Overshoot path (metros)&'+ '%.2e'.rjust(4)%(listaz[0]['ospath']) + 
'& ' + 2 * '\\') 
f.write('\n' + 2 * ' ')

f.write('Reach &'+ '%.2e'.rjust(4)%(listaz[0]['reach']*(180/sp.pi)) + 
'&' + '' + 2 * '\\')
f.write('\n' + 2 * ' ')

f.write('\\end{tabular}')
f.write('\n ')
f.write('\\end{center}')
f.write('\n')


##
##   Segunda Execução
##

f.write('\section{Segunda Execução}')
f.write('\n ')
f.write('\\begin{center}')
f.write('\n ')
f.write('\\begin{tabular}{l|l|l}')
f.write('\n  ')

f.write('&Simulado &MarAd ' + 2 * '\\' + ' \hline')
f.write('\n  ')

f.write('Execução' + 2*(' &' +'%.0f'.rjust(4)%(listaz[0]['exeNumber'])) + 
 2 * '\\')
f.write('\n  ')

f.write('Tempo até a execução (segundos) &' +
'%.2e'.rjust(4)%(listaz[1]['time']) + '& ' + 2 * '\\') 
f.write('\n' + 2 * ' ')

f.write('Ângulo de overshoot (graus) &'+
'%.2f'.rjust(4)%(listaz[1]['osangle']*(180/sp.pi)) + '& ' + 2 * '\\') 
f.write('\n' + 2 * ' ')

f.write('Overshoot path (metros)&'+ '%.2e'.rjust(4)%(listaz[1]['ospath']) +
'& ' + 2 * '\\') 
f.write('\n' + 2 * ' ')

f.write('Reach &'+ '%.2e'.rjust(4)%(listaz[1]['reach']*(180/sp.pi)) + '& ' + 
2 * '\\') 
f.write('\n ')

f.write('\\end{tabular}')
f.write('\n ')
f.write('\\end{center}')


##
##   Terceira Execução
##

f.write('\section{Terceira Execução}')
f.write('\n ')
f.write('\\begin{center}')
f.write('\n ')
f.write('\\begin{tabular}{l|l|l}')
f.write('\n  ')

f.write('&Simulado &MarAd ' + 2 * '\\' + ' \hline')
f.write('\n  ')

f.write('Execução' + 2*(' &' +'%.0f'.rjust(4)%(listaz[0]['exeNumber'])) + 
 2 * '\\')
f.write('\n  ')

f.write('Tempo até a execução (segundos) &' +
'%.2e'.rjust(4)%(listaz[2]['time']) + '& ' + 2 * '\\') 
f.write('\n' + 2 * ' ')

f.write('Ângulo de overshoot (graus) &'+
'%.2f'.rjust(4)%(listaz[2]['osangle']*(180/sp.pi)) + '& ' + 2 * '\\') 
f.write('\n' + 2 * ' ')

f.write('Overshoot path (metros)&'+ '%.2e'.rjust(4)%(listaz[2]['ospath']) +
'& ' + 2 * '\\') 
f.write('\n' + 2 * ' ')

f.write('Reach &'+ '%.2e'.rjust(4)%(listaz[2]['reach']*(180/sp.pi)) + '& ' + 
2 * '\\') 
f.write('\n ')

f.write('\\end{tabular}')
f.write('\n ')
f.write('\\end{center}')


##
##   Relatório Zig-Zag
##
f.write('\\begin{figure}[H]')
f.write('\n  ')
f.write('\includegraphics[scale=' + escala + ']{'+dirzz + TipoModelo +
'PosOri.' + formato + '}')
f.write('\n ')
f.write('\caption{\ extit{Curva de Zigzag ' +
str(int(lemezz))+'/'+str(int(proazz)) +'}}')
f.write('\n ')
f.write('\\end{figure}')
f.write('\n ')

f.write('\subsection{Velocidades}')
f.write('\n\n ')

f.write('\\begin{figure}[H]')
f.write('\n  ')
f.write('\includegraphics[scale=' + escala + ']{'+dirzz + TipoModelo + 'Velo.'
+ formato + '}')
f.write('\n ')
f.write('\caption{\ extit{Curva de Zigzag ' +
str(int(lemezz))+'/'+str(int(proazz)) +'}}')
f.write('\n ')
f.write('\\end{figure}')
f.write('\n\n ')

f.write('\subsection{Acelerações}')
f.write('\n ')

f.write('\\begin{figure}[H]')
f.write('\n  ')
f.write('\includegraphics[scale=' + escala + ']{'+dirzz + TipoModelo + 'Acel.'
+ formato + '}')
f.write('\n ')
f.write('\caption{\ extit{Curva de Zigzag ' +
str(int(lemezz))+'/'+str(int(proazz)) +'}}')
f.write('\n ')
f.write('\\end{figure}')
f.write('\n\n ')

f.write('\subsection{Forças e Momentos}')
f.write('\n ')

f.write('\\begin{figure}[H]')
f.write('\n  ')
f.write('\includegraphics[scale=' + escala + ']{'+dirzz + TipoModelo +
'ForMom.' + formato + '}')
f.write('\n ')
f.write('\caption{\ extit{Curva de Zigzag ' +
str(int(lemezz))+'/'+str(int(proazz)) +'}. As forças e os momentos estão' +
'multiplicados por '+ str(ForEs) + '}')
f.write('\n ')
f.write('\\end{figure}')

f.write('\n\n ')

f.write('\subsection{Eta}')
f.write('\n ')

f.write('\\begin{figure}[H]')
f.write('\n  ')
f.write('\includegraphics[scale=' + escala + ']{'+ dirzz + TipoModelo
+'pltetat.' + formato + '}')
f.write('\n ')
f.write('\caption{\ extit{Curva de Zigzag ' +
str(int(lemezz))+'/'+str(int(proazz)) +'}}')
f.write('\n ')
f.write('\\end{figure}')
f.write('\n\n ')

f.close()
