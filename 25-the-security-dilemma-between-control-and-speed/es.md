# El dilema de Security: entre el control y la velocidad

_El desafío de integrar Security a la ingeniería sin convertir la protección en burocracia._

**Resumen:** Defiendo que el dilema entre Security y velocidad no se resuelve eligiendo un lado, sino acercando Security a la ingeniería y llevando el conocimiento de seguridad al momento en que las decisiones todavía se están construyendo. En lugar de depender de gates, aprobaciones e intervenciones manuales, debemos transformar el conocimiento especializado en patrones, automatización y guardrails proporcionales al riesgo. Así, Security deja de ser una etapa que la ingeniería debe esperar y pasa a ser una capacidad integrada al proceso. El objetivo final no es eliminar los riesgos, sino permitir que la organización aprenda, experimente e innove sabiendo qué riesgos está asumiendo.

---

Durante mucho tiempo, mi visión de Security probablemente fue más simple de lo que realmente es el área. Como alguien que trabaja más cerca de la arquitectura y la ingeniería que de las disciplinas de seguridad, tendía a ver Security de una manera relativamente objetiva: existe un área responsable de seguridad, con políticas, herramientas, procesos, evaluaciones y controles que deben considerarse durante la construcción de las soluciones.

Basta con observar un poco más de cerca, sin embargo, para darse cuenta de hasta qué punto esta visión es limitada. Security es una disciplina mucho más amplia de lo que su nombre sugiere. Identidad, aplicaciones, infraestructura, cloud, datos, arquitectura, privacidad, fraude, respuesta a incidentes, inteligencia, terceros, cumplimiento y muchas otras dimensiones pueden estar directa o indirectamente relacionadas con la seguridad de una organización.

Esta amplitud también explica por qué es difícil hablar de Security como si estuviéramos tratando una única función. El ritmo de un equipo de respuesta a incidentes es diferente del ritmo de GRC. Threat Intelligence tiene necesidades diferentes de Application Security. Identity and Access Management tiene problemas diferentes de Product Security. Cada una de estas funciones tiene objetivos, responsabilidades y horizontes temporales propios.

Este texto no pretende abordar Security como un todo. La reflexión aquí es más específica y nace precisamente de la frontera entre Security y aquello que está más cerca de mi realidad: arquitectura, ingeniería y desarrollo de software. Es en esta interacción donde comencé a percibir un dilema que me parece cada vez más relevante.

Security necesita estar cerca del desarrollo para ser efectiva. Necesita comprender las decisiones de arquitectura, las tecnologías utilizadas y los riesgos asociados a cada contexto. Al mismo tiempo, la forma en que se estructura esta participación puede producir resultados bastante diferentes. Cuando depende principalmente de una secuencia de gates, tickets, aprobaciones, homologaciones y controles manuales, puede surgir una etapa adicional entre la ingeniería y la toma de decisiones, especialmente cuando mecanismos similares se aplican a contextos con diferentes niveles de riesgo.

El desafío, por lo tanto, no es elegir entre seguridad y velocidad. Es construir un modelo en el que Security pueda proteger a la organización sin reducir su capacidad de aprender, experimentar e innovar. Y, cuando hablamos de velocidad, no estamos hablando solamente de entregar software más rápido. Estamos hablando de la capacidad de una organización para aprender rápidamente sobre nuevas tecnologías, evaluar sus riesgos, tomar decisiones y transformar ese aprendizaje en innovación.

## Security y el momento de la decisión

Existe un patrón común en las organizaciones. Producto define qué necesita construirse, arquitectura e ingeniería definen cómo se construirá la solución y, en algún momento, Security es convocada para evaluar si aquello cumple con los requisitos de seguridad.

A primera vista, este modelo parece razonable. Cada área tiene sus responsabilidades y Security funciona como una capa especializada de evaluación. El punto de atención está en el momento en que ocurre esta participación. Cuando Security entra en la discusión después de que gran parte de las decisiones que influyen en el riesgo ya se han tomado, sus posibilidades de contribución naturalmente se vuelven más limitadas.

