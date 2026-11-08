# Service as a Service: quando serviços se tornam capacidades consumíveis

_Se aprendemos a consumir infraestrutura, plataformas e software como serviço, por que ainda tratamos tantos serviços como entregas isoladas?_

**Resumo**: Neste artigo, proponho uma reflexão: se aprendemos a consumir infraestrutura, plataformas e software como serviços, por que ainda tratamos tantas capacidades das organizações como entregas isoladas? Acredito que podemos mudar essa perspectiva, pensando em serviços que sejam descobertos, acessados e consumidos continuamente por diferentes áreas, aplicações e processos. Isso exige olhar além da entrega de projetos e considerar como essas capacidades são disponibilizadas, operadas, governadas e evoluídas ao longo do tempo. Não se trata de criar mais um modelo arquitetural, mas de questionar se estamos aproveitando todo o valor daquilo que já construímos.

---

Existe uma mudança importante na forma como consumimos tecnologia. Durante muito tempo, para utilizar determinada capacidade computacional, uma empresa precisava adquirir equipamentos, instalar sistemas, configurar ambientes e manter toda a estrutura necessária para operá-los. A evolução dos modelos de serviço mudou essa relação. Passamos a consumir infraestrutura, plataformas e software sem necessariamente possuir ou administrar os recursos que os sustentam. Mais do que uma mudança tecnológica, foi uma transformação na maneira de pensar acesso, responsabilidade e valor.

Essa evolução me levou a uma reflexão: se aprendemos a disponibilizar infraestrutura, plataformas e software como serviços, por que ainda temos tanta dificuldade em pensar os serviços que nossas próprias organizações oferecem da mesma maneira?

A provocação que proponho chamar de _Service as a Service_ parte dessa pergunta. Não se trata de apresentar um novo modelo arquitetural, uma metodologia ou uma categoria que precise disputar espaço com conceitos já estabelecidos. É uma maneira de olhar para algo que já existe, mas que nem sempre é concebido para ser reutilizado, acessado e consumido continuamente. A ideia é simples: e se passássemos a tratar os serviços de uma organização como capacidades disponíveis para diferentes consumidores, em vez de entregas vinculadas a projetos, equipes ou estruturas específicas?

## Da tecnologia consumida à capacidade organizacional

A ideia de consumir software como serviço não é nova. Há décadas, empresas utilizam aplicações hospedadas e operadas por terceiros, sem precisar instalar, administrar ou manter toda a estrutura necessária para sua execução. O modelo ganhou escala e protagonismo com a expansão da internet e, posteriormente, com a computação em nuvem, mas sua essência é anterior a esses movimentos: oferecer acesso a uma capacidade tecnológica sem transferir ao consumidor toda a responsabilidade por construí-la e operá-la.

Com a evolução da computação em nuvem, essa lógica passou a alcançar outras camadas. A infraestrutura, antes adquirida e administrada diretamente pelas empresas, tornou-se consumível como serviço. Plataformas de desenvolvimento também passaram a ser disponibilizadas sob demanda, abstraindo parte da complexidade de preparar e manter ambientes tecnológicos. Assim se consolidaram os modelos que conhecemos como SaaS, IaaS e PaaS.

Embora atendam a necessidades diferentes, esses modelos compartilham uma característica importante: mudam a relação entre quem oferece uma capacidade e quem a utiliza. O consumidor não precisa necessariamente conhecer ou administrar todos os componentes que tornam o serviço possível. Precisa compreender o que está disponível, como acessá-lo, quais resultados pode esperar e quais responsabilidades permanecem sob seu controle. A complexidade não desaparece, mas passa a ser administrada em outra camada e, muitas vezes, por outro responsável. O consumidor pode, assim, concentrar seus esforços naquilo que pretende realizar, em vez de precisar construir e operar tudo o que é necessário para chegar ao resultado.

Essa lógica, já consolidada no universo da tecnologia, me leva a uma pergunta: por que não pensar da mesma forma sobre as capacidades que existem dentro das próprias organizações?

É comum encontrar empresas em que determinadas capacidades são desenvolvidas para atender a uma necessidade específica. Um projeto identifica um problema, mobiliza uma equipe, define um escopo e entrega uma solução. O resultado passa a ser utilizado por uma aplicação, por uma área de negócio ou por um processo. Em muitos casos, porém, a capacidade permanece fortemente associada ao contexto que motivou sua criação.

O problema aparece quando outra área identifica uma necessidade semelhante. Em vez de consumir algo que já existe, pode ser necessário iniciar um novo projeto, negociar prioridades, encontrar os responsáveis pela solução original e construir integrações específicas. Mesmo quando a capacidade poderia ser reutilizada, sua disponibilidade não é necessariamente evidente, seu acesso pode não estar estruturado e seu consumo pode depender de acordos informais.

