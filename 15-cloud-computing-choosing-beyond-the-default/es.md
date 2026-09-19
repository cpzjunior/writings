# Computación en la nube: eligiendo más allá del default

_Un mapa de las principales clouds, sus puntos fuertes, equivalencias y los trade-offs entre simplicidad, portabilidad, costo y resiliencia._

**Resumen:** Defiendo que elegir una cloud no debería ser una decisión basada en familiaridad o en el tamaño del proveedor, sino en las características concretas de cada workload. Las equivalencias entre plataformas ayudan a orientar la comparación, pero no eliminan diferencias de costo, operación, servicios, hardware, compliance y lock-in. Single-cloud y multi-cloud tampoco son posiciones ideológicas: cada una trae costos, beneficios y riesgos que deben evaluarse junto con las dependencias reales de la arquitectura. Al final, la mejor elección es aquella que equilibra lo que el workload exige con el costo de implementar, operar y eventualmente cambiar esa arquitectura.

---

Históricamente, siempre tuve una preferencia bastante clara por AWS. No necesariamente porque considere AWS la mejor cloud en cualquier escenario, sino porque fue la plataforma con la que tuve más contacto y familiaridad. A lo largo del tiempo, fui acostumbrándome a sus servicios, su organización, su documentación y su ecosistema. Y existe una consecuencia bastante natural de eso: cuando conoces bien una tecnología, tiende a parecerte la opción más simple para el próximo problema.

En los últimos años, sin embargo, comencé a mirar otras clouds con más atención. Uno de los principales motivos fue bastante pragmático: GPUs. A medida que los proyectos de inteligencia artificial comenzaron a exigir cada vez más capacidad computacional, empecé a percibir que la familiaridad con una plataforma ya no podía ser el principal criterio para decidir dónde ejecutar un workload. El precio, la disponibilidad de GPUs, la ubicación de los recursos, la capacidad de expansión e incluso los modelos de contratación pasaron a tener un peso mucho mayor en la decisión.

Esto me hizo volver a mirar un mercado que, aunque frecuentemente se resume en la disputa entre AWS, Azure y Google Cloud, es mucho más amplio. Existen clouds especializadas, proveedores regionales, plataformas con propuestas deliberadamente más simples y empresas que consiguen ser extremadamente competitivas en determinados tipos de workload precisamente porque no intentan ofrecer todo para todos.

El objetivo de este texto no es hacer una comparación exhaustiva entre cientos de servicios o declarar cuál es la mejor cloud. La idea es construir un mapa suficientemente amplio para entender quiénes son los principales players, cuáles son sus puntos fuertes, qué servicios poseen equivalentes entre sí y, principalmente, en qué situaciones vale la pena salir del camino más obvio.

Elegir una cloud por familiaridad es perfectamente razonable. Elegir una cloud sin conocer las alternativas, no.

## El mapa de las clouds

Cuando hablamos de cloud computing, tres nombres inevitablemente aparecen primero: AWS, Microsoft Azure y Google Cloud. Continúan siendo las principales plataformas generalistas del mercado de public cloud, con una amplitud que va mucho más allá de máquinas virtuales y almacenamiento. Computación, bases de datos, redes, containers, Kubernetes, serverless, analytics, inteligencia artificial, seguridad, observabilidad y una cantidad cada vez mayor de servicios administrados forman parte de este ecosistema.

Existe una razón para que estas tres dominen la conversación. No son solamente proveedores de infraestructura, sino plataformas completas. Una aplicación puede utilizar computación, almacenamiento, base de datos, colas, identidad, observabilidad, gestión de secretos, CDN y servicios de inteligencia artificial del mismo proveedor, todos integrados entre sí. Esta integración es una de las grandes ventajas de las hyperscalers y también uno de los factores que hacen que una eventual migración sea más compleja.

Pero el mercado de cloud no es una jerarquía simple. Existen proveedores con propuestas diferentes y, dependiendo del workload, un proveedor que parece pequeño cuando se lo compara con una hyperscaler puede ser una opción mucho más interesante.

Oracle Cloud Infrastructure, IBM Cloud, Alibaba Cloud y Tencent Cloud son ejemplos de proveedores que poseen posiciones particularmente fuertes en determinados mercados y ecosistemas. OCI tiene una relación natural con entornos que dependen fuertemente de Oracle. IBM mantiene una presencia importante en grandes organizaciones y en el ecosistema Red Hat. Alibaba y Tencent poseen una relevancia mucho mayor cuando consideramos China y otros mercados asiáticos. En estos casos, la pregunta no es necesariamente qué proveedor ofrece más servicios, sino cuál posee mayor adecuación al problema que necesita resolverse.

Existe además un grupo de proveedores que adopta una propuesta deliberadamente más simple. DigitalOcean, Hetzner, OVHcloud, Scaleway y Akamai, a través de Linode, pueden ser interesantes cuando el objetivo es obtener computación, almacenamiento y red sin necesariamente depender de la enorme cantidad de servicios administrados ofrecidos por las hyperscalers. Para determinados workloads, esta simplicidad puede significar menor complejidad operativa y costos más previsibles.

