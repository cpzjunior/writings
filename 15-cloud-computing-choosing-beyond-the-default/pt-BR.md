# Cloud Computing: escolhendo além do default

_Um mapa das principais clouds, seus pontos fortes, equivalências e os trade-offs entre simplicidade, portabilidade, custo e resiliência._

**Resumo:** Eu defendo que escolher uma cloud não deveria ser uma decisão baseada em familiaridade ou no tamanho do provedor, mas nas características concretas de cada workload. As equivalências entre plataformas ajudam a orientar a comparação, mas não eliminam diferenças de custo, operação, serviços, hardware, compliance e lock-in. Single-cloud e multi-cloud também não são posições ideológicas: cada uma traz custos, benefícios e riscos que precisam ser avaliados junto às dependências reais da arquitetura. No fim, a melhor escolha é aquela que equilibra o que o workload exige com o custo de implementar, operar e eventualmente mudar essa arquitetura.

------------------------------------------------------------------------

Historicamente, sempre tive uma preferência bastante clara pela AWS. Não necessariamente porque considero a AWS a melhor cloud em qualquer cenário, mas porque foi a plataforma com a qual tive mais contato e familiaridade. Ao longo do tempo, fui me acostumando com seus serviços, sua organização, sua documentação e seu ecossistema. E existe uma consequência bastante natural nisso: quando você conhece bem uma tecnologia, ela tende a parecer a escolha mais simples para o próximo problema.

Nos últimos anos, porém, comecei a olhar para outras clouds com mais atenção. Um dos principais motivos foi bastante pragmático: GPUs. Conforme projetos de inteligência artificial passaram a exigir cada vez mais capacidade computacional, comecei a perceber que a familiaridade com uma plataforma não poderia mais ser o principal critério para decidir onde executar um workload. Preço, disponibilidade de GPUs, localização dos recursos, capacidade de expansão e até modelos de contratação passaram a ter um peso muito maior na decisão.

Isso me fez olhar novamente para um mercado que, apesar de frequentemente ser resumido à disputa entre AWS, Azure e Google Cloud, é muito mais amplo. Existem clouds especializadas, provedores regionais, plataformas com propostas deliberadamente mais simples e empresas que conseguem ser extremamente competitivas em determinados tipos de workload justamente porque não tentam oferecer tudo para todos.

O objetivo deste texto não é fazer uma comparação exaustiva entre centenas de serviços ou declarar qual é a melhor cloud. A ideia é construir um mapa suficientemente amplo para entender quem são os principais players, quais são seus pontos fortes, quais serviços possuem equivalentes entre si e, principalmente, em quais situações vale a pena sair do caminho mais óbvio.

Escolher uma cloud por familiaridade é perfeitamente razoável. Escolher uma cloud sem conhecer as alternativas, não.

## O mapa das clouds

Quando falamos em cloud computing, três nomes inevitavelmente aparecem primeiro: AWS, Microsoft Azure e Google Cloud. Elas continuam sendo as principais plataformas generalistas do mercado de public cloud, com uma abrangência que vai muito além de máquinas virtuais e armazenamento. Computação, bancos de dados, redes, containers, Kubernetes, serverless, analytics, inteligência artificial, segurança, observabilidade e uma quantidade cada vez maior de serviços gerenciados fazem parte desse ecossistema.

Existe uma razão para essas três dominarem a conversa. Elas não são apenas provedores de infraestrutura, mas plataformas completas. Uma aplicação pode utilizar computação, armazenamento, banco de dados, filas, identidade, observabilidade, gerenciamento de segredos, CDN e serviços de inteligência artificial do mesmo provedor, todos integrados entre si. Essa integração é uma das grandes vantagens das hyperscalers e também um dos fatores que tornam uma eventual migração mais complexa.

Mas o mercado de cloud não é uma hierarquia simples. Existem provedores com propostas diferentes e, dependendo do workload, um provedor que parece pequeno quando comparado a uma hyperscaler pode ser uma opção muito mais interessante.

Oracle Cloud Infrastructure, IBM Cloud, Alibaba Cloud e Tencent Cloud são exemplos de provedores que possuem posições particularmente fortes em determinados mercados e ecossistemas. A OCI tem uma relação natural com ambientes que dependem fortemente de Oracle. A IBM mantém uma presença importante em grandes organizações e no ecossistema Red Hat. Alibaba e Tencent possuem uma relevância muito maior quando consideramos a China e outros mercados asiáticos. Nesses casos, a pergunta não é necessariamente qual provedor oferece mais serviços, mas qual possui maior aderência ao problema que precisa ser resolvido.

Existe ainda um grupo de provedores que adota uma proposta deliberadamente mais simples. DigitalOcean, Hetzner, OVHcloud, Scaleway e Akamai, através da Linode, podem ser interessantes quando o objetivo é obter computação, armazenamento e rede sem necessariamente depender da enorme quantidade de serviços gerenciados oferecidos pelas hyperscalers. Para determinados workloads, essa simplicidade pode significar menor complexidade operacional e custos mais previsíveis.

