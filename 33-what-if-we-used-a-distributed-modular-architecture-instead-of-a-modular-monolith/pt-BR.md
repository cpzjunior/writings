# E se usarmos uma arquitetura modular distribuída no lugar do monólito modular?

_Uma ideia de arquitetura para startups em estágio inicial que precisam crescer sem pagar desproporcionalmente por infraestrutura ou pela complexidade dos microservices._

**Resumo:** Eu proponho uma arquitetura modular distribuída que separa a unidade de desenvolvimento da unidade de processamento: o módulo continua organizando código, regras e testes, enquanto cada use case pode adotar sua própria estratégia de execução e escala quando houver uma necessidade concreta. Com isso, startups podem começar com uma estrutura simples, distribuindo apenas os workloads que realmente exigirem mais capacidade, sem assumir antecipadamente a complexidade dos microservices. A ideia não é substituir o monólito modular ou os microservices, mas criar uma alternativa de partida que permita adiar decisões de infraestrutura e introduzir complexidade de forma gradual.

------------------------------------------------------------------------

Quando uma startup está começando, arquitetura de software costuma ser uma questão de equilíbrio. A equipe é pequena, o produto ainda está descobrindo o próprio mercado, o volume de usuários é incerto e o orçamento é limitado. Ao mesmo tempo, algumas decisões tomadas no início podem permanecer por anos e se tornar difíceis ou caras de mudar depois. Nesse contexto, uma arquitetura precisa fazer mais do que organizar o código: ela precisa permitir que a empresa adie decisões caras até que exista uma razão concreta para tomá-las.

Há alguns anos, fui presidente voluntário da Se Doar, uma ONG que mantinha uma plataforma para conectar organizações sociais a pessoas e empresas interessadas em fazer doações ou oferecer trabalho voluntário. Além da presidência, eu cuidava da plataforma junto com outros voluntários. Era um contexto em que essas restrições ficavam particularmente evidentes. Tínhamos poucos recursos, uma equipe pequena e pouco espaço para manter infraestrutura ociosa. Cada decisão técnica precisava ser avaliada também pelo seu impacto operacional e financeiro.

A primeira versão da plataforma utilizava um monólito modular. Naquele momento, fazia sentido. A aplicação era relativamente pequena, os módulos ajudavam a separar responsabilidades e a infraestrutura permanecia simples de operar. Conforme o sistema evoluiu, porém, ficou evidente que as diferentes partes da aplicação não tinham necessariamente o mesmo comportamento. Algumas funcionalidades recebiam requisições constantemente, enquanto outras eram utilizadas apenas ocasionalmente. Algumas precisavam permanecer disponíveis continuamente, enquanto outras poderiam ser executadas sob demanda. O código podia estar bem modularizado e, ainda assim, a aplicação continuava sendo a unidade principal de deployment e escala.

Foi nesse contexto que a possibilidade de utilizar functions se tornou interessante. Em vez de manter capacidade computacional disponível permanentemente para toda a aplicação, determinadas funcionalidades poderiam consumir recursos apenas quando fossem executadas. Isso não significa que serverless seja sempre mais barato, nem que seja a melhor escolha para qualquer workload. O ponto que me chamou atenção foi outro: diferentes partes do mesmo produto podem ter perfis de processamento muito diferentes, mas normalmente somos levados a escolher uma única estratégia de execução para toda a aplicação.

Essa experiência acabou me levando a uma pergunta que considero especialmente relevante para startups em estágio inicial: por que a granularidade do desenvolvimento precisa ser necessariamente a mesma granularidade do deployment e da infraestrutura? Um módulo pode ser uma excelente unidade para organizar código, testes, regras de negócio e dependências sem precisar ser, necessariamente, a unidade mínima de deployment e escala.

A pergunta ganha mais contexto quando olhamos para a evolução das arquiteturas modernas. Microservices oferecem independência de deployment, escala e ownership, mas introduzem a complexidade inerente aos sistemas distribuídos. O monólito modular, por outro lado, procura preservar a simplicidade operacional de uma aplicação única enquanto cria fronteiras mais fortes dentro do código.

Para uma startup pequena, isso pode ser exatamente o que se procura. Mas existe uma questão que permanece: se conseguimos modularizar o desenvolvimento, precisamos necessariamente escalar e provisionar esses módulos como unidades indivisíveis? É essa questão que quero explorar neste artigo.

