# El PMBOK no es una receta: el papel del tailoring en la gestión de proyectos

_Así como la arquitectura de software es una respuesta a requisitos y restricciones, la gestión también necesita diseñarse para el contexto._

**Resumen:** Defiendo que el PMBOK no debe tratarse como una receta, sino como un repertorio de prácticas que necesita adaptarse al contexto de cada proyecto. Así como en la arquitectura de software, primero debemos entender requisitos, restricciones, riesgos y trade-offs para luego definir la solución de gestión adecuada. Tailoring no significa simplemente hacer menos, sino dimensionar conscientemente la gobernanza necesaria, evitando tanto la burocracia como los controles insuficientes. La madurez, por lo tanto, está menos en seguir procesos y más en saber justificar las decisiones y evolucionarlas conforme cambia el problema.

---

Recientemente, en una conversación con una amiga que trabaja como Product Manager, surgió casi por casualidad un comentario que me llamó la atención. Contó que la empresa donde trabaja no utiliza el PMBOK porque considera que el enfoque es demasiado rígido para la realidad de la organización.

La percepción no me parece extraña. En tecnología, veo algo parecido con frecuencia en discusiones sobre arquitectura de soluciones. Una determinada arquitectura se presenta como buena práctica, pasa a reproducirse en otros contextos y, cuando no encaja, la conclusión es que la propia arquitectura era inadecuada. Muchas veces, el problema está en elegir la solución antes de comprender el problema que necesita resolver. En system design, sabemos que no tiene sentido comenzar por la arquitectura. Primero entendemos el problema, sus requisitos, restricciones y trade-offs. Solo entonces decidimos cómo se construirá el sistema.

Cuando escuché aquel comentario sobre el PMBOK, hice la misma asociación. Tal vez parte de la resistencia al framework provenga de tratarlo como una arquitectura de gestión lista, algo que debería aplicarse de manera uniforme para que una organización pueda decir que “hace gestión de proyectos”. Si ese es el punto de partida, es fácil transformar conocimiento en procedimiento, procedimiento en obligación y obligación en burocracia.

El problema está precisamente en esa interpretación. El PMBOK no necesita entenderse como una metodología lista, así como un conjunto de patrones arquitectónicos no constituye, por sí solo, la arquitectura de una aplicación. Ofrece conocimiento, prácticas y conceptos que pueden utilizarse para construir enfoques de gestión adecuados a diferentes situaciones. La cuestión deja de ser cuánto del PMBOK utiliza una organización y pasa a ser por qué se eligieron determinadas prácticas, qué problema resuelven y qué nivel de formalidad es necesario.

Tal vez sea útil pensar en esto como una especie de management design. No como una disciplina formal o un nuevo framework, sino como una lente para observar la gestión con la misma lógica que utilizamos al diseñar sistemas: entender el problema antes de elegir los componentes, explicitar restricciones, evaluar trade-offs y evitar tanto la complejidad innecesaria como las soluciones insuficientes.

## El problema comienza antes de la metodología

Cuando hablamos de gestión de proyectos, con frecuencia ponemos al mismo nivel cosas que cumplen roles diferentes: el cuerpo de conocimiento sobre gestión, el enfoque elegido para conducir un proyecto y la metodología utilizada por la organización para operacionalizar ese enfoque. Confundir estas capas facilita la idea de que, para aplicar determinado conocimiento, es necesario reproducir íntegramente un proceso. Pero una organización puede utilizar prácticas de gestión sin adoptar una metodología formal, así como puede tener una metodología corporativa y aun así adaptar su aplicación a cada proyecto.

Esta diferencia se hace evidente cuando observamos la escala y la naturaleza del trabajo. Un equipo pequeño puede administrar riesgos, prioridades, dependencias y decisiones mediante mecanismos informales porque la proximidad entre las personas hace que la coordinación sea barata. A medida que la organización crece, aumentan las interfaces, los involucrados, el costo de los desalineamientos y las consecuencias de determinadas decisiones. Surgen, entonces, necesidades de gobernanza, comunicación y trazabilidad que antes simplemente no existían. No es que la organización se haya vuelto más “adherente” a una metodología; el sistema que necesita coordinar se volvió más complejo.