La inteligencia artificial, sin embargo, está alterando este escenario. El crecimiento de la demanda de GPUs creó un mercado en el que la disponibilidad y el costo del hardware pueden ser más importantes que la cantidad de servicios ofrecidos por la plataforma. Una aplicación de IA que necesita cientos de GPUs no necesariamente se beneficia de estar en el proveedor que ofrece el mayor catálogo de servicios. En este escenario, precio por GPU, disponibilidad, arquitectura de los aceleradores, interconexión entre máquinas, capacidad de escalar y ubicación de los recursos pueden ser los factores determinantes.

Esto abrió espacio para proveedores especializados. CoreWeave es uno de los ejemplos más conocidos, habiendo construido su plataforma alrededor de workloads de GPU e inteligencia artificial. También existen otros proveedores especializados en GPU y computación de alto rendimiento que pueden ser muy competitivos para este tipo de carga, incluso sin ofrecer una plataforma generalista comparable a las hyperscalers.

Al mismo tiempo, las propias hyperscalers están invirtiendo fuertemente en hardware especializado, modelos fundacionales, servicios administrados de IA e integración de estos recursos con el resto de sus plataformas. Esto crea una competencia diferente de la que existía en el mercado tradicional de cloud. La ventaja puede estar tanto en la infraestructura como en el ecosistema construido alrededor de ella.

En la práctica, esto significa que no existe un único perfil de cloud que sea adecuado para todos los workloads. Las plataformas generalistas continúan siendo extremadamente relevantes, pero los proveedores especializados pueden ser más competitivos en determinadas situaciones. Una empresa puede ser una excelente elección para infraestructura tradicional y una mala elección para entrenamiento de modelos. Otra puede ser poco interesante como plataforma principal, pero extremadamente competitiva para un workload específico de GPU.

Este es precisamente uno de los motivos por los que vale la pena mirar más allá del default. La cloud elegida para una aplicación no necesariamente tiene que ser la misma elegida para todos los workloads de la organización. Un proveedor que históricamente parece pequeño o secundario puede convertirse en una alternativa relevante cuando cambiamos la pregunta de “¿cuál es la mejor cloud?” a “¿cuál es la mejor infraestructura para este workload?”.

Al final, AWS, Azure y Google Cloud continúan siendo las principales plataformas generalistas, pero el tamaño y la cantidad de servicios no son los únicos criterios relevantes. El mercado se está volviendo más especializado, y la inteligencia artificial está acelerando este proceso. Conocer este escenario significa entender dónde las grandes plataformas son más fuertes, dónde los proveedores más pequeños consiguen competir y en qué situaciones tiene sentido considerar alternativas que normalmente ni siquiera aparecerían en la primera búsqueda.

## Equivalencia no significa igualdad

Una de las primeras cosas que alguien percibe al estudiar diferentes clouds es que los grandes proveedores poseen equivalentes para buena parte de los servicios fundamentales. En el nivel de computación, podemos pensar en EC2 en AWS, Virtual Machines en Azure y Compute Engine en Google Cloud. Para object storage, tenemos S3, Blob Storage y Cloud Storage. Para redes virtuales, VPC en AWS, Virtual Network en Azure y VPC en Google Cloud. Para Kubernetes administrado, EKS, AKS y GKE. Para container registry, ECR, Azure Container Registry y Artifact Registry. Para balanceo de carga, Elastic Load Balancing, Azure Load Balancer y Cloud Load Balancing. Para CDN, CloudFront, Azure Front Door y Cloud CDN. Los nombres cambian, pero los conceptos fundamentales son bastante similares.

Lo mismo ocurre con los servicios de datos. Para bases de datos relacionales administradas, AWS posee RDS, mientras que Azure y Google Cloud ofrecen familias de servicios como Azure Database for PostgreSQL y MySQL y Cloud SQL. En el mundo NoSQL, tenemos DynamoDB, Cosmos DB y Firestore. Para data warehouses, Redshift, Synapse y BigQuery. Para almacenamiento de archivos, EFS, Azure Files y Filestore. Para mensajería, podemos encontrar SQS, Azure Service Bus y Pub/Sub. Incluso los servicios de identidad, gestión de secretos y observabilidad poseen equivalentes claros: IAM, Entra ID y Cloud IAM; Secrets Manager, Key Vault y Secret Manager; CloudWatch, Azure Monitor y Cloud Monitoring.

Esta correspondencia también aparece en las arquitecturas más modernas. Lambda, Azure Functions y Cloud Run functions atienden modelos de ejecución serverless, mientras que Fargate, Azure Container Apps y Cloud Run permiten ejecutar containers sin necesidad de administrar directamente las máquinas virtuales. Para infraestructura como código, tenemos CloudFormation en AWS y ARM Templates y Bicep en el ecosistema Microsoft, mientras que herramientas independientes como Terraform permiten trabajar con diferentes proveedores utilizando un enfoque común.