## Microservices e monólitos modulares

À medida que sistemas e organizações crescem, diferentes problemas começam a aparecer. Uma aplicação grande pode se tornar difícil de manter porque suas responsabilidades não possuem fronteiras claras, mas também pode se tornar difícil de operar porque diferentes partes precisam evoluir, ser implantadas ou escalar de maneiras diferentes. Não existe uma única razão pela qual um sistema grande se torna complexo, e diferentes arquiteturas surgiram para responder a diferentes partes desse problema.

Microservices ganharam espaço principalmente como uma resposta a problemas de escala organizacional e operacional. Diferentes partes do domínio podem evoluir em velocidades diferentes, equipes precisam trabalhar com maior autonomia e determinados componentes podem ter requisitos de escala ou disponibilidade muito diferentes. Ao separar essas responsabilidades em serviços independentes, cada serviço pode ter seu próprio ciclo de desenvolvimento e deployment, sua própria infraestrutura e sua própria estratégia de escala.

Essa independência, porém, tem um preço. Quando dois componentes estão no mesmo processo, uma dependência pode ser resolvida por uma chamada de método ou pela utilização direta de uma biblioteca. Quando esses componentes passam a ser serviços diferentes, a comunicação atravessa uma rede. Uma operação que antes falhava com uma exceção pode passar a falhar com um timeout; uma chamada síncrona pode exigir retries; uma transação local pode atravessar uma fronteira de processo; logs e métricas precisam ser correlacionados para acompanhar uma requisição entre diferentes componentes.

Microservices não eliminam a complexidade: eles deslocam parte dela para a comunicação, a infraestrutura e a operação de um sistema distribuído. Para organizações grandes, esse trade-off pode ser excelente. A independência entre serviços pode ser mais valiosa do que a complexidade adicional que ela introduz. Para uma startup em estágio inicial, porém, assumir essa complexidade antes que exista uma necessidade concreta pode representar um custo significativo. Com poucos desenvolvedores, cada serviço adicional também significa mais deployments, observabilidade, infraestrutura, troubleshooting e decisões operacionais.

Os monólitos modulares partem de uma preocupação diferente. Sistemas grandes também se tornam difíceis de manter quando suas responsabilidades não possuem fronteiras claras, quando dependências se espalham pelo código e quando mudanças em uma parte do sistema produzem efeitos inesperados em outras. A modularização tenta atacar esse problema sem necessariamente introduzir uma fronteira de processo. Podemos organizar uma aplicação em módulos bem definidos, mantendo as interações entre eles dentro do próprio processo.

Essa abordagem também reconhece uma característica importante do desenvolvimento de software: as fronteiras do domínio mudam. Conforme uma equipe entende melhor o produto, novas regras aparecem, responsabilidades são descobertas e módulos que inicialmente pareciam bem definidos podem precisar ser divididos, combinados ou reorganizados. Manter essas fronteiras dentro de uma única aplicação torna essas mudanças mais simples do que transformá-las imediatamente em decisões de distribuição.

Por isso, monólitos modulares e microservices não representam necessariamente etapas diferentes de uma mesma evolução arquitetural. São abordagens que priorizam propriedades diferentes. Microservices privilegiam independência operacional e organizacional, enquanto o monólito modular busca preservar a simplicidade operacional de uma aplicação única e, ao mesmo tempo, criar fronteiras claras dentro do software.

O problema que me interessa neste artigo aparece justamente entre essas duas preocupações. Podemos ter um sistema suficientemente pequeno para que a complexidade dos microservices não seja justificável, mas que ainda tenha workloads com necessidades de processamento muito diferentes. Podemos também ter um código perfeitamente modularizado e, ainda assim, precisar escalar a aplicação inteira porque ela continua sendo a unidade de deployment e processamento.

É nesse ponto que surge a pergunta central deste artigo: e se a unidade de desenvolvimento pudesse continuar sendo o módulo, enquanto a unidade de processamento e escala pudesse ser um use case?

## Uma arquitetura modular distribuída