La misma lógica se aplica a la forma de ejecución. Un proyecto con requisitos relativamente estables y alto costo de cambio puede justificar un enfoque más predictivo. Un producto en un entorno de alta incertidumbre puede beneficiarse de ciclos cortos de aprendizaje y adaptación. Entre estos extremos existe una variedad de combinaciones posibles, incluso dentro de una misma iniciativa, cuando diferentes partes del trabajo tienen distintos niveles de previsibilidad.

Por eso, la pregunta sobre qué metodología utilizar no debería ser el punto de partida. Antes de ella viene una cuestión más fundamental: ¿qué necesitamos gestionar, cuáles son los riesgos involucrados, qué restricciones existen y cuánta coordinación y gobernanza exige realmente este contexto? A partir de esas respuestas puede diseñarse un enfoque de gestión.

## Management design

En system design, no comenzamos diciendo que toda aplicación necesita microservicios o mensajería. Comenzamos entendiendo requisitos y restricciones. Volumen, disponibilidad, latencia, seguridad, costo, capacidad operativa y criticidad ayudan a determinar qué decisiones arquitectónicas están justificadas. No existe una arquitectura correcta en abstracto. Existe una arquitectura adecuada para un determinado conjunto de requisitos y restricciones, considerando los trade-offs involucrados.

La misma lógica puede aplicarse a la gestión. Un proyecto crítico puede requerir mecanismos de gobernanza que serían desproporcionados en una iniciativa pequeña. Un proyecto con muchas dependencias puede necesitar mecanismos de coordinación que no tienen sentido para un equipo que trabaja de forma independiente. Una iniciativa altamente incierta puede obtener poco valor de una planificación excesivamente detallada cuando todavía no existen suficientes informaciones para sostenerla. Lo que cambia de un contexto a otro no es la importancia de la gestión, sino los problemas que necesita resolver y la complejidad necesaria para resolverlos.

Las prácticas de gestión pueden, por lo tanto, tratarse como componentes de una solución. El PMBOK ofrece parte de ese repertorio, pero no determina por sí solo cómo deben combinarse esos componentes. La composición final depende del contexto, de las necesidades y de las restricciones del proyecto. Es en este sentido que propongo pensar en management design: la construcción deliberada de un enfoque de gestión a partir del problema que necesita administrarse.

La idea es similar al montaje de un sistema. Tener más componentes disponibles no hace que la solución sea automáticamente mejor. Cada componente añade capacidades, pero también puede introducir costo, complejidad, dependencias o nuevas necesidades operativas. El trabajo de diseño está precisamente en decidir qué debe formar parte de la solución, qué puede simplificarse y qué trade-offs son aceptables.

Tailoring, en este sentido, deja de ser simplemente el acto de “adaptar el PMBOK”. Pasa a ser una consecuencia natural del propio proceso de diseño: entender el contexto, seleccionar los componentes adecuados y componer un enfoque proporcional al problema que necesita resolverse.

## Tailoring no es hacer menos

Es fácil interpretar tailoring como una licencia para reducir procesos. Si una organización tiene muchos documentos, elimina algunos; si tiene muchas reuniones, cancela algunas; si determinada etapa parece burocrática, deja de ejecutarla. El resultado puede incluso ser un enfoque mejor, pero reducir procesos por sí solo no caracteriza el tailoring. La diferencia está en el criterio utilizado para tomar esa decisión.

En arquitectura, una solución no es mejor simplemente porque tiene menos componentes. Una aplicación con pocos componentes puede ser elegante o insuficiente; una arquitectura más compleja puede ser necesaria o puede representar overengineering. El número de componentes importa menos que la relación entre ellos y los requisitos que necesitan atender. La misma lógica vale para la gestión: la cantidad de prácticas utilizadas no determina la calidad del enfoque.

