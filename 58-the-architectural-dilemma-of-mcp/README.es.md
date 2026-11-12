# El dilema arquitectónico del MCP

_Cómo distribuir capacidades para administrar la complejidad cognitiva de los agentes de IA._

**Resumen**: Sostengo que el principal dilema arquitectónico del MCP no está en centralizar o distribuir servidores, sino en administrar cómo sus capacidades son descubiertas, seleccionadas y puestas a disposición de los agentes. En entornos corporativos, poner todas las herramientas a disposición de una sola vez aumenta la complejidad cognitiva y dificulta la selección contextual. La solución pasa por separar el catálogo global de capacidades, el descubrimiento progresivo y la ejecución, combinando gobernanza centralizada con autonomía de los dominios y enrutamiento inteligente. Así, los agentes acceden únicamente a lo que necesitan, cuando lo necesitan, sin asumir la complejidad de administrar toda la infraestructura. El desafío es transformar la diversidad de recursos corporativos en un ecosistema selectivo, seguro y eficiente.

---

En mi último artículo, "[Más allá de los Agentes Generalistas: Una Arquitectura de Microagentes de IA](https://cpzjunior.substack.com/p/alem-dos-agentes-generalistas-uma?utm_source=chatgpt.com)", exploré una cuestión que considero cada vez más relevante a medida que los agentes de IA comienzan a ocupar un espacio más significativo en las arquitecturas de software: ¿debemos seguir concentrando responsabilidades en agentes generalistas o empezar a pensar en una distribución más especializada de la capacidad de razonamiento?

En aquella discusión, una de las ideas que surgieron fue la necesidad de separar el universo de capacidades que posee una organización de aquello que cada agente necesita conocer efectivamente durante una ejecución. Un catálogo global puede ser amplio, mientras que el contexto de cada agente debe ser específico y construirse de acuerdo con la tarea que necesita realizar.

Esta premisa, sin embargo, plantea una cuestión arquitectónica que merece ser explorada. Si comenzamos a distribuir la inteligencia entre diferentes agentes, ¿cómo debemos organizar y poner a disposición las herramientas y capacidades que utilizan para interactuar con el mundo?

Aquí es donde el Model Context Protocol (MCP) introduce un nuevo dilema. Imaginemos una gran organización, con decenas de productos, cientos de APIs y diferentes dominios de negocio. Cada producto comienza a poner sus funcionalidades a disposición mediante servidores MCP, haciendo que sus capacidades sean accesibles para los agentes. Inicialmente, la solución parece relativamente sencilla: crear un servidor MCP para cada producto y permitir que los agentes se conecten a los servidores que necesitan.

Pero este enfoque plantea rápidamente otras cuestiones. ¿Y si un agente necesita acceder a decenas de productos? ¿Debemos conectarlo a todos esos servidores? ¿Debemos poner todas las herramientas a su disposición de una sola vez? ¿Qué ocurre cuando las descripciones, los parámetros y los contratos de esas herramientas comienzan a consumir una parte significativa de la ventana de contexto?

Una alternativa sería centralizarlo todo en un gran servidor MCP corporativo. Pero ¿estaríamos simplemente recreando, bajo una nueva interfaz, los mismos problemas de concentración y acoplamiento que históricamente hemos intentado resolver con arquitecturas distribuidas?

Quizás estemos ante una nueva categoría de problema. La arquitectura deja de influir únicamente en la organización de los componentes de software y pasa a influir también en la forma en que los agentes descubren, comprenden y seleccionan sus capacidades.

Si antes discutíamos cómo distribuir la inteligencia, ahora necesitamos discutir cómo distribuir el conocimiento sobre aquello que la inteligencia puede hacer.

## El problema de la abundancia de herramientas

Una de las características más interesantes del MCP es permitir que diferentes sistemas pongan sus funcionalidades a disposición de los agentes de IA de manera estandarizada. En lugar de depender exclusivamente de integraciones desarrolladas específicamente para cada aplicación, podemos establecer una interfaz común para el descubrimiento y la ejecución de herramientas.