A proposta parte de uma separação entre duas preocupações que normalmente acabam acopladas: a unidade de desenvolvimento e a unidade de processamento. O módulo continua sendo a unidade de organização do software. É nele que ficam os use cases relacionados, as regras de negócio, a persistência, os testes e as dependências. O fato de um módulo conter vários use cases, porém, não significa que todos eles precisem ser executados ou escalados da mesma maneira.

Podemos imaginar, por exemplo, um módulo `Orders` contendo `CreateOrder`, `CancelOrder`, `GetOrder` e `GenerateReport`. Esses use cases continuam pertencendo ao mesmo módulo e podem ser desenvolvidos, testados e versionados juntos. A diferença aparece no momento da execução: `CreateOrder` pode ser executado por uma function, `CancelOrder` pode permanecer em uma aplicação convencional, `GetOrder` pode utilizar outra estratégia de processamento e `GenerateReport` pode ser processado de forma assíncrona.

    Orders
    ├── CreateOrder       → function
    ├── CancelOrder       → aplicação
    ├── GetOrder          → function
    └── GenerateReport    → job

Se a demanda por `GetOrder` aumentar, por exemplo, podemos aumentar a capacidade destinada a esse use case sem necessariamente replicar todo o módulo. Essa é a principal característica da proposta: o módulo continua sendo a unidade de desenvolvimento e evolução, enquanto o use case pode, quando fizer sentido, ser uma unidade independente de execução e escala.

Não estou propondo que todo use case precise ser executado isoladamente, muito menos que cada use case deva virar um serviço. A granularidade menor só existe quando existe uma razão para utilizá-la.

Para tornar a ideia concreta, vou utilizar ao longo do artigo algumas tecnologias com as quais gosto de trabalhar, como .NET, PostgreSQL, Dapper, AWS e ferramentas de Infrastructure as Code. Essas escolhas são exemplos de implementação, não requisitos da arquitetura. Em uma implementação com .NET, por exemplo, cada módulo poderia ser uma biblioteca contendo seus use cases, regras de negócio, persistência e testes. A infraestrutura necessária para executar esses use cases poderia ser definida junto ao módulo, utilizando uma ferramenta de Infrastructure as Code como o AWS CDK ou equivalente em outro provedor.

Assim, `Orders` poderia declarar tanto os recursos necessários para sua execução quanto a forma como cada use case seria exposto. `GetOrder` poderia ser associado a uma function e a um endpoint de API, enquanto `GenerateReport` poderia utilizar uma fila e um worker.

A ideia não é duplicar infraestrutura entre os módulos. Existe uma distinção entre aquilo que é compartilhado e aquilo que pertence a um contexto específico. O que realmente é utilizado por todos pode fazer parte de um core comum. Uma capacidade utilizada por alguns módulos pode ser representada por um módulo próprio. Aquilo que pertence a apenas um módulo pode permanecer junto dele.

    Usado por todos
          ↓
        Core

    Usado por alguns
          ↓
    Módulo próprio

    Usado por um
          ↓
    Módulo consumidor

Essa regra também ajuda a evitar que o `Core` se transforme gradualmente em um depósito de abstrações genéricas.

Se `Orders` e `Payments` utilizarem uma capacidade de precificação, por exemplo, isso não significa que `Pricing` precise fazer parte do core. Ele pode ser um módulo próprio, utilizado pelos dois consumidores.

    Orders ────────► Pricing
    Payments ──────► Pricing
    Customers

A mesma lógica vale para a comunicação, mas existe uma diferença importante entre fluxos síncronos e assíncronos.

Em um fluxo síncrono, uma fronteira modular não precisa representar uma fronteira de rede. Se `Orders` utiliza `Customers`, a aplicação pode simplesmente depender da biblioteca correspondente e executar o código de `Customers` diretamente.

Se `Orders.GetOrder` estiver sendo executado dentro de uma function, isso não precisa mudar. A function tem como ponto de entrada o use case de `Orders`, e suas dependências continuam podendo ser resolvidas dentro do próprio processo.

    API
     │
     ▼
    Orders.GetOrder
     │
     ▼
    Customers.GetCustomer
     │
     ▼
    Repository
     │
     ▼
    Database

