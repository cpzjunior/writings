**Resumo:** Eu defendo que o cloud gaming está sendo pensado pelo modelo errado: em vez de transformar jogos em uma Netflix, deveríamos separar o jogo da máquina que o executa. O usuário não precisa de centenas de títulos, mas de acesso à capacidade computacional necessária para jogar aquilo que escolheu, sem precisar comprar hardware para vários anos. Assim como a nuvem transformou computação em uma infraestrutura elástica, jogos poderiam ser executados em máquinas alugadas sob demanda, enquanto a compra e a distribuição dos jogos permanecem independentes. O futuro, portanto, pode estar menos em uma Netflix dos games e mais em uma AWS dos games.

------------------------------------------------------------------------

Eu comprei um Xbox Series S com uma ideia bastante simples na cabeça: queria jogar meus jogos favoritos sem precisar montar um PC gamer. O Game Pass parecia ser a solução perfeita. Uma assinatura, uma biblioteca enorme e um console relativamente barato. Na prática, descobri uma coisa curiosa: o catálogo é gigantesco, mas poucos jogos realmente me interessam. Há centenas de títulos disponíveis, mas continuo querendo jogar essencialmente os mesmos gêneros e algumas franquias específicas. O tamanho do catálogo, que deveria ser a principal justificativa para a assinatura, acaba tendo pouco significado quando os jogos que realmente quero jogar representam uma parcela minúscula dele.

O problema ficou ainda mais evidente quando comecei a pensar no hardware. O Series S continua sendo um console capaz, mas já consigo enxergar o caminho que ele está seguindo. Os jogos mais recentes exigem cada vez mais do hardware, e aquilo que hoje é uma máquina perfeitamente adequada gradualmente se transforma em uma máquina limitada pela geração para a qual foi projetada. Meu PC também não resolve o problema. Ele já tem alguns anos e, embora continue sendo perfeitamente útil para muita coisa e rode jogos que permanecem excelentes, não possui mais capacidade para acompanhar confortavelmente os lançamentos mais exigentes. Tenho, portanto, dois problemas diferentes: uma biblioteca de jogos muito maior do que aquilo que efetivamente quero jogar e um conjunto de hardware que precisa ser substituído periodicamente para acompanhar a evolução dos jogos.

Foi nesse ponto que comecei a questionar se estamos olhando para o problema da maneira correta. Eu não quero centenas de jogos. Quero jogar alguns jogos específicos. Também não quero necessariamente comprar uma nova máquina a cada geração. Quero ter acesso à capacidade computacional necessária para executar o jogo que decidi jogar naquele momento. Essas duas necessidades parecem bastante diferentes daquilo que os serviços de assinatura e o mercado tradicional de hardware estão tentando vender.

A pergunta que me ocorreu foi simples: e se o erro fundamental dos serviços de jogos por assinatura for tratar o catálogo de jogos como o produto, quando o verdadeiro produto que o usuário quer alugar é a capacidade computacional?

## O problema de transformar jogos em Netflix

Talvez o problema esteja justamente na tentativa de transformar videogames em uma categoria de entretenimento semelhante a filmes e séries. A analogia funciona em alguns aspectos, mas falha em um ponto fundamental: um jogo não é apenas conteúdo. Ele também é uma aplicação que precisa ser executada.

Quando assisto a um filme, o trabalho computacional pesado já foi realizado durante a produção. O serviço precisa armazenar e transmitir o vídeo de maneira eficiente. Quando jogo um título moderno na nuvem, a situação é completamente diferente. O servidor precisa executar o jogo em tempo real. Cada movimento do controle altera o estado do jogo, a CPU e a GPU processam essas informações, uma nova imagem é renderizada, ela é codificada e enviada pela rede até a minha tela, enquanto meus comandos fazem o caminho inverso.

Isso muda completamente a natureza do produto. No streaming tradicional, o conteúdo é o principal produto e a infraestrutura existe para entregá-lo. No cloud gaming, o conteúdo continua sendo necessário, mas a capacidade computacional passa a ser uma parte essencial daquilo que está sendo vendido. Quando alguém utiliza cloud gaming porque não possui um PC capaz de executar determinado jogo, o que essa pessoa está efetivamente tentando comprar é acesso temporário a uma máquina suficientemente poderosa.

