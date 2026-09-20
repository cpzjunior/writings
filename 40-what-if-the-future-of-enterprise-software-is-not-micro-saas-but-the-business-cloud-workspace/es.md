# ¿Y si el futuro del software empresarial no fuera el Micro-SaaS, sino el Business Cloud Workspace?

_De la especialización de las aplicaciones a una plataforma que absorba software, agentes, conocimiento y relaciones de negocio_

**Resumen:** Defiendo que el futuro del software empresarial puede no estar en crear una aplicación para cada necesidad, sino en construir una plataforma capaz de reunir diferentes capacidades en un único entorno. Llamo a esta idea Business Cloud Workspace: un espacio que combina software especializado, agentes, datos, conocimiento e integraciones bajo una experiencia orientada al trabajo, no a los productos. La IA hace esto más viable al traducir la forma en que la empresa piensa en estructuras, workflows y automatizaciones, mientras que un ecosistema de plugins permite incorporar nuevas capacidades sin crear nuevas islas. El diferencial está en generar lock-in por el valor entregado: cuanto más construye y opera la empresa dentro de este entorno, más se convierte en parte de su forma de trabajar, haciendo que la permanencia sea una consecuencia del valor, y no de la dependencia.

---

Desde hace algún tiempo sigo la comunidad de Micro-SaaS y me gusta mucho la perspectiva que hay detrás de ella: encontrar un problema específico, construir un software simple que lo resuelva muy bien y, a partir de ahí, crear un negocio. Hay algo particularmente atractivo en la idea de que un equipo pequeño pueda identificar un dolor real y transformarlo en un producto independiente.

Pero cada vez tengo más la sensación de que la inteligencia artificial está amenazando precisamente este enfoque. No porque los problemas específicos estén desapareciendo o porque el Micro-SaaS haya dejado de tener sentido. Al contrario. La IA está haciendo cada vez más fácil transformar una necesidad específica en software. Y, cuando construir una determinada capacidad deja de ser una barrera relevante, la funcionalidad aislada se vuelve menos defendible.

Esto me lleva naturalmente a una pregunta: si el software especializado se está volviendo cada vez más abundante, ¿dónde estará el valor?

Durante mucho tiempo, la evolución del software empresarial pareció avanzar hacia la especialización. El ERP se ocupaba de la operación, el CRM de los clientes, el software de RR. HH. de las personas, otra aplicación de los proyectos, otra de los contratos, otra de los gastos. El SaaS hizo económicamente viable transformar prácticamente cualquier necesidad en un producto independiente. El Micro-SaaS llevó esa lógica al extremo: si existe un dolor específico, puede existir un software específico para resolverlo.

Esta lógica tenía sentido. Construir software era caro, y encontrar una necesidad suficientemente específica para atenderla mejor que los grandes proveedores podía ser una excelente oportunidad. Un equipo pequeño podía transformar una única funcionalidad en un producto y, a partir de ella, construir una empresa.

Pero esta ecuación está cambiando. La cantidad de software disponible ha crecido enormemente, mientras que la inteligencia artificial está reduciendo el coste de construir nuevas aplicaciones y funcionalidades. Si una capacidad puede implementarse, reproducirse y personalizarse cada vez más rápidamente, probablemente tendremos más software especializado que nunca. Esto no significa que el Micro-SaaS vaya a desaparecer. Tal vez ocurra precisamente lo contrario. La cuestión es dónde vivirá ese software.