Aplicar menos prácticas puede, sí, ser más maduro que aplicarlas todas indiscriminadamente, siempre que la elección sea deliberada. Si determinado control fue eliminado, es necesario comprender qué problema resolvía, qué riesgo está asociado con su ausencia y por qué ese nivel de control no es necesario en ese contexto. Del mismo modo, añadir una práctica debería exigir una justificación equivalente: ¿qué necesidad atiende y qué complejidad introduce?

Tailoring no consiste en elegir el camino más simple. Consiste en dimensionar la gestión de acuerdo con el problema, aceptando conscientemente los trade-offs involucrados.

## El riesgo del overengineering de gestión

En tecnología, el overengineering es un problema conocido. Una solución puede estar técnicamente correcta y aun así ser inadecuada porque introduce una complejidad que los requisitos no justifican. Más componentes pueden significar más capacidad, pero también más dependencias, más esfuerzo operativo y más puntos de falla. La complejidad necesita existir por una razón.

En la gestión, el equivalente ocurre cuando una iniciativa recibe documentos, aprobaciones, reuniones e indicadores porque esos mecanismos forman parte de la metodología corporativa, y no porque el proyecto realmente los necesite. Cada elemento puede parecer razonable de manera aislada. El problema aparece cuando observamos el enfoque como un sistema y percibimos que su complejidad introduce más fricción que control, consumiendo capacidad que podría estar utilizándose en la ejecución del propio proyecto.

Esto no significa que la documentación, la gobernanza o los controles sean malos. Significa que necesitan tener una función clara. Una reunión debe existir porque alguna coordinación necesita ocurrir. Un registro debe existir porque determinada información necesita preservarse, compartirse o utilizarse en una decisión. Una aprobación debe existir porque determinada decisión requiere esa autoridad. Un indicador debe existir porque existe una pregunta relevante que necesita ser respondida.

Cuando esa relación se pierde, el mecanismo deja de ser una herramienta de gestión y pasa a ser simplemente un ritual. Es posible tener una organización extremadamente disciplinada en la ejecución de procesos y, aun así, poco madura en la gestión de proyectos. Cumplir un proceso demuestra adherencia al proceso; no demuestra, por sí mismo, que el proceso haya sido bien elegido.

## El riesgo de una gestión subdimensionada también existe

La crítica a la burocracia puede llevar al extremo opuesto. Si demasiada complejidad es mala, puede parecer que la mejor gestión es aquella que tiene el mínimo posible de procesos. Esta conclusión es tan equivocada como asociar madurez con la cantidad de controles. En arquitectura, una solución minimalista puede ser exactamente lo que el problema exige o simplemente estar subdimensionada. La diferencia está en los requisitos y en las consecuencias de las decisiones.

En la gestión, el equivalente es eliminar controles porque son inconvenientes, lentos o incompatibles con la cultura del equipo, sin evaluar el riesgo que permanece después de esa decisión. Una empresa puede decir que no necesita documentar decisiones porque “somos Agile”, evitar determinado mecanismo de gobernanza porque “somos pequeños” o no hacer seguimiento formal de riesgos porque “el equipo habla todos los días”. En determinados contextos, esas decisiones son perfectamente razonables. En otros, simplemente trasladan el costo a un problema futuro que nadie decidió explícitamente aceptar.

Este punto es importante porque la ausencia de un control también es una decisión de gestión. Si un mecanismo fue deliberadamente retirado, debería ser posible explicar qué necesidad atendía, por qué no es relevante en ese contexto y qué riesgo se está asumiendo al no mantenerlo. Tailoring no significa eliminar aquello que parece burocrático; significa decidir conscientemente el nivel de control necesario.

El objetivo, por lo tanto, no es minimizar procesos. Es dimensionar la gestión de acuerdo con la complejidad, los riesgos y las restricciones del contexto.

## Una startup no es una corporación en escala reducida

Es en este punto donde las startups en etapa inicial se vuelven un caso particularmente interesante. Una organización pequeña, con pocas personas, alta incertidumbre y un producto todavía en evolución, opera bajo condiciones muy diferentes de las de una empresa establecida. La comunicación es directa, las decisiones pueden tomarse con poca intermediación y mucha información permanece disponible en el contexto de las propias personas. Reproducir en este entorno una estructura corporativa completa de gestión puede significar introducir una complejidad que la organización todavía no necesita.