Incluso la inteligencia artificial ya posee un conjunto relativamente claro de equivalencias. SageMaker, Azure Machine Learning y Vertex AI ofrecen plataformas para desarrollo y operación de workloads de machine learning. Bedrock, Azure AI Foundry y Vertex AI ofrecen diferentes caminos para consumir modelos y construir aplicaciones de inteligencia artificial. Sin embargo, aquí las diferencias comienzan a ser particularmente importantes, porque los modelos disponibles, aceleradores, APIs, herramientas de entrenamiento, servicios administrados e integraciones con el resto de la plataforma varían bastante entre los proveedores.

Este paralelismo es útil porque permite construir un vocabulario común para comparar plataformas. Quien conoce AWS puede identificar rápidamente dónde buscar conceptos similares en Azure o Google Cloud. Esto reduce bastante la barrera inicial para aprender una nueva plataforma y también hace posible transportar parte del conocimiento arquitectónico de una cloud a otra.

Pero existe una trampa en esta comparación. El hecho de que dos servicios resuelvan problemas similares no significa que sean equivalentes en comportamiento, arquitectura o experiencia operativa. Un object storage continúa siendo object storage, pero los mecanismos de control de acceso, integración con otros servicios, consistencia, cuotas, precios, replicación y políticas de ciclo de vida pueden ser diferentes. Lo mismo ocurre con bases de datos, servicios de mensajería, Kubernetes y prácticamente cualquier otra categoría.

Las diferencias son aún mayores cuando subimos el nivel de abstracción. Una base de datos relacional administrada puede parecer simplemente una base de datos relacional administrada, pero los engines disponibles, extensiones soportadas, mecanismos de replicación, opciones de alta disponibilidad, backups, integración con analytics y herramientas de migración pueden cambiar completamente la decisión. De la misma manera, dos plataformas pueden ofrecer Kubernetes administrado, pero tener diferencias significativas en la integración con red, identidad, storage, observabilidad y servicios propietarios.

Existe además una diferencia más importante: cada cloud posee servicios que no tienen un equivalente directo en las demás. Y es precisamente en esos servicios donde muchas veces se encuentra una parte significativa del valor de una plataforma. Si todas las clouds ofrecen máquinas virtuales, object storage y Kubernetes, estos recursos son relativamente fáciles de comparar. Ya servicios como DynamoDB, BigQuery, Cosmos DB o Cloud Run representan decisiones arquitectónicas más específicas y pueden crear dependencias mucho mayores respecto del proveedor.

La inteligencia artificial hace este punto aún más evidente. Las grandes clouds ofrecen servicios similares para entrenamiento, inferencia y consumo de modelos, pero la combinación entre modelos propios y de terceros, GPUs y otros aceleradores, APIs, herramientas de desarrollo, data pipelines, bases de datos vectoriales y servicios administrados puede ser bastante diferente. Además, no siempre determinado modelo o hardware está disponible en la misma región, por el mismo precio o con la misma capacidad en todos los proveedores.

Por eso, una matriz de equivalencias es un excelente punto de partida para comparar clouds, pero no debería utilizarse como una prueba de que son intercambiables. Ayuda a responder “¿dónde encuentro algo parecido a lo que ya conozco?”, pero no necesariamente “¿qué plataforma es mejor para lo que estoy intentando construir?”.

Conocer las equivalencias reduce el costo de aprender una nueva cloud. Conocer las diferencias es lo que permite elegir entre ellas.

## Single cloud, multi-cloud y el costo de la simplicidad

Existe un argumento bastante fuerte a favor de elegir una única cloud: simplicidad. Operar una infraestructura completa dentro de una misma plataforma reduce la cantidad de conceptos que necesitan dominarse, las integraciones que necesitan mantenerse y las diferencias de comportamiento que deben considerarse. IAM, networking, observabilidad, billing, políticas de seguridad, deployment y troubleshooting pueden seguir un conjunto relativamente consistente de patrones. El equipo también puede concentrar conocimiento, automatización y procesos operativos en una única plataforma.

Para un equipo pequeño o para una organización que no posee una necesidad concreta de multi-cloud, esta simplicidad tiene un valor enorme. No es solamente una cuestión de productividad. Cada tecnología adicional exige conocimiento, procesos, monitoreo, automatización y capacidad de troubleshooting. Una segunda cloud significa aprender una segunda forma de hacer muchas de las mismas cosas, además de lidiar con las diferencias entre ellas.

Herramientas como Terraform reducen bastante este problema. Es posible declarar infraestructura de diferentes proveedores utilizando un mismo lenguaje y, en muchos casos, reutilizar módulos, pipelines y prácticas operativas. Esto hace que una estrategia multi-cloud sea mucho más viable de lo que sería si cada proveedor exigiera un stack completamente independiente. Pero Terraform no transforma AWS, Azure y Google Cloud en plataformas intercambiables. Abstrae la forma de declarar infraestructura, no necesariamente la arquitectura que está siendo declarada.

Un recurso creado en Terraform continúa siendo un recurso específico de determinado proveedor. Una VPC continúa teniendo las características de AWS, una Virtual Network continúa teniendo las características de Azure y una VPC de Google Cloud posee sus propias particularidades. El código puede incluso parecer similar, pero el comportamiento de los recursos, sus limitaciones y sus integraciones continúan perteneciendo a la plataforma.

