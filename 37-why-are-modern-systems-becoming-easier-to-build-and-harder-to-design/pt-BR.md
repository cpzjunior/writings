# Por que sistemas modernos estão ficando mais fáceis de construir e mais difíceis de projetar?

_Abstrações de cloud, o paradoxo da escolha e a inteligência artificial estão mudando a natureza da arquitetura de soluções mais rápido do que conseguimos nos adaptar._

**Resumo:** Exploro os motivos pelos quais sistemas modernos estão mais fáceis de construir, mas mais difíceis de projetar: cloud, serviços gerenciados, SaaS e IA reduziram o custo de implementar soluções, mas ampliaram o espaço de escolhas e tornaram o julgamento arquitetural o principal gargalo. Nesse cenário, experiência significa saber eliminar alternativas, avaliar trade-offs, reconhecer dependências ocultas e preservar a reversibilidade das decisões. Por isso, proponho que a arquitetura de soluções precisa de um corpo de conhecimento mais sistemático, algo próximo de um “PMBOK de Solution Architecture”, para organizar o processo de decisão sem substituir o julgamento do arquiteto.

------------------------------------------------------------------------

Tenho um certo vício em assistir a vídeos de System Design. Gosto particularmente daqueles em que alguém explica como uma grande empresa resolveu um problema em escala: como uma plataforma processa milhões de eventos, como uma aplicação lida com picos de tráfego, como uma empresa estruturou sua arquitetura de dados ou como determinado serviço foi dividido em dezenas de componentes. É interessante observar uma arquitetura depois que as principais decisões já foram tomadas. Cada componente parece ter um propósito claro e, olhando para trás, muitas escolhas parecem quase óbvias.

A situação é diferente quando precisamos desenhar uma arquitetura do zero. Já desenhei dezenas de arquiteturas ao longo da minha carreira. Já precisei tomar decisões sobre integração, dados, escalabilidade, disponibilidade, segurança, cloud e operação em contextos bastante diferentes. Sei que existem várias maneiras razoáveis de resolver a maioria dos problemas que encontro. E, ainda assim, frequentemente me sinto sobrecarregado quando começo um desenho do zero. Não por falta de experiência, mas pelo excesso de opções.

O ponto de partida deveria ser simples: quais são os requisitos que a solução precisa atender? Qual disponibilidade é necessária? Qual volume de dados esperamos? Que latência é aceitável? Quais são as restrições de custo, segurança, operação e compliance? Quão importante é a capacidade de evoluir ou migrar a solução no futuro? Em teoria, essas respostas deveriam reduzir o espaço de decisão. Na prática, mesmo depois de estabelecermos as restrições, ainda podemos chegar a dezenas de soluções tecnicamente viáveis.

E é aí que costumo voltar para o arroz com feijão. Escolho os serviços da AWS que já conheço bem, recorro a padrões que já funcionaram em outros projetos e evito, quando não existe uma razão forte para isso, introduzir uma tecnologia ou uma arquitetura completamente nova. Pode haver conservadorismo nessa escolha. Pode haver também uma certa falta de experimentação. Mas existe algo mais pragmático: conheço melhor os riscos daquilo que já usei.

Experimentar uma solução nova em outra cloud, introduzir múltiplas clouds ou adotar uma tecnologia que ainda não conheço profundamente pode produzir uma arquitetura tecnicamente interessante. Mas também pode resultar em uma solução que não atende tão bem aos requisitos, que a equipe tem dificuldade para operar ou que se transforma em dívida técnica quando a realidade do projeto se mostra diferente daquilo que imaginávamos. A responsabilidade pela decisão não desaparece porque a tecnologia é nova.

O problema é que as consequências nem sempre aparecem imediatamente. A insatisfação com uma escolha, o débito técnico e até mesmo o arrependimento de ter adotado determinada tecnologia podem surgir meses depois da implementação, quando o sistema já acumulou dados, integrações e dependências ao seu redor. Uma decisão que parecia reversível pode então atrasar um projeto ou tornar sua substituição tão custosa que deixa de ser uma alternativa viável.

