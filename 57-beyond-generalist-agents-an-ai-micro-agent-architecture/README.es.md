# Más allá de los Agentes Generalistas: Una Arquitectura de Microagentes de IA

_Especialización de responsabilidades cognitivas, contextos selectivos y composición dinámica de agentes._

**Resumen**: Creo que la evolución de los agentes de IA no depende de concentrar cada vez más capacidades en un único agente, sino de distribuir las responsabilidades cognitivas entre agentes especializados, cada uno con un contexto, una autonomía y unos límites bien definidos. Propongo organizar esta especialización mediante una arquitectura que componga equipos dinámicamente, reutilice capacidades existentes y preserve la visión del conjunto a través de una coordinación arquitectónica. Más que multiplicar agentes o paralelizar tareas, la cuestión es definir quién debe pensar sobre qué, con qué contexto y bajo qué responsabilidades. Es en esta organización donde veo el camino para construir soluciones de IA más coherentes, controlables y eficientes.

---

Me gusta seguir la evolución de los proyectos de inteligencia artificial disponibles en GitHub. Es interesante observar cómo la comunidad experimenta con diferentes formas de construir agentes, amplía sus capacidades, incorpora herramientas y desarrolla nuevas estrategias de ejecución. Los agentes que antes se limitaban a responder preguntas hoy pueden navegar por internet, interpretar documentos, escribir código, ejecutar comandos, consumir APIs y llevar a cabo flujos de trabajo con diferentes niveles de autonomía. Esta evolución amplía el campo de aplicación de la tecnología, pero también plantea una cuestión arquitectónica que considero cada vez más relevante: ¿hasta qué punto tiene sentido concentrar tantas capacidades en un único agente?

La idea de un agente capaz de llevar adelante un proyecto entero resulta atractiva. Recibe una solicitud, interpreta los requisitos, planifica la solución, desarrolla el código, crea pruebas, configura la infraestructura y entrega el resultado. Para ello, acumula instrucciones, herramientas, skills y conocimientos de diferentes disciplinas. A medida que los modelos se vuelven más capaces, parece natural ampliar aún más ese alcance. Sin embargo, la capacidad de ejecutar actividades distintas no significa que todas deban estar concentradas en la misma unidad.

Esta discusión me remite a un problema conocido en la arquitectura de software: la concentración excesiva de responsabilidades en sistemas monolíticos. Un monolito puede ser una elección adecuada, especialmente cuando el sistema todavía es sencillo. La dificultad aparece cuando funcionalidades de distinta naturaleza empiezan a compartir una estructura cada vez más compleja, lo que dificulta la evolución, el mantenimiento y la comprensión del sistema. La descomposición en componentes o servicios especializados surgió, entre otras razones, para establecer fronteras más claras y permitir que cada parte evolucione con mayor independencia.

Veo un paralelismo con la construcción de agentes de IA. Un agente generalista puede acumular conocimientos y herramientas de diversas áreas, pero esa amplitud también aumenta la complejidad de sus instrucciones, de su contexto y de sus decisiones. El problema no está en poseer muchas capacidades, sino en tener que movilizarlas todas, o considerar su existencia, incluso cuando la tarea exige solo una parte de ese conocimiento.

La comparación con los microservicios debe entenderse como una analogía organizativa, no como una propuesta de reproducir literalmente esa arquitectura. En los sistemas distribuidos, la descomposición busca delimitar responsabilidades funcionales. En una arquitectura de agentes, la cuestión central es delimitar responsabilidades cognitivas: qué conocimientos deben estar disponibles, qué decisiones corresponden a cada agente y qué resultados deben producirse para que el conjunto funcione de manera coherente.

Esta discusión no parte de cero. La especialización, la delegación, la orquestación y la colaboración entre agentes ya forman parte de las investigaciones e implementaciones de sistemas multiagente. Tampoco pretendo reivindicar la creación de un nuevo paradigma ni la autoría exclusiva del concepto de microagentes. Lo que me interesa es organizar estos principios en una propuesta arquitectónica que explore la descomposición de responsabilidades cognitivas, la selección de contextos y la composición dinámica de equipos. A lo largo de este artículo, utilizo el nombre Micro-Agent Architecture (MAA) para identificar esta organización específica de conceptos y mecanismos.