A inteligência artificial, porém, está alterando esse cenário. O crescimento da demanda por GPUs criou um mercado em que disponibilidade e custo de hardware podem ser mais importantes do que a quantidade de serviços oferecidos pela plataforma. Uma aplicação de IA que precisa de centenas de GPUs não necessariamente se beneficia de estar no provedor que oferece o maior catálogo de serviços. Nesse cenário, preço por GPU, disponibilidade, arquitetura dos aceleradores, interconexão entre máquinas, capacidade de escalar e localização dos recursos podem ser os fatores determinantes.

Isso abriu espaço para provedores especializados. A CoreWeave é um dos exemplos mais conhecidos, tendo construído sua plataforma em torno de workloads de GPU e inteligência artificial. Existem também outros provedores especializados em GPU e computação de alto desempenho que podem ser muito competitivos para esse tipo de carga, mesmo sem oferecer uma plataforma generalista comparável às hyperscalers.

Ao mesmo tempo, as próprias hyperscalers estão investindo pesadamente em hardware especializado, modelos fundacionais, serviços gerenciados de IA e integração desses recursos com o restante de suas plataformas. Isso cria uma competição diferente daquela que existia no mercado tradicional de cloud. A vantagem pode estar tanto na infraestrutura quanto no ecossistema construído em torno dela.

Na prática, isso significa que não existe um único perfil de cloud que seja adequado para todos os workloads. As plataformas generalistas continuam sendo extremamente relevantes, mas provedores especializados podem ser mais competitivos em determinadas situações. Uma empresa pode ser uma excelente escolha para infraestrutura tradicional e uma escolha ruim para treinamento de modelos. Outra pode ser pouco interessante como plataforma principal, mas extremamente competitiva para um workload específico de GPU.

Esse é justamente um dos motivos pelos quais vale olhar além do default. A cloud escolhida para uma aplicação não precisa necessariamente ser a mesma escolhida para todos os workloads da organização. Um provedor que historicamente parece pequeno ou secundário pode se tornar uma alternativa relevante quando mudamos a pergunta de “qual é a melhor cloud?” para “qual é a melhor infraestrutura para este workload?”.

No fim, AWS, Azure e Google Cloud continuam sendo as principais plataformas generalistas, mas tamanho e quantidade de serviços não são os únicos critérios relevantes. O mercado está se tornando mais especializado, e a inteligência artificial está acelerando esse processo. Conhecer esse cenário significa entender onde as grandes plataformas são mais fortes, onde os provedores menores conseguem competir e em quais situações faz sentido considerar alternativas que normalmente nem apareceriam na primeira pesquisa.

## Equivalência não significa igualdade

Uma das primeiras coisas que alguém percebe ao estudar diferentes clouds é que os grandes provedores possuem equivalentes para boa parte dos serviços fundamentais. No nível de computação, podemos pensar em EC2 na AWS, Virtual Machines no Azure e Compute Engine no Google Cloud. Para object storage, temos S3, Blob Storage e Cloud Storage. Para redes virtuais, VPC na AWS, Virtual Network no Azure e VPC no Google Cloud. Para Kubernetes gerenciado, EKS, AKS e GKE. Para container registry, ECR, Azure Container Registry e Artifact Registry. Para balanceamento de carga, Elastic Load Balancing, Azure Load Balancer e Cloud Load Balancing. Para CDN, CloudFront, Azure Front Door e Cloud CDN. Os nomes mudam, mas os conceitos fundamentais são bastante semelhantes.

O mesmo acontece com os serviços de dados. Para bancos relacionais gerenciados, a AWS possui o RDS, enquanto Azure e Google Cloud oferecem famílias de serviços como Azure Database for PostgreSQL e MySQL e Cloud SQL. No mundo NoSQL, temos DynamoDB, Cosmos DB e Firestore. Para data warehouses, Redshift, Synapse e BigQuery. Para armazenamento de arquivos, EFS, Azure Files e Filestore. Para mensageria, podemos encontrar SQS, Azure Service Bus e Pub/Sub. Até serviços de identidade, gerenciamento de secrets e observabilidade possuem equivalentes claros: IAM, Entra ID e Cloud IAM; Secrets Manager, Key Vault e Secret Manager; CloudWatch, Azure Monitor e Cloud Monitoring.

Essa correspondência também aparece nas arquiteturas mais modernas. Lambda, Azure Functions e Cloud Run functions atendem a modelos de execução serverless, enquanto Fargate, Azure Container Apps e Cloud Run permitem executar containers sem precisar administrar diretamente as máquinas virtuais. Para infraestrutura como código, temos CloudFormation na AWS e ARM Templates e Bicep no ecossistema Microsoft, enquanto ferramentas independentes como Terraform permitem trabalhar com diferentes provedores utilizando uma abordagem comum.

