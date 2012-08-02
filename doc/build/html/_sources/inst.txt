.. sectionauthor:: Alex S. Oliveira <asoliveira85@gmail.com>
.. _Python: http://www.python.org/
.. _SciPy: http://www.scipy.org/SciPy/
.. _NumPy: http://www.numpy.org/
.. _Matplotlib: http://matplotlib.sourceforge.net/
.. _Git: https://github.com/git/git
.. _UFRJ: http://www.coppe.ufrj.br
.. _PENO: http://www.oceanica.ufrj.br
.. _NumShip-repos: https://github.com/asoliveira/NumShip

==========
Instalação
==========

    Certifique-se que possui o Python_ \, SciPy_ \, NumPy_ e Matplotlib_ instalado em seu computador.
    Caso possua o Git_ instalado em seu computador digite o comando:
    ::
    
        git clone https://github.com/asoliveira/NumShip

    Caso não faça download do repositório NumShip-repos_  entre na raiz do repositório e digite: 
    ::
    
        ./main
    
    no interpretador de comandos (caso esteja em linux). Caso contrário rode o script simula.py (em qualquer plataforma).
    ::
    
        python simula.py
    
    O usuário do linux deve tomar o cuidado de permitir que todos os arquivos sejam executáveis. Caso tenha dúvidas em como fazer isso
    digite o comando:
    ::
    
        sudo chmod -R +x NumShip/*
    
    Será pedido uma senha que é provável que seja a sua senha do sistema. O camando anterior deve ser digitado de fora do repositório 
    que você baixou.

    Os arquivos de configuração estão na pasta `dados`. Utilize um  editor de texto qualquer para inserir os coeficientes hidrodinâmicos 
    no arquivo `dados/marad_derivada.dat` e configurações da simulação no arquivo `dados/config.py`
