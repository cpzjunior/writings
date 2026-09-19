**Resumo:** Defendo que o dilema entre Security e velocidade não se resolve escolhendo um lado, mas aproximando Security da engenharia e levando o conhecimento de segurança para o momento em que as decisões ainda estão sendo construídas. Em vez de depender de gates, aprovações e intervenções manuais, devemos transformar conhecimento especializado em padrões, automação e guardrails proporcionais ao risco. Assim, Security deixa de ser uma etapa que a engenharia precisa esperar e passa a ser uma capacidade integrada ao processo. O objetivo final não é eliminar riscos, mas permitir que a organização aprenda, experimente e inove sabendo quais riscos está assumindo.

------------------------------------------------------------------------

Por muito tempo, minha visão de Security foi provavelmente mais simples do que a realidade da área. Como alguém que atua mais próximo de arquitetura e engenharia do que das disciplinas de segurança, eu tendia a enxergar Security de uma forma relativamente objetiva: existe uma área responsável por segurança, com políticas, ferramentas, processos, avaliações e controles que precisam ser considerados durante a construção das soluções.

Basta olhar um pouco mais de perto, porém, para perceber o quanto essa visão é limitada. Security é uma disciplina muito mais ampla do que o nome sugere. Identidade, aplicações, infraestrutura, cloud, dados, arquitetura, privacidade, fraude, resposta a incidentes, inteligência, terceiros, conformidade e diversas outras dimensões podem estar direta ou indiretamente relacionadas à segurança de uma organização.

Essa amplitude também explica por que é difícil falar de Security como se estivéssemos tratando de uma única função. O ritmo de um time de resposta a incidentes é diferente do ritmo de GRC. Threat Intelligence tem necessidades diferentes de Application Security. Identity and Access Management possui problemas diferentes de Product Security. Cada uma dessas funções tem objetivos, responsabilidades e horizontes temporais próprios.

Este texto não pretende tratar de Security como um todo. A reflexão aqui é mais específica e nasce justamente da fronteira entre Security e aquilo que está mais próximo da minha realidade: arquitetura, engenharia e desenvolvimento de software. É nessa interação que comecei a perceber um dilema que me parece cada vez mais relevante.

Security precisa estar próxima do desenvolvimento para ser efetiva. Precisa compreender as decisões de arquitetura, as tecnologias utilizadas e os riscos associados a cada contexto. Ao mesmo tempo, a forma como essa participação é estruturada pode produzir resultados bastante diferentes. Quando ela depende principalmente de uma sequência de gates, tickets, aprovações, homologações e controles manuais, pode surgir uma etapa adicional entre a engenharia e a tomada de decisão, especialmente quando mecanismos semelhantes são aplicados a contextos com diferentes níveis de risco.

O desafio, portanto, não é escolher entre segurança e velocidade. É construir um modelo no qual Security consiga proteger a organização sem reduzir sua capacidade de aprender, experimentar e inovar. E, quando falamos em velocidade, não estamos falando apenas de entregar software mais rápido. Estamos falando da capacidade de uma organização aprender rapidamente sobre novas tecnologias, avaliar seus riscos, tomar decisões e transformar esse aprendizado em inovação.

## Security e o momento da decisão

Existe um padrão comum nas organizações. O produto define o que precisa ser construído, arquitetura e engenharia definem como a solução será construída e, em algum momento, Security é acionada para avaliar se aquilo atende aos requisitos de segurança.

À primeira vista, esse modelo parece razoável. Cada área possui suas responsabilidades e Security funciona como uma camada especializada de avaliação. O ponto de atenção está no momento em que essa participação acontece. Quando Security entra na discussão depois que grande parte das decisões que influenciam o risco já foi tomada, suas possibilidades de contribuição naturalmente se tornam mais restritas.

