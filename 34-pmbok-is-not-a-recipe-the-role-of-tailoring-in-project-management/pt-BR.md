**Resumo:** Defendo que o PMBOK não deve ser tratado como uma receita de bolo, mas como um repertório de práticas que precisa ser adaptado ao contexto de cada projeto. Assim como na arquitetura de software, primeiro devemos entender requisitos, restrições, riscos e trade-offs para então definir a solução de gestão adequada. Tailoring não significa simplesmente fazer menos, mas dimensionar conscientemente a governança necessária, evitando tanto burocracia quanto controles insuficientes. Maturidade, portanto, está menos em seguir processos e mais em saber justificar as escolhas e evoluí-las conforme o problema muda.

------------------------------------------------------------------------

Recentemente, em uma conversa com uma amiga que trabalha como Product Manager, surgiu quase por acaso um comentário que me chamou atenção. Ela contou que a empresa onde trabalha não utiliza o PMBOK porque considera a abordagem engessada demais para a realidade da organização.

A percepção não me parece estranha. Em tecnologia, vejo algo parecido acontecer com frequência em discussões sobre arquitetura de soluções. Uma determinada arquitetura é apresentada como boa prática, passa a ser reproduzida em outros contextos e, quando não se encaixa, a conclusão é que a própria arquitetura era inadequada. Muitas vezes, o problema está em escolher a solução antes de compreender o problema que ela precisa resolver. Em system design, sabemos que não faz sentido começar pela arquitetura. Primeiro entendemos o problema, seus requisitos, restrições e trade-offs. Só então decidimos como o sistema será construído.

Quando ouvi aquele comentário sobre o PMBOK, fiz a mesma associação. Talvez parte da resistência ao framework venha de tratá-lo como uma arquitetura pronta de gestão, algo que deveria ser aplicado de maneira uniforme para que uma organização pudesse dizer que “faz gerenciamento de projetos”. Se esse for o ponto de partida, é fácil transformar conhecimento em procedimento, procedimento em obrigação e obrigação em burocracia.

O problema está justamente nessa interpretação. O PMBOK não precisa ser entendido como uma metodologia pronta, assim como um conjunto de padrões arquiteturais não constitui, sozinho, a arquitetura de uma aplicação. Ele oferece conhecimento, práticas e conceitos que podem ser utilizados para construir abordagens de gestão adequadas a diferentes situações. A questão deixa de ser quanto do PMBOK uma organização utiliza e passa a ser por que determinadas práticas foram escolhidas, que problema elas resolvem e qual nível de formalidade é necessário.

Talvez seja útil pensar nisso como uma espécie de management design. Não como uma disciplina formal ou um novo framework, mas como uma lente para olhar a gestão com a mesma lógica que usamos ao projetar sistemas: entender o problema antes de escolher os componentes, explicitar restrições, avaliar trade-offs e evitar tanto complexidade desnecessária quanto soluções insuficientes.

## O problema começa antes da metodologia

Quando falamos em gerenciamento de projetos, frequentemente colocamos no mesmo nível coisas que cumprem papéis diferentes: o corpo de conhecimento sobre gerenciamento, a abordagem escolhida para conduzir um projeto e a metodologia utilizada pela organização para operacionalizar essa abordagem. Confundir essas camadas facilita a ideia de que, para aplicar determinado conhecimento, é necessário reproduzir integralmente um processo. Mas uma organização pode utilizar práticas de gerenciamento sem adotar uma metodologia formal, assim como pode possuir uma metodologia corporativa e ainda adaptar sua aplicação a cada projeto.

Essa diferença fica evidente quando observamos a escala e a natureza do trabalho. Uma equipe pequena pode administrar riscos, prioridades, dependências e decisões por meio de mecanismos informais porque a proximidade entre as pessoas torna a coordenação barata. À medida que a organização cresce, aumentam as interfaces, os envolvidos, o custo dos desalinhamentos e as consequências de determinadas decisões. Surgem, então, necessidades de governança, comunicação e rastreabilidade que antes simplesmente não existiam. Não é que a organização tenha se tornado mais “aderente” a uma metodologia; o sistema que ela precisa coordenar se tornou mais complexo.

