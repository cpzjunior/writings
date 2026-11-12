# O dilema arquitetural do MCP

_Como distribuir capacidades para administrar a complexidade cognitiva dos agentes de IA._

**Resumo**: Defendo que o principal dilema arquitetural do MCP não está em centralizar ou distribuir servidores, mas em administrar como suas capacidades são descobertas, selecionadas e disponibilizadas aos agentes. Em ambientes corporativos, disponibilizar todas as ferramentas de uma só vez aumenta a complexidade cognitiva e dificulta a seleção contextual. A solução passa por separar o catálogo global de capacidades, a descoberta progressiva e a execução, combinando governança centralizada com autonomia dos domínios e roteamento inteligente. Assim, os agentes acessam apenas o que precisam, quando precisam, sem assumir a complexidade de administrar toda a infraestrutura. O desafio é transformar a diversidade de recursos corporativos em um ecossistema seletivo, seguro e eficiente.

---

No meu último artigo, "[Além dos Agentes Generalistas: Uma Arquitetura de Micro-Agentes de IA](https://cpzjunior.substack.com/p/alem-dos-agentes-generalistas-uma)", explorei uma questão que considero cada vez mais relevante à medida que os agentes de IA começam a ocupar um espaço mais significativo nas arquiteturas de software: será que devemos continuar concentrando responsabilidades em agentes generalistas ou começar a pensar em uma distribuição mais especializada da capacidade de raciocínio?

Naquela discussão, uma das ideias que emergiram foi a necessidade de separar o universo de capacidades que uma organização possui daquilo que cada agente efetivamente precisa conhecer durante uma execução. Um catálogo global pode ser amplo, enquanto o contexto de cada agente deve ser específico e construído de acordo com a tarefa que precisa realizar.

Essa premissa, entretanto, traz uma questão arquitetural que merece ser explorada. Se começamos a distribuir a inteligência entre diferentes agentes, como devemos organizar e disponibilizar as ferramentas e capacidades que eles utilizam para interagir com o mundo?

É aqui que o Model Context Protocol (MCP) introduz um novo dilema. Imagine uma grande organização, com dezenas de produtos, centenas de APIs e diferentes domínios de negócio. Cada produto começa a disponibilizar suas funcionalidades por meio de servidores MCP, tornando suas capacidades acessíveis aos agentes. Inicialmente, a solução parece relativamente simples: criar um servidor MCP para cada produto e permitir que os agentes se conectem aos servidores de que precisam.

Mas essa abordagem rapidamente levanta outras questões. E se um agente precisar acessar dezenas de produtos? Devemos conectá-lo a todos esses servidores? Devemos disponibilizar todas as ferramentas de uma só vez? O que acontece quando as descrições, os parâmetros e os contratos dessas ferramentas começam a consumir uma parcela significativa da janela de contexto?

Uma alternativa seria centralizar tudo em um grande servidor MCP corporativo. Mas será que estamos apenas recriando, sob uma nova interface, os mesmos problemas de concentração e acoplamento que historicamente procuramos resolver com arquiteturas distribuídas?

Talvez estejamos diante de uma nova categoria de problema. A arquitetura deixa de impactar apenas a organização dos componentes de software e passa a influenciar também a forma como os agentes descobrem, compreendem e selecionam suas capacidades.

Se antes discutíamos como distribuir a inteligência, agora precisamos discutir como distribuir o conhecimento sobre aquilo que a inteligência pode fazer.

## O problema da abundância de ferramentas

Uma das características mais interessantes do MCP é permitir que diferentes sistemas disponibilizem suas funcionalidades de maneira padronizada para agentes de IA. Em vez de depender exclusivamente de integrações desenvolvidas especificamente para cada aplicação, podemos estabelecer uma interface comum para descoberta e execução de ferramentas.

Essa padronização abre possibilidades importantes de integração, mas também cria uma consequência que merece atenção: quanto mais sistemas aderem ao protocolo, maior se torna o universo de capacidades potencialmente disponível para os agentes.

Em uma aplicação pequena, com poucos servidores e ferramentas bem delimitadas, esse cenário dificilmente representa um problema. Entretanto, quando transportamos essa arquitetura para uma organização com dezenas ou centenas de produtos, a situação muda consideravelmente.

Cada servidor pode disponibilizar diversas ferramentas, acompanhadas de descrições, parâmetros e schemas necessários para sua utilização. Quando um cliente agrega ferramentas de múltiplos servidores e apresenta essas definições ao modelo, o volume de informações cresce rapidamente. Parte delas será irrelevante para a tarefa atual, mas continuará ocupando espaço no contexto e ampliando o conjunto de alternativas que o modelo precisa avaliar.