La pregunta que orienta la propuesta es sencilla: en lugar de ampliar indefinidamente las capacidades de un único agente, ¿cómo podemos estructurar diferentes especialidades para resolver problemas complejos sin perder la visión del conjunto?

## El contexto como decisión arquitectónica

Una de las características más valoradas de los modelos actuales es la capacidad de trabajar con ventanas de contexto cada vez mayores. Esto permite proporcionar documentos extensos, historiales de conversaciones, instrucciones detalladas y grandes volúmenes de información en una única interacción. Es una evolución importante, pero existe una interpretación que merece ser cuestionada: la idea de que cuanto más contexto recibe un agente, mejor será su capacidad para resolver problemas.

El contexto es un recurso, no un objetivo. Su valor depende de la relación entre la información disponible y la responsabilidad que el agente debe ejecutar. Un contexto amplio puede ser necesario cuando la tarea exige una visión global, pero también puede introducir información irrelevante, instrucciones contradictorias y conocimientos que no contribuyen a la decisión en cuestión.

Consideremos un agente responsable de implementar una API. Necesita conocer los requisitos funcionales, las reglas de negocio pertinentes, los contratos de integración, los estándares de desarrollo y las restricciones técnicas del backend. Dependiendo de la tarea, también tendrá que consultar información sobre persistencia, autenticación y seguridad. Esto no significa que necesite cargar permanentemente todas las instrucciones de diseño de interfaces, los criterios de experiencia de usuario o el historial completo de las decisiones de infraestructura.

Esta información puede ser importante para el proyecto, pero no necesariamente para todas las ejecuciones de ese agente. Cuando se concentran responsabilidades heterogéneas en una única unidad, tendemos a ampliar su conjunto de instrucciones, herramientas y conocimientos disponibles. El modelo necesita interpretar qué directrices se aplican, qué herramientas son pertinentes y qué información debe influir en su respuesta. El resultado puede ser un contexto más costoso y difícil de administrar, sin que ello represente necesariamente una mejora de calidad.

No se trata de afirmar que los contextos extensos siempre perjudican el rendimiento. Hay decisiones que exigen una visión sistémica, y retirar información relevante puede comprometer la solución. El problema está en el contexto indiscriminado, no en la amplitud en sí misma. La arquitectura debe distinguir el conocimiento necesario para comprender el problema del necesario para ejecutar cada responsabilidad.

Un agente responsable de la visión arquitectónica necesita conocer los requisitos, las principales decisiones, las interfaces, las restricciones y las dependencias de la solución. Eso no significa que necesite cargar todos los detalles operativos de cada especialidad. Del mismo modo, un especialista necesita profundidad en su propio dominio, pero no necesariamente todo el conocimiento utilizado por los demás agentes.

Esta distinción conduce a una separación importante entre el conocimiento disponible y el contexto efectivamente utilizado. El sistema puede mantener un catálogo amplio de skills, documentos, decisiones e información, mientras que cada agente recibe únicamente el conjunto pertinente para su responsabilidad y para la ejecución actual. Cuando sea necesario, puede consultar información adicional mediante mecanismos de recuperación, como RAG, sin tener que incorporar permanentemente todo el conocimiento a su configuración.

El catálogo global de capacidades puede ser amplio. El perfil de cada agente debe ser específico. Y el contexto de ejecución debe seleccionarse de acuerdo con la tarea. Esta es una de las premisas que orientan la organización propuesta.

## Descomponer responsabilidades antes de paralelizar tareas

Cuando se habla de arquitecturas multiagente, es habitual que la discusión comience por la distribución de tareas y la posibilidad de ejecución en paralelo. Varios agentes trabajan simultáneamente en diferentes partes de un problema, mientras que un mecanismo de orquestación coordina las actividades y reúne los resultados. Este modelo tiene aplicaciones legítimas, pero no considero que la paralelización sea el punto de partida para diseñar un equipo de agentes.

