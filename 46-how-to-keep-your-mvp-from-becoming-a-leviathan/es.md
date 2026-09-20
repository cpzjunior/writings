# Cómo impedir que tu MVP se convierta en un Leviatán

_Entre la complejidad que anticipa el futuro y la simplicidad que impide el aprendizaje._

**Resumen:** Un MVP no es el producto más pequeño que podemos poner en marcha, sino el conjunto mínimo necesario para probar una hipótesis y aprender algo relevante del resultado. El riesgo está tanto en construir demasiado, anticipando problemas que quizá nunca existan, como en construir demasiado poco y comprometer la validez del aprendizaje. Por eso, la complejidad debe ser proporcional a lo que sabemos, a los riesgos que realmente importan y a las preguntas que necesitamos responder en ese momento. El MVP puede crecer a medida que aprendemos, pero ese crecimiento debe ser consecuencia del conocimiento adquirido, no del intento de anticipar el futuro.

---

He visto a mucha gente con buenas ideas enfrentar dificultades para sacarlas del papel. Abordé parte de este problema en “[Antes de sacar una idea del papel, primero hay que ponerla en él](https://cpzjunior.substack.com/p/antes-de-tirar-uma-ideia-do-papel)“, pero existe una dificultad que comienza precisamente cuando la idea deja de ser solo una idea y pasa a construirse: mantener el MVP pequeño sin comprometer su viabilidad.

La intención inicial suele ser simple. Construir lo suficiente para poner una hipótesis a prueba y aprender del resultado. El problema es que, a medida que avanza la construcción, surgen buenas razones para ampliar el alcance. Una funcionalidad parece necesaria, una excepción parece importante, una decisión arquitectónica puede generalizarse, una preocupación por la escala futura parece prudente. Poco a poco, aquello que debería servir para probar una hipótesis comienza a incorporar respuestas para problemas que todavía ni siquiera sabemos si tendremos.

Para facilitar el registro de los usuarios, vamos a implementar diferentes mecanismos de autenticación, como SSO y OAuth. Como el sistema necesita considerar diferentes niveles, perfiles y reglas de acceso, necesitaremos un modelo de permisos multidimensional, al estilo de plataformas corporativas como Salesforce. Como tendremos un sistema de suscripciones, construiremos un ledger basado en blockchain y un sistema de geolocalización para el antifraude. Para garantizar disponibilidad total, adoptaremos una arquitectura multicloud en múltiples AZs. Para anticiparnos a una eventual expansión a América Latina y Asia, también tendremos soporte para múltiples localidades y configuraciones regionales. Cuando nos damos cuenta, empezamos intentando validar una hipótesis de producto y estamos diseñando una plataforma distribuida globalmente para resolver problemas hipotéticos incluso antes de saber si el producto resuelve el problema para el que fue creado.

Ahí surge la comparación con el Leviatán. En la tradición bíblica, el Leviatán es un monstruo asociado al mar y al caos, una criatura que escapa al dominio humano. La comparación es casi literal: el MVP comienza como algo pequeño y controlable, pero puede acumular funcionalidades, dependencias, reglas y excepciones hasta transformarse en un monstruo cuya complejidad ya no responde fácilmente a la intención que dio origen al producto.

Pero existe una trampa en el sentido contrario. En el intento de mantener el MVP bajo control, podemos recortar precisamente los elementos necesarios para probar la hipótesis. El resultado es pequeño, pero ya no es suficientemente viable para decirnos si estamos ante una solución adecuada.

Es en esta tensión, entre construir demasiado y construir demasiado poco, donde comienza la discusión sobre qué debe realmente caber dentro de un MVP.

## El MVP no es un producto pequeño

MVP suele entenderse como un producto con pocas funcionalidades. Es una definición intuitiva, pero insuficiente. Lo “mínimo” no está en la cantidad de software que podemos construir, sino en el menor conjunto necesario para poner a prueba una hipótesis relevante de forma suficientemente confiable.

Esta distinción cambia la manera en que decidimos qué entra en el producto. La pregunta no debería ser “¿cuál es la menor cantidad de código que podemos poner en producción?”, sino “¿cuál es la menor inversión capaz de enseñarnos algo relevante sobre el producto?”. La segunda pregunta nos obliga a considerar no solo lo que se construirá, sino también la calidad del aprendizaje que aquello será capaz de producir.

Una funcionalidad puede ser sencilla de implementar y, aun así, ser indispensable para probar la hipótesis. Otra puede requerir poco esfuerzo y no aportar prácticamente nada a lo que necesitamos descubrir. El esfuerzo de desarrollo, por tanto, no es un buen indicador aislado de relevancia. Lo que importa es la contribución de esa parte al experimento.

Por eso un MVP pequeño puede ser inadecuado. Al eliminar una parte esencial de la experiencia, podemos poner algo en marcha rápidamente, pero producir un resultado que no responde a la pregunta original. En ese caso, reducimos el producto sin necesariamente reducir la incertidumbre. Construimos menos, pero también aprendemos menos.

El mismo razonamiento vale para el exceso. Una solución puede ser técnicamente sofisticada y funcionar perfectamente, pero incorporar capacidades que todavía no son necesarias para probar la tesis. El problema, en ese caso, no está necesariamente en la calidad de la solución, sino en el momento en que elegimos construirla. Estamos invirtiendo para responder preguntas que el producto todavía no nos ha obligado a plantear.

El tamaño del MVP, por tanto, no es una medida absoluta. Debe ser proporcional a lo que queremos descubrir en ese momento.

### Cómo nace el Leviatán

El crecimiento del MVP rara vez ocurre por causa de una gran decisión. Suele nacer de la sucesión de pequeñas decisiones que, tomadas individualmente, parecen perfectamente defendibles. Una integración parece necesaria, una excepción parece sencilla de acomodar, una estructura más genérica parece evitar retrabajo, una preocupación por la escala parece prudente. Una configuración adicional parece barata. Una funcionalidad solicitada por un usuario parece demasiado importante como para dejarla fuera.

Es en este contexto donde aparece el conocido “ya que estamos haciendo esto, también podemos hacer aquello”. Con cada decisión, el alcance se desplaza un poco. Como ningún cambio parece suficiente para justificar una interrupción, la suma de ellos pasa desapercibida hasta que el producto ya está respondiendo a problemas que no formaban parte de la pregunta original.

El punto más traicionero es que el costo de una decisión rara vez termina en su implementación. Una nueva funcionalidad pasa a exigir pruebas, monitoreo, documentación, soporte y mantenimiento. Puede introducir dependencias, nuevos estados, reglas de negocio y caminos de ejecución que antes no existían. También puede restringir decisiones futuras, haciendo más costoso cambiar de dirección cuando aparezca nueva información.

Por eso, el costo de una funcionalidad no es solo el esfuerzo necesario para ponerla en producción. También es todo aquello que pasa a existir después de que entra en el sistema.

Así es como el alcance puede escapar de la intención original sin que exista un error evidente que señalar. Cada decisión local puede tener sentido, mientras que el resultado acumulado deja de tenerlo. El Leviatán no nace necesariamente de una elección absurda, sino de la suma de elecciones razonables que, juntas, producen una complejidad que nadie pretendía construir.

## El problema de intentar resolver el mundo

Existe una forma particularmente peligrosa de anticipación: intentar construir, desde el principio, la solución para todos los problemas que el producto quizá tenga en el futuro.

Cuando la tesis todavía es incierta, comenzamos a imaginar diferentes perfiles de usuario, modelos de negocio, grandes volúmenes de datos, múltiples integraciones, necesidades de internacionalización, diferentes niveles de permisos y escenarios de escala. Cada preocupación puede ser legítima de forma aislada. El problema aparece cuando todas ellas pasan a influir en la primera versión del producto.

Es comprensible. Quien construye sistemas sabe que algunas decisiones son difíciles de cambiar después y que determinadas elecciones pueden generar deuda técnica. También sabe que corregir una arquitectura inadecuada más tarde puede ser mucho más caro que tomar una buena decisión desde el principio. El riesgo está en transformar esa preocupación legítima en un intento de predecir el producto entero antes incluso de saber si es, de hecho, una solución adecuada y viable.

Es como asumir el papel de Atlas antes de saber si habrá un mundo que sostener: cargamos anticipadamente con el peso de todos los futuros posibles, incluso sin saber cuáles de ellos realmente existirán.

Hay una inversión ahí. En lugar de que la solución evolucione a partir de lo que aprendemos sobre el problema, comenzamos a construir una solución para un futuro hipotético. Pasamos a tomar decisiones basándonos en usuarios que quizá existan, volúmenes que quizá se alcancen, mercados que quizá se exploren y requisitos que quizá nunca aparezcan.

Ese futuro tiene un costo en el presente. Y, en la etapa inicial, quizá ni siquiera sepamos si llegaremos hasta él.

La arquitectura debe lidiar con riesgos reales, no con todas las posibilidades imaginables. Lo mismo vale para el producto. Una decisión merece una inversión proporcional a la importancia y a la probabilidad del problema que pretende resolver. Prepararlo todo para una escala que quizá nunca exista es pagar anticipadamente por un futuro que todavía no ha sido validado.

## La complejidad también puede ser necesaria

Esto no significa que toda complejidad sea una señal de exceso. Hay productos en los que la seguridad, la auditoría, la resiliencia, la observabilidad, el control de acceso o los requisitos operativos forman parte de la propia solución. En esos casos, retirar complejidad no significa necesariamente simplificar el producto. Puede significar retirar una propiedad necesaria para que funcione correctamente.

En determinados contextos, simplificar demasiado el sistema puede ser precisamente la decisión irresponsable. Un MVP que mueve dinero, trata datos sensibles o participa en procesos críticos no puede utilizar la experimentación como justificación para ignorar propiedades esenciales del dominio. El hecho de que estemos validando una hipótesis no suspende los riesgos que ya existen.

También existe una diferencia entre la complejidad percibida por el usuario y la complejidad necesaria en el sistema. Una experiencia puede ser sencilla en la superficie y depender de una infraestructura bastante sofisticada para funcionar de manera segura, resiliente y confiable. El objetivo, por tanto, no es eliminar la complejidad, sino evitar una complejidad que no tenga una razón concreta para existir en ese momento.

Por eso, la pregunta no debería ser simplemente “¿cómo hacer que el sistema sea más sencillo?”, sino “¿qué complejidad es necesaria para esta etapa del producto?”. La respuesta depende tanto de la hipótesis que queremos validar como de los riesgos que no podemos aceptar.

Esta distinción también ayuda a evitar una falsa oposición entre producto e ingeniería. Producto puede estar intentando reducir el alcance para validar una hipótesis, mientras que ingeniería puede estar intentando reducir un riesgo técnico relevante o evitar una decisión difícil de revertir. Ambas preocupaciones son legítimas. El trabajo de arquitectura consiste precisamente en evaluar estos trade-offs y encontrar una solución proporcional a la etapa del producto, sin transformar la simplicidad o la sofisticación en principios absolutos.

## Construir menos también puede ser un error

La reacción al exceso suele ser recortar. Eliminamos funcionalidades, simplificamos flujos y reducimos el alcance hasta llegar a algo que parezca lo suficientemente pequeño como para llamarlo MVP. El problema es que reducir el producto no significa necesariamente aumentar la calidad del experimento.

Existe una diferencia importante entre reducir lo que se construirá y reducir la capacidad de aprender de aquello que se construyó. Una hipótesis puede depender de determinados elementos de la experiencia para ser probada de forma mínimamente representativa. Retirar precisamente esos elementos puede producir un resultado aparentemente objetivo, pero que responde a una pregunta diferente de la que pretendíamos plantear.

Podemos, por ejemplo, concluir que una solución no funciona cuando, en realidad, probamos una versión tan simplificada que dejó de representar la propuesta de valor original. En ese caso, construimos menos, pero también aprendimos menos.

Por eso, el MVP no sirve solo para poner algo en producción. Necesita producir un resultado que sea útil para la siguiente decisión. Cuanto más se simplifica la solución, más importante se vuelve entender qué se preservó y qué se eliminó. Una simplificación que elimina precisamente el elemento responsable de conectar el problema con la solución puede hacer que el experimento sea barato, pero poco informativo.

En algunos casos, incluso, el mejor MVP puede no ser software. Un prototipo, una operación manual o un piloto limitado pueden responder a la pregunta con menos inversión y menos complejidad. Si podemos probar la hipótesis sin construir todo el sistema, quizá esa sea la forma más adecuada de empezar.

El objetivo no es construir lo mínimo posible. Es construir solo lo necesario para que el resultado nos diga algo que valga la pena saber.

## El MVP necesita ser diagnosticable

Este quizá sea uno de los criterios más importantes para decidir qué entra en una primera versión: cuando termine el experimento, necesitamos poder interpretar lo que ocurrió.

Un MVP puede fallar por diferentes motivos. La hipótesis sobre el problema puede ser incorrecta. La solución puede no ser adecuada. La experiencia puede no funcionar como esperábamos. El precio puede ser incorrecto. El canal de adquisición puede no funcionar. La tecnología puede imponer alguna limitación. La operación puede ser inviable. El resultado observado es consecuencia de una combinación de estas variables, y no siempre es posible determinar con precisión cuál de ellas fue responsable.

Cuantas más cosas cambiamos simultáneamente, más difícil resulta interpretar el resultado. Un producto puede haber sido rechazado porque la propuesta de valor no tenía sentido, porque la experiencia era mala o simplemente porque una limitación de la implementación impidió que el usuario percibiera el valor de la solución. Sin cierto cuidado en la composición del MVP, un resultado negativo puede decir muy poco sobre la hipótesis que pretendíamos probar.

Esto no significa que todo MVP deba ser un experimento controlado o que sea posible aislar perfectamente cada variable. Los productos reales rara vez ofrecen ese nivel de control. Significa simplemente que necesitamos preservar cierta capacidad de distinguir lo que estamos aprendiendo. Existe una diferencia entre aceptar la incertidumbre inherente al producto e introducir tanta complejidad en el experimento que el propio resultado se vuelva difícil de interpretar.

Un MVP, por tanto, necesita ser más que ejecutable. Necesita ser diagnosticable. Su resultado debe ser capaz de orientar la siguiente decisión, ya sea para corregir la solución, reformular la hipótesis o simplemente abandonar una dirección que no haya demostrado ser prometedora.

## El mínimo también se mueve

Hay otro aspecto importante: el MVP no es una categoría permanente del producto. La tesis de un producto puede cambiar a medida que surgen nuevas evidencias. Una hipótesis inicial puede ser refinada, descartada o sustituida por otra más sofisticada. Las preguntas también cambian. En consecuencia, aquello que era suficiente para probar una hipótesis en determinado momento puede dejar de ser suficiente para responder a la siguiente pregunta.

Una solución sencilla puede ser adecuada para descubrir si determinado problema realmente existe. Después, puede ser necesario entender si la solución propuesta es suficientemente valiosa para ser adoptada. Más adelante, quizá sea necesario evaluar la retención, el comportamiento a escala, la integración con otros sistemas o algún aspecto operativo que no formaba parte de la pregunta inicial.

En este proceso, el concepto de mínimo se desplaza. Una tesis más sofisticada puede exigir una solución más sofisticada. Esto no significa que el MVP haya fracasado y se haya convertido en un producto inflado. Puede significar simplemente que aprendimos lo suficiente como para formular mejores preguntas y, por tanto, necesitamos una solución capaz de responderlas.

La cuestión está en la dirección de este movimiento. La complejidad debe acompañar la evolución de la tesis, y no intentar anticiparla. El producto puede crecer a medida que aumenta el conocimiento sobre el problema, los usuarios y la propia solución. Lo que no tiene sentido es construir anticipadamente aquello que solo tendría sentido después de haber aprendido.

El problema no es que el MVP crezca. El problema es que crezca antes de que sepamos por qué necesita crecer.

## Cuando el MVP empieza a convertirse en un Leviatán

La señal más preocupante quizá no sea el número de funcionalidades, el tamaño del código o la cantidad de componentes arquitectónicos. Es cuando la complejidad deja de estar claramente relacionada con el propósito de la primera versión.

En algún momento, puede volverse difícil explicar por qué determinadas partes del producto existen, qué preguntas ayudan a responder o qué riesgos concretos justificaron su inclusión. Las decisiones empiezan a tomarse para escenarios que todavía no existen, las excepciones comienzan a moldear el comportamiento principal y una parte creciente del esfuerzo pasa a ser consumida por la propia complejidad del sistema.

Este es el punto en el que vale la pena volver a la pregunta que dio origen al MVP: ¿qué estamos intentando descubrir?

La respuesta también impide el movimiento contrario. No todo lo que puede eliminarse debería eliminarse. Una funcionalidad puede ser indispensable para que la hipótesis sea probada de manera válida, aunque parezca aumentar el tamaño de la primera versión. El objetivo nunca fue construir el sistema más pequeño posible, sino una solución proporcional a lo que sabemos, a lo que todavía necesitamos descubrir y a los riesgos que realmente importan.

Por eso, el Leviatán no es simplemente un MVP grande. Es el MVP que perdió el control sobre su propia complejidad.

Una primera versión no necesita ser una versión reducida de todo aquello que imaginamos construir en el futuro. Necesita ser una respuesta deliberadamente limitada a las preguntas que tenemos ahora. A medida que aprendemos, la tesis puede cambiar, pueden surgir nuevas preguntas y la solución puede necesitar crecer. En ese caso, el crecimiento deja de ser anticipación y pasa a ser consecuencia del conocimiento adquirido.

El peligro comienza cuando hacemos el camino inverso: construimos primero y esperamos que el futuro nos dé una razón para todo aquello. En ese escenario, aquello que debería ayudarnos a descubrir el camino puede terminar creando un camino que tendremos dificultades para abandonar.