Esta estandarización abre importantes posibilidades de integración, pero también crea una consecuencia que merece atención: cuantos más sistemas adoptan el protocolo, mayor se vuelve el universo de capacidades potencialmente disponibles para los agentes.

En una aplicación pequeña, con pocos servidores y herramientas bien delimitadas, este escenario difícilmente representa un problema. Sin embargo, cuando trasladamos esta arquitectura a una organización con decenas o cientos de productos, la situación cambia considerablemente.

Cada servidor puede ofrecer diversas herramientas, acompañadas de descripciones, parámetros y schemas necesarios para su utilización. Cuando un cliente agrega herramientas de múltiples servidores y presenta esas definiciones al modelo, el volumen de información crece rápidamente. Parte de ella será irrelevante para la tarea actual, pero seguirá ocupando espacio en el contexto y ampliando el conjunto de alternativas que el modelo necesita evaluar.

Es tentador tratar este problema únicamente como una limitación de la ventana de contexto. Al fin y al cabo, los modelos cada vez más grandes pueden procesar cantidades crecientes de información. Pero creo que esta interpretación es insuficiente.

Incluso cuando hay espacio disponible, presentar cientos de herramientas no significa necesariamente mejorar la capacidad de decisión del agente. Un catálogo extenso puede aumentar la ambigüedad entre operaciones similares, dificultar la selección de la herramienta adecuada e introducir información que no contribuye a la resolución de la tarea. La cuestión no está únicamente en la cantidad de tokens consumidos, sino también en la calidad del conjunto de alternativas presentado al modelo.

Existe, por lo tanto, una distinción importante entre tres dimensiones que frecuentemente terminan tratándose como si fueran una sola. La primera es la disponibilidad: ¿qué capacidades existen en la organización? La segunda es la accesibilidad: ¿a cuáles de esas capacidades está autorizado y técnicamente habilitado a acceder un determinado agente? La tercera es la relevancia contextual: ¿cuáles de ellas necesitan realmente presentarse durante una ejecución específica?

Estos conjuntos no tienen por qué ser iguales. Una organización puede poseer miles de capacidades, un agente puede tener acceso autorizado a algunos cientos y una determinada tarea puede requerir únicamente un pequeño subconjunto de ellas.

Esta distinción es el punto de partida para replantear la arquitectura MCP. El desafío no consiste simplemente en hacer que todas las herramientas sean accesibles, sino en administrar qué capacidades deben descubrirse, ponerse a disposición y utilizarse en cada contexto.

## El dilema de la centralización y la distribución

La primera analogía que surge es con una discusión bastante conocida en la arquitectura de software: centralizar funcionalidades en una aplicación monolítica o distribuirlas entre servicios independientes.

Podríamos imaginar un gran servidor MCP corporativo, responsable de concentrar las herramientas de diferentes productos y ofrecer un único punto de conexión para los agentes. Este enfoque simplifica la experiencia de integración, facilita la administración de conexiones y puede favorecer una gobernanza centralizada.

Por otro lado, a medida que el catálogo crece, el servidor comienza a concentrar responsabilidades cada vez mayores. El mantenimiento se vuelve más complejo, la evolución puede generar dependencias entre dominios y la cantidad de herramientas disponibles sigue creciendo. Centralizar la conexión no significa necesariamente resolver la sobrecarga cognitiva. Podemos tener un único punto de acceso y, aun así, ofrecer un universo de capacidades difícil de administrar.

En el extremo opuesto, podríamos adoptar servidores MCP independientes por producto o dominio funcional. Cada equipo sería responsable de sus herramientas, contratos y ciclos de evolución. Tendríamos mayor autonomía, aislamiento y flexibilidad para administrar las capacidades.

