# Service as a Service: cuando los servicios se convierten en capacidades consumibles

_Si aprendimos a consumir infraestructura, plataformas y software como servicio, ¿por qué seguimos tratando tantos servicios como entregas aisladas?_

**Resumen**: En este artículo, propongo una reflexión: si aprendimos a consumir infraestructura, plataformas y software como servicios, ¿por qué seguimos tratando tantas capacidades de las organizaciones como entregas aisladas? Creo que podemos cambiar esta perspectiva, pensando en servicios que puedan descubrirse, accederse y consumirse continuamente por diferentes áreas, aplicaciones y procesos. Esto exige mirar más allá de la entrega de proyectos y considerar cómo estas capacidades se ponen a disposición, se operan, se gobiernan y evolucionan a lo largo del tiempo. No se trata de crear otro modelo arquitectónico, sino de cuestionarnos si estamos aprovechando todo el valor de aquello que ya hemos construido.

---

Existe un cambio importante en la forma en que consumimos tecnología. Durante mucho tiempo, para utilizar determinada capacidad computacional, una empresa necesitaba adquirir equipos, instalar sistemas, configurar entornos y mantener toda la estructura necesaria para operarlos. La evolución de los modelos de servicio cambió esta relación. Pasamos a consumir infraestructura, plataformas y software sin necesariamente poseer o administrar los recursos que los sustentan. Más que un cambio tecnológico, fue una transformación en la manera de pensar el acceso, la responsabilidad y el valor.

Esta evolución me llevó a una reflexión: si aprendimos a ofrecer infraestructura, plataformas y software como servicios, ¿por qué todavía tenemos tanta dificultad para pensar de la misma manera en los servicios que ofrecen nuestras propias organizaciones?

La provocación que propongo llamar Service as a Service parte de esta pregunta. No se trata de presentar un nuevo modelo arquitectónico, una metodología o una categoría que necesite disputar espacio con conceptos ya establecidos. Es una manera de mirar algo que ya existe, pero que no siempre se concibe para ser reutilizado, accesible y consumido continuamente. La idea es simple: ¿y si empezáramos a tratar los servicios de una organización como capacidades disponibles para diferentes consumidores, en lugar de entregas vinculadas a proyectos, equipos o estructuras específicas?

## De la tecnología consumida a la capacidad organizacional

La idea de consumir software como servicio no es nueva. Desde hace décadas, las empresas utilizan aplicaciones alojadas y operadas por terceros, sin necesidad de instalar, administrar o mantener toda la estructura necesaria para su ejecución. El modelo ganó escala y protagonismo con la expansión de internet y, posteriormente, con la computación en la nube, pero su esencia es anterior a estos movimientos: ofrecer acceso a una capacidad tecnológica sin transferir al consumidor toda la responsabilidad de construirla y operarla.

Con la evolución de la computación en la nube, esta lógica comenzó a alcanzar otras capas. La infraestructura, antes adquirida y administrada directamente por las empresas, pasó a ser consumible como servicio. Las plataformas de desarrollo también comenzaron a ofrecerse bajo demanda, abstrayendo parte de la complejidad de preparar y mantener entornos tecnológicos. Así se consolidaron los modelos que conocemos como SaaS, IaaS y PaaS.

Aunque atienden necesidades diferentes, estos modelos comparten una característica importante: cambian la relación entre quien ofrece una capacidad y quien la utiliza. El consumidor no necesita necesariamente conocer ni administrar todos los componentes que hacen posible el servicio. Necesita comprender qué está disponible, cómo acceder a ello, qué resultados puede esperar y qué responsabilidades permanecen bajo su control. La complejidad no desaparece, sino que pasa a ser administrada en otra capa y, muchas veces, por otro responsable. Así, el consumidor puede concentrar sus esfuerzos en aquello que pretende realizar, en lugar de tener que construir y operar todo lo necesario para alcanzar el resultado.

Esta lógica, ya consolidada en el universo de la tecnología, me lleva a una pregunta: ¿por qué no pensar de la misma manera sobre las capacidades que existen dentro de las propias organizaciones?

Es común encontrar empresas en las que determinadas capacidades se desarrollan para atender una necesidad específica. Un proyecto identifica un problema, moviliza un equipo, define un alcance y entrega una solución. El resultado pasa a ser utilizado por una aplicación, un área de negocio o un proceso. Sin embargo, en muchos casos, la capacidad permanece fuertemente asociada al contexto que motivó su creación.

El problema aparece cuando otra área identifica una necesidad similar. En lugar de consumir algo que ya existe, puede ser necesario iniciar un nuevo proyecto, negociar prioridades, encontrar a los responsables de la solución original y construir integraciones específicas. Incluso cuando la capacidad podría reutilizarse, su disponibilidad no es necesariamente evidente, su acceso puede no estar estructurado y su consumo puede depender de acuerdos informales.