É tentador tratar esse problema apenas como uma limitação da janela de contexto. Afinal, modelos cada vez maiores conseguem processar quantidades crescentes de informação. Mas acredito que essa interpretação seja insuficiente.

Mesmo quando existe espaço disponível, apresentar centenas de ferramentas não significa necessariamente melhorar a capacidade de decisão do agente. Um catálogo extenso pode aumentar a ambiguidade entre operações semelhantes, dificultar a seleção da ferramenta adequada e introduzir informações que não contribuem para a resolução da tarefa. A questão não está apenas na quantidade de tokens consumidos, mas também na qualidade do conjunto de alternativas apresentado ao modelo.

Existe, portanto, uma distinção importante entre três dimensões que frequentemente acabam tratadas como se fossem uma só. A primeira é a disponibilidade: quais capacidades existem na organização? A segunda é a acessibilidade: quais dessas capacidades um determinado agente está autorizado e tecnicamente habilitado a utilizar? A terceira é a relevância contextual: quais delas realmente precisam ser apresentadas durante uma execução específica?

Esses conjuntos não precisam ser iguais. Uma organização pode possuir milhares de capacidades, um agente pode ter acesso autorizado a algumas centenas e uma determinada tarefa pode exigir apenas um pequeno subconjunto delas.

Essa distinção é o ponto de partida para repensarmos a arquitetura MCP. O desafio não é simplesmente tornar todas as ferramentas acessíveis, mas administrar quais capacidades devem ser descobertas, disponibilizadas e utilizadas em cada contexto.

## O dilema da centralização e da distribuição

A primeira analogia que surge é com uma discussão bastante conhecida na arquitetura de software: centralizar funcionalidades em uma aplicação monolítica ou distribuí-las entre serviços independentes.

Poderíamos imaginar um grande servidor MCP corporativo, responsável por concentrar as ferramentas de diferentes produtos e disponibilizar um único ponto de conexão para os agentes. Essa abordagem simplifica a experiência de integração, facilita a administração de conexões e pode favorecer uma governança centralizada.

Por outro lado, à medida que o catálogo cresce, o servidor passa a concentrar responsabilidades cada vez maiores. A manutenção se torna mais complexa, a evolução pode gerar dependências entre domínios e a quantidade de ferramentas disponíveis continua crescendo. Centralizar a conexão não significa necessariamente resolver a sobrecarga cognitiva. Podemos ter um único ponto de acesso e, ainda assim, disponibilizar um universo de capacidades difícil de administrar.

No extremo oposto, poderíamos adotar servidores MCP independentes por produto ou domínio funcional. Cada equipe seria responsável por suas ferramentas, contratos e ciclos de evolução. Teríamos maior autonomia, isolamento e flexibilidade para administrar as capacidades.

Entretanto, essa distribuição também traz custos. A multiplicação de servidores exige mecanismos de descoberta, administração de conexões, autenticação, observabilidade e governança. Além disso, o agente ou a infraestrutura responsável por sua execução ainda precisaria decidir quais servidores utilizar e quais ferramentas apresentar.

É importante reconhecer que a analogia com monólitos e microsserviços tem seus limites. Estamos falando de universos arquiteturais diferentes. A distribuição de serviços procura administrar principalmente responsabilidades operacionais, dependências e escalabilidade. No contexto do MCP, existe uma dimensão adicional: a maneira como organizamos os servidores influencia a forma como suas capacidades são descobertas e disponibilizadas ao modelo.

Um servidor centralizado pode disponibilizar ferramentas seletivamente. Da mesma forma, dezenas de servidores distribuídos podem ser administrados por uma camada central de descoberta e roteamento. A topologia física dos servidores não precisa determinar a organização lógica das capacidades.

Essa percepção muda a natureza da discussão. Não precisamos necessariamente escolher entre centralizar ou distribuir tudo. Podemos distribuir a execução, centralizar determinadas responsabilidades de governança e manter mecanismos compartilhados de descoberta. O importante é separar a organização dos servidores da forma como suas capacidades chegam aos agentes.

## Do catálogo de servidores ao catálogo de capacidades

Uma possível resposta seria introduzir uma camada intermediária responsável por conhecer os servidores MCP disponíveis e administrar o acesso às suas capacidades.

