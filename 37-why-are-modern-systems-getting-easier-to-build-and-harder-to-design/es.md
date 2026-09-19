# ¿Por qué los sistemas modernos son cada vez más fáciles de construir y más difíciles de diseñar?

_Las abstracciones de cloud, la paradoja de la elección y la inteligencia artificial están cambiando la naturaleza de la arquitectura de soluciones más rápido de lo que conseguimos adaptarnos._

**Resumen:** Exploro los motivos por los cuales los sistemas modernos son más fáciles de construir, pero más difíciles de diseñar: cloud, servicios gestionados, SaaS e IA redujeron el costo de implementar soluciones, pero ampliaron el espacio de elecciones y convirtieron el juicio arquitectónico en el principal cuello de botella. En este escenario, la experiencia significa saber eliminar alternativas, evaluar trade-offs, reconocer dependencias ocultas y preservar la reversibilidad de las decisiones. Por eso, propongo que la arquitectura de soluciones necesita un cuerpo de conocimiento más sistemático, algo cercano a un “PMBOK de Solution Architecture”, para organizar el proceso de decisión sin sustituir el juicio del arquitecto.

---

Tengo cierto vicio de ver videos de System Design. Me gustan particularmente aquellos en los que alguien explica cómo una gran empresa resolvió un problema a escala: cómo una plataforma procesa millones de eventos, cómo una aplicación maneja picos de tráfico, cómo una empresa estructuró su arquitectura de datos o cómo determinado servicio fue dividido en decenas de componentes. Es interesante observar una arquitectura después de que las principales decisiones ya fueron tomadas. Cada componente parece tener un propósito claro y, mirando hacia atrás, muchas elecciones parecen casi obvias.

La situación es diferente cuando necesitamos diseñar una arquitectura desde cero. Ya diseñé decenas de arquitecturas a lo largo de mi carrera. Ya tuve que tomar decisiones sobre integración, datos, escalabilidad, disponibilidad, seguridad, cloud y operación en contextos bastante diferentes. Sé que existen varias maneras razonables de resolver la mayoría de los problemas que encuentro. Y, aun así, con frecuencia me siento sobrecargado cuando comienzo un diseño desde cero. No por falta de experiencia, sino por el exceso de opciones.

El punto de partida debería ser simple: ¿cuáles son los requisitos que la solución necesita cumplir? ¿Qué disponibilidad se necesita? ¿Qué volumen de datos esperamos? ¿Qué latencia es aceptable? ¿Cuáles son las restricciones de costo, seguridad, operación y compliance? ¿Qué tan importante es la capacidad de evolucionar o migrar la solución en el futuro? En teoría, estas respuestas deberían reducir el espacio de decisión. En la práctica, incluso después de establecer las restricciones, todavía podemos llegar a decenas de soluciones técnicamente viables.

Y es ahí donde suelo volver a lo básico. Elijo los servicios de AWS que ya conozco bien, recurro a patrones que ya funcionaron en otros proyectos y evito, cuando no existe una razón fuerte para ello, introducir una tecnología o una arquitectura completamente nueva. Puede haber conservadurismo en esta elección. También puede haber cierta falta de experimentación. Pero existe algo más pragmático: conozco mejor los riesgos de aquello que ya utilicé.

Experimentar con una solución nueva en otra cloud, introducir múltiples clouds o adoptar una tecnología que todavía no conozco profundamente puede producir una arquitectura técnicamente interesante. Pero también puede resultar en una solución que no atienda tan bien los requisitos, que el equipo tenga dificultades para operar o que se transforme en deuda técnica cuando la realidad del proyecto demuestre ser diferente de aquello que imaginábamos. La responsabilidad por la decisión no desaparece porque la tecnología sea nueva.