Esto sucede porque con frecuencia organizamos la entrega de tecnología en torno a proyectos y sistemas, pero no necesariamente organizamos la disponibilidad de las capacidades que esos proyectos producen. El proyecto tiene inicio, alcance, presupuesto y cierre. La capacidad, por otro lado, puede seguir generando valor durante muchos años, atendiendo a diferentes consumidores y participando en procesos que ni siquiera existían cuando fue creada.

Quizás sea útil, por lo tanto, separar la entrega que dio origen a una capacidad de la propia capacidad que permanece disponible después de ella. Un servicio no necesita existir únicamente porque un proyecto requiere su implementación o porque una aplicación específica depende de él. Puede concebirse para atender una necesidad recurrente, con diferentes consumidores y formas de utilización que evolucionan a lo largo del tiempo.

Esto no significa transformar todo en un servicio compartido, ni presuponer que toda funcionalidad deba exponerse a toda la organización. Significa reconocer que algunas capacidades tienen valor más allá del contexto en el que fueron desarrolladas inicialmente y que ese valor puede ampliarse cuando su disponibilidad y consumo se piensan de manera deliberada.

## Servicio no es simplemente producto

Vale la pena hacer una distinción. Cuando hablo de servicio, no me refiero necesariamente a un producto de software o a una aplicación. Un producto suele reconocerse por su propuesta de valor, sus usuarios y la experiencia que ofrece. Un servicio puede estar detrás de varios productos y procesos, haciendo posible una capacidad específica sin necesidad de presentarse como una solución completa para el consumidor.

Una aplicación puede, por ejemplo, ofrecer una experiencia de pago. Detrás de ella existen diferentes capacidades: autenticación, validación de datos, análisis de riesgo, autorización, liquidación y notificación. Estas capacidades pueden estar distribuidas entre diferentes sistemas y equipos, pero no necesitan ser consumidas exclusivamente por la aplicación que las reunió inicialmente.

La diferencia está en la perspectiva. Cuando pensamos únicamente en el producto o la aplicación, tendemos a organizar la solución en torno a la experiencia final. Cuando también pensamos en las capacidades que la sustentan, comenzamos a identificar oportunidades de reutilización y composición. Un mismo servicio puede participar en diferentes productos, recorridos y procesos, siempre que exista una forma clara de acceder a él y comprender sus condiciones de uso.

Una analogía ayuda a concretar la idea. Imaginemos una institución financiera que desarrolla una capacidad de prevención del fraude. En el modelo más restringido, esta capacidad puede surgir como parte de un proyecto de tarjetas, con reglas, integraciones e infraestructura orientadas a ese contexto. Si otra área quiere utilizarla en un proceso de apertura de cuentas o en una transferencia, quizás necesite desarrollar una solución propia o negociar una integración específica con el equipo responsable.

Desde una perspectiva de servicio, la capacidad de prevención del fraude pasa a concebirse para atender diferentes contextos de negocio. Cada consumidor proporciona la información necesaria, recibe una evaluación de riesgo y utiliza el resultado dentro de su propio proceso. El servicio puede evolucionar internamente, incorporar nuevos modelos analíticos y perfeccionar sus mecanismos de detección sin exigir que cada consumidor reconstruya esta capacidad.

Naturalmente, esto no significa que todos los contextos deban recibir la misma respuesta o utilizar exactamente las mismas reglas. Una transacción con tarjeta, una apertura de cuenta y una transferencia tienen características y riesgos distintos. El servicio necesita ofrecer parámetros, contratos y posibilidades de configuración compatibles con estas diferencias. La reutilización no consiste en obligar a todos los consumidores a hacer lo mismo, sino en evitar que cada uno tenga que construir y operar, de manera aislada, una capacidad que podría compartirse.

## Consumir no significa simplemente llamar a una API

Cuando hablamos de poner servicios a disposición, es común asociar inmediatamente la idea con las API. De hecho, son un mecanismo importante para exponer capacidades de manera estructurada, con contratos explícitos e integración entre sistemas. Pero reducir el consumo de servicios a llamadas a API limitaría innecesariamente la discusión.

Una capacidad puede consumirse mediante diferentes mecanismos, dependiendo de la naturaleza de la interacción. Puede existir una interfaz para la interacción humana, una API para la comunicación síncrona entre aplicaciones, eventos para notificar cambios de estado, colas para procesar solicitudes de forma asíncrona o automatizaciones para ejecutar actividades recurrentes. El mecanismo debe ser una consecuencia de la necesidad de consumo, y no una decisión que defina previamente lo que el servicio puede ser.

