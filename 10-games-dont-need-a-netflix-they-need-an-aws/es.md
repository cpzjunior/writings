# Los juegos no necesitan una Netflix, necesitan una AWS

_Si el error fundamental de los servicios de juegos por suscripción fuera tratar el catálogo de juegos como el producto, cuando el verdadero producto que el usuario quiere alquilar es capacidad computacional?_

**Resumen:** Defiendo que el cloud gaming se está planteando con el modelo equivocado: en lugar de transformar los juegos en una Netflix, deberíamos separar el juego de la máquina que lo ejecuta. El usuario no necesita cientos de títulos, sino acceso a la capacidad computacional necesaria para jugar aquello que eligió, sin tener que comprar hardware para varios años. Así como la nube transformó la computación en una infraestructura elástica, los juegos podrían ejecutarse en máquinas alquiladas bajo demanda, mientras la compra y la distribución de los juegos permanecen independientes. El futuro, por lo tanto, puede estar menos en una Netflix de los juegos y más en una AWS de los juegos.

---

Compré una Xbox Series S con una idea bastante sencilla en mente: quería jugar mis juegos favoritos sin tener que montar un PC gamer. El Game Pass parecía ser la solución perfecta. Una suscripción, una biblioteca enorme y una consola relativamente barata. En la práctica, descubrí algo curioso: el catálogo es gigantesco, pero pocos juegos realmente me interesan. Hay cientos de títulos disponibles, pero sigo queriendo jugar esencialmente los mismos géneros y algunas franquicias específicas. El tamaño del catálogo, que debería ser la principal justificación de la suscripción, termina teniendo poco significado cuando los juegos que realmente quiero jugar representan una fracción minúscula de él.

El problema se hizo aún más evidente cuando empecé a pensar en el hardware. La Series S sigue siendo una consola capaz, pero ya puedo ver el camino que está siguiendo. Los juegos más recientes exigen cada vez más al hardware, y aquello que hoy es una máquina perfectamente adecuada gradualmente se convierte en una máquina limitada por la generación para la que fue diseñada. Mi PC tampoco resuelve el problema. Ya tiene algunos años y, aunque sigue siendo perfectamente útil para muchas cosas y ejecuta juegos que continúan siendo excelentes, ya no tiene capacidad para acompañar cómodamente los lanzamientos más exigentes. Tengo, por lo tanto, dos problemas diferentes: una biblioteca de juegos mucho mayor que aquello que efectivamente quiero jugar y un conjunto de hardware que necesita ser reemplazado periódicamente para acompañar la evolución de los juegos.

Fue en ese punto cuando empecé a cuestionar si estamos mirando el problema de la manera correcta. No quiero cientos de juegos. Quiero jugar algunos juegos específicos. Tampoco quiero necesariamente comprar una nueva máquina en cada generación. Quiero tener acceso a la capacidad computacional necesaria para ejecutar el juego que decidí jugar en ese momento. Estas dos necesidades parecen bastante diferentes de aquello que los servicios de suscripción y el mercado tradicional de hardware están intentando vender.

La pregunta que se me ocurrió fue sencilla: ¿y si el error fundamental de los servicios de juegos por suscripción fuera tratar el catálogo de juegos como el producto, cuando el verdadero producto que el usuario quiere alquilar es la capacidad computacional?

## El problema de transformar los juegos en Netflix

Tal vez el problema esté precisamente en el intento de transformar los videojuegos en una categoría de entretenimiento similar a las películas y las series. La analogía funciona en algunos aspectos, pero falla en un punto fundamental: un juego no es solo contenido. También es una aplicación que necesita ser ejecutada.

Cuando veo una película, el trabajo computacional pesado ya se realizó durante la producción. El servicio necesita almacenar y transmitir el vídeo de manera eficiente. Cuando juego un título moderno en la nube, la situación es completamente diferente. El servidor necesita ejecutar el juego en tiempo real. Cada movimiento del control altera el estado del juego, la CPU y la GPU procesan esa información, se renderiza una nueva imagen, se codifica y se envía por la red hasta mi pantalla, mientras mis comandos hacen el camino inverso.