Esto no significa ausencia de gestión. La startup sigue necesitando definir objetivos, evaluar riesgos, administrar dependencias, tomar decisiones y hacer seguimiento de resultados. Lo que cambia es la forma en que estas actividades necesitan estructurarse. Cuando pocas personas necesitan alinear una decisión, una conversación puede ser suficiente. A medida que aumentan las personas involucradas, las interfaces entre equipos y el costo de una decisión mal coordinada, mecanismos que antes parecían innecesarios pueden pasar a tener valor.

La práctica de gestión puede, por lo tanto, permanecer mientras su forma evoluciona. Una startup no necesita importar la estructura de gobernanza de una gran corporación para ser profesional, así como no necesita transformar cada decisión en un proceso formal para demostrar madurez. Pero tampoco debería confundir informalidad con ausencia de gestión. Lo que hoy puede resolverse mediante proximidad y contexto compartido puede mañana requerir mecanismos explícitos de coordinación, no porque la organización finalmente haya “adoptado una metodología”, sino porque el problema que necesita administrar cambió.

Este es uno de los ejemplos más claros de management design. El enfoque adecuado no es una versión reducida de una metodología corporativa, sino una solución construida a partir de las características de la propia organización. A medida que crece, esta solución puede evolucionar junto con el sistema que necesita coordinar.

## La gestión también es una arquitectura evolutiva

Lo que funciona para una organización pequeña puede dejar de funcionar a medida que crece, de la misma manera que una arquitectura adecuada para una aplicación en determinada etapa puede necesitar ser revisada cuando sus requisitos cambian. Esto no significa que la solución anterior estuviera equivocada. Significa que fue diseñada para condiciones que ya no son las mismas.

El crecimiento altera la naturaleza del problema. Más personas aumentan las interfaces y el costo de comunicación. Más equipos crean dependencias que antes no existían. Más clientes aumentan las consecuencias de determinadas fallas. Más recursos involucrados elevan el costo de decisiones equivocadas. Nuevas obligaciones regulatorias introducen restricciones adicionales. En algún momento, mecanismos que antes serían burocráticos pasan a ser necesarios para mantener la coordinación y el control.

En arquitectura de software, este proceso es conocido: una solución evoluciona porque el sistema que la rodea evolucionó. La arquitectura de gestión sigue la misma lógica. Una organización no debería preservar una determinada estructura de gobernanza solo porque funcionó en el pasado, así como tampoco debería introducir nuevos mecanismos solo porque alcanzó determinado tamaño. El detonante del cambio debería estar en las nuevas necesidades, restricciones y riesgos que surgieron.

La madurez, en este contexto, no consiste en llegar a un estado en el que todos los proyectos utilicen la misma cantidad de procesos. Consiste en desarrollar la capacidad de reconocer cuándo la arquitectura de gestión dejó de ser adecuada y evolucionarla antes de que la complejidad del sistema haga que ese cambio sea necesario de manera traumática.

## Agile cambia la forma, pero no elimina el problema

Esta perspectiva también cambia la manera de observar Agile. La oposición entre PMBOK y Agile suele partir de la idea de que uno representa procesos estructurados mientras el otro representa adaptación. Esta dicotomía pierde de vista el punto principal: ambos pueden ofrecer mecanismos para abordar problemas de gestión, pero parten de condiciones diferentes respecto de la previsibilidad, la incertidumbre y el cambio.

Un enfoque adaptativo tiene sentido cuando existe una incertidumbre relevante sobre qué debe construirse o sobre qué solución producirá valor. Trabajar de forma iterativa permite aprender y ajustar el camino a medida que surgen nuevas informaciones. Pero la iteratividad no elimina riesgos, dependencias, stakeholders, restricciones presupuestarias, requisitos de seguridad o necesidades de gobernanza. Simplemente cambia la forma en que estos elementos son tratados.