Esta distinción adquiere aún más relevancia con la evolución de la inteligencia artificial. Los agentes de IA comienzan a actuar como consumidores de capacidades organizacionales. En lugar de limitarse a presentar información o responder preguntas, pueden identificar una necesidad, seleccionar una herramienta, solicitar una operación y combinar diferentes servicios para completar una tarea.

Iniciativas y estándares como MCP y A2A ayudan a ilustrar este movimiento. El primero está asociado a la conexión de modelos y agentes con herramientas y fuentes de contexto; el segundo, a la comunicación y colaboración entre agentes. No es necesario asumir que estos estándares serán la forma definitiva de integración para reconocer el punto central: los consumidores de servicios están dejando de ser exclusivamente aplicaciones tradicionales y usuarios humanos.

Esto amplía la importancia de hacer que las capacidades sean fáciles de descubrir, comprender y acceder mediante contratos claros. Un agente necesita saber qué hace un servicio, qué información debe proporcionar, qué resultados puede recibir y qué operaciones está autorizado a ejecutar. En este escenario, una capacidad mal documentada o dependiente del conocimiento informal se vuelve aún más difícil de consumir.

La cuestión, por lo tanto, no es simplemente poner más API a disposición o adoptar nuevos protocolos. Es pensar en la experiencia de consumo de una capacidad, independientemente de quién o qué la esté consumiendo.

## Qué debe existir detrás de un servicio

Poner una capacidad a disposición de diferentes consumidores exige algo más que crear un punto de integración. Es necesario establecer un conjunto de condiciones que permita su uso de manera predecible y sostenible.

El primer aspecto es el contrato. El consumidor necesita comprender qué ofrece el servicio, qué información se requiere, qué resultados se producirán y qué limitaciones existen. El contrato también debe dejar claras las condiciones de uso, los comportamientos esperados y las responsabilidades de cada parte. Sin esto, la integración puede incluso funcionar técnicamente, pero seguirá dependiendo del conocimiento tácito y de negociaciones específicas.

También es necesario gestionar la identidad, la autenticación, la autorización y la segregación de accesos. No todos los consumidores pueden ejecutar todas las operaciones, y diferentes contextos pueden exigir distintos niveles de permisos. La seguridad no puede ser un complemento incorporado después de que el servicio ya esté disponible. Forma parte del propio modelo de consumo.

Otro punto es la operación. Un servicio consumido por diferentes áreas o aplicaciones pasa a tener un impacto potencialmente mayor que una solución restringida a un único contexto. La disponibilidad, el rendimiento, la capacidad, la observabilidad, la continuidad y el tratamiento de fallos dejan de ser preocupaciones internas del equipo responsable y pasan a influir directamente en la experiencia de los consumidores. El versionado y la compatibilidad también deben tenerse en cuenta, porque la evolución del servicio no puede interrumpir arbitrariamente a quienes dependen de él.

Todo esto exige una definición clara de responsabilidades. ¿Quién es el responsable del servicio? ¿Quién decide su evolución? ¿Quién prioriza las mejoras? ¿Quién responde cuando la capacidad deja de cumplir el nivel esperado? ¿Quién evalúa el impacto de un cambio sobre los consumidores existentes?

Estas preguntas revelan una dimensión organizacional importante. Un servicio no se sostiene únicamente porque exista un equipo técnico capaz de mantenerlo. Es necesario que haya ownership sobre la capacidad, con responsabilidad por su evolución y por su valor a lo largo del tiempo. Esto no significa necesariamente crear un equipo independiente para cada servicio, sino reconocer que la responsabilidad sobre la capacidad no termina con la entrega del proyecto que le dio origen.

Es un cambio sutil, pero relevante: el éxito deja de medirse únicamente por la finalización de la implementación y pasa a considerar también la calidad y la continuidad del servicio ofrecido.

## Compartir tiene costes y límites

La idea de transformar capacidades en servicios consumibles puede parecer naturalmente ventajosa. La reutilización evita duplicaciones, concentra conocimiento y permite que diferentes áreas se beneficien de una misma implementación. Pero compartir también crea dependencias y costes que deben tenerse en cuenta.

Un servicio utilizado por muchos consumidores puede convertirse en un punto crítico de la organización. Un cambio aparentemente sencillo puede afectar a procesos distintos, cada uno con sus propias reglas, prioridades y ventanas de cambio. La necesidad de atender múltiples contextos puede aumentar la complejidad del contrato y dificultar la evolución. En algunos casos, la abstracción creada para atender a todos acaba siendo tan genérica que deja de atender bien a cualquiera.