Sin embargo, esta distribución también implica costes. La multiplicación de servidores exige mecanismos de descubrimiento, administración de conexiones, autenticación, observabilidad y gobernanza. Además, el agente o la infraestructura responsable de su ejecución todavía tendría que decidir qué servidores utilizar y qué herramientas presentar.

Es importante reconocer que la analogía con los monolitos y los microservicios tiene sus límites. Estamos hablando de universos arquitectónicos diferentes. La distribución de servicios busca administrar principalmente responsabilidades operativas, dependencias y escalabilidad. En el contexto del MCP, existe una dimensión adicional: la topología de los servidores influye en la forma en que sus capacidades se descubren y se ponen a disposición del modelo.

Un servidor centralizado puede ofrecer herramientas de forma selectiva. Del mismo modo, decenas de servidores distribuidos pueden ser administrados por una capa central de descubrimiento y enrutamiento. La topología física de los servidores no tiene por qué determinar la organización lógica de las capacidades.

Esta percepción cambia la naturaleza de la discusión. No necesitamos necesariamente elegir entre centralizarlo o distribuirlo todo. Podemos distribuir la ejecución, centralizar determinadas responsabilidades de gobernanza y mantener mecanismos compartidos de descubrimiento. Lo importante es separar la organización de los servidores de la forma en que sus capacidades llegan a los agentes.

## Del catálogo de servidores al catálogo de capacidades

Una posible respuesta sería introducir una capa intermedia responsable de conocer los servidores MCP disponibles y administrar el acceso a sus capacidades.

Inicialmente, podríamos pensar en un MCP Registry, que funcionaría como un inventario de los servidores existentes. Permitiría localizar integraciones, identificar a sus responsables, consultar metadatos y conocer información relevante sobre cada servidor.

Pero existe una diferencia importante entre conocer los servidores de una organización y conocer aquello que la organización puede hacer a través de ellos.

Un registry responde qué servidores existen, dónde están disponibles y quién es responsable de su mantenimiento. Un catálogo de capacidades necesita ir más allá. Debe representar las herramientas ofrecidas por esos servidores, sus finalidades, sus contratos, sus restricciones, sus dependencias y las condiciones necesarias para su utilización.

Imaginemos una organización que posee diferentes sistemas responsables de la información de clientes. Cada uno ofrece herramientas relacionadas con consultas de datos personales, posiciones financieras y movimientos. Un inventario de servidores permite descubrir dónde están alojadas estas funcionalidades. Un catálogo de capacidades permite comprender qué operación satisface una determinada necesidad, qué fuente de datos debe considerarse y qué condiciones deben cumplirse antes de la ejecución.

Esta diferencia es fundamental. El descubrimiento de una herramienta no debería depender exclusivamente del conocimiento previo sobre el servidor que la ofrece. Idealmente, el agente debería poder partir de una necesidad funcional y encontrar la capacidad correspondiente, independientemente de su ubicación física.

En este escenario, un MCP Hub o Gateway podría asumir responsabilidades complementarias, como administrar conexiones, intermediar llamadas, aplicar políticas de acceso y centralizar aspectos operativos de la comunicación. Sin embargo, es importante no confundir estas responsabilidades. Conocer la existencia de una herramienta no significa necesariamente saber cuándo utilizarla. Localizar un servidor tampoco significa que el agente necesite establecer una conexión permanente con él.

Comenzamos así a percibir la necesidad de separar tres preocupaciones arquitectónicas: el registro de las capacidades disponibles, el descubrimiento de aquellas que tienen sentido para una determinada demanda y la ejecución de las operaciones en los servidores responsables.

Esta separación permite que la infraestructura evolucione sin obligar a los productos a abandonar su autonomía. Cada dominio puede seguir administrando sus servidores MCP, mientras que la organización mantiene una visión compartida de sus capacidades.

## Descubrimiento progresivo y selección contextual

Una vez establecido un catálogo global, surge una posibilidad particularmente interesante: en lugar de poner todas las herramientas a disposición desde el principio, el agente podría comenzar con un conjunto reducido de capacidades de descubrimiento.