En un texto anterior, “[¿Por qué los sistemas modernos son cada vez más fáciles de construir y más difíciles de diseñar?](https://cpzjunior.substack.com/p/por-que-sistemas-modernos-estao-ficando)“, argumenté que la cloud y la IA están haciendo que la implementación de soluciones sea cada vez más accesible, pero que esto no significa necesariamente menos complejidad. La complejidad no desaparece; cambia de lugar. En lugar de tener que construir cada componente, necesitamos decidir cómo combinarlos y convivir con las consecuencias de esas decisiones.

El software empresarial parece estar pasando por el mismo proceso. El SaaS hizo mucho más fácil adquirir una capacidad específica. La IA está haciendo más fácil construir nuevas capacidades. Pero, al mismo tiempo, una empresa necesita administrar una cantidad creciente de aplicaciones, integraciones, contratos, credenciales, datos y dependencias distribuidas entre diferentes proveedores.

Tal vez la próxima evolución no sea añadir aún más aplicaciones a este ecosistema, sino crear una capa capaz de absorber esta abundancia sin transferir toda su complejidad a quienes necesitan utilizarla.

De esta idea surge lo que llamo, provisionalmente, Business Cloud Workspace, o BCW.

## El coste de la fragmentación

El SaaS resolvió una parte importante del problema del software empresarial: hizo mucho más sencillo adquirir una capacidad. En lugar de comprar infraestructura, contratar un equipo o desarrollar una solución internamente, una empresa puede simplemente suscribirse a un servicio.

El problema es que esta simplicidad de adquisición no necesariamente se traduce en simplicidad de operación. Una pequeña empresa puede empezar con algunas decisiones perfectamente razonables: un CRM para ventas, una solución financiera, una herramienta de comunicación, otra para documentos, otra para proyectos y algunas aplicaciones específicas para necesidades particulares. Individualmente, cada decisión parece sencilla. La complejidad aparece cuando estas herramientas necesitan funcionar juntas.

Cada sistema tiene su propio modelo de datos, autenticación, permisos, interfaz, política de cobro y mecanismos de integración. Las personas necesitan saber dónde está determinada información, qué sistema utilizar para cada tarea y cómo hacer que un proceso atraviese diferentes aplicaciones.

También existe un coste financiero que tiende a subestimarse. Cada aplicación puede parecer barata de forma aislada, pero la suma de decenas de suscripciones representa un gasto recurrente relevante. Además de la mensualidad, existen costes asociados a implementación, integración, formación, administración y mantenimiento. La facilidad para adquirir software puede, paradójicamente, hacer que sea más fácil acumular software que evaluar el coste total de mantenerlo.

La fragmentación también aumenta la dependencia de proveedores. Cada nuevo servicio introduce una relación que necesita ser administrada, con sus propias políticas de precio, seguridad, disponibilidad, evolución del producto y condiciones contractuales. La empresa pasa a depender no solo de sus propios sistemas, sino de la continuidad y de las decisiones de una colección de proveedores externos.

Esto también crea un problema de supply chain. Una vulnerabilidad, indisponibilidad o cambio relevante en un proveedor puede afectar procesos que la empresa no controla directamente. Cuanto mayor sea la cantidad de servicios externos que participan en la operación, mayor será la superficie de dependencias que necesita ser supervisada.

Pero existe además un coste menos visible: el coste cognitivo. Al pasar de una aplicación a otra, la persona no está simplemente cambiando de ventana. Necesita reorganizar mentalmente la información relacionada con la tarea, recuperar lo que estaba haciendo y adaptar su forma de pensar a la manera en que aquella aplicación presenta el problema. El Alt+Tab resuelve el cambio de ventana, pero no resuelve ese esfuerzo cognitivo.

Cuando una tarea atraviesa varias aplicaciones, este esfuerzo se acumula. Parte de la atención deja de estar concentrada en el problema de negocio y pasa a utilizarse para reconstruir, en cada aplicación, el contexto mental necesario para continuar trabajando.

El problema, por lo tanto, no está necesariamente en tener muchos softwares. Algunas soluciones especializadas están perfectamente justificadas. Un software puede resolver tan bien una necesidad específica que vale la pena incorporarlo a la operación. La cuestión surge cuando cada nueva capacidad añade una nueva frontera que necesita ser administrada en términos financieros, técnicos y cognitivos.

La inteligencia artificial puede hacer que este escenario sea aún más extremo. A medida que resulta más barato producir software, se vuelve económicamente viable crear herramientas para necesidades cada vez menores y más específicas. El resultado puede ser una abundancia aún mayor de aplicaciones especializadas: más capacidades disponibles, pero también más decisiones sobre dónde encontrarlas, cómo conectarlas y quién será responsable de mantenerlas.

La especialización reduce el coste de construir cada componente, pero puede transferir parte del coste a quien necesita operar el conjunto. Cuanto más barato resulta crear software para resolver problemas específicos, mayor puede ser el esfuerzo necesario para administrar todos estos softwares como parte de una operación coherente.

Es en este punto donde surge una oportunidad. Tal vez no necesitemos menos software especializado. Necesitamos una capa capaz de absorberlo. En lugar de que cada nueva necesidad dé lugar necesariamente a otra aplicación independiente, podría incorporarse al entorno existente como un módulo, plugin, agente o integración.

El valor, en este escenario, no estaría únicamente en la capacidad individual ofrecida por cada software, sino en la infraestructura que permite combinarlos de forma coherente: contexto, datos, identidad, permisos, integración, gobernanza y experiencia.

La cuestión deja de ser cómo crear menos aplicaciones y pasa a ser cómo hacer que una empresa pueda utilizar más software sin tener que administrar proporcionalmente más coste, dependencias y complejidad cognitiva.

Es precisamente en este punto donde el BCW empieza a tener sentido.

## Una cloud para el negocio

La idea del BCW comienza con una inversión sencilla: en lugar de organizar el software en torno a las aplicaciones que una empresa necesita contratar, organizarlo en torno a las capacidades que necesita utilizar. La plataforma funcionaría como una cloud, ofreciendo estas capacidades bajo demanda y permitiendo que cada empresa componga progresivamente su propio entorno operativo.

En AWS, no necesito decidir anticipadamente cuál será toda mi arquitectura. Puedo empezar con almacenamiento, añadir una base de datos, crear una máquina virtual y, conforme aparece la necesidad, incorporar nuevos servicios. Puedo construir un MVP extremadamente sencillo o una arquitectura enterprise sofisticada utilizando la misma infraestructura.

Lo que cambia no es la plataforma, sino la combinación de recursos que utilizo y el nivel de complejidad que decido exponer. El BCW aplicaría esta lógica al negocio. Una empresa podría empezar con pocas capacidades básicas y, conforme crece, incorporar recursos para ventas, finanzas, personas, proyectos, pagos, conciliación, automatización o cualquier otra necesidad que surja. Estas capacidades no tendrían que aparecer para el usuario como sistemas independientes. Podrían compartir datos, identidad, permisos, workflows y contexto dentro del mismo entorno.

Esto permite que una tarea sea tratada como una tarea, y no como una secuencia de aplicaciones. Si para resolver un problema fueran necesarios datos de clientes, un contrato, una aprobación financiera y un documento, el usuario no debería necesitar saber en qué sistemas están almacenadas estas informaciones. El BCW debería reunir el contexto necesario y presentar la experiencia como una única operación.

La plataforma tampoco tendría que construirlo todo internamente. Así como una cloud ofrece servicios fundamentales sobre los cuales pueden construirse otras soluciones, el BCW podría proporcionar primitives empresariales para que módulos de terceros, agentes y aplicaciones especializadas fueran incorporados al entorno. Identidad, datos, permisos, billing, workflows y gobernanza podrían ser responsabilidades de la plataforma, mientras que desarrolladores y socios se concentrarían en las capacidades específicas que desean ofrecer.

Esta es una diferencia importante respecto a la lógica tradicional de las suites empresariales. El objetivo no sería ofrecer un conjunto cerrado de productos capaz de cubrir todas las áreas de la empresa, sino proporcionar una infraestructura sobre la cual la propia empresa pueda montar su entorno de trabajo.

El software dejaría de estar organizado a partir de las fronteras de los productos y pasaría a organizarse a partir de lo que la empresa necesita realizar. El resultado sería una especie de cloud del negocio: una plataforma que permite empezar con poco, incorporar nuevas capacidades conforme se vuelven necesarias y crecer sin tener que reconstruir la operación en cada nueva etapa.

## Del MVP a la operación

Una de las características más interesantes de una cloud es permitir que la misma infraestructura sustente proyectos con niveles de sofisticación completamente diferentes. Un desarrollador puede comenzar con una aplicación sencilla y, si funciona, utilizar la misma base para construir una operación mucho más compleja.

El BCW podría aplicar este principio a la creación de negocios. Hoy, transformar una idea en una empresa exige construir una cantidad significativa de infraestructura que no necesariamente forma parte de la hipótesis que se está probando. Es necesario lidiar con autenticación, usuarios, permisos, documentos, pagos, comunicación, procesos internos y una serie de otras capacidades incluso antes de saber si existe un negocio.

En “[Antes de sacar una idea del papel, hay que ponerla en él](https://cpzjunior.substack.com/p/antes-de-tirar-uma-ideia-do-papel)“, discutí cómo un MVP implica mucho más que implementar algunas funcionalidades. Antes de que una idea llegue al mercado, es necesario tomar decisiones de producto, experiencia, arquitectura, datos, seguridad, operación y ejecución. Muchas de ellas son simplemente el precio de construir la infraestructura necesaria para que el experimento exista.

El BCW podría abstraer parte de este trabajo. Quien está experimentando con una idea podría utilizar las capacidades ya disponibles en la plataforma y concentrar su energía en aquello que realmente necesita descubrir. Autenticación, usuarios, permisos, documentos, pagos, comunicación y workflows no tendrían que construirse desde cero solo para poner en funcionamiento la primera versión del negocio.

Esto cambia el significado de MVP. El objetivo deja de ser construir una pequeña versión de toda la infraestructura necesaria para operar una empresa y pasa a ser construir únicamente aquello que es necesario para probar la hipótesis.

Si la hipótesis se valida, la misma solución podría seguir evolucionando dentro del entorno. Lo que comenzó como una operación sencilla podría incorporar procesos más sofisticados, nuevos usuarios, agentes, integraciones y módulos sin exigir una reconstrucción completa de la infraestructura.

Esto crea una propiedad particularmente interesante: la distancia entre experimentar con un negocio y operarlo puede reducirse. Hoy, validar una idea y estructurar una empresa se tratan frecuentemente como problemas diferentes. Primero construimos el MVP; después necesitamos elegir e implantar los sistemas que sostendrán la operación real.

En un BCW, estos dos momentos podrían formar parte de la misma trayectoria. La plataforma podría ser lo suficientemente sencilla como para no obstaculizar el experimento y lo suficientemente profunda como para sostener aquello que venga después.

## La experiencia como producto

Esto lleva a lo que considero el principal diferencial del BCW: la experiencia. Existe una diferencia entre tomar un café en el bar de la esquina y tomar un café en Starbucks. En ambos casos, la necesidad fundamental puede ser exactamente la misma: tomar café. Lo que cambia es todo aquello que existe a su alrededor. El entorno, la consistencia, la forma de pedir, el pago, la personalización, la previsibilidad. El producto no es solo el café. Es la forma en que los elementos necesarios fueron organizados para que el cliente no tenga que pensar en ellos.

El software empresarial puede seguir la misma lógica. Un all-in-one tradicional intenta reunir diferentes productos bajo el mismo proveedor. Un producto como Zoho puede ofrecer CRM, finanzas, proyectos, RR. HH. y otras aplicaciones en una misma suite. Esto reduce la cantidad de proveedores que una empresa necesita administrar, pero no necesariamente elimina las fronteras entre los productos. El usuario sigue necesitando entender qué aplicación utilizar, dónde está disponible determinada capacidad y cómo una tarea atraviesa diferentes módulos.

El BCW parte de una premisa diferente: la unidad de la experiencia no debería ser el producto, sino el trabajo que la empresa necesita realizar. El usuario no debería entrar en el entorno pensando en qué sistema necesita abrir. Debería simplemente pensar en lo que necesita hacer. Si necesita contratar a un proveedor, la plataforma presenta el proceso. Si necesita consultar un contrato, encuentra el documento y el contexto relacionado. Si necesita descubrir una política interna, consulta la knowledge base. Si necesita ejecutar una actividad repetitiva, puede delegarla a un agente. Una tarea que requiere información financiera, datos de clientes y una aprobación debería aparecer como una única operación, aunque diferentes capacidades estén involucradas por detrás.

Esta distinción es fundamental. El all-in-one organiza la experiencia a partir de los productos que ofrece. El BCW debería organizarla a partir del trabajo que necesita realizarse. Por eso, CRM, finanzas, RR. HH., documentos, agentes, workflows y módulos de terceros no tendrían que presentarse como destinos diferentes dentro de la plataforma. Serían capacidades que pueden combinarse según lo que requiera la tarea. La integración, en este modelo, deja de ser una actividad que el usuario necesita comprender. Pasa a ser una propiedad del entorno.

Esto también cambia lo que significa competir por funcionalidades. El objetivo no es ofrecer una aplicación para cada necesidad, sino permitir que una empresa resuelva sus problemas sin tener que conocer la arquitectura necesaria para ello.

El ejemplo de Starbucks ayuda a entender esta diferencia. El valor no está únicamente en aquello que se ofrece, sino en la forma en que los elementos necesarios fueron organizados en una experiencia consistente y previsible.

En el BCW, el producto tampoco sería la suma de las aplicaciones. Sería la experiencia que emerge cuando dejan de ser el centro de la interacción.

## IA como capa de interpretación

La inteligencia artificial puede ser fundamental para reducir una de las mayores barreras para la adopción de software empresarial: la necesidad de traducir el funcionamiento de una empresa al lenguaje del sistema.

Una empresa conoce su propio negocio, pero eso no significa que conozca la estructura necesaria para representarlo dentro de un software. Tradicionalmente, esta traducción exige configuración, consultoría, formación y, muchas veces, desarrollo. El usuario necesita aprender cómo el sistema organiza entidades, relaciones, workflows y permisos antes de poder utilizarlo plenamente.

La IA puede funcionar como una capa de interpretación entre la forma en que la empresa describe su negocio y la forma en que la plataforma necesita representarlo. Una empresa podría importar sus hojas de cálculo y permitir que la plataforma identificara clientes, proveedores, productos, empleados y relaciones entre estas entidades. Podría importar documentos, políticas y procedimientos. Podría conectar sistemas existentes y dejar que la plataforma ayudara a mapear sus estructuras.

Del mismo modo, el usuario podría explicar lo que necesita en lenguaje natural y dejar que la plataforma determinara qué datos, capacidades y workflows son necesarios para ejecutar aquello.

El objetivo no sería simplemente importar datos o permitir comandos en lenguaje natural. Sería reducir la distancia entre la forma en que la empresa piensa sobre su negocio y la estructura necesaria para representarlo en el software.

Esto es especialmente importante para empresas pequeñas. Cuanto menor sea la organización, menos probable es que exista alguien dedicado a administrar sistemas empresariales o traducir procesos de negocio a modelos de software. La plataforma necesita asumir una parte mayor de este trabajo precisamente donde la capacidad técnica es menor.

Esta interpretación también podría ocurrir continuamente. A medida que el negocio cambia, el BCW podría transformar nuevas necesidades descritas por el usuario en estructuras, workflows, automatizaciones y configuraciones, sin exigir que la empresa conozca anticipadamente la mejor forma de modelarlas.

Una buena plataforma empresarial no debería exigir que el usuario aprenda a pensar como el sistema. Debería ser capaz de entender cómo piensa la empresa y traducirlo al sistema.

En este sentido, la IA no es solo una funcionalidad del BCW. Es parte de la propia abstracción que permite ocultar la complejidad de la plataforma sin eliminar la capacidad que existe detrás de ella.

## Knowledge bases y agentes de IA

Una vez que los datos, documentos y procesos están en el mismo entorno, el conocimiento organizacional puede dejar de ser solo documentación y pasar a formar parte de la propia operación.

La empresa podría mantener una wiki dentro del BCW, pero una wiki conectada al resto de la plataforma. Políticas, procedimientos, manuales, decisiones y aprendizajes podrían estar relacionados con los procesos que ejecutan estas reglas.

Este conocimiento podría estructurarse como una especie de wiki as code: versionado, organizado y gobernado por la propia empresa, mientras que la IA lo utilizaría como contexto para responder preguntas, ejecutar procesos y orientar agentes.

Una política podría convertirse en una regla de ejecución. Un procedimiento podría transformarse en un workflow. Una orientación recurrente podría dar lugar a un agente. En este contexto, los agentes no serían simplemente asistentes conversacionales. Serían componentes operativos de la empresa, capaces de acceder a los recursos de la plataforma, consultar la knowledge base, ejecutar workflows y operar dentro de los permisos definidos para ellos.

La empresa podría personalizar no solo lo que un agente conoce, sino también cómo trabaja. Un proceso podría tener su propio agente, con objetivos, permisos, herramientas y criterios de decisión definidos por la organización.

Incluso la estrategia utilizada para resolver un problema podría formar parte de esta configuración. Un agente podría estar orientado a trabajar según PDCA, mientras que otro utilizaría OODA o una metodología específica definida internamente. La metodología dejaría de ser solo una orientación documentada y pasaría a formar parte de la lógica de ejecución del agente.

El mismo principio se aplicaría a los workflows. En lugar de simplemente elegir entre procesos predefinidos, la empresa podría adaptar etapas, reglas de aprobación, condiciones y responsabilidades de acuerdo con su forma de operar.

El resultado sería una capa diferente de personalización. La empresa no estaría simplemente almacenando su conocimiento dentro del BCW. Estaría transformando ese conocimiento en comportamiento operativo.

Y todo esto podría ocurrir dentro de la propia plataforma. No sería necesario desarrollar un agente desde cero, crear un MCP server, construir integraciones específicas o mantener una arquitectura paralela únicamente para conectar la IA con los sistemas de la empresa. Las primitives necesarias ya estarían disponibles en el entorno.

El BCW dejaría, entonces, de ser únicamente el lugar donde la empresa almacena información y ejecuta procesos. Pasaría a ser también el lugar donde define cómo deben funcionar estos procesos y cómo pueden ejecutarlos los agentes.

## Micro-SaaS como plugins

Aquí es donde el Micro-SaaS puede encontrar un nuevo papel. En lugar de desaparecer, puede dejar de ser necesariamente una isla.

Una plataforma de este tipo podría tener un Marketplace en el que desarrolladores crearan módulos para necesidades que el proveedor principal jamás podría anticipar. Un producto extremadamente específico para determinado sector, una integración con un sistema legado, un workflow especializado o una nueva capacidad de IA podría instalarse directamente en el BCW.

La mejor analogía quizá esté en los mods de Skyrim. Bethesda no necesitó imaginar todas las funcionalidades, historias, mapas y experiencias que los jugadores podrían querer. Creó un juego suficientemente extensible para que toda una comunidad pudiera construir sobre él.

Un BCW podría funcionar de manera similar. El proveedor construiría la infraestructura común, mientras que una comunidad de desarrolladores podría crear capacidades que la empresa central jamás tendría capacidad o incentivo para anticipar. La diferencia es que, en este caso, los mods no añadirían únicamente contenido. Podrían añadir capacidades reales al negocio.

El desarrollador no necesitaría reconstruir toda la infraestructura empresarial necesaria para entregar su funcionalidad. Identidad, permisos, datos, billing, workflows y otras primitives podrían ser proporcionados por la plataforma. Se concentraría en la capacidad específica que desea ofrecer.

Esto cambia la naturaleza del Micro-SaaS. En lugar de que cada producto tenga que conquistar clientes individualmente, desplegar su propia infraestructura y crear otra isla de datos, podría distribuirse como una extensión del entorno que el cliente ya utiliza. El desarrollador obtiene acceso a una base existente. El cliente obtiene una nueva capacidad sin tener que adoptar otro sistema.

Esta dinámica también reduce el coste de experimentación. Un desarrollador puede crear un módulo para un nicho muy específico sin tener que construir toda la infraestructura empresarial a su alrededor. Si existe demanda, el módulo crece dentro del ecosistema. Si no existe, el coste del fracaso es menor.

Pero esta apertura trae una consecuencia inevitable: cuanto más cosas puedan construirse sobre el BCW, mayor será la necesidad de gobernanza. Permitir que terceros creen módulos, agentes y workflows significa lidiar con identidad, permisos, aislamiento, seguridad, auditoría, versionado, observabilidad, billing y políticas. La plataforma tendría que ofrecer a los componentes que se ejecutan sobre ella una infraestructura de gobernanza similar a la que una cloud ofrece a los workloads. La libertad estaría en aquello que puede construirse. El control estaría en la infraestructura que permite construir esas cosas de forma segura.

El BCW, por lo tanto, no debería ser un intento de centralizar todo el software empresarial en un único proveedor. Su función sería centralizar la experiencia y las primitives comunes, manteniendo abierta la posibilidad de incorporar software especializado.

Si el mejor sistema de nómina continúa siendo externo, puede integrarse. Si surge una solución jurídica mejor, puede participar en el entorno. Si un desarrollador crea una herramienta especializada superior al módulo nativo, puede instalarse.

El proveedor del BCW no necesita prever todas las necesidades, ni construir la mejor solución para cada una de ellas. Cuanto más extensible sea la plataforma, menos necesario será anticipar el futuro. El proveedor construye el sustrato; el ecosistema descubre qué debe existir sobre él.

En este escenario, el Marketplace no sería solo un canal de distribución. Sería parte del mecanismo mediante el cual el BCW evoluciona más rápido que la propia empresa que lo construyó.

El BCW no necesita vencer a todo el software. Necesita hacer innecesario salir de él para utilizarlo.

## El lock-in por valor

Esta arquitectura también crea un tipo diferente de lock-in. Existe un lock-in basado en la restricción, en el que el cliente permanece porque salir es difícil. Existe otro, más interesante, basado en el valor: el cliente permanece porque la plataforma se convirtió en el entorno natural donde resuelve sus problemas.

Así es como pienso sobre una plataforma como AWS. Cuando una plataforma se vuelve suficientemente familiar, ante un problema nuevo la pregunta deja de ser “¿qué proveedor debo contratar?” y pasa a ser “¿cómo resuelvo esto dentro de la plataforma que ya utilizo?”

El BCW debería buscar algo similar en el contexto empresarial. Con el tiempo, una empresa no estaría simplemente utilizando la plataforma. Estaría construyendo sobre ella. Sus procesos, workflows, agentes, integraciones y conocimiento se moldearían de acuerdo con su propia forma de operar.

En ese punto, el BCW dejaría de ser simplemente el software que utiliza la empresa. Pasaría a ser el entorno que la propia empresa construyó para sí misma.

Skyrim también ofrece una analogía interesante aquí. Después de cientos de horas y decenas de mods instalados, el jugador no está simplemente jugando el producto que Bethesda entregó. Está jugando una versión del juego moldeada por sus propias elecciones.

Lo mismo podría ocurrir con una empresa. Después de años, el BCW ya no sería una herramienta genérica. Sería una versión de la plataforma moldeada por la propia organización: con sus procesos, su conocimiento, sus agentes y su forma particular de trabajar.

Ahí es donde el lock-in por valor se vuelve interesante. El verdadero lock-in no sería impedir la salida. Sería hacer que salir supusiera una regresión. La empresa continuaría utilizando el BCW no porque estuviera atrapada en él, sino porque habría construido allí una forma de trabajar que no encontraría preparada en ningún otro lugar.

## Del Workspace a la Business Network

Cuando el BCW pasa a concentrar la operación de una empresa, conectar diferentes empresas se convierte en una evolución natural. Si la plataforma conoce procesos, personas, documentos, proveedores y necesidades de una organización, también posee parte del contexto necesario para facilitar las relaciones de esa organización con otras.

VTEX ofrece una referencia interesante. En lugar de tratar el comercio electrónico únicamente como una aplicación aislada, su plataforma participa en una operación que conecta empresas, consumidores, vendedores, pagos, pedidos y otros elementos de la transacción. El BCW podría llevar una lógica similar más allá del comercio electrónico, transformando el propio entorno de trabajo empresarial en una capa de relación entre organizaciones.

Esto podría comenzar con un catálogo público de servicios. Un proveedor podría registrar su empresa, productos, servicios, capacidades, regiones de atención y condiciones comerciales. Este catálogo sería accesible incluso para empresas que todavía no utilizan el BCW, creando una capa pública de descubrimiento sobre la Business Network.

A partir de ahí, descubrimiento y operación podrían formar parte del mismo flujo. Una empresa podría buscar un proveedor de servicios, comparar alternativas, solicitar una cotización, negociar, contratar, emitir un pedido y realizar el pago sin tener que reconstruir el contexto en diferentes sistemas. El proveedor, por su parte, podría responder a la demanda, seguir la relación y operar sus propios procesos dentro del mismo entorno.

La diferencia respecto a un marketplace tradicional estaría precisamente en el contexto. La plataforma ya conoce los usuarios, políticas, límites de aprobación y procesos del comprador. Al mismo tiempo, puede incorporar los datos, servicios, documentos e historial del proveedor.

Una solicitud de compra podría comenzar como una necesidad interna y terminar como una transacción externa, sin exigir que alguien copie información de un sistema a otro.

Es en este punto donde la Business Network se diferencia del Marketplace discutido anteriormente. El Marketplace conecta una empresa con capacidades de software. La Business Network conecta una empresa con otras empresas. En el primer caso, el ecosistema amplía aquello que puede construirse dentro de la plataforma. En el segundo, amplía aquello que puede realizarse a través de ella. El BCW dejaría, entonces, de ser únicamente un workspace individual y pasaría a funcionar también como una infraestructura de relación entre empresas.

Esta dinámica introduciría un efecto de red. Cuantas más empresas estén presentes, más proveedores y servicios podrán encontrarse. Cuantos más proveedores estén presentes, más útil será la plataforma para las empresas. Y cuanto mayor sea esta base, mayor será también el mercado para módulos, agentes y soluciones desarrolladas por terceros.

En este punto, la frontera entre software empresarial e infraestructura de negocios empieza a desaparecer. La plataforma no solo ayuda a una empresa a operar. También pasa a facilitar el descubrimiento, la contratación y la operación de las relaciones que permiten que una empresa funcione.

El ecosistema pasa a reforzar la propia plataforma.

## El riesgo de crear una nueva complejidad

Existe, sin embargo, una paradoja en la propia propuesta. Una plataforma capaz de hacer muchas cosas también puede convertirse en una plataforma difícil de utilizar.

Salesforce es un buen ejemplo de este desafío. Su propuesta como plataforma es poderosa precisamente porque permite modelar procesos, objetos, permisos, automatizaciones e integraciones en profundidad. Pero esta flexibilidad también crea una capa de administración que puede requerir conocimiento especializado.

Sería perfectamente posible transformar el BCW en algo similar: una plataforma extremadamente poderosa, con cientos de recursos, configuraciones, permisos y posibilidades, pero que exigiera conocimiento especializado para ser utilizada.

En ese caso, la plataforma simplemente habría desplazado el problema. En lugar de administrar decenas de sistemas independientes, la empresa pasaría a administrar un único sistema excesivamente complejo.

La abstracción, por lo tanto, no puede ser únicamente una característica de la interfaz. Tiene que formar parte de la propia arquitectura del producto. La complejidad debe seguir existiendo para quien la necesita, pero no puede ser una exigencia para quien no la necesita.

Un pequeño negocio debería poder operar el BCW sin conocer su estructura interna. Un profesional más avanzado debería poder acceder a configuraciones profundas cuando fuera necesario. Un administrador podría definir políticas y workflows sofisticados sin obligar a cada empleado a comprenderlos. Un arquitecto enterprise podría acceder a APIs, integraciones y configuraciones avanzadas sin convertir esta misma experiencia en la interfaz estándar de todos los usuarios.

La experiencia de un emprendedor y la experiencia de un arquitecto enterprise pueden ser radicalmente diferentes sin que estén utilizando productos diferentes.

Aquí es donde AWS ofrece una referencia importante. La misma infraestructura puede atender desde quien solo necesita una abstracción sencilla hasta quien necesita controlar detalles mucho más profundos. La plataforma no necesita elegir entre simplicidad y sofisticación. Puede ofrecer ambas, siempre que consiga exponer la complejidad de forma progresiva.

El BCW tendría que hacer lo mismo. Su ventaja no estaría en eliminar la complejidad, algo que probablemente no sea posible en una plataforma de este tipo, sino en hacer que cada persona interactúe únicamente con la complejidad necesaria para realizar su trabajo.

La plataforma necesita ofrecer profundidad sin imponer profundidad. Tal vez esta sea la condición fundamental para que una plataforma de este tipo siga siendo sencilla incluso cuando aquello que existe detrás de ella se vuelve extremadamente sofisticado.

## Una idea que ya está tomando forma

La idea de BCW puede parecer una extrapolación, pero sus componentes ya están siendo construidos, por separado, por diferentes empresas.

Salesforce transformó el software empresarial en una plataforma extensible de aplicaciones, automatizaciones y datos. Microsoft viene acercando productividad, datos, desarrollo y agentes dentro de un mismo ecosistema. Shopify y VTEX muestran cómo una plataforma puede conectar la operación de una empresa con un ecosistema de terceros. AWS demostró, en otra capa, cómo una infraestructura puede ofrecer capacidades muy diferentes sin exigir que todos los usuarios conozcan su complejidad interna. Lo que todavía no está completamente resuelto es la combinación de estas ideas en una experiencia coherente. Tal vez el BCW no sea una ruptura que aún está por ocurrir, sino el resultado de movimientos que ya han comenzado.

La IA está haciendo más barato crear software. Las plataformas se están volviendo más extensibles. Los agentes están empezando a participar en la operación. Los marketplaces están conectando empresas con nuevas capacidades. Y, al mismo tiempo, la cantidad de software que una empresa necesita administrar continúa creciendo.

La cuestión, por lo tanto, quizá no sea si tendremos más software, sino dónde vivirá ese software. ¿Aplicaciones agrupadas en suites, cada una preservando su propia frontera? ¿O un entorno en el que aplicaciones, agentes, datos, conocimiento, servicios externos y módulos especializados sean simplemente diferentes formas de ampliar aquello que una empresa puede hacer?

La cloud transformó la infraestructura en capacidad bajo demanda. El BCW podría aplicar una lógica similar al software empresarial: no entregar una colección fija de aplicaciones, sino un entorno capaz de incorporar nuevas capacidades conforme se vuelven necesarias.

En este modelo, la empresa no tendría que elegir anticipadamente todo el software que utilizará. Podría empezar con poco, incorporar nuevas capacidades, conectar sistemas existentes, añadir agentes e instalar extensiones conforme evoluciona su operación.

Esto cambia la unidad de valor. El software deja de ser únicamente la aplicación que resuelve un problema específico y pasa a ser el entorno que permite a la empresa resolver problemas diferentes sin reconstruir su forma de trabajar ante cada nueva necesidad.

Tal vez este sea el cambio más importante. El futuro del software empresarial puede no ser una aplicación para cada cosa, ni necesariamente una suite que intente hacerlo todo. Puede ser una plataforma sobre la cual cada empresa construye, progresivamente, su propia manera de trabajar.