Este problema se hace particularmente evidente cuando aparecen servicios nuevos. Los proveedores de cloud lanzan constantemente productos que explotan características específicas de sus propias plataformas. Existe naturalmente un intervalo entre el lanzamiento de un servicio y la existencia de soporte maduro para él en las herramientas de infraestructura como código. Incluso cuando el soporte existe, no siempre todas las funcionalidades del servicio se exponen de la misma manera.

Existe además una cuestión más sutil. Cuanto más una arquitectura intenta ser portable, mayor tiende a ser la presión para utilizar únicamente recursos que posean equivalentes razonablemente próximos en todos los proveedores. Esto puede ser una decisión consciente y perfectamente válida, pero significa renunciar a parte del diferencial ofrecido por cada plataforma.

Si decides utilizar únicamente servicios que pueden encontrarse en AWS, Azure y Google Cloud, aumentas la portabilidad de la aplicación. Pero también puedes dejar de utilizar servicios que harían esa aplicación más simple, más barata o más eficiente dentro de una determinada cloud.

Este es uno de los grandes trade-offs de la portabilidad. No es gratuita. Es perfectamente posible construir una aplicación que funcione en AWS, Azure y Google Cloud. La cuestión es cuánto valor estás dejando sobre la mesa para conseguir hacerlo.

En algunos casos, la respuesta será “ningún valor relevante”. Si la aplicación utiliza únicamente containers, PostgreSQL, object storage y algunos componentes relativamente estandarizados, la portabilidad puede ser una propiedad bastante razonable. En otros, la respuesta puede ser muy diferente. Una aplicación que depende profundamente de servicios propietarios de una cloud puede obtener enormes beneficios en simplicidad, performance o costo precisamente por aceptar cierto nivel de lock-in.

La discusión sobre utilizar una o varias clouds suele presentarse como una elección entre simplicidad y resiliencia. En la práctica, es un poco más complicada. Una única cloud puede concentrar riesgos. Si una falla significativa afecta al proveedor, una parte importante de la infraestructura puede quedar indisponible simultáneamente. Es posible reducir ese riesgo utilizando múltiples regiones, zonas de disponibilidad y mecanismos adecuados de disaster recovery, pero existe un límite respecto de cuánto podemos protegernos contra una falla que supere la frontera de una región o incluso de la propia plataforma.

Por otro lado, distribuir workloads entre diferentes proveedores aumenta la cantidad de componentes e integraciones que deben operarse. Pasamos a lidiar con diferentes modelos de red, identidad, seguridad, observabilidad, deployment y gestión de costos. La arquitectura puede ganar independencia en algunas dimensiones y perder simplicidad en otras.

Multi-cloud, por lo tanto, no significa automáticamente mayor disponibilidad. Es posible tener una aplicación distribuida entre AWS y Azure y aun así poseer un punto único de falla. Puede estar en el DNS, en el proveedor de identidad, en la CDN, en la conectividad, en la observabilidad, en un SaaS utilizado por ambas arquitecturas o en cualquier otra dependencia compartida.

Este es un punto que considero particularmente importante: diversidad de proveedores no es necesariamente diversidad de dependencias. Imagina una aplicación cuyo backend está distribuido entre AWS y Azure, pero que utiliza el mismo proveedor de DNS, la misma CDN y el mismo servicio de identidad. Desde el punto de vista del compute, existen dos proveedores. Desde el punto de vista del camino crítico de la aplicación, quizá no existan. Si una de esas dependencias compartidas falla, tener dos clouds puede no hacer ninguna diferencia.

El caso de Cloudflare es un buen ejemplo para ilustrar este problema. En junio de 2022, un cambio de configuración en la red de la empresa provocó una indisponibilidad que afectó a diversos servicios que dependían de su infraestructura. El punto interesante para una arquitectura multi-cloud no es simplemente que un proveedor haya quedado indisponible, sino que una dependencia ubicada en una capa transversal puede afectar a aplicaciones independientemente de dónde esté alojado su compute.

Este tipo de dependencia es fácil de ignorar porque normalmente no aparece cuando miramos únicamente el diagrama principal de la infraestructura. Podemos dibujar AWS de un lado y Azure del otro y concluir que tenemos redundancia. Pero, si ambos dependen del mismo DNS, de la misma CDN, del mismo proveedor de identidad o de cualquier otro componente crítico, existe una dependencia común oculta entre ellos.

Esto también ayuda a poner el concepto de resiliencia en una perspectiva más realista. Multi-cloud puede reducir determinados riesgos, pero no elimina el riesgo. En algunos casos, simplemente desplaza el punto en el que aparece el riesgo.

La pregunta, por lo tanto, no debería ser únicamente si la aplicación está distribuida entre más de una cloud, sino si sus dependencias críticas también lo están. Para evaluar la resiliencia de una arquitectura, es necesario mirar toda la cadena de dependencias, incluyendo DNS, identidad, CDN, conectividad, observabilidad y servicios externos, y no solamente dónde están ejecutándose los containers o las máquinas virtuales.