Quando um risco é identificado nesse estágio, a arquitetura já pode estar definida, o código já pode ter sido escrito, as dependências já podem ter sido escolhidas e o produto já pode ter expectativas sobre a entrega. Uma decisão de segurança que poderia ter sido incorporada naturalmente durante a definição da solução pode, nesse momento, exigir uma mudança mais significativa, alterar uma escolha tecnológica ou até demandar a revisão de uma parte relevante do que já foi construído.

É nesse ponto que o timing se torna importante. Uma recomendação de segurança feita no início da definição de uma solução pode representar apenas uma decisão arquitetural. A mesma recomendação feita quando a implementação está avançada pode significar retrabalho, alteração de componentes, revisão de integrações ou impacto sobre um cronograma que já está comprometido com uma data de entrega.

Os tickets entram nesse processo como uma forma legítima de registrar essas demandas, organizar responsabilidades e acompanhar sua resolução. O problema não está no ticket em si, mas no que ele representa quando uma decisão relevante de segurança é descoberta apenas em uma etapa avançada do desenvolvimento. A partir desse momento, existe uma tensão entre tratar adequadamente o risco e preservar o prazo e o escopo que já foram estabelecidos para a entrega.

Quando isso acontece de forma recorrente, a interação entre Security e engenharia pode ficar concentrada na avaliação do que já foi produzido, em vez de acontecer durante as decisões que deram origem à solução. A atuação continua sendo importante, mas parte do potencial de contribuição de Security é perdida porque o espaço para alterar a solução com baixo custo já diminuiu.

Há também uma consequência organizacional relevante. Quanto mais distante Security estiver das decisões que originam uma solução, maior pode ser a importância de mecanismos formais para garantir que os requisitos de segurança sejam considerados. Políticas, aprovações, evidências, gates e processos são instrumentos legítimos para isso. Ao mesmo tempo, quando Security participa mais cedo das decisões, parte dessa necessidade pode ser atendida de outras formas, como padrões, automação, componentes reutilizáveis e conhecimento compartilhado.

A questão não é eliminar mecanismos de controle, mas encontrar a forma mais adequada de exercê-los. Em alguns contextos, uma aprovação formal será necessária. Em outros, o mesmo conhecimento pode estar incorporado à arquitetura, à plataforma ou ao próprio processo de desenvolvimento. A forma de exercer esse controle pode variar conforme o risco, o contexto e, principalmente, o momento em que a decisão é tomada.

## O verdadeiro significado de velocidade

Quando falamos que Security precisa acompanhar a velocidade da engenharia, não deveríamos estar falando apenas de tempo de resposta a tickets ou de velocidade de entrega de software. A questão mais importante é a velocidade com que a organização consegue aprender, tomar decisões e transformar esse aprendizado em inovação.

Uma organização de tecnologia precisa experimentar. Precisa testar novas arquiteturas, plataformas, serviços, frameworks e ferramentas. Precisa descobrir rapidamente o que funciona, quais são os riscos, quais são os custos e quais tecnologias podem gerar vantagem competitiva. Esse processo de aprendizado não acontece necessariamente em ciclos trimestrais. Muitas vezes, uma decisão relevante precisa ser tomada em horas ou dias.

Imagine que uma nova tecnologia apareça e que um squad enxergue uma oportunidade estratégica em utilizá-la. Se o processo necessário para que Security avalie essa tecnologia leva semanas ou meses, o impacto pode ir muito além do time to market. A organização perde capacidade de experimentar e, principalmente, de aprender. Enquanto a tecnologia evolui, a oportunidade pode desaparecer e a decisão pode deixar de fazer sentido.

Existe ainda uma consequência menos óbvia. Quando os processos de segurança não acompanham a necessidade da engenharia, pode aumentar a pressão por alternativas. Um time pode buscar outra ferramenta, utilizar um serviço fora dos padrões corporativos ou construir uma integração provisória para conseguir avançar. Isso nem sempre decorre de uma intenção deliberada de contornar controles. Muitas vezes, é simplesmente o resultado de uma necessidade de negócio ou de engenharia que surgiu antes de existir uma resposta adequada no processo formal. O efeito pode ser uma redução da visibilidade sobre aquilo que está sendo utilizado e uma menor oportunidade de influenciar a forma como a tecnologia é adotada.