Cuando se identifica un riesgo en esta etapa, la arquitectura puede ya estar definida, el código puede ya haber sido escrito, las dependencias pueden ya haber sido elegidas y el producto puede ya tener expectativas sobre la entrega. Una decisión de seguridad que podría haberse incorporado naturalmente durante la definición de la solución puede, en ese momento, exigir un cambio más significativo, alterar una elección tecnológica o incluso requerir la revisión de una parte relevante de lo que ya se ha construido.

Es en este punto donde el timing se vuelve importante. Una recomendación de seguridad realizada al inicio de la definición de una solución puede representar apenas una decisión arquitectónica. La misma recomendación realizada cuando la implementación está avanzada puede significar retrabajo, modificación de componentes, revisión de integraciones o impacto sobre un cronograma que ya está comprometido con una fecha de entrega.

Los tickets entran en este proceso como una forma legítima de registrar estas demandas, organizar responsabilidades y hacer seguimiento de su resolución. El problema no está en el ticket en sí, sino en lo que representa cuando una decisión relevante de seguridad se descubre apenas en una etapa avanzada del desarrollo. A partir de ese momento, existe una tensión entre tratar adecuadamente el riesgo y preservar el plazo y el alcance que ya se han establecido para la entrega.

Cuando esto ocurre de forma recurrente, la interacción entre Security e ingeniería puede quedar concentrada en la evaluación de lo que ya se ha producido, en lugar de ocurrir durante las decisiones que dieron origen a la solución. La actuación continúa siendo importante, pero parte del potencial de contribución de Security se pierde porque el espacio para modificar la solución con bajo costo ya se ha reducido.

También existe una consecuencia organizacional relevante. Cuanto más alejada esté Security de las decisiones que originan una solución, mayor puede ser la importancia de mecanismos formales para garantizar que los requisitos de seguridad sean considerados. Políticas, aprobaciones, evidencias, gates y procesos son instrumentos legítimos para ello. Al mismo tiempo, cuando Security participa antes en las decisiones, parte de esta necesidad puede ser atendida de otras formas, como patrones, automatización, componentes reutilizables y conocimiento compartido.

La cuestión no es eliminar mecanismos de control, sino encontrar la forma más adecuada de ejercerlos. En algunos contextos, será necesaria una aprobación formal. En otros, el mismo conocimiento puede estar incorporado a la arquitectura, a la plataforma o al propio proceso de desarrollo. La forma de ejercer este control puede variar según el riesgo, el contexto y, principalmente, el momento en que se toma la decisión.

## El verdadero significado de velocidad

Cuando decimos que Security necesita acompañar la velocidad de la ingeniería, no deberíamos estar hablando únicamente del tiempo de respuesta a tickets o de la velocidad de entrega de software. La cuestión más importante es la velocidad con la que la organización consigue aprender, tomar decisiones y transformar ese aprendizaje en innovación.

Una organización tecnológica necesita experimentar. Necesita probar nuevas arquitecturas, plataformas, servicios, frameworks y herramientas. Necesita descubrir rápidamente qué funciona, cuáles son los riesgos, cuáles son los costos y qué tecnologías pueden generar ventaja competitiva. Este proceso de aprendizaje no ocurre necesariamente en ciclos trimestrales. Muchas veces, una decisión relevante necesita tomarse en horas o días.

Imaginemos que aparece una nueva tecnología y que un squad ve una oportunidad estratégica para utilizarla. Si el proceso necesario para que Security evalúe esta tecnología tarda semanas o meses, el impacto puede ir mucho más allá del time to market. La organización pierde capacidad de experimentar y, principalmente, de aprender. Mientras la tecnología evoluciona, la oportunidad puede desaparecer y la decisión puede dejar de tener sentido.