Isso também expõe uma limitação do modelo baseado em catálogo. Existe uma premissa de que quanto mais jogos disponíveis, maior o valor da assinatura. Mas essa relação não é necessariamente verdadeira para videogames. Um jogador pode ter interesse em apenas alguns gêneros e franquias específicas. Centenas de títulos adicionais podem representar uma quantidade enorme de conteúdo disponível e, ao mesmo tempo, quase nenhum valor adicional para aquele usuário.

A diferença em relação a filmes e séries é importante. Quando assino um serviço de vídeo, posso assistir a uma série policial hoje, uma comédia amanhã, um documentário no fim de semana e talvez um filme de ficção científica depois. O custo para experimentar algo novo é baixo. Em jogos, o investimento é muito maior. Muitos títulos exigem dezenas de horas e uma adaptação às suas próprias mecânicas, sistemas, controles e progressão. O jogador não está simplesmente consumindo conteúdo. Está aprendendo a operar um sistema interativo.

É possível, portanto, ter um catálogo enorme e ainda assim oferecer pouco valor para determinado usuário. A quantidade de jogos disponíveis é uma métrica objetiva, mas não necessariamente uma boa métrica de utilidade.

E isso levanta uma questão bastante estranha sobre o modelo atual: se eu já sei qual jogo quero jogar, por que preciso assinar um catálogo inteiro para ter acesso à máquina que consegue executá-lo?

Se eu comprei Elden Ring, por exemplo, e quero jogá-lo em um computador que não possui uma GPU adequada, o problema que tenho não é falta de acesso a jogos. Eu já tenho o jogo. O problema é falta de capacidade computacional.

Talvez o produto que o cloud gaming deveria vender seja justamente essa capacidade.

## AWS e GPU como serviço

A computação em nuvem encontrou uma solução para um problema muito parecido. Uma empresa que precisa de capacidade computacional não precisa comprar um servidor para os próximos cinco anos. Ela pode alugar infraestrutura conforme a necessidade. Se precisa de mais processamento, provisiona uma máquina maior. Se precisa de menos, reduz a capacidade. Se não precisa de nada, desliga os recursos.

A grande inovação não foi simplesmente colocar servidores em um datacenter e acessá-los pela internet. Foi transformar capacidade computacional em um recurso elástico, que pode ser provisionado, dimensionado e consumido conforme a demanda.

O mesmo princípio poderia ser aplicado aos jogos. Em vez de comprar uma GPU para os próximos anos, o jogador poderia alugar capacidade computacional quando precisasse. Em vez de escolher uma máquina que precisa continuar sendo suficiente durante toda uma geração, ele poderia escolher a configuração necessária para o jogo que pretende executar naquele momento.

Um serviço desse tipo poderia oferecer diferentes classes de máquinas. Uma configuração mais barata poderia atender jogos menos exigentes ou jogadores dispostos a abrir mão de qualidade gráfica. Uma configuração intermediária poderia oferecer uma experiência em 1080p ou 1440p. Uma máquina mais poderosa poderia atender quem deseja gráficos no máximo, altas taxas de quadros ou ray tracing. O usuário escolheria a capacidade de acordo com aquilo que pretende jogar e com quanto está disposto a gastar.

Essa possibilidade muda completamente a relação entre jogador e hardware. Hoje, quando compro uma GPU, preciso tentar prever quais serão minhas necessidades futuras. Se compro uma placa muito poderosa, pago por uma capacidade que talvez não utilize durante boa parte do tempo. Se compro uma placa mais barata, corro o risco de descobrir alguns anos depois que ela não é mais suficiente para os jogos que quero jogar. Em ambos os casos, estou fazendo uma aposta antecipada.

Na nuvem, essa decisão deixa de ser permanente. Imagine que, em vez de uma assinatura tradicional, eu pudesse simplesmente comprar créditos de computação. Coloco R\$ 100 na minha conta e utilizo esse saldo conforme jogo. Uma máquina básica pode consumir poucos créditos por hora, enquanto uma máquina equipada com uma GPU de última geração consome muito mais. O preço da sessão passa a refletir diretamente a capacidade computacional que estou utilizando.