Já escrevi sobre parte desse dilema em [“Cloud Computing: escolhendo além do default”](https://cpzjunior.substack.com/p/cloud-computing-escolhendo-alem-do), discutindo por que não deveríamos aceitar automaticamente as escolhas padrão oferecidas pela cloud. O problema que me interessa aqui é um passo adiante: mesmo quando sabemos que existem alternativas ao default, como decidimos quais delas realmente merecem ser consideradas?

Quanto mais tecnologias conhecemos, maior se torna o espaço de soluções que conseguimos enxergar. E quanto maior esse espaço, mais difícil fica avaliar cada alternativa com a profundidade necessária para tomar uma decisão realmente consciente.

Isso acontece justamente enquanto construir sistemas nunca foi tão fácil. A cloud transformou boa parte da infraestrutura em serviços consumíveis. SaaS transformou capacidades inteiras em APIs. Plataformas gerenciadas eliminaram uma quantidade enorme de trabalho operacional. E a inteligência artificial está reduzindo também o custo de implementar e experimentar software.

O resultado é um paradoxo: estamos ficando cada vez melhores em construir soluções, mas isso não significa que estamos ficando igualmente melhores em decidir quais soluções construir.

Não estou argumentando que sistemas modernos sejam piores, nem que deveríamos voltar a administrar servidores, configurar infraestrutura manualmente ou evitar novas tecnologias. Seria justamente o contrário do que esses avanços representam. O ponto é que, ao tornar determinadas partes do problema mais fáceis, essas tecnologias também mudaram a natureza das decisões que permanecem.

Quando o custo de implementar alternativas cai drasticamente, o problema deixa de ser apenas como construir e passa a ser, cada vez mais, como escolher.

## A complexidade não desapareceu. Ela mudou de lugar.

Uma das grandes virtudes da abstração é justamente permitir que deixemos de nos preocupar com determinados detalhes. Não precisamos conhecer a implementação interna de um serviço para utilizá-lo. Esse é um dos princípios fundamentais por trás de boa parte da engenharia de software moderna.

A cloud levou esse princípio a uma escala enorme. Durante muito tempo, construir um sistema significava lidar diretamente com uma quantidade considerável de infraestrutura. Servidores, storage, redes, balanceadores, capacidade, replicação e recuperação de desastres faziam parte do problema porque não havia como simplesmente delegá-los.

Hoje, grande parte disso pode ser consumida como serviço. Um banco de dados pode ser provisionado em minutos. Uma fila pode ser criada por configuração. Capacidade pode ser ajustada automaticamente. Uma função pode ser executada sem que precisemos administrar o servidor onde ela roda.

Isso reduziu enormemente o custo de implementação. Mas reduzir a complexidade de uma camada não significa necessariamente reduzir a complexidade do sistema como um todo.

A complexidade pode simplesmente mudar de lugar. Em vez de precisarmos saber como construir cada componente, precisamos decidir como combiná-los. Um serviço individual pode ser simples de consumir, enquanto o sistema formado pela composição de dezenas deles pode apresentar comportamentos difíceis de prever.

Essa mudança também altera o tipo de conhecimento exigido do arquiteto. Já não basta saber como implementar determinado mecanismo, nem é necessário conhecer todos os detalhes de sua implementação. É preciso entender as propriedades relevantes para a decisão: suas garantias, seus limites, seus modelos de falha, seus custos e, principalmente, como essas propriedades interagem com as dos demais componentes.

## O paradoxo da escolha

Existe uma ideia conhecida como paradoxo da escolha: aumentar o número de alternativas disponíveis não produz necessariamente decisões melhores. O chamado “dilema do supermercado” ilustra bem isso. Diante de uma prateleira com dezenas de opções aparentemente semelhantes, escolher pode se tornar mais difícil, não mais fácil. Depois de determinado ponto, comparar alternativas exige tanto esforço que acabamos preferindo aquilo que já conhecemos, simplesmente porque o custo de decidir é menor.

A arquitetura de soluções parece ter encontrado uma versão própria desse problema. Durante muito tempo, muitas decisões arquiteturais eram limitadas pelo que era possível construir com os recursos disponíveis. Hoje, para uma parcela crescente dos problemas, a situação é quase inversa. Temos dezenas de serviços capazes de resolver uma mesma necessidade e inúmeras formas de combiná-los. O problema deixou de ser encontrar uma tecnologia capaz de fazer algo e passou a ser decidir qual das tecnologias capazes de fazê-lo deveria ser utilizada.

E a dificuldade não cresce apenas com o número de alternativas. Cada alternativa possui propriedades diferentes e cria novas possibilidades de composição. Escolher um banco de dados não é uma decisão isolada. A escolha afeta o modelo de dados, os mecanismos de integração, as estratégias de backup, a observabilidade, os custos operacionais e até as tecnologias que passam a fazer sentido nas camadas seguintes. O espaço de decisão pode crescer rapidamente à medida que essas escolhas se combinam.

É aqui que a experiência do arquiteto se torna particularmente importante. Um arquiteto experiente não avalia todas as possibilidades. Ele utiliza conhecimento acumulado, restrições do problema e heurísticas para eliminar rapidamente aquilo que não precisa ser considerado. Parte importante da experiência arquitetural é justamente saber quais opções podem ser descartadas sem uma investigação mais profunda.

Meu “arroz com feijão” da AWS é, em grande medida, uma consequência disso. São tecnologias que conheço, cujas propriedades e limitações já encontrei em projetos anteriores e sobre as quais consigo estimar melhor os riscos. Quando escolho uma solução conhecida, não estou necessariamente buscando a tecnologia mais sofisticada. Estou reduzindo deliberadamente o espaço de decisão para conseguir dedicar atenção às decisões que realmente importam.

O risco aparece quando essa heurística deixa de ser uma escolha consciente e passa a ser apenas um reflexo. Se sempre escolho aquilo que conheço porque existem opções demais para avaliar, posso estar trocando sobrecarga cognitiva por dívida arquitetural.

A abundância de alternativas, portanto, não torna apenas o problema mais amplo. Ela aumenta a importância de saber quais alternativas não precisam ser consideradas. O desafio arquitetural passa a ser menos conhecer todas as possibilidades e mais construir critérios suficientemente bons para eliminá-las.

## Quando a abstração esconde limitações e dependências

Existe ainda outro efeito da abstração que merece atenção. Quando consumimos serviços gerenciados, passamos a enxergar apenas parte da arquitetura da qual dependemos. Nosso diagrama representa aquilo que decidimos modelar, não necessariamente tudo aquilo que sustenta o sistema.

Isso não é necessariamente um problema. Não precisamos conhecer todos os detalhes de uma plataforma para utilizá-la corretamente. O problema aparece quando confundimos a simplicidade da interface com independência entre os componentes.

Quando colocamos um S3, uma Lambda ou um DynamoDB em um diagrama, o que exatamente estamos representando? Um storage de objetos, uma função executável, um banco de dados. Mas o que existe por baixo dessas abstrações? Como os dados são distribuídos e replicados? Como os recursos são provisionados e compartilhados? Quais são os limites dessas abstrações? Quais dependências existem entre elas e a infraestrutura que as sustenta? E, principalmente, quais dessas propriedades podem se tornar relevantes quando alguma coisa falha?

Não precisamos conhecer todos esses mecanismos para utilizar os serviços. Mas isso não significa que eles deixem de existir ou que suas propriedades sejam irrelevantes para determinadas decisões arquiteturais.

Um sistema pode parecer distribuído entre diferentes serviços, regiões ou até diferentes clouds e ainda depender de componentes comuns que não aparecem no nosso diagrama. A diversidade que enxergamos na superfície não garante independência em todas as camadas.

O caso da Cloudflare em 2022 é um exemplo desse tipo de dependência invisível, embora eu já tenha explorado aquele incidente em outro artigo. Para esta discussão, basta a ideia: abstrações podem esconder não apenas detalhes de implementação, mas também dependências e pontos comuns de falha relevantes para a resiliência de uma arquitetura.

O mesmo vale para os próprios provedores de cloud. Diferentes plataformas podem oferecer uma enorme variedade de serviços, mas depender dos mesmos fornecedores ou de componentes compartilhados em partes de sua cadeia tecnológica. A abstração nos permite tratar esses serviços como blocos independentes porque é assim que precisamos consumi-los. Isso não significa que sejam completamente independentes na realidade.

Esse é um dos limites importantes da abstração arquitetural. Podemos deliberadamente ignorar detalhes que não são relevantes para uma determinada decisão, mas precisamos reconhecer quando eles deixam de ser irrelevantes. Uma dependência que pode ser perfeitamente aceitável para uma aplicação comum pode se tornar crítica quando estamos projetando alta disponibilidade, disaster recovery ou uma estratégia de multi-cloud.

O arquiteto não precisa conhecer tudo o que existe por baixo de uma abstração. Precisa saber o suficiente para reconhecer quando suas limitações ou dependências podem mudar a decisão que está tomando.

## A IA agrava o problema

A inteligência artificial adiciona outra dimensão a essa transformação porque reduz ainda mais o custo de implementação. A discussão sobre IA na engenharia de software costuma se concentrar em produtividade: quanto código conseguimos produzir, quantos testes conseguimos gerar ou quanto tempo conseguimos economizar. Esses efeitos são relevantes, mas existe uma consequência arquitetural menos discutida.

Se fica mais barato implementar uma alternativa, fica mais barato também experimentar alternativas. Isso é positivo. Experimentação é uma das melhores formas de reduzir incerteza. O problema é que a redução do custo de experimentação também aumenta a quantidade de soluções que podemos colocar em prática antes mesmo de termos clareza sobre qual delas deveríamos escolher.

A IA é uma evidência particularmente clara desse fenômeno. Há uma quantidade crescente de modelos disponíveis, oferecidos por diferentes provedores, com diferenças de capacidade, custo, latência, contexto e comportamento. Novos modelos surgem continuamente, versões são atualizadas e benchmarks mudam. Para quem está projetando uma solução, isso significa que até mesmo uma decisão aparentemente simples, como escolher um modelo para uma determinada tarefa, pode envolver um espaço de alternativas difícil de acompanhar.

E o problema não termina no modelo. Uma solução que utiliza IA pode envolver estratégias de inferência, mecanismos de recuperação, bancos vetoriais, técnicas de prompting, ferramentas, agentes e diferentes formas de integração. Cada uma dessas escolhas abre novas possibilidades de composição. A tecnologia não apenas adicionou mais uma ferramenta ao catálogo. Ela ampliou rapidamente o espaço de soluções que um arquiteto pode considerar.

A IA também reduz drasticamente o custo de experimentar essas alternativas. Uma ideia que antes exigiria dias de desenvolvimento pode ser transformada em um protótipo em poucas horas. Isso é uma vantagem inequívoca. Mas existe uma assimetria interessante: o custo de construir e testar uma solução pode cair muito mais rapidamente do que o custo de compreender suas consequências arquiteturais.

Podemos, portanto, chegar à implementação antes de chegar à compreensão. Podemos construir um protótipo funcional, integrá-lo a outros serviços e até colocá-lo em produção antes de termos uma visão suficientemente clara sobre seus custos, limitações, dependências e comportamento em diferentes condições.

É justamente por isso que considero a IA uma evidência, e não apenas mais um exemplo, do fenômeno discutido neste artigo. Ela mostra de forma particularmente evidente que estamos reduzindo o custo de transformar decisões em software sem reduzir na mesma proporção o custo de tomar boas decisões.

A IA não elimina o problema da arquitetura. Ela torna mais evidente a diferença entre conseguir construir alguma coisa e saber se deveríamos construí-la daquela maneira.

E essa diferença importa porque o custo de uma decisão arquitetural raramente aparece no momento em que ela é tomada.

## O custo de uma decisão aparece depois

Uma decisão arquitetural ruim não precisa produzir imediatamente um sistema quebrado. Muitas vezes, ela produz um sistema que funciona perfeitamente dentro das premissas existentes no momento da escolha.

O problema aparece quando essas premissas mudam. Uma decisão pode introduzir acoplamento a um fornecedor, um modelo de dados difícil de migrar, uma dependência operacional, uma arquitetura difícil de escalar ou uma tecnologia que exige competências muito específicas. Enquanto o sistema cresce, aquilo que parecia uma escolha simples se torna cada vez mais difícil de reverter.

Technical debt encontra uma boa analogia na dívida de cartão de crédito. O problema não é apenas o que deixamos para depois, mas os juros que começam a correr enquanto adiamos a correção. Na arquitetura, esses juros são pagos em forma de complexidade, acoplamento e custo de mudança.

Uma alteração que inicialmente exigia apenas uma pequena adaptação pode, alguns anos depois, envolver migração de dados, alteração de contratos, mudanças em integrações, treinamento de equipes, reescrita de componentes e interrupções operacionais. O sistema cresce ao redor da escolha original, e cada nova dependência torna sua reversão mais cara.

Por isso, technical debt não é apenas trabalho acumulado. É o custo crescente de manter uma decisão que já deixou de ser adequada.

Existe uma diferença importante entre custo de implementação e custo de reversibilidade. Um serviço gerenciado pode resolver um problema em horas. Uma arquitetura construída ao redor dele pode permanecer por anos. Quanto mais o sistema passa a depender daquela escolha, maior tende a ser o custo para abandoná-la.

Isso muda a forma como uma decisão arquitetural deveria ser avaliada. Não basta perguntar quanto custa implementar uma solução. É preciso perguntar também quanto custa mudá-la, quais premissas sustentam essa escolha e quão fácil será revertê-la caso essas premissas deixem de ser verdadeiras.

Essa preocupação se torna ainda mais importante justamente porque a tecnologia tornou a adoção tão fácil. Quanto menor o custo para começar, maior a tentação de adiar a pergunta sobre quanto custará sair.

## O problema dos frameworks

É nesse contexto que comecei a perceber outra coisa. Minha formação em gestão de projetos me acostumou à ideia de que uma disciplina pode construir um corpo de conhecimento relativamente estável, capaz de organizar conceitos, práticas e decisões mesmo quando as ferramentas e metodologias utilizadas mudam.

Em arquitetura de soluções, não vejo o mesmo nível de consolidação. Existem frameworks, métodos e práticas bastante úteis, mas eles parecem resolver partes diferentes do problema. Muitas vezes, cabe ao próprio arquiteto combinar essas peças para construir seu processo de decisão.

O TOGAF é um bom exemplo. Ele tem uma função importante e nunca pretendeu ser um manual de System Design. Foi concebido para Enterprise Architecture, com uma preocupação muito mais ampla com organização, capacidades, governança, processos e alinhamento estratégico. Por isso, não me parece justo criticá-lo por não resolver um problema que não é exatamente o seu.

Ainda assim, existe um desconforto legítimo quando olhamos para a velocidade com que o ambiente tecnológico mudou. A estrutura de conhecimento necessária para discutir arquitetura parece mudar mais rapidamente do que conseguimos consolidá-la. E isso cria uma tensão difícil de resolver: se um framework incorpora continuamente novas tecnologias e práticas, corre o risco de se tornar rapidamente obsoleto; se permanece estável, corre o risco de se afastar da realidade na qual os arquitetos estão tomando decisões.

O arc42 ilustra outro lado dessa questão. Ele está muito mais próximo da prática de arquitetura de software e oferece uma estrutura pragmática para documentar contexto, requisitos de qualidade, decisões arquiteturais, building blocks, runtime e deployment. É extremamente útil para organizar e comunicar uma arquitetura. Mas documentar uma decisão não é exatamente o mesmo que estruturar o processo que levou a ela.

O mesmo vale para outras práticas. Um Architecture Decision Record ajuda a registrar uma decisão. C4 ajuda a representar a arquitetura. ATAM ajuda a explorar determinados trade-offs. Cada uma dessas abordagens resolve um problema real e pode ser bastante útil. O que sinto falta é de uma estrutura que conecte essas práticas em um processo abrangente de decisão arquitetural.

Um ADR pode registrar que três alternativas foram consideradas e que uma delas foi escolhida. Mas registrar uma decisão não é o mesmo que estruturar o processo que levou a ela. Quais critérios deveriam ser considerados? Como avaliar os trade-offs? Como ponderar custo, risco, complexidade operacional, capacidade da equipe, reversibilidade e dependência de fornecedores? Quando uma decisão é suficientemente importante para ser formalizada? Quando deveria ser revisitada?

Essas perguntas continuam dependendo, em grande medida, da experiência e do julgamento de quem está projetando o sistema.

Talvez seja justamente por isso que, na prática, seja tão comum encontrar uma arquitetura representada diretamente pelos componentes de uma cloud em um Draw.io, Lucidchart, Miro ou ferramenta equivalente, sem que nenhum framework de arquitetura apareça explicitamente no processo.

O diagrama começa a ser construído a partir dos serviços disponíveis. Uma API aqui, uma fila ali, um banco gerenciado, alguma função serverless, talvez um serviço de observabilidade. A arquitetura emerge da composição dos componentes.

Isso não significa que não exista raciocínio arquitetural. Existe. O problema é que boa parte dele permanece implícita. O diagrama mostra o que foi escolhido, mas não necessariamente mostra por que foi escolhido, quais alternativas foram consideradas, quais premissas sustentam a decisão ou quanto custaria desfazê-la.

E talvez essa seja a lacuna que realmente me incomoda. Não sinto falta de um framework que me diga qual tecnologia devo utilizar. Sinto falta de um corpo de conhecimento que ajude a estruturar e comunicar decisões arquiteturais sem depender exclusivamente da experiência individual de cada arquiteto.

## Um PMBOK de Solution Architecture

Foi nesse ponto que comecei a entender melhor aquela sensação inicial de que faltava alguma coisa. Não sinto falta de um framework que me diga qual tecnologia utilizar. Isso seria inviável em um ambiente que muda tão rapidamente. Sinto falta de algo mais próximo do que o PMBOK representa para gestão de projetos: um corpo de conhecimento que forneça uma linguagem, princípios e estruturas para organizar o processo de decisão sem precisar prescrever a solução.

Quando falo em um “PMBOK de Solution Architecture”, não estou imaginando um manual que diga qual banco de dados, cloud ou padrão arquitetural devemos escolher. A ideia seria ter uma referência que ajude o arquiteto a estruturar o problema e tornar explícito o raciocínio por trás das decisões, sem transformar arquitetura em um processo mecânico.

O arc42 chega bastante perto de alguns desses objetivos. Ele oferece uma estrutura pragmática para organizar e comunicar uma arquitetura e é uma ferramenta bastante útil. Mas também evidencia a distinção que estou tentando fazer: estruturar e documentar uma arquitetura não é exatamente o mesmo que estruturar o processo de decisão que levou até ela.

O mesmo vale para outras práticas. ADRs ajudam a registrar decisões, C4 ajuda a representar arquiteturas e ATAM ajuda a explorar determinados trade-offs. Cada uma dessas abordagens resolve um problema real. O que sinto falta é de uma estrutura que conecte essas práticas em um processo mais abrangente, sem exigir que cada arquiteto monte sozinho esse processo a partir de diferentes referências.

Talvez exista uma razão para isso. Arquitetura é profundamente contextual, e decisões arquiteturais raramente possuem uma resposta objetivamente correta. Uma metodologia excessivamente prescritiva poderia criar uma falsa sensação de precisão ou transformar julgamento arquitetural em cumprimento de etapas. Não faria sentido substituir a experiência do arquiteto por um checklist que tentasse determinar a arquitetura correta para cada situação.

Ainda assim, acredito que seja possível sistematizar parte desse conhecimento. A gestão de projetos oferece uma referência interessante. O PMBOK não determina qual projeto deve ser executado nem qual decisão um gerente de projetos deve tomar. Ele organiza conhecimentos, processos e práticas que ajudam a estruturar o trabalho em diferentes contextos.

Arquitetura de soluções poderia beber da mesma fonte. Não para copiar seus processos, mas para adotar uma abordagem semelhante de sistematização: transformar conhecimento disperso em uma disciplina que ajude a estruturar decisões, tornar premissas explícitas, comunicar o raciocínio e preservar o julgamento de quem está projetando o sistema.

O desafio seria encontrar um nível de abstração suficientemente estável para sobreviver às mudanças tecnológicas e, ao mesmo tempo, suficientemente concreto para ajudar alguém a tomar uma decisão real. O objetivo não seria acompanhar cada nova tecnologia, mas oferecer uma estrutura que continue fazendo sentido quando as tecnologias mudarem.

Talvez essa seja uma das próximas fronteiras de maturidade da disciplina: transformar o conhecimento que hoje está espalhado entre frameworks, métodos, práticas e, principalmente, na experiência individual dos arquitetos em um corpo de conhecimento mais sistemático para a tomada de decisão arquitetural.

## O gargalo mudou

Talvez a questão não seja se os sistemas estão ficando mais fáceis ou mais difíceis. Eles estão ficando mais fáceis de construir e, justamente por isso, mais difíceis de projetar.

Cloud, serviços gerenciados, SaaS e IA reduziram drasticamente o custo de implementar e experimentar soluções. O gargalo migrou da implementação para o julgamento: decidir o que construir, quais alternativas descartar, quais trade-offs aceitar e quais consequências estamos dispostos a carregar.

Isso também muda o que esperamos de um arquiteto de soluções. Conhecer mais tecnologias continua sendo importante, mas não é suficiente. À medida que o espaço de soluções cresce, torna-se cada vez mais importante saber reduzi-lo de maneira consciente. Talvez o arquiteto mais valioso não seja aquele que conhece mais serviços, mas aquele que consegue eliminar alternativas sem eliminar as certas.

É por isso que a falta de um “PMBOK de Solution Architecture” me incomoda. Não porque precisemos de mais um framework para acompanhar a próxima tecnologia, mas porque talvez precisemos de uma disciplina mais consolidada para tomar decisões em um ambiente que muda continuamente.

Construir uma solução nunca foi o objetivo da arquitetura. O objetivo é tomar boas decisões sobre aquilo que vale a pena construir e preservar, tanto quanto possível, a capacidade de mudar de ideia quando as premissas mudarem.