Isso acontece porque frequentemente organizamos a entrega de tecnologia em torno de projetos e sistemas, mas não necessariamente organizamos a disponibilidade das capacidades que esses projetos produzem. O projeto tem início, escopo, orçamento e encerramento. A capacidade, por outro lado, pode continuar gerando valor por muitos anos, atendendo a diferentes consumidores e participando de processos que sequer existiam quando foi criada.

Talvez seja útil, portanto, separar a entrega que originou uma capacidade da própria capacidade que permanece disponível depois dela. Um serviço não precisa existir apenas porque um projeto demanda sua implementação ou porque uma aplicação específica depende dela. Pode ser concebido para atender a uma necessidade recorrente, com diferentes consumidores e formas de utilização que evoluem ao longo do tempo.

Isso não significa transformar tudo em serviço compartilhado, nem pressupor que toda funcionalidade deva ser exposta para toda a organização. Significa reconhecer que algumas capacidades possuem valor além do contexto em que foram inicialmente desenvolvidas e que esse valor pode ser ampliado quando sua disponibilidade e seu consumo são pensados de forma deliberada.

## Serviço não é apenas produto

Vale fazer uma distinção. Quando falo em serviço, não estou necessariamente me referindo a um produto de software ou a uma aplicação. Um produto costuma ser reconhecido por sua proposta de valor, por seus usuários e pela experiência que oferece. Um serviço pode estar por trás de vários produtos e processos, viabilizando uma capacidade específica sem precisar se apresentar como uma solução completa para o consumidor.

Uma aplicação pode, por exemplo, oferecer uma experiência de pagamento. Por trás dela existem diferentes capacidades: autenticação, validação de dados, análise de risco, autorização, liquidação e notificação. Essas capacidades podem estar distribuídas entre sistemas e equipes diferentes, mas não precisam ser consumidas exclusivamente pela aplicação que primeiro as reuniu.

A diferença está na perspectiva. Quando pensamos apenas no produto ou na aplicação, tendemos a organizar a solução em torno da experiência final. Quando pensamos também nas capacidades que a sustentam, começamos a enxergar oportunidades de reutilização e composição. Um mesmo serviço pode participar de diferentes produtos, jornadas e processos, desde que exista uma forma clara de acessá-lo e de compreender suas condições de uso.

Uma analogia ajuda a concretizar a ideia. Imagine uma instituição financeira que desenvolve uma capacidade de prevenção a fraudes. No modelo mais restrito, essa capacidade pode nascer como parte de um projeto de cartões, com regras, integrações e infraestrutura voltadas para aquele contexto. Se outra área quiser utilizá-la em uma jornada de abertura de conta ou em uma transferência, talvez precise desenvolver uma solução própria ou negociar uma integração específica com a equipe responsável.

Sob uma perspectiva de serviço, a capacidade de prevenção a fraudes passa a ser pensada para atender diferentes contextos de negócio. Cada consumidor fornece as informações necessárias, recebe uma avaliação de risco e utiliza o resultado dentro de seu próprio processo. O serviço pode evoluir internamente, incorporar novos modelos analíticos e aprimorar seus mecanismos de detecção sem exigir que cada consumidor reconstrua essa capacidade.

Naturalmente, isso não significa que todos os contextos devam receber a mesma resposta ou utilizar exatamente as mesmas regras. Uma transação com cartão, uma abertura de conta e uma transferência possuem características e riscos distintos. O serviço precisa oferecer parâmetros, contratos e possibilidades de configuração compatíveis com essas diferenças. A reutilização não está em obrigar todos os consumidores a fazer a mesma coisa, mas em evitar que cada um precise construir e operar, isoladamente, uma capacidade que poderia ser compartilhada.

## Consumir não significa apenas chamar uma API

Quando falamos em disponibilizar serviços, é comum associar imediatamente a ideia a APIs. Elas são, de fato, um mecanismo importante para expor capacidades de maneira estruturada, com contratos explícitos e integração entre sistemas. Mas reduzir o consumo de serviços a chamadas de API seria limitar desnecessariamente a discussão.

Uma capacidade pode ser consumida por diferentes mecanismos, dependendo da natureza da interação. Pode existir uma interface para interação humana, uma API para comunicação síncrona entre aplicações, eventos para notificar mudanças de estado, filas para processar solicitações de forma assíncrona ou automações para executar atividades recorrentes. O mecanismo deve ser consequência da necessidade de consumo, e não uma decisão que define previamente o que o serviço pode ser.