También existe una consecuencia menos obvia. Cuando los procesos de seguridad no acompañan las necesidades de la ingeniería, puede aumentar la presión por buscar alternativas. Un equipo puede buscar otra herramienta, utilizar un servicio fuera de los estándares corporativos o construir una integración provisional para poder avanzar. Esto no siempre deriva de una intención deliberada de eludir controles. Muchas veces, es simplemente el resultado de una necesidad de negocio o de ingeniería que surgió antes de que existiera una respuesta adecuada en el proceso formal. El efecto puede ser una reducción de la visibilidad sobre aquello que se está utilizando y una menor oportunidad de influir en la forma en que se adopta la tecnología.

Por eso, la velocidad también es una dimensión de seguridad. Una Security eficiente necesita ser suficientemente rápida para participar en el proceso de experimentación mientras la decisión todavía se está construyendo. No basta con evaluar una tecnología después de que el negocio ya haya decidido utilizarla. Es necesario poder comprender sus riesgos, proponer controles proporcionales y establecer condiciones para que la experimentación ocurra de manera segura.

Esta proximidad también beneficia a la propia Security. Las nuevas tecnologías no representan solamente riesgos que deben evaluarse. También exigen aprendizaje. Nuevos modelos arquitectónicos, servicios de cloud, herramientas de desarrollo y tecnologías emergentes pueden introducir riesgos que no encajan perfectamente en los controles existentes. Estar cerca de la ingeniería permite que Security comprenda estos cambios en el mismo momento en que están siendo explorados por la organización.

El objetivo no es simplemente reducir el tiempo de entrega. Es reducir el intervalo entre una hipótesis, una experimentación, el aprendizaje sobre sus riesgos y una decisión consciente sobre su adopción. Cuando una organización consigue acortar este ciclo, no solamente entrega más rápido. Aumenta su capacidad de aprender, adaptarse e innovar sin renunciar a una evaluación consciente de los riesgos.

## Security como parte de la ingeniería

Tal vez el cambio más importante sea dejar de pensar en Security como una etapa del proceso de desarrollo y comenzar a tratarla como una de las disciplinas que participan en este proceso. La seguridad no debería ser algo que se verifica solamente al final de una solución. Debería ser una de las dimensiones consideradas mientras la solución todavía está siendo diseñada y las decisiones aún pueden modificarse con un menor costo.

Security no debería aparecer solamente cuando existe algo que aprobar. Debería participar en la definición de la solución. Un profesional de Security cercano a la ingeniería puede discutir con el arquitecto cuáles son los límites de confianza de la solución, cómo se realizará la autenticación entre servicios, qué datos serán tratados, dónde estarán los puntos de exposición, qué privilegios serán necesarios, cómo se almacenarán los secrets, qué dependencias externas se utilizarán y qué amenazas son realmente relevantes en ese contexto. El valor de esta participación está precisamente en que ocurre mientras estas decisiones se están tomando, y no después de que la arquitectura ya está consolidada.

Esta participación es diferente de colocar a alguien dentro del squad para fiscalizar el trabajo. La proximidad con la ingeniería debería existir para permitir una colaboración más efectiva en la construcción de la solución, y no simplemente para acompañar lo que están haciendo los desarrolladores.

En este sentido, me gusta la idea de tratar al profesional de Security como un socio del arquitecto de soluciones. Producto, arquitectura e ingeniería necesitan decidir cómo se construirá determinada solución. Security contribuye a comprender qué riesgos introduce esta arquitectura, qué amenazas son relevantes y cómo estos riesgos pueden mitigarse sin comprometer innecesariamente el objetivo del sistema.

Esta proximidad también cambia la naturaleza de la conversación. En lugar de discutir únicamente si determinada tecnología puede o no utilizarse, es posible discutir bajo qué condiciones puede utilizarse de forma segura. En lugar de descubrir posteriormente que determinada arquitectura posee una exposición indeseada, es posible identificar esta exposición mientras las alternativas todavía están siendo evaluadas.

Esto no significa transferir a Security la responsabilidad sobre la solución. Producto continúa siendo responsable del producto, ingeniería de la implementación y las decisiones arquitectónicas corresponden a las personas responsables de la solución. Security añade conocimiento especializado sobre riesgos y controles a esta discusión.

