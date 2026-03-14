## Porque aprender a anatomia do olho?

Para começar, primeiros temos que responder a pergunta: porque a computação gráfica precisa da biologia da visão? O objetivo principal da Computação Gráfica não é necessariamente, simular a luz do universo exatamente conforme as leis da física, mas sim gerar uma imagem que o cérebro humano aceite como real. O visão humana é o objetivo final de todo o processo.

Entender a biologia nos permite ser eficientes. Se soubermos o que o olho não consegue ver, não precisamos gastar poder de processamento renderizando aquilo. A biologia dita nossos padrões de cores (RGB), nossa taxa de quadros por segundo (FPS) e até como comprimimos arquivos (JPEG).

Brilho Relativo (Percepção de Luminância)

O olho humano não é um medidor de luz absoluto. Nós percebemos o brilho de forma relativa ao contexto e ao contraste.

- Escolha de cores importa! Cores impactam outras cores ao redor delas.

- Contraste Simultâneo: Um objeto cinza parecerá muito mais claro se estiver sobre um fundo preto do que se estiver sobre um fundo branco. Isso ocorre devido à inibição lateral nas células da retina.

Lei de Weber-Fechner: A relação entre o estímulo físico (I) e a percepção psicológica (S) é logarítmica. Isso significa que, para percebermos um aumento linear no brilho, a intensidade da luz precisa aumentar exponencialmente. Por isso conseguimos exergar detalhes tanto em um dia ensolarado quanto em uma noite escura, mesmo que a diferença da intensidade da luz em ambos seja de milhões de vezes.

## Anatomia do Olho

Falando sobre a anatomia do olho: Nosso olho é um órgão com várias partes que atuam em conjunto para ser efetivo como um sistema de captura de imagem.

Partes do nosso olho:

Córnea: é uma camada transparente na frente do nosso olho, ela atua como proteção e também age como uma lente convergente fixa dos raios  de luz do ambiente. (Aliás, nosso olho não é um círculo perfeito por causa da córnea, é uma pequena protuberância). Funcionam como a objetiva de uma câmera, refratando a luz para que ela converja exatamente na retina.

Iris: É a parte colorida do olho, ela controla o quão aberta está a pupila.

Pupila: É a parte preta do olho, e é realmente um "buraco" que permite a luz entrar e chegar no fundo do olho.

Cristalino: O cristalino é quem faz a parte voluntária do foco da visão, ele vai mudar de forma ao flexionar ou relaxar, e isso vai influenciar como a luz chega na retina. 

Retina: É o sensor do olho humano, captando a luz. Na retina estão os cones e os bastonetes, os cones detectam cores e detalhes, e estão concentrados no centro da retina, enquanto os bastonetes são sensíveis à luz mas não detectam luz, eles são responsáveis pela visão periférica e pela detecção de movimento.

Nervo óptico: é o cabo que leva os dados para o cérebro. 

Inclusive a visão humana é feita em conjunto com o olho e o cérebro humano (não é só o olho ou só o cérebro que participa da visão), a imagem chega invertida para nosso olho e nosso cérebro detecta cobras antes do que outros animais. 

Nosso cérebro automaticamente junta as imagens dos dois olhos para fazer uma única imagem, e o nosso cérebro faz triangulação automaticamente, nos dando assim uma perspectiva 3D (e por isso ciclopes não tem boa perspectiva, pois eles só tem 1 olho)

Adaptação do Olho Humano

A adaptação é a capacidade do sistema visual de ajustar sua sensibilidade a diferentes níveis de iluminação. Ela ocorre através de dois mecanismos principais:

    Adaptação Pupilar (Rápida): A íris se contrai ou expande para controlar a entrada de luz. É uma resposta mecânica que leva frações de segundo.

    Adaptação Fotoquímica (Lenta): São os pigmentos na retina que são queimados ou repostos lentamente

    Por isso piratas usavam tapa-olhos, permitia que eles tivessem a "visão noturna" imediatamente ao entrar dentro do barco

## Óptica Geometrizada

Agora partindo para a parte física da visão.

A luz se comporta de forma previsível, o que nos permite modelar câmeras virtuais usando a geometria.

Lentes Convergentes e Divergentes: O olho utiliza lentes convergentes (convexas). Elas pegam raios de luz paralelos ou divergentes e os "dobram" para um ponto focal comum. Se o foco não cai exatamente na retina, temos os problemas de visão (miopia ou hipermetropia).

Inversão da Imagem: Devido à geometria das lentes convergentes, a imagem projetada na retina é, fisicamente, invertida (de cabeça para baixo e espelhada). O cérebro faz o "pós-processamento" para desinverter a imagem.

Profundidade de Campo: A relação entre a abertura da pupila e a distância focal do cristalino cria o efeito onde apenas um plano está em foco, enquanto o resto fica borrado.

## Acomodação e Nitidez

Agora partindo para a parte física da visão.

A luz se comporta de forma previsível, o que nos permite modelar câmeras virtuais usando a geometria.

Lentes Convergentes e Divergentes: O olho utiliza lentes convergentes (convexas). Elas pegam raios de luz paralelos ou divergentes e os "dobram" para um ponto focal comum. Se o foco não cai exatamente na retina, temos os problemas de visão (miopia ou hipermetropia).

Inversão da Imagem: Devido à geometria das lentes convergentes, a imagem projetada na retina é, fisicamente, invertida (de cabeça para baixo e espelhada). O cérebro faz o "pós-processamento" para desinverter a imagem.

Profundidade de Campo: A relação entre a abertura da pupila e a distância focal do cristalino cria o efeito onde apenas um plano está em foco, enquanto o resto fica borrado.

## Conclusão e curiosidades finais

Bandas de Mach

É um fenômeno de Inibição Lateral. Nossas células da retina "competem" entre si; quando uma célula detecta muita luz, ela inibe as vizinhas. Isso faz com que o cérebro exagere o contraste nas bordas de gradientes. Em CG, isso é crucial porque, se um sombreamento (shading) não for suave o suficiente, o olho humano vai perceber "degraus" de cor que nem deveriam estar lá.
Persistência Retiniana

É a incapacidade do olho de registrar mudanças de luz instantaneamente. Uma imagem permanece na retina por uma fração de segundo (cerca de 1/16 de segundo). A Computação Gráfica se aproveita disso para criar a ilusão de movimento: ao exibir uma sequência de imagens estáticas rapidamente (acima de 24 quadros por segundo), o cérebro "funde" essas imagens, criando uma percepção de fluxo contínuo. Sem a persistência retiniana, o cinema e os videogames seriam apenas apresentações de slides rápidas.