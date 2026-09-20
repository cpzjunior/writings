# Arquitecturas Investigativas: de la recopilación de información a la inteligencia continua

_Una arquitectura orientada por IA para investigar preguntas de negocio, aprender del contexto y acompañar continuamente aquello que puede cambiar una decisión._

**Resumen:** Defiendo una arquitectura de inteligencia que trate la investigación como su unidad principal: un proceso persistente que formula hipótesis, conecta evidencias, preserva contexto y retoma el trabajo cuando surgen nuevas informaciones. Un scheduler decide qué investigaciones merecen procesamiento, cuánto esfuerzo vale la pena invertir y cuál debe ser el siguiente paso, mientras que la memoria, el feedback humano y la gobernanza dan continuidad y confiabilidad al proceso. Así, la IA deja de simplemente recopilar, monitorear o resumir información y pasa a sostener un proceso continuo de investigación, en el cual la propia arquitectura aprende de lo que descubrió y vuelve al problema cuando el mundo cambia.

---

Mientras escribía “[El Anti-Mago: Un Proyecto Literario](https://cpzjunior.substack.com/p/o-anti-mago-um-projeto-literario)”, fui percibiendo que la trayectoria de Alden como investigador me hacía pensar cada vez más sobre el propio acto de investigar: seguir pistas, formular hipótesis, conectar acontecimientos y descubrir que una respuesta puede cambiar la siguiente pregunta. En algún momento, esa idea salió de la ficción. Empecé a pensar que el papel de un investigador también podría ser interesante en un producto. No como metáfora, sino como una forma diferente de pensar los sistemas de inteligencia.

Imaginemos una empresa a punto de contratar a un proveedor estratégico. Antes de firmar el contrato, surge una pregunta simple: ¿existen señales públicas de que ese proveedor esté entrando en una situación que pueda afectar nuestra relación comercial?

Responder a esa pregunta puede involucrar noticias, bases públicas, reclamaciones, información corporativa y redes sociales. Cuando algo parece relevante, son necesarias nuevas búsquedas para comprender el contexto.

Ahora imaginemos entregar esa pregunta a una arquitectura de inteligencia. Investiga al proveedor, sus empresas relacionadas y acontecimientos recientes. Encuentra una noticia relevante, identifica una empresa relacionada y abre una nueva línea de investigación. Después encuentra información contradictoria y busca fuentes más cercanas al hecho original. Una hipótesis gana fuerza, otra pierde relevancia y surge una nueva pregunta. En determinado momento, la arquitectura puede concluir que todavía no existen evidencias suficientes para recomendar una acción y colocar aquella investigación bajo monitoreo.

Días después, surge una nueva información. La investigación vuelve a la cola, pero no comienza desde cero. Retoma el estado anterior, con sus hipótesis, evidencias, fuentes e incertidumbres.

Ese es el comportamiento que me interesa. La misma arquitectura podría investigar a un competidor, una oportunidad de mercado, una tecnología emergente, un potencial cliente o una hipótesis estratégica. El punto de partida deja de ser solamente la entidad que queremos monitorear y pasa a ser la pregunta que necesitamos investigar.

## De monitoreo a investigación

Existe una diferencia importante entre monitorear e investigar. Un sistema de monitoreo puede avisar que una empresa fue mencionada en una noticia, pero la mención, de forma aislada, no necesariamente dice qué ocurrió, cuál es su relevancia o si debería cambiar alguna decisión.

En seguridad de la información, un SOC, Security Operations Center, existe precisamente para lidiar con este problema. Logs, eventos de red, alertas de endpoints y otras fuentes producen continuamente señales que, de forma aislada, pueden significar poco. El SOC correlaciona estos eventos, busca patrones, investiga el contexto, evalúa la severidad y, cuando es necesario, activa una respuesta. Una alerta no es necesariamente un incidente. El trabajo consiste en comprender qué existe detrás de ella.

La misma lógica puede aplicarse a la información pública y a las preguntas de negocio. Una reclamación es una señal. Diez reclamaciones similares en pocos días pueden indicar otra cosa. Un video puede ampliar la exposición, una publicación puede acelerar la propagación y un reportaje puede transformar un problema puntual en un incidente en evolución. El trabajo pasa a ser comprender cómo se relacionan estos eventos, qué hipótesis explican mejor lo que está ocurriendo y qué todavía necesita ser descubierto.

Esto también cambia el papel de la búsqueda. Una búsqueda tradicional termina cuando encontramos una respuesta satisfactoria. En una investigación, el resultado de una búsqueda puede determinar qué debe investigarse a continuación. Una noticia sobre una tecnología puede llevar a investigar a la empresa que la desarrolló. Una adquisición puede generar preguntas sobre inversores, tecnología u otros movimientos relacionados. Una información contradictoria puede requerir una fuente primaria.

La investigación evoluciona conforme aparecen nuevas evidencias. Algunas líneas son descartadas, otras ganan prioridad y surgen nuevas preguntas. La arquitectura necesita acompañar este proceso, manteniendo el contexto de lo que ya fue descubierto y decidiendo cuál debe ser el siguiente paso. La diferencia no está en hacer que una IA investigue Internet. Está en hacer que una arquitectura mantenga una investigación.

Esto también cambia la manera en que pensamos los agentes. En lugar de agentes ejecutando búsquedas permanentemente, podemos tener investigaciones permanentemente existentes, cada una con su propio estado y esperando el momento adecuado para recibir capacidad de procesamiento.

## Un scheduler para investigaciones

Cuando empecé a pensar en esta arquitectura, una analogía con los sistemas operativos me pareció particularmente útil. Un sistema operativo necesita administrar una capacidad limitada de procesamiento entre diversos procesos. Acompaña el estado de cada proceso, define prioridades, interrumpe algunos, retoma otros y distribuye el tiempo de CPU de acuerdo con lo que necesita ser ejecutado.

Una arquitectura investigativa podría funcionar de manera similar. En lugar de tener un conjunto de agentes ejecutando búsquedas continuamente, tendríamos un conjunto de investigaciones persistentes, cada una con su propio estado, prioridad, objetivo, nivel de incertidumbre y presupuesto. Algunas estarían activas, otras esperando nuevas evidencias y otras prácticamente concluidas. El scheduler sería responsable de decidir cuál de ellas recibe la siguiente unidad de capacidad de procesamiento.

Imaginemos decenas o miles de investigaciones ocurriendo simultáneamente. Una acompaña a un proveedor que no presenta ninguna señal relevante desde hace semanas. Otra investiga a un competidor que anunció recientemente una adquisición. Una tercera acompaña una tecnología emergente. Una cuarta intenta comprender una secuencia de reclamaciones que comenzó hace pocas horas. No tendría sentido tratar todas de la misma manera.

La primera quizá solo necesite una nueva verificación periódica. La segunda puede requerir una investigación más profunda. La tercera puede permanecer en baja prioridad hasta que aparezca alguna señal relevante. La cuarta, dependiendo del impacto potencial y de la velocidad de los acontecimientos, puede necesitar recibir capacidad inmediatamente.

Y el siguiente ciclo de procesamiento también depende del estado de la investigación. Una investigación puede comenzar buscando noticias recientes. Después de encontrar una empresa relacionada, el siguiente ciclo puede dedicarse a comprender esa nueva entidad. Si surge una información contradictoria, puede ser necesario buscar una fuente primaria. Si aparece un cambio societario, puede tener sentido investigar a los controladores. Si varias fuentes están reproduciendo la misma información, el siguiente paso puede ser identificar su origen.

El scheduler, por lo tanto, no está simplemente preguntando “¿qué búsqueda ejecutar ahora?”. Está preguntando “¿qué investigación merece atención ahora y cuál es la acción más útil que podemos ejecutar dentro de ella?”.

Esto aproxima la arquitectura a un sistema de procesos concurrentes. Una investigación puede ser interrumpida para dar lugar a otra más urgente. Puede generar una subinvestigación que pasa a competir por recursos. Una línea puede cerrarse mientras otra continúa. Una investigación puede quedar bloqueada esperando nuevas evidencias y volver a la cola cuando algo cambie.

La analogía con el sistema operativo también ayuda a pensar en un problema que suele quedar oculto cuando hablamos de agentes. No necesitamos un agente dedicado para cada problema. Así como un sistema operativo comparte capacidad de procesamiento entre procesos, una arquitectura investigativa puede compartir capacidad agentiva entre investigaciones.

Esto cambia bastante la idea de automatización continua. No estamos creando miles de robots haciendo polling de Internet en intervalos fijos. Estamos manteniendo investigaciones en diferentes estados y decidiendo dinámicamente cuáles merecen procesamiento, cuánto procesamiento deben recibir y cuál debería ser el siguiente paso.

En el límite, el scheduler se convierte en una pieza central de la arquitectura. No es solamente un distribuidor de recursos. Es el mecanismo que transforma una colección de investigaciones persistentes en un sistema capaz de trabajar continuamente sobre ellas.

Y esto nos lleva a una pregunta inevitable: si investigar cuesta recursos, ¿cómo decidir cuándo vale la pena continuar investigando?

## ¿Cuánto vale la pena continuar investigando?

Existe otra cuestión que aparece cuando llevamos esta arquitectura en serio: investigar tiene costos. Hay llamadas a APIs, búsquedas, procesamiento, almacenamiento, inferencia, tiempo de agentes y, en algunos casos, acceso a fuentes de pago. Si el sistema puede profundizar cualquier investigación indefinidamente, podrá producir análisis cada vez más completos, pero también consumir recursos sin que eso necesariamente genere más valor.

Por eso, la arquitectura no solo necesita decidir qué investigar. Necesita decidir cuánto esfuerzo vale la pena dedicar a cada investigación.

Aquí me gusta hacer un juego de palabras con ROI. El ROI tradicional pregunta si vale la pena invertir. En este caso, podemos preguntar si vale la pena investigar. La I pasa a ser de Investigation.

No necesita ser una fórmula rígida. Puede ser una heurística basada en algunas preguntas simples: ¿cuál es la probabilidad de que una nueva información cambie nuestra conclusión? ¿Cuál sería el impacto de ese cambio? ¿Cuánto cuesta obtenerla?

Si la investigación ya posee evidencias consistentes, la incertidumbre restante es pequeña y una nueva búsqueda difícilmente cambiará la decisión, quizá sea mejor reducir la frecuencia, entrar en monitoreo o simplemente cerrar esa línea. Por otro lado, si una única información adicional puede alterar una decisión importante, el siguiente ciclo de investigación puede tener un valor mucho mayor.

Esto crea la idea de un presupuesto investigativo. La arquitectura puede concentrar capacidad donde existe un mayor potencial de información y reducir el esfuerzo donde el retorno marginal ha disminuido. El scheduler pasa a considerar no solo urgencia y riesgo, sino también el valor potencial del siguiente paso.

Y aquí aparece una característica interesante de este problema: probablemente no sabremos de antemano cuál es la mejor estrategia para todas las situaciones. Algunas decisiones se definirán inicialmente mediante heurísticas y después se ajustarán a partir de los resultados observados. La arquitectura puede aprender qué caminos suelen producir evidencias relevantes, cuánto cuestan y en qué momento continuar investigando deja de tener sentido.

Al final, la inteligencia no está solamente en descubrir más. También está en saber cuándo ya hemos descubierto lo suficiente.

## La investigación necesita recordar y aprender

Una investigación no debería simplemente acumular documentos. Necesita trabajar con hipótesis, preservar lo que ya descubrió e incorporar el contexto de quien está investigando.

Supongamos que una secuencia de críticas públicas contra una empresa está creciendo. Una posibilidad es que exista un problema operativo real. Otra es que el problema sea puntual y esté siendo amplificado. Otra es que exista una campaña coordinada. Otra es que diferentes acontecimientos estén siendo agrupados porque parecen similares.

La arquitectura no debería elegir inmediatamente una narrativa y buscar únicamente información que la confirme. Debería mantener hipótesis concurrentes y buscar evidencias que ayuden a diferenciarlas.

Esto exige también separar aquello que fue encontrado de aquello que fue inferido. Una fuente afirma determinado hecho. Eso es evidencia. La conclusión de que ese hecho representa un riesgo específico para la organización es una inferencia. Del mismo modo, una relación entre dos acontecimientos puede ser relevante sin demostrar que uno causó al otro.

La investigación necesita considerar además la independencia de las fuentes. Diez sitios repitiendo la misma noticia no representan necesariamente diez evidencias. Es necesario comprender el origen de la información, identificar duplicaciones y, cuando sea posible, buscar la fuente más cercana al hecho.

Y existe una limitación que debería estar presente en cualquier conclusión: no encontrar información no significa demostrar que determinada cosa no existe. Una conclusión responsable sería: no se encontró ninguna señal relevante dentro del perímetro de fuentes investigado. La diferencia entre certeza y ausencia de evidencia es pequeña en la frase y enorme en la práctica.

Pero este rigor pierde valor si cada investigación comienza desde cero. Para que exista continuidad, la arquitectura necesita preservar lo que estaba siendo investigado, qué hipótesis fueron planteadas, qué evidencias fueron encontradas, qué fuentes fueron consideradas, qué hipótesis fueron descartadas, qué dudas permanecieron abiertas y cuál fue la última conclusión. No basta con guardar el historial de conversaciones con un modelo. Es necesario mantener el estado de la investigación.

Este estado también necesita convivir con el conocimiento específico de la organización. Una empresa puede considerar determinado proveedor crítico mientras que otra puede considerarlo fácilmente sustituible. Una información que representa un riesgo relevante en un contexto puede ser irrelevante en otro. La misma entidad puede tener relaciones completamente diferentes con distintas organizaciones.

Por eso, la arquitectura necesita construir un contexto propio para cada organización, incorporando entidades, relaciones, definiciones, políticas, fuentes preferenciales, clasificaciones, decisiones anteriores y, principalmente, correcciones realizadas por las personas.

Este feedback humano pasa a formar parte del ciclo de la investigación. Un usuario puede corregir una asociación entre empresas, cuestionar una inferencia, confirmar una relación, descartar una hipótesis o indicar que determinada evidencia es más relevante de lo que el sistema consideró. Estas correcciones no deberían desaparecer cuando aquella investigación termina. Pueden modificar el contexto utilizado en las siguientes.

Esto no significa necesariamente volver a entrenar el modelo. Existe una diferencia entre que el modelo aprenda y que la arquitectura aprenda. El modelo puede permanecer exactamente igual mientras la arquitectura acumula conocimiento sobre la organización, incorpora correcciones, identifica qué fuentes son más útiles para determinados problemas y ajusta sus heurísticas.

En este sentido, la arquitectura no aprende solamente sobre el mundo. Aprende de la organización y sobre cómo investigar el mundo.

## La autonomía exige gobernanza

Es tentador llamar a todo esto investigación autónoma, pero existe una distinción importante. La autonomía que me interesa está principalmente en la conducción de la investigación.

El sistema puede decidir qué fuente consultar, qué hipótesis profundizar, cuándo crear una subinvestigación, cuándo reducir el esfuerzo, cuándo buscar evidencia adicional y cuándo regresar a una investigación que estaba detenida.

Esto no significa que deba tomar por sí solo una decisión jurídica, terminar una relación comercial o rechazar a un proveedor. Cuanto mayor sea el impacto de la decisión, mayor debe ser el nivel de gobernanza exigido.

Una arquitectura empresarial necesita permitir diferentes niveles de autonomía, desde observar y alertar hasta recomendar acciones que dependan de aprobación humana. En algunos contextos altamente controlados, determinadas acciones podrían eventualmente automatizarse. En otros, esto sería inadecuado.

Esta autonomía también crea otra exigencia: la arquitectura necesita representar sus incertidumbres y ser capaz de explicar el camino que recorrió.

Cuanto más influya la investigación en una decisión, más importante se vuelve poder reconstruir cómo se alcanzó esa conclusión. Un log técnico puede decir que un agente ejecutó una búsqueda a las 14:32. Eso no explica la investigación.

Sería necesario algo más cercano a una traza investigativa: cuál era la pregunta original, qué hipótesis existían, qué fuentes fueron consultadas, qué evidencias fueron consideradas o descartadas, qué contexto de la organización fue utilizado, qué conclusiones intermedias fueron producidas, por qué se realizó determinada nueva búsqueda y cómo todo esto llevó a la recomendación final.

Si un usuario corrigió una información, esa corrección también debería formar parte de la historia. Si una recomendación fue aceptada y posteriormente resultó inadecuada, ese resultado debería volver al ciclo de aprendizaje de la arquitectura.

La auditabilidad, en este contexto, no es solo una preocupación de compliance. Es parte de la propia calidad de la inteligencia. Cuanto más autonomía damos al sistema, más necesitamos poder entender qué hizo, por qué lo hizo y en qué evidencias se basó.

Una investigación que no puede explicar su camino es mucho más difícil de confiar.

## El mercado ya posee varias de estas piezas

Es importante poner esta idea en perspectiva. No estoy proponiendo una categoría tecnológica que todavía no exista. El mercado internacional ya posee plataformas maduras de inteligencia competitiva y de mercado, monitoreo, investigación asistida por IA y análisis de fuentes externas. En 2026, por ejemplo, Gartner ya trata Competitive and Market Intelligence Platforms como una categoría propia de evaluación, contemplando capacidades como agregación de fuentes, validación, búsqueda y análisis con IA, gestión del conocimiento e integración empresarial.

También existen soluciones que trabajan con grandes volúmenes de fuentes, monitoreo continuo y generación de insights sobre competidores, mercados y otras entidades estratégicas. En Brasil, hay empresas que actúan en inteligencia competitiva, monitoreo, inteligencia de mercado, reputación y análisis de información. Por lo tanto, no veo novedad en cada uno de estos componentes de forma aislada.

La cuestión que me parece más interesante es otra: ¿cómo reorganizar estas capacidades en torno a la investigación como unidad principal? En lugar de comenzar por la entidad y preguntar qué ocurrió con ella, propongo que la arquitectura comience por la pregunta y, a partir de ella, descubra qué entidades, fuentes, acontecimientos y relaciones necesitan ser investigados. La búsqueda deja de ser una ejecución aislada que termina en un informe y pasa a formar parte de una investigación que evoluciona conforme aparecen nuevas evidencias. El informe deja de ser el punto final y la decisión pasa a ser un estado que puede ser revisitado siempre que nuevas informaciones puedan cambiar lo que sabemos.

Es en esta composición donde veo espacio para una arquitectura diferente. No para sustituir las capacidades que ya existen, sino para conectarlas en un proceso investigativo persistente, capaz de adaptar su profundidad, priorizar el uso de recursos, incorporar conocimiento organizacional y aprender del feedback.

También veo espacio para adaptar esta arquitectura al contexto brasileño, donde las fuentes públicas, las estructuras societarias, el entorno regulatorio, las características del mercado y las necesidades de gobernanza pueden exigir estrategias específicas de investigación. En ese caso, la adaptación al contexto no sería solo una capa de localización, sino parte de la propia inteligencia del sistema.

## De la recopilación de información a la inteligencia continua

Cuando estas ideas se unen, la arquitectura deja de parecer simplemente un mecanismo de búsqueda sofisticado. La información pasa a ser el combustible de una investigación persistente, capaz de formular preguntas, acompañar hipótesis, preservar contexto, decidir los siguientes pasos y regresar al problema cuando surjan nuevas evidencias. La IA participa en este proceso, pero es la arquitectura la que proporciona continuidad, memoria, contexto y gobernanza.

Esto cambia la pregunta central. En lugar de comenzar por “¿qué modelo vamos a utilizar?”, quizá sea más interesante preguntar “¿cómo vamos a organizar el proceso mediante el cual el sistema investiga?”. Algunas respuestas se definirán inicialmente mediante heurísticas y otras se descubrirán en la práctica. Con el tiempo, la arquitectura puede aprender qué fuentes funcionan mejor para determinados problemas, qué caminos producen evidencias relevantes y cuándo continuar investigando deja de generar valor. No se trata solo de hacer que el modelo responda mejor, sino de hacer que el sistema investigue mejor.

Si observamos esta evolución, primero construimos sistemas para recopilar información. Después, sistemas para monitorearla. Más recientemente, sistemas capaces de resumir y analizar grandes volúmenes de contenido. El siguiente paso puede ser una arquitectura en la cual la información deje de ser el producto final y pase a alimentar un proceso continuo de investigación.

Todavía existen muchas cuestiones por definir sobre prioridad, costo, calidad, heurísticas y autonomía. Más que problemas que deban resolverse de una única forma, estas variables pueden formar parte de la propia configuración del producto, permitiendo adaptar el comportamiento de la arquitectura al contexto, al riesgo y a los objetivos de cada organización. La diferencia entre una herramienta de investigación y una inteligencia continua puede estar precisamente ahí: no en encontrar más información o producir mejores resúmenes, sino en construir un sistema capaz de investigar preguntas, aprender de lo que descubrió y volver al problema cuando el mundo cambie.