Até inteligência artificial já possui um conjunto relativamente claro de equivalências. SageMaker, Azure Machine Learning e Vertex AI oferecem plataformas para desenvolvimento e operação de workloads de machine learning. Bedrock, Azure AI Foundry e Vertex AI oferecem diferentes caminhos para consumir modelos e construir aplicações de inteligência artificial. No entanto, aqui as diferenças começam a ficar particularmente importantes, porque os modelos disponíveis, aceleradores, APIs, ferramentas de treinamento, serviços gerenciados e integrações com o restante da plataforma variam bastante entre os provedores.

Esse paralelismo é útil porque permite construir um vocabulário comum para comparar plataformas. Quem conhece AWS consegue rapidamente identificar onde procurar conceitos semelhantes no Azure ou no Google Cloud. Isso reduz bastante a barreira inicial para aprender uma nova plataforma e também torna possível transportar parte do conhecimento arquitetural de uma cloud para outra.

Mas existe uma armadilha nessa comparação. O fato de dois serviços resolverem problemas semelhantes não significa que sejam equivalentes em comportamento, arquitetura ou experiência operacional. Um object storage continua sendo object storage, mas os mecanismos de controle de acesso, integração com outros serviços, consistência, quotas, preços, replicação e políticas de ciclo de vida podem ser diferentes. O mesmo vale para bancos de dados, serviços de mensagens, Kubernetes e praticamente qualquer outra categoria.

As diferenças ficam ainda maiores quando subimos o nível de abstração. Um banco relacional gerenciado pode parecer simplesmente um banco relacional gerenciado, mas as engines disponíveis, extensões suportadas, mecanismos de replicação, opções de alta disponibilidade, backups, integração com analytics e ferramentas de migração podem mudar completamente a decisão. Da mesma forma, duas plataformas podem oferecer Kubernetes gerenciado, mas possuir diferenças significativas na integração com rede, identidade, storage, observabilidade e serviços proprietários.

Existe ainda uma diferença mais importante: cada cloud possui serviços que não possuem um equivalente direto nas demais. E é justamente nesses serviços que muitas vezes está uma parte significativa do valor de uma plataforma. Se todas as clouds oferecem máquinas virtuais, object storage e Kubernetes, esses recursos são relativamente fáceis de comparar. Já serviços como DynamoDB, BigQuery, Cosmos DB ou Cloud Run representam decisões arquiteturais mais específicas e podem criar dependências muito maiores em relação ao provedor.

A inteligência artificial torna esse ponto ainda mais evidente. As grandes clouds oferecem serviços semelhantes para treinamento, inferência e consumo de modelos, mas a combinação entre modelos próprios e de terceiros, GPUs e outros aceleradores, APIs, ferramentas de desenvolvimento, data pipelines, bancos vetoriais e serviços gerenciados pode ser bastante diferente. Além disso, nem sempre determinado modelo ou hardware está disponível na mesma região, pelo mesmo preço ou com a mesma capacidade em todos os provedores.

Por isso, uma matriz de equivalências é um excelente ponto de partida para comparar clouds, mas não deveria ser utilizada como uma prova de que elas são intercambiáveis. Ela ajuda a responder “onde encontro algo parecido com o que já conheço?”, mas não necessariamente “qual plataforma é melhor para o que estou tentando construir?”.

Conhecer as equivalências reduz o custo de aprender uma nova cloud. Conhecer as diferenças é o que permite escolher entre elas.

## Single cloud, multi-cloud e o custo da simplicidade

Existe um argumento bastante forte a favor de escolher uma única cloud: simplicidade. Operar uma infraestrutura inteira dentro de uma mesma plataforma reduz a quantidade de conceitos que precisam ser dominados, as integrações que precisam ser mantidas e as diferenças de comportamento que precisam ser consideradas. IAM, networking, observabilidade, billing, políticas de segurança, deployment e troubleshooting podem seguir um conjunto relativamente consistente de padrões. A equipe também consegue concentrar conhecimento, automação e processos operacionais em uma única plataforma.

Para uma equipe pequena ou para uma organização que não possui uma necessidade concreta de multi-cloud, essa simplicidade tem um valor enorme. Não é apenas uma questão de produtividade. Cada tecnologia adicional exige conhecimento, processos, monitoramento, automação e capacidade de troubleshooting. Uma segunda cloud significa aprender uma segunda forma de fazer muitas das mesmas coisas, além de lidar com as diferenças entre elas.

Ferramentas como Terraform reduzem bastante esse problema. É possível declarar infraestrutura de diferentes provedores utilizando uma mesma linguagem e, em muitos casos, reutilizar módulos, pipelines e práticas operacionais. Isso torna uma estratégia multi-cloud muito mais viável do que seria se cada provedor exigisse uma stack completamente independente. Mas Terraform não transforma AWS, Azure e Google Cloud em plataformas intercambiáveis. Ele abstrai a forma de declarar infraestrutura, não necessariamente a arquitetura que está sendo declarada.

Um recurso criado em Terraform continua sendo um recurso específico de determinado provedor. Uma VPC continua tendo as características da AWS, uma Virtual Network continua tendo as características do Azure e uma VPC do Google Cloud possui suas próprias particularidades. O código pode até parecer semelhante, mas o comportamento dos recursos, suas limitações e suas integrações continuam pertencendo à plataforma.