Por isso, velocidade também é uma dimensão de segurança. Uma Security eficiente precisa ser suficientemente rápida para participar do processo de experimentação enquanto a decisão ainda está sendo construída. Não basta avaliar uma tecnologia depois que o negócio já decidiu utilizá-la. É preciso conseguir entender seus riscos, propor controles proporcionais e estabelecer condições para que a experimentação aconteça de maneira segura.

Essa proximidade também beneficia a própria Security. Tecnologias novas não representam apenas riscos a serem avaliados. Elas também exigem aprendizado. Novos modelos arquiteturais, serviços de cloud, ferramentas de desenvolvimento e tecnologias emergentes podem introduzir riscos que não se encaixam perfeitamente nos controles existentes. Estar próxima da engenharia permite que Security compreenda essas mudanças no mesmo momento em que elas estão sendo exploradas pela organização.

O objetivo não é simplesmente reduzir o tempo de entrega. É reduzir o intervalo entre uma hipótese, uma experimentação, o aprendizado sobre seus riscos e uma decisão consciente sobre sua adoção. Quando uma organização consegue encurtar esse ciclo, ela não apenas entrega mais rapidamente. Ela aumenta sua capacidade de aprender, adaptar-se e inovar sem abrir mão de uma avaliação consciente dos riscos.

## Security como parte da engenharia

Talvez a mudança mais importante seja deixar de pensar em Security como uma etapa do processo de desenvolvimento e começar a tratá-la como uma das disciplinas que participam desse processo. Segurança não deveria ser algo que se verifica apenas ao final de uma solução. Deveria ser uma das dimensões consideradas enquanto a solução ainda está sendo desenhada e as decisões ainda podem ser alteradas com menor custo.

Security não deveria aparecer apenas quando existe algo para aprovar. Deveria participar da definição da solução. Um profissional de Security próximo da engenharia pode discutir com o arquiteto quais são os limites de confiança da solução, como será feita a autenticação entre serviços, quais dados serão tratados, onde estarão os pontos de exposição, quais privilégios serão necessários, como serão armazenados os secrets, quais dependências externas serão utilizadas e quais ameaças são realmente relevantes naquele contexto. O valor dessa participação está justamente em acontecer enquanto essas decisões estão sendo tomadas, e não depois que a arquitetura já está consolidada.

Essa participação é diferente de colocar alguém dentro do squad para fiscalizar o trabalho. A proximidade com a engenharia deveria existir para permitir uma colaboração mais efetiva na construção da solução, e não apenas para acompanhar o que os desenvolvedores estão fazendo.

Nesse sentido, gosto da ideia de tratar o profissional de Security como um parceiro do arquiteto de soluções. Produto, arquitetura e engenharia precisam decidir como determinada solução será construída. Security contribui para entender quais riscos essa arquitetura introduz, quais ameaças são relevantes e como esses riscos podem ser mitigados sem comprometer desnecessariamente o objetivo do sistema.

Essa proximidade também muda a natureza da conversa. Em vez de discutir apenas se uma determinada tecnologia pode ou não ser utilizada, é possível discutir em quais condições ela pode ser utilizada com segurança. Em vez de descobrir posteriormente que determinada arquitetura possui uma exposição indesejada, é possível identificar essa exposição enquanto as alternativas ainda estão sendo avaliadas.

Isso não significa transferir para Security a responsabilidade pela solução. O produto continua responsável pelo produto, a engenharia pela implementação e as decisões arquiteturais pelas pessoas responsáveis pela solução. Security acrescenta conhecimento especializado sobre riscos e controles a essa discussão.