Antes de decidir cuántos agentes pueden trabajar al mismo tiempo, necesitamos comprender qué responsabilidades existen y qué conocimientos, criterios de decisión y contextos se necesitan para ejecutarlas. La primera pregunta no es cómo distribuir el trabajo, sino cómo organizar el razonamiento necesario para resolver el problema.

Consideremos el desarrollo de una aplicación bancaria. La solución puede involucrar reglas de negocio, arquitectura, interfaces, servicios, persistencia de datos, seguridad, pruebas e infraestructura. Estas disciplinas tienen conceptos, restricciones y criterios de calidad propios. Un agente generalista puede ser capaz de trabajar en todas ellas, pero eso no significa que concentrar todo ese conocimiento en un único contexto sea la mejor decisión.

Una alternativa es reconocer estas fronteras y organizar agentes especializados por dominio. Un agente puede responsabilizarse de las funciones de frontend, otro de las de backend, otro del modelado y la persistencia de datos, mientras que especialistas adicionales se encargan de la seguridad, la calidad o la infraestructura. La división no necesita corresponder a departamentos, cargos o tecnologías. El criterio debe ser la coherencia entre el conocimiento necesario, las decisiones que deben tomarse y los resultados esperados.

Tampoco tiene sentido crear un agente para cada lenguaje, framework, archivo o pequeña actividad. Eso solo sustituiría un agente excesivamente amplio por una estructura fragmentada, con elevados costes de comunicación y coordinación. La especialización debe encontrar un equilibrio: la responsabilidad debe estar suficientemente delimitada para permitir profundidad, pero ser lo bastante amplia como para producir un resultado consistente.

Esta decisión depende de la naturaleza del problema. Una solicitud sencilla puede resolverse con un único agente. Un proyecto más complejo puede justificar varios especialistas, cada uno responsable de una parte coherente de la solución. La cantidad de agentes no es, por sí sola, un indicador de calidad. El objetivo es encontrar la composición mínima capaz de cubrir adecuadamente las responsabilidades involucradas.

La paralelización puede surgir después, como una estrategia de ejecución. Un agente de backend puede dividir su trabajo entre agentes auxiliares, delegar una actividad específica o ejecutarlo todo de forma secuencial. Esta decisión depende de las características de la tarea, de las dependencias existentes y de los contratos establecidos. La arquitectura no debe imponer concurrencia cuando esta no aporta ningún beneficio.

Esta perspectiva cambia el enfoque del diseño de sistemas multiagente. En lugar de comenzar por la distribución de tareas, comenzamos por la descomposición cognitiva. Primero definimos quién debe pensar sobre qué. Después decidimos cómo y cuándo se ejecutarán esas responsabilidades.

## La composición dinámica de equipos

Una vez identificadas las responsabilidades, surge una cuestión práctica: ¿quién define qué agentes deben existir, qué capacidades necesita cada uno y cómo se organizarán estas unidades?

Una posibilidad que considero interesante es estructurar este proceso en torno a un componente denominado Agent Factory. Su función es analizar una solicitud y diseñar el equipo de agentes necesario para atenderla. A diferencia de los especialistas, la Factory necesita una visión amplia de diferentes disciplinas, ya que su trabajo no consiste en ejecutar continuamente las actividades del proyecto, sino en comprender el problema y diseñar una estructura cognitiva adecuada.

A partir de los requisitos, la Factory identifica las principales responsabilidades, establece fronteras, consulta un catálogo de agentes y skills, selecciona herramientas, define permisos y especifica los contratos de comunicación. También evalúa si los agentes existentes pueden reutilizarse o adaptarse, evitando la creación de especialistas innecesarios.