Al recibir una demanda, consultaría el catálogo para identificar herramientas potencialmente relevantes. Solo después de esta selección se pondrían a disposición las definiciones completas, incluidos los parámetros y schemas necesarios para su utilización.

Este enfoque, frecuentemente denominado Progressive Tool Discovery, busca separar el universo global de herramientas de aquello que realmente necesita estar presente en el contexto del modelo.

El agente no necesita conocer de antemano todas las capacidades disponibles. Necesita tener la posibilidad de descubrir aquellas que serán necesarias.

Podemos imaginar este proceso en dos niveles. En el primero, el catálogo presenta información resumida sobre las capacidades, suficiente para permitir su identificación y comparación. En el segundo, después de seleccionar las alternativas más adecuadas, el agente recibe los contratos completos necesarios para invocarlas.

Esta separación reduce la cantidad de información presentada inicialmente al modelo y permite que el contexto se construya progresivamente, a medida que evoluciona la tarea.

Sin embargo, el descubrimiento dinámico no es simplemente una cuestión de buscar herramientas en un catálogo. La búsqueda debe ser suficientemente precisa para evitar que se seleccionen capacidades similares, pero funcionalmente inadecuadas. Una búsqueda que devuelve operaciones relacionadas con el tema, pero que no satisfacen efectivamente la necesidad, simplemente traslada el problema de selección a una etapa anterior.

Por eso, creo que el descubrimiento debería combinar diferentes mecanismos. La información estructurada sobre dominio, finalidad, permisos y restricciones puede reducir el universo de posibilidades. Las técnicas de búsqueda léxica y semántica pueden identificar herramientas relacionadas con la intención planteada. Un mecanismo de ranking puede entonces considerar la adecuación funcional de las alternativas encontradas.

También es importante considerar las dependencias entre capacidades. Algunas operaciones pueden requerir que otras se ejecuten previamente, mientras que determinadas funcionalidades pueden depender de herramientas ofrecidas por diferentes servidores. El descubrimiento debe poder representar estas relaciones, evitando tratar cada herramienta como una unidad completamente aislada.

Sin embargo, existe una cuestión interesante en este modelo: para descubrir aquello que todavía no conoce, el agente necesita tener acceso a algún mecanismo de descubrimiento. Esto significa que la propia capacidad de buscar herramientas pasa a ser una capacidad fundamental de la arquitectura. El catálogo deja de ser únicamente un repositorio de consulta y pasa a formar parte del mecanismo de construcción del contexto operativo del agente.

## Cuando la descripción de la herramienta se convierte en parte de la arquitectura cognitiva

En un ecosistema pequeño, las descripciones inconsistentes pueden corregirse relativamente rápido. Sin embargo, cuando existen cientos de herramientas, la calidad de los metadatos pasa a tener un impacto directo sobre la confiabilidad de la arquitectura.

Imaginemos diferentes productos que ofrecen herramientas llamadas get_customer, retrieve_customer, find_client y get_customer_details. Todas parecen razonables, pero pueden representar operaciones diferentes, consultar fuentes distintas o satisfacer necesidades específicas.

El modelo no conoce necesariamente estas fronteras funcionales. Necesita inferirlas a partir de la información proporcionada por el servidor: nombre, descripción, parámetros, schema de entrada y contexto de utilización.

Una descripción como "Retrieve customer information" es técnicamente válida, pero ofrece poca información para orientar la decisión. ¿Qué información se devolverá? ¿Cuál es la fuente oficial? ¿En qué situaciones debe utilizarse esta herramienta? ¿Existen restricciones? ¿Cuándo sería más adecuada otra herramienta?

Una descripción realmente útil necesita explicar no solo qué hace la operación, sino también su finalidad, su alcance, sus limitaciones y las circunstancias en las que debe elegirse.