Esse problema fica particularmente evidente quando surgem serviços novos. Os provedores de cloud lançam constantemente produtos que exploram características específicas de suas próprias plataformas. Existe naturalmente um intervalo entre o lançamento de um serviço e a existência de suporte maduro para ele nas ferramentas de infraestrutura como código. Mesmo quando o suporte existe, nem sempre todos os recursos do serviço são expostos da mesma maneira.

Existe ainda uma questão mais sutil. Quanto mais uma arquitetura tenta ser portável, maior tende a ser a pressão para utilizar apenas recursos que possuam equivalentes razoavelmente próximos em todos os provedores. Isso pode ser uma decisão consciente e perfeitamente válida, mas significa abrir mão de parte do diferencial oferecido por cada plataforma.

Se você decide utilizar apenas serviços que podem ser encontrados em AWS, Azure e Google Cloud, aumenta a portabilidade da aplicação. Mas também pode deixar de utilizar serviços que tornariam essa aplicação mais simples, mais barata ou mais eficiente dentro de uma determinada cloud.

Esse é um dos grandes trade-offs da portabilidade. Ela não é gratuita. É perfeitamente possível construir uma aplicação que rode em AWS, Azure e Google Cloud. A questão é quanto valor você está deixando na mesa para conseguir fazer isso.

Em alguns casos, a resposta será “nenhum valor relevante”. Se a aplicação utiliza apenas containers, PostgreSQL, object storage e alguns componentes relativamente padronizados, a portabilidade pode ser uma propriedade bastante razoável. Em outros, a resposta pode ser muito diferente. Uma aplicação que depende profundamente de serviços proprietários de uma cloud pode obter ganhos enormes em simplicidade, performance ou custo justamente por aceitar um determinado nível de lock-in.

A discussão sobre utilizar uma ou várias clouds costuma ser apresentada como uma escolha entre simplicidade e resiliência. Na prática, é um pouco mais complicada. Uma única cloud pode concentrar riscos. Se uma falha significativa atingir o provedor, parte importante da infraestrutura pode ficar indisponível simultaneamente. É possível reduzir esse risco utilizando múltiplas regiões, zonas de disponibilidade e mecanismos adequados de disaster recovery, mas existe um limite para o quanto podemos nos proteger contra uma falha que ultrapasse a fronteira de uma região ou até mesmo da própria plataforma.

Por outro lado, distribuir workloads entre diferentes provedores aumenta a quantidade de componentes e integrações que precisam ser operados. Passamos a lidar com diferentes modelos de rede, identidade, segurança, observabilidade, deployment e gerenciamento de custos. A arquitetura pode ganhar independência em algumas dimensões e perder simplicidade em outras.

Multi-cloud, portanto, não significa automaticamente maior disponibilidade. É possível ter uma aplicação distribuída entre AWS e Azure e ainda possuir um ponto único de falha. Ele pode estar no DNS, no provedor de identidade, na CDN, na conectividade, na observabilidade, em um SaaS utilizado pelas duas arquiteturas ou em qualquer outra dependência compartilhada.

Esse é um ponto que considero particularmente importante: diversidade de fornecedores não é necessariamente diversidade de dependências. Imagine uma aplicação cujo backend está distribuído entre AWS e Azure, mas que utiliza o mesmo provedor de DNS, a mesma CDN e o mesmo serviço de identidade. Do ponto de vista do compute, existem dois provedores. Do ponto de vista do caminho crítico da aplicação, talvez não existam. Se uma dessas dependências compartilhadas falhar, ter duas clouds pode não fazer nenhuma diferença.

O caso da Cloudflare é um bom exemplo para ilustrar esse problema. Em junho de 2022, uma alteração de configuração na rede da empresa provocou uma indisponibilidade que afetou diversos serviços que dependiam de sua infraestrutura. O ponto interessante para uma arquitetura multi-cloud não é simplesmente que um fornecedor ficou indisponível, mas que uma dependência localizada em uma camada transversal pode afetar aplicações independentemente de onde seu compute esteja hospedado.

Esse tipo de dependência é fácil de ignorar porque normalmente não aparece quando olhamos apenas para o diagrama principal da infraestrutura. Podemos desenhar AWS de um lado e Azure do outro e concluir que temos redundância. Mas, se as duas dependem do mesmo DNS, da mesma CDN, do mesmo provedor de identidade ou de qualquer outro componente crítico, existe uma dependência comum escondida entre elas.

Isso também ajuda a colocar o conceito de resiliência em uma perspectiva mais realista. Multi-cloud pode reduzir determinados riscos, mas não elimina risco. Em alguns casos, ele simplesmente desloca o ponto em que o risco aparece.

A pergunta, portanto, não deveria ser apenas se a aplicação está distribuída entre mais de uma cloud, mas se as suas dependências críticas também estão. Para avaliar a resiliência de uma arquitetura, é preciso olhar para toda a cadeia de dependências, incluindo DNS, identidade, CDN, conectividade, observabilidade e serviços externos, e não apenas para onde os containers ou máquinas virtuais estão executando.