También existe el riesgo de centralizar excesivamente capacidades que deberían permanecer cerca del contexto de negocio. No toda funcionalidad necesita compartirse. Algunas son específicas, poco reutilizables o dependen de decisiones locales. El coste de crear y operar un servicio común puede ser mayor que el beneficio de su reutilización.

Por eso, la cuestión no debería ser transformar todo en un servicio, sino identificar dónde existe una capacidad con potencial para atender a diferentes consumidores de manera consistente. La decisión debe considerar la frecuencia de uso, el grado de especialización, la criticidad, el coste de mantenimiento, las dependencias y la autonomía necesaria de los consumidores.

La estandarización también tiene límites. Un servicio compartido no debe imponer una uniformidad artificial a procesos que tienen necesidades legítimas diferentes. El objetivo es ofrecer una capacidad común sin borrar las particularidades de los contextos en los que se utilizará. Encontrar este equilibrio forma parte del trabajo de arquitectura, pero también de gestión y gobernanza.

## De la entrega de proyectos a la disponibilidad de capacidades

Quizás la principal reflexión que plantea Service as a Service no esté en la tecnología, sino en la forma en que las organizaciones se estructuran para producir y ofrecer valor.

En muchas empresas, los proyectos son la principal unidad de movilización de recursos y ejecución de cambios. Esto tiene sentido: los proyectos ayudan a organizar inversiones, establecer objetivos, controlar el alcance y coordinar entregas. El problema surge cuando esta lógica también pasa a determinar la forma en que las capacidades se mantienen y consumen después de que la entrega termina.

Una organización puede concluir decenas de proyectos exitosos y, aun así, acumular soluciones fragmentadas, integraciones redundantes y capacidades difíciles de reutilizar. Cada iniciativa resuelve su problema, pero el conjunto no necesariamente evoluciona como un ecosistema coherente.

Pensar en los servicios como capacidades consumibles sugiere otra perspectiva. Los proyectos siguen siendo importantes para crear o transformar soluciones, pero las capacidades resultantes pueden tener un ciclo de vida propio. Necesitan ser descubiertas, accesibles, operadas, gobernadas y mejoradas continuamente. Su valor no está únicamente en lo que entregaron en el pasado, sino en lo que todavía pueden hacer posible para diferentes consumidores.

Esta visión también acerca la arquitectura a la gestión. La arquitectura deja de mirar solamente los componentes y las integraciones de una solución específica y pasa a considerar cómo se relacionan las capacidades, cuáles pueden compartirse y qué dependencias surgen cuando diferentes partes de la organización comienzan a consumirlas. La gestión, a su vez, necesita considerar la continuidad de estas capacidades, su priorización y la responsabilidad por su evolución.

No se trata de sustituir una estructura orientada a proyectos por otra estructura rígida, organizada en torno a servicios. Se trata de reconocer que la entrega de una solución y la disponibilidad de una capacidad son problemas relacionados, pero diferentes. Confundirlos puede hacer que la organización sea eficiente en la entrega de proyectos y poco eficiente en el aprovechamiento de lo que ha construido.

## Una provocación, no una nueva receta

Quizás Service as a Service no necesite ser más que una provocación. No es un intento de cambiar el nombre de conceptos conocidos, proponer una nueva arquitectura o establecer un modelo universal. SOA, las API, las plataformas internas, la arquitectura orientada a eventos y la gestión de capacidades ya abordan partes importantes de esta discusión. Lo que me interesa es la pregunta que surge cuando acercamos estas ideas a la manera en que las organizaciones trabajan realmente.

Si conseguimos consumir infraestructura, plataformas y software como servicios, ¿por qué tantas capacidades organizacionales siguen tratándose como entregas aisladas? ¿Por qué necesitamos reconstruir soluciones que ya existen? ¿Por qué el acceso a determinadas capacidades depende tanto de conocer al equipo adecuado, negociar una integración específica o encontrar a alguien que sepa cómo funciona determinado sistema?

Quizás parte de la respuesta esté en la forma en que concebimos nuestras soluciones. Construimos proyectos, aplicaciones y sistemas para resolver problemas concretos, pero no siempre pensamos en las capacidades que estamos creando como algo que podrá ser consumido por otros, de manera independiente y continua.

Cambiar esta perspectiva no exige transformar todo en servicio ni adoptar una tecnología específica. Exige reconocer cuándo una capacidad tiene valor más allá de su contexto original y considerar, desde su concepción, cómo podría ponerse a disposición de otros consumidores.

Al final, la pregunta no es si necesitamos otro modelo arquitectónico. Es si estamos aprovechando todo el valor de las capacidades que ya hemos construido. Quizás sea hora de dejar de pensar únicamente en las soluciones que entregamos y empezar a pensar también en los servicios que somos capaces de ofrecer continuamente.
