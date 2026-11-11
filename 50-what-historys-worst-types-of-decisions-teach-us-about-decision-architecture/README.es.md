# Lo que los peores tipos de decisión de la historia nos enseñan sobre arquitectura de decisiones

_Sobre lo que los errores de imperios, gobiernos y empresas revelan acerca de estrategia, gestión y toma de decisiones_

**Resumen:** Me gusta la historia porque permite observar cómo las decisiones, los recursos, las restricciones y los incentivos se combinan a lo largo del tiempo. En este texto, utilizo algunos casos históricos y empresariales para entender por qué ciertas decisiones colocaron a organizaciones en posiciones difíciles de revertir, ya fuera por un error en la forma de ver el problema, por la creación de dependencias, por la pérdida de opciones o por la dificultad de cambiar de rumbo a tiempo. Lo que me interesa no es juzgar estas decisiones por el resultado que conocemos hoy, sino entender qué había detrás de ellas cuando fueron tomadas y qué consecuencias estaban implícitas en cada camino. Es esta perspectiva la que quiero explorar cuando pienso en arquitectura de decisiones.

---

Me gusta la historia. Soy fan de juegos como Europa Universalis, Victoria y Civilization y sigo la geopolítica por el mismo motivo por el que me gustan estos juegos: la posibilidad de observar cómo las decisiones, los recursos, las restricciones y los incentivos se combinan para producir resultados a lo largo del tiempo. Esta perspectiva también está detrás de un texto que escribí anteriormente, “[Arquitectura de soluciones aplicada a mercados financieros, gobiernos, cadenas de suministro y geopolítica](https://cpzjunior.substack.com/p/arquitetura-de-solucoes-aplicada)”. En él, utilicé la arquitectura de soluciones como una lente para entender sistemas complejos. Pero me di cuenta de que faltaba una capa: las decisiones que construyen estos sistemas. Eso es lo que quiero explorar aquí. No como una colección de fracasos históricos, sino como un análisis de diferentes tipos de decisión que pueden colocar a las organizaciones en posiciones difíciles de revertir.

Y existe una diferencia importante. Algunas de las empresas que aparecen en este texto quebraron. Otras no. Algunas decisiones produjeron consecuencias catastróficas. Otras simplemente colocaron a una organización en una posición peor que aquella que podría haber ocupado. El resultado final, por lo tanto, no es el único criterio. Lo que me interesa es la calidad de la elección frente a las informaciones, restricciones, incentivos y alternativas disponibles en aquel momento.

El paralelismo entre los casos históricos y empresariales tampoco está en los acontecimientos en sí. Una guerra no equivale a la gestión de una empresa, así como un imperio no es una corporación. Lo que podemos comparar es la estructura de la elección: cómo se definió un problema, qué objetivos orientaron la acción, qué recursos estaban disponibles y qué alternativas parecían viables en aquel momento.

Esto también exige cuidado con el hindsight bias. Una elección que produjo un mal resultado no fue necesariamente una mala elección, así como una elección que salió bien no fue necesariamente una buena decisión. El desafío consiste en volver al momento de la elección e intentar entender qué tenía sentido, qué fue ignorado y qué premisas sustentaban ese camino.

La selección de los casos es, naturalmente, subjetiva. Sería posible elegir decenas de otros ejemplos, quizás más conocidos o incluso más extremos. Los siete casos de este texto fueron elegidos porque permiten observar mecanismos diferentes y, principalmente, porque ayudan a construir el argumento sobre arquitectura de decisiones. El objetivo no es establecer un ranking de las peores decisiones de la historia, sino utilizar algunos casos particularmente ilustrativos para entender cómo diferentes tipos de decisión pueden alterar la capacidad de una organización para responder a lo que viene después.

Es desde esta perspectiva que vale la pena observar algunos de los peores tipos de decisión de la historia.

## Craso × New Coke: el error de modelado

En 53 a. C., Marco Licinio Craso se enfrentó a los partos en Carras, en Mesopotamia. Roma poseía una de las fuerzas militares más poderosas del mundo conocido, pero eso no impidió que la campaña terminara en una derrota catastrófica.

Es tentador explicar el episodio por la arrogancia de Craso o por la superioridad de la caballería parta. Pero eso significa observar la decisión después de conocer el resultado. Para entender el problema, es más interesante retroceder un paso y preguntarse cómo veía Craso la situación antes de la batalla.

Roma tenía una ventaja militar real. Sus legiones eran experimentadas, disciplinadas y capaces de derrotar a adversarios muy poderosos. Esa experiencia creaba una expectativa razonable: frente a un nuevo enemigo, la superioridad de las legiones seguiría siendo el principal factor de la campaña. El problema es que esa conclusión trataba la capacidad militar romana como una propiedad casi independiente del contexto en el que sería empleada.

En Carras, el contexto era una parte central del problema. Los partos podían explotar la movilidad de la caballería, mantener la distancia de las tropas romanas y utilizar arqueros montados para atacar sin ofrecer al ejército romano la oportunidad de emplear sus principales ventajas. El terreno y las condiciones de abastecimiento también aumentaban el peso de estas diferencias. La cuestión, por lo tanto, no era simplemente quién poseía el ejército más poderoso, sino si la forma en que Roma obtenía ventaja militar seguía siendo válida en aquel entorno.

Craso no estaba tomando una decisión con información cero. Tenía una capacidad militar comprobada y experiencia suficiente para confiar en ella. El problema estaba en la premisa operativa: la idea de que una capacidad que funcionaba muy bien en determinados contextos seguiría produciendo una ventaja cuando las condiciones del problema cambiaran.

Es exactamente este tipo de error lo que hace que New Coke sea un caso interesante. Coca-Cola tampoco tomó su decisión a ciegas. La empresa realizó una extensa investigación y utilizó pruebas ciegas de sabor en las que muchos consumidores demostraban preferencia por la nueva fórmula. Había, por lo tanto, una evidencia concreta de que el cambio podía funcionar.

Pero había una diferencia entre aquello que medía la prueba y aquello que la empresa necesitaba decidir. La prueba respondía, esencialmente, a una pregunta sobre preferencia de sabor en una situación controlada. La decisión de Coca-Cola, sin embargo, era mucho mayor: sustituir el producto original, una marca con décadas de historia, hábitos de consumo, identidad y una fuerte asociación emocional.

La empresa transformó una evidencia sobre una dimensión del producto en una conclusión sobre el producto como un todo. La premisa implícita era algo parecido a: si los consumidores prefieren el nuevo sabor en una prueba, entonces la nueva fórmula será un mejor sustituto de la Coca-Cola original. El dato podía ser correcto. El salto entre el dato y la decisión era lo problemático.

Ahí es donde el paralelismo con Craso se vuelve más claro. En ambos casos, había una evidencia legítima que sustentaba la confianza en la decisión. Roma tenía una fuerza militar extremadamente eficaz. Coca-Cola tenía pruebas que indicaban preferencia por la nueva fórmula. El problema fue tratar esa evidencia como suficiente para representar el sistema que realmente necesitaba ser comprendido.

Craso necesitaba saber si las condiciones que convertían a las legiones en una ventaja seguían presentes en aquel teatro de operaciones. Coca-Cola necesitaba saber si la preferencia de sabor justificaba sustituir un producto cuya propuesta de valor incluía mucho más que el sabor. En ambos casos, una variable relevante fue tomada como representación suficiente de un problema más amplio.

Este tipo de error es particularmente peligroso porque no necesariamente se presenta como falta de información. Muchas veces ocurre lo contrario. Hay datos, especialistas, análisis, modelos y precedentes suficientes para dar a la decisión una apariencia de rigor. Lo que puede estar equivocado es la relación entre esas informaciones y la representación del problema que se pretende resolver.

En arquitectura de soluciones, conocemos este riesgo. Una solución puede ser técnicamente excelente y, aun así, resolver el problema equivocado. Podemos elegir una tecnología adecuada, diseñar una integración robusta y automatizar un proceso con eficiencia, pero partir de una definición equivocada de la necesidad. En ese caso, mejorar la solución no corrige el error. Solo hace más eficiente la ejecución de una premisa equivocada.

La arquitectura de decisiones comienza antes de elegir entre alternativas. Comienza por entender qué problema estamos realmente intentando resolver, cómo estamos representando ese problema, qué premisas sustentan esa representación y qué condiciones necesitan permanecer verdaderas para que la decisión siga teniendo sentido.

## Napoleón en Rusia × Lehman Brothers: el exceso de dependencia

En 1812, Napoleón invadió Rusia al frente de una fuerza gigantesca. La escala era, en sí misma, una demostración extraordinaria de capacidad militar. Un ejército más grande significaba más tropas, más caballería, más artillería y una mayor capacidad para sostener operaciones en diferentes frentes.

Pero una capacidad de este tamaño no existe de forma aislada. Para poder emplearse, necesitaba una estructura capaz de sostenerla.

A medida que el ejército avanzaba hacia el interior de Rusia, las distancias aumentaban y, con ellas, las necesidades de abastecimiento, transporte, comunicación y coordinación. La fuerza necesitaba alimentar a un contingente enorme, mover equipos, mantener líneas de suministro y seguir operando a una distancia cada vez mayor de sus bases. Cada una de estas funciones dependía de las demás.

Esto cambia la naturaleza del problema. No basta con preguntar cuánta capacidad posee una solución. Es necesario entender de cuántas condiciones depende esa capacidad para seguir disponible.

La campaña de Rusia expuso esta relación. La fuerza de Napoleón no dejó de ser poderosa simplemente porque avanzara. El problema era que su poder de combate dependía de una estructura logística cada vez más difícil de mantener. Un fallo en cualquier parte de esta estructura podía reducir la capacidad de todo el sistema.

Lehman Brothers presentó un mecanismo similar en el sistema financiero. Durante los años anteriores a la crisis de 2008, el banco había construido una operación de enorme escala, con una fuerte presencia en los mercados de capitales y una exposición relevante al mercado inmobiliario. El apalancamiento ampliaba los retornos sobre el capital, mientras que la expansión de las operaciones aumentaba la capacidad de generar ingresos.

Ninguna de estas características era necesariamente problemática de forma aislada. La escala puede generar eficiencia y permitir que una institución opere en mercados que serían inviables a menor dimensión. El apalancamiento también puede ser racional cuando los activos son líquidos, los riesgos se comprenden y las condiciones de financiación permanecen favorables.

El problema surge cuando la capacidad pasa a depender de una extensa cadena de condiciones que funcionan simultáneamente.

Una institución como Lehman dependía de financiación, liquidez, contrapartes, mercados activos, valoraciones de activos y confianza para mantener sus operaciones funcionando. Mientras estas condiciones permanecían favorables, la estructura podía parecer eficiente. Cuando algunas de ellas comenzaron a deteriorarse, las interdependencias hicieron que los problemas en una parte del sistema afectaran a otras.

Ahí es donde el paralelismo con Napoleón se vuelve más claro. No se trata de decir que un ejército y un banco son lo mismo. El mecanismo común está en la dependencia estructural.

Napoleón no necesitaba solo soldados. Necesitaba que la alimentación, el transporte, la comunicación, los caballos, las municiones y las líneas de suministro funcionaran en conjunto. Lehman no necesitaba solo capital. Necesitaba que la financiación, la liquidez, las contrapartes, la valoración, los mercados y la confianza permanecieran disponibles simultáneamente.

En ambos casos, la capacidad final del sistema era mucho mayor que la capacidad de cualquiera de sus componentes de forma aislada. Pero eso también significaba que la interrupción de una condición crítica podía comprometer una parte significativa del resultado producido por el conjunto.

Esta es una distinción importante en arquitectura de soluciones. Cuando añadimos componentes, integraciones, proveedores, mercados o capas a una solución, estamos aumentando su capacidad, pero también aumentando el número de relaciones que necesitan mantenerse. Cada nueva dependencia crea una condición adicional para que el sistema siga funcionando como fue diseñado.

Por eso, la pregunta arquitectónica no debería ser solo “¿cuánta más capacidad podemos añadir?”. También necesitamos preguntar “¿de cuántas condiciones depende esta capacidad?” y “¿cuáles de ellas son críticas para que el sistema siga funcionando?”.

Una solución puede ser extremadamente poderosa y, aun así, poseer una estructura de dependencias tan extensa que pequeñas perturbaciones produzcan efectos desproporcionados.

El riesgo no está solo en construir algo complejo. Está en construir una capacidad cuyo funcionamiento dependa de que demasiadas condiciones sigan siendo verdaderas al mismo tiempo.

## Alaska rusa × IBM: la pérdida de opcionalidad

En 1867, Rusia vendió Alaska a Estados Unidos por US$ 7,2 millones. Retrospectivamente, la decisión parece extraordinariamente barata frente al valor económico y estratégico que el territorio adquiriría posteriormente. Pero evaluarla solo por lo que sabemos hoy sería ignorar las condiciones en las que se tomó la decisión.

Alaska era remoto, caro de administrar y difícil de defender. Después de la Guerra de Crimea, también existía una preocupación concreta: en un eventual conflicto con el Reino Unido, Rusia podía perder el territorio sin conseguir defenderlo adecuadamente y sin recibir ninguna compensación. Dentro de estas premisas, vender el territorio y transformar una posición difícil de sostener en dinero inmediato era una decisión defendible.

El problema es que una decisión puede ser racional frente al presente y, aun así, revelar un coste cuando el futuro se materializa. Al vender Alaska, Rusia resolvió una cuestión inmediata, pero también eliminó una posibilidad futura. No había garantía de que esa posibilidad tuviera un gran valor. El territorio podía seguir siendo caro, remoto y poco relevante durante décadas. Mantener la posición también habría tenido un coste. La cuestión no era simplemente elegir entre una decisión correcta y otra incorrecta, sino decidir cuánto valía preservar una opción cuyo retorno futuro era incierto.

El valor de esta opción solo quedó claro posteriormente, con el descubrimiento de recursos naturales y la transformación de Alaska en una posición económica y geopolítica relevante. Esto no convierte la venta en irracional en 1867. Muestra cómo las decisiones tomadas para resolver problemas presentes pueden eliminar posibilidades que solo adquieren valor después.

La historia de IBM presenta una dinámica similar, aunque en otro tipo de sistema. Cuando entró en el mercado de las computadoras personales, IBM tenía un problema concreto: necesitaba lanzar rápidamente un producto competitivo en un mercado que se estaba formando. Para ello, adoptó una arquitectura relativamente abierta y utilizó componentes de terceros. La decisión funcionó. El IBM PC fue un enorme éxito y ayudó a establecer un estándar que sería ampliamente adoptado por la industria.

Pero algunas decisiones que hicieron posible este éxito inicial también alteraron las opciones estratégicas de IBM para el futuro. La contratación de Microsoft para proporcionar el sistema operativo es un ejemplo conocido. IBM necesitaba una solución rápida y competitiva, mientras que Microsoft estructuró un modelo que permitía licenciar el sistema a otros fabricantes. Al mismo tiempo, el uso de componentes de terceros y la arquitectura relativamente abierta del PC contribuyeron a la formación de un ecosistema de compatibles.

Nada de esto significa que IBM haya “perdido el PC”. Había conseguido exactamente lo que necesitaba en aquel primer momento: poner un producto competitivo en el mercado y convertirlo en un éxito comercial. El problema apareció después. El ecosistema que creció alrededor del IBM PC permitió que otras empresas acumularan posiciones estratégicas en capas fundamentales de la arquitectura. Microsoft ganó escala en el sistema operativo. Intel ganó escala en los procesadores. Los fabricantes de computadoras pudieron producir máquinas compatibles.

IBM había resuelto el problema presente, pero algunas de las decisiones tomadas para resolverlo permitieron que otros actores capturaran valor y construyeran posiciones que posteriormente serían difíciles de recuperar.

Ahí es donde el paralelismo con Alaska se vuelve más claro. En ambos casos, la decisión se tomó frente a una necesidad concreta y tenía una lógica propia en aquel momento. Rusia necesitaba lidiar con los costes y riesgos de mantener un territorio remoto. IBM necesitaba entrar rápidamente en un mercado emergente. En ambos casos, la elección produjo beneficios inmediatos.

Lo que reveló el futuro fue el valor de algunas posibilidades que habían sido sacrificadas durante el proceso. Esta es una dimensión importante de la arquitectura de decisiones. Al elegir una alternativa, no solo estamos eligiendo aquello que queremos obtener. También estamos alterando el conjunto de alternativas que estarán disponibles después.

El desafío es que preservar opciones también tiene un coste. Mantener una posición territorial, una tecnología, una capacidad interna o el control sobre determinada capa de una arquitectura exige recursos. Por lo tanto, no tiene sentido tratar la preservación de opciones como un objetivo absoluto. Algunas opciones son demasiado caras de mantener y otras no tienen suficiente valor estratégico para justificar ese coste.

La cuestión es reconocer que este trade-off existe. Una decisión orientada exclusivamente al problema actual puede parecer eficiente porque transforma la incertidumbre en un resultado inmediato. Pero, al hacerlo, puede consumir una opción cuyo valor todavía no somos capaces de ver.

Es esta pregunta la que conecta Alaska con IBM: no solo “¿qué resuelve esta decisión ahora?”, sino también “¿qué posibilidades futuras hace más difícil recuperar esta decisión?”.

El futuro no puede predecirse con precisión. Pero podemos reconocer que algunas decisiones consumen opcionalidad. Y quizá solo percibamos el valor de aquello que cerramos cuando ya no sea posible volver a abrirlo.

## Italia en la Segunda Guerra Mundial × Yahoo: el error de priorización

Italia entró en la Segunda Guerra Mundial con ambiciones mayores que su capacidad para sostenerlas. Sus limitaciones industriales, logísticas, de combustible y transporte exigían elecciones. No había capacidad para transformar todos los objetivos políticos y militares en campañas simultáneas. Era necesario identificar qué posiciones podían producir un mayor impacto estratégico y concentrar en ellas los recursos disponibles.

El Mediterráneo era una de esas posiciones. Malta, Gibraltar y el Canal de Suez afectaban las rutas de abastecimiento, el movimiento de tropas y la capacidad británica para operar en la región. Controlar estos puntos no garantizaría una victoria italiana, pero podía alterar las condiciones de varias otras operaciones. Una estrategia de concentración podía, por lo tanto, buscar primero las posiciones capaces de modificar el equilibrio regional.

Italia siguió otro camino. En 1940, abrió una campaña en el norte de África y avanzó desde Libia hacia Egipto. La ofensiva terminó siendo detenida y sufrió un contraataque británico que destruyó gran parte de la fuerza italiana. Para evitar el colapso de la posición italiana, Alemania tuvo que enviar tropas y equipos a la región, creando una dependencia adicional.

Ese mismo año, Italia abrió otro frente al invadir Grecia. La campaña, que debía ser rápida, encontró resistencia y se prolongó. Alemania acabó interviniendo nuevamente en los Balcanes. Recursos que podrían haber estado concentrados en otras posiciones pasaron a ser necesarios para sostener operaciones que habían creado sus propias necesidades logísticas.

Lo que llama la atención de estos movimientos no es que Italia hubiera elegido objetivos completamente carentes de valor. El norte de África, Grecia y el Mediterráneo tenían importancia estratégica. La cuestión era la cantidad de capacidad necesaria para perseguir cada objetivo y qué dejaba de ser posible cuando esa capacidad quedaba comprometida.

Este es el punto central de la priorización: los recursos empleados en un frente no están disponibles para otro. Una operación militar, al igual que una iniciativa empresarial, no consume solo la inversión inicial. Crea costes de sostenimiento, exige capacidad de ejecución y puede generar nuevas demandas a medida que avanza.

Yahoo enfrentó una elección similar en otro contexto. A comienzos de los años 2000, la empresa ocupaba una de las mayores posiciones de internet. Tenía audiencia, portal, correo electrónico, publicidad, distribución y una presencia relevante en búsquedas. Y tomó decisiones que podrían haber fortalecido precisamente esta última posición. En 2002, compró Inktomi para reforzar su tecnología de búsqueda. En 2003, adquirió Overture, fortaleciendo su posición en publicidad asociada a las búsquedas.

Había, por lo tanto, una posición estratégica que podía profundizarse. Yahoo podía concentrar capital, talento y atención en búsquedas y publicidad e intentar transformar esa combinación en una ventaja cada vez más difícil de desplazar.

Pero esta no fue la única dirección elegida. Yahoo continuó ampliando su cartera de productos y realizando adquisiciones en diferentes áreas. Compró Flickr, una plataforma con enorme relevancia en fotografía digital. Invirtió en contenido, medios, comunicación y móvil. En 2013, adquirió Tumblr por unos US$ 1.100 millones, apostando a que su enorme audiencia podría transformarse en una nueva fuente de crecimiento y publicidad.

Estas decisiones no eran necesariamente irracionales de forma aislada. Tumblr tenía una comunidad enorme. Flickr tenía una posición relevante en fotografía. El contenido y el móvil eran mercados importantes. El punto es otro: cada una de estas apuestas competía por el mismo conjunto limitado de capital, talento y atención ejecutiva.

Mientras tanto, Google concentraba sus recursos en una posición que se volvía cada vez más valiosa: búsquedas y publicidad. Esta concentración producía ventajas acumulativas. Más usuarios generaban más consultas y datos; más datos y escala mejoraban la publicidad; más ingresos permitían nuevas inversiones en producto e infraestructura.

Yahoo tenía una posición inicial suficientemente fuerte como para disputar ese mercado. Pero la empresa no transformó esa posición en una ventaja acumulativa comparable. En 2009, terminó transfiriendo a Microsoft la infraestructura de su búsqueda, manteniendo la experiencia del usuario y la relación con los anunciantes. La decisión tenía justificaciones financieras y operativas, pero también significaba reducir el control sobre una capacidad tecnológica central precisamente cuando Google consolidaba su liderazgo.

El contraste es importante. Yahoo no estaba eligiendo entre una oportunidad y ninguna oportunidad. Tenía demasiadas oportunidades. El desafío era decidir cuál de ellas merecía suficiente concentración de recursos como para convertirse en decisiva.

Una adquisición puede verse, en este sentido, como una conquista territorial. La empresa utiliza capital para ocupar una posición, pero después necesita invertir en integración, tecnología, personas y operación para mantenerla. Si esa posición no refuerza una ventaja estratégica mayor, puede consumir recursos sin mejorar proporcionalmente la posición de la organización.

Lo mismo se aplica a un nuevo frente militar. Conquistar territorio no es lo mismo que crear ventaja. Es necesario evaluar cuánto cuesta llegar hasta él, cuánto cuesta sostenerlo y si su importancia justifica retirar recursos de otras posiciones.

Ahí es donde el paralelismo entre Italia y Yahoo se vuelve más claro. Ambos tenían objetivos relevantes y recursos limitados. La cuestión no era identificar todas las oportunidades posibles, sino determinar cuáles merecían suficiente concentración para alterar el equilibrio del sistema.

La prioridad, por lo tanto, no es una lista de cosas importantes. Es una decisión sobre dónde colocar capacidad y, en consecuencia, dónde aceptar no colocarla.

La estrategia no consiste en perseguir todas las oportunidades. Consiste en elegir las posiciones que merecen suficientes recursos para convertirse en decisivas.

## Japón en Pearl Harbor × Blockbuster: el coste del tiempo

En diciembre de 1941, Japón atacó Pearl Harbor con el objetivo de reducir la capacidad de la flota estadounidense en el Pacífico y crear espacio para su expansión en el Sudeste Asiático. Como operación militar, el ataque fue significativo. Como decisión estratégica, sin embargo, llevaba un problema estructural: Japón estaba iniciando una guerra contra una potencia con una capacidad industrial muy superior.

Esto no convierte la decisión simplemente en irracional. Japón enfrentaba importantes restricciones económicas y estratégicas, y las alternativas también implicaban riesgos. La cuestión era evaluar no solo el resultado inmediato, sino el tipo de conflicto que esa elección hacía probable.

El ataque creaba una ventaja inicial que necesitaba convertirse rápidamente en una nueva realidad estratégica. Cuanto más se prolongara la guerra, mayor sería la capacidad estadounidense para movilizar recursos. Pearl Harbor, por lo tanto, no resolvía el problema central. Creaba una ventana de oportunidad que Japón tendría que aprovechar antes de que cambiara el equilibrio de fuerzas. La cuestión no era solo qué podía destruirse en ese momento, sino cuánto tiempo compraría realmente la ventaja obtenida.

Blockbuster enfrentó una dinámica diferente, pero comparable. La empresa tenía una posición dominante en el alquiler de películas, una marca fuerte y una enorme red de tiendas. Mantener el modelo tradicional todavía generaba ingresos y, por lo tanto, no era una decisión irracional a corto plazo. El problema era que el mercado ya mostraba señales de un cambio estructural.

La trayectoria de Netflix ilustra este cambio. La empresa comenzó con el alquiler de DVD por correo y un modelo de suscripción que eliminaba parte de las limitaciones de los videoclubes tradicionales. Después avanzó hacia el streaming y ayudó a transformar el comportamiento del consumidor.

Blockbuster llegó a reaccionar. Creó un servicio de suscripción y posteriormente invirtió en iniciativas digitales. Pero la transformación competía con un negocio físico que todavía era grande y rentable. La cuestión pasó a ser cuánto capital, talento y atención debían desplazarse de una operación que funcionaba para financiar una alternativa cuyo retorno todavía era incierto.

Mientras Blockbuster protegía la rentabilidad del modelo existente, Netflix acumulaba experiencia, clientes y capacidad tecnológica para el mercado que estaba surgiendo.

El punto común entre los dos casos está en el horizonte de la decisión. En Japón, la ventaja militar inmediata recibió más peso que el riesgo de una guerra prolongada. En Blockbuster, la rentabilidad del negocio existente dificultó atribuir suficiente peso a la velocidad de la transformación del mercado.

En ambos casos, había alternativas y ninguna ofrecía garantía de éxito. El problema estaba en la forma en que se comparaban. El criterio utilizado favorecía aquello que todavía funcionaba, mientras subestimaba el coste de esperar.

El problema, por lo tanto, no era solo elegir entre alternativas. Era reconocer que el valor de cada alternativa cambiaba con el tiempo. Una posición que parece suficiente hoy puede volverse mucho más difícil de sostener mañana, mientras que una oportunidad que parece incierta puede perder valor si no se explota mientras todavía existe espacio para construirla.

Una arquitectura de decisiones necesita considerar no solo el retorno de una elección, sino también la velocidad con la que están cambiando las condiciones que sostienen ese retorno.

El tiempo, en este sentido, también es un recurso estratégico. Una decisión puede consumir tiempo, comprar tiempo o transformar una ventana de oportunidad en una obligación de actuar después.

A veces, la decisión que parece más segura hoy es precisamente la que deja menos tiempo para construir la siguiente posición.

## Operación Barbarroja × WeWork: la dependencia de la escala

La Operación Barbarroja comenzó con una apuesta por escala y velocidad. La ofensiva alemana contra la Unión Soviética presuponía que una campaña rápida permitiría destruir gran parte de la capacidad soviética antes de que el conflicto se transformara en una guerra prolongada.

El problema logístico no era desconocido. La campaña de Napoleón contra Rusia, poco más de un siglo antes, ya había demostrado cómo la distancia, el abastecimiento, el transporte y las condiciones del territorio podían comprometer una fuerza militar muy superior. Los planificadores alemanes conocían este precedente y sabían que una campaña en el interior de la Unión Soviética produciría desafíos logísticos extraordinarios.

La respuesta no fue eliminar esta dependencia, sino apostar a que la velocidad y la escala permitirían superarla. Cuanto mayor fuera la fuerza empleada y más rápidamente avanzara, mayor sería la posibilidad de destruir la capacidad soviética antes de que los problemas de sostenimiento se volvieran decisivos. La propia escala de la operación era, por lo tanto, parte de la apuesta para resolver una limitación que ya era conocida.

Cuando esta premisa no se confirmó, la propia expansión comenzó a crear problemas adicionales. Una fuerza que avanza necesita abastecerse. Cuanto mayor es la distancia, mayores son las necesidades de transporte, combustible, municiones y mantenimiento. Cuanto mayor es el territorio ocupado, mayor es la estructura necesaria para sostenerlo. Una operación diseñada para avanzar rápidamente pasa a enfrentar otra lógica cuando necesita permanecer en el territorio conquistado.

El problema no era simplemente haber avanzado demasiado. Cada etapa de la expansión aumentaba los recursos necesarios para sostener la siguiente. La apuesta por la escala creaba una dependencia creciente de que la propia expansión siguiera funcionando.

WeWork ayuda a observar el mismo mecanismo en una organización empresarial. La empresa dependía de la escala para sostener una estructura operativa cuyo coste crecía junto con la propia expansión. Más espacios significaban una mayor presencia y más clientes potenciales, pero también más contratos, costes fijos y capital necesario para mantener la operación.

Esto creaba una dependencia creciente: captar recursos para expandirse, expandirse para aumentar los ingresos y aumentar los ingresos para sostener la estructura construida.

El problema aparece cuando esta dinámica necesita continuar indefinidamente. Los recursos son finitos. Existe un límite para el capital disponible, para la capacidad de absorción del mercado y para el crecimiento que puede convertirse en ingresos suficientes para financiar la estructura existente.

Cuando el coste de la expansión crece junto con la propia expansión, crecer deja de ser una forma de capturar una oportunidad y pasa a ser una condición para mantener lo que ya se ha construido.

Ahí es donde el modelo revela su fragilidad. Mientras los recursos disponibles crecen más rápidamente que las obligaciones creadas, la estructura puede parecer sostenible. Cuando esta relación se invierte, la expansión acumulada deja de producir suficiente ventaja para compensar el coste que creó.

La misma lógica aparece en proyectos y productos. Una arquitectura puede dimensionarse para una escala futura que nunca llega. Una operación puede asumir costes fijos apostando por una demanda aún inexistente. Una empresa puede construir una estructura cuya viabilidad dependa de un volumen que debe alcanzarse para que la propia estructura tenga sentido.

El problema no es crecer. El problema es cuando la siguiente etapa deja de ser una oportunidad y pasa a ser una necesidad. En ese punto, la organización deja de utilizar el crecimiento para construir capacidad y pasa a utilizar recursos futuros para sostener decisiones pasadas.

El riesgo está en construir una estructura cuya sostenibilidad dependa precisamente de la condición que ella misma necesita seguir expandiendo para alcanzar.

## Dinastía Ming × Google: la pérdida de oportunidades

Este caso se aparta un poco del orden cronológico porque trata de un tipo diferente de decisión. En los anteriores, analizamos elecciones que colocaron a las organizaciones en trayectorias difíciles de revertir. Aquí, el problema está en dejar de desarrollar una capacidad porque su valor inmediato parece pequeño, sin considerar el coste de reconstruirla si las condiciones cambian.

A comienzos del siglo XV, las expediciones marítimas asociadas a Zheng He demostraron una extraordinaria capacidad naval y logística de la China Ming. Grandes flotas atravesaron el océano Índico, llegaron a regiones distantes y proyectaron poder diplomático y comercial.

Estas expediciones fueron interrumpidas en la década de 1430, en medio de cambios de prioridades, disputas políticas, preocupaciones fiscales y cuestiones relacionadas con la defensa del territorio. La historia es más compleja que la narrativa de que China simplemente “dejó de explorar” y, por eso, quedó atrás. La actividad marítima Ming continuó de otras formas, y no existe consenso histórico en que el fin de las grandes expediciones haya sido una decisión única que determinara el futuro chino.

Aun así, el episodio plantea una cuestión importante: ¿cuál es el valor de mantener una capacidad cuando su beneficio inmediato parece pequeño frente al coste necesario?

Esta cuestión aparece con frecuencia en empresas de tecnología. Google construyó un verdadero cementerio de innovaciones a lo largo de su historia, con productos y proyectos que fueron lanzados, probados y posteriormente cerrados. Esto no es, por sí mismo, señal de mala gestión. Una organización necesita abandonar iniciativas que no justifican el capital, el talento y la atención que consumen.

Google Glass es un ejemplo interesante. La empresa apostó temprano por una nueva categoría de computación portátil, pero el producto encontró problemas de adopción, precio, privacidad y adecuación al comportamiento del consumidor. La versión dirigida al mercado empresarial continuó durante algunos años más, hasta que Glass Enterprise Edition también fue descontinuado en 2023.

El cierre de Glass como producto no significa que la apuesta tecnológica fuera necesariamente equivocada. Años después, las Ray-Ban Meta mostraron que los consumidores podían adoptar una forma diferente de computación portátil basada en cámara, audio e inteligencia artificial, integrada en un producto ya familiar.

La diferencia es importante. Una iniciativa puede fracasar porque el mercado aún no está preparado, porque el modelo de negocio es inadecuado o porque la tecnología depende de condiciones que todavía no existen. Cerrar el producto puede ser racional. El riesgo está en abandonar también el conocimiento, las competencias y la infraestructura que permitirían volver a intentarlo cuando esas condiciones fueran diferentes.

El mismo razonamiento ayuda a observar la China Ming. No es posible afirmar que la interrupción de las grandes expediciones determinara por sí sola el futuro marítimo chino, ni que China hubiera necesariamente dominado el comercio del océano Índico si hubiera mantenido aquellas expediciones. El punto es que reducir una actividad también puede reducir la capacidad de explorar determinadas oportunidades. Retomar una competencia muchos años después puede ser mucho más caro que mantenerla a escala limitada.

Esto crea un trade-off difícil. Las personas necesitan ser asignadas, la infraestructura necesita mantenerse y la atención gerencial es limitada. Intentar preservar todas las posibilidades sería inviable.

La cuestión arquitectónica, por lo tanto, no es “¿debemos mantener esta iniciativa?”. Es “¿qué dejaremos de poder hacer si cerramos esta iniciativa?” y “¿cuánto costará recuperar esa capacidad después?”.

El retorno actual sigue siendo importante, pero no es el único criterio. También necesitamos considerar el tiempo necesario para reconstruir una competencia y la posibilidad de que, cuando surja la oportunidad, otras organizaciones ya hayan ocupado ese espacio.

No podemos saber qué oportunidades futuras existirán realmente. Pero podemos reconocer cuándo una decisión hace mucho más difícil aprovecharlas.

A veces, no decidir también es una decisión. Y el coste puede aparecer solo cuando surge una oportunidad y descubrimos que ya no estamos preparados para aprovecharla.

## La importancia de la arquitectura de decisiones

Los siete casos muestran diferentes tipos de decisión que pueden comprometer el futuro: error de modelado, exceso de dependencia, pérdida de opcionalidad, coste del tiempo, error de priorización, dependencia de la escala y pérdida de oportunidades. El punto común es que las decisiones no producen solo resultados. Alteran las condiciones en las que se tomarán las próximas decisiones.

Eso es lo que aproxima la estrategia, la gestión de proyectos y la arquitectura de soluciones. Una elección tecnológica crea dependencias. Una inversión compromete recursos. Una expansión crea obligaciones. Una decisión sobre un proveedor puede restringir alternativas futuras. Una desinversión puede eliminar una oportunidad que todavía no sabemos si necesitaremos explorar.

No necesitamos predecir el futuro para tomar buenas decisiones. Necesitamos entender las premisas, dependencias, trade-offs y consecuencias que cada elección crea para las decisiones siguientes.

Muchas de las decisiones analizadas aquí parecían razonables cuando fueron tomadas. El problema es que sus autores no estaban simplemente eligiendo una respuesta para el presente. Estaban definiendo las condiciones de la próxima decisión.

Decidir es comenzar a construir el próximo problema que la organización tendrá que resolver.