Essa distinção ganha ainda mais relevância com a evolução da inteligência artificial. Agentes de IA começam a atuar como consumidores de capacidades organizacionais. Em vez de apenas apresentar informações ou responder a perguntas, podem identificar uma necessidade, selecionar uma ferramenta, solicitar uma operação e combinar diferentes serviços para concluir uma tarefa.

Iniciativas e padrões como MCP e A2A ajudam a ilustrar esse movimento. O primeiro está associado à conexão de modelos e agentes com ferramentas e fontes de contexto; o segundo, à comunicação e colaboração entre agentes. Não é necessário assumir que esses padrões serão a forma definitiva de integração para reconhecer o ponto central: os consumidores de serviços estão deixando de ser exclusivamente aplicações tradicionais e usuários humanos.

Isso amplia a importância de tornar as capacidades descobertas, compreensíveis e acessíveis por contratos claros. Um agente precisa saber o que um serviço faz, quais informações deve fornecer, quais resultados pode receber e quais operações está autorizado a executar. Nesse cenário, uma capacidade mal documentada ou dependente de conhecimento informal torna-se ainda mais difícil de consumir.

A questão, portanto, não é simplesmente disponibilizar mais APIs ou adotar novos protocolos. É pensar a experiência de consumo de uma capacidade, independentemente de quem ou do que esteja consumindo.

## O que precisa existir por trás de um serviço

Disponibilizar uma capacidade para diferentes consumidores exige mais do que criar um ponto de integração. É necessário estabelecer um conjunto de condições que permita seu uso de forma previsível e sustentável.

O primeiro aspecto é o contrato. O consumidor precisa compreender o que o serviço oferece, quais informações são necessárias, quais resultados serão produzidos e quais limitações existem. O contrato também precisa deixar claras as condições de uso, os comportamentos esperados e as responsabilidades de cada parte. Sem isso, a integração pode até funcionar tecnicamente, mas continuará dependendo de conhecimento tácito e de negociações específicas.

Também é necessário tratar identidade, autenticação, autorização e segregação de acesso. Nem todo consumidor pode executar todas as operações, e diferentes contextos podem exigir níveis distintos de permissão. Segurança não pode ser um complemento incorporado depois que o serviço já está disponível. Ela faz parte do próprio modelo de consumo.

Outro ponto é a operação. Um serviço consumido por diferentes áreas ou aplicações passa a ter impacto potencialmente maior do que uma solução restrita a um único contexto. Disponibilidade, desempenho, capacidade, observabilidade, continuidade e tratamento de falhas deixam de ser preocupações internas da equipe responsável e passam a influenciar diretamente a experiência dos consumidores. Versionamento e compatibilidade também precisam ser considerados, porque a evolução do serviço não pode interromper arbitrariamente quem depende dele.

Tudo isso exige uma definição clara de responsabilidade. Quem é o responsável pelo serviço? Quem decide sua evolução? Quem prioriza melhorias? Quem responde quando a capacidade deixa de atender ao nível esperado? Quem avalia o impacto de uma mudança sobre os consumidores existentes?

Essas perguntas revelam uma dimensão organizacional importante. Um serviço não se sustenta apenas porque existe uma equipe técnica capaz de mantê-lo. É preciso haver ownership sobre a capacidade, com responsabilidade por sua evolução e por seu valor ao longo do tempo. Isso não significa necessariamente criar uma equipe independente para cada serviço, mas reconhecer que a responsabilidade pela capacidade não termina com a entrega do projeto que a originou.

É uma mudança sutil, mas relevante: o sucesso deixa de ser medido apenas pela conclusão da implementação e passa a considerar também a qualidade e a continuidade do serviço disponibilizado.

## Compartilhar tem custos e limites

A ideia de transformar capacidades em serviços consumíveis pode parecer naturalmente vantajosa. Reutilizar evita duplicações, concentra conhecimento e permite que diferentes áreas se beneficiem de uma mesma implementação. Mas compartilhar também cria dependências e custos que precisam ser considerados.

Um serviço utilizado por muitos consumidores pode se tornar um ponto crítico da organização. Uma alteração aparentemente simples pode afetar processos distintos, cada um com suas próprias regras, prioridades e janelas de mudança. A necessidade de atender a múltiplos contextos pode aumentar a complexidade do contrato e dificultar a evolução. Em alguns casos, a abstração criada para atender a todos acaba ficando tão genérica que deixa de atender bem a qualquer um.