Em um fluxo assíncrono, por outro lado, a comunicação pode continuar utilizando mensageria ou streaming. Um evento ou comando pode ser publicado em uma fila, como SQS, ou em um stream, dependendo das características do workload.

    Orders
       │
       │ evento
       ▼
     SQS / Stream
       │
       ▼
    Payments

A arquitetura, portanto, não tenta eliminar a comunicação distribuída. Ela tenta evitar introduzi-la onde ela não é necessária.

Se amanhã `Payments.ProcessPayment` precisar ser executado separadamente, por exemplo, ele já pode estar atrás de uma fronteira assíncrona sem que isso exija transformar todo o módulo `Payments` em um serviço independente.

Essa é uma diferença importante em relação a uma abordagem baseada em microservices. A arquitetura não transforma automaticamente cada módulo em um serviço. O sistema pode começar inteiro dentro de um único processo e, conforme surgirem necessidades concretas, determinados use cases podem receber estratégias diferentes de processamento e deployment.

Uma function pode ser uma dessas estratégias, mas também pode ser uma aplicação convencional, um container, um worker ou qualquer outro mecanismo adequado ao workload.

    Aplicação
    ├── Orders
    ├── Customers
    ├── Payments
    └── Inventory

pode evoluir para:

    Aplicação
    ├── Orders
    ├── Customers
    └── Inventory

    Functions
    ├── Orders.GetOrder
    └── Payments.ProcessPayment

sem que `Orders`, `Customers` ou `Payments` precisem ser transformados em microservices.

O que foi distribuído não foi necessariamente o módulo. Foi a execução de determinados use cases.

Essa é, para mim, a distinção central da arquitetura: podemos preservar uma unidade de desenvolvimento suficientemente grande para manter o código organizado e, ao mesmo tempo, utilizar uma unidade de execução suficientemente pequena para que determinados workloads possam ser processados e escalados de forma independente.

## Functions como ponto de partida

Para essa proposta, eu começaria utilizando functions como estratégia padrão para os use cases expostos por endpoints síncronos.

Não porque functions sejam necessariamente superiores a containers ou processos convencionais, mas porque oferecem uma combinação interessante para uma startup em estágio inicial: processamento sob demanda, escala independente e pouca capacidade ociosa quando a utilização é baixa ou variável.

A ideia é começar com uma estratégia simples e mudar apenas quando os dados mostrarem que ela deixou de ser adequada. Em vez de provisionar capacidade permanente com base em uma estimativa de crescimento, podemos deixar que cada use case consuma recursos conforme for utilizado.

Isso é particularmente interessante no início de uma startup, quando muitas características do workload ainda são desconhecidas. O tráfego pode ser baixo, irregular ou difícil de prever. Uma funcionalidade pode permanecer quase sem utilização durante meses e, de repente, passar a receber uma quantidade significativa de requisições.

Se `GetOrder` apresentar um volume constante e elevado, por exemplo, pode fazer sentido migrá-lo para um container ou processo provisionado. Se `GenerateReport` continuar sendo executado poucas vezes por dia, pode permanecer como function.

    Orders
    ├── GetOrder        → container
    ├── CreateOrder     → function
    ├── CancelOrder     → function
    └── GenerateReport  → function

A mudança acontece no nível do use case. O módulo `Orders` não precisa ser reorganizado nem transformado em um novo serviço. Estamos apenas substituindo a estratégia utilizada para executar uma determinada parte dele.

Para workloads assíncronos, a estratégia pode ser diferente desde o início. Um use case que consome mensagens de uma fila ou de um stream pode ser executado por um worker, por exemplo. Function continua sendo uma possibilidade, mas não precisa ser o padrão para todos os tipos de workload.

Existe, naturalmente, o problema do cold start. Dependendo do runtime e dos requisitos de latência, o tempo necessário para inicializar uma function pode ser relevante. Para um workload executado poucas vezes por dia, isso pode ser irrelevante. Para uma operação de baixa latência e tráfego constante, pode ser uma razão para escolher outra estratégia de execução.

Esse é justamente o ponto da proposta. Functions são um ponto de partida, não uma decisão definitiva. Conforme o sistema revela suas características reais, cada use case pode adotar a estratégia de execução que melhor se adapta ao seu workload.

A arquitetura, portanto, não depende de permanecer serverless. Ela depende da possibilidade de mudar essa decisão sem precisar mudar a organização do software.

