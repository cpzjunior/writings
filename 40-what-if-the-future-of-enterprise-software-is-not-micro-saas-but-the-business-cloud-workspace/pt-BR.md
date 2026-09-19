# E se o futuro do software empresarial não for o Micro-SaaS, mas o Business Cloud Workspace?

_Da especialização das aplicações a uma plataforma que absorva software, agentes, conhecimento e relações de negócio_

**Resumo:** Defendo que o futuro do software empresarial pode não estar em criar uma aplicação para cada necessidade, mas em construir uma plataforma capaz de reunir diferentes capacidades em um único ambiente. Chamo essa ideia de Business Cloud Workspace: um espaço que combina software especializado, agentes, dados, conhecimento e integrações sob uma experiência orientada ao trabalho, não aos produtos. A IA torna isso mais viável ao traduzir a forma como a empresa pensa em estruturas, workflows e automações, enquanto um ecossistema de plugins permite incorporar novas capacidades sem criar novas ilhas. O diferencial está em gerar lock-in pelo valor entregue: quanto mais a empresa constrói e opera dentro desse ambiente, mais ele se torna parte da sua forma de trabalhar, tornando a permanência uma consequência do valor, e não da dependência.

------------------------------------------------------------------------

Acompanho há algum tempo a comunidade de Micro-SaaS e gosto muito da perspectiva por trás dela: encontrar um problema específico, construir um software simples que o resolva muito bem e, a partir disso, criar um negócio. Existe algo particularmente atraente na ideia de que uma equipe pequena pode identificar uma dor real e transformá-la em um produto independente.

Mas tenho cada vez mais a sensação de que a inteligência artificial está ameaçando justamente essa abordagem. Não porque os problemas específicos estejam desaparecendo ou porque o Micro-SaaS tenha deixado de fazer sentido. Pelo contrário. A IA está tornando cada vez mais fácil transformar uma necessidade específica em software. E, quando construir uma determinada capacidade deixa de ser uma barreira relevante, a funcionalidade isolada se torna menos defensável.

Isso me leva naturalmente a uma pergunta: se software especializado está se tornando cada vez mais abundante, onde estará o valor?

Durante muito tempo, a evolução do software empresarial pareceu caminhar em direção à especialização. O ERP cuidava da operação, o CRM dos clientes, o software de RH das pessoas, outra aplicação dos projetos, outra dos contratos, outra das despesas. O SaaS tornou economicamente viável transformar praticamente qualquer necessidade em um produto independente. O Micro-SaaS levou essa lógica ao extremo: se existe uma dor específica, pode existir um software específico para resolvê-la.

Essa lógica fez sentido. Construir software era caro, e encontrar uma necessidade suficientemente específica para atender melhor do que os grandes fornecedores podia ser uma excelente oportunidade. Uma pequena equipe conseguia transformar uma única funcionalidade em um produto e, a partir dela, construir uma empresa.

Mas essa equação está mudando. A quantidade de software disponível cresceu enormemente, enquanto a inteligência artificial está reduzindo o custo de construir novas aplicações e funcionalidades. Se uma capacidade pode ser implementada, reproduzida e personalizada cada vez mais rapidamente, teremos provavelmente mais software especializado do que nunca. Isso não significa que o Micro-SaaS vai desaparecer. Talvez aconteça justamente o contrário. A questão é onde esse software vai viver.