Esta diferencia es relevante porque, en una arquitectura tradicional, una API mal documentada perjudica principalmente a los desarrolladores responsables de integrarla. En una arquitectura agéntica, una herramienta mal descrita puede perjudicar al propio proceso de decisión del agente.

La descripción deja de ser únicamente documentación. Pasa a formar parte de la interfaz cognitiva entre el software y la inteligencia artificial.

Por eso, creo que un catálogo corporativo de capacidades necesitaría ir más allá de almacenar nombres, descripciones y schemas. Debería incorporar información sobre dominio funcional, finalidad, precondiciones, efectos secundarios, dependencias, permisos, origen de los datos y posibles solapamientos con otras herramientas.

También existe una distinción importante entre el contrato técnico y el contrato semántico de una herramienta. El schema define cómo invocar una operación. El contrato semántico explica qué representa, en qué condiciones debe utilizarse y qué garantías ofrece sobre el resultado.

Dos herramientas pueden presentar descripciones muy similares y, aun así, no ser intercambiables. Una puede consultar una fuente oficial, mientras que otra utiliza información derivada o actualizada en intervalos diferentes. La elección correcta no depende únicamente de la similitud entre la intención y la descripción, sino también de la autoridad de la fuente y de las características del resultado esperado.

En este contexto, los modelos de IA podrían ayudar a evaluar descripciones, identificar ambigüedades, sugerir mejoras y enriquecer los metadatos. Sin embargo, existe un límite importante: la inferencia de un modelo no puede confundirse con la definición oficial de una capacidad. La información técnica, los contratos y las reglas de negocio deben seguir teniendo fuentes verificables y responsables identificados.

## El ciclo de vida de las capacidades

Hasta aquí, estamos considerando que existe un catálogo capaz de representar el universo de capacidades de una organización. Pero ¿cómo garantizar que ese catálogo permanezca actualizado?

En una empresa con diferentes productos y equipos de desarrollo, se crean nuevas funcionalidades, se modifican herramientas, evolucionan los contratos y se retiran APIs. Un registry que dependa exclusivamente de actualizaciones manuales corre el riesgo de convertirse en otro inventario desactualizado.

El descubrimiento dinámico solo funciona si la información utilizada para encontrar las herramientas es confiable.

Esto sugiere que necesitamos administrar el ciclo de vida de las capacidades. Un nuevo servidor MCP debería ser identificado y registrado. Las nuevas herramientas deberían generar actualizaciones en el catálogo. Los cambios en los contratos deberían provocar una revalidación y un versionado. Las capacidades discontinuadas deberían dejar de presentarse como opciones válidas.

Quizás este proceso pueda orientarse a eventos, utilizando triggers provenientes de los pipelines de CI/CD, plataformas de gestión de APIs, registros de servicios y de los propios servidores MCP.

En este modelo, la publicación de una nueva versión podría activar automáticamente un proceso de descubrimiento, registro y validación de las capacidades. Los cambios de permisos podrían actualizar las políticas asociadas. Los cambios incompatibles podrían requerir aprobación antes de su publicación.

El catálogo dejaría de ser un documento mantenido manualmente y pasaría a funcionar como un inventario vivo de las capacidades corporativas.

Sin embargo, automatizar el registro no significa eliminar la responsabilidad sobre aquello que se está registrando. Cada capacidad necesita tener un origen verificable, una versión de referencia y un responsable identificable. La infraestructura debe poder determinar quién mantiene la herramienta, qué contrato está publicado y qué agentes o aplicaciones pueden utilizarla.

También necesitamos considerar la consistencia entre el catálogo y la ejecución. Imaginemos que una herramienta modifica su contrato mientras un agente todavía utiliza una definición anterior. El descubrimiento puede haberse realizado correctamente, pero la ejecución fallará porque la información utilizada por el agente ya no corresponde a la versión ofrecida por el servidor.