Existe además otro aspecto importante: multi-cloud puede adoptarse por motivos que no tienen relación directa con la disponibilidad. Negociación comercial, requisitos regulatorios, ubicación de datos, disponibilidad de determinados servicios, capacidad de GPU y diferencias de costo pueden ser razones suficientes para utilizar más de un proveedor.

De la misma manera, una estrategia single-cloud puede ser perfectamente defendible cuando la simplicidad operativa tiene más valor que la independencia adicional. Una única cloud, distribuida adecuadamente entre regiones y zonas, puede ofrecer un nivel de resiliencia suficiente para muchos workloads.

Single-cloud y multi-cloud no deberían tratarse como posiciones ideológicas. Son estrategias arquitectónicas diferentes, con costos, beneficios y riesgos diferentes. La elección debería partir del riesgo que queremos reducir, del workload que estamos intentando ejecutar y de la complejidad que estamos dispuestos a asumir para alcanzar ese objetivo.

## El diferencial de las clouds más pequeñas

Es precisamente aquí donde vale la pena ampliar el mapa. Las hyperscalers poseen una ventaja evidente cuando necesitamos una plataforma extremadamente completa, con decenas o cientos de servicios integrados. Pero esa amplitud también puede ser irrelevante para determinados workloads.

Una aplicación que necesita esencialmente máquinas virtuales, almacenamiento, red y quizás Kubernetes no necesariamente necesita toda la complejidad ofrecida por AWS, Azure o Google Cloud. En este escenario, proveedores como Hetzner, OVHcloud, DigitalOcean, Scaleway o Akamai pueden entrar en el análisis. La propuesta de estas empresas no es necesariamente competir con las hyperscalers en cantidad de servicios, sino ofrecer determinados recursos de infraestructura de manera más simple y, en algunos casos, con una estructura de costos más competitiva.

Existe además una categoría diferente de alternativa: plataformas que abstraen aún más la infraestructura. Heroku, Render y Railway son ejemplos de plataformas en las que el desarrollador puede concentrarse en la aplicación sin necesidad de administrar directamente buena parte de los componentes de infraestructura que existirían en un enfoque tradicional. Para determinados proyectos, esta abstracción puede valer más que el acceso a un catálogo gigantesco de servicios.

Esta diferencia puede ser bastante relevante. Si una aplicación utiliza apenas una fracción de los servicios disponibles en una hyperscaler, existe un punto en el que la capacidad adicional deja de representar valor y pasa a representar solamente complejidad. Para determinados workloads, tener una máquina virtual predecible, una red simple y almacenamiento adecuado puede ser más importante que tener cientos de servicios administrados disponibles. Para otros, puede tener sentido subir aún más el nivel de abstracción y utilizar una plataforma que oculte buena parte de esa infraestructura.

El mismo razonamiento vale para workloads específicos. Si el principal recurso necesario es GPU, la pregunta puede dejar de ser “¿cuál es mi cloud estándar?” y pasar a ser “¿quién ofrece la GPU que necesito, en la cantidad que necesito, por el costo que puedo pagar?”. En este escenario, disponibilidad de hardware, precio por hora, capacidad de expansión, ubicación y características de la infraestructura pueden ser mucho más relevantes que la cantidad de servicios disponibles en la plataforma.

Es en este tipo de situación donde una preferencia histórica por determinada cloud comienza a perder importancia. La familiaridad continúa teniendo valor, pero pasa a competir con criterios objetivos del workload. Una plataforma que nunca utilicé puede ser una mejor elección para determinado proyecto simplemente porque ofrece el recurso necesario en condiciones significativamente mejores.

Existe además una ventaja importante: una cloud más pequeña o una plataforma especializada no tiene que ser un sustituto completo de la cloud principal. Puede ser simplemente una pieza de la arquitectura. Un workload específico puede tener más sentido en otro proveedor mientras el resto de la organización permanece en una única plataforma.

Esto permite un enfoque intermedio entre single-cloud y multi-cloud. En lugar de intentar construir una aplicación completamente portable entre varias plataformas, podemos aceptar que la mayor parte de la infraestructura esté en una cloud principal y utilizar otros proveedores únicamente cuando exista una ventaja concreta.

Este enfoque también cambia la forma en que pensamos sobre multi-cloud. No es necesario distribuir toda la aplicación entre varios proveedores para obtener algún beneficio de la diversidad. Podemos tener una cloud principal y, al mismo tiempo, elegir deliberadamente otro proveedor para workloads en los que sea más competitivo.

El diferencial de una cloud más pequeña no tiene que ser ofrecer más recursos que una hyperscaler. Puede ser precisamente ofrecer menos, pero ofrecer aquello que el workload realmente necesita de una manera más simple, más barata o más especializada.

## El problema del lock-in

