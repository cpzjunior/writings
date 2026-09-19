# ¿Y si utilizamos una arquitectura modular distribuida en lugar del monolito modular?

_Una idea de arquitectura para startups en etapa inicial que necesitan crecer sin pagar desproporcionadamente por infraestructura o por la complejidad de los microservicios._

**Resumen:** Propongo una arquitectura modular distribuida que separa la unidad de desarrollo de la unidad de procesamiento: el módulo continúa organizando código, reglas y pruebas, mientras que cada use case puede adoptar su propia estrategia de ejecución y escalado cuando exista una necesidad concreta. Con esto, las startups pueden comenzar con una estructura simple, distribuyendo únicamente los workloads que realmente requieran más capacidad, sin asumir anticipadamente la complejidad de los microservicios. La idea no es sustituir el monolito modular ni los microservicios, sino crear una alternativa de partida que permita posponer decisiones de infraestructura e introducir complejidad de forma gradual.

---

Cuando una startup está comenzando, la arquitectura de software suele ser una cuestión de equilibrio. El equipo es pequeño, el producto todavía está descubriendo su propio mercado, el volumen de usuarios es incierto y el presupuesto es limitado. Al mismo tiempo, algunas decisiones tomadas al principio pueden permanecer durante años y volverse difíciles o costosas de cambiar después. En este contexto, una arquitectura necesita hacer algo más que organizar el código: necesita permitir que la empresa posponga decisiones costosas hasta que exista una razón concreta para tomarlas.

Hace algunos años, fui presidente voluntario de Se Doar, una ONG que mantenía una plataforma para conectar organizaciones sociales con personas y empresas interesadas en hacer donaciones u ofrecer trabajo voluntario. Además de la presidencia, me ocupaba de la plataforma junto con otros voluntarios. Era un contexto en el que estas restricciones resultaban especialmente evidentes. Teníamos pocos recursos, un equipo pequeño y poco margen para mantener infraestructura ociosa. Cada decisión técnica también tenía que evaluarse por su impacto operativo y financiero.

La primera versión de la plataforma utilizaba un monolito modular. En aquel momento, tenía sentido. La aplicación era relativamente pequeña, los módulos ayudaban a separar responsabilidades y la infraestructura seguía siendo sencilla de operar. Sin embargo, a medida que el sistema evolucionó, quedó claro que las diferentes partes de la aplicación no tenían necesariamente el mismo comportamiento. Algunas funcionalidades recibían solicitudes constantemente, mientras que otras se utilizaban solo ocasionalmente. Algunas necesitaban permanecer disponibles continuamente, mientras que otras podían ejecutarse bajo demanda. El código podía estar bien modularizado y, aun así, la aplicación seguía siendo la unidad principal de deployment y escalado.

Fue en ese contexto cuando la posibilidad de utilizar functions se volvió interesante. En lugar de mantener capacidad computacional disponible permanentemente para toda la aplicación, determinadas funcionalidades podían consumir recursos solo cuando se ejecutaran. Esto no significa que serverless sea siempre más barato, ni que sea la mejor opción para cualquier workload. El punto que me llamó la atención fue otro: diferentes partes del mismo producto pueden tener perfiles de procesamiento muy diferentes, pero normalmente nos vemos obligados a elegir una única estrategia de ejecución para toda la aplicación.

Esta experiencia terminó llevándome a una pregunta que considero especialmente relevante para startups en etapa inicial: ¿por qué la granularidad del desarrollo tiene que ser necesariamente la misma que la granularidad del deployment y de la infraestructura? Un módulo puede ser una excelente unidad para organizar código, pruebas, reglas de negocio y dependencias sin tener que ser, necesariamente, la unidad mínima de deployment y escalado.

La pregunta adquiere más contexto cuando observamos la evolución de las arquitecturas modernas. Los microservicios ofrecen independencia de deployment, escalado y ownership, pero introducen la complejidad inherente a los sistemas distribuidos. El monolito modular, por otro lado, busca preservar la simplicidad operativa de una aplicación única mientras crea fronteras más fuertes dentro del código.

Para una startup pequeña, esto puede ser exactamente lo que se busca. Pero existe una cuestión que permanece: si podemos modularizar el desarrollo, ¿necesitamos necesariamente escalar y provisionar esos módulos como unidades indivisibles? Es esta cuestión la que quiero explorar en este artículo.