Existe ainda outro aspecto importante: multi-cloud pode ser adotado por motivos que não têm relação direta com disponibilidade. Negociação comercial, requisitos regulatórios, localização de dados, disponibilidade de determinados serviços, capacidade de GPU e diferenças de custo podem ser razões suficientes para utilizar mais de um provedor.

Da mesma forma, uma estratégia single-cloud pode ser perfeitamente defensável quando a simplicidade operacional tem mais valor do que a independência adicional. Uma única cloud, distribuída adequadamente entre regiões e zonas, pode oferecer um nível de resiliência suficiente para muitos workloads.

Single-cloud e multi-cloud não deveriam ser tratados como posições ideológicas. São estratégias arquiteturais diferentes, com custos, benefícios e riscos diferentes. A escolha deveria partir do risco que queremos reduzir, do workload que estamos tentando executar e da complexidade que estamos dispostos a assumir para atingir esse objetivo.

## O diferencial das clouds menores

É justamente aqui que vale ampliar o mapa. As hyperscalers possuem uma vantagem evidente quando precisamos de uma plataforma extremamente completa, com dezenas ou centenas de serviços integrados. Mas essa abrangência também pode ser irrelevante para determinados workloads.

Uma aplicação que precisa essencialmente de máquinas virtuais, armazenamento, rede e talvez Kubernetes não necessariamente precisa de toda a complexidade oferecida por AWS, Azure ou Google Cloud. Nesse cenário, provedores como Hetzner, OVHcloud, DigitalOcean, Scaleway ou Akamai podem entrar na análise. A proposta dessas empresas não é necessariamente competir com as hyperscalers em quantidade de serviços, mas oferecer determinados recursos de infraestrutura de maneira mais simples e, em alguns casos, com uma estrutura de custos mais competitiva.

Existe ainda uma categoria diferente de alternativa: plataformas que abstraem ainda mais a infraestrutura. Heroku, Render e Railway são exemplos de plataformas em que o desenvolvedor pode se concentrar na aplicação sem precisar administrar diretamente boa parte dos componentes de infraestrutura que existiriam em uma abordagem tradicional. Para determinados projetos, essa abstração pode valer mais do que o acesso a um catálogo gigantesco de serviços.

Essa diferença pode ser bastante relevante. Se uma aplicação utiliza apenas uma fração dos serviços disponíveis em uma hyperscaler, existe um ponto em que a capacidade adicional deixa de representar valor e passa a representar apenas complexidade. Para determinados workloads, ter uma máquina virtual previsível, uma rede simples e armazenamento adequado pode ser mais importante do que ter centenas de serviços gerenciados disponíveis. Para outros, pode fazer sentido subir ainda mais o nível de abstração e utilizar uma plataforma que esconda boa parte dessa infraestrutura.

O mesmo raciocínio vale para workloads específicos. Se o principal recurso necessário é GPU, a pergunta pode deixar de ser “qual é a minha cloud padrão?” e passar a ser “quem oferece a GPU que preciso, na quantidade que preciso, pelo custo que consigo pagar?”. Nesse cenário, disponibilidade de hardware, preço por hora, capacidade de expansão, localização e características da infraestrutura podem ser muito mais relevantes do que a quantidade de serviços disponíveis na plataforma.

É nesse tipo de situação que uma preferência histórica por determinada cloud começa a perder importância. A familiaridade continua tendo valor, mas passa a competir com critérios objetivos do workload. Uma plataforma que eu nunca utilizei pode ser uma escolha melhor para determinado projeto simplesmente porque oferece o recurso necessário em condições significativamente melhores.

Existe ainda uma vantagem importante: uma cloud menor ou uma plataforma especializada não precisa ser uma substituta completa da cloud principal. Ela pode simplesmente ser uma peça da arquitetura. Um workload específico pode fazer mais sentido em outro provedor enquanto o restante da organização permanece em uma única plataforma.

Isso permite uma abordagem intermediária entre single-cloud e multi-cloud. Em vez de tentar construir uma aplicação completamente portável entre várias plataformas, podemos aceitar que a maior parte da infraestrutura esteja em uma cloud principal e utilizar outros provedores apenas quando existir uma vantagem concreta.

Essa abordagem também muda a forma como pensamos sobre multi-cloud. Não é necessário distribuir toda a aplicação entre vários provedores para obter algum benefício da diversidade. Podemos ter uma cloud principal e, ao mesmo tempo, escolher deliberadamente outro fornecedor para workloads em que ele seja mais competitivo.

O diferencial de uma cloud menor não precisa ser oferecer mais recursos do que uma hyperscaler. Pode ser justamente oferecer menos, mas oferecer aquilo que o workload realmente precisa de uma maneira mais simples, mais barata ou mais especializada.

## O problema do lock-in