Toda discusión sobre clouds inevitablemente llega al lock-in. Existe una percepción de que utilizar únicamente servicios básicos, como máquinas virtuales, containers y storage, hace que una arquitectura sea más portable. En parte esto es verdad. Cuanto más específica es una dependencia de un proveedor, mayor tiende a ser el costo para sustituirla. Una aplicación basada en containers, PostgreSQL y object storage tiende a tener más opciones de migración que otra profundamente dependiente de decenas de servicios propietarios.

Pero el lock-in no es solamente una cuestión tecnológica. También existe el lock-in operativo. Una organización puede construir procesos, automatizaciones, conocimiento interno y herramientas de observabilidad profundamente integrados con una determinada plataforma. Aunque técnicamente sea posible migrar una aplicación, el costo de capacitar equipos, reconstruir pipelines, adaptar procesos y operar una nueva infraestructura puede hacer que la migración sea mucho más difícil de lo que sugiere el diagrama arquitectónico.

Existe además el lock-in económico. Los datos son un buen ejemplo. Migrar máquinas virtuales puede ser relativamente simple, pero mover grandes volúmenes de datos entre proveedores puede implicar costos de transferencia, tiempo y una ventana operativa significativa. Una arquitectura puede ser técnicamente portable y, aun así, ser económicamente muy cara de mover.

Por eso, evitar cualquier lock-in también tiene un costo. Si una cloud ofrece un servicio administrado que reduce drásticamente la complejidad operativa de una aplicación, evitar ese servicio únicamente para mantener una posibilidad futura de migración puede significar asumir hoy un costo real para evitar un costo hipotético. En algunos casos, aceptar deliberadamente una dependencia del proveedor es una decisión arquitectónica perfectamente racional.

El objetivo, por lo tanto, no debería ser eliminar completamente el lock-in. Eso probablemente sea imposible. El objetivo debería ser entenderlo. Existen dependencias que son estratégicas y otras que son fácilmente sustituibles. Existen servicios cuyo costo de migración sería gigantesco y otros que podrían ser sustituidos en semanas. Existen componentes que justifican una dependencia profunda de un proveedor y otros en los que la elección puede basarse simplemente en precio, disponibilidad o conveniencia.

También es importante entender que no todo lock-in es necesariamente malo. Si un servicio propietario ofrece una ventaja significativa de costo, performance, disponibilidad o productividad, la dependencia puede ser un precio aceptable por el beneficio obtenido. Lo importante es que esa dependencia sea una decisión consciente y no una consecuencia que solo descubrimos cuando necesitamos migrar.

Una forma útil de pensar sobre esto es preguntar, para cada dependencia importante, cuánto esfuerzo sería necesario para sustituirla, cuánto tiempo llevaría, cuánto costaría y qué partes de la arquitectura se verían afectadas. Este análisis permite entender dónde existe lock-in, por qué fue asumido y cuál sería el costo de eliminarlo. El objetivo no es evitar el lock-in a cualquier costo, sino garantizar que las dependencias de la arquitectura sean decisiones conscientes.

## El costo de implementación

Existe otro costo que suele desaparecer de las comparaciones entre clouds: el costo de implementación y operación de la propia arquitectura. Dos clouds pueden ofrecer recursos técnicamente equivalentes y precios similares, pero exigir niveles completamente diferentes de esfuerzo para poner una aplicación en producción. Una plataforma puede tener integraciones listas para determinado servicio, mientras otra exige que el equipo construya y mantenga parte de esa integración. Una puede ofrecer un servicio administrado que elimina decenas de componentes, mientras otra exige que esos componentes sean operados directamente.

Este costo no aparece únicamente en arquitecturas multi-cloud. Una arquitectura excesivamente sofisticada dentro de una única cloud también puede exigir más automatización, conocimiento y esfuerzo operativo que una solución más simple. La diferencia es que, cuando agregamos múltiples proveedores, esta complejidad tiende a aumentar porque también necesitamos lidiar con diferentes modelos de red, identidad, seguridad, observabilidad y deployment.

Cuantas más diferencias necesitamos ocultar detrás de abstracciones, mayor tiende a ser la cantidad de código, infraestructura y automatización necesaria. Terraform ayuda bastante en la capa de provisionamiento, pero no elimina las diferencias entre las plataformas. En algún momento, alguien necesita lidiar con esas diferencias.

Lo mismo ocurre con observabilidad, seguridad y operación. Una arquitectura single-cloud puede aprovechar las integraciones nativas del proveedor para centralizar logs, métricas, identidad, políticas y alertas. En una arquitectura multi-cloud, podemos necesitar crear una capa adicional para unificar esta información. Puede ser una decisión correcta, pero esa capa también necesita ser construida, monitoreada y mantenida.

Existe además el costo del conocimiento. Un equipo que opera AWS y Azure necesita conocer las particularidades de ambas plataformas. Esto no significa necesariamente tener el doble de costo, pero sí significa aumentar la superficie de conocimiento necesaria para operar la infraestructura. Lo mismo vale para procesos de troubleshooting, incident response, seguridad y gestión de cambios.