Inicialmente, poderíamos pensar em um MCP Registry, funcionando como um inventário dos servidores existentes. Ele permitiria localizar integrações, identificar seus responsáveis, consultar metadados e conhecer informações relevantes sobre cada servidor.

Mas existe uma diferença importante entre conhecer os servidores de uma organização e conhecer aquilo que a organização consegue fazer por meio deles.

Um registry responde quais servidores existem, onde estão disponíveis e quem é responsável por sua manutenção. Um catálogo de capacidades precisa ir além. Deve representar as ferramentas disponibilizadas por esses servidores, suas finalidades, seus contratos, suas restrições, suas dependências e as condições necessárias para sua utilização.

Imagine uma organização que possua diferentes sistemas responsáveis por informações de clientes. Cada um disponibiliza ferramentas relacionadas a consultas cadastrais, posições financeiras e movimentações. Um inventário de servidores permite descobrir onde essas funcionalidades estão hospedadas. Um catálogo de capacidades permite compreender qual operação atende a determinada necessidade, qual fonte de dados deve ser considerada e quais condições precisam ser satisfeitas antes da execução.

Essa diferença é fundamental. A descoberta de uma ferramenta não deveria depender exclusivamente do conhecimento prévio sobre o servidor que a disponibiliza. Idealmente, o agente deveria conseguir partir de uma necessidade funcional e encontrar a capacidade correspondente, independentemente de sua localização física.

Nesse cenário, um MCP Hub ou Gateway poderia assumir responsabilidades complementares, como administrar conexões, intermediar chamadas, aplicar políticas de acesso e centralizar aspectos operacionais da comunicação. Entretanto, é importante não confundir essas responsabilidades. Conhecer a existência de uma ferramenta não significa necessariamente saber quando utilizá-la. Localizar um servidor também não significa que o agente precise estabelecer uma conexão permanente com ele.

Começamos, assim, a perceber a necessidade de separar três preocupações arquiteturais: o registro das capacidades disponíveis, a descoberta daquelas que fazem sentido para determinada demanda e a execução das operações nos servidores responsáveis.

Essa separação permite que a infraestrutura evolua sem obrigar os produtos a abandonar sua autonomia. Cada domínio pode continuar administrando seus servidores MCP, enquanto a organização mantém uma visão compartilhada de suas capacidades.

## Descoberta progressiva e seleção contextual

Uma vez estabelecido um catálogo global, surge uma possibilidade particularmente interessante: em vez de disponibilizar todas as ferramentas desde o início, o agente poderia começar com um conjunto reduzido de capacidades de descoberta.

Ao receber uma demanda, consultaria o catálogo para identificar ferramentas potencialmente relevantes. Somente depois dessa seleção as definições completas, incluindo parâmetros e schemas, seriam disponibilizadas para utilização.

Essa abordagem, frequentemente chamada de Progressive Tool Discovery, procura separar o universo global de ferramentas daquilo que efetivamente precisa estar presente no contexto do modelo.

O agente não precisa conhecer antecipadamente todas as capacidades disponíveis. Precisa ter condições de descobrir aquelas que serão necessárias.

Podemos imaginar esse processo em dois níveis. No primeiro, o catálogo apresenta informações resumidas sobre as capacidades, suficientes para permitir sua identificação e comparação. No segundo, depois de selecionar as alternativas mais adequadas, o agente recebe os contratos completos necessários para invocá-las.

Essa separação reduz a quantidade de informações inicialmente apresentada ao modelo e permite que o contexto seja construído progressivamente, conforme a tarefa evolui.

Entretanto, a descoberta dinâmica não é simplesmente uma questão de pesquisar ferramentas em um catálogo. A busca precisa ser suficientemente precisa para evitar que capacidades semelhantes, mas funcionalmente inadequadas, sejam selecionadas. Uma pesquisa que retorna operações relacionadas ao assunto, mas que não atendem efetivamente à necessidade, apenas transfere o problema da seleção para uma etapa anterior.

Por isso, acredito que a descoberta deveria combinar diferentes mecanismos. Informações estruturadas sobre domínio, finalidade, permissões e restrições podem reduzir o universo de possibilidades. Técnicas de busca lexical e semântica podem identificar ferramentas relacionadas à intenção apresentada. Um mecanismo de ranking pode então considerar a adequação funcional das alternativas encontradas.

Também é importante considerar dependências entre capacidades. Algumas operações podem exigir que outras sejam executadas previamente, enquanto determinadas funcionalidades podem depender de ferramentas disponibilizadas por diferentes servidores. A descoberta precisa conseguir representar essas relações, evitando tratar cada ferramenta como uma unidade completamente isolada.