Toda discussão sobre clouds inevitavelmente chega ao lock-in. Existe uma percepção de que utilizar apenas serviços básicos, como máquinas virtuais, containers e storage, torna uma arquitetura mais portável. Em parte isso é verdade. Quanto mais específica é uma dependência de um provedor, maior tende a ser o custo para substituí-la. Uma aplicação baseada em containers, PostgreSQL e object storage tende a ter mais opções de migração do que outra profundamente dependente de dezenas de serviços proprietários.

Mas lock-in não é apenas uma questão tecnológica. Existe também o lock-in operacional. Uma organização pode construir processos, automações, conhecimento interno e ferramentas de observabilidade profundamente integrados a uma determinada plataforma. Mesmo que tecnicamente seja possível migrar uma aplicação, o custo de treinar equipes, reconstruir pipelines, adaptar processos e operar uma nova infraestrutura pode tornar a migração muito mais difícil do que o diagrama arquitetural sugere.

Existe ainda o lock-in econômico. Dados são um bom exemplo. Migrar máquinas virtuais pode ser relativamente simples, mas mover grandes volumes de dados entre provedores pode envolver custos de transferência, tempo e uma janela operacional significativa. Uma arquitetura pode ser tecnicamente portável e, ainda assim, economicamente muito cara de mover.

Por isso, evitar qualquer lock-in também tem um custo. Se uma cloud oferece um serviço gerenciado que reduz drasticamente a complexidade operacional de uma aplicação, evitar esse serviço apenas para manter uma possibilidade futura de migração pode significar assumir hoje um custo real para evitar um custo hipotético. Em alguns casos, aceitar deliberadamente uma dependência do provedor é uma decisão arquitetural perfeitamente racional.

O objetivo, portanto, não deveria ser eliminar completamente o lock-in. Isso provavelmente é impossível. O objetivo deveria ser entendê-lo. Existem dependências que são estratégicas e outras que são facilmente substituíveis. Existem serviços cujo custo de migração seria gigantesco e outros que poderiam ser substituídos em semanas. Existem componentes que justificam uma dependência profunda de um provedor e outros em que a escolha pode ser baseada simplesmente em preço, disponibilidade ou conveniência.

Também é importante entender que nem todo lock-in é necessariamente ruim. Se um serviço proprietário oferece uma vantagem significativa de custo, performance, disponibilidade ou produtividade, a dependência pode ser um preço aceitável pelo benefício obtido. O importante é que essa dependência seja uma decisão consciente, e não uma consequência que só descobrimos quando precisamos migrar.

Uma forma útil de pensar sobre isso é perguntar, para cada dependência importante, quanto esforço seria necessário para substituí-la, quanto tempo levaria, quanto custaria e quais partes da arquitetura seriam afetadas. Essa análise permite entender onde o lock-in existe, por que ele foi assumido e qual seria o custo para removê-lo. O objetivo não é evitar lock-in a qualquer custo, mas garantir que as dependências da arquitetura sejam decisões conscientes.

## O custo de implementação

Existe outro custo que costuma desaparecer das comparações entre clouds: o custo de implementação e operação da própria arquitetura. Duas clouds podem oferecer recursos tecnicamente equivalentes e preços semelhantes, mas exigir níveis completamente diferentes de esforço para colocar uma aplicação em produção. Uma plataforma pode ter integrações prontas para determinado serviço, enquanto outra exige que a equipe construa e mantenha parte dessa integração. Uma pode oferecer um serviço gerenciado que elimina dezenas de componentes, enquanto outra exige que esses componentes sejam operados diretamente.

Esse custo não aparece apenas em arquiteturas multi-cloud. Uma arquitetura excessivamente sofisticada dentro de uma única cloud também pode exigir mais automação, conhecimento e esforço operacional do que uma solução mais simples. A diferença é que, quando adicionamos múltiplos provedores, essa complexidade tende a aumentar porque precisamos lidar também com diferentes modelos de rede, identidade, segurança, observabilidade e deployment.

Quanto mais diferenças precisamos esconder atrás de abstrações, maior tende a ser a quantidade de código, infraestrutura e automação necessária. Terraform ajuda bastante na camada de provisionamento, mas não elimina as diferenças entre as plataformas. Em algum momento, alguém precisa lidar com essas diferenças.

O mesmo vale para observabilidade, segurança e operação. Uma arquitetura single-cloud pode aproveitar as integrações nativas do provedor para centralizar logs, métricas, identidade, políticas e alertas. Em uma arquitetura multi-cloud, podemos precisar criar uma camada adicional para unificar essas informações. Isso pode ser uma decisão correta, mas essa camada também precisa ser construída, monitorada e mantida.

Existe ainda o custo de conhecimento. Uma equipe que opera AWS e Azure precisa conhecer as particularidades das duas plataformas. Isso não significa necessariamente ter o dobro do custo, mas significa aumentar a superfície de conhecimento necessária para operar a infraestrutura. O mesmo vale para processos de troubleshooting, incident response, segurança e gestão de mudanças.