A mesma lógica se aplica à forma de execução. Um projeto com requisitos relativamente estáveis e alto custo de mudança pode justificar uma abordagem mais preditiva. Um produto em ambiente de alta incerteza pode se beneficiar de ciclos curtos de aprendizado e adaptação. Entre esses extremos existe uma variedade de combinações possíveis, inclusive dentro de uma mesma iniciativa, quando diferentes partes do trabalho possuem diferentes níveis de previsibilidade.

Por isso, a pergunta sobre qual metodologia utilizar não deveria ser o ponto de partida. Antes dela vem uma questão mais fundamental: o que precisamos gerenciar, quais são os riscos envolvidos, quais restrições existem e quanto de coordenação e governança esse contexto realmente exige? É a partir dessas respostas que uma abordagem de gestão pode ser desenhada.

## Management design

Em system design, não começamos dizendo que toda aplicação precisa de microsserviços ou mensageria. Começamos entendendo requisitos e restrições. Volume, disponibilidade, latência, segurança, custo, capacidade operacional e criticidade ajudam a determinar quais decisões arquiteturais são justificadas. Não existe uma arquitetura correta em abstrato. Existe uma arquitetura adequada a determinado conjunto de requisitos e restrições, considerando os trade-offs envolvidos.

A mesma lógica pode ser aplicada à gestão. Um projeto crítico pode exigir mecanismos de governança que seriam desproporcionais em uma iniciativa pequena. Um projeto com muitas dependências pode precisar de mecanismos de coordenação que não fazem sentido para uma equipe trabalhando de forma independente. Uma iniciativa altamente incerta pode obter pouco valor de um planejamento excessivamente detalhado quando ainda não existem informações suficientes para sustentá-lo. O que muda de um contexto para outro não é a importância da gestão, mas os problemas que ela precisa resolver e a complexidade necessária para resolvê-los.

As práticas de gestão podem, portanto, ser tratadas como componentes de uma solução. O PMBOK oferece parte desse repertório, mas não determina sozinho como esses componentes devem ser combinados. A composição final depende do contexto, das necessidades e das restrições do projeto. É nesse sentido que proponho pensar em management design: a construção deliberada de uma abordagem de gestão a partir do problema que precisa ser administrado.

A ideia é semelhante à montagem de um sistema. Ter mais componentes disponíveis não torna automaticamente a solução melhor. Cada componente acrescenta capacidades, mas também pode introduzir custo, complexidade, dependências ou novas necessidades operacionais. O trabalho de design está justamente em decidir o que precisa fazer parte da solução, o que pode ser simplificado e quais trade-offs são aceitáveis.

Tailoring, nesse sentido, deixa de ser apenas o ato de “adaptar o PMBOK”. Ele passa a ser uma consequência natural do próprio processo de design: entender o contexto, selecionar os componentes adequados e compor uma abordagem proporcional ao problema que precisa ser resolvido.

## Tailoring não é fazer menos

É fácil interpretar tailoring como uma licença para reduzir processos. Se uma organização tem muitos documentos, elimina alguns; se possui muitas reuniões, cancela algumas; se determinada etapa parece burocrática, deixa de executá-la. O resultado pode até ser uma abordagem melhor, mas reduzir processos por si só não caracteriza tailoring. A diferença está no critério utilizado para tomar essa decisão.

Em arquitetura, uma solução não é melhor simplesmente porque possui menos componentes. Uma aplicação com poucos componentes pode ser elegante ou insuficiente; uma arquitetura mais complexa pode ser necessária ou pode representar overengineering. O número de componentes importa menos do que a relação entre eles e os requisitos que precisam atender. A mesma lógica vale para gestão: a quantidade de práticas utilizadas não determina a qualidade da abordagem.