Existe, contudo, uma questão interessante nesse modelo: para descobrir aquilo que ainda não conhece, o agente precisa ter acesso a algum mecanismo de descoberta. Isso significa que a própria capacidade de pesquisar ferramentas passa a ser uma capacidade fundamental da arquitetura. O catálogo deixa de ser apenas um repositório consultivo e passa a integrar o mecanismo de construção do contexto operacional do agente.

## Quando a descrição da ferramenta se torna parte da arquitetura cognitiva

Em um ecossistema pequeno, descrições inconsistentes podem ser corrigidas relativamente rápido. Quando existem centenas de ferramentas, entretanto, a qualidade dos metadados passa a ter impacto direto sobre a confiabilidade da arquitetura.

Imagine diferentes produtos disponibilizando ferramentas chamadas get_customer, retrieve_customer, find_client e get_customer_details. Todas parecem razoáveis, mas podem representar operações diferentes, consultar fontes distintas ou atender a necessidades específicas.

O modelo não conhece necessariamente essas fronteiras funcionais. Precisa inferi-las a partir das informações disponibilizadas pelo servidor: nome, descrição, parâmetros, schema de entrada e contexto de utilização.

Uma descrição como "Retrieve customer information" é tecnicamente válida, mas oferece pouca informação para orientar a decisão. Qual informação será retornada? Qual é a fonte oficial? Em quais situações essa ferramenta deve ser utilizada? Existem restrições? Quando outra ferramenta seria mais adequada?

Uma descrição realmente útil precisa explicar não apenas o que a operação faz, mas também sua finalidade, seu escopo, suas limitações e as circunstâncias em que deve ser escolhida.

Essa diferença é relevante porque, em uma arquitetura tradicional, uma API mal documentada prejudica principalmente os desenvolvedores responsáveis por integrá-la. Em uma arquitetura agentiva, uma ferramenta mal descrita pode prejudicar o próprio processo de decisão do agente.

A descrição deixa de ser apenas documentação. Ela passa a fazer parte da interface cognitiva entre o software e a inteligência artificial.

Por isso, acredito que um catálogo corporativo de capacidades precisaria ir além de armazenar nomes, descrições e schemas. Deveria incorporar informações sobre domínio funcional, finalidade, pré-condições, efeitos colaterais, dependências, permissões, origem dos dados e possíveis sobreposições com outras ferramentas.

Existe ainda uma distinção importante entre o contrato técnico e o contrato semântico de uma ferramenta. O schema define como invocar uma operação. O contrato semântico explica o que ela representa, em quais condições deve ser utilizada e quais garantias oferece sobre o resultado.

Duas ferramentas podem apresentar descrições muito semelhantes e ainda assim não ser intercambiáveis. Uma pode consultar uma fonte oficial, enquanto outra utiliza informações derivadas ou atualizadas em intervalos diferentes. A escolha correta não depende apenas da similaridade entre a intenção e a descrição, mas também da autoridade da fonte e das características do resultado esperado.

Nesse contexto, modelos de IA poderiam ajudar a avaliar descrições, identificar ambiguidades, sugerir melhorias e enriquecer os metadados. Entretanto, existe um limite importante: a inferência de um modelo não pode ser confundida com a definição oficial de uma capacidade. Informações técnicas, contratos e regras de negócio precisam continuar tendo fontes verificáveis e responsáveis identificados.

## O ciclo de vida das capacidades

Até aqui, estamos considerando que existe um catálogo capaz de representar o universo de capacidades de uma organização. Mas como garantir que esse catálogo permaneça atualizado?

Em uma empresa com diferentes produtos e equipes de desenvolvimento, novas funcionalidades são criadas, ferramentas são modificadas, contratos evoluem e APIs são descontinuadas. Um registry que depende exclusivamente de atualizações manuais corre o risco de se tornar mais um inventário desatualizado.

A descoberta dinâmica só funciona se as informações utilizadas para encontrar as ferramentas forem confiáveis.

Isso sugere que precisamos administrar o ciclo de vida das capacidades. Um novo servidor MCP deveria ser identificado e registrado. Novas ferramentas precisariam gerar atualizações no catálogo. Alterações de contratos deveriam provocar revalidação e versionamento. Capacidades descontinuadas precisariam deixar de ser apresentadas como opções válidas.