Esse custo também aparece quando chega a hora de mudar a arquitetura. Uma aplicação pode ser relativamente barata de executar em uma determinada configuração e exigir um esforço significativo para ser adaptada a outra. A mudança pode envolver não apenas máquinas e containers, mas também dados, configurações, identidades, redes, pipelines, observabilidade, integrações e processos operacionais. Em muitos casos, o trabalho está justamente nas dependências que não aparecem no diagrama principal da aplicação.

Por isso, o custo de uma arquitetura deveria ser analisado em pelo menos três momentos: quanto custa implementar, quanto custa operar e quanto custa mudar. O preço mensal da infraestrutura é apenas uma dessas dimensões.

Isso também ajuda a explicar por que nem sempre vale a pena escolher a opção tecnicamente mais barata. Se uma alternativa reduz o custo de infraestrutura, mas exige muito mais engenharia para ser implementada e operada, a economia pode desaparecer rapidamente. Da mesma forma, pagar mais por um serviço gerenciado pode ser racional se o custo evitado de operação for maior do que a diferença de preço.

## Compliance e regulação

Existe um critério que pode eliminar uma cloud da lista de opções antes mesmo de começarmos a comparar preço ou funcionalidades: compliance. Dependendo do setor, do país e do tipo de dado processado, uma organização pode estar sujeita a requisitos específicos de segurança, privacidade, residência de dados, auditoria e continuidade de negócio. Bancos, seguradoras, empresas de saúde e órgãos públicos, por exemplo, normalmente possuem restrições muito diferentes de uma aplicação pessoal ou de um produto SaaS sem dados regulados.

As grandes clouds investem bastante nessa área e possuem uma quantidade enorme de certificações, padrões e mecanismos de controle. Também oferecem regiões em diferentes países, recursos de criptografia, gerenciamento de chaves, logs de auditoria, controles de identidade e ferramentas voltadas para requisitos regulatórios específicos. Provedores menores também podem atender a determinados requisitos, mas não necessariamente terão a mesma cobertura geográfica ou o mesmo conjunto de certificações.

Isso pode mudar completamente a escolha. Uma cloud pode ser tecnicamente excelente e competitiva em preço, mas deixar de ser uma opção se não possuir uma região adequada, determinada certificação ou os controles necessários para o workload.

Também é importante separar a certificação do provedor da conformidade da aplicação. O fato de uma cloud possuir uma determinada certificação não significa que qualquer aplicação executada nela esteja automaticamente em conformidade. A responsabilidade costuma ser compartilhada entre o provedor e o cliente, e a arquitetura precisa utilizar corretamente os mecanismos de segurança, controle de acesso, criptografia, logging e retenção de dados disponíveis.

A localização também merece atenção. “A cloud está disponível no país” não significa necessariamente que todos os dados e serviços utilizados pela aplicação permanecerão naquele país. Backups, logs, serviços gerenciados, suporte e integrações podem possuir características diferentes. Em ambientes regulados, é preciso entender onde os dados realmente são armazenados, processados e replicados.

Esse é um ponto em que as clouds também podem ter vantagens diferentes. Uma hyperscaler pode oferecer uma quantidade enorme de regiões e controles, enquanto um provedor regional pode ter uma vantagem justamente por manter sua infraestrutura concentrada em determinadas jurisdições. Para alguns workloads, essa característica pode ser mais importante do que a quantidade de serviços disponíveis.

Por isso, compliance não deveria aparecer apenas no final do processo de escolha. Ele pode funcionar como um filtro inicial. Antes de comparar preço, performance ou quantidade de serviços, pode ser necessário perguntar quais provedores são efetivamente elegíveis para aquele workload.

Em ambientes regulados, a primeira pergunta não é qual cloud oferece mais recursos, mas quais clouds podem atender aos requisitos do workload. A partir desse conjunto de opções, preço, performance, simplicidade, portabilidade e demais critérios podem entrar na decisão.

## Descontos, parcerias e free tiers

Comparar o preço das clouds também é mais complicado do que olhar para a tabela pública de preços. O valor efetivamente pago por uma organização pode ser bastante diferente dependendo do volume contratado, do compromisso assumido e dos programas comerciais disponíveis.

As grandes clouds possuem diferentes mecanismos para reduzir o custo de workloads que permanecem por determinado período ou atingem determinado volume. Reserved Instances, Savings Plans, committed use discounts e contratos empresariais são exemplos de mecanismos que podem alterar significativamente o preço final. Em alguns casos, a diferença entre o preço de tabela e o preço efetivamente negociado é grande o suficiente para mudar completamente uma comparação superficial entre provedores.

Existem também créditos e programas específicos para startups, projetos de pesquisa, educação e empresas que estão migrando ou expandindo seus workloads. Para uma empresa em estágio inicial, por exemplo, créditos podem reduzir significativamente o custo durante os primeiros meses. Mas esse tipo de benefício precisa ser analisado com cuidado. Um crédito inicial pode reduzir drasticamente o custo de entrada sem necessariamente tornar a plataforma mais barata no longo prazo.