## Microservicios y monolitos modulares

A medida que los sistemas y las organizaciones crecen, empiezan a aparecer diferentes problemas. Una aplicación grande puede volverse difícil de mantener porque sus responsabilidades no tienen fronteras claras, pero también puede volverse difícil de operar porque diferentes partes necesitan evolucionar, desplegarse o escalar de maneras diferentes. No existe una única razón por la que un sistema grande se vuelve complejo, y diferentes arquitecturas surgieron para responder a diferentes partes de este problema.

Los microservicios ganaron espacio principalmente como respuesta a problemas de escala organizacional y operativa. Diferentes partes del dominio pueden evolucionar a velocidades distintas, los equipos necesitan trabajar con mayor autonomía y determinados componentes pueden tener requisitos de escala o disponibilidad muy diferentes. Al separar estas responsabilidades en servicios independientes, cada servicio puede tener su propio ciclo de desarrollo y deployment, su propia infraestructura y su propia estrategia de escalado.

Esta independencia, sin embargo, tiene un precio. Cuando dos componentes están en el mismo proceso, una dependencia puede resolverse mediante una llamada a un método o mediante el uso directo de una biblioteca. Cuando estos componentes pasan a ser servicios diferentes, la comunicación atraviesa una red. Una operación que antes fallaba con una excepción puede pasar a fallar con un timeout; una llamada síncrona puede requerir retries; una transacción local puede atravesar una frontera de proceso; los logs y las métricas necesitan correlacionarse para seguir una solicitud entre diferentes componentes.

Los microservicios no eliminan la complejidad: desplazan parte de ella hacia la comunicación, la infraestructura y la operación de un sistema distribuido. Para organizaciones grandes, este trade-off puede ser excelente. La independencia entre servicios puede ser más valiosa que la complejidad adicional que introduce. Para una startup en etapa inicial, sin embargo, asumir esta complejidad antes de que exista una necesidad concreta puede representar un coste significativo. Con pocos desarrolladores, cada servicio adicional también significa más deployments, observabilidad, infraestructura, troubleshooting y decisiones operativas.

Los monolitos modulares parten de una preocupación diferente. Los sistemas grandes también se vuelven difíciles de mantener cuando sus responsabilidades no tienen fronteras claras, cuando las dependencias se dispersan por el código y cuando los cambios en una parte del sistema producen efectos inesperados en otras. La modularización intenta atacar este problema sin necesariamente introducir una frontera de proceso. Podemos organizar una aplicación en módulos bien definidos, manteniendo las interacciones entre ellos dentro del propio proceso.

Este enfoque también reconoce una característica importante del desarrollo de software: las fronteras del dominio cambian. A medida que un equipo comprende mejor el producto, aparecen nuevas reglas, se descubren responsabilidades y los módulos que inicialmente parecían bien definidos pueden necesitar dividirse, combinarse o reorganizarse. Mantener estas fronteras dentro de una única aplicación hace que estos cambios sean más sencillos que transformarlos inmediatamente en decisiones de distribución.

Por eso, los monolitos modulares y los microservicios no representan necesariamente etapas diferentes de una misma evolución arquitectónica. Son enfoques que priorizan propiedades diferentes. Los microservicios privilegian la independencia operativa y organizacional, mientras que el monolito modular busca preservar la simplicidad operativa de una aplicación única y, al mismo tiempo, crear fronteras claras dentro del software.

El problema que me interesa en este artículo aparece precisamente entre estas dos preocupaciones. Podemos tener un sistema suficientemente pequeño como para que la complejidad de los microservicios no esté justificada, pero que aun así tenga workloads con necesidades de procesamiento muy diferentes. También podemos tener un código perfectamente modularizado y, aun así, necesitar escalar la aplicación completa porque continúa siendo la unidad de deployment y procesamiento.

Es en este punto donde surge la pregunta central de este artículo: ¿y si la unidad de desarrollo pudiera seguir siendo el módulo, mientras que la unidad de procesamiento y escalado pudiera ser un use case?

## Una arquitectura modular distribuida