Esta distinción es importante porque integrar Security a la ingeniería no significa hacer que Security sea responsable de todo lo relacionado con la seguridad. Significa distribuir mejor el conocimiento necesario para que las decisiones sean tomadas por quienes poseen el contexto, con la participación de quienes poseen la especialización.

La pregunta deja de ser solamente “¿Security aprobó?” y pasa a ser “¿La solución fue construida considerando los riesgos relevantes para su contexto y las medidas necesarias para tratarlos?”. El cambio tiene menos que ver con retirar una etapa de aprobación y más con llevar el conocimiento de seguridad al momento en que las decisiones todavía se están construyendo.

Esta integración trae una exigencia para el propio profesional de Security. No basta con estar presente en las reuniones del squad o conocer el ciclo de desarrollo como un proceso descrito en documentación. Para participar efectivamente en la ingeniería, es necesario comprender el proceso como práctica.

Una forma concreta de desarrollar esta comprensión es construir. Una prueba de concepto puede recorrer todo el camino de una solución, desde la definición del requisito y de la arquitectura hasta el desarrollo, pull request, pipeline, pruebas, controles de seguridad, deploy y observabilidad. El objetivo no es transformar al Security Engineer en desarrollador, sino proporcionar experiencia práctica suficiente para comprender las restricciones, incentivos y trade-offs que forman parte del día a día de la ingeniería.

La experiencia práctica también cambia la forma en que Security evalúa sus propias recomendaciones. Al implementar un control en una solución real, el profesional comienza a percibir las dependencias, el esfuerzo de implementación y los impactos que esa decisión produce en el pipeline y en el ciclo de desarrollo. Esta perspectiva es difícil de obtener únicamente mediante la definición de políticas o la revisión de documentos y ayuda a evaluar si determinado control está produciendo una reducción de riesgo proporcional a la fricción que introduce.

Si una recomendación exige procesos manuales excesivos, genera muchas excepciones o es difícil de implementar, esto puede ser una señal de que el control necesita ser rediseñado, automatizado o incorporado a un patrón arquitectónico o componente de plataforma.

Cuanto más entiende Security cómo se construye efectivamente el software, mejor puede evaluar no solo los riesgos de una solución, sino también la forma más adecuada de tratarlos. De la misma manera, cuanto más comprende la ingeniería las razones detrás de los controles, mayor es la posibilidad de que la seguridad se incorpore a las propias decisiones técnicas, reduciendo la necesidad de intervenciones posteriores.

## Del gate al guardrail

Esto nos lleva a una distinción importante entre gates y guardrails. Un gate condiciona la continuidad del flujo al cumplimiento de una condición o a la toma de una decisión. Un guardrail establece los límites dentro de los cuales el trabajo puede avanzar, pudiendo incorporar verificaciones y bloqueos directamente en el entorno de ingeniería. La diferencia está menos en la existencia o no de bloqueos y más en la forma en que se incorporan al proceso. En el modelo basado en gates, determinadas decisiones deben evaluarse explícitamente antes de que el flujo avance. En el modelo basado en guardrails, parte de estas condiciones puede estar incorporada al propio proceso de desarrollo.

Ambos pueden ser necesarios. Un cambio que involucre datos altamente sensibles, privilegios elevados o una exposición crítica puede justificar una evaluación humana. En otros contextos, especialmente cuando la decisión es recurrente y previsible, los controles automatizados pueden ofrecer una forma más eficiente de tratar el mismo riesgo.

No todas las decisiones tienen el mismo nivel de riesgo y, por eso, no todas necesitan exigir el mismo nivel de intervención. Cuanto más recurrente, previsible y bajo sea el riesgo, mayor puede ser la capacidad de tratarlo mediante patrones, automatización y self service. A medida que aumentan la criticidad, la exposición o la complejidad de la decisión, también crece el valor del análisis especializado de Security.