Aplicar menos práticas pode, sim, ser mais maduro do que aplicar todas indiscriminadamente, desde que a escolha seja deliberada. Se determinado controle foi eliminado, é preciso compreender qual problema ele resolvia, qual risco está associado à sua ausência e por que aquele nível de controle não é necessário naquele contexto. Da mesma forma, adicionar uma prática deveria exigir uma justificativa equivalente: qual necessidade ela atende e qual complexidade introduz?

Tailoring não é escolher o caminho mais simples. É dimensionar a gestão de acordo com o problema, aceitando conscientemente os trade-offs envolvidos.

## O risco do overengineering de gestão

Em tecnologia, overengineering é um problema conhecido. Uma solução pode estar tecnicamente correta e ainda assim ser inadequada porque introduz complexidade que os requisitos não justificam. Mais componentes podem significar mais capacidade, mas também mais dependências, mais esforço operacional e mais pontos de falha. A complexidade precisa existir por uma razão.

Na gestão, o equivalente acontece quando uma iniciativa recebe documentos, aprovações, reuniões e indicadores porque esses mecanismos fazem parte da metodologia corporativa, e não porque o projeto efetivamente precisa deles. Cada elemento pode parecer razoável isoladamente. O problema aparece quando observamos a abordagem como um sistema e percebemos que sua complexidade introduz mais fricção do que controle, consumindo capacidade que poderia estar sendo utilizada na execução do próprio projeto.

Isso não significa que documentação, governança ou controles sejam ruins. Significa que precisam ter uma função clara. Uma reunião deve existir porque alguma coordenação precisa acontecer. Um registro deve existir porque determinada informação precisa ser preservada, compartilhada ou utilizada em uma decisão. Uma aprovação deve existir porque determinada decisão exige aquela autoridade. Um indicador deve existir porque existe uma pergunta relevante que precisa ser respondida.

Quando essa relação se perde, o mecanismo deixa de ser uma ferramenta de gestão e passa a ser apenas um ritual. É possível ter uma organização extremamente disciplinada na execução de processos e, ainda assim, pouco madura em gerenciamento de projetos. Cumprir um processo demonstra aderência ao processo; não demonstra, por si só, que o processo foi bem escolhido.

## O risco de uma gestão subdimensionada também existe

A crítica à burocracia pode levar ao extremo oposto. Se complexidade demais é ruim, pode parecer que a melhor gestão é aquela que possui o mínimo possível de processos. Essa conclusão é tão equivocada quanto associar maturidade à quantidade de controles. Em arquitetura, uma solução minimalista pode ser exatamente o que o problema exige ou simplesmente estar subdimensionada. A diferença está nos requisitos e nas consequências das escolhas.

Na gestão, o equivalente é eliminar controles porque são inconvenientes, lentos ou incompatíveis com a cultura da equipe, sem avaliar o risco que permanece depois dessa decisão. Uma empresa pode dizer que não precisa documentar decisões porque “somos Agile”, evitar determinado mecanismo de governança porque “somos pequenos” ou não acompanhar riscos formalmente porque “o time conversa todos os dias”. Em determinados contextos, essas escolhas são perfeitamente razoáveis. Em outros, apenas transferem o custo para um problema futuro que ninguém decidiu explicitamente aceitar.

Esse ponto é importante porque a ausência de um controle também é uma decisão de gestão. Se um mecanismo foi deliberadamente retirado, deveria ser possível explicar qual necessidade ele atendia, por que ela não é relevante naquele contexto e qual risco está sendo assumido ao não mantê-lo. Tailoring não significa remover aquilo que parece burocrático; significa decidir conscientemente o nível de controle necessário.

O objetivo, portanto, não é minimizar processos. É dimensionar a gestão de acordo com a complexidade, os riscos e as restrições do contexto.

## Uma startup não é uma corporação em escala reduzida

É nesse ponto que startups em estágio inicial se tornam um caso particularmente interessante. Uma organização pequena, com poucas pessoas, alta incerteza e um produto ainda em evolução, opera sob condições muito diferentes de uma empresa estabelecida. A comunicação é direta, as decisões podem ser tomadas com pouca intermediação e muitas informações permanecem disponíveis no contexto das próprias pessoas. Reproduzir nesse ambiente uma estrutura corporativa completa de gerenciamento pode significar introduzir uma complexidade que a organização ainda não precisa.

