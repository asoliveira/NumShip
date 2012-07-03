# -*- coding: iso-8859-1 -*-

################################################
##
##   Relatório
##
################################################

f = open(scgarq + '/relzz.tex', 'w')

f.write('\chapter{Relatório da Curva Zig-Zag Navio '+ nome +' }\n\n\t')

##
##   Primeira Execução
##
f.write('\section{Primera Execução}')
f.write('\n\t')
f.write('\\begin{center}')
f.write('\n\t')
f.write('\begin{tabular}{l|l|l}')
f.write('\n\t\t')
f.write('&Simulado &MarAd \\')
f.write('\n\t\t')
f.write('Execução' + 2*(' &' +'%.0f'.rjust(4)%(listaz[0]['exeNumber'])) + '\\')
f.write('\\\\n\t\t')

f.write('Tempo até a execução (segundos) &' +
'%.2e'.rjust(4)%(listaz[0]['time']) +' &')
f.write('\\\\n\t\t')

f.write('Ângulo de overshoot (graus) &'+
'%.2f'.rjust(4)%(listaz[0]['osangle']*(180/sp.pi)) +' &')
f.write('\\\\n\t\t')

f.write('\Overshoot path (metros)&'+ '%.2e'.rjust(4)%(listaz[0]['ospath']) + 
'&')
f.write('\\\\n\t\t')

f.write('Reach &'+ '%.2e'.rjust(4)%(listaz[0]['reach']*(180/sp.pi)) + 
'&')
f.write('\\\\n\t')

f.write('\end{tabular}')
f.write('\n\t')
f.write('\end{center}')


##
##   Segunda Execução
##

f.write('\section{Segunda Execução}')
f.write('\n\t')
f.write('\\begin{center}')
f.write('\n\t')
f.write('\begin{tabular}{l|l|l}')
f.write('\\\n\t\t')

f.write('&Simulado &MarAd\\')
f.write('\n\t\t')

f.write('Execução' + 2*(' &' +'%.0f'.rjust(4)%(listaz[0]['exeNumber'])) + 
'\\')
f.write('\n\t\t')

f.write('Tempo até a execução (segundos) &' +
'%.2e'.rjust(4)%(listaz[1]['time']) + '&')
f.write('\\\\n\t\t')

f.write('Ângulo de overshoot (graus) &'+
'%.2f'.rjust(4)%(listaz[1]['osangle']*(180/sp.pi)) + '&')
f.write('\\\\n\t\t')

f.write('Overshoot path (metros)&'+ '%.2e'.rjust(4)%(listaz[1]['ospath']) +
'&')
f.write('\\\\n\t\t')

f.write('Reach &'+ '%.2e'.rjust(4)%(listaz[1]['reach']*(180/sp.pi)) + '&')
f.write('\\\\n\t')

f.write('\end{tabular}')
f.write('\n\t')
f.write('\end{center}')


##
##   Terceira Execução
##

f.write('\section{Terceira Execução}')
f.write('\n\t')
f.write('\\begin{center}')
f.write('\n\t')
f.write('\begin{tabular}{l|l|l}')
f.write('\\\n\t\t')

f.write('&Simulado &MarAd\\')
f.write('\n\t\t')

f.write('Execução' + 2*(' &' +'%.0f'.rjust(4)%(listaz[0]['exeNumber'])) + 
'\\')
f.write('\n\t\t')

f.write('Tempo até a execução (segundos) &' +
'%.2e'.rjust(4)%(listaz[2]['time']))
f.write('\\\\n\t\t')

f.write('Ângulo de overshoot (graus) &'+
'%.2f'.rjust(4)%(listaz[2]['osangle']*(180/sp.pi)) + '&')
f.write('\\\\n\t\t')

f.write('Overshoot path (metros)&'+ '%.2e'.rjust(4)%(listaz[2]['ospath']) +
'&')
f.write('\\\\n\t\t')

f.write('Reach &'+ '%.2e'.rjust(4)%(listaz[2]['reach']*(180/sp.pi)) + '&')
f.write('\\\\n\t')

f.write('\end{tabular}')
f.write('\n\t')
f.write('\end{center}')


##
##   Relatório Zig-Zag
##
f.write('\\begin{figure}[H]')
f.write('\n\t\t')
f.write('\includegraphics[scale=' + escala + ']{'+dirzz + TipoModelo + 'PosOri.' + formato + '}')
f.write('\n\t')
f.write('\caption{\\textit{Curva de Zigzag ' +
str(int(lemezz))+'/'+str(int(proazz)) +'}}')
f.write('\n\t')
f.write('\end{figure}')
f.write('\n\t')

f.write('\subsection{Velocidades}')
f.write('\n\n\t')

f.write('\\begin{figure}[H]')
f.write('\n\t\t')
f.write('\includegraphics[scale=' + escala + ']{'+dirzz + TipoModelo + 'Velo.'
+ formato + '}')
f.write('\n\t')
f.write('\caption{\\textit{Curva de Zigzag ' +
str(int(lemezz))+'/'+str(int(proazz)) +'}}')
f.write('\n\t')
f.write('\end{figure}')
f.write('\n\n\t')

f.write('\subsection{Acelerações}')
f.write('\n\t')

f.write('\\begin{figure}[H]')
f.write('\n\t\t')
f.write('\includegraphics[scale=' + escala + ']{'+dirzz + TipoModelo + 'Acel.'
+ formato + '}')
f.write('\n\t')
f.write('\caption{\\textit{Curva de Zigzag ' +
str(int(lemezz))+'/'+str(int(proazz)) +'}}')
f.write('\n\t')
f.write('\end{figure}')
f.write('\n\n\t')

f.write('\subsection{Forças e Momentos}')
f.write('\n\t')

f.write('\\begin{figure}[H]')
f.write('\n\t\t')
f.write('\includegraphics[scale=' + escala + ']{'+dirzz + TipoModelo +
'ForMom.' + formato + '}')
f.write('\n\t')
f.write('\caption{\\textit{Curva de Zigzag ' +
str(int(lemezz))+'/'+str(int(proazz)) +'}. As forças e os momentos estão' +
'multiplicados por '+ str(ForEs) + '}')
f.write('\n\t')
f.write('\end{figure}')

f.write('\n\n\t')

f.write('\subsection{Eta}')
f.write('\n\t')

f.write('\\begin{figure}[H]')
f.write('\n\t\t')
f.write('\includegraphics[scale=' + escala + ']{'+ dirzz + TipoModelo
+'pltetat.' + formato + '}')
f.write('\n\t')
f.write('\caption{\\textit{Curva de Zigzag ' +
str(int(lemezz))+'/'+str(int(proazz)) +'}}')
f.write('\n\t')
f.write('\end{figure}')
f.write('\n\n\t')

f.close()