## Vantagens e trade-offs

A principal vantagem da proposta é separar a granularidade do desenvolvimento da granularidade do processamento. Um módulo pode continuar sendo uma unidade coesa de código, testes e evolução, enquanto seus use cases podem utilizar estratégias de execução diferentes.

Imagine um módulo `Orders` em que `GetOrder` recebe muito mais requisições do que `CancelOrder`, enquanto `GenerateReport` é executado apenas algumas vezes por dia. No monólito modular, todos continuam fazendo parte da mesma aplicação e compartilham a mesma unidade de deployment e processamento. Na arquitetura proposta, cada um poderia utilizar uma estratégia diferente.

    GetOrder        → function
    CreateOrder     → function
    CancelOrder     → aplicação
    GenerateReport  → job

O código não precisa ser reorganizado para isso. O módulo continua sendo `Orders`, com seus use cases, regras de negócio, persistência e testes. O que muda é a forma como cada workload é executado.

Essa granularidade também pode ser interessante do ponto de vista econômico. Uma startup em estágio inicial pode passar bastante tempo com demanda baixa e imprevisível. Nesse cenário, manter capacidade permanente para toda a aplicação pode significar pagar por recursos que permanecem ociosos durante boa parte do tempo. Para determinados workloads, o processamento sob demanda pode aproximar o custo da utilização efetiva.

Isso não significa que a arquitetura seja necessariamente mais barata. Workloads constantes e previsíveis podem ser mais econômicos em infraestrutura provisionada. A vantagem está na possibilidade de não obrigar toda a aplicação a utilizar a mesma estratégia. Um use case pode utilizar uma function, outro um container, outro uma aplicação convencional e outro um worker.

A decisão pode acompanhar o comportamento real do workload. Esse talvez seja um dos pontos mais interessantes para uma startup: mais do que otimizar a infraestrutura desde o primeiro dia, a proposta tenta adiar decisões de infraestrutura até que o comportamento real do produto forneça informação suficiente para tomá-las.

Em vez de provisionar hoje uma infraestrutura dimensionada para um crescimento que talvez aconteça daqui a dois anos, podemos começar com uma capacidade compatível com a demanda atual e mudar a estratégia apenas quando existir uma necessidade concreta. A arquitetura não tenta antecipar o crescimento. Ela tenta evitar que seja necessário antecipar a infraestrutura.

Essa flexibilidade também muda a forma como a aplicação pode evoluir. Em vez de escolher entre permanecer inteiramente monolítica ou migrar progressivamente para microservices, podemos imaginar uma evolução mais seletiva:

    Monólito modular
           ↓
    Distribuição seletiva
           ↓
    Mais distribuição quando necessário

Um sistema pode permanecer majoritariamente em um único processo enquanto apenas os use cases que justificam uma estratégia diferente são distribuídos. Não é necessário antecipar quais partes da aplicação precisarão ser escaladas, isoladas ou processadas de maneira diferente no futuro.

Isso pode ser particularmente interessante quando workloads muito diferentes coexistem dentro do mesmo produto. Uma funcionalidade de IA, por exemplo, pode ter requisitos de processamento, latência e custo completamente diferentes de uma operação tradicional de CRUD. Não existe necessariamente uma razão para que ambos utilizem a mesma estratégia de execução apenas porque pertencem ao mesmo módulo.

A funcionalidade de IA poderia utilizar uma infraestrutura específica e escalar de maneira independente, enquanto os demais use cases continuariam utilizando uma infraestrutura convencional.

No fundo, a vantagem não é simplesmente conseguir escalar com mais granularidade. É evitar que a necessidade de um workload determine a infraestrutura dos demais. Mas essa flexibilidade não elimina a complexidade. Ela permite introduzi-la de forma seletiva.

Quando um use case passa a ser executado fora do processo principal, surgem os problemas conhecidos de sistemas distribuídos: latência, timeouts, retries, observabilidade, idempotência e falhas parciais. A diferença é que esses custos não precisam ser assumidos por toda a aplicação. Se dez use cases podem continuar sendo executados dentro de uma aplicação convencional, não existe necessariamente uma razão para distribuí-los. Se um décimo primeiro apresenta uma necessidade diferente de escala ou processamento, podemos distribuir apenas esse use case. A proposta, portanto, não é criar microservices menores. É permitir que a distribuição seja uma decisão local, tomada quando houver um benefício concreto.