El resultado de este proceso es una composición de agentes con responsabilidades explícitas y capacidades compatibles con cada dominio. Para que esta configuración sea reproducible, considero útil representar cada agente mediante un Agent Blueprint, una especificación estructurada que describe su responsabilidad, sus capacidades, las herramientas disponibles, su perfil de contexto, sus permisos, sus dependencias y sus contratos.

El Blueprint funciona como referencia para la creación, configuración, versionado y evolución de los agentes. En lugar de depender exclusivamente de instrucciones dispersas, el equipo pasa a disponer de una definición explícita de cómo debe actuar cada especialista y qué límites debe respetar. Esto también facilita la reutilización de agentes entre proyectos y permite comparar diferentes configuraciones a lo largo del tiempo.

La Agent Factory actúa principalmente en una etapa que podemos denominar design time. Realiza el análisis y la preparación del equipo antes de la ejecución propiamente dicha. Este trabajo tiene un coste, ya que exige comprender la solicitud, identificar responsabilidades y configurar a los especialistas. Sin embargo, no necesita repetirse íntegramente en cada interacción. Los agentes y equipos pueden reutilizarse, versionarse y adaptarse a medida que evolucionan las necesidades.

La Factory tampoco necesita permanecer involucrada en todas las decisiones operativas. Su función principal es diseñar y construir el equipo. Durante la ejecución, la conducción del proyecto pasa a un agente responsable de preservar la visión sistémica y coordinar la colaboración entre los especialistas.

Esta separación entre composición y ejecución es importante. Diseñar un equipo exige una visión amplia de las capacidades disponibles. Conducir el trabajo exige seguir las decisiones, las dependencias y los resultados sin convertir al coordinador en otro agente responsable de ejecutar todas las actividades.

## El Solution Architect Agent y la visión del conjunto

Un equipo de especialistas necesita preservar la coherencia de la solución. La especialización aumenta la profundidad de actuación, pero también crea el riesgo de que se tomen decisiones locales que no tengan en cuenta sus efectos sobre los demás componentes. Una elección técnicamente adecuada para un dominio puede generar incompatibilidades, dependencias o restricciones en otra parte del sistema.

En este modelo, asigno esta responsabilidad al Solution Architect Agent. Su función es mantener la visión sistémica, interpretar los requisitos, tomar decisiones arquitectónicas, establecer interfaces entre los dominios y coordinar la actuación de los especialistas. Necesita comprender cómo se relacionan las partes, qué restricciones son compartidas y qué decisiones pueden afectar a la solución en su conjunto.

Esto no significa que el arquitecto necesite conocer cada detalle operativo de todos los agentes. Existe una diferencia entre amplitud de responsabilidad y amplitud indiscriminada de contexto. El Solution Architect necesita conocer los requisitos, las decisiones, los contratos, las dependencias y los resultados relevantes de cada dominio. No necesita cargar permanentemente todos los detalles de implementación del frontend, backend, base de datos o infraestructura.

Su visión global debe sustentarse en información estructurada. Hace seguimiento de las decisiones tomadas por los especialistas, evalúa los resultados, identifica conflictos y verifica que el trabajo siga alineado con los objetivos y las restricciones del proyecto. Cuando es necesario, consulta información más específica o solicita aclaraciones al agente responsable del dominio.

Esta función también exige capacidad de adaptación. La composición inicial del equipo es una hipótesis basada en los requisitos conocidos en ese momento. Durante la ejecución, pueden surgir problemas que revelen nuevas necesidades de especialización. El Solution Architect identifica estas situaciones y puede solicitar a la Agent Factory la creación o adaptación de un agente.

La relación entre los componentes queda así delimitada: la Agent Factory diseña y construye el equipo; el Solution Architect preserva la coherencia sistémica y conduce la ejecución; los especialistas se responsabilizan de las decisiones y entregas de sus respectivos dominios.

El arquitecto no necesita centralizar todas las decisiones técnicas. Su responsabilidad es garantizar que las decisiones locales compongan una solución consistente. Esta distinción permite preservar la autonomía de los especialistas sin renunciar a una visión integrada del proyecto.

## Autonomía y especialización recursiva

