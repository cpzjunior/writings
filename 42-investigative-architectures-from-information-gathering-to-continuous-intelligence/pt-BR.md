# Arquiteturas Investigativas: da coleta de informação à inteligência contínua

_Uma arquitetura orientada por IA para investigar perguntas de negócio, aprender com o contexto e acompanhar continuamente o que pode mudar uma decisão._

**Resumo:** Defendo uma arquitetura de inteligência que trate a investigação como sua unidade principal: um processo persistente que formula hipóteses, conecta evidências, preserva contexto e retoma o trabalho quando novas informações surgem. Um scheduler decide quais investigações merecem processamento, quanto esforço vale a pena investir e qual deve ser o próximo passo, enquanto memória, feedback humano e governança dão continuidade e confiabilidade ao processo. Assim, a IA deixa de apenas coletar, monitorar ou resumir informação e passa a sustentar um processo contínuo de investigação, no qual a própria arquitetura aprende com o que descobriu e volta ao problema quando o mundo muda.

------------------------------------------------------------------------

Enquanto escrevia “[O Anti-Mago: Um Projeto Literário](https://cpzjunior.substack.com/p/o-anti-mago-um-projeto-literario)”, fui percebendo que a trajetória de Alden como investigador estava me fazendo pensar cada vez mais sobre o próprio ato de investigar: seguir pistas, formular hipóteses, conectar acontecimentos e descobrir que uma resposta pode mudar a pergunta seguinte. Em algum momento, essa ideia saiu da ficção. Comecei a pensar que o papel de um investigador também poderia ser interessante em um produto. Não como metáfora, mas como uma forma diferente de pensar sistemas de inteligência.

Imagine uma empresa prestes a contratar um fornecedor estratégico. Antes de assinar o contrato, surge uma pergunta simples: existem sinais públicos de que esse fornecedor esteja entrando em uma situação que possa afetar nossa relação comercial?

Responder a essa pergunta pode envolver notícias, bases públicas, reclamações, informações corporativas e redes sociais. Quando algo parece relevante, novas buscas são necessárias para entender o contexto.

Agora imagine entregar essa pergunta a uma arquitetura de inteligência. Ela pesquisa o fornecedor, suas empresas relacionadas e acontecimentos recentes. Encontra uma notícia relevante, identifica uma empresa relacionada e abre uma nova linha de investigação. Depois encontra informações conflitantes e procura fontes mais próximas do fato original. Uma hipótese ganha força, outra perde relevância e uma nova pergunta surge. Em determinado momento, a arquitetura pode concluir que ainda não há evidências suficientes para recomendar uma ação e colocar aquela investigação em monitoramento.

Dias depois, surge uma nova informação. A investigação volta à fila, mas não começa do zero. Ela retoma o estado anterior, com suas hipóteses, evidências, fontes e incertezas.

É esse comportamento que me interessa. A mesma arquitetura poderia investigar um concorrente, uma oportunidade de mercado, uma tecnologia emergente, um potencial cliente ou uma hipótese estratégica. O ponto de partida deixa de ser apenas a entidade que queremos monitorar e passa a ser a pergunta que precisamos investigar.

## De monitoramento para investigação

Existe uma diferença importante entre monitorar e investigar. Um sistema de monitoramento pode avisar que uma empresa foi mencionada em uma notícia, mas a menção, isoladamente, não diz necessariamente o que aconteceu, qual é sua relevância ou se deveria alterar alguma decisão.

Em segurança da informação, um SOC, Security Operations Center, existe justamente para lidar com esse problema. Logs, eventos de rede, alertas de endpoints e outras fontes produzem continuamente sinais que, isoladamente, podem significar pouco. O SOC correlaciona esses eventos, procura padrões, investiga o contexto, avalia a severidade e, quando necessário, aciona uma resposta. Um alerta não é necessariamente um incidente. O trabalho está em entender o que existe por trás dele.

A mesma lógica pode ser aplicada à informação pública e às perguntas de negócio. Uma reclamação é um sinal. Dez reclamações semelhantes em poucos dias podem indicar outra coisa. Um vídeo pode ampliar a exposição, uma publicação pode acelerar a propagação e uma reportagem pode transformar um problema pontual em um incidente em evolução. O trabalho passa a ser entender como esses eventos se relacionam, quais hipóteses explicam melhor o que está acontecendo e o que ainda precisa ser descoberto.

Isso também muda o papel da busca. Uma busca tradicional termina quando encontramos uma resposta satisfatória. Em uma investigação, o resultado de uma busca pode determinar o que deve ser pesquisado em seguida. Uma notícia sobre uma tecnologia pode levar à investigação da empresa que a desenvolveu. Uma aquisição pode gerar perguntas sobre investidores, tecnologia ou outros movimentos relacionados. Uma informação conflitante pode exigir uma fonte primária.

A investigação evolui conforme novas evidências aparecem. Algumas linhas são descartadas, outras ganham prioridade e novas perguntas surgem. A arquitetura precisa acompanhar esse processo, mantendo o contexto do que já foi descoberto e decidindo qual deve ser o próximo passo. A diferença não está em fazer uma IA pesquisar a Internet. Está em fazer uma arquitetura manter uma investigação.

Isso também muda a maneira como pensamos os agentes. Em vez de agentes permanentemente executando buscas, podemos ter investigações permanentemente existentes, cada uma com seu próprio estado e esperando pelo momento adequado para receber capacidade de processamento.

## Um scheduler para investigações

Quando comecei a pensar nessa arquitetura, uma analogia com sistemas operacionais me pareceu particularmente útil. Um sistema operacional precisa administrar uma capacidade limitada de processamento entre diversos processos. Ele acompanha o estado de cada processo, define prioridades, interrompe alguns, retoma outros e distribui o tempo de CPU de acordo com o que precisa ser executado.

Uma arquitetura investigativa poderia funcionar de maneira semelhante. Em vez de termos um conjunto de agentes executando buscas continuamente, teríamos um conjunto de investigações persistentes, cada uma com seu próprio estado, prioridade, objetivo, nível de incerteza e orçamento. Algumas estariam ativas, outras aguardando novas evidências e outras praticamente concluídas. O scheduler seria responsável por decidir qual delas recebe a próxima unidade de capacidade de processamento.

Imagine dezenas ou milhares de investigações acontecendo simultaneamente. Uma acompanha um fornecedor que não apresenta nenhum sinal relevante há semanas. Outra investiga um concorrente que anunciou recentemente uma aquisição. Uma terceira acompanha uma tecnologia emergente. Uma quarta tenta entender uma sequência de reclamações que começou há poucas horas. Não faria sentido tratar todas da mesma maneira.

A primeira talvez precise apenas de uma nova verificação periódica. A segunda pode exigir uma investigação mais profunda. A terceira pode permanecer em baixa prioridade até que apareça algum sinal relevante. A quarta, dependendo do impacto potencial e da velocidade dos acontecimentos, pode precisar receber capacidade imediatamente.

E o próximo ciclo de processamento também depende do estado da investigação. Uma investigação pode começar procurando notícias recentes. Depois de encontrar uma empresa relacionada, o próximo ciclo pode ser dedicado a entender essa nova entidade. Se surgir uma informação conflitante, pode ser necessário procurar uma fonte primária. Se aparecer uma alteração societária, pode fazer sentido investigar os controladores. Se várias fontes estiverem reproduzindo a mesma informação, o próximo passo pode ser identificar sua origem.

O scheduler, portanto, não está simplesmente perguntando “qual busca executar agora?”. Está perguntando “qual investigação merece atenção agora e qual é a ação mais útil que podemos executar dentro dela?”.

Isso aproxima a arquitetura de um sistema de processos concorrentes. Uma investigação pode ser interrompida para dar lugar a outra mais urgente. Pode gerar uma subinvestigação que passa a competir por recursos. Uma linha pode ser encerrada enquanto outra continua. Uma investigação pode ficar bloqueada aguardando novas evidências e voltar à fila quando alguma coisa mudar.

A analogia com o sistema operacional também ajuda a pensar em um problema que costuma ficar escondido quando falamos de agentes. Não precisamos de um agente dedicado para cada problema. Assim como um sistema operacional compartilha capacidade de processamento entre processos, uma arquitetura investigativa pode compartilhar capacidade agentiva entre investigações.

Isso muda bastante a ideia de automação contínua. Não estamos criando milhares de robôs fazendo polling da Internet em intervalos fixos. Estamos mantendo investigações em diferentes estados e decidindo dinamicamente quais merecem processamento, quanto processamento devem receber e qual deveria ser o próximo passo.

No limite, o scheduler se torna uma peça central da arquitetura. Ele não é apenas um distribuidor de recursos. É o mecanismo que transforma uma coleção de investigações persistentes em um sistema capaz de trabalhar continuamente sobre elas.

E isso nos leva a uma pergunta inevitável: se investigar custa recursos, como decidir quando vale a pena continuar investigando?

## Quanto vale a pena continuar investigando?

Existe outra questão que aparece quando levamos essa arquitetura a sério: investigar tem custos. Há chamadas a APIs, buscas, processamento, armazenamento, inferência, tempo de agentes e, em alguns casos, acesso a fontes pagas. Se o sistema puder aprofundar qualquer investigação indefinidamente, poderá produzir análises cada vez mais completas, mas também consumir recursos sem que isso necessariamente gere mais valor.

Por isso, a arquitetura não precisa apenas decidir o que investigar. Precisa decidir quanto esforço vale a pena dedicar a cada investigação.

Aqui, gosto de fazer um trocadilho com ROI. O ROI tradicional pergunta se vale a pena investir. Neste caso, podemos perguntar se vale a pena investigar. O I passa a ser de Investigation.

Não precisa ser uma fórmula rígida. Pode ser uma heurística baseada em algumas perguntas simples: qual a probabilidade de uma nova informação mudar nossa conclusão? Qual seria o impacto dessa mudança? Quanto custa obtê-la?

Se a investigação já possui evidências consistentes, a incerteza restante é pequena e uma nova busca dificilmente mudará a decisão, talvez seja melhor reduzir a frequência, entrar em monitoramento ou simplesmente encerrar aquela linha. Por outro lado, se uma única informação adicional puder alterar uma decisão importante, o próximo ciclo de investigação pode ter um valor muito maior.

Isso cria a ideia de um orçamento investigativo. A arquitetura pode concentrar capacidade onde existe maior potencial de informação e reduzir o esforço onde o retorno marginal caiu. O scheduler passa a considerar não apenas urgência e risco, mas também o valor potencial do próximo passo.

E aqui aparece uma característica interessante desse problema: provavelmente não saberemos de antemão qual é a melhor estratégia para todas as situações. Algumas decisões serão definidas inicialmente por heurísticas e depois ajustadas a partir dos resultados observados. A arquitetura pode aprender quais caminhos costumam produzir evidências relevantes, quanto custam e em que momento continuar investigando deixa de fazer sentido.

No fim, a inteligência não está apenas em descobrir mais. Está também em saber quando já descobrimos o suficiente.

## A investigação precisa lembrar e aprender

Uma investigação não deveria apenas acumular documentos. Ela precisa trabalhar com hipóteses, preservar o que já descobriu e incorporar o contexto de quem está investigando.

Suponha que uma sequência de críticas públicas contra uma empresa esteja crescendo. Uma possibilidade é que exista um problema operacional real. Outra é que o problema seja pontual e esteja sendo amplificado. Outra é que exista uma campanha coordenada. Outra é que diferentes acontecimentos estejam sendo agrupados porque parecem semelhantes.

A arquitetura não deveria escolher imediatamente uma narrativa e procurar apenas informações que a confirmem. Ela deveria manter hipóteses concorrentes e procurar evidências que ajudem a diferenciá-las.

Isso exige também separar aquilo que foi encontrado daquilo que foi inferido. Uma fonte afirma determinado fato. Isso é evidência. A conclusão de que esse fato representa um risco específico para a organização é uma inferência. Da mesma forma, uma relação entre dois acontecimentos pode ser relevante sem provar que um causou o outro.

A investigação precisa considerar ainda a independência das fontes. Dez sites repetindo a mesma notícia não representam necessariamente dez evidências. É preciso entender a origem da informação, identificar duplicações e, quando possível, buscar a fonte mais próxima do fato.

E existe uma limitação que deveria estar presente em qualquer conclusão: não encontrar informação não significa provar que determinada coisa não existe. Uma conclusão responsável seria: nenhum sinal relevante foi encontrado dentro do perímetro de fontes pesquisado. A diferença entre certeza e ausência de evidência é pequena na frase e enorme na prática.

Mas esse rigor perde valor se cada investigação começar do zero. Para existir continuidade, a arquitetura precisa preservar o que estava sendo investigado, quais hipóteses foram levantadas, quais evidências foram encontradas, quais fontes foram consideradas, quais hipóteses foram descartadas, quais dúvidas permaneceram abertas e qual foi a última conclusão. Não basta guardar o histórico de conversas com um modelo. É preciso manter o estado da investigação.

Esse estado também precisa conviver com o conhecimento específico da organização. Uma empresa pode considerar determinado fornecedor crítico enquanto outra pode considerá-lo facilmente substituível. Uma informação que representa risco relevante em um contexto pode ser irrelevante em outro. A mesma entidade pode ter relações completamente diferentes com organizações distintas.

Por isso, a arquitetura precisa construir um contexto próprio para cada organização, incorporando entidades, relacionamentos, definições, políticas, fontes preferenciais, classificações, decisões anteriores e, principalmente, correções feitas pelas pessoas.

Esse feedback humano passa a fazer parte do ciclo da investigação. Um usuário pode corrigir uma associação entre empresas, contestar uma inferência, confirmar uma relação, descartar uma hipótese ou indicar que determinada evidência é mais relevante do que o sistema considerou. Essas correções não deveriam desaparecer quando aquela investigação termina. Elas podem alterar o contexto usado nas próximas.

Isso não significa necessariamente treinar novamente o modelo. Existe uma diferença entre o modelo aprender e a arquitetura aprender. O modelo pode permanecer exatamente o mesmo enquanto a arquitetura acumula conhecimento sobre a organização, incorpora correções, identifica quais fontes são mais úteis para determinados problemas e ajusta suas heurísticas.

Nesse sentido, a arquitetura não aprende apenas sobre o mundo. Ela aprende com a organização e sobre como investigar o mundo.

## Autonomia exige governança

É tentador chamar tudo isso de investigação autônoma, mas existe uma distinção importante. A autonomia que me interessa está principalmente na condução da investigação.

O sistema pode decidir qual fonte consultar, qual hipótese aprofundar, quando criar uma subinvestigação, quando reduzir o esforço, quando procurar evidência adicional e quando retornar a uma investigação que estava parada.

Isso não significa que ele deva tomar sozinho uma decisão jurídica, encerrar uma relação comercial ou rejeitar um fornecedor. Quanto maior o impacto da decisão, maior deve ser o nível de governança exigido.

Uma arquitetura empresarial precisa permitir diferentes níveis de autonomia, desde observar e alertar até recomendar ações que dependam de aprovação humana. Em alguns contextos altamente controlados, determinadas ações poderiam eventualmente ser automatizadas. Em outros, isso seria inadequado.

Essa autonomia também cria outra exigência: a arquitetura precisa representar suas incertezas e ser capaz de explicar o caminho que percorreu.

Quanto mais a investigação influencia uma decisão, mais importante se torna conseguir reconstruir como aquela conclusão foi alcançada. Um log técnico pode dizer que um agente executou uma busca às 14h32. Isso não explica a investigação.

Seria necessário algo mais próximo de uma trilha investigativa: qual era a pergunta original, quais hipóteses existiam, quais fontes foram consultadas, quais evidências foram consideradas ou descartadas, que contexto da organização foi utilizado, quais conclusões intermediárias foram produzidas, por que determinada nova busca foi realizada e como tudo isso levou à recomendação final.

Se um usuário corrigiu uma informação, essa correção também deveria fazer parte da história. Se uma recomendação foi aceita e posteriormente se mostrou inadequada, esse resultado deveria voltar para o ciclo de aprendizado da arquitetura.

Auditabilidade, nesse contexto, não é apenas uma preocupação de compliance. É parte da própria qualidade da inteligência. Quanto mais autonomia damos ao sistema, mais precisamos conseguir entender o que ele fez, por que fez e em que evidências se baseou.

Uma investigação que não consegue explicar seu caminho é muito mais difícil de confiar.

## O mercado já possui várias dessas peças

É importante colocar essa ideia em perspectiva. Não estou propondo uma categoria tecnológica que ainda não existe. O mercado internacional já possui plataformas maduras de inteligência competitiva e de mercado, monitoramento, pesquisa assistida por IA e análise de fontes externas. Em 2026, por exemplo, a Gartner já trata Competitive and Market Intelligence Platforms como uma categoria própria de avaliação, contemplando capacidades como agregação de fontes, validação, busca e análise com IA, gestão de conhecimento e integração empresarial.

Também existem soluções que trabalham com grandes volumes de fontes, monitoramento contínuo e geração de insights sobre concorrentes, mercados e outras entidades estratégicas. No Brasil, há empresas atuando em inteligência competitiva, monitoramento, inteligência de mercado, reputação e análise de informações. Portanto, não vejo novidade em cada um desses componentes isoladamente.

A questão que me parece mais interessante é outra: como reorganizar essas capacidades em torno da investigação como unidade principal? Em vez de começar pela entidade e perguntar o que aconteceu com ela, proponho que a arquitetura comece pela pergunta e, a partir dela, descubra quais entidades, fontes, acontecimentos e relações precisam ser investigados. A busca deixa de ser uma execução isolada que termina em um relatório e passa a fazer parte de uma investigação que evolui conforme novas evidências aparecem. O relatório deixa de ser o ponto final e a decisão passa a ser um estado que pode ser revisitado sempre que novas informações puderem alterar o que sabemos.

É nessa composição que vejo espaço para uma arquitetura diferente. Não para substituir as capacidades que já existem, mas para conectá-las em um processo investigativo persistente, capaz de adaptar sua profundidade, priorizar o uso de recursos, incorporar conhecimento organizacional e aprender com o feedback.

Também vejo espaço para adaptar essa arquitetura ao contexto brasileiro, onde fontes públicas, estruturas societárias, ambiente regulatório, características de mercado e necessidades de governança podem exigir estratégias específicas de investigação. Nesse caso, a adaptação ao contexto não seria apenas uma camada de localização, mas parte da própria inteligência do sistema.

## Da coleta de informação à inteligência contínua

Quando essas ideias se juntam, a arquitetura deixa de parecer apenas um mecanismo de busca sofisticado. A informação passa a ser o combustível de uma investigação persistente, capaz de formular perguntas, acompanhar hipóteses, preservar contexto, decidir os próximos passos e retornar ao problema quando novas evidências surgirem. A IA participa desse processo, mas é a arquitetura que fornece continuidade, memória, contexto e governança.

Isso muda a pergunta central. Em vez de começar por “qual modelo vamos usar?”, talvez seja mais interessante perguntar “como vamos organizar o processo pelo qual o sistema investiga?”. Algumas respostas serão definidas inicialmente por heurísticas e outras descobertas na prática. Com o tempo, a arquitetura pode aprender quais fontes funcionam melhor para determinados problemas, quais caminhos produzem evidências relevantes e quando continuar investigando deixa de gerar valor. Não se trata apenas de fazer o modelo responder melhor, mas de fazer o sistema investigar melhor.

Se olharmos para essa evolução, primeiro construímos sistemas para coletar informação. Depois, sistemas para monitorá-la. Mais recentemente, sistemas capazes de resumir e analisar grandes volumes de conteúdo. O próximo passo pode ser uma arquitetura na qual a informação deixa de ser o produto final e passa a alimentar um processo contínuo de investigação.

Ainda existem muitas questões a definir sobre prioridade, custo, qualidade, heurísticas e autonomia. Mais do que problemas a serem resolvidos de uma única forma, essas variáveis podem fazer parte da própria configuração do produto, permitindo adaptar o comportamento da arquitetura ao contexto, ao risco e aos objetivos de cada organização. A diferença entre uma ferramenta de pesquisa e uma inteligência contínua pode estar justamente aí: não em encontrar mais informação ou produzir resumos melhores, mas em construir um sistema capaz de investigar perguntas, aprender com o que descobriu e voltar ao problema quando o mundo mudar.