Existe também um custo relacionado às dependências. Quando um módulo utiliza outro como biblioteca, uma alteração incompatível nessa dependência exige que os consumidores sejam atualizados, recompilados e testados. Isso reduz parte da independência de deployment que seria obtida com serviços completamente separados. Por outro lado, enquanto a dependência permanecer dentro do mesmo processo, não precisamos pagar o custo de uma comunicação remota para cada interação entre módulos. `Orders` pode utilizar `Customers` diretamente como biblioteca, sem transformar essa dependência em uma chamada HTTP apenas porque os módulos possuem fronteiras diferentes.

    Orders ───────► Customers
       │
       └──────────► Pricing
                      │
                      ▼
                   Products

Esse ponto torna o grafo de dependências especialmente importante. As dependências entre módulos precisam ter direção clara e evitar ciclos. Se `Orders` depende de `Customers` e `Customers` depende de `Orders`, distribuí-los separadamente pode apenas transformar um acoplamento de código em um acoplamento de rede.

A distribuição de um use case também não implica a distribuição de todas as suas dependências. Se `Orders.GetOrder` utiliza `Customers.GetCustomer`, por exemplo, essa chamada pode continuar sendo feita diretamente pela biblioteca de `Customers`.

    Orders.GetOrder
          │
          └──► Customers.GetCustomer
                    │
                    └──► Repository

Nesse cenário, apenas a execução de `Orders.GetOrder` foi distribuída. `Customers` continua sendo uma dependência in-process. Uma nova fronteira distribuída só aparece quando existe uma decisão explícita de executar `Customers` separadamente.

Esse é um aspecto importante da proposta: a distribuição não precisa acompanhar as fronteiras dos módulos. Um use case pode ser distribuído sem que todos os módulos dos quais ele depende também sejam transformados em serviços.

Existe ainda um custo relacionado à própria granularidade do processamento. Separar use cases permite escalar cada workload individualmente, mas também pode significar replicar o runtime e as dependências do módulo em várias unidades de execução. Uma function ou container pode precisar carregar as mesmas bibliotecas utilizadas por outros use cases, aumentando consumo de memória, tempo de inicialização e, dependendo do workload, o custo total de processamento. A granularidade menor, portanto, não é gratuita. Ela precisa trazer um benefício suficiente para compensar essa duplicação.

Outro limite importante está nos recursos compartilhados. A possibilidade de escalar `GetOrder` independentemente não significa que o banco de dados consiga acompanhar essa expansão. PostgreSQL, filas, caches e serviços externos continuam podendo ser gargalos.

A proposta aumenta a granularidade com que podemos escalar o processamento, mas não remove os limites dos componentes dos quais esse processamento depende. Se o banco é o gargalo, simplesmente aumentar a quantidade de functions pode piorar o problema. Por isso, a ideia não é que cada use case possa escalar indefinidamente de forma independente. É que, quando houver capacidade disponível nos recursos dos quais ele depende, não seja necessário escalar junto aquilo que não participa daquele workload.

Existe também uma consequência operacional. Um sistema com diferentes estratégias de execução terá mais deployments, configurações, permissões, observabilidade e recursos de infraestrutura do que um monólito convencional. A proposta não elimina esse custo. O que ela tenta fazer é evitar que ele seja introduzido antes de existir uma necessidade concreta. Esse talvez seja o principal trade-off da arquitetura: ganhar flexibilidade e granularidade ao custo de alguma complexidade operacional adicional.

A pergunta, portanto, não deveria ser se essa arquitetura é mais simples do que um monólito ou do que microservices. Provavelmente ela não é. A pergunta é se a complexidade adicional aparece apenas onde existe uma necessidade que a justifique.

## O que essa arquitetura é, e quando ela faz sentido

Eu não chamaria essa proposta de microservices. Não porque uma arquitetura modular distribuída seja incompatível com microservices, mas porque a unidade arquitetural proposta é diferente. Em microservices, o serviço normalmente concentra decisões de modularidade, deployment, ownership, operação e escala. Aqui, essas decisões são deliberadamente separadas.