La propuesta parte de una separación entre dos preocupaciones que normalmente terminan acopladas: la unidad de desarrollo y la unidad de procesamiento. El módulo continúa siendo la unidad de organización del software. Es allí donde se encuentran los use cases relacionados, las reglas de negocio, la persistencia, las pruebas y las dependencias. Sin embargo, el hecho de que un módulo contenga varios use cases no significa que todos tengan que ejecutarse o escalarse de la misma manera.

Podemos imaginar, por ejemplo, un módulo `Orders` que contenga `CreateOrder`, `CancelOrder`, `GetOrder` y `GenerateReport`. Estos use cases continúan perteneciendo al mismo módulo y pueden desarrollarse, probarse y versionarse juntos. La diferencia aparece en el momento de la ejecución: `CreateOrder` puede ejecutarse mediante una function, `CancelOrder` puede permanecer en una aplicación convencional, `GetOrder` puede utilizar otra estrategia de procesamiento y `GenerateReport` puede procesarse de forma asíncrona.

```
Orders
├── CreateOrder       → function
├── CancelOrder       → aplicación
├── GetOrder          → function
└── GenerateReport    → job
```

Si la demanda de `GetOrder` aumenta, por ejemplo, podemos incrementar la capacidad destinada a este use case sin necesidad de replicar todo el módulo. Esta es la principal característica de la propuesta: el módulo continúa siendo la unidad de desarrollo y evolución, mientras que el use case puede, cuando tenga sentido, ser una unidad independiente de ejecución y escalado.

No estoy proponiendo que todo use case tenga que ejecutarse de forma aislada, mucho menos que cada use case deba convertirse en un servicio. La granularidad menor solo existe cuando hay una razón para utilizarla.

Para hacer la idea concreta, utilizaré a lo largo del artículo algunas tecnologías con las que me gusta trabajar, como .NET, PostgreSQL, Dapper, AWS y herramientas de Infrastructure as Code. Estas elecciones son ejemplos de implementación, no requisitos de la arquitectura. En una implementación con .NET, por ejemplo, cada módulo podría ser una biblioteca que contenga sus use cases, reglas de negocio, persistencia y pruebas. La infraestructura necesaria para ejecutar estos use cases podría definirse junto con el módulo, utilizando una herramienta de Infrastructure as Code como AWS CDK o un equivalente en otro proveedor.

Así, `Orders` podría declarar tanto los recursos necesarios para su ejecución como la forma en que cada use case sería expuesto. `GetOrder` podría asociarse a una function y a un endpoint de API, mientras que `GenerateReport` podría utilizar una cola y un worker.

La idea no es duplicar infraestructura entre los módulos. Existe una distinción entre aquello que es compartido y aquello que pertenece a un contexto específico. Lo que realmente es utilizado por todos puede formar parte de un core común. Una capacidad utilizada por algunos módulos puede representarse mediante un módulo propio. Aquello que pertenece a un solo módulo puede permanecer junto a él.

```
Usado por todos
      ↓
    Core

Usado por algunos
      ↓
Módulo propio

Usado por uno
      ↓
Módulo consumidor
```

Esta regla también ayuda a evitar que el `Core` se convierta gradualmente en un depósito de abstracciones genéricas.

Si `Orders` y `Payments` utilizan una capacidad de pricing, por ejemplo, eso no significa que `Pricing` tenga que formar parte del core. Puede ser un módulo propio, utilizado por ambos consumidores.

```
Orders ────────► Pricing
Payments ──────► Pricing
Customers
```

La misma lógica se aplica a la comunicación, pero existe una diferencia importante entre flujos síncronos y asíncronos.

En un flujo síncrono, una frontera modular no tiene por qué representar una frontera de red. Si `Orders` utiliza `Customers`, la aplicación puede simplemente depender de la biblioteca correspondiente y ejecutar el código de `Customers` directamente dentro del propio proceso.

Si `Orders.GetOrder` se está ejecutando dentro de una function, esto no tiene por qué cambiar. La function tiene como punto de entrada el use case de `Orders`, y sus dependencias pueden seguir resolviéndose dentro del propio proceso.

```
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
```

En un flujo asíncrono, por otro lado, la comunicación puede continuar utilizando mensajería o streaming. Un evento o comando puede publicarse en una cola, como SQS, o en un stream, dependiendo de las características del workload.

```
Orders
   │
   │ evento
   ▼
 SQS / Stream
   │
   ▼
Payments
```