Existe também o risco de centralizar excessivamente capacidades que deveriam permanecer próximas do contexto de negócio. Nem toda funcionalidade precisa ser compartilhada. Algumas são específicas, pouco reutilizáveis ou dependentes de decisões locais. O custo de criar e operar um serviço comum pode ser maior do que o benefício de sua reutilização.

Por isso, a questão não deveria ser transformar tudo em serviço, mas identificar onde existe uma capacidade com potencial de atender diferentes consumidores de maneira consistente. A decisão precisa considerar frequência de uso, grau de especialização, criticidade, custo de manutenção, dependências e autonomia necessária aos consumidores.

A padronização também tem limites. Um serviço compartilhado não deve impor uniformidade artificial a processos que possuem necessidades legítimas diferentes. O objetivo é oferecer uma capacidade comum sem apagar as particularidades dos contextos em que ela será utilizada. Encontrar esse equilíbrio é parte do trabalho de arquitetura, mas também de gestão e governança.

## Da entrega de projetos à disponibilidade de capacidades

Talvez a principal reflexão trazida por _Service as a Service_ não esteja na tecnologia, mas na forma como as organizações se estruturam para produzir e disponibilizar valor.

Em muitas empresas, projetos são a principal unidade de mobilização de recursos e execução de mudanças. Isso faz sentido: projetos ajudam a organizar investimentos, estabelecer objetivos, controlar escopo e coordenar entregas. O problema surge quando essa lógica passa a determinar também a forma como as capacidades são mantidas e consumidas depois que a entrega termina.

Uma organização pode concluir dezenas de projetos bem-sucedidos e, ainda assim, acumular soluções fragmentadas, integrações redundantes e capacidades difíceis de reutilizar. Cada iniciativa resolve seu problema, mas o conjunto não necessariamente evolui como um ecossistema coerente.

Pensar em serviços como capacidades consumíveis sugere outra perspectiva. Projetos continuam sendo importantes para criar ou transformar soluções, mas as capacidades resultantes podem ter um ciclo de vida próprio. Elas precisam ser descobertas, acessadas, operadas, governadas e aprimoradas continuamente. Seu valor não está apenas no que entregaram no passado, mas no que ainda podem viabilizar para diferentes consumidores.

Essa visão também aproxima arquitetura e gestão. A arquitetura deixa de olhar somente para os componentes e integrações de uma solução específica e passa a considerar como as capacidades se relacionam, quais podem ser compartilhadas e quais dependências surgem quando diferentes partes da organização passam a consumi-las. A gestão, por sua vez, precisa considerar a continuidade dessas capacidades, sua priorização e a responsabilidade por sua evolução.

Não se trata de substituir uma estrutura orientada a projetos por outra estrutura rígida, organizada em torno de serviços. Trata-se de reconhecer que a entrega de uma solução e a disponibilização de uma capacidade são problemas relacionados, mas diferentes. Confundi-los pode fazer com que a organização seja eficiente em entregar projetos e pouco eficiente em aproveitar aquilo que construiu.

## Uma provocação, não uma nova receita

Talvez _Service as a Service_ não precise ser mais do que uma provocação. Não é uma tentativa de renomear conceitos conhecidos, propor uma nova arquitetura ou estabelecer um modelo universal. SOA, APIs, plataformas internas, arquitetura orientada a eventos e gestão de capacidades já tratam de partes importantes dessa discussão. O que me interessa é a pergunta que surge quando aproximamos essas ideias da maneira como as organizações efetivamente trabalham.

Se conseguimos consumir infraestrutura, plataformas e software como serviços, por que tantas capacidades organizacionais ainda são tratadas como entregas isoladas? Por que precisamos reconstruir soluções que já existem? Por que o acesso a determinadas capacidades depende tanto de conhecer a equipe certa, negociar uma integração específica ou encontrar alguém que saiba como determinado sistema funciona?

Talvez parte da resposta esteja na forma como concebemos nossas soluções. Construímos projetos, aplicações e sistemas para resolver problemas concretos, mas nem sempre pensamos nas capacidades que estamos criando como algo que poderá ser consumido por outros, de maneira independente e contínua.

Mudar essa perspectiva não exige transformar tudo em serviço, nem adotar uma tecnologia específica. Exige reconhecer quando uma capacidade tem valor além de seu contexto original e considerar, desde sua concepção, como ela poderia ser disponibilizada para outros consumidores.

No fim, a pergunta não é se precisamos de mais um modelo arquitetural. É se estamos aproveitando todo o valor das capacidades que já construímos. Talvez seja hora de deixar de pensar apenas nas soluções que entregamos e começar a pensar também nos serviços que somos capazes de oferecer continuamente.