O módulo continua sendo a unidade de desenvolvimento e evolução. Os use cases continuam pertencendo a esse módulo e podem compartilhar código, regras de negócio, dependências e testes. A diferença é que um use case pode, quando necessário, ter uma estratégia própria de execução e escala.

Isso significa que um módulo pode permanecer inteiramente dentro de uma aplicação convencional durante toda a vida do produto. Outro pode ter apenas um use case executado como function. Um terceiro pode utilizar processamento assíncrono para uma operação específica. A distribuição não é o objetivo da arquitetura; é uma possibilidade que pode ser utilizada quando houver uma razão concreta.

Por isso, prefiro chamar essa ideia de arquitetura modular distribuída. Ela não pretende ser uma versão simplificada de microservices, nem uma etapa obrigatória entre o monólito modular e uma arquitetura de serviços. A proposta é explorar se podemos separar duas decisões que normalmente acabam sendo tomadas juntas: como organizamos e desenvolvemos o software e como provisionamos e escalamos seu processamento.

Isso também significa que não vejo essa arquitetura como adequada para qualquer sistema. Se uma aplicação é pequena, possui uma carga previsível e uma infraestrutura convencional atende ao problema com folga, introduzir essa granularidade pode simplesmente adicionar complexidade sem produzir um benefício proporcional.

Da mesma forma, sistemas com requisitos muito específicos de segurança, disponibilidade, governança, auditoria, isolamento ou consistência podem exigir outras decisões arquiteturais. A proposta deste artigo parte de um contexto mais específico: startups em estágio inicial, com equipes pequenas, orçamento limitado e workloads que podem crescer de maneira bastante desigual.

Mesmo nesse cenário, existe um limite importante. Distribuir o processamento não elimina os recursos compartilhados. Se vários use cases dependem do mesmo banco de dados e o banco se torna o gargalo, aumentar a quantidade de functions não resolve o problema. Pode, inclusive, aumentar a pressão sobre o recurso já saturado. A arquitetura permite escalar o processamento com mais granularidade, mas não elimina os limites dos componentes dos quais esse processamento depende.

Por isso, vejo essa abordagem principalmente como uma hipótese para um determinado contexto, e não como uma recomendação universal. Ela parece fazer mais sentido quando existe uma combinação de equipe pequena, demanda inicialmente baixa ou variável e uma expectativa de que diferentes partes do produto possam crescer em velocidades muito diferentes.

Nessas condições, a possibilidade de escolher a estratégia de processamento por use case pode permitir que a infraestrutura acompanhe o comportamento real do produto, sem exigir que a startup assuma antecipadamente toda a capacidade ou complexidade operacional que talvez só seja necessária no futuro.

No fim, a proposta não é escolher entre monólito modular e microservices. É questionar se precisamos escolher uma única unidade de execução para todo o sistema. Talvez seja possível manter a simplicidade do desenvolvimento modular e, ao mesmo tempo, distribuir apenas aquilo que realmente precisar ser distribuído.

## Como eu saberia se a arquitetura funcionou?

É importante deixar claro que este artigo apresenta uma proposta arquitetural, não uma arquitetura validada empiricamente. Eu não tive a oportunidade de implementar esse modelo em uma startup real e acompanhar sua evolução ao longo dos anos. Portanto, não tenho dados para afirmar que ele necessariamente reduz custos, simplifica a evolução do sistema ou produz uma experiência melhor para uma equipe de desenvolvimento.

O que tenho é uma experiência anterior que me levou a enxergar um possível espaço entre o monólito modular e microservices: de um lado, a importância de manter o desenvolvimento simples e modular; de outro, a possibilidade de que diferentes partes de um produto tenham necessidades muito diferentes de processamento e infraestrutura.

Para mim, a proposta só faria sentido se essa separação entre desenvolvimento e processamento trouxesse benefícios reais sem criar uma complexidade maior do que aquela que pretende evitar. Um dos primeiros sinais seria a capacidade de manter os módulos relativamente simples mesmo quando alguns de seus use cases passassem a ser executados de maneiras diferentes. A equipe deveria conseguir desenvolver e testar o módulo sem precisar transformar cada diferença de infraestrutura em uma preocupação do código. Ao mesmo tempo, um use case deveria poder ganhar uma estratégia própria de execução ou escala sem exigir que todo o módulo acompanhasse essa mudança.