Essa distinção é importante porque integrar Security à engenharia não significa tornar Security responsável por tudo que envolve segurança. Significa distribuir melhor o conhecimento necessário para que as decisões sejam tomadas por quem possui o contexto, com a participação de quem possui a especialização.

A pergunta deixa de ser apenas “Security aprovou?” e passa a ser “A solução foi construída considerando os riscos relevantes para o seu contexto e as medidas necessárias para tratá-los?”. A mudança é menos sobre retirar uma etapa de aprovação e mais sobre trazer conhecimento de segurança para o momento em que as decisões ainda estão sendo construídas.

Essa integração traz uma exigência para o próprio profissional de Security. Não basta estar presente nas reuniões do squad ou conhecer o ciclo de desenvolvimento como um processo descrito em documentação. Para participar efetivamente da engenharia, é preciso compreender o processo como prática.

Uma forma concreta de desenvolver essa compreensão é construir. Uma prova de conceito pode percorrer todo o caminho de uma solução, desde a definição do requisito e da arquitetura até o desenvolvimento, pull request, pipeline, testes, controles de segurança, deploy e observabilidade. O objetivo não é transformar o Security Engineer em desenvolvedor, mas proporcionar experiência prática suficiente para compreender as restrições, incentivos e trade-offs que fazem parte do cotidiano de engenharia.

A experiência prática também muda a forma como Security avalia suas próprias recomendações. Ao implementar um controle em uma solução real, o profissional passa a enxergar as dependências, o esforço de implementação e os impactos que aquela decisão produz no pipeline e no ciclo de desenvolvimento. Essa perspectiva é difícil de obter apenas pela definição de políticas ou pela revisão de documentos e ajuda a avaliar se determinado controle está produzindo redução de risco proporcional à fricção que introduz.

Se uma recomendação exige processos manuais excessivos, gera muitas exceções ou é difícil de implementar, isso pode ser um sinal de que o controle precisa ser redesenhado, automatizado ou incorporado a um padrão arquitetural ou componente de plataforma.

Quanto mais Security entende como software é efetivamente construído, melhor consegue avaliar não apenas os riscos de uma solução, mas também a forma mais adequada de tratá-los. Da mesma forma, quanto mais a engenharia entende as razões por trás dos controles, maior a possibilidade de que segurança seja incorporada às próprias decisões técnicas, reduzindo a necessidade de intervenções posteriores.

## Do gate ao guardrail

Isso nos leva a uma distinção importante entre gates e guardrails. Um gate condiciona a continuidade do fluxo ao atendimento de uma condição ou à tomada de uma decisão. Um guardrail estabelece os limites dentro dos quais o trabalho pode avançar, podendo incorporar verificações e bloqueios diretamente ao ambiente de engenharia. A diferença está menos na existência ou não de bloqueios e mais na forma como eles são incorporados ao processo. No modelo baseado em gates, determinadas decisões precisam ser explicitamente avaliadas antes que o fluxo avance. No modelo baseado em guardrails, parte dessas condições pode estar incorporada ao próprio processo de desenvolvimento.

Ambos podem ser necessários. Uma mudança envolvendo dados altamente sensíveis, privilégios elevados ou uma exposição crítica pode justificar uma avaliação humana. Em outros contextos, especialmente quando a decisão é recorrente e previsível, controles automatizados podem oferecer uma forma mais eficiente de tratar o mesmo risco.

Nem toda decisão possui o mesmo nível de risco e, por isso, nem toda decisão precisa exigir o mesmo nível de intervenção. Quanto mais recorrente, previsível e baixo for o risco, maior pode ser a capacidade de tratá-lo por meio de padrões, automação e self service. À medida que aumentam a criticidade, a exposição ou a complexidade da decisão, cresce também o valor da análise especializada de Security.