Talvez esse processo possa ser orientado a eventos, utilizando triggers provenientes dos pipelines de CI/CD, plataformas de gerenciamento de APIs, registros de serviços e dos próprios servidores MCP.

Nesse modelo, a publicação de uma nova versão poderia disparar automaticamente um processo de descoberta, registro e validação das capacidades. Mudanças de permissões poderiam atualizar as políticas associadas. Alterações incompatíveis poderiam exigir aprovação antes da publicação.

O catálogo deixaria de ser um documento mantido manualmente e passaria a funcionar como um inventário vivo das capacidades corporativas.

Entretanto, automatizar o registro não significa eliminar a responsabilidade sobre aquilo que está sendo registrado. Cada capacidade precisa possuir uma origem verificável, uma versão de referência e um responsável identificável. A infraestrutura deve conseguir determinar quem mantém a ferramenta, qual contrato está publicado e quais agentes ou aplicações podem utilizá-la.

Também precisamos considerar a consistência entre o catálogo e a execução. Imagine que uma ferramenta tenha seu contrato alterado enquanto um agente ainda utiliza uma definição anterior. A descoberta pode ter sido realizada corretamente, mas a execução falhará porque as informações utilizadas pelo agente não correspondem mais à versão disponibilizada pelo servidor.

Portanto, o ciclo de vida não termina no registro. Precisamos administrar compatibilidade, versionamento e descontinuação, garantindo que as definições apresentadas aos agentes correspondam às capacidades efetivamente disponíveis.

No fundo, estamos introduzindo uma nova preocupação arquitetural: não basta construir um catálogo de capacidades. Precisamos construir uma infraestrutura capaz de descobrir, registrar, validar, versionar e manter continuamente esse catálogo.

## E se o agente não precisasse manter todas as conexões?

Existe outra possibilidade que considero particularmente interessante, inclusive a partir de uma dificuldade que encontro na utilização cotidiana de agentes com múltiplos servidores MCP.

Em determinadas situações, preciso ativar ou desativar manualmente conexões com servidores que não fazem parte do contexto da tarefa. A razão é simples: manter muitas ferramentas simultaneamente disponíveis pode interferir na seleção daquelas que realmente interessam à execução.

Essa experiência sugere que talvez não seja suficiente controlar quais definições de ferramentas são carregadas no contexto. Poderíamos precisar também de uma camada responsável por administrar dinamicamente as próprias conexões com os servidores.

Imagine um roteador inteligente, um Intelligent MCP Router, que recebesse a demanda do agente, interpretasse sua intenção e identificasse quais domínios funcionais seriam necessários. A partir dessa análise, poderia consultar o catálogo, localizar as capacidades relevantes e disponibilizar suas ferramentas por meio dos servidores correspondentes.

Se durante a tarefa surgisse a necessidade de uma nova capacidade, o roteador poderia realizar outra consulta, identificar o servidor responsável e incorporar as novas ferramentas ao conjunto disponível.

Da mesma forma, servidores que deixassem de ser relevantes poderiam ter suas ferramentas retiradas do conjunto exposto ao agente. Dependendo da estratégia de conexão adotada, suas sessões também poderiam ser encerradas.

A infraestrutura passaria a administrar dinamicamente o universo de possibilidades apresentado ao modelo.

Essa abordagem, que poderíamos chamar de Context-Aware MCP Routing, acrescenta uma dimensão interessante à arquitetura. O roteador não seria apenas um intermediário responsável por encaminhar chamadas. Ele participaria da administração do contexto operacional do agente.

Entretanto, existe uma distinção técnica importante. Desconectar um servidor MCP não é a mesma coisa que simplesmente deixar de expor suas ferramentas ao modelo. Podemos manter uma sessão ativa e controlar quais ferramentas são disponibilizadas. Também podemos manter o servidor conectado, mas não carregar suas definições no contexto atual.

Cada alternativa tem custos diferentes. Estabelecer conexões sob demanda pode introduzir latência, enquanto manter sessões abertas pode consumir recursos. Alguns servidores também possuem estados que não podem ser descartados arbitrariamente.

Por isso, não acredito que a solução esteja necessariamente em conectar e desconectar servidores continuamente. Uma arquitetura mais eficiente provavelmente combinará diferentes estratégias: manter determinados servidores disponíveis, carregar ferramentas seletivamente e ativar novas conexões apenas quando necessário.

Também é importante separar a seleção contextual do roteamento de execução. Uma ferramenta pode ser considerada relevante sem estar autorizada para determinado agente. Da mesma forma, uma capacidade pode estar disponível e autorizada, mas não fazer sentido para a tarefa atual.