Se quero jogar um título relativamente leve durante vinte horas, posso escolher uma máquina mais simples e fazer meus créditos durarem bastante. Se quero passar cinco horas em um jogo extremamente pesado, posso escolher uma máquina premium e aceitar um consumo maior. Se não jogar durante um mês inteiro, não há motivo para consumir créditos.

O modelo pode continuar tendo planos recorrentes, mas a assinatura deixaria de representar principalmente acesso a um catálogo. Ela poderia funcionar como uma carteira de computação, com créditos acumulados e consumidos conforme a utilização. A diferença parece pequena, mas economicamente é enorme: eu passo a pagar pelaquilo que efetivamente estou utilizando, e não por uma coleção de jogos que talvez nunca abra.

Isso também cria uma relação muito mais transparente entre preço e experiência. Se quero uma imagem melhor, mais resolução ou uma GPU mais potente, pago mais. Se estou disposto a aceitar uma máquina mais simples, pago menos. O serviço não precisa decidir antecipadamente qual configuração todos os usuários devem receber.

A diferença fundamental é que a unidade de valor deixa de ser o jogo disponível e passa a ser a capacidade computacional consumida. O jogo continua sendo necessário, mas a infraestrutura deixa de ser um detalhe invisível e passa a ser o próprio serviço.

## O hardware deixa de ser uma aposta

Há ainda uma consequência mais profunda. O hardware local exige que o consumidor antecipe o futuro.

Quando compro um console ou uma GPU, estou comprando uma determinada quantidade de capacidade computacional que espero que seja suficiente durante vários anos. Não sei quais serão os requisitos dos jogos futuros, mas preciso tomar uma decisão hoje.

Isso é particularmente relevante quando pensamos na velocidade com que a tecnologia gráfica evolui. Uma máquina que parece poderosa no lançamento de uma geração pode continuar funcionando perfeitamente por muitos anos, mas gradualmente passa a exigir compromissos: reduzir a resolução, diminuir a qualidade gráfica, abrir mão de ray tracing ou aceitar taxas de quadros menores.

Meu Series S não deixa de funcionar quando surge uma nova geração de jogos. Meu PC também não se transforma em uma máquina inútil. O que acontece é mais sutil: eles deixam de oferecer a capacidade computacional necessária para executar determinados jogos da maneira que eu gostaria.

No modelo de cloud gaming, essa obsolescência pode ser deslocada do consumidor para o provedor. Quando uma nova geração de GPUs chega, ela pode ser adicionada ao datacenter. Quando determinado hardware envelhece, ele pode continuar disponível como uma opção mais barata para jogos menos exigentes. O usuário não precisa comprar uma nova máquina para acompanhar a evolução da infraestrutura.

Isso não significa que a obsolescência desapareça. Ela apenas deixa de ser um problema que cada consumidor precisa resolver individualmente e passa a ser um problema de infraestrutura que o provedor administra em escala.

Em vez de perguntar qual hardware preciso comprar hoje para continuar jogando durante os próximos cinco anos, posso simplesmente perguntar qual capacidade preciso para jogar o título que quero jogar hoje.

Essa é uma mudança conceitual importante. O consumidor deixa de fazer uma aposta sobre o futuro da tecnologia e passa a consumir a capacidade computacional disponível no presente.

## O jogo e a máquina não precisam ser o mesmo produto

O modelo tradicional juntou duas coisas porque isso era necessário. O console ou PC fornecia a capacidade computacional e o jogo era executado localmente. A chegada da nuvem torna possível separar essas duas camadas.

Eu posso comprar um jogo independentemente da máquina que irá executá-lo. Posso ter minha biblioteca em uma plataforma digital e utilizar hardware local quando ele for suficiente. Quando não for, posso utilizar uma infraestrutura remota. O jogo continua sendo meu produto de entretenimento, enquanto a máquina passa a ser um serviço separado.

Isso significa que não precisamos necessariamente de uma “Netflix dos games” para fazer o cloud gaming funcionar. O catálogo de jogos pode continuar sendo um produto das próprias plataformas. Sony, Microsoft e Nintendo podem continuar vendendo jogos, mantendo suas bibliotecas, oferecendo títulos exclusivos e construindo seus próprios ecossistemas. O que muda é que o hardware necessário para executar esses jogos pode ser fornecido por outra camada da indústria.