La arquitectura, por tanto, no intenta eliminar la comunicación distribuida. Intenta evitar introducirla donde no es necesaria.

Si mañana `Payments.ProcessPayment` necesita ejecutarse por separado, por ejemplo, ya puede estar detrás de una frontera asíncrona sin que sea necesario transformar todo el módulo `Payments` en un servicio independiente.

Esta es una diferencia importante respecto de un enfoque basado en microservicios. La arquitectura no transforma automáticamente cada módulo en un servicio. El sistema puede comenzar íntegramente dentro de un único proceso y, conforme surjan necesidades concretas, determinados use cases pueden recibir estrategias diferentes de procesamiento y deployment.

Una function puede ser una de esas estrategias, pero también puede ser una aplicación convencional, un container, un worker o cualquier otro mecanismo adecuado al workload.

```
Aplicación
├── Orders
├── Customers
├── Payments
└── Inventory
```

puede evolucionar a:

```
Aplicación
├── Orders
├── Customers
└── Inventory

Functions
├── Orders.GetOrder
└── Payments.ProcessPayment
```

sin que `Orders`, `Customers` o `Payments` tengan que transformarse en microservicios.

Lo que se distribuyó no fue necesariamente el módulo. Fue la ejecución de determinados use cases.

Esta es, para mí, la distinción central de la arquitectura: podemos preservar una unidad de desarrollo suficientemente grande como para mantener el código organizado y, al mismo tiempo, utilizar una unidad de ejecución suficientemente pequeña como para que determinados workloads puedan procesarse y escalarse de forma independiente.

## Functions como punto de partida

Para esta propuesta, comenzaría utilizando functions como estrategia predeterminada para los use cases expuestos mediante endpoints síncronos.

No porque las functions sean necesariamente superiores a containers o procesos convencionales, sino porque ofrecen una combinación interesante para una startup en etapa inicial: procesamiento bajo demanda, escalado independiente y poca capacidad ociosa cuando la utilización es baja o variable.

La idea es comenzar con una estrategia simple y cambiar solo cuando los datos demuestren que ha dejado de ser adecuada. En lugar de provisionar capacidad permanente basándonos en una estimación de crecimiento, podemos dejar que cada use case consuma recursos a medida que se utiliza.

Esto es particularmente interesante al inicio de una startup, cuando muchas características del workload todavía son desconocidas. El tráfico puede ser bajo, irregular o difícil de prever. Una funcionalidad puede permanecer prácticamente sin uso durante meses y, de repente, empezar a recibir una cantidad significativa de solicitudes.

Si `GetOrder` presenta un volumen constante y elevado, por ejemplo, puede tener sentido migrarlo a un container o proceso provisionado. Si `GenerateReport` continúa ejecutándose pocas veces al día, puede permanecer como function.

```
Orders
├── GetOrder        → container
├── CreateOrder     → function
├── CancelOrder     → function
└── GenerateReport  → function
```

El cambio ocurre en el nivel del use case. El módulo `Orders` no necesita reorganizarse ni transformarse en un nuevo servicio. Simplemente estamos sustituyendo la estrategia utilizada para ejecutar una determinada parte de él.

Para workloads asíncronos, la estrategia puede ser diferente desde el principio. Un use case que consume mensajes de una cola o de un stream puede ejecutarse mediante un worker, por ejemplo. Function sigue siendo una posibilidad, pero no tiene por qué ser el estándar para todos los tipos de workload.

Existe, naturalmente, el problema del cold start. Dependiendo del runtime y de los requisitos de latencia, el tiempo necesario para inicializar una function puede ser relevante. Para un workload ejecutado pocas veces al día, esto puede ser irrelevante. Para una operación de baja latencia y tráfico constante, puede ser una razón para elegir otra estrategia de ejecución.

Este es precisamente el punto de la propuesta. Functions son un punto de partida, no una decisión definitiva. A medida que el sistema revele sus características reales, cada use case puede adoptar la estrategia de ejecución que mejor se adapte a su workload.

La arquitectura, por tanto, no depende de permanecer serverless. Depende de la posibilidad de cambiar esta decisión sin tener que cambiar la organización del software.

## Ventajas y trade-offs