El problema es que las consecuencias no siempre aparecen inmediatamente. La insatisfacción con una elección, la deuda técnica e incluso el arrepentimiento de haber adoptado determinada tecnología pueden surgir meses después de la implementación, cuando el sistema ya acumuló datos, integraciones y dependencias a su alrededor. Una decisión que parecía reversible puede entonces retrasar un proyecto o hacer que su sustitución sea tan costosa que deje de ser una alternativa viable.

Ya escribí sobre parte de este dilema en [“Cloud Computing: escolhendo além do default”](https://cpzjunior.substack.com/p/cloud-computing-escolhendo-alem-do), discutiendo por qué no deberíamos aceptar automáticamente las elecciones predeterminadas ofrecidas por la cloud. El problema que me interesa aquí es un paso más allá: incluso cuando sabemos que existen alternativas al default, ¿cómo decidimos cuáles de ellas realmente merecen ser consideradas?

Cuantas más tecnologías conocemos, mayor se vuelve el espacio de soluciones que conseguimos visualizar. Y cuanto mayor es ese espacio, más difícil resulta evaluar cada alternativa con la profundidad necesaria para tomar una decisión realmente consciente.

Esto ocurre justamente mientras construir sistemas nunca fue tan fácil. La cloud transformó buena parte de la infraestructura en servicios consumibles. SaaS transformó capacidades enteras en APIs. Las plataformas gestionadas eliminaron una enorme cantidad de trabajo operativo. Y la inteligencia artificial también está reduciendo el costo de implementar y experimentar con software.

El resultado es una paradoja: estamos siendo cada vez mejores construyendo soluciones, pero eso no significa que estemos siendo igualmente mejores decidiendo qué soluciones construir.

No estoy argumentando que los sistemas modernos sean peores, ni que debamos volver a administrar servidores, configurar infraestructura manualmente o evitar nuevas tecnologías. Sería justamente lo contrario de lo que estos avances representan. El punto es que, al hacer determinadas partes del problema más fáciles, estas tecnologías también cambiaron la naturaleza de las decisiones que permanecen.

Cuando el costo de implementar alternativas cae drásticamente, el problema deja de ser solamente cómo construir y pasa a ser, cada vez más, cómo elegir.

## La complejidad no desapareció. Cambió de lugar.

Una de las grandes virtudes de la abstracción es precisamente permitirnos dejar de preocuparnos por determinados detalles. No necesitamos conocer la implementación interna de un servicio para utilizarlo. Este es uno de los principios fundamentales detrás de buena parte de la ingeniería de software moderna.

La cloud llevó este principio a una escala enorme. Durante mucho tiempo, construir un sistema significaba lidiar directamente con una cantidad considerable de infraestructura. Servidores, storage, redes, balanceadores, capacidad, replicación y recuperación ante desastres formaban parte del problema porque no había manera de simplemente delegarlos.

Hoy, gran parte de eso puede consumirse como servicio. Una base de datos puede aprovisionarse en minutos. Una cola puede crearse mediante configuración. La capacidad puede ajustarse automáticamente. Una función puede ejecutarse sin que necesitemos administrar el servidor donde se ejecuta.

Esto redujo enormemente el costo de implementación. Pero reducir la complejidad de una capa no significa necesariamente reducir la complejidad del sistema como un todo.

La complejidad simplemente puede cambiar de lugar. En lugar de necesitar saber cómo construir cada componente, necesitamos decidir cómo combinarlos. Un servicio individual puede ser sencillo de consumir, mientras que el sistema formado por la composición de decenas de ellos puede presentar comportamientos difíciles de predecir.

Este cambio también altera el tipo de conocimiento exigido al arquitecto. Ya no basta con saber cómo implementar determinado mecanismo, ni es necesario conocer todos los detalles de su implementación. Es preciso entender las propiedades relevantes para la decisión: sus garantías, sus límites, sus modelos de fallo, sus costos y, principalmente, cómo esas propiedades interactúan con las de los demás componentes.

## La paradoja de la elección

Existe una idea conocida como paradoja de la elección: aumentar el número de alternativas disponibles no necesariamente produce mejores decisiones. El llamado “dilema del supermercado” lo ilustra bien. Ante un estante con decenas de opciones aparentemente similares, elegir puede volverse más difícil, no más fácil. Después de cierto punto, comparar alternativas exige tanto esfuerzo que terminamos prefiriendo aquello que ya conocemos, simplemente porque el costo de decidir es menor.

La arquitectura de soluciones parece haber encontrado una versión propia de este problema. Durante mucho tiempo, muchas decisiones arquitectónicas estaban limitadas por lo que era posible construir con los recursos disponibles. Hoy, para una proporción creciente de los problemas, la situación es casi inversa. Tenemos decenas de servicios capaces de resolver una misma necesidad e innumerables formas de combinarlos. El problema dejó de ser encontrar una tecnología capaz de hacer algo y pasó a ser decidir cuál de las tecnologías capaces de hacerlo debería utilizarse.

Y la dificultad no crece solamente con el número de alternativas. Cada alternativa posee propiedades diferentes y crea nuevas posibilidades de composición. Elegir una base de datos no es una decisión aislada. La elección afecta el modelo de datos, los mecanismos de integración, las estrategias de backup, la observabilidad, los costos operativos e incluso las tecnologías que pasan a tener sentido en las capas siguientes. El espacio de decisión puede crecer rápidamente a medida que estas elecciones se combinan.

Es aquí donde la experiencia del arquitecto se vuelve particularmente importante. Un arquitecto experimentado no evalúa todas las posibilidades. Utiliza conocimiento acumulado, restricciones del problema y heurísticas para eliminar rápidamente aquello que no necesita ser considerado. Una parte importante de la experiencia arquitectónica consiste precisamente en saber qué opciones pueden descartarse sin una investigación más profunda.

Mi “arroz con frijoles” de AWS es, en gran medida, una consecuencia de eso. Son tecnologías que conozco, cuyas propiedades y limitaciones ya encontré en proyectos anteriores y sobre las cuales puedo estimar mejor los riesgos. Cuando elijo una solución conocida, no necesariamente estoy buscando la tecnología más sofisticada. Estoy reduciendo deliberadamente el espacio de decisión para poder dedicar atención a las decisiones que realmente importan.

El riesgo aparece cuando esta heurística deja de ser una elección consciente y pasa a ser simplemente un reflejo. Si siempre elijo aquello que conozco porque existen demasiadas opciones para evaluar, puedo estar cambiando sobrecarga cognitiva por deuda arquitectónica.

La abundancia de alternativas, por lo tanto, no solamente hace que el problema sea más amplio. Aumenta la importancia de saber qué alternativas no necesitan ser consideradas. El desafío arquitectónico pasa a ser menos conocer todas las posibilidades y más construir criterios suficientemente buenos para eliminarlas.

## Cuando la abstracción oculta limitaciones y dependencias

Existe además otro efecto de la abstracción que merece atención. Cuando consumimos servicios gestionados, pasamos a ver solamente una parte de la arquitectura de la que dependemos. Nuestro diagrama representa aquello que decidimos modelar, no necesariamente todo aquello que sustenta el sistema.

Esto no es necesariamente un problema. No necesitamos conocer todos los detalles de una plataforma para utilizarla correctamente. El problema aparece cuando confundimos la simplicidad de la interfaz con independencia entre los componentes.

Cuando colocamos un S3, una Lambda o un DynamoDB en un diagrama, ¿qué estamos representando exactamente? Un storage de objetos, una función ejecutable, una base de datos. Pero ¿qué existe debajo de estas abstracciones? ¿Cómo se distribuyen y replican los datos? ¿Cómo se aprovisionan y comparten los recursos? ¿Cuáles son los límites de estas abstracciones? ¿Qué dependencias existen entre ellas y la infraestructura que las sustenta? Y, principalmente, ¿cuáles de estas propiedades pueden volverse relevantes cuando algo falla?

No necesitamos conocer todos estos mecanismos para utilizar los servicios. Pero eso no significa que dejen de existir o que sus propiedades sean irrelevantes para determinadas decisiones arquitectónicas.

Un sistema puede parecer distribuido entre diferentes servicios, regiones o incluso diferentes clouds y aun así depender de componentes comunes que no aparecen en nuestro diagrama. La diversidad que vemos en la superficie no garantiza independencia en todas las capas.

El caso de Cloudflare en 2022 es un ejemplo de este tipo de dependencia invisible, aunque ya exploré aquel incidente en otro artículo. Para esta discusión, basta con la idea: las abstracciones pueden ocultar no solamente detalles de implementación, sino también dependencias y puntos comunes de fallo relevantes para la resiliencia de una arquitectura.

Lo mismo aplica a los propios proveedores de cloud. Diferentes plataformas pueden ofrecer una enorme variedad de servicios, pero depender de los mismos proveedores o de componentes compartidos en partes de su cadena tecnológica. La abstracción nos permite tratar estos servicios como bloques independientes porque así es como necesitamos consumirlos. Eso no significa que sean completamente independientes en la realidad.

Este es uno de los límites importantes de la abstracción arquitectónica. Podemos deliberadamente ignorar detalles que no son relevantes para una determinada decisión, pero necesitamos reconocer cuándo dejan de ser irrelevantes. Una dependencia que puede ser perfectamente aceptable para una aplicación común puede volverse crítica cuando estamos diseñando alta disponibilidad, disaster recovery o una estrategia de multi-cloud.

El arquitecto no necesita conocer todo lo que existe debajo de una abstracción. Necesita saber lo suficiente para reconocer cuándo sus limitaciones o dependencias pueden cambiar la decisión que está tomando.

## La IA agrava el problema

La inteligencia artificial añade otra dimensión a esta transformación porque reduce aún más el costo de implementación. La discusión sobre IA en la ingeniería de software suele concentrarse en productividad: cuánto código conseguimos producir, cuántas pruebas conseguimos generar o cuánto tiempo conseguimos ahorrar. Estos efectos son relevantes, pero existe una consecuencia arquitectónica menos discutida.

Si resulta más barato implementar una alternativa, también resulta más barato experimentar con alternativas. Esto es positivo. La experimentación es una de las mejores formas de reducir incertidumbre. El problema es que la reducción del costo de experimentación también aumenta la cantidad de soluciones que podemos poner en práctica incluso antes de tener claridad sobre cuál de ellas deberíamos elegir.

La IA es una evidencia particularmente clara de este fenómeno. Existe una cantidad creciente de modelos disponibles, ofrecidos por diferentes proveedores, con diferencias de capacidad, costo, latencia, contexto y comportamiento. Surgen nuevos modelos continuamente, se actualizan versiones y cambian los benchmarks. Para quien está diseñando una solución, esto significa que incluso una decisión aparentemente simple, como elegir un modelo para determinada tarea, puede involucrar un espacio de alternativas difícil de seguir.

Y el problema no termina en el modelo. Una solución que utiliza IA puede involucrar estrategias de inferencia, mecanismos de recuperación, bases de datos vectoriales, técnicas de prompting, herramientas, agentes y diferentes formas de integración. Cada una de estas elecciones abre nuevas posibilidades de composición. La tecnología no solamente añadió una herramienta más al catálogo. Amplió rápidamente el espacio de soluciones que un arquitecto puede considerar.

La IA también reduce drásticamente el costo de experimentar con estas alternativas. Una idea que antes requería días de desarrollo puede transformarse en un prototipo en pocas horas. Esto es una ventaja inequívoca. Pero existe una asimetría interesante: el costo de construir y probar una solución puede caer mucho más rápidamente que el costo de comprender sus consecuencias arquitectónicas.

Podemos, por lo tanto, llegar a la implementación antes de llegar a la comprensión. Podemos construir un prototipo funcional, integrarlo con otros servicios e incluso ponerlo en producción antes de tener una visión suficientemente clara sobre sus costos, limitaciones, dependencias y comportamiento en diferentes condiciones.

Es precisamente por eso que considero la IA una evidencia, y no solamente un ejemplo más, del fenómeno discutido en este artículo. Muestra de forma particularmente evidente que estamos reduciendo el costo de transformar decisiones en software sin reducir en la misma proporción el costo de tomar buenas decisiones.

La IA no elimina el problema de la arquitectura. Hace más evidente la diferencia entre conseguir construir algo y saber si deberíamos construirlo de esa manera.

Y esa diferencia importa porque el costo de una decisión arquitectónica rara vez aparece en el momento en que se toma.

## El costo de una decisión aparece después

Una mala decisión arquitectónica no necesita producir inmediatamente un sistema roto. Muchas veces, produce un sistema que funciona perfectamente dentro de las premisas existentes en el momento de la elección.

El problema aparece cuando esas premisas cambian. Una decisión puede introducir acoplamiento a un proveedor, un modelo de datos difícil de migrar, una dependencia operativa, una arquitectura difícil de escalar o una tecnología que exige competencias muy específicas. Mientras el sistema crece, aquello que parecía una elección simple se vuelve cada vez más difícil de revertir.

Technical debt encuentra una buena analogía en la deuda de tarjeta de crédito. El problema no es solamente lo que dejamos para después, sino los intereses que comienzan a correr mientras aplazamos la corrección. En arquitectura, esos intereses se pagan en forma de complejidad, acoplamiento y costo de cambio.

Un cambio que inicialmente requería apenas una pequeña adaptación puede, algunos años después, involucrar migración de datos, modificación de contratos, cambios en integraciones, capacitación de equipos, reescritura de componentes e interrupciones operativas. El sistema crece alrededor de la elección original, y cada nueva dependencia hace que su reversión sea más costosa.

Por eso, technical debt no es solamente trabajo acumulado. Es el costo creciente de mantener una decisión que ya dejó de ser adecuada.

Existe una diferencia importante entre costo de implementación y costo de reversibilidad. Un servicio gestionado puede resolver un problema en horas. Una arquitectura construida alrededor de él puede permanecer durante años. Cuanto más pasa el sistema a depender de esa elección, mayor tiende a ser el costo de abandonarla.

Esto cambia la forma en que una decisión arquitectónica debería ser evaluada. No basta con preguntar cuánto cuesta implementar una solución. También es necesario preguntar cuánto cuesta cambiarla, qué premisas sustentan esa elección y qué tan fácil será revertirla si esas premisas dejan de ser verdaderas.

Esta preocupación se vuelve aún más importante precisamente porque la tecnología hizo que la adopción fuera tan fácil. Cuanto menor es el costo para comenzar, mayor es la tentación de postergar la pregunta sobre cuánto costará salir.

## El problema de los frameworks

Es en este contexto que comencé a percibir otra cosa. Mi formación en gestión de proyectos me acostumbró a la idea de que una disciplina puede construir un cuerpo de conocimiento relativamente estable, capaz de organizar conceptos, prácticas y decisiones incluso cuando las herramientas y metodologías utilizadas cambian.

En arquitectura de soluciones, no veo el mismo nivel de consolidación. Existen frameworks, métodos y prácticas bastante útiles, pero parecen resolver partes diferentes del problema. Muchas veces, corresponde al propio arquitecto combinar estas piezas para construir su proceso de decisión.

TOGAF es un buen ejemplo. Tiene una función importante y nunca pretendió ser un manual de System Design. Fue concebido para Enterprise Architecture, con una preocupación mucho más amplia por organización, capacidades, gobernanza, procesos y alineamiento estratégico. Por eso, no me parece justo criticarlo por no resolver un problema que no es exactamente el suyo.

Aun así, existe una incomodidad legítima cuando observamos la velocidad con la que cambió el entorno tecnológico. La estructura de conocimiento necesaria para discutir arquitectura parece cambiar más rápidamente de lo que conseguimos consolidarla. Y esto crea una tensión difícil de resolver: si un framework incorpora continuamente nuevas tecnologías y prácticas, corre el riesgo de quedar rápidamente obsoleto; si permanece estable, corre el riesgo de alejarse de la realidad en la que los arquitectos están tomando decisiones.

arc42 ilustra otro lado de esta cuestión. Está mucho más cerca de la práctica de arquitectura de software y ofrece una estructura pragmática para documentar contexto, requisitos de calidad, decisiones arquitectónicas, building blocks, runtime y deployment. Es extremadamente útil para organizar y comunicar una arquitectura. Pero documentar una decisión no es exactamente lo mismo que estructurar el proceso que llevó hasta ella.

Lo mismo ocurre con otras prácticas. Un Architecture Decision Record ayuda a registrar una decisión. C4 ayuda a representar la arquitectura. ATAM ayuda a explorar determinados trade-offs. Cada uno de estos enfoques resuelve un problema real y puede ser bastante útil. Lo que echo en falta es una estructura que conecte estas prácticas en un proceso integral de decisión arquitectónica.

Un ADR puede registrar que se consideraron tres alternativas y que una de ellas fue elegida. Pero registrar una decisión no es lo mismo que estructurar el proceso que llevó hasta ella. ¿Qué criterios deberían considerarse? ¿Cómo evaluar los trade-offs? ¿Cómo ponderar costo, riesgo, complejidad operativa, capacidad del equipo, reversibilidad y dependencia de proveedores? ¿Cuándo una decisión es suficientemente importante como para formalizarla? ¿Cuándo debería revisarse?

Estas preguntas continúan dependiendo, en gran medida, de la experiencia y del juicio de quien está diseñando el sistema.

Tal vez sea precisamente por eso que, en la práctica, sea tan común encontrar una arquitectura representada directamente por los componentes de una cloud en un Draw.io, Lucidchart, Miro o herramienta equivalente, sin que ningún framework de arquitectura aparezca explícitamente en el proceso.

El diagrama comienza a construirse a partir de los servicios disponibles. Una API aquí, una cola allí, una base de datos gestionada, alguna función serverless, quizá un servicio de observabilidad. La arquitectura emerge de la composición de los componentes.

Esto no significa que no exista razonamiento arquitectónico. Existe. El problema es que buena parte de él permanece implícito. El diagrama muestra lo que fue elegido, pero no necesariamente muestra por qué fue elegido, qué alternativas fueron consideradas, qué premisas sustentan la decisión o cuánto costaría deshacerla.

Y quizá esa sea la brecha que realmente me incomoda. No echo de menos un framework que me diga qué tecnología debo utilizar. Echo de menos un cuerpo de conocimiento que ayude a estructurar y comunicar decisiones arquitectónicas sin depender exclusivamente de la experiencia individual de cada arquitecto.

## Un PMBOK de Solution Architecture

Fue en este punto cuando comencé a entender mejor aquella sensación inicial de que faltaba algo. No echo de menos un framework que me diga qué tecnología utilizar. Eso sería inviable en un entorno que cambia tan rápidamente. Echo de menos algo más cercano a lo que PMBOK representa para la gestión de proyectos: un cuerpo de conocimiento que proporcione un lenguaje, principios y estructuras para organizar el proceso de decisión sin necesidad de prescribir la solución.

Cuando hablo de un “PMBOK de Solution Architecture”, no estoy imaginando un manual que diga qué base de datos, cloud o patrón arquitectónico debemos elegir. La idea sería tener una referencia que ayude al arquitecto a estructurar el problema y hacer explícito el razonamiento detrás de las decisiones, sin transformar la arquitectura en un proceso mecánico.

arc42 se acerca bastante a algunos de estos objetivos. Ofrece una estructura pragmática para organizar y comunicar una arquitectura y es una herramienta bastante útil. Pero también evidencia la distinción que estoy intentando hacer: estructurar y documentar una arquitectura no es exactamente lo mismo que estructurar el proceso de decisión que llevó hasta ella.

Lo mismo ocurre con otras prácticas. Los ADR ayudan a registrar decisiones, C4 ayuda a representar arquitecturas y ATAM ayuda a explorar determinados trade-offs. Cada uno de estos enfoques resuelve un problema real. Lo que echo en falta es una estructura que conecte estas prácticas en un proceso más integral, sin exigir que cada arquitecto construya por sí solo este proceso a partir de diferentes referencias.

Tal vez exista una razón para ello. La arquitectura es profundamente contextual, y las decisiones arquitectónicas rara vez tienen una respuesta objetivamente correcta. Una metodología excesivamente prescriptiva podría crear una falsa sensación de precisión o transformar el juicio arquitectónico en cumplimiento de etapas. No tendría sentido sustituir la experiencia del arquitecto por un checklist que intentara determinar la arquitectura correcta para cada situación.

Aun así, creo que es posible sistematizar parte de este conocimiento. La gestión de proyectos ofrece una referencia interesante. PMBOK no determina qué proyecto debe ejecutarse ni qué decisión debe tomar un project manager. Organiza conocimientos, procesos y prácticas que ayudan a estructurar el trabajo en diferentes contextos.

La arquitectura de soluciones podría beber de la misma fuente. No para copiar sus procesos, sino para adoptar un enfoque similar de sistematización: transformar conocimiento disperso en una disciplina que ayude a estructurar decisiones, hacer explícitas las premisas, comunicar el razonamiento y preservar el juicio de quien está diseñando el sistema.

El desafío sería encontrar un nivel de abstracción suficientemente estable para sobrevivir a los cambios tecnológicos y, al mismo tiempo, suficientemente concreto para ayudar a alguien a tomar una decisión real. El objetivo no sería seguir cada nueva tecnología, sino ofrecer una estructura que continúe teniendo sentido cuando las tecnologías cambien.

Tal vez esta sea una de las próximas fronteras de madurez de la disciplina: transformar el conocimiento que hoy está disperso entre frameworks, métodos, prácticas y, principalmente, en la experiencia individual de los arquitectos en un cuerpo de conocimiento más sistemático para la toma de decisiones arquitectónicas.

## El cuello de botella cambió

Tal vez la cuestión no sea si los sistemas se están volviendo más fáciles o más difíciles. Se están volviendo más fáciles de construir y, precisamente por eso, más difíciles de diseñar.

Cloud, servicios gestionados, SaaS e IA redujeron drásticamente el costo de implementar y experimentar con soluciones. El cuello de botella migró de la implementación al juicio: decidir qué construir, qué alternativas descartar, qué trade-offs aceptar y qué consecuencias estamos dispuestos a asumir.

Esto también cambia lo que esperamos de un arquitecto de soluciones. Conocer más tecnologías continúa siendo importante, pero no es suficiente. A medida que crece el espacio de soluciones, se vuelve cada vez más importante saber reducirlo de manera consciente. Tal vez el arquitecto más valioso no sea aquel que conoce más servicios, sino aquel que consigue eliminar alternativas sin eliminar las correctas.

Por eso me incomoda la falta de un “PMBOK de Solution Architecture”. No porque necesitemos otro framework para seguir la próxima tecnología, sino porque quizá necesitemos una disciplina más consolidada para tomar decisiones en un entorno que cambia continuamente.

Construir una solución nunca fue el objetivo de la arquitectura. El objetivo es tomar buenas decisiones sobre aquello que vale la pena construir y preservar, tanto como sea posible, la capacidad de cambiar de opinión cuando cambien las premisas.