Esto cambia completamente la naturaleza del producto. En el streaming tradicional, el contenido es el principal producto y la infraestructura existe para entregarlo. En el cloud gaming, el contenido sigue siendo necesario, pero la capacidad computacional pasa a ser una parte esencial de aquello que se está vendiendo. Cuando alguien utiliza cloud gaming porque no posee un PC capaz de ejecutar determinado juego, lo que esa persona está efectivamente intentando comprar es acceso temporal a una máquina suficientemente potente.

Esto también expone una limitación del modelo basado en catálogo. Existe una premisa de que cuantos más juegos estén disponibles, mayor será el valor de la suscripción. Pero esa relación no es necesariamente verdadera para los videojuegos. Un jugador puede tener interés en apenas algunos géneros y franquicias específicas. Cientos de títulos adicionales pueden representar una cantidad enorme de contenido disponible y, al mismo tiempo, casi ningún valor adicional para ese usuario.

La diferencia respecto de las películas y las series es importante. Cuando me suscribo a un servicio de vídeo, puedo ver una serie policial hoy, una comedia mañana, un documental el fin de semana y quizá una película de ciencia ficción después. El coste de experimentar algo nuevo es bajo. En los juegos, la inversión es mucho mayor. Muchos títulos requieren decenas de horas y una adaptación a sus propias mecánicas, sistemas, controles y progresión. El jugador no está simplemente consumiendo contenido. Está aprendiendo a operar un sistema interactivo.

Es posible, por lo tanto, tener un catálogo enorme y aun así ofrecer poco valor para determinado usuario. La cantidad de juegos disponibles es una métrica objetiva, pero no necesariamente una buena métrica de utilidad.

Y eso plantea una cuestión bastante extraña sobre el modelo actual: si ya sé qué juego quiero jugar, ¿por qué necesito suscribirme a un catálogo entero para tener acceso a la máquina que puede ejecutarlo?

Si compré Elden Ring, por ejemplo, y quiero jugarlo en un ordenador que no posee una GPU adecuada, el problema que tengo no es la falta de acceso a juegos. Ya tengo el juego. El problema es la falta de capacidad computacional.

Tal vez el producto que el cloud gaming debería vender sea precisamente esa capacidad.

## AWS y GPU como servicio

La computación en la nube encontró una solución para un problema muy parecido. Una empresa que necesita capacidad computacional no necesita comprar un servidor para los próximos cinco años. Puede alquilar infraestructura según la necesidad. Si necesita más procesamiento, aprovisiona una máquina más grande. Si necesita menos, reduce la capacidad. Si no necesita nada, apaga los recursos.

La gran innovación no fue simplemente colocar servidores en un datacenter y acceder a ellos por internet. Fue transformar la capacidad computacional en un recurso elástico, que puede ser aprovisionado, dimensionado y consumido según la demanda.

El mismo principio podría aplicarse a los juegos. En lugar de comprar una GPU para los próximos años, el jugador podría alquilar capacidad computacional cuando la necesitara. En lugar de elegir una máquina que debe seguir siendo suficiente durante toda una generación, podría elegir la configuración necesaria para el juego que pretende ejecutar en ese momento.

Un servicio de este tipo podría ofrecer diferentes clases de máquinas. Una configuración más barata podría atender juegos menos exigentes o jugadores dispuestos a renunciar a calidad gráfica. Una configuración intermedia podría ofrecer una experiencia en 1080p o 1440p. Una máquina más potente podría atender a quienes desean gráficos al máximo, altas tasas de cuadros o ray tracing. El usuario elegiría la capacidad según aquello que pretende jugar y cuánto está dispuesto a gastar.

Esta posibilidad cambia completamente la relación entre jugador y hardware. Hoy, cuando compro una GPU, necesito intentar prever cuáles serán mis necesidades futuras. Si compro una tarjeta muy potente, pago por una capacidad que quizá no utilice durante buena parte del tiempo. Si compro una tarjeta más barata, corro el riesgo de descubrir algunos años después que ya no es suficiente para los juegos que quiero jugar. En ambos casos, estoy haciendo una apuesta anticipada.

En la nube, esa decisión deja de ser permanente. Imaginemos que, en lugar de una suscripción tradicional, pudiera simplemente comprar créditos de computación. Pongo R$ 100 en mi cuenta y utilizo ese saldo mientras juego. Una máquina básica puede consumir pocos créditos por hora, mientras que una máquina equipada con una GPU de última generación consume mucho más. El precio de la sesión pasa a reflejar directamente la capacidad computacional que estoy utilizando.