Un equipo puede trabajar con ciclos cortos, priorización continua y feedback frecuente y, al mismo tiempo, necesitar lidiar con compliance, proveedores, presupuesto o dependencias entre equipos. Del mismo modo, una iniciativa puede utilizar planificación predictiva en determinadas dimensiones y mecanismos adaptativos en otras. La elección no necesita ser ideológica. Necesita responder a las características del trabajo.

Por eso, los enfoques híbridos no deberían verse como una contradicción, sino como una posible consecuencia del propio tailoring. Diferentes partes de una iniciativa pueden presentar distintos niveles de previsibilidad, riesgo y necesidad de control. La pregunta relevante no es qué metodología ganó el debate, sino qué mecanismos de gestión son necesarios para abordar adecuadamente el contexto.

Agile no elimina la necesidad de gestión. Así como un enfoque predictivo no implica, por sí mismo, burocracia. Lo que cambia es la arquitectura utilizada para organizar y conducir el trabajo.

## La automatización cambia los trade-offs de la gestión

La discusión sobre management design adquiere otra dimensión cuando consideramos IA y automatización. Elegir qué prácticas aplicar también implica considerar el costo de operacionalizarlas. Actualizar registros, consolidar información, producir informes, hacer seguimiento de indicadores e identificar cambios requiere esfuerzo, y ese esfuerzo influye en la decisión sobre el nivel de gestión adecuado. Una práctica puede ser relevante y, aun así, ser desproporcionada para el contexto cuando su costo de ejecución es alto.

La automatización altera este trade-off. Una actividad que antes requería horas de trabajo manual puede pasar a requerir apenas una revisión humana. Información dispersa puede consolidarse automáticamente, los informes pueden producirse a partir de datos ya disponibles y los sistemas pueden ayudar a identificar patrones, inconsistencias y posibles riesgos. Esto no significa simplemente añadir más procesos porque ahora son baratos. Significa que prácticas antes consideradas excesivamente costosas pueden empezar a tener sentido cuando disminuye el costo de operacionalizarlas.

El valor de una práctica no cambia necesariamente porque se haya vuelto más barata de ejecutar. Lo que cambia es la relación entre su beneficio, su costo y la complejidad que introduce. Una solución que antes sería desproporcionada puede volverse adecuada al contexto, alterando las decisiones posibles dentro del management design.

Existe, sin embargo, una frontera importante. Automatizar la recopilación y el análisis de información no significa automatizar el juicio. Una herramienta puede identificar un posible riesgo o desviación, pero evaluar su relevancia, decidir si debe aceptarse y determinar una respuesta sigue requiriendo contexto y responsabilidad. La IA puede reducir el costo de la gestión, pero no elimina la necesidad de diseñarla.

## Diseñar la gestión, no seguir la receta

El problema comienza con la propia pregunta “¿qué metodología debemos utilizar?”. En arquitectura de soluciones, primero entendemos el sistema, sus requisitos, restricciones, riesgos y trade-offs; solo entonces definimos la arquitectura. Management design sigue la misma lógica: comprender el contexto, dimensionar la gobernanza necesaria y seleccionar las prácticas que responden a los problemas reales del proyecto. Cuando los requisitos cambian, el enfoque también puede necesitar evolucionar.

Es en este proceso donde el PMBOK encuentra su lugar. No como una receta que deba aplicarse íntegramente, sino como un repertorio para orientar decisiones. La madurez no está en la cantidad de prácticas adoptadas, sino en la capacidad de justificar las decisiones: qué riesgos están siendo tratados, qué mecanismos son necesarios, qué complejidad es aceptable y qué controles deliberadamente no forman parte de la solución. Aplicar menos prácticas puede ser más maduro que aplicarlas todas, siempre que esa elección sea consciente y proporcional al contexto.

En arquitectura, no consideramos maduro al arquitecto que utiliza todos los componentes disponibles, sino a aquel que sabe componer una solución adecuada a los requisitos y restricciones, asumiendo conscientemente los trade-offs. La gestión de proyectos no debería ser diferente. El PMBOK proporciona parte del repertorio; el trabajo está en saber transformarlo en un enfoque adecuado al problema que se pretende resolver.