Outro sinal seria a evolução do sistema. Se a aplicação pudesse começar de forma simples, permanecer majoritariamente em um único processo e distribuir apenas alguns use cases conforme surgissem necessidades concretas, isso seria uma evidência de que a arquitetura está cumprindo uma de suas principais propostas: permitir que a complexidade seja introduzida de forma gradual, em vez de antecipada.

As dependências também seriam importantes. A arquitetura deveria permitir que módulos continuassem utilizando bibliotecas diretamente quando isso fosse adequado, sem transformar toda fronteira modular em uma chamada de rede. Se, para distribuir um único use case, fosse necessário transformar uma grande parte das dependências em serviços independentes, isso seria um sinal de que a granularidade proposta talvez esteja criando mais acoplamento do que removendo.

O aspecto econômico seria outro ponto a observar. A granularidade adicional deveria, em alguns workloads, permitir que os recursos acompanhassem melhor a utilização real. Mas essa conta não poderia considerar apenas o custo de processamento. Seria necessário incluir observabilidade, deployments, infraestrutura, manutenção e o tempo da própria equipe. Se a economia obtida com o processamento sob demanda fosse menor do que o custo adicional de operar a arquitetura, a proposta não estaria cumprindo seu objetivo.

Por fim, eu observaria o que acontece conforme a empresa cresce. Se, depois de atingir uma escala maior, fosse necessário reescrever os módulos, substituir sistematicamente as dependências por APIs ou migrar obrigatoriamente para microservices para recuperar propriedades importantes, isso seria um sinal de que a arquitetura apenas adiou o problema. Por outro lado, se o sistema pudesse evoluir gradualmente, distribuindo apenas aquilo que realmente justificasse a distribuição, teríamos uma evidência mais interessante de que a abordagem funciona.

Ainda assim, existe uma possibilidade importante: talvez o resultado do experimento seja descobrir que essa arquitetura não oferece uma vantagem suficiente sobre um monólito modular tradicional. E isso também seria um resultado válido.

A proposta, portanto, não parte da certeza de que encontrou uma arquitetura melhor. Parte de uma hipótese: talvez exista uma forma de preservar a simplicidade do desenvolvimento modular sem obrigar todo o sistema a compartilhar a mesma estratégia de processamento.

## Uma arquitetura a ser testada

Talvez essa abordagem não funcione tão bem quanto imagino. A complexidade operacional pode aparecer cedo demais. Conforme a organização cresça, determinadas características do sistema podem tornar microservices uma escolha mais adequada. E, em muitos casos, o próprio monólito modular pode continuar sendo a melhor resposta.

Isso não contradiz a proposta. A arquitetura foi pensada para um contexto específico: startups em estágio inicial, com equipes pequenas, recursos limitados e workloads que podem apresentar diferenças significativas de demanda. Fora desse contexto, os trade-offs podem ser completamente diferentes.

A ideia também não é eliminar microservices. Se uma organização chegar a um ponto em que isolamento, ownership, ciclos de deployment independentes ou outras propriedades de uma arquitetura distribuída se tornarem mais importantes do que a simplicidade inicial, microservices podem ser uma evolução perfeitamente razoável. Da mesma forma, se a aplicação permanecer pequena e previsível, pode não existir razão alguma para abandonar o monólito modular.

A proposta é mais específica: começar com uma arquitetura modular simples e manter a liberdade de distribuir apenas aquilo que realmente precisar ser distribuído. Se isso funcionar, uma startup poderá adiar tanto decisões de infraestrutura quanto parte da complexidade operacional até que exista uma razão concreta para assumi-las. Não estou propondo uma substituta para microservices. Estou propondo uma alternativa para o ponto de partida.

A arquitetura modular distribuída é, no fim, uma ideia que eu gostaria de colocar em prática. Ainda não sei onde estão seus limites, nem se os benefícios serão suficientes para compensar os custos. Mas acredito que existe uma pergunta interessante o bastante para justificar o experimento: podemos manter a simplicidade do desenvolvimento modular e, ao mesmo tempo, permitir que o processamento seja provisionado na granularidade dos use cases que realmente precisam dele?