Este costo también aparece cuando llega el momento de cambiar la arquitectura. Una aplicación puede ser relativamente barata de ejecutar en una determinada configuración y exigir un esfuerzo significativo para ser adaptada a otra. El cambio puede involucrar no solo máquinas y containers, sino también datos, configuraciones, identidades, redes, pipelines, observabilidad, integraciones y procesos operativos. En muchos casos, el trabajo está precisamente en las dependencias que no aparecen en el diagrama principal de la aplicación.

Por eso, el costo de una arquitectura debería analizarse en al menos tres momentos: cuánto cuesta implementarla, cuánto cuesta operarla y cuánto cuesta cambiarla. El precio mensual de la infraestructura es solamente una de estas dimensiones.

Esto también ayuda a explicar por qué no siempre vale la pena elegir la opción técnicamente más barata. Si una alternativa reduce el costo de infraestructura, pero exige mucha más ingeniería para ser implementada y operada, el ahorro puede desaparecer rápidamente. De la misma manera, pagar más por un servicio administrado puede ser racional si el costo operativo evitado es mayor que la diferencia de precio.

## Compliance y regulación

Existe un criterio que puede eliminar una cloud de la lista de opciones incluso antes de comenzar a comparar precio o funcionalidades: compliance. Dependiendo del sector, del país y del tipo de dato procesado, una organización puede estar sujeta a requisitos específicos de seguridad, privacidad, residencia de datos, auditoría y continuidad de negocio. Bancos, aseguradoras, empresas de salud y organismos públicos, por ejemplo, normalmente poseen restricciones muy diferentes de una aplicación personal o de un producto SaaS sin datos regulados.

Las grandes clouds invierten bastante en esta área y poseen una enorme cantidad de certificaciones, estándares y mecanismos de control. También ofrecen regiones en diferentes países, recursos de cifrado, gestión de claves, logs de auditoría, controles de identidad y herramientas orientadas a requisitos regulatorios específicos. Los proveedores más pequeños también pueden cumplir determinados requisitos, pero no necesariamente tendrán la misma cobertura geográfica o el mismo conjunto de certificaciones.

Esto puede cambiar completamente la elección. Una cloud puede ser técnicamente excelente y competitiva en precio, pero dejar de ser una opción si no posee una región adecuada, determinada certificación o los controles necesarios para el workload.

También es importante separar la certificación del proveedor del cumplimiento de la aplicación. El hecho de que una cloud posea determinada certificación no significa que cualquier aplicación ejecutada en ella esté automáticamente en conformidad. La responsabilidad suele ser compartida entre el proveedor y el cliente, y la arquitectura necesita utilizar correctamente los mecanismos de seguridad, control de acceso, cifrado, logging y retención de datos disponibles.

La ubicación también merece atención. “La cloud está disponible en el país” no significa necesariamente que todos los datos y servicios utilizados por la aplicación permanecerán en ese país. Backups, logs, servicios administrados, soporte e integraciones pueden tener características diferentes. En entornos regulados, es necesario entender dónde los datos realmente se almacenan, procesan y replican.

Este es un punto en el que las clouds también pueden tener ventajas diferentes. Una hyperscaler puede ofrecer una enorme cantidad de regiones y controles, mientras que un proveedor regional puede tener una ventaja precisamente por mantener su infraestructura concentrada en determinadas jurisdicciones. Para algunos workloads, esta característica puede ser más importante que la cantidad de servicios disponibles.

Por eso, compliance no debería aparecer solamente al final del proceso de elección. Puede funcionar como un filtro inicial. Antes de comparar precio, performance o cantidad de servicios, puede ser necesario preguntar qué proveedores son efectivamente elegibles para ese workload.

En entornos regulados, la primera pregunta no es qué cloud ofrece más recursos, sino qué clouds pueden atender los requisitos del workload. A partir de ese conjunto de opciones, precio, performance, simplicidad, portabilidad y demás criterios pueden entrar en la decisión.

## Descuentos, asociaciones y free tiers

Comparar el precio de las clouds también es más complicado que mirar la tabla pública de precios. El valor efectivamente pagado por una organización puede ser bastante diferente dependiendo del volumen contratado, del compromiso asumido y de los programas comerciales disponibles.

Las grandes clouds poseen diferentes mecanismos para reducir el costo de workloads que permanecen durante determinado período o alcanzan determinado volumen. Reserved Instances, Savings Plans, committed use discounts y contratos empresariales son ejemplos de mecanismos que pueden alterar significativamente el precio final. En algunos casos, la diferencia entre el precio de lista y el precio efectivamente negociado es lo suficientemente grande como para cambiar completamente una comparación superficial entre proveedores.

También existen créditos y programas específicos para startups, proyectos de investigación, educación y empresas que están migrando o expandiendo sus workloads. Para una empresa en etapa inicial, por ejemplo, los créditos pueden reducir significativamente el costo durante los primeros meses. Pero este tipo de beneficio debe analizarse con cuidado. Un crédito inicial puede reducir drásticamente el costo de entrada sin necesariamente hacer que la plataforma sea más barata a largo plazo.