Uma empresa poderia se especializar exclusivamente em infraestrutura para jogos. Ela não precisaria possuir uma biblioteca de títulos nem negociar exclusividades. Sua função seria disponibilizar máquinas capazes de executar os jogos que o usuário já possui, da mesma forma que um provedor de nuvem fornece servidores para aplicações que pertencem a outras empresas.

Isso permitiria que o mercado de cloud gaming competisse por infraestrutura em vez de competir exclusivamente por catálogo. Um provedor poderia oferecer preços menores, outro poderia ter menor latência, outro poderia disponibilizar GPUs mais modernas e outro poderia ter datacenters melhor posicionados geograficamente.

A biblioteca de jogos continuaria sendo uma camada independente. Ela poderia até ser o principal diferencial competitivo de uma plataforma. O usuário poderia escolher onde comprar seus jogos com base em preço, exclusividades, serviços ou conveniência e, separadamente, escolher onde executar esses jogos com base em capacidade computacional, latência e custo.

Esse desacoplamento é justamente uma das características mais poderosas da computação em nuvem. A aplicação não precisa ser dona do servidor. A empresa não precisa comprar o hardware que executa seu software. A infraestrutura se torna uma camada independente, consumida conforme a necessidade.

Não existe uma razão fundamental para que os jogos sejam diferentes. O jogo pode ser um produto. A máquina pode ser um serviço. E não há necessidade de que os dois sejam vendidos pela mesma empresa.

## O que estamos realmente alugando?

Essa talvez seja a pergunta que a indústria deveria fazer. Estamos falando de dois produtos diferentes que foram colocados no mesmo pacote: acesso aos jogos e acesso à capacidade computacional necessária para executá-los.

Uma assinatura de jogos resolve o primeiro problema. O usuário paga para acessar um catálogo, que pode ser amplo, exclusivo ou simplesmente conveniente. É um modelo de distribuição de software e conteúdo. O cloud gaming resolve o segundo. O usuário paga para utilizar remotamente uma máquina capaz de executar o jogo. É um modelo de infraestrutura.

Não existe razão para que esses dois produtos precisem ser vendidos juntos.

Posso comprar um jogo da Microsoft, Sony, Nintendo ou de qualquer outra loja e executá-lo no meu PC. Se o meu hardware não for suficiente, posso alugar capacidade computacional de um provedor especializado. A empresa que vende o jogo não precisa ser a mesma que fornece a máquina, assim como a empresa que desenvolve uma aplicação não precisa ser dona do servidor que a executa.

Isso cria dois mercados diferentes. De um lado, plataformas competem por jogos, preços, exclusividades, serviços e bibliotecas. De outro, provedores de infraestrutura competem por preço, desempenho, latência, disponibilidade e eficiência operacional.

O problema dos modelos atuais é que frequentemente tratamos esses dois mercados como se fossem um só. A assinatura de jogos tenta vender o catálogo junto com a infraestrutura, enquanto a proposta de cloud gaming acaba sendo apresentada como uma forma diferente de consumir uma assinatura.

Mas não precisa ser assim. Eu posso querer jogar apenas três jogos durante um ano e não ter interesse em centenas de outros títulos. Posso comprar esses três jogos e, quando meu hardware não for suficiente, alugar uma máquina capaz de executá-los. Nesse cenário, não preciso de uma assinatura de jogos. Preciso de um jogo e de capacidade computacional.

A nuvem permite justamente essa separação. O jogo pode continuar sendo um produto comprado ou assinado, enquanto a máquina pode ser uma utility consumida sob demanda.

A indústria passou décadas nos vendendo computadores cada vez mais poderosos para executar jogos cada vez mais exigentes. A nuvem oferece a possibilidade de inverter essa relação: em vez de comprar uma máquina para acompanhar os jogos, podemos alugar a capacidade necessária para executar o jogo que escolhemos.

Talvez o futuro da indústria de jogos não seja uma Netflix dos videogames, mas sim uma AWS dos games.