Por lo tanto, el ciclo de vida no termina con el registro. Necesitamos administrar la compatibilidad, el versionado y la discontinuación, garantizando que las definiciones presentadas a los agentes correspondan a las capacidades efectivamente disponibles.

En el fondo, estamos introduciendo una nueva preocupación arquitectónica: no basta con construir un catálogo de capacidades. Necesitamos construir una infraestructura capaz de descubrir, registrar, validar, versionar y mantener continuamente ese catálogo.

## ¿Y si el agente no necesitara mantener todas las conexiones?

Existe otra posibilidad que considero particularmente interesante, incluso a partir de una dificultad que encuentro en el uso cotidiano de agentes con múltiples servidores MCP.

En determinadas situaciones, necesito activar o desactivar manualmente conexiones con servidores que no forman parte del contexto de la tarea. La razón es sencilla: mantener muchas herramientas disponibles simultáneamente puede interferir en la selección de aquellas que realmente interesan para la ejecución.

Esta experiencia sugiere que quizás no sea suficiente controlar qué definiciones de herramientas se cargan en el contexto. También podríamos necesitar una capa responsable de administrar dinámicamente las propias conexiones con los servidores.

Imaginemos un enrutador inteligente, un Intelligent MCP Router, que recibiera la demanda del agente, interpretara su intención e identificara qué dominios funcionales serían necesarios. A partir de este análisis, podría consultar el catálogo, localizar las capacidades relevantes y poner sus herramientas a disposición mediante los servidores correspondientes.

Si durante la tarea surgiera la necesidad de una nueva capacidad, el enrutador podría realizar otra consulta, identificar el servidor responsable e incorporar las nuevas herramientas al conjunto disponible.

Del mismo modo, los servidores que dejaran de ser relevantes podrían tener sus herramientas retiradas del conjunto expuesto al agente. Dependiendo de la estrategia de conexión adoptada, sus sesiones también podrían cerrarse.

La infraestructura pasaría a administrar dinámicamente el universo de posibilidades presentado al modelo.

Este enfoque, que podríamos denominar Context-Aware MCP Routing, añade una dimensión interesante a la arquitectura. El enrutador no sería únicamente un intermediario responsable de encaminar llamadas. Participaría en la administración del contexto operativo del agente.

Sin embargo, existe una distinción técnica importante. Desconectar un servidor MCP no es lo mismo que simplemente dejar de exponer sus herramientas al modelo. Podemos mantener una sesión activa y controlar qué herramientas se ponen a disposición. También podemos mantener el servidor conectado, pero no cargar sus definiciones en el contexto actual.

Cada alternativa tiene costes diferentes. Establecer conexiones bajo demanda puede introducir latencia, mientras que mantener sesiones abiertas puede consumir recursos. Algunos servidores también poseen estados que no pueden descartarse arbitrariamente.

Por eso, no creo que la solución esté necesariamente en conectar y desconectar servidores continuamente. Una arquitectura más eficiente probablemente combinará diferentes estrategias: mantener determinados servidores disponibles, cargar herramientas de forma selectiva y activar nuevas conexiones solo cuando sea necesario.

También es importante separar la selección contextual del enrutamiento de ejecución. Una herramienta puede considerarse relevante sin estar autorizada para un determinado agente. Del mismo modo, una capacidad puede estar disponible y autorizada, pero no tener sentido para la tarea actual.

El enrutador debe respetar estas fronteras. La selección semántica no sustituye a la autorización. La identidad del agente, el contexto del usuario, los permisos, las políticas de dominio y la auditoría deben tenerse en cuenta antes de que una herramienta esté disponible o se ejecute.

Esta distinción es especialmente importante en entornos corporativos, en los que determinadas operaciones pueden producir efectos financieros, modificar información o acceder a datos protegidos. La infraestructura no puede delegar en el modelo la decisión sobre aquello que está autorizado a hacer.

## Una arquitectura en múltiples planos