Esta es la lógica de un enfoque basado en riesgo: el nivel de control debe ser proporcional al riesgo que se pretende tratar. El objetivo no debería ser maximizar la cantidad de controles, sino encontrar una forma eficiente de reducir los riesgos relevantes sin introducir una fricción desproporcionada en el proceso de ingeniería. Un control que exige intervención manual recurrente de decenas de squads puede consumir una cantidad significativa de capacidad especializada, incluso cuando su aplicación esté justificada en determinados contextos.

En este contexto, la automatización deja de ser solamente una iniciativa de eficiencia y pasa a ser una estrategia de escala. Si cincuenta squads necesitan implementar el mismo control, el conocimiento utilizado en estas decisiones puede transformarse en un componente, una política, un pipeline, un template o una capacidad de plataforma que ya incorpore este control de forma segura. En lugar de reproducir el mismo análisis en diferentes contextos, parte de este conocimiento puede estar disponible directamente para la ingeniería.

Esta transformación permite que Security concentre su capacidad humana donde su participación aporta más valor: decisiones nuevas, complejas, de alto impacto o que dependen del contexto. Para aquello que es recurrente y previsible, el conocimiento puede incorporarse a la propia ingeniería.

Security no escala de forma sostenible agregando personas en la misma proporción en que crecen los squads. Escala cuando transforma conocimiento especializado en capacidades reutilizables y permite que los controles se apliquen de forma consistente por muchos equipos. Siempre que sea posible, esto hace que el camino seguro sea también el camino más simple para la ingeniería.

## Tiempo y escala: Security más allá de la cola

Existe una consecuencia operativa importante cuando Security pasa a formar parte del ciclo de ingeniería. Si la ingeniería toma decisiones en horas o días, el tiempo necesario para una evaluación de seguridad debe ser compatible con el horizonte temporal de estas decisiones. Esto no significa convertir toda demanda en atención urgente, sino evitar que el análisis de seguridad opere a un ritmo completamente disociado del proceso de ingeniería.

Esto también cambia la discusión sobre escala. El desafío no es simplemente hacer que Security responda más rápidamente a las solicitudes que recibe, sino reducir la cantidad de decisiones que dependen de una respuesta manual específica. Una tecnología común y de bajo riesgo puede utilizarse mediante patrones previamente definidos. Una arquitectura recurrente puede tener mecanismos de seguridad ya incorporados. Una política simple puede validarse automáticamente. Una vulnerabilidad conocida puede, siempre que sea posible, detectarse y tratarse mediante el pipeline.

Cuanto más previsible sea una decisión, menor tiende a ser la necesidad de una intervención humana específica. Cuando el camino seguro está automatizado, el squad no necesita esperar. Cuando un patrón arquitectónico ya incorpora los controles necesarios, no es necesario reproducir el mismo análisis en cada nueva implementación. Cuando Security participa en la discusión arquitectónica, una decisión puede tratarse mientras la solución todavía está siendo construida, reduciendo la necesidad de enviarla posteriormente a una nueva evaluación.

Es en este punto donde los tickets revelan una cuestión de capacidad. Continúan siendo útiles para registrar demandas, responsabilidades y decisiones, pero no eliminan la dependencia estructural entre muchos squads y una capacidad especializada de Security. Si diferentes equipos necesitan consultar individualmente a Security para tomar decisiones similares, la organización está repitiendo interacciones en torno a un conocimiento que podría reutilizarse.

Una Security que escala necesita transformar conocimiento especializado en capacidades que puedan ser utilizadas por muchos equipos al mismo tiempo. Esto incluye patrones arquitectónicos, automatización, componentes reutilizables, documentación, capacitación, guardrails y plataformas que incorporen controles directamente al proceso de desarrollo.

Las nuevas tecnologías pueden ayudar en este proceso. La inteligencia artificial, por ejemplo, puede ampliar la capacidad de los profesionales de Security en actividades de análisis, triaje, orientación e identificación de riesgos. Puede hacer que el conocimiento especializado sea más accesible y reducir el esfuerzo necesario para determinadas tareas. Pero esto, por sí solo, no cambia el modelo operativo. Si el proceso continúa dependiendo de tickets, aprobaciones e intervenciones individuales, herramientas más sofisticadas pueden simplemente hacer que este flujo sea más eficiente, sin eliminar su dependencia de interacciones específicas.