Parcerias também podem pesar nessa decisão. Uma organização pode já possuir contratos, competências, suporte especializado ou benefícios comerciais associados a determinado fornecedor. Nesse caso, mudar de cloud significa abrir mão não apenas de uma infraestrutura, mas de parte desse ecossistema comercial. Da mesma forma, uma empresa pode ter uma parceria com determinado provedor que torne uma alternativa menos óbvia muito mais competitiva.

Os free tiers entram nessa mesma lógica. Eles são excelentes para experimentar uma plataforma, aprender seus serviços ou colocar no ar projetos pequenos sem custo significativo. Também podem ser uma forma interessante de comparar a experiência entre provedores antes de assumir um compromisso maior. Mas é importante separar o custo de experimentar uma cloud do custo de operar nela em produção.

Uma aplicação que cabe confortavelmente no free tier pode se tornar bastante cara quando cresce. O mesmo vale para créditos promocionais. Eles são excelentes para reduzir o custo de entrada, mas não necessariamente representam o custo recorrente da arquitetura.

Existe ainda uma armadilha específica quando comparamos clouds apenas pelo preço de um recurso isolado. Uma GPU pode ser mais barata em determinado provedor, mas o custo total do workload depende também de armazenamento, transferência de dados, rede, balanceamento, observabilidade e dos demais serviços necessários para colocar aquela GPU para trabalhar. O mesmo vale para qualquer outro recurso.

Por isso, quando falamos em custo de cloud, o número mais importante não é necessariamente o preço de uma instância ou de uma GPU. É o custo total para executar aquele workload.

Isso é especialmente importante porque as condições comerciais podem mudar a análise de forma significativa. Uma cloud pode parecer mais cara no preço de tabela e se tornar competitiva depois de descontos, créditos e contratos empresariais. Da mesma forma, uma oferta muito atraente durante os primeiros meses pode deixar de fazer sentido quando os benefícios promocionais terminarem.

O preço de tabela é, portanto, apenas o ponto de partida. O custo real depende do que será utilizado, de quanto será utilizado, por quanto tempo, de quais serviços adicionais serão necessários e das condições comerciais disponíveis para aquele contexto.

## Então, qual caminho escolher?

Não existe uma resposta universal. A escolha deveria começar pelo workload e pelos requisitos, não pelo nome da cloud. Quais serviços realmente são necessários? Onde os dados precisam estar? Qual é o custo total, incluindo transferência de dados? Qual é a disponibilidade necessária? Quais competências a equipe já possui? Quanto lock-in é aceitável? Existem requisitos de compliance ou regulação? Existe algum serviço específico que justifique a escolha de determinado provedor? E, principalmente, quanto custa implementar, operar e eventualmente migrar essa arquitetura?

Essa última pergunta é particularmente importante porque o preço da infraestrutura é apenas uma parte do custo. Uma cloud pode oferecer máquinas virtuais ou GPUs mais baratas e ainda assim ser uma opção mais cara quando consideramos o esforço de implementação, as integrações, a operação e a necessidade de desenvolver componentes que outra plataforma já oferece como serviço gerenciado. Da mesma forma, uma arquitetura mais portável pode exigir mais engenharia para ser construída e mantida.

O mesmo raciocínio vale para a migração. Uma escolha que parece barata hoje pode criar uma dependência cujo custo de substituição será muito maior no futuro. Por outro lado, evitar qualquer dependência específica para preservar uma possibilidade de migração também significa pagar por essa portabilidade desde o primeiro dia.

Por isso, comparar clouds apenas por preço ou quantidade de funcionalidades dificilmente é suficiente. O que importa é o custo total da decisão e o valor que cada plataforma entrega para aquele workload. Descontos, créditos, free tiers e contratos comerciais também entram nessa conta, mas precisam ser analisados junto com o custo recorrente e não como substitutos dele.

A melhor arquitetura não é necessariamente aquela que utiliza mais clouds, assim como a melhor cloud não é necessariamente aquela que oferece mais serviços. Uma única cloud pode ser a melhor escolha quando simplicidade e integração são prioritárias. Duas ou mais podem fazer sentido quando existe uma razão concreta para distribuir workloads entre fornecedores. Uma cloud menor pode ser mais adequada para um workload específico. E uma solução que parece tecnicamente mais sofisticada pode ser simplesmente mais complexa sem entregar um benefício proporcional.

No final, escolher uma cloud é escolher um conjunto de compromissos. Simplicidade, custo, portabilidade, lock-in, disponibilidade, resiliência, compliance e complexidade operacional fazem parte da mesma decisão. Não existe uma escolha sem trade-offs. Existe apenas a possibilidade de entender quais trade-offs estamos assumindo e por que eles fazem sentido para aquele contexto.

Conhecer as alternativas não significa utilizar todas elas. Significa saber quando a escolha padrão faz sentido, quando vale a pena procurar outra opção e qual será o impacto dessa decisão no presente e no futuro. No meu caso, conhecer melhor as alternativas não fez com que eu deixasse de preferir a AWS. Apenas fez com que ela deixasse de ser a resposta automática.