La principal ventaja de la propuesta es separar la granularidad del desarrollo de la granularidad del procesamiento. Un módulo puede continuar siendo una unidad cohesiva de código, pruebas y evolución, mientras que sus use cases pueden utilizar diferentes estrategias de ejecución.

Imaginemos un módulo `Orders` en el que `GetOrder` recibe muchas más solicitudes que `CancelOrder`, mientras que `GenerateReport` se ejecuta solo algunas veces al día. En el monolito modular, todos continúan formando parte de la misma aplicación y comparten la misma unidad de deployment y procesamiento. En la arquitectura propuesta, cada uno podría utilizar una estrategia diferente.

```
GetOrder        → function
CreateOrder     → function
CancelOrder     → aplicación
GenerateReport  → job
```

El código no necesita reorganizarse para ello. El módulo continúa siendo `Orders`, con sus use cases, reglas de negocio, persistencia y pruebas. Lo que cambia es la forma en que cada workload se ejecuta.

Esta granularidad también puede ser interesante desde el punto de vista económico. Una startup en etapa inicial puede pasar bastante tiempo con una demanda baja e impredecible. En este escenario, mantener capacidad permanente para toda la aplicación puede significar pagar por recursos que permanecen ociosos durante buena parte del tiempo. Para determinados workloads, el procesamiento bajo demanda puede aproximar el coste a la utilización efectiva.

Esto no significa que la arquitectura sea necesariamente más barata. Los workloads constantes y previsibles pueden ser más económicos con infraestructura provisionada. La ventaja está en la posibilidad de no obligar a toda la aplicación a utilizar la misma estrategia. Un use case puede utilizar una function, otro un container, otro una aplicación convencional y otro un worker.

La decisión puede acompañar el comportamiento real del workload. Este quizá sea uno de los puntos más interesantes para una startup: más que optimizar la infraestructura desde el primer día, la propuesta intenta posponer decisiones de infraestructura hasta que el comportamiento real del producto proporcione información suficiente para tomarlas.

En lugar de provisionar hoy una infraestructura dimensionada para un crecimiento que quizá ocurra dentro de dos años, podemos comenzar con una capacidad compatible con la demanda actual y cambiar la estrategia solo cuando exista una necesidad concreta. La arquitectura no intenta anticipar el crecimiento. Intenta evitar que sea necesario anticipar la infraestructura.

Esta flexibilidad también cambia la forma en que la aplicación puede evolucionar. En lugar de elegir entre permanecer completamente monolítica o migrar progresivamente hacia microservicios, podemos imaginar una evolución más selectiva:

```
Monolito modular
       ↓
Distribución selectiva
       ↓
Más distribución cuando sea necesario
```

Un sistema puede permanecer mayoritariamente en un único proceso mientras solo los use cases que justifican una estrategia diferente se distribuyen. No es necesario anticipar qué partes de la aplicación necesitarán escalar, aislarse o procesarse de manera diferente en el futuro.

Esto puede ser particularmente interesante cuando workloads muy diferentes coexisten dentro del mismo producto. Una funcionalidad de IA, por ejemplo, puede tener requisitos de procesamiento, latencia y coste completamente diferentes de una operación tradicional de CRUD. No existe necesariamente una razón para que ambos utilicen la misma estrategia de ejecución solo porque pertenecen al mismo módulo.

La funcionalidad de IA podría utilizar una infraestructura específica y escalar de manera independiente, mientras que los demás use cases continuarían utilizando una infraestructura convencional.

En el fondo, la ventaja no es simplemente poder escalar con mayor granularidad. Es evitar que la necesidad de un workload determine la infraestructura de los demás. Pero esta flexibilidad no elimina la complejidad. Permite introducirla de forma selectiva.

Cuando un use case pasa a ejecutarse fuera del proceso principal, aparecen los problemas conocidos de los sistemas distribuidos: latencia, timeouts, retries, observabilidad, idempotencia y fallos parciales. La diferencia es que estos costes no tienen que ser asumidos por toda la aplicación. Si diez use cases pueden continuar ejecutándose dentro de una aplicación convencional, no existe necesariamente una razón para distribuirlos. Si un undécimo presenta una necesidad diferente de escalado o procesamiento, podemos distribuir solo ese use case. La propuesta, por tanto, no consiste en crear microservicios más pequeños. Consiste en permitir que la distribución sea una decisión local, tomada cuando exista un beneficio concreto.