La especialización no debe producir una estructura rígida en la que todas las decisiones dependan de un coordinador central. Un agente de backend, por ejemplo, recibe una responsabilidad delimitada, pero eso no significa que su implementación deba estar determinada íntegramente por el Solution Architect. Corresponde al especialista evaluar el problema dentro de su dominio, elegir estrategias, organizar actividades y decidir qué recursos son necesarios.

En determinados casos, el propio especialista puede darse cuenta de que la responsabilidad recibida es demasiado compleja para gestionarla eficientemente desde una única unidad. El agente de backend puede identificar la necesidad de separar una actividad de integración, una estrategia de migración o un análisis técnico específico. En otros casos, puede concluir que la división no aportaría ningún beneficio y que el trabajo debe permanecer bajo su responsabilidad.

Esta posibilidad de descomposición recursiva permite que la arquitectura evolucione a medida que se conoce mejor el problema. No es necesario anticipar todos los niveles de especialización durante el análisis inicial. Los agentes pueden identificar nuevas fronteras dentro de sus dominios y proponer una descomposición adicional.

Esta autonomía, sin embargo, debe operar dentro de límites claros. Un especialista no debe modificar unilateralmente decisiones arquitectónicas globales, ignorar contratos de integración ni comprometer requisitos que pertenecen al conjunto de la solución. Su libertad reside en la gestión de su propio dominio, respetando los objetivos, las restricciones y los contratos establecidos.

La creación de nuevos agentes tampoco debe producirse de manera irrestricta. El especialista puede identificar y justificar la necesidad de una nueva unidad, pero la Agent Factory debe evaluar si la responsabilidad realmente exige un agente independiente, si existe algún especialista reutilizable o si basta con una adaptación. El Solution Architect, por su parte, debe evaluar el impacto del cambio en la arquitectura en su conjunto.

De esta manera, la especialización recursiva no significa un crecimiento descontrolado del equipo. Significa permitir que la estructura se adapte a la complejidad encontrada, manteniendo mecanismos de validación y gobernanza. La autonomía está distribuida, pero las fronteras siguen siendo explícitas.

## Contratos y memoria compartida

La colaboración entre agentes especializados exige mecanismos consistentes de comunicación y continuidad. La especialización no puede producir islas de conocimiento que desconozcan el estado del proyecto o tomen decisiones incompatibles entre sí. Para ello, considero fundamentales dos elementos: contratos explícitos y memoria compartida.

Los contratos definen qué recibe cada agente, qué debe entregar, qué criterios debe cumplir y qué situaciones requieren escalamiento. Un contrato puede establecer que el agente de backend debe proporcionar determinados servicios, respetar las interfaces definidas por el arquitecto, documentar las decisiones relevantes e informar de las limitaciones que afecten a otros componentes.

Esta definición reduce las ambigüedades y hace que las responsabilidades sean verificables. En lugar de depender exclusivamente de instrucciones genéricas, cada especialista trabaja con expectativas claras sobre sus entregas y sus límites de actuación. Los contratos también permiten evaluar si una entrega cumple los criterios acordados y si puede ser consumida por los demás agentes.

La memoria compartida complementa este mecanismo. Preserva los requisitos, las decisiones arquitectónicas, las especificaciones, los contratos, los artefactos, el historial relevante y el estado actual del proyecto. De esta manera, un agente no necesita reconstruir todo el contexto en cada interacción, y la información importante no queda restringida al historial privado de una única ejecución.

Es importante distinguir entre memoria compartida y contexto íntegramente compartido. Todos los agentes pueden consultar una misma base de conocimiento sin necesidad de cargar todo su contenido en cada ejecución. El acceso debe ser selectivo, de acuerdo con la responsabilidad y la necesidad del momento. La memoria representa el conocimiento persistente del proyecto; el contexto representa el subconjunto de información efectivamente disponible para el agente durante una ejecución determinada.