El beneficio de escala ocurre cuando el conocimiento deja de depender de una interacción individual y pasa a formar parte del propio proceso de ingeniería. Un patrón puede reutilizarse por decenas de squads. Un control puede automatizarse. Una capacidad de plataforma puede eliminar la necesidad de implementación manual. Una orientación puede estar disponible en el momento en que se toma la decisión.

Esto también redefine el papel del equipo central de Security. En lugar de concentrar su capacidad en la revisión individual de todo lo que ocurre en la organización, puede dirigir su actuación humana hacia decisiones nuevas, complejas o de mayor impacto, mientras invierte en la construcción de capacidades que permitan a los demás equipos tomar decisiones recurrentes con mayor autonomía.

Escalar Security no significa simplemente atender más solicitudes o responder más tickets. Significa hacer que el conocimiento especializado pueda influir en un número mucho mayor de decisiones de ingeniería sin exigir una interacción humana proporcional al número de estas decisiones.

## Seguridad como parte de la cultura

Al final, existe una dimensión que ningún proceso, herramienta o estructura organizacional resuelve por sí solo: la cultura. No en el sentido de campañas, capacitaciones obligatorias o declaraciones sobre “security first”, sino en la forma en que la organización toma decisiones cuando seguridad, velocidad e innovación entran en tensión.

Una organización madura no debería depender de Security para recordar continuamente a la ingeniería que la seguridad importa. Del mismo modo, Security no debería depender de procesos para recordar continuamente a la ingeniería que determinados controles deben cumplirse. El conocimiento sobre riesgo necesita estar presente allí donde se toman las decisiones.

Esto exige aprendizaje de ambos lados. Security necesita conocer la ingeniería no solo para entender cómo se construye el software, sino para comprender cómo la organización aprende, experimenta y transforma tecnología en producto. Ingeniería necesita conocer seguridad no solo para cumplir controles, sino para incorporar el riesgo a sus propias decisiones técnicas.

Es en este punto donde el dilema cambia de naturaleza. La pregunta deja de ser cuánto control necesita ejercer la organización sobre la ingeniería y pasa a ser cuánto conocimiento de seguridad puede distribuir sin convertir cada decisión en una dependencia de Security.

El objetivo no es hacer que Security corra detrás de la ingeniería, ni hacer que la ingeniería espere a Security. Es reducir las situaciones en las que una necesita esperar a la otra. Para ello, Security necesita estar lo suficientemente cerca como para participar en las decisiones y transformar el conocimiento especializado en contexto, patrones y capacidades que puedan ser utilizados por la ingeniería.

Tal vez el verdadero equilibrio entre control y velocidad esté precisamente ahí: no en eliminar controles, ni en acelerar indefinidamente los procesos de aprobación, sino en colocar cada mecanismo en el lugar en el que produce más valor.

Como arquitecto de soluciones, es desde esta perspectiva que veo este dilema. No desde la responsabilidad de definir cómo debe operar Security, sino desde la experiencia de estar en el punto en el que las decisiones de producto, arquitectura, ingeniería y seguridad necesitan converger. Es en este punto donde resulta evidente que seguridad y velocidad no necesitan disputar el mismo espacio. El desafío está en crear mecanismos que permitan que ambas avancen juntas.

Una organización capaz de innovar necesita aprender rápidamente sobre tecnología, pero también sobre los riesgos que esta tecnología introduce. No para eliminar el riesgo, sino para distinguir aquello que necesita mitigarse, aquello que puede aceptarse y aquello que no puede asumirse.

Security, en este contexto, deja de ser solamente una función que protege aquello que la organización ha construido. Pasa a contribuir para que pueda decidir, con conciencia sobre el riesgo, aquello que todavía puede construir.