También existe un coste relacionado con las dependencias. Cuando un módulo utiliza otro como biblioteca, un cambio incompatible en esa dependencia exige que los consumidores sean actualizados, recompilados y probados. Esto reduce parte de la independencia de deployment que se obtendría con servicios completamente separados. Por otro lado, mientras la dependencia permanezca dentro del mismo proceso, no necesitamos pagar el coste de una comunicación remota por cada interacción entre módulos. `Orders` puede utilizar `Customers` directamente como biblioteca, sin transformar esta dependencia en una llamada HTTP solo porque los módulos tengan fronteras diferentes.

```
Orders ───────► Customers
   │
   └──────────► Pricing
                  │
                  ▼
               Products
```

Este punto hace que el grafo de dependencias sea especialmente importante. Las dependencias entre módulos necesitan tener una dirección clara y evitar ciclos. Si `Orders` depende de `Customers` y `Customers` depende de `Orders`, distribuirlos por separado puede simplemente transformar un acoplamiento de código en un acoplamiento de red.

La distribución de un use case tampoco implica la distribución de todas sus dependencias. Si `Orders.GetOrder` utiliza `Customers.GetCustomer`, por ejemplo, esta llamada puede seguir realizándose directamente mediante la biblioteca de `Customers`.

```
Orders.GetOrder
      │
      └──► Customers.GetCustomer
                │
                └──► Repository
```

En este escenario, solo la ejecución de `Orders.GetOrder` fue distribuida. `Customers` continúa siendo una dependencia in-process. Una nueva frontera distribuida solo aparece cuando existe una decisión explícita de ejecutar `Customers` por separado.

Este es un aspecto importante de la propuesta: la distribución no tiene por qué seguir las fronteras de los módulos. Un use case puede distribuirse sin que todos los módulos de los que depende también se transformen en servicios.

También existe un coste relacionado con la propia granularidad del procesamiento. Separar use cases permite escalar cada workload individualmente, pero también puede significar replicar el runtime y las dependencias del módulo en varias unidades de ejecución. Una function o container puede necesitar cargar las mismas bibliotecas utilizadas por otros use cases, aumentando el consumo de memoria, el tiempo de inicialización y, dependiendo del workload, el coste total de procesamiento. La granularidad menor, por tanto, no es gratuita. Necesita aportar un beneficio suficiente para compensar esta duplicación.

Otro límite importante está en los recursos compartidos. La posibilidad de escalar `GetOrder` de forma independiente no significa que la base de datos pueda acompañar esta expansión. PostgreSQL, colas, caches y servicios externos pueden seguir siendo cuellos de botella.

La propuesta aumenta la granularidad con la que podemos escalar el procesamiento, pero no elimina los límites de los componentes de los que depende este procesamiento. Si la base de datos es el cuello de botella, simplemente aumentar la cantidad de functions puede empeorar el problema. Por eso, la idea no es que cada use case pueda escalar indefinidamente de forma independiente. Es que, cuando exista capacidad disponible en los recursos de los que depende, no sea necesario escalar junto aquello que no participa de ese workload.

También existe una consecuencia operativa. Un sistema con diferentes estrategias de ejecución tendrá más deployments, configuraciones, permisos, observabilidad y recursos de infraestructura que un monolito convencional. La propuesta no elimina este coste. Lo que intenta hacer es evitar que se introduzca antes de que exista una necesidad concreta. Este quizá sea el principal trade-off de la arquitectura: ganar flexibilidad y granularidad a costa de cierta complejidad operativa adicional.

Por tanto, la pregunta no debería ser si esta arquitectura es más simple que un monolito o que los microservicios. Probablemente no lo sea. La pregunta es si la complejidad adicional aparece únicamente allí donde existe una necesidad que la justifique.

## Qué es esta arquitectura y cuándo tiene sentido

No llamaría microservicios a esta propuesta. No porque una arquitectura modular distribuida sea incompatible con los microservicios, sino porque la unidad arquitectónica propuesta es diferente. En los microservicios, el servicio normalmente concentra decisiones de modularidad, deployment, ownership, operación y escalado. Aquí, estas decisiones están deliberadamente separadas.