Esta separación permite mantener la continuidad sin reproducir el problema de un contexto excesivamente amplio. Un agente puede consultar decisiones arquitectónicas, especificaciones o contratos cuando sea necesario, sin tener que recibir todo el historial del proyecto en cada llamada.

También es necesario definir fuentes de verdad, versionado y mecanismos para gestionar información contradictoria o desactualizada. Una decisión arquitectónica modificada debe reflejarse en los registros pertinentes. Un contrato actualizado no puede coexistir indefinidamente con instrucciones antiguas que algún especialista siga utilizando.

La memoria compartida garantiza la continuidad; los contratos establecen la previsibilidad. Juntos, estos mecanismos permiten que los agentes especializados colaboren sin necesidad de operar con contextos idénticos ni depender de una comunicación informal.

## Una arquitectura lógica, no necesariamente distribuida

Al hablar de una arquitectura de múltiples agentes, no estoy defendiendo que cada especialista deba ejecutarse en un proceso independiente, en un servidor propio o en una infraestructura distribuida. La separación que considero fundamental es lógica y cognitiva.

Cada agente necesita tener una identidad, una responsabilidad, un perfil de capacidades, un contexto y contratos propios. Esto puede implementarse sobre un mismo runtime de agentes, siempre que se preserven las fronteras. La distribución física puede tener sentido cuando existen requisitos de escalabilidad, aislamiento, seguridad, disponibilidad o integración con sistemas distintos, pero es una decisión de implementación, no una condición para que exista la arquitectura.

Esta distinción también ayuda a evitar una interpretación literal de la analogía con los microservicios. La unidad central de descomposición no es el servicio de software, sino la responsabilidad cognitiva. Un agente puede tener un alcance reducido sin ser pequeño en parámetros. Lo que lo caracteriza no es el tamaño del modelo utilizado, sino la delimitación de su responsabilidad y la coherencia entre su contexto y sus capacidades.

Del mismo modo, la cantidad de agentes no debe tratarse como un indicador de calidad. Crear muchos especialistas sin fronteras claras puede generar fragmentación, dependencias excesivas y complejidad de coordinación. El equipo ideal no es el más grande posible, sino la composición mínima capaz de cubrir adecuadamente las responsabilidades del problema.

Este enfoque permite comenzar con una estructura sencilla y evolucionar según las necesidades. Una implementación inicial puede ejecutar todos los agentes en el mismo entorno, compartir una capa de memoria y utilizar contratos para organizar la comunicación. Si los requisitos operativos lo justifican, algunos componentes específicos pueden distribuirse posteriormente. La arquitectura lógica no debe confundirse con la infraestructura elegida para implementarla.

## Eficiencia y viabilidad económica

La especialización ofrece la oportunidad de reducir el volumen de contexto irrelevante, pero no garantiza, por sí sola, un menor consumo total de recursos. La composición de agentes introduce costes adicionales: llamadas entre agentes, transferencia de información, coordinación, planificación y consolidación de resultados. Dependiendo de la tarea, estos costes pueden superar cualquier ahorro obtenido mediante la especialización.

Por eso, sería incorrecto afirmar que los microagentes siempre son más baratos o rápidos. El argumento es que los agentes especializados pueden utilizar su contexto de forma más eficiente, reduciendo la información innecesaria y mejorando la calidad de ejecución en problemas que realmente exigen diferentes especialidades. Se trata de una hipótesis arquitectónica que debe validarse, no de una ventaja garantizada.

La métrica relevante no debe ser únicamente el consumo de tokens por llamada, sino el coste total para completar una tarea con éxito. Es necesario considerar la calidad, el retrabajo, el tiempo de ejecución, la cantidad de interacciones, el esfuerzo de coordinación y el coste de mantenimiento de los agentes. Una solución que consume menos tokens, pero exige más correcciones o produce resultados inconsistentes, no representa necesariamente una mejora.

La Agent Factory también debe incluirse en esta ecuación. Su trabajo de análisis y construcción del equipo representa un coste inicial, pero esta inversión puede amortizarse cuando los agentes se reutilizan en diferentes solicitudes o a lo largo del ciclo de vida de un proyecto. Lo mismo ocurre con los Blueprints, que permiten preservar configuraciones y reducir el esfuerzo necesario para reconstruir equipos con responsabilidades similares.