Si quiero jugar un título relativamente ligero durante veinte horas, puedo elegir una máquina más sencilla y hacer que mis créditos duren bastante. Si quiero pasar cinco horas en un juego extremadamente pesado, puedo elegir una máquina premium y aceptar un consumo mayor. Si no juego durante un mes entero, no hay motivo para consumir créditos.

El modelo puede seguir teniendo planes recurrentes, pero la suscripción dejaría de representar principalmente el acceso a un catálogo. Podría funcionar como una cartera de computación, con créditos acumulados y consumidos según el uso. La diferencia parece pequeña, pero económicamente es enorme: paso a pagar por aquello que efectivamente estoy utilizando, y no por una colección de juegos que quizá nunca abra.

Esto también crea una relación mucho más transparente entre precio y experiencia. Si quiero una imagen mejor, más resolución o una GPU más potente, pago más. Si estoy dispuesto a aceptar una máquina más sencilla, pago menos. El servicio no necesita decidir de antemano qué configuración deben recibir todos los usuarios.

La diferencia fundamental es que la unidad de valor deja de ser el juego disponible y pasa a ser la capacidad computacional consumida. El juego sigue siendo necesario, pero la infraestructura deja de ser un detalle invisible y pasa a ser el propio servicio.

## El hardware deja de ser una apuesta

Existe además una consecuencia más profunda. El hardware local exige que el consumidor anticipe el futuro.

Cuando compro una consola o una GPU, estoy comprando una determinada cantidad de capacidad computacional que espero que sea suficiente durante varios años. No sé cuáles serán los requisitos de los juegos futuros, pero necesito tomar una decisión hoy.

Esto es particularmente relevante cuando pensamos en la velocidad con la que evoluciona la tecnología gráfica. Una máquina que parece potente en el lanzamiento de una generación puede seguir funcionando perfectamente durante muchos años, pero gradualmente empieza a exigir compromisos: reducir la resolución, disminuir la calidad gráfica, renunciar al ray tracing o aceptar tasas de cuadros menores.

Mi Series S no deja de funcionar cuando aparece una nueva generación de juegos. Mi PC tampoco se transforma en una máquina inútil. Lo que ocurre es más sutil: dejan de ofrecer la capacidad computacional necesaria para ejecutar determinados juegos de la manera que me gustaría.

En el modelo de cloud gaming, esta obsolescencia puede desplazarse del consumidor al proveedor. Cuando llega una nueva generación de GPUs, puede añadirse al datacenter. Cuando determinado hardware envejece, puede seguir disponible como una opción más barata para juegos menos exigentes. El usuario no necesita comprar una nueva máquina para acompañar la evolución de la infraestructura.

Esto no significa que la obsolescencia desaparezca. Simplemente deja de ser un problema que cada consumidor necesita resolver individualmente y pasa a ser un problema de infraestructura que el proveedor administra a escala.

En lugar de preguntar qué hardware necesito comprar hoy para seguir jugando durante los próximos cinco años, puedo simplemente preguntar qué capacidad necesito para jugar el título que quiero jugar hoy.

Este es un cambio conceptual importante. El consumidor deja de hacer una apuesta sobre el futuro de la tecnología y pasa a consumir la capacidad computacional disponible en el presente.

## El juego y la máquina no necesitan ser el mismo producto

El modelo tradicional juntó dos cosas porque era necesario. La consola o el PC proporcionaba la capacidad computacional y el juego se ejecutaba localmente. La llegada de la nube hace posible separar estas dos capas.

Puedo comprar un juego independientemente de la máquina que lo ejecutará. Puedo tener mi biblioteca en una plataforma digital y utilizar hardware local cuando sea suficiente. Cuando no lo sea, puedo utilizar una infraestructura remota. El juego sigue siendo mi producto de entretenimiento, mientras que la máquina pasa a ser un servicio separado.

Esto significa que no necesitamos necesariamente una “Netflix de los juegos” para hacer que el cloud gaming funcione. El catálogo de juegos puede seguir siendo un producto de las propias plataformas. Sony, Microsoft y Nintendo pueden seguir vendiendo juegos, manteniendo sus bibliotecas, ofreciendo títulos exclusivos y construyendo sus propios ecosistemas. Lo que cambia es que el hardware necesario para ejecutar esos juegos puede ser proporcionado por otra capa de la industria.