Isso não significa ausência de gestão. A startup continua precisando definir objetivos, avaliar riscos, administrar dependências, tomar decisões e acompanhar resultados. O que muda é a forma como essas atividades precisam ser estruturadas. Quando poucas pessoas precisam alinhar uma decisão, uma conversa pode ser suficiente. Conforme aumentam as pessoas envolvidas, as interfaces entre equipes e o custo de uma decisão mal coordenada, mecanismos que antes pareciam desnecessários podem passar a ter valor.

A prática de gestão pode, portanto, permanecer enquanto sua forma evolui. Uma startup não precisa importar a estrutura de governança de uma grande corporação para ser profissional, assim como não precisa transformar cada decisão em um processo formal para demonstrar maturidade. Mas também não deveria confundir informalidade com ausência de gestão. O que hoje pode ser resolvido por proximidade e contexto compartilhado pode amanhã exigir mecanismos explícitos de coordenação, não porque a organização finalmente “adotou uma metodologia”, mas porque o problema que ela precisa administrar mudou.

Esse é um dos exemplos mais claros de management design. A abordagem adequada não é uma versão reduzida de uma metodologia corporativa, mas uma solução construída a partir das características da própria organização. À medida que ela cresce, essa solução pode evoluir junto com o sistema que precisa coordenar.

## A gestão também é uma arquitetura evolutiva

O que funciona para uma organização pequena pode deixar de funcionar conforme ela cresce, da mesma maneira que uma arquitetura adequada para uma aplicação em determinado estágio pode precisar ser revista quando seus requisitos mudam. Isso não significa que a solução anterior estava errada. Significa que ela foi desenhada para condições que já não são as mesmas.

Crescimento altera a natureza do problema. Mais pessoas aumentam as interfaces e o custo de comunicação. Mais equipes criam dependências que antes não existiam. Mais clientes aumentam as consequências de determinadas falhas. Mais recursos envolvidos elevam o custo de decisões equivocadas. Novas obrigações regulatórias introduzem restrições adicionais. Em algum momento, mecanismos que antes seriam burocráticos passam a ser necessários para manter a coordenação e o controle.

Em arquitetura de software, esse processo é conhecido: uma solução evolui porque o sistema ao seu redor evoluiu. A arquitetura de gestão segue a mesma lógica. Uma organização não deveria preservar uma determinada estrutura de governança apenas porque ela funcionou no passado, assim como não deveria introduzir novos mecanismos apenas porque atingiu determinado tamanho. O gatilho para a mudança deveria estar nas novas necessidades, restrições e riscos que surgiram.

Maturidade, nesse contexto, não é chegar a um estado em que todos os projetos utilizam a mesma quantidade de processo. É desenvolver a capacidade de reconhecer quando a arquitetura de gestão deixou de ser adequada e evoluí-la antes que a complexidade do sistema torne essa mudança necessária de forma traumática.

## Agile muda a forma, mas não elimina o problema

Essa perspectiva também muda a maneira de olhar para Agile. A oposição entre PMBOK e Agile costuma partir da ideia de que um representa processos estruturados enquanto o outro representa adaptação. Essa dicotomia perde de vista o ponto principal: ambos podem oferecer mecanismos para lidar com problemas de gestão, mas partem de condições diferentes sobre previsibilidade, incerteza e mudança.

Uma abordagem adaptativa faz sentido quando existe incerteza relevante sobre o que deve ser construído ou sobre qual solução produzirá valor. Trabalhar de forma iterativa permite aprender e ajustar o caminho conforme novas informações surgem. Mas iteratividade não elimina riscos, dependências, stakeholders, restrições orçamentárias, requisitos de segurança ou necessidades de governança. Ela apenas muda a forma como esses elementos são tratados.