El módulo continúa siendo la unidad de desarrollo y evolución. Los use cases continúan perteneciendo a ese módulo y pueden compartir código, reglas de negocio, dependencias y pruebas. La diferencia es que un use case puede, cuando sea necesario, tener su propia estrategia de ejecución y escalado.

Esto significa que un módulo puede permanecer íntegramente dentro de una aplicación convencional durante toda la vida del producto. Otro puede tener solo un use case ejecutándose como function. Un tercero puede utilizar procesamiento asíncrono para una operación específica. La distribución no es el objetivo de la arquitectura; es una posibilidad que puede utilizarse cuando exista una razón concreta.

Por eso, prefiero llamar a esta idea arquitectura modular distribuida. No pretende ser una versión simplificada de los microservicios, ni una etapa obligatoria entre el monolito modular y una arquitectura de servicios. La propuesta es explorar si podemos separar dos decisiones que normalmente terminan tomándose juntas: cómo organizamos y desarrollamos el software y cómo provisionamos y escalamos su procesamiento.

Esto también significa que no considero esta arquitectura adecuada para cualquier sistema. Si una aplicación es pequeña, tiene una carga previsible y una infraestructura convencional resuelve el problema con holgura, introducir esta granularidad puede simplemente añadir complejidad sin producir un beneficio proporcional.

Del mismo modo, los sistemas con requisitos muy específicos de seguridad, disponibilidad, gobernanza, auditoría, aislamiento o consistencia pueden requerir otras decisiones arquitectónicas. La propuesta de este artículo parte de un contexto más específico: startups en etapa inicial, con equipos pequeños, presupuesto limitado y workloads que pueden crecer de manera bastante desigual.

Incluso en este escenario, existe un límite importante. Distribuir el procesamiento no elimina los recursos compartidos. Si varios use cases dependen de la misma base de datos y esta se convierte en el cuello de botella, aumentar la cantidad de functions no resuelve el problema. Incluso puede aumentar la presión sobre el recurso ya saturado. La arquitectura permite escalar el procesamiento con mayor granularidad, pero no elimina los límites de los componentes de los que depende este procesamiento.

Por eso, veo este enfoque principalmente como una hipótesis para un determinado contexto, y no como una recomendación universal. Parece tener más sentido cuando existe una combinación de equipo pequeño, demanda inicialmente baja o variable y una expectativa de que diferentes partes del producto puedan crecer a velocidades muy diferentes.

En estas condiciones, la posibilidad de elegir la estrategia de procesamiento por use case puede permitir que la infraestructura acompañe el comportamiento real del producto, sin exigir que la startup asuma anticipadamente toda la capacidad o complejidad operativa que quizá solo sea necesaria en el futuro.

Al final, la propuesta no consiste en elegir entre monolito modular y microservicios. Consiste en cuestionar si necesitamos elegir una única unidad de ejecución para todo el sistema. Quizá sea posible mantener la simplicidad del desarrollo modular y, al mismo tiempo, distribuir solo aquello que realmente necesite ser distribuido.

## ¿Cómo sabría si la arquitectura funcionó?

Es importante dejar claro que este artículo presenta una propuesta arquitectónica, no una arquitectura validada empíricamente. No tuve la oportunidad de implementar este modelo en una startup real y acompañar su evolución a lo largo de los años. Por lo tanto, no tengo datos para afirmar que necesariamente reduzca costes, simplifique la evolución del sistema o produzca una mejor experiencia para un equipo de desarrollo.

Lo que tengo es una experiencia anterior que me llevó a identificar un posible espacio entre el monolito modular y los microservicios: por un lado, la importancia de mantener el desarrollo simple y modular; por otro, la posibilidad de que diferentes partes de un producto tengan necesidades muy diferentes de procesamiento e infraestructura.

Para mí, la propuesta solo tendría sentido si esta separación entre desarrollo y procesamiento aportara beneficios reales sin crear una complejidad mayor que aquella que pretende evitar. Una de las primeras señales sería la capacidad de mantener los módulos relativamente simples incluso cuando algunos de sus use cases pasaran a ejecutarse de maneras diferentes. El equipo debería poder desarrollar y probar el módulo sin tener que transformar cada diferencia de infraestructura en una preocupación del código. Al mismo tiempo, un use case debería poder adquirir su propia estrategia de ejecución o escalado sin exigir que todo el módulo acompañara ese cambio.