Una empresa podría especializarse exclusivamente en infraestructura para juegos. No necesitaría poseer una biblioteca de títulos ni negociar exclusividades. Su función sería proporcionar máquinas capaces de ejecutar los juegos que el usuario ya posee, de la misma manera que un proveedor de nube proporciona servidores para aplicaciones que pertenecen a otras empresas.

Esto permitiría que el mercado de cloud gaming compitiera por infraestructura en lugar de competir exclusivamente por catálogo. Un proveedor podría ofrecer precios menores, otro podría tener menor latencia, otro podría poner a disposición GPUs más modernas y otro podría tener datacenters mejor ubicados geográficamente.

La biblioteca de juegos seguiría siendo una capa independiente. Incluso podría ser el principal diferencial competitivo de una plataforma. El usuario podría elegir dónde comprar sus juegos en función del precio, exclusividades, servicios o conveniencia y, por separado, elegir dónde ejecutar esos juegos en función de la capacidad computacional, latencia y coste.

Este desacoplamiento es precisamente una de las características más poderosas de la computación en la nube. La aplicación no necesita ser dueña del servidor. La empresa no necesita comprar el hardware que ejecuta su software. La infraestructura se convierte en una capa independiente, consumida según la necesidad.

No existe una razón fundamental para que los juegos sean diferentes. El juego puede ser un producto. La máquina puede ser un servicio. Y no hay necesidad de que ambos sean vendidos por la misma empresa.

## ¿Qué estamos realmente alquilando?

Esta quizá sea la pregunta que la industria debería hacerse. Estamos hablando de dos productos diferentes que fueron colocados en el mismo paquete: acceso a los juegos y acceso a la capacidad computacional necesaria para ejecutarlos.

Una suscripción de juegos resuelve el primer problema. El usuario paga para acceder a un catálogo, que puede ser amplio, exclusivo o simplemente conveniente. Es un modelo de distribución de software y contenido. El cloud gaming resuelve el segundo. El usuario paga para utilizar remotamente una máquina capaz de ejecutar el juego. Es un modelo de infraestructura.

No existe ninguna razón para que estos dos productos tengan que venderse juntos.

Puedo comprar un juego de Microsoft, Sony, Nintendo o cualquier otra tienda y ejecutarlo en mi PC. Si mi hardware no es suficiente, puedo alquilar capacidad computacional de un proveedor especializado. La empresa que vende el juego no necesita ser la misma que proporciona la máquina, al igual que la empresa que desarrolla una aplicación no necesita ser dueña del servidor que la ejecuta.

Esto crea dos mercados diferentes. Por un lado, las plataformas compiten por juegos, precios, exclusividades, servicios y bibliotecas. Por otro, los proveedores de infraestructura compiten por precio, rendimiento, latencia, disponibilidad y eficiencia operativa.

El problema de los modelos actuales es que frecuentemente tratamos estos dos mercados como si fueran uno solo. La suscripción de juegos intenta vender el catálogo junto con la infraestructura, mientras que la propuesta de cloud gaming termina presentándose como una forma diferente de consumir una suscripción.

Pero no tiene por qué ser así. Puedo querer jugar apenas tres juegos durante un año y no tener interés en cientos de otros títulos. Puedo comprar esos tres juegos y, cuando mi hardware no sea suficiente, alquilar una máquina capaz de ejecutarlos. En ese escenario, no necesito una suscripción de juegos. Necesito un juego y capacidad computacional.

La nube permite precisamente esta separación. El juego puede seguir siendo un producto comprado o suscrito, mientras que la máquina puede ser una utility consumida bajo demanda.

La industria pasó décadas vendiéndonos ordenadores cada vez más potentes para ejecutar juegos cada vez más exigentes. La nube ofrece la posibilidad de invertir esta relación: en lugar de comprar una máquina para acompañar los juegos, podemos alquilar la capacidad necesaria para ejecutar el juego que elegimos.

Tal vez el futuro de la industria de los juegos no sea una Netflix de los videojuegos, sino una AWS de los juegos.