Um time pode trabalhar com ciclos curtos, priorização contínua e feedback frequente e, ao mesmo tempo, precisar lidar com compliance, fornecedores, orçamento ou dependências entre equipes. Da mesma forma, uma iniciativa pode utilizar planejamento preditivo em determinadas dimensões e mecanismos adaptativos em outras. A escolha não precisa ser ideológica. Precisa responder às características do trabalho.

É por isso que abordagens híbridas não deveriam ser vistas como uma contradição, mas como uma consequência possível do próprio tailoring. Diferentes partes de uma iniciativa podem apresentar diferentes níveis de previsibilidade, risco e necessidade de controle. A pergunta relevante não é qual metodologia venceu o debate, mas quais mecanismos de gestão são necessários para lidar adequadamente com o contexto.

Agile não elimina a necessidade de gestão. Assim como uma abordagem preditiva não implica, por si só, burocracia. O que muda é a arquitetura utilizada para organizar e conduzir o trabalho.

## A automação muda os trade-offs da gestão

A discussão sobre management design ganha outra dimensão quando consideramos IA e automação. Escolher quais práticas aplicar envolve também considerar o custo de operacionalizá-las. Atualizar registros, consolidar informações, produzir relatórios, acompanhar indicadores e identificar mudanças exige esforço, e esse esforço influencia a decisão sobre o nível de gestão adequado. Uma prática pode ser relevante e, ainda assim, ser desproporcional ao contexto quando seu custo de execução é alto.

Automação altera esse trade-off. Uma atividade que antes exigia horas de trabalho manual pode passar a exigir apenas uma revisão humana. Informações dispersas podem ser consolidadas automaticamente, relatórios podem ser produzidos a partir de dados já disponíveis e sistemas podem auxiliar na identificação de padrões, inconsistências e possíveis riscos. Isso não significa simplesmente adicionar mais processos porque agora eles são baratos. Significa que práticas antes consideradas excessivamente custosas podem passar a fazer sentido quando o custo de operacionalização cai.

O valor de uma prática não muda necessariamente porque ela ficou mais barata de executar. O que muda é a relação entre seu benefício, seu custo e a complexidade que ela introduz. Uma solução que antes seria desproporcional pode se tornar adequada ao contexto, alterando as escolhas possíveis dentro do management design.

Existe, porém, uma fronteira importante. Automatizar a coleta e a análise de informações não significa automatizar o julgamento. Uma ferramenta pode identificar um possível risco ou desvio, mas avaliar sua relevância, decidir se ele deve ser aceito e determinar uma resposta continua exigindo contexto e responsabilidade. A IA pode reduzir o custo da gestão, mas não elimina a necessidade de projetá-la.

## Projetar a gestão, não seguir a receita

O problema começa na própria pergunta “qual metodologia devemos usar?”. Em arquitetura de soluções, primeiro entendemos o sistema, seus requisitos, restrições, riscos e trade-offs; só então definimos a arquitetura. Management design segue a mesma lógica: compreender o contexto, dimensionar a governança necessária e selecionar as práticas que respondem aos problemas reais do projeto. Quando os requisitos mudam, a abordagem também pode precisar evoluir.

É nesse processo que o PMBOK encontra seu lugar. Não como uma receita a ser aplicada integralmente, mas como repertório para orientar decisões. Maturidade não está na quantidade de práticas adotadas, mas na capacidade de justificar as escolhas: quais riscos estão sendo tratados, quais mecanismos são necessários, qual complexidade é aceitável e quais controles deliberadamente não fazem parte da solução. Aplicar menos práticas pode ser mais maduro do que aplicar todas, desde que essa escolha seja consciente e proporcional ao contexto.

Em arquitetura, não consideramos maduro o arquiteto que utiliza todos os componentes disponíveis, mas aquele que sabe compor uma solução adequada aos requisitos e restrições, assumindo conscientemente os trade-offs. Gestão de projetos não deveria ser diferente. O PMBOK fornece parte do repertório; o trabalho está em saber transformá-lo em uma abordagem adequada ao problema que se pretende resolver.