Este análisis es especialmente importante cuando observamos la propuesta desde la perspectiva de la gestión de proyectos. No basta con demostrar que una tarea puede dividirse entre varios agentes. Es necesario evaluar si la división mejora la previsibilidad, reduce riesgos, aumenta la calidad de las entregas o disminuye el esfuerzo total para alcanzar el resultado esperado.

Una forma simplificada de representar esta relación es considerar el coste total como la suma del coste de creación y configuración del equipo más el coste acumulado de ejecución y coordinación. La especialización será económicamente interesante cuando los beneficios obtenidos compensen estos costes.

Si coordinar un equipo exige un esfuerzo desproporcionado, quizá las fronteras de responsabilidad estén mal definidas, la descomposición haya sido excesiva o los contratos no sean suficientemente claros. La respuesta no es necesariamente crear más agentes, sino revisar la composición y encontrar una estructura más coherente.

## Evolución y validación de la propuesta

La arquitectura descrita en este artículo reúne principios conocidos de ingeniería de software y sistemas multiagente en una organización que considero prometedora para abordar problemas complejos. La especialización de agentes, la separación de responsabilidades, la orquestación y el intercambio de conocimiento no son ideas nuevas por separado. El interés reside en cómo estos elementos pueden combinarse con mecanismos de composición dinámica, especificaciones reutilizables y gobernanza distribuida.

La Agent Factory, los Agent Blueprints, el Solution Architect Agent y la especialización recursiva constituyen el núcleo de la organización propuesta. La Factory prepara el equipo a partir de las necesidades identificadas. Los Blueprints describen las responsabilidades y capacidades de los agentes. El Solution Architect preserva la visión sistémica durante la ejecución. Los especialistas trabajan con autonomía dentro de sus dominios y pueden identificar oportunidades de descomposición adicional, respetando los mecanismos de gobernanza.

Esta estructura todavía necesita explorarse mediante implementaciones concretas. Es necesario evaluar cómo representar los contratos, cómo versionar los Blueprints, cómo controlar los permisos, cómo compartir la memoria y cómo decidir cuándo una responsabilidad justifica la creación de un nuevo agente. También será importante establecer métricas que permitan comparar diferentes configuraciones e identificar en qué escenarios la especialización ofrece realmente ventajas.

No considero que exista una composición universalmente adecuada. El número de agentes, la profundidad de la especialización y el grado de autonomía deben variar en función del problema. En tareas sencillas, un único agente puede seguir siendo la mejor opción. En sistemas más complejos, un equipo especializado puede ofrecer mayor claridad en las responsabilidades, una mejor organización del contexto y una mayor previsibilidad.

El punto central es no confundir capacidad con responsabilidad. El hecho de que un agente pueda trabajar en diferentes disciplinas no significa que sea deseable concentrarlas todas en un único componente. A medida que aumenta la complejidad, resulta importante pensar no solo en lo que los agentes pueden hacer, sino en cómo deben organizarse sus responsabilidades.

La evolución de los agentes de IA no necesita seguir exclusivamente el camino de modelos cada vez más grandes, contextos cada vez más extensos y herramientas cada vez más numerosas. También puede avanzar mediante la calidad de la arquitectura que organiza estas capacidades. Esto exige reconocer las especialidades necesarias, establecer fronteras, definir contratos y coordinar decisiones sin centralizar todo el conocimiento en un único agente.

Quizá la cuestión más importante no sea cuántos agentes pueden trabajar al mismo tiempo, sino cómo identificar qué responsabilidades deben existir, qué conocimientos deben asociarse a cada una de ellas y cómo pueden combinarse estas capacidades de forma coherente.

Antes de decidir cómo distribuir el trabajo, necesitamos responder a una pregunta más fundamental: ¿quién debe pensar sobre qué?