Las asociaciones también pueden pesar en esta decisión. Una organización puede ya poseer contratos, competencias, soporte especializado o beneficios comerciales asociados a determinado proveedor. En ese caso, cambiar de cloud significa renunciar no solo a una infraestructura, sino también a parte de ese ecosistema comercial. De la misma manera, una empresa puede tener una asociación con determinado proveedor que haga que una alternativa menos obvia sea mucho más competitiva.

Los free tiers entran en esta misma lógica. Son excelentes para experimentar con una plataforma, aprender sus servicios o poner en marcha proyectos pequeños sin un costo significativo. También pueden ser una forma interesante de comparar la experiencia entre proveedores antes de asumir un compromiso mayor. Pero es importante separar el costo de experimentar con una cloud del costo de operarla en producción.

Una aplicación que cabe cómodamente en el free tier puede volverse bastante cara cuando crece. Lo mismo ocurre con los créditos promocionales. Son excelentes para reducir el costo de entrada, pero no necesariamente representan el costo recurrente de la arquitectura.

También existe una trampa específica cuando comparamos clouds únicamente por el precio de un recurso aislado. Una GPU puede ser más barata en determinado proveedor, pero el costo total del workload depende también del almacenamiento, transferencia de datos, red, balanceo, observabilidad y de los demás servicios necesarios para poner esa GPU a trabajar. Lo mismo vale para cualquier otro recurso.

Por eso, cuando hablamos del costo de cloud, el número más importante no es necesariamente el precio de una instancia o de una GPU. Es el costo total de ejecutar ese workload.

Esto es especialmente importante porque las condiciones comerciales pueden cambiar el análisis de forma significativa. Una cloud puede parecer más cara en el precio de lista y volverse competitiva después de descuentos, créditos y contratos empresariales. De la misma manera, una oferta muy atractiva durante los primeros meses puede dejar de tener sentido cuando terminen los beneficios promocionales.

El precio de lista es, por lo tanto, apenas el punto de partida. El costo real depende de qué se utilizará, cuánto se utilizará, durante cuánto tiempo, qué servicios adicionales serán necesarios y de las condiciones comerciales disponibles para ese contexto.

## Entonces, ¿qué camino elegir?

No existe una respuesta universal. La elección debería comenzar por el workload y los requisitos, no por el nombre de la cloud. ¿Qué servicios son realmente necesarios? ¿Dónde deben estar los datos? ¿Cuál es el costo total, incluyendo la transferencia de datos? ¿Cuál es la disponibilidad necesaria? ¿Qué competencias ya posee el equipo? ¿Cuánto lock-in es aceptable? ¿Existen requisitos de compliance o regulación? ¿Existe algún servicio específico que justifique la elección de determinado proveedor? Y, principalmente, ¿cuánto cuesta implementar, operar y eventualmente migrar esa arquitectura?

Esta última pregunta es particularmente importante porque el precio de la infraestructura es solamente una parte del costo. Una cloud puede ofrecer máquinas virtuales o GPUs más baratas y aun así ser una opción más cara cuando consideramos el esfuerzo de implementación, las integraciones, la operación y la necesidad de desarrollar componentes que otra plataforma ya ofrece como servicio administrado. De la misma manera, una arquitectura más portable puede exigir más ingeniería para ser construida y mantenida.

El mismo razonamiento vale para la migración. Una elección que parece barata hoy puede crear una dependencia cuyo costo de sustitución será mucho mayor en el futuro. Por otro lado, evitar cualquier dependencia específica para preservar una posibilidad de migración también significa pagar por esa portabilidad desde el primer día.

Por eso, comparar clouds únicamente por precio o cantidad de funcionalidades difícilmente sea suficiente. Lo que importa es el costo total de la decisión y el valor que cada plataforma entrega para ese workload. Descuentos, créditos, free tiers y contratos comerciales también entran en esta cuenta, pero deben analizarse junto con el costo recurrente y no como sustitutos de este.

La mejor arquitectura no es necesariamente aquella que utiliza más clouds, así como la mejor cloud no es necesariamente aquella que ofrece más servicios. Una única cloud puede ser la mejor elección cuando la simplicidad y la integración son prioritarias. Dos o más pueden tener sentido cuando existe una razón concreta para distribuir workloads entre proveedores. Una cloud más pequeña puede ser más adecuada para un workload específico. Y una solución que parece técnicamente más sofisticada puede ser simplemente más compleja sin entregar un beneficio proporcional.

Al final, elegir una cloud es elegir un conjunto de compromisos. Simplicidad, costo, portabilidad, lock-in, disponibilidad, resiliencia, compliance y complejidad operativa forman parte de la misma decisión. No existe una elección sin trade-offs. Existe solamente la posibilidad de entender qué trade-offs estamos asumiendo y por qué tienen sentido para ese contexto.

Conocer las alternativas no significa utilizarlas todas. Significa saber cuándo la elección estándar tiene sentido, cuándo vale la pena buscar otra opción y cuál será el impacto de esa decisión en el presente y en el futuro. En mi caso, conocer mejor las alternativas no hizo que dejara de preferir AWS. Simplemente hizo que dejara de ser la respuesta automática.