O roteador precisa respeitar essas fronteiras. A seleção semântica não substitui a autorização. Identidade do agente, contexto do usuário, permissões, políticas de domínio e auditoria precisam ser considerados antes que uma ferramenta seja disponibilizada ou executada.

Essa distinção é especialmente importante em ambientes corporativos, nos quais determinadas operações podem produzir efeitos financeiros, alterar informações ou acessar dados protegidos. A infraestrutura não pode delegar ao modelo a decisão sobre aquilo que ele está autorizado a fazer.

## Uma arquitetura em múltiplos planos

Quando reunimos essas ideias, começamos a perceber que o problema não possui uma única dimensão. A organização dos servidores, o registro das capacidades, a descoberta contextual e a execução das ferramentas são responsabilidades relacionadas, mas que não precisam estar concentradas no mesmo componente.

Uma forma de organizar essa arquitetura seria separá-la em três planos. O primeiro seria o plano de controle, responsável pelo catálogo global de capacidades, metadados, contratos, versionamento, ownership e políticas de governança. Sua função seria manter uma representação confiável daquilo que a organização disponibiliza por meio de seus servidores MCP.

O segundo seria o plano de descoberta e seleção, responsável por interpretar as necessidades apresentadas, consultar o catálogo, identificar capacidades relevantes e determinar quais ferramentas devem ser disponibilizadas em determinado contexto. É nesse plano que a descoberta progressiva e a seleção contextual ganhariam forma.

O terceiro seria o plano de execução, responsável pelas conexões com os servidores, autenticação, autorização, invocação das ferramentas, tratamento dos resultados e observabilidade. Aqui, os servidores MCP continuariam distribuídos e sob responsabilidade dos respectivos domínios de negócio.

Essa separação permite combinar governança corporativa com autonomia dos produtos. O catálogo pode ser compartilhado, enquanto os servidores permanecem distribuídos. A descoberta pode utilizar mecanismos centralizados, enquanto a execução continua sob responsabilidade dos sistemas de origem. O roteamento pode ser coordenado por uma camada comum sem exigir que todas as ferramentas passem a residir em um único servidor.

É importante observar que essa divisão representa uma separação lógica de responsabilidades, não necessariamente três plataformas ou serviços independentes. Dependendo do porte da organização, algumas dessas funções podem coexistir no mesmo componente. O objetivo é evitar que decisões de descoberta, governança e execução fiquem acopladas apenas porque pertencem ao mesmo ecossistema MCP.

Essa arquitetura também permite que o mecanismo de seleção evolua independentemente dos servidores. Podemos aprimorar a busca semântica, alterar critérios de ranking, incorporar novas políticas ou modificar a estratégia de conexão sem exigir que cada produto reestruture suas integrações.

O próprio catálogo pode evoluir para representar não apenas ferramentas individuais, mas também capacidades compostas, que dependem de operações disponibilizadas por diferentes servidores. Nesse cenário, ele começa a funcionar como um mapa das capacidades corporativas, aproximando a visão técnica dos serviços daquilo que a organização efetivamente consegue realizar.

## O novo desafio da arquitetura MCP

A adoção de arquiteturas agentivas em ambientes corporativos amplia o escopo das decisões de integração. Não basta definir como os sistemas expõem suas funcionalidades; é necessário estabelecer como essas funcionalidades serão descritas, localizadas, selecionadas e disponibilizadas de acordo com as necessidades de cada agente.

O MCP oferece uma interface padronizada para conectar modelos a ferramentas, mas não resolve, por si só, a organização desse ecossistema. Essa responsabilidade cabe à arquitetura que o envolve, incluindo mecanismos de catalogação, descoberta, governança e roteamento. É nesse nível que se torna possível conciliar a distribuição das capacidades entre diferentes domínios com uma gestão coerente de sua utilização.

As escolhas sobre granularidade dos servidores, seleção contextual e separação entre descoberta, autorização e execução terão consequências diretas sobre a escalabilidade e a governança das plataformas agentivas. Mais do que uma questão de implementação do protocolo, trata-se de definir como a organização pretende administrar suas capacidades em um cenário no qual agentes passam a interagir com um conjunto cada vez mais amplo de sistemas.

O desafio arquitetural está em transformar essa diversidade de recursos em um ecossistema que possa ser explorado de forma seletiva, segura e eficiente, sem transferir para o agente a complexidade de administrar toda a infraestrutura que o sustenta.