Cuando reunimos estas ideas, comenzamos a percibir que el problema no tiene una única dimensión. La organización de los servidores, el registro de las capacidades, el descubrimiento contextual y la ejecución de las herramientas son responsabilidades relacionadas, pero no necesitan estar concentradas en el mismo componente.

Una forma de organizar esta arquitectura sería separarla en tres planos. El primero sería el plano de control, responsable del catálogo global de capacidades, metadatos, contratos, versionado, ownership y políticas de gobernanza. Su función sería mantener una representación confiable de aquello que la organización ofrece a través de sus servidores MCP.

El segundo sería el plano de descubrimiento y selección, responsable de interpretar las necesidades planteadas, consultar el catálogo, identificar capacidades relevantes y determinar qué herramientas deben ponerse a disposición en un contexto determinado. Es en este plano donde el descubrimiento progresivo y la selección contextual cobrarían forma.

El tercero sería el plano de ejecución, responsable de las conexiones con los servidores, autenticación, autorización, invocación de las herramientas, tratamiento de los resultados y observabilidad. Aquí, los servidores MCP seguirían distribuidos y bajo la responsabilidad de sus respectivos dominios de negocio.

Esta separación permite combinar la gobernanza corporativa con la autonomía de los productos. El catálogo puede ser compartido, mientras que los servidores permanecen distribuidos. El descubrimiento puede utilizar mecanismos centralizados, mientras que la ejecución sigue siendo responsabilidad de los sistemas de origen. El enrutamiento puede ser coordinado por una capa común sin exigir que todas las herramientas pasen a residir en un único servidor.

Es importante observar que esta división representa una separación lógica de responsabilidades, no necesariamente tres plataformas o servicios independientes. Dependiendo del tamaño de la organización, algunas de estas funciones pueden coexistir en el mismo componente. El objetivo es evitar que las decisiones de descubrimiento, gobernanza y ejecución queden acopladas únicamente porque pertenecen al mismo ecosistema MCP.

Esta arquitectura también permite que el mecanismo de selección evolucione independientemente de los servidores. Podemos mejorar la búsqueda semántica, modificar los criterios de ranking, incorporar nuevas políticas o cambiar la estrategia de conexión sin exigir que cada producto reestructure sus integraciones.

El propio catálogo puede evolucionar para representar no solo herramientas individuales, sino también capacidades compuestas, que dependen de operaciones ofrecidas por diferentes servidores. En este escenario, comienza a funcionar como un mapa de las capacidades corporativas, acercando la visión técnica de los servicios a aquello que la organización realmente puede realizar.

## El nuevo desafío de la arquitectura MCP

La adopción de arquitecturas agénticas en entornos corporativos amplía el alcance de las decisiones de integración. No basta con definir cómo los sistemas exponen sus funcionalidades; es necesario establecer cómo se describirán, localizarán, seleccionarán y pondrán a disposición de acuerdo con las necesidades de cada agente.

El MCP ofrece una interfaz estandarizada para conectar modelos con herramientas, pero no resuelve por sí solo la organización de este ecosistema. Esa responsabilidad corresponde a la arquitectura que lo rodea, incluidos los mecanismos de catalogación, descubrimiento, gobernanza y enrutamiento. Es en este nivel donde resulta posible conciliar la distribución de capacidades entre diferentes dominios con una gestión coherente de su utilización.

Las decisiones sobre la granularidad de los servidores, la selección contextual y la separación entre descubrimiento, autorización y ejecución tendrán consecuencias directas sobre la escalabilidad y la gobernanza de las plataformas agénticas. Más que una cuestión de implementación del protocolo, se trata de definir cómo pretende la organización administrar sus capacidades en un escenario en el que los agentes comienzan a interactuar con un conjunto cada vez más amplio de sistemas.

El desafío arquitectónico consiste en transformar esta diversidad de recursos en un ecosistema que pueda explorarse de forma selectiva, segura y eficiente, sin transferir al agente la complejidad de administrar toda la infraestructura que lo sustenta.