Essa é a lógica de uma abordagem baseada em risco: o nível de controle deve ser proporcional ao risco que se pretende tratar. O objetivo não deveria ser maximizar a quantidade de controles, mas encontrar uma forma eficiente de reduzir os riscos relevantes sem introduzir uma fricção desproporcional ao processo de engenharia. Um controle que exige intervenção manual recorrente de dezenas de squads pode consumir uma quantidade significativa de capacidade especializada, mesmo quando sua aplicação é justificável em determinados contextos.

Nesse contexto, automação deixa de ser apenas uma iniciativa de eficiência e passa a ser uma estratégia de escala. Se cinquenta squads precisam implementar o mesmo controle, o conhecimento utilizado nessas decisões pode ser transformado em um componente, uma política, um pipeline, um template ou uma capacidade de plataforma que já incorpore esse controle de forma segura. Em vez de reproduzir a mesma análise em diferentes contextos, parte desse conhecimento pode ser disponibilizada diretamente para a engenharia.

Essa transformação permite que Security concentre sua capacidade humana onde sua participação agrega mais valor: decisões novas, complexas, de alto impacto ou que dependem de contexto. Para aquilo que é recorrente e previsível, o conhecimento pode ser incorporado à própria engenharia.

Security não escala de forma sustentável adicionando pessoas na mesma proporção em que crescem os squads. Escala quando transforma conhecimento especializado em capacidades reutilizáveis e permite que controles sejam aplicados de forma consistente por muitos times. Sempre que possível, isso faz com que o caminho seguro seja também o caminho mais simples para a engenharia.

## Tempo e escala: Security além da fila

Existe uma consequência operacional importante quando Security passa a fazer parte do ciclo de engenharia. Se a engenharia toma decisões em horas ou dias, o tempo necessário para uma avaliação de segurança precisa ser compatível com o horizonte temporal dessas decisões. Isso não significa transformar toda demanda em atendimento urgente, mas evitar que a análise de segurança opere em um ritmo completamente dissociado do processo de engenharia.

Isso também muda a discussão sobre escala. O desafio não é simplesmente fazer Security responder mais rapidamente às solicitações que recebe, mas reduzir a quantidade de decisões que dependem de uma resposta manual específica. Uma tecnologia comum e de baixo risco pode ser utilizada por meio de padrões previamente definidos. Uma arquitetura recorrente pode ter mecanismos de segurança já incorporados. Uma política simples pode ser validada automaticamente. Uma vulnerabilidade conhecida pode, sempre que possível, ser detectada e tratada pelo pipeline.

Quanto mais previsível for uma decisão, menor tende a ser a necessidade de uma intervenção humana específica. Quando o caminho seguro está automatizado, o squad não precisa esperar. Quando um padrão arquitetural já incorpora os controles necessários, não é necessário reproduzir a mesma análise a cada nova implementação. Quando Security participa da discussão arquitetural, uma decisão pode ser tratada enquanto a solução ainda está sendo construída, reduzindo a necessidade de encaminhá-la posteriormente para uma nova avaliação.

É nesse ponto que os tickets revelam uma questão de capacidade. Eles continuam sendo úteis para registrar demandas, responsabilidades e decisões, mas não eliminam a dependência estrutural entre muitos squads e uma capacidade especializada de Security. Se diferentes times precisam consultar Security individualmente para tomar decisões semelhantes, a organização está repetindo interações em torno de um conhecimento que poderia ser reutilizado.

Uma Security que escala precisa transformar conhecimento especializado em capacidades que possam ser utilizadas por muitos times ao mesmo tempo. Isso inclui padrões arquiteturais, automação, componentes reutilizáveis, documentação, capacitação, guardrails e plataformas que incorporem controles diretamente ao processo de desenvolvimento.