Em um texto anterior, “[Por que sistemas modernos estão ficando mais fáceis de construir e mais difíceis de projetar?](https://cpzjunior.substack.com/p/por-que-sistemas-modernos-estao-ficando)“, argumentei que a cloud e a IA estão tornando a implementação de soluções cada vez mais acessível, mas que isso não significa necessariamente menos complexidade. A complexidade não desaparece; ela muda de lugar. Em vez de precisarmos construir cada componente, precisamos decidir como combiná-los e conviver com as consequências dessas escolhas.

O software empresarial parece estar passando pelo mesmo processo. O SaaS tornou muito mais fácil adquirir uma capacidade específica. A IA está tornando mais fácil construir novas capacidades. Mas, ao mesmo tempo, uma empresa precisa administrar uma quantidade crescente de aplicações, integrações, contratos, credenciais, dados e dependências distribuídas entre diferentes fornecedores.

Talvez a próxima evolução não seja adicionar ainda mais aplicações a esse ecossistema, mas criar uma camada capaz de absorver essa abundância sem transferir toda a sua complexidade para quem precisa utilizá-la.

É dessa ideia que surge o que chamo, provisoriamente, de Business Cloud Workspace, ou BCW.

## O custo da fragmentação

O SaaS resolveu uma parte importante do problema de software empresarial: tornou muito mais simples adquirir uma capacidade. Em vez de comprar infraestrutura, contratar uma equipe ou desenvolver uma solução internamente, uma empresa pode simplesmente assinar um serviço.

O problema é que essa simplicidade de aquisição não necessariamente se traduz em simplicidade de operação. Uma pequena empresa pode começar com algumas escolhas perfeitamente razoáveis: um CRM para vendas, uma solução financeira, uma ferramenta de comunicação, outra para documentos, outra para projetos e algumas aplicações específicas para necessidades particulares. Individualmente, cada decisão parece simples. A complexidade aparece quando essas ferramentas precisam funcionar juntas.

Cada sistema possui seu próprio modelo de dados, autenticação, permissões, interface, política de cobrança e mecanismos de integração. As pessoas precisam saber onde determinada informação está, qual sistema utilizar para cada tarefa e como fazer um processo atravessar diferentes aplicações.

Existe também um custo financeiro que tende a ser subestimado. Cada aplicação pode parecer barata isoladamente, mas a soma de dezenas de assinaturas representa uma despesa recorrente relevante. Além da mensalidade, existem custos associados a implantação, integração, treinamento, administração e manutenção. A facilidade de adquirir software pode, paradoxalmente, tornar mais fácil acumular software do que avaliar o custo total de mantê-lo.

A fragmentação também aumenta a dependência de fornecedores. Cada novo serviço introduz uma relação que precisa ser administrada, com suas próprias políticas de preço, segurança, disponibilidade, evolução do produto e condições contratuais. A empresa passa a depender não apenas de seus próprios sistemas, mas da continuidade e das decisões de uma coleção de fornecedores externos.

Isso cria também um problema de supply chain. Uma vulnerabilidade, indisponibilidade ou mudança relevante em um fornecedor pode afetar processos que a empresa não controla diretamente. Quanto maior a quantidade de serviços externos que participam da operação, maior a superfície de dependências que precisa ser acompanhada.

Mas existe ainda um custo menos visível: o custo cognitivo. Ao passar de uma aplicação para outra, a pessoa não está apenas mudando de janela. Ela precisa reorganizar mentalmente as informações relacionadas à tarefa, recuperar o que estava fazendo e adaptar sua forma de pensar à maneira como aquela aplicação apresenta o problema. O Alt+Tab resolve a mudança de janela, mas não resolve esse esforço cognitivo.

Quando uma tarefa atravessa várias aplicações, esse esforço se acumula. Parte da atenção deixa de estar concentrada no problema de negócio e passa a ser utilizada para reconstruir, a cada aplicação, o contexto mental necessário para continuar trabalhando.

O problema, portanto, não está necessariamente em ter muitos softwares. Algumas soluções especializadas são perfeitamente justificáveis. Um software pode resolver tão bem uma necessidade específica que vale a pena incorporá-lo à operação. A questão surge quando cada nova capacidade adiciona uma nova fronteira que precisa ser administrada em termos financeiros, técnicos e cognitivos.

A inteligência artificial pode tornar esse cenário ainda mais extremo. À medida que fica mais barato produzir software, torna-se economicamente viável criar ferramentas para necessidades cada vez menores e mais específicas. O resultado pode ser uma abundância ainda maior de aplicações especializadas: mais capacidades disponíveis, mas também mais decisões sobre onde encontrá-las, como conectá-las e quem será responsável por mantê-las.

A especialização reduz o custo de construir cada componente, mas pode transferir parte do custo para quem precisa operar o conjunto. Quanto mais barato fica criar software para resolver problemas específicos, maior pode se tornar o esforço necessário para administrar todos esses softwares como parte de uma operação coerente.

É nesse ponto que surge uma oportunidade. Talvez não precisemos de menos software especializado. Precisamos de uma camada capaz de absorvê-lo. Em vez de cada nova necessidade resultar necessariamente em mais uma aplicação independente, ela poderia ser incorporada ao ambiente existente como um módulo, plugin, agente ou integração.

O valor, nesse cenário, não estaria apenas na capacidade individual oferecida por cada software, mas na infraestrutura que permite combiná-los de forma coerente: contexto, dados, identidade, permissões, integração, governança e experiência.

A questão deixa de ser como criar menos aplicações e passa a ser como fazer com que uma empresa consiga utilizar mais software sem precisar administrar proporcionalmente mais custo, dependências e complexidade cognitiva.

É justamente nesse ponto que o BCW começa a fazer sentido.

## Uma cloud para o negócio

A ideia do BCW começa por uma inversão simples: em vez de organizar o software em torno das aplicações que uma empresa precisa contratar, organizá-lo em torno das capacidades que ela precisa utilizar. A plataforma funcionaria como uma cloud, oferecendo essas capacidades sob demanda e permitindo que cada empresa componha progressivamente seu próprio ambiente operacional.

Na AWS, eu não preciso decidir antecipadamente qual será toda a minha arquitetura. Posso começar com armazenamento, adicionar um banco de dados, criar uma máquina virtual e, conforme a necessidade aparece, incorporar novos serviços. Posso construir um MVP extremamente simples ou uma arquitetura enterprise sofisticada utilizando a mesma infraestrutura.

O que muda não é a plataforma, mas a combinação de recursos que utilizo e o nível de complexidade que escolho expor. O BCW aplicaria essa lógica ao negócio. Uma empresa poderia começar com poucas capacidades básicas e, conforme cresce, incorporar recursos para vendas, finanças, pessoas, projetos, pagamentos, reconciliação, automação ou qualquer outra necessidade que surja. Essas capacidades não precisariam aparecer para o usuário como sistemas independentes. Poderiam compartilhar dados, identidade, permissões, workflows e contexto dentro do mesmo ambiente.

Isso permite que uma tarefa seja tratada como uma tarefa, e não como uma sequência de aplicações. Se para resolver um problema forem necessários dados de clientes, um contrato, uma aprovação financeira e um documento, o usuário não deveria precisar saber em quais sistemas essas informações estão armazenadas. O BCW deveria reunir o contexto necessário e apresentar a experiência como uma única operação.

A plataforma também não precisaria construir tudo internamente. Assim como uma cloud oferece serviços fundamentais sobre os quais outras soluções podem ser construídas, o BCW poderia fornecer primitives empresariais para que módulos de terceiros, agentes e aplicações especializadas fossem incorporados ao ambiente. Identidade, dados, permissões, billing, workflows e governança poderiam ser responsabilidades da plataforma, enquanto desenvolvedores e parceiros se concentrariam nas capacidades específicas que desejam oferecer.

Essa é uma diferença importante em relação à lógica tradicional das suítes empresariais. O objetivo não seria oferecer um conjunto fechado de produtos capaz de cobrir todas as áreas da empresa, mas fornecer uma infraestrutura sobre a qual a própria empresa possa montar seu ambiente de trabalho.

O software deixaria de ser organizado a partir das fronteiras dos produtos e passaria a ser organizado a partir do que a empresa precisa realizar. O resultado seria uma espécie de cloud do negócio: uma plataforma que permite começar com pouco, incorporar novas capacidades conforme elas se tornam necessárias e crescer sem precisar reconstruir a operação a cada nova etapa.

## Do MVP à operação

Uma das características mais interessantes de uma cloud é permitir que a mesma infraestrutura sustente projetos com níveis de sofisticação completamente diferentes. Um desenvolvedor pode começar com uma aplicação simples e, se ela funcionar, utilizar a mesma base para construir uma operação muito mais complexa.

O BCW poderia aplicar esse princípio à criação de negócios. Hoje, transformar uma ideia em uma empresa exige construir uma quantidade significativa de infraestrutura que não necessariamente faz parte da hipótese que está sendo testada. É preciso lidar com autenticação, usuários, permissões, documentos, pagamentos, comunicação, processos internos e uma série de outras capacidades antes mesmo de saber se existe um negócio.

Em “[Antes de tirar uma ideia do papel, é preciso colocá-la nele](https://cpzjunior.substack.com/p/antes-de-tirar-uma-ideia-do-papel)“, discuti como um MVP envolve muito mais do que implementar algumas funcionalidades. Antes de uma ideia chegar ao mercado, é preciso tomar decisões de produto, experiência, arquitetura, dados, segurança, operação e execução. Muitas delas são simplesmente o preço de construir a infraestrutura necessária para que o experimento exista.

O BCW poderia abstrair parte desse trabalho. Quem está experimentando uma ideia poderia utilizar as capacidades já disponíveis na plataforma e concentrar sua energia naquilo que realmente precisa descobrir. Autenticação, usuários, permissões, documentos, pagamentos, comunicação e workflows não precisariam ser construídos do zero apenas para colocar a primeira versão do negócio em funcionamento.

Isso muda o significado de MVP. O objetivo deixa de ser construir uma pequena versão de toda a infraestrutura necessária para operar uma empresa e passa a ser construir apenas aquilo que é necessário para testar a hipótese.

Se a hipótese for validada, a mesma solução poderia continuar evoluindo dentro do ambiente. O que começou como uma operação simples poderia incorporar processos mais sofisticados, novos usuários, agentes, integrações e módulos sem exigir uma reconstrução completa da infraestrutura.

Isso cria uma propriedade particularmente interessante: a distância entre experimentar um negócio e operá-lo pode diminuir. Hoje, validar uma ideia e estruturar uma empresa são frequentemente tratados como problemas diferentes. Primeiro construímos o MVP; depois precisamos escolher e implantar os sistemas que vão sustentar a operação real.

Em um BCW, esses dois momentos poderiam fazer parte da mesma trajetória. A plataforma poderia ser simples o suficiente para não atrapalhar o experimento e profunda o suficiente para sustentar aquilo que vier depois.

## A experiência como produto

Isso leva ao que considero o principal diferencial do BCW: a experiência. Existe uma diferença entre tomar um café no bar da esquina e tomar um café no Starbucks. Nos dois casos, a necessidade fundamental pode ser exatamente a mesma: tomar café. O que muda é tudo aquilo que existe ao redor dela. O ambiente, a consistência, a forma de pedir, o pagamento, a personalização, a previsibilidade. O produto não é apenas o café. É a forma como os elementos necessários foram organizados para que o cliente não precise pensar neles.

Software empresarial pode seguir a mesma lógica. Um all-in-one tradicional tenta reunir diferentes produtos sob o mesmo fornecedor. Um produto como o Zoho pode oferecer CRM, financeiro, projetos, RH e outras aplicações em uma mesma suíte. Isso reduz a quantidade de fornecedores que uma empresa precisa administrar, mas não necessariamente elimina as fronteiras entre os produtos. O usuário continua precisando entender qual aplicação utilizar, onde determinada capacidade está disponível e como uma tarefa atravessa diferentes módulos.

O BCW parte de uma premissa diferente: a unidade da experiência não deveria ser o produto, mas o trabalho que a empresa precisa realizar. O usuário não deveria entrar no ambiente pensando em qual sistema precisa abrir. Deveria simplesmente pensar no que precisa fazer. Se precisa contratar um fornecedor, a plataforma apresenta o processo. Se precisa consultar um contrato, encontra o documento e o contexto relacionado. Se precisa descobrir uma política interna, consulta a knowledge base. Se precisa executar uma atividade repetitiva, pode delegá-la a um agente. Uma tarefa que exige informações financeiras, dados de clientes e uma aprovação deveria aparecer como uma única operação, mesmo que diferentes capacidades estejam envolvidas por trás dela.

Essa distinção é fundamental. O all-in-one organiza a experiência a partir dos produtos que oferece. O BCW deveria organizá-la a partir do trabalho que precisa ser realizado. Por isso, CRM, financeiro, RH, documentos, agentes, workflows e módulos de terceiros não precisariam ser apresentados como destinos diferentes dentro da plataforma. Seriam capacidades que podem ser combinadas conforme a tarefa exigir. A integração, nesse modelo, deixa de ser uma atividade que o usuário precisa compreender. Ela passa a ser uma propriedade do ambiente.

Isso também muda o que significa competir por funcionalidades. O objetivo não é oferecer uma aplicação para cada necessidade, mas permitir que uma empresa resolva seus problemas sem precisar conhecer a arquitetura necessária para isso.

O exemplo do Starbucks ajuda a entender essa diferença. O valor não está apenas naquilo que é oferecido, mas na forma como os elementos necessários foram organizados em uma experiência consistente e previsível.

No BCW, o produto também não seria a soma das aplicações. Seria a experiência que emerge quando elas deixam de ser o centro da interação.

## IA como camada de interpretação

A inteligência artificial pode ser fundamental para reduzir uma das maiores barreiras à adoção de software empresarial: a necessidade de traduzir o funcionamento de uma empresa para a linguagem do sistema.

Uma empresa conhece seu próprio negócio, mas isso não significa que conheça a estrutura necessária para representá-lo dentro de um software. Tradicionalmente, essa tradução exige configuração, consultoria, treinamento e, muitas vezes, desenvolvimento. O usuário precisa aprender como o sistema organiza entidades, relacionamentos, workflows e permissões antes de conseguir utilizá-lo plenamente.

A IA pode funcionar como uma camada de interpretação entre a forma como a empresa descreve seu negócio e a forma como a plataforma precisa representá-lo. Uma empresa poderia importar suas planilhas e permitir que a plataforma identificasse clientes, fornecedores, produtos, funcionários e relações entre essas entidades. Poderia importar documentos, políticas e procedimentos. Poderia conectar sistemas existentes e deixar que a plataforma ajudasse a mapear suas estruturas.

Da mesma forma, o usuário poderia explicar o que precisa em linguagem natural e deixar que a plataforma determinasse quais dados, capacidades e workflows são necessários para executar aquilo.

O objetivo não seria simplesmente importar dados ou permitir comandos em linguagem natural. Seria reduzir a distância entre a forma como a empresa pensa sobre seu negócio e a estrutura necessária para representá-lo no software.

Isso é especialmente importante para empresas pequenas. Quanto menor a organização, menos provável que exista alguém dedicado a administrar sistemas empresariais ou traduzir processos de negócio para modelos de software. A plataforma precisa assumir uma parte maior desse trabalho justamente onde a capacidade técnica é menor.

Essa interpretação também poderia acontecer continuamente. À medida que o negócio muda, o BCW poderia transformar novas necessidades descritas pelo usuário em estruturas, workflows, automações e configurações, sem exigir que a empresa conheça antecipadamente a melhor forma de modelá-las.

Uma boa plataforma empresarial não deveria exigir que o usuário aprenda a pensar como o sistema. Deveria ser capaz de entender como a empresa pensa e traduzir isso para o sistema.

Nesse sentido, a IA não é apenas uma funcionalidade do BCW. Ela é parte da própria abstração que permite esconder a complexidade da plataforma sem eliminar a capacidade que existe por trás dela.

## Knowledge bases e agentes de IA

Uma vez que dados, documentos e processos estejam no mesmo ambiente, o conhecimento organizacional pode deixar de ser apenas documentação e passar a fazer parte da própria operação.

A empresa poderia manter uma wiki dentro do BCW, mas uma wiki conectada ao restante da plataforma. Políticas, procedimentos, manuais, decisões e aprendizados poderiam estar relacionados aos processos que executam essas regras.

Esse conhecimento poderia ser estruturado como uma espécie de wiki as code: versionado, organizado e governado pela própria empresa, enquanto a IA o utilizaria como contexto para responder perguntas, executar processos e orientar agentes.

Uma política poderia se tornar uma regra de execução. Um procedimento poderia se transformar em um workflow. Uma orientação recorrente poderia dar origem a um agente. Nesse contexto, agentes não seriam simplesmente assistentes conversacionais. Seriam componentes operacionais da empresa, capazes de acessar os recursos da plataforma, consultar a knowledge base, executar workflows e operar dentro das permissões definidas para eles.

A empresa poderia customizar não apenas o que um agente conhece, mas também como ele trabalha. Um processo poderia ter seu próprio agente, com objetivos, permissões, ferramentas e critérios de decisão definidos pela organização.

Até mesmo a estratégia utilizada para resolver um problema poderia fazer parte dessa configuração. Um agente poderia ser orientado a trabalhar segundo PDCA, enquanto outro utilizaria OODA ou uma metodologia específica definida internamente. A metodologia deixaria de ser apenas uma orientação documentada e passaria a fazer parte da lógica de execução do agente.

O mesmo princípio se aplicaria aos workflows. Em vez de simplesmente escolher entre processos pré-definidos, a empresa poderia adaptar etapas, regras de aprovação, condições e responsabilidades de acordo com sua forma de operar.

O resultado seria uma camada diferente de personalização. A empresa não estaria apenas armazenando seu conhecimento dentro do BCW. Estaria transformando esse conhecimento em comportamento operacional.

E tudo isso poderia acontecer dentro da própria plataforma. Não seria necessário desenvolver um agente do zero, criar um MCP server, construir integrações específicas ou manter uma arquitetura paralela apenas para conectar a IA aos sistemas da empresa. As primitives necessárias já estariam disponíveis no ambiente.

O BCW deixaria, então, de ser apenas o lugar onde a empresa armazena informações e executa processos. Passaria a ser também o lugar onde ela define como esses processos devem funcionar e como agentes podem executá-los.

## Micro-SaaS como plugins

É aqui que o Micro-SaaS pode encontrar um novo papel. Em vez de desaparecer, ele pode deixar de ser necessariamente uma ilha.

Uma plataforma desse tipo poderia possuir um Marketplace no qual desenvolvedores criassem módulos para necessidades que o fornecedor principal jamais conseguiria antecipar. Um produto extremamente específico para determinado setor, uma integração com um sistema legado, um workflow especializado ou uma nova capacidade de IA poderia ser instalado diretamente no BCW.

A melhor analogia talvez esteja nos mods de Skyrim. A Bethesda não precisou imaginar todas as funcionalidades, histórias, mapas e experiências que os jogadores poderiam querer. Ela criou um jogo suficientemente extensível para que uma comunidade inteira pudesse construir sobre ele.

Um BCW poderia funcionar de maneira semelhante. O fornecedor construiria a infraestrutura comum, enquanto uma comunidade de desenvolvedores poderia criar capacidades que a empresa central jamais teria capacidade ou incentivo para antecipar. A diferença é que, nesse caso, os mods não adicionariam apenas conteúdo. Poderiam adicionar capacidades reais ao negócio.

O desenvolvedor não precisaria reconstruir toda a infraestrutura empresarial necessária para entregar sua funcionalidade. Identidade, permissões, dados, billing, workflows e outras primitives poderiam ser fornecidos pela plataforma. Ele se concentraria na capacidade específica que deseja oferecer.

Isso muda a natureza do Micro-SaaS. Em vez de cada produto precisar conquistar clientes individualmente, implantar sua própria infraestrutura e criar mais uma ilha de dados, ele poderia ser distribuído como uma extensão do ambiente que o cliente já utiliza. O desenvolvedor ganha acesso a uma base existente. O cliente ganha uma nova capacidade sem precisar adotar outro sistema.

Essa dinâmica também reduz o custo de experimentação. Um desenvolvedor pode criar um módulo para um nicho muito específico sem precisar construir toda a infraestrutura empresarial ao redor dele. Se houver demanda, o módulo cresce dentro do ecossistema. Se não houver, o custo do fracasso é menor.

Mas essa abertura traz uma consequência inevitável: quanto mais coisas puderem ser construídas sobre o BCW, maior será a necessidade de governança. Permitir que terceiros criem módulos, agentes e workflows significa lidar com identidade, permissões, isolamento, segurança, auditoria, versionamento, observabilidade, billing e políticas. A plataforma precisaria oferecer aos componentes que rodam sobre ela uma infraestrutura de governança semelhante àquela que uma cloud oferece aos workloads. A liberdade estaria naquilo que pode ser construído. O controle estaria na infraestrutura que permite construir essas coisas com segurança.

O BCW, portanto, não deveria ser uma tentativa de centralizar todo o software empresarial em um único fornecedor. Sua função seria centralizar a experiência e as primitives comuns, mantendo aberta a possibilidade de incorporar software especializado.

Se o melhor sistema de folha de pagamento continuar sendo externo, ele pode ser integrado. Se surgir uma solução jurídica melhor, ela pode participar do ambiente. Se um desenvolvedor criar uma ferramenta especializada superior ao módulo nativo, ela pode ser instalada.

O fornecedor do BCW não precisa prever todas as necessidades, nem construir a melhor solução para cada uma delas. Quanto mais extensível for a plataforma, menos necessário será antecipar o futuro. O fornecedor constrói o substrato; o ecossistema descobre o que deve existir sobre ele.

Nesse cenário, o Marketplace não seria apenas um canal de distribuição. Seria parte do mecanismo pelo qual o BCW evolui mais rápido do que a própria empresa que o construiu.

O BCW não precisa vencer todo o software. Precisa tornar desnecessário sair dele para utilizá-lo.

## O lock-in por valor

Essa arquitetura também cria um tipo diferente de lock-in. Existe um lock-in baseado em restrição, no qual o cliente permanece porque sair é difícil. Existe outro, mais interessante, baseado em valor: o cliente permanece porque a plataforma se tornou o ambiente natural onde ele resolve seus problemas.

É assim que eu penso sobre uma plataforma como a AWS. Quando uma plataforma se torna suficientemente familiar, diante de um problema novo a pergunta deixa de ser “qual fornecedor devo contratar?” e passa a ser “como resolvo isso dentro da plataforma que já utilizo?”

O BCW deveria buscar algo semelhante no contexto empresarial. Ao longo do tempo, uma empresa não estaria apenas utilizando a plataforma. Estaria construindo sobre ela. Seus processos, workflows, agentes, integrações e conhecimento seriam moldados de acordo com a própria forma de operar.

Nesse ponto, o BCW deixaria de ser apenas o software que a empresa utiliza. Passaria a ser o ambiente que a própria empresa construiu para si mesma.

Skyrim também oferece uma analogia interessante aqui. Depois de centenas de horas e dezenas de mods instalados, o jogador não está simplesmente jogando o produto que a Bethesda entregou. Está jogando uma versão do jogo moldada pelas próprias escolhas.

O mesmo poderia acontecer com uma empresa. Depois de anos, o BCW não seria mais uma ferramenta genérica. Seria uma versão da plataforma moldada pela própria organização: com seus processos, seu conhecimento, seus agentes e sua forma particular de trabalhar.

É aí que o lock-in por valor se torna interessante. O verdadeiro lock-in não seria impedir a saída. Seria tornar a saída uma regressão. A empresa continuaria utilizando o BCW não porque estivesse presa a ele, mas porque teria construído ali uma forma de trabalhar que não encontraria pronta em nenhum outro lugar.

## Do Workspace à Business Network

Quando o BCW passa a concentrar a operação de uma empresa, conectar diferentes empresas se torna uma evolução natural. Se a plataforma conhece processos, pessoas, documentos, fornecedores e necessidades de uma organização, ela também possui parte do contexto necessário para facilitar as relações dessa organização com outras.

A VTEX oferece uma referência interessante. Em vez de tratar o comércio eletrônico apenas como uma aplicação isolada, sua plataforma participa de uma operação que conecta empresas, consumidores, vendedores, pagamentos, pedidos e outros elementos da transação. O BCW poderia levar uma lógica semelhante para além do comércio eletrônico, transformando o próprio ambiente de trabalho empresarial em uma camada de relacionamento entre organizações.

Isso poderia começar com um catálogo público de serviços. Um fornecedor poderia cadastrar sua empresa, produtos, serviços, capacidades, regiões de atendimento e condições comerciais. Esse catálogo seria acessível mesmo para empresas que ainda não utilizam o BCW, criando uma camada pública de descoberta sobre a Business Network.

A partir daí, descoberta e operação poderiam fazer parte do mesmo fluxo. Uma empresa poderia procurar um prestador de serviço, comparar alternativas, solicitar uma cotação, negociar, contratar, emitir um pedido e realizar o pagamento sem precisar reconstruir o contexto em diferentes sistemas. O fornecedor, por sua vez, poderia responder à demanda, acompanhar o relacionamento e operar seus próprios processos dentro do mesmo ambiente.

A diferença em relação a um marketplace tradicional estaria justamente no contexto. A plataforma já conhece os usuários, políticas, limites de aprovação e processos do comprador. Ao mesmo tempo, pode incorporar os dados, serviços, documentos e histórico do fornecedor.

Uma solicitação de compra poderia começar como uma necessidade interna e terminar como uma transação externa, sem exigir que alguém copie informações de um sistema para outro.

É nesse ponto que a Business Network se diferencia do Marketplace discutido anteriormente. O Marketplace conecta uma empresa a capacidades de software. A Business Network conecta uma empresa a outras empresas. No primeiro caso, o ecossistema amplia aquilo que pode ser construído dentro da plataforma. No segundo, amplia aquilo que pode ser realizado por meio dela. O BCW deixaria, então, de ser apenas um workspace individual e passaria a funcionar também como uma infraestrutura de relacionamento entre empresas.

Essa dinâmica introduziria um efeito de rede. Quanto mais empresas estiverem presentes, mais fornecedores e serviços poderão ser encontrados. Quanto mais fornecedores estiverem presentes, mais útil será a plataforma para as empresas. E quanto maior essa base, maior será também o mercado para módulos, agentes e soluções desenvolvidas por terceiros.

Nesse ponto, a fronteira entre software empresarial e infraestrutura de negócios começa a desaparecer. A plataforma não apenas ajuda uma empresa a operar. Ela passa a facilitar a descoberta, a contratação e a operação das relações que permitem que uma empresa funcione.

O ecossistema passa a reforçar a própria plataforma.

## O risco de criar uma nova complexidade

Existe, porém, um paradoxo na própria proposta. Uma plataforma capaz de fazer muitas coisas também pode se tornar uma plataforma difícil de usar.

A Salesforce é um bom exemplo desse desafio. Sua proposta como plataforma é poderosa justamente porque permite modelar processos, objetos, permissões, automações e integrações em profundidade. Mas essa flexibilidade também cria uma camada de administração que pode exigir conhecimento especializado.

Seria perfeitamente possível transformar o BCW em algo semelhante: uma plataforma extremamente poderosa, com centenas de recursos, configurações, permissões e possibilidades, mas que exigisse conhecimento especializado para ser utilizada.

Nesse caso, a plataforma teria apenas deslocado o problema. Em vez de administrar dezenas de sistemas independentes, a empresa passaria a administrar um único sistema excessivamente complexo.

A abstração, portanto, não pode ser apenas uma característica da interface. Ela precisa fazer parte da própria arquitetura do produto. A complexidade deve continuar existindo para quem precisa dela, mas não pode ser uma exigência para quem não precisa.

Um pequeno negócio deveria conseguir operar o BCW sem conhecer sua estrutura interna. Um profissional mais avançado deveria conseguir acessar configurações profundas quando necessário. Um administrador poderia definir políticas e workflows sofisticados sem obrigar cada funcionário a compreendê-los. Um arquiteto enterprise poderia acessar APIs, integrações e configurações avançadas sem transformar essa mesma experiência na interface padrão de todos os usuários.

A experiência de um empreendedor e a experiência de um arquiteto enterprise podem ser radicalmente diferentes sem que estejam utilizando produtos diferentes.

É aqui que a AWS oferece uma referência importante. A mesma infraestrutura consegue atender desde quem precisa apenas de uma abstração simples até quem precisa controlar detalhes muito mais profundos. A plataforma não precisa escolher entre simplicidade e sofisticação. Ela pode oferecer ambas, desde que consiga expor a complexidade de forma progressiva.

O BCW precisaria fazer o mesmo. Sua vantagem não estaria em eliminar a complexidade, algo que provavelmente não é possível em uma plataforma desse tipo, mas em fazer com que cada pessoa interaja apenas com a complexidade necessária para realizar seu trabalho.

A plataforma precisa oferecer profundidade sem impor profundidade. Talvez essa seja a condição fundamental para que uma plataforma desse tipo continue simples mesmo quando aquilo que existe por trás dela se torna extremamente sofisticado.

## Uma ideia que já está tomando forma

A ideia de BCW pode parecer uma extrapolação, mas seus componentes já estão sendo construídos, separadamente, por diferentes empresas.

A Salesforce transformou software empresarial em uma plataforma extensível de aplicações, automações e dados. A Microsoft vem aproximando produtividade, dados, desenvolvimento e agentes dentro de um mesmo ecossistema. Shopify e VTEX mostram como uma plataforma pode conectar a operação de uma empresa a um ecossistema de terceiros. A AWS demonstrou, em outra camada, como uma infraestrutura pode oferecer capacidades muito diferentes sem exigir que todos os usuários conheçam sua complexidade interna. O que ainda não está completamente resolvido é a combinação dessas ideias em uma experiência coerente. Talvez o BCW não seja uma ruptura que ainda está por acontecer, mas o resultado de movimentos que já começaram.

A IA está tornando mais barato criar software. As plataformas estão se tornando mais extensíveis. Agentes estão começando a participar da operação. Marketplaces estão conectando empresas a novas capacidades. E, ao mesmo tempo, a quantidade de software que uma empresa precisa administrar continua crescendo.

A questão, portanto, talvez não seja se teremos mais software, mas onde esse software vai viver. Aplicações agrupadas em suítes, cada uma preservando sua própria fronteira? Ou um ambiente no qual aplicações, agentes, dados, conhecimento, serviços externos e módulos especializados sejam apenas diferentes formas de ampliar aquilo que uma empresa consegue fazer?

A cloud transformou infraestrutura em capacidade sob demanda. O BCW poderia aplicar uma lógica semelhante ao software empresarial: não entregar uma coleção fixa de aplicações, mas um ambiente capaz de incorporar novas capacidades conforme elas se tornam necessárias.

Nesse modelo, a empresa não precisaria escolher antecipadamente todo o software que utilizará. Poderia começar com pouco, incorporar novas capacidades, conectar sistemas existentes, adicionar agentes e instalar extensões conforme sua operação evolui.

Isso muda a unidade de valor. O software deixa de ser apenas a aplicação que resolve um problema específico e passa a ser o ambiente que permite à empresa resolver problemas diferentes sem reconstruir sua forma de trabalhar a cada nova necessidade.

Talvez seja essa a mudança mais importante. O futuro do software empresarial pode não ser uma aplicação para cada coisa, nem necessariamente uma suíte que tenta fazer tudo. Pode ser uma plataforma sobre a qual cada empresa constrói, progressivamente, a sua própria maneira de trabalhar.