Otra señal sería la evolución del sistema. Si la aplicación pudiera comenzar de forma simple, permanecer mayoritariamente en un único proceso y distribuir solo algunos use cases a medida que surgieran necesidades concretas, esto sería una evidencia de que la arquitectura está cumpliendo una de sus principales propuestas: permitir que la complejidad se introduzca de forma gradual, en lugar de anticiparla.

Las dependencias también serían importantes. La arquitectura debería permitir que los módulos siguieran utilizando bibliotecas directamente cuando fuera adecuado, sin transformar toda frontera modular en una llamada de red. Si, para distribuir un único use case, fuera necesario transformar una gran parte de las dependencias en servicios independientes, esto sería una señal de que la granularidad propuesta quizá esté creando más acoplamiento del que elimina.

El aspecto económico sería otro punto que observar. La granularidad adicional debería, en algunos workloads, permitir que los recursos acompañaran mejor la utilización real. Pero esta cuenta no podría considerar únicamente el coste de procesamiento. Sería necesario incluir observabilidad, deployments, infraestructura, mantenimiento y el tiempo del propio equipo. Si el ahorro obtenido mediante el procesamiento bajo demanda fuera menor que el coste adicional de operar la arquitectura, la propuesta no estaría cumpliendo su objetivo.

Por último, observaría qué ocurre a medida que la empresa crece. Si, después de alcanzar una escala mayor, fuera necesario reescribir los módulos, sustituir sistemáticamente las dependencias por APIs o migrar obligatoriamente a microservicios para recuperar propiedades importantes, esto sería una señal de que la arquitectura simplemente pospuso el problema. Por otro lado, si el sistema pudiera evolucionar gradualmente, distribuyendo solo aquello que realmente justificara la distribución, tendríamos una evidencia más interesante de que el enfoque funciona.

Aun así, existe una posibilidad importante: quizá el resultado del experimento sea descubrir que esta arquitectura no ofrece una ventaja suficiente sobre un monolito modular tradicional. Y eso también sería un resultado válido.

La propuesta, por tanto, no parte de la certeza de haber encontrado una arquitectura mejor. Parte de una hipótesis: quizá exista una forma de preservar la simplicidad del desarrollo modular sin obligar a todo el sistema a compartir la misma estrategia de procesamiento.

## Una arquitectura que debe probarse

Quizá este enfoque no funcione tan bien como imagino. La complejidad operativa puede aparecer demasiado pronto. A medida que la organización crezca, determinadas características del sistema pueden hacer que los microservicios sean una elección más adecuada. Y, en muchos casos, el propio monolito modular puede seguir siendo la mejor respuesta.

Esto no contradice la propuesta. La arquitectura fue pensada para un contexto específico: startups en etapa inicial, con equipos pequeños, recursos limitados y workloads que pueden presentar diferencias significativas de demanda. Fuera de este contexto, los trade-offs pueden ser completamente diferentes.

La idea tampoco es eliminar los microservicios. Si una organización llega a un punto en el que el aislamiento, el ownership, los ciclos de deployment independientes u otras propiedades de una arquitectura distribuida se vuelven más importantes que la simplicidad inicial, los microservicios pueden ser una evolución perfectamente razonable. Del mismo modo, si la aplicación permanece pequeña y previsible, puede no existir ninguna razón para abandonar el monolito modular.

La propuesta es más específica: comenzar con una arquitectura modular simple y mantener la libertad de distribuir solo aquello que realmente necesite ser distribuido. Si esto funciona, una startup podrá posponer tanto decisiones de infraestructura como parte de la complejidad operativa hasta que exista una razón concreta para asumirlas. No estoy proponiendo un sustituto para los microservicios. Estoy proponiendo una alternativa como punto de partida.

La arquitectura modular distribuida es, al final, una idea que me gustaría poner en práctica. Todavía no sé dónde están sus límites, ni si los beneficios serán suficientes para compensar los costes. Pero creo que existe una pregunta suficientemente interesante como para justificar el experimento: ¿podemos mantener la simplicidad del desarrollo modular y, al mismo tiempo, permitir que el procesamiento sea provisionado con la granularidad de los use cases que realmente lo necesitan?