Novas tecnologias podem ajudar nesse processo. Inteligência artificial, por exemplo, pode ampliar a capacidade dos profissionais de Security em atividades de análise, triagem, orientação e identificação de riscos. Pode tornar conhecimento especializado mais acessível e reduzir o esforço necessário para determinadas tarefas. Mas isso, por si só, não muda o modelo operacional. Se o processo continuar dependendo de tickets, aprovações e intervenções individuais, ferramentas mais sofisticadas podem apenas tornar esse fluxo mais eficiente, sem eliminar sua dependência de interações específicas.

O ganho de escala acontece quando o conhecimento deixa de depender de uma interação individual e passa a fazer parte do próprio processo de engenharia. Um padrão pode ser reutilizado por dezenas de squads. Um controle pode ser automatizado. Uma capacidade de plataforma pode eliminar a necessidade de implementação manual. Uma orientação pode estar disponível no momento em que a decisão é tomada.

Isso também redefine o papel do time central de Security. Em vez de concentrar sua capacidade na revisão individual de tudo que acontece na organização, pode direcionar sua atuação humana para decisões novas, complexas ou de maior impacto, enquanto investe na construção das capacidades que permitem aos demais times tomar decisões recorrentes com maior autonomia.

Escalar Security não significa simplesmente atender mais solicitações ou responder mais tickets. Significa fazer com que o conhecimento especializado consiga influenciar um número muito maior de decisões de engenharia sem exigir uma interação humana proporcional ao número dessas decisões.

## Segurança como parte da cultura

No final, existe uma dimensão que nenhum processo, ferramenta ou estrutura organizacional resolve sozinho: cultura. Não no sentido de campanhas, treinamentos obrigatórios ou declarações sobre “security first”, mas na forma como a organização toma decisões quando segurança, velocidade e inovação entram em tensão.

Uma organização madura não deveria depender de Security para lembrar continuamente à engenharia que segurança importa. Da mesma forma, Security não deveria depender de processos para lembrar continuamente à engenharia que determinados controles precisam ser cumpridos. O conhecimento sobre risco precisa estar presente onde as decisões são tomadas.

Isso exige aprendizado dos dois lados. Security precisa conhecer a engenharia não apenas para entender como o software é construído, mas para compreender como a organização aprende, experimenta e transforma tecnologia em produto. Engenharia precisa conhecer segurança não apenas para cumprir controles, mas para incorporar risco às próprias decisões técnicas.

É nesse ponto que o dilema muda de natureza. A pergunta deixa de ser quanto controle a organização precisa exercer sobre a engenharia e passa a ser quanto conhecimento de segurança consegue distribuir sem transformar cada decisão em uma dependência de Security.

O objetivo não é fazer Security correr atrás da engenharia, tampouco fazer a engenharia esperar por Security. É reduzir as situações em que uma precisa esperar pela outra. Para isso, Security precisa estar próxima o suficiente para participar das decisões e transformar conhecimento especializado em contexto, padrões e capacidades que possam ser utilizados pela engenharia.

Talvez o verdadeiro equilíbrio entre controle e velocidade esteja justamente aí: não em eliminar controles, nem em acelerar indefinidamente processos de aprovação, mas em colocar cada mecanismo no lugar em que ele produz mais valor.

Como arquiteto de soluções, é dessa perspectiva que vejo esse dilema. Não a partir da responsabilidade de definir como Security deve operar, mas da experiência de estar no ponto em que decisões de produto, arquitetura, engenharia e segurança precisam convergir. É nesse ponto que fica evidente que segurança e velocidade não precisam disputar o mesmo espaço. O desafio está em criar mecanismos que permitam que as duas avancem juntas.

Uma organização capaz de inovar precisa aprender rapidamente sobre tecnologia, mas também sobre os riscos que essa tecnologia introduz. Não para eliminar o risco, mas para distinguir aquilo que precisa ser mitigado, aquilo que pode ser aceito e aquilo que não pode ser assumido.

Security, nesse contexto, deixa de ser apenas uma função que protege aquilo que a organização construiu. Passa a contribuir para que ela consiga decidir, com consciência sobre o risco, aquilo que ainda pode construir.
