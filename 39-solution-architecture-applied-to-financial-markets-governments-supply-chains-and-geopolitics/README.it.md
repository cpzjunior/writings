# Architettura delle soluzioni applicata ai mercati finanziari, ai governi, alle catene di approvvigionamento e alla geopolitica

_Una prospettiva architetturale su autorità, fiducia, dipendenze, interfacce e modalità di guasto nei sistemi complessi_

**Sintesi:** Propongo di applicare la lente dell'architettura delle soluzioni a sistemi che vanno ben oltre il software, come mercati finanziari, governi, catene di approvvigionamento e relazioni geopolitiche. Osservando componenti, interfacce, dipendenze, capacità, autorità e modalità di guasto, possiamo rendere visibili relazioni che normalmente rimangono nascoste. Questa prospettiva non pretende di spiegare completamente questi sistemi, ma di offrire un modo più preciso di ragionare sulla loro struttura e sul loro comportamento sotto stress. In questo modo, l'architettura delle soluzioni smette di essere soltanto una disciplina tecnica e diventa anche un modo per analizzare e progettare sistemi complessi.

---

Una cosa curiosa è accaduta quando ho finito di scrivere “*[Fondamenti dell'architettura patrimoniale: progettare il patrimonio come un sistema](https://cpzjunior.substack.com/p/fundamentos-da-arquitetura-patrimonial)*“: ho iniziato a chiedermi cosa sarebbe successo se avessi applicato lo stesso principio ad altri problemi della realtà. In quell'articolo, il patrimonio ha smesso di essere trattato semplicemente come un insieme di attività ed è passato a essere osservato come un sistema. Questo ha permesso di vedere componenti, responsabilità, flussi, dipendenze, vincoli e punti di guasto che risultano meno evidenti quando osserviamo soltanto gli elementi singolarmente.

Da quel momento, ho iniziato a rendermi conto che lo stesso esercizio poteva essere fatto in domini molto diversi. Mercati finanziari, governi, catene di approvvigionamento e relazioni geopolitiche hanno qualcosa in comune: sono sistemi composti da parti che devono coordinare qualche tipo di attività, dipendono le une dalle altre e devono gestire i guasti. Più esempi trovavo, più curiosa diventava la ricorrenza.

Quando ho iniziato a cercare di capire perché strutture così diverse sembrassero permettere lo stesso tipo di modellazione, sono arrivato alla Legge di Conway. L'idea che l'architettura di un sistema tenda a riflettere la struttura di comunicazione dell'organizzazione che lo produce è piuttosto conosciuta nella tecnologia. Ma questa osservazione mi ha portato a una provocazione diversa: e se alcuni degli strumenti utilizzati per pensare all'architettura dei sistemi fossero utili anche per pensare a sistemi molto più grandi del software?

La proposta non è spiegare l'economia come un economista, i governi come uno scienziato politico o la geopolitica come uno specialista. Né affermare che una banca sia letteralmente un sistema distribuito, che una federazione sia un sistema gerarchico o che un conflitto possa essere ridotto a un problema logistico. La proposta è più specifica: osservare questi sistemi come farebbe un architetto di soluzioni.

Un architetto lavora costantemente con le astrazioni. Un modello architetturale non deve rappresentare tutta la realtà. Deve preservare le proprietà rilevanti per la domanda a cui stiamo cercando di rispondere. Quando progettiamo un sistema, ignoriamo deliberatamente un'enorme quantità di dettagli per poter ragionare su responsabilità, interfacce, dipendenze, stati, capacità e guasti.

Forse questo stesso modo di pensare è utile al di fuori del software, non per spiegare completamente i sistemi complessi, ma per renderli più trattabili. Cambiando la rappresentazione di un problema, alcune relazioni che erano nascoste diventano visibili. E, quando queste relazioni diventano visibili, possiamo iniziare a porci domande architetturali su di esse.

## Mercati finanziari: un'architettura distribuita della fiducia

Se trattiamo il sistema finanziario come un esercizio di system design, il primo passo è identificare i suoi componenti, i loro stati, le loro interfacce e le dipendenze tra di essi. Non perché le banche siano server o perché il denaro sia semplicemente informazione, ma perché alcune delle proprietà che utilizziamo per progettare sistemi distribuiti compaiono anche nella struttura del mercato finanziario.

Una banca può essere intesa, ai fini di questa modellazione, come un nodo che mantiene stati finanziari ed espone interfacce ai clienti e ad altre istituzioni. Un conto rappresenta uno stato che può essere modificato dalle operazioni. Un trasferimento è un'operazione che deve attraversare diversi componenti fino a produrre modifiche coerenti dello stato. Il regolamento è il meccanismo che trasforma un'obbligazione in un'operazione effettivamente completata.

Questo ci pone già di fronte a un problema classico dei sistemi distribuiti: lo stato non si trova necessariamente in un unico luogo. Un'operazione finanziaria può coinvolgere più di un'istituzione, sistemi diversi e diverse fasi prima del suo completamento. Ogni partecipante possiede soltanto una parte dello stato rilevante per il sistema nel suo complesso, e la coerenza deve essere preservata tra componenti che non condividono necessariamente lo stesso processo, la stessa infrastruttura o la stessa organizzazione.

Per rendere l'esercizio più concreto, possiamo utilizzare il mercato finanziario brasiliano come riferimento. La sua architettura istituzionale possiede componenti e responsabilità differenti. Banche e altri partecipanti eseguono operazioni. Le infrastrutture di mercato permettono a diversi partecipanti di interagire. Su questi livelli esistono meccanismi di regolamentazione, supervisione, regolamento e protezione. La Banca Centrale occupa una posizione centrale in questo disegno, mentre la CVM esercita responsabilità specifiche sul mercato dei valori mobiliari. Il COPOM, a sua volta, agisce su un parametro sistemico, il tasso di interesse di base, modificando le condizioni alle quali diversi componenti operano.

Queste istituzioni non sono equivalenti a componenti software, ma l'analogia permette di identificare una distinzione architetturale importante: non tutti i componenti eseguono il flusso principale. Alcuni elaborano operazioni, altri stabiliscono vincoli, altri osservano il comportamento dei partecipanti e altri modificano parametri che influenzano il sistema nel suo complesso.

Possiamo pensare a questo come a una separazione approssimativa tra data plane e control plane. I partecipanti eseguono le operazioni che movimentano risorse e posizioni, mentre diversi meccanismi istituzionali stabiliscono condizioni, monitorano il comportamento e modificano i parametri entro i quali queste operazioni avvengono. La separazione non è perfetta, ma è utile per comprendere perché i sistemi complessi abbiano spesso bisogno di distribuire le responsabilità tra piani differenti.

Emerge quindi una proprietà importante di qualsiasi architettura distribuita: l'osservabilità. Non basta possedere componenti indipendenti; è necessario poter identificare quando uno di essi si sta avvicinando a una condizione di guasto. Nei sistemi finanziari, le informazioni su capitale, liquidità, esposizioni e altre condizioni dei partecipanti permettono ai meccanismi di supervisione di identificare determinati rischi prima che si trasformino necessariamente in un guasto sistemico. Sotto questa lente, anche la supervisione può essere osservata come una capacità architetturale: conoscere lo stato dei componenti per agire prima che il blast radius di un guasto diventi maggiore di quanto il sistema sia in grado di assorbire.

Il problema successivo è la tolleranza ai guasti. In qualsiasi sistema distribuito, dobbiamo assumere che i componenti possano guastarsi. Anche una banca può fallire. La questione architetturale non è come garantire che nessuna banca abbia mai problemi, ma come impedire che il guasto di un partecipante si trasformi automaticamente nel guasto dell'intero sistema.

L'esistenza di più banche crea già una forma di distribuzione, ma distribuzione non significa necessariamente resilienza. Se tutti i partecipanti dipendono dalla stessa infrastruttura, dalla stessa controparte critica o dalla stessa fonte di liquidità, l'architettura può comunque contenere un punto di concentrazione.

Per questo dobbiamo osservare il grafo delle dipendenze, e non soltanto il numero di componenti. Una banca può smettere di operare senza che tutte le altre debbano smettere di operare. Questa proprietà dipende dall'esistenza di meccanismi capaci di limitare il blast radius di un guasto.

Il FGC può essere osservato, nell'ambito e nei limiti stabiliti, come un meccanismo di contenimento. Non impedisce il guasto dell'istituzione, ma riduce determinati effetti di tale guasto sui depositanti protetti. La logica architetturale è simile a quella di un sistema che isola un guasto in un componente per evitare che tutti i consumatori dipendenti da quel componente debbano sperimentare lo stesso guasto.

Esiste un'altra strategia possibile: sostituire il componente. Quando un'istituzione in difficoltà viene acquisita da un'altra, l'istituzione originaria può smettere di esistere come componente indipendente senza che tutte le sue funzioni debbano scomparire. Operazioni, clienti, attività, passività o altre relazioni possono essere assorbite o trasferite, a seconda della struttura dell'operazione e del processo applicabile.

Sotto una lente di system design, questo si avvicina a un failover mediante sostituzione del componente. L'obiettivo non è necessariamente recuperare il componente che ha fallito, ma preservare le funzioni che il sistema deve continuare a offrire.

L'architettura può anche distribuire determinate esposizioni tra i componenti. Quando diverse istituzioni mantengono posizioni e attività correlate tra loro, determinate esposizioni smettono di essere concentrate in un unico partecipante. Questo può ridurre una dipendenza individuale, anche se crea nuove relazioni tra i componenti.

Questa distinzione è importante. Distribuire il rischio non significa eliminarlo. Significa modificarne la topologia. È possibile ridurre la dipendenza da un nodo e, contemporaneamente, aumentare l'interdipendenza tra diversi nodi. È possibile avere decine di istituzioni e dipendere comunque da un'infrastruttura centrale. È possibile possedere ridondanza nominale senza possedere una capacità sufficiente ad assorbire un guasto.

Questo è lo stesso problema che incontriamo nelle architetture software quando confondiamo il numero di server con la resilienza. La domanda non è quanti componenti esistano, ma quali componenti siano necessari per mantenere determinato flusso, quali dipendenze condividano e cosa accada quando ciascuno di essi smette di funzionare.

Il sistema finanziario presenta inoltre una proprietà che rende particolarmente rilevante la propagazione dei guasti: i componenti hanno obblighi reciproci. L'attivo di un'istituzione può essere il passivo di un'altra. Un'obbligazione non adempiuta può modificare lo stato di un altro partecipante, che a sua volta può smettere di adempiere a una propria obbligazione. Il guasto smette di essere un evento localizzato e inizia a percorrere il grafo.

Abbiamo qui un altro concetto noto nel system design: failure propagation. Il problema non consiste soltanto nel rilevare che un componente ha fallito, ma nel comprendere quanti altri componenti dipendano da esso, quali stati saranno interessati e fin dove il guasto possa propagarsi.

Per questo, l'architettura deve controllare non soltanto il guasto dei componenti, ma anche il loro blast radius. Supervisione, requisiti prudenziali, meccanismi di risoluzione, strutture di protezione e infrastrutture di regolamento possono essere osservati, sotto questa lente, come parti di un'architettura di fault containment.

Questo cambia anche il modo di vedere la regolamentazione. Nel software, un'interfaccia definisce più della forma della comunicazione. Stabilisce un contratto. Chi consuma un servizio conosce determinate garanzie e restrizioni senza dover conoscere la sua implementazione interna.

Nel sistema finanziario, regole e requisiti svolgono una funzione parzialmente analoga. Definiscono le condizioni alle quali le istituzioni possono operare e interagire. L'architettura non è formata soltanto dai componenti, ma anche dai contratti che determinano come questi componenti possono relazionarsi.

La fiducia emerge da questa architettura. Il cliente osserva un'interfaccia relativamente semplice: il proprio saldo, un trasferimento, un ordine, un pagamento. Non osserva tutte le istituzioni, infrastrutture e meccanismi coinvolti nell'operazione. Tuttavia, si aspetta che lo stato rappresentato da quell'interfaccia continui a essere valido.

Un saldo, in questo senso, è più di un numero visualizzato sullo schermo. È una rappresentazione di stato che dipende da una catena di componenti affinché continui ad avere validità operativa.

È per questo che una crisi finanziaria non deve necessariamente iniziare con un'indisponibilità tecnica. Il sistema può continuare a essere operativo e, tuttavia, subire un deterioramento della sua proprietà più importante se i partecipanti smettono di fidarsi degli stati che rappresenta o delle obbligazioni che gli altri componenti dovrebbero adempiere.

A questo punto, la fiducia si comporta come un requisito non funzionale. Non basta che il sistema elabori transazioni. Deve preservare le condizioni che fanno sì che i partecipanti credano che tali transazioni continueranno a essere riconosciute e regolate.

La cosa interessante è che questa proprietà non è localizzata in un singolo componente. Emerge dall'intera architettura: dai partecipanti, dalle infrastrutture, dalle regole, dalla supervisione, dai meccanismi di protezione, dalla capacità di sostituire componenti e dalla possibilità di contenere i guasti prima che attraversino l'intera rete.

Da questa prospettiva, il mercato finanziario può essere inteso come un'architettura distribuita nella quale la risorsa più importante non è soltanto il denaro che circola tra i componenti, ma la fiducia che gli stati, le obbligazioni e le interfacce del sistema continueranno a funzionare anche quando alcuni dei suoi componenti falliranno.

Ed è questa una delle caratteristiche più interessanti dei sistemi complessi: la loro resilienza non risiede necessariamente nell'assenza di guasti, ma nell'architettura che determina ciò che accade dopo che si verificano.

## Governi: l'autorità come architettura

Un governo può essere osservato, da una prospettiva di system design, come un sistema di distribuzione dell'autorità.

La domanda architetturale non è semplicemente chi governa, ma dove si trova l'autorità per ciascun tipo di decisione. Chi può modificare una determinata regola? Chi esegue questa decisione? Chi controlla? Chi può contestarla? In quali circostanze una decisione deve essere sottoposta a un altro componente?

Queste domande definiscono gli authority boundaries. Un'architettura altamente centralizzata concentra gran parte delle decisioni in un nucleo. Un'architettura decentralizzata distribuisce queste decisioni tra componenti differenti. Una federazione offre un caso particolarmente interessante: gli stati conservano determinate competenze mentre ne delegano altre a una struttura federale.

Il problema è simile a quello che incontriamo nella decomposizione dei sistemi software. Dobbiamo partizionare le responsabilità tra componenti che possiedono un'autonomia parziale e stabilire interfacce per coordinare ciò che non può essere deciso isolatamente.

Una volta definito questo partizionamento, emerge il problema della comunicazione. Se una decisione dipende da più componenti, dobbiamo determinare chi può richiedere una modifica, chi deve approvarla, chi eseguirà la decisione e chi potrà contestarla. Il disegno delle competenze crea quindi un grafo di dipendenze.

In una federazione, determinate decisioni possono rimanere a livello statale mentre altre vengono attribuite al governo federale. Il confine tra queste competenze funziona come un boundary architetturale. Quanto più numerose sono le responsabilità concentrate a livello federale, tanto maggiore è la centralizzazione del sistema. Quanto più numerose sono le responsabilità che rimangono nei componenti locali, tanto maggiore è la loro autonomia.

Questo produce un trade-off simile a quello che incontriamo nella decomposizione dei sistemi software. Centralizzare facilita il coordinamento e può ridurre le incoerenze tra i componenti, ma concentra l'autorità e aumenta il carico sul nucleo decisionale. Distribuire permette maggiore autonomia e parallelismo, ma aumenta la necessità di coordinamento e crea più interfacce tra i componenti.

Questa dimensione del carico è particolarmente importante. Un sistema può essere centralizzato mentre il volume delle decisioni rimane ridotto. Quando la quantità, la velocità o la diversità delle decisioni cresce, la concentrazione può trasformare il centro in un collo di bottiglia. La decentralizzazione, in questo senso, non è soltanto una scelta politica: può essere osservata come una strategia di distribuzione della capacità decisionale.

L'architettura istituzionale deve inoltre definire cosa accade quando due componenti non sono d'accordo. In un sistema distribuito, componenti indipendenti possono raggiungere stati o decisioni incompatibili e hanno bisogno di meccanismi per risolvere questi conflitti. In un governo, i conflitti di competenza e interpretazione richiedono meccanismi equivalenti di risoluzione. Tribunali, legislativi, esecutivi e diversi livelli di governo possono essere osservati, sotto questa lente, come componenti con responsabilità distinte all'interno di un protocollo istituzionale più ampio.

Il sistema elettorale introduce un secondo livello architetturale: l'aggregazione. Un'elezione deve trasformare un enorme insieme di preferenze individuali in una decisione collettiva riconosciuta dal sistema. Dal punto di vista del system design, questo può essere osservato come un problema di aggregazione di input distribuiti.

Ogni elettore è una fonte di input. Distretti, collegi elettorali, partiti o altre unità intermedie possono funzionare come diverse forme di aggregazione. Il risultato finale dipende non soltanto dagli input, ma dalla topologia attraverso la quale questi input vengono raggruppati e trasformati.

È per questo che sistemi elettorali differenti possono produrre risultati differenti a partire da insiemi simili di preferenze. In un sistema di rappresentanza distrettuale, per esempio, i voti vengono prima aggregati spazialmente per produrre rappresentanti di determinate unità. In altri sistemi, l'aggregazione avviene in modo diverso. La preferenza individuale percorre una sequenza differente di componenti prima di trasformarsi in rappresentanza.

Questa è una proprietà fondamentale dei sistemi di aggregazione: il risultato dipende non soltanto dai dati di input e dalla regola decisionale, ma anche da come gli input vengono partizionati prima di essere aggregati.

Questo introduce anche una questione di rappresentanza. Un sistema elettorale non si limita ad aggregare input; definisce quanto ciascun gruppo di input pesi nella formazione dello stato finale. Modificare l'unità di aggregazione, il metodo di conversione dei voti in rappresentanza o il numero di livelli intermedi modifica la topologia del sistema e, di conseguenza, le sue proprietà.

Lo stesso ragionamento aiuta a osservare diverse architetture di governo. Un governo centralizzato possiede una topologia diversa da una federazione. Un sistema parlamentare possiede una relazione diversa tra esecutivo e legislativo rispetto a un sistema presidenziale. Un sistema elettorale distrettuale possiede una topologia di aggregazione diversa da un sistema proporzionale.

Non è necessario affermare che un modello sia superiore a un altro per osservare la conseguenza architetturale. Ogni topologia crea percorsi differenti per la decisione, differenti punti di concentrazione, differenti dipendenze e differenti modalità di guasto. Ancora una volta, non esiste un'architettura priva di trade-off. Esistono invece forme differenti di distribuire autorità, comunicazione e responsabilità.

In questo senso, forse la caratteristica più interessante di un governo non è la sua ideologia o la sua struttura giuridica isolatamente, ma la sua architettura decisionale: chi può decidere, chi deve partecipare, chi può bloccare, chi esegue, chi supervisiona e come il sistema continua a funzionare quando questi componenti non sono d'accordo, falliscono o devono elaborare più decisioni di quante riescano ad assorbire.

La topologia istituzionale, così come la topologia di un sistema distribuito, determina non soltanto dove si trovano i componenti, ma come una decisione attraversa il sistema. E, quando modifichiamo questa topologia, modifichiamo anche le proprietà del sistema che ne emerge.

## Catene di approvvigionamento: una rete distribuita di dipendenze

Una catena di approvvigionamento è un esempio naturale di sistema distribuito. Aziende diverse producono componenti differenti, spesso in luoghi distinti, utilizzando risorse e infrastrutture di altri partecipanti. Non esiste necessariamente un singolo componente responsabile dell'intero processo e l'operazione dipende dal coordinamento tra organizzazioni che possiedono obiettivi, capacità e vincoli propri.

Per questo, una rappresentazione lineare di una catena di approvvigionamento può essere fuorviante. La realtà è più vicina a un grafo di dipendenze, nel quale i fornitori hanno fornitori, le rotte convergono verso hub, i prodotti passano attraverso diversi centri di distribuzione e componenti differenti possono dipendere dalla stessa infrastruttura logistica.

Questa struttura produce una proprietà nota nei sistemi distribuiti: le dipendenze indirette possono essere importanti quanto quelle dirette.

Un'azienda può non dipendere direttamente da un determinato porto, stretto o ferrovia. Può dipendere da un fornitore che dipende da una fabbrica che dipende da quell'infrastruttura. Quanto maggiore è la profondità di queste dipendenze, tanto più difficile diventa identificare i punti la cui indisponibilità può influenzare il sistema.

Questo rende particolarmente importante distinguere la ridondanza nominale dalla ridondanza effettiva. Consideriamo un collo di bottiglia logistico come lo Stretto di Hormuz. Non deve essere l'unico percorso possibile per essere architetturalmente critico. Possono esistere altre rotte, ma, se non possiedono capacità sufficiente ad assorbire il flusso che normalmente attraversa il collo di bottiglia, la rete possiede ridondanza nel disegno, ma non necessariamente ridondanza operativa.

Questa distinzione compare costantemente nel system design. Avere due server non significa necessariamente possedere alta disponibilità. Se il secondo server non ha la capacità di assumere il carico del primo, abbiamo ridondanza di componenti, ma non necessariamente ridondanza di capacità.

Lo stesso vale per la logistica. La domanda non è più soltanto “esiste un'altra rotta?”, ma “questa rotta è in grado di assorbire il guasto entro i requisiti di capacità, tempo e costo che il sistema deve preservare?”.

Una rotta alternativa può esistere e tuttavia non essere un vero meccanismo di failover. Può sostenere soltanto una frazione del volume, aumentare significativamente la latenza del flusso o dipendere da altri componenti che sono anch'essi vicini alla loro capacità massima. In alcuni casi, il percorso alternativo esiste, ma il suo tempo di attivazione è così lungo che l'interruzione iniziale produce già conseguenze rilevanti.

Questo mostra perché non ogni punto critico sia un single point of failure in senso stretto. Un componente può possedere alternative e continuare a essere strutturalmente critico perché la sua rimozione aumenta significativamente il costo, il tempo o la complessità dell'operazione.

In architettura, questo è importante perché i sistemi non possiedono soltanto stati di funzionamento e di guasto. Esiste tutta una gamma intermedia di degradazione.

Una rete può continuare a funzionare con una rotta alternativa, ma operare con capacità inferiore. Può servire tutti i clienti, ma con maggiore latenza. Può preservare il flusso, ma a un costo che rende l'operazione economicamente insostenibile. La resilienza, quindi, non dovrebbe essere valutata soltanto con la domanda “il sistema continua a funzionare?”, ma anche con “a quali condizioni continua a funzionare?”.

Quando il guasto di un componente sposta il carico sugli altri componenti, emerge inoltre un altro fenomeno noto nei sistemi distribuiti: cascading failure. Il guasto iniziale modifica le condizioni operative del resto della rete e può innescare nuovi guasti.

Immaginiamo una catena nella quale un fornitore perde capacità. La domanda viene trasferita ai fornitori alternativi. Questi fornitori iniziano a operare vicino al limite. Una seconda interruzione, che normalmente sarebbe assorbibile, passa a provocare una nuova rottura. La rete non è fallita perché esisteva un singolo componente indispensabile, ma perché la capacità residua dei componenti rimanenti non era sufficiente ad assorbire la perturbazione.

Questa è una differenza importante tra ridondanza e resilienza. La ridondanza descrive l'esistenza di alternative. La resilienza dipende dalla capacità di queste alternative di assumere la funzione, entro il tempo e le condizioni richieste dal sistema.

La stessa logica vale per gli hub. Un centro di distribuzione può non essere un single point of failure, ma può concentrare un volume tale che la sua indisponibilità obblighi il resto della rete a operare molto al di sopra della capacità pianificata. Il componente alternativo esiste, ma il sistema non è stato dimensionato per la distribuzione del carico che emerge durante il guasto.

È a questo punto che la capacità diventa una proprietà architetturale importante quanto la connettività. Un grafo può possedere molteplici percorsi e continuare a essere fragile. È sufficiente che i percorsi alternativi condividano risorse, abbiano capacità insufficiente o dipendano da componenti che falliscono simultaneamente.

Questo introduce anche il concetto di dipendenza condivisa. Due fornitori possono sembrare indipendenti perché appartengono ad aziende diverse, ma dipendere dalla stessa regione, dallo stesso porto, dalla stessa materia prima, dalla stessa fonte energetica o dalla stessa infrastruttura logistica. La diversità organizzativa non garantisce diversità architetturale.

Lo stesso problema appare nel software quando due availability zone differenti dipendono dallo stesso componente esterno. Nella documentazione esistono due percorsi. Nel comportamento reale del sistema esiste un'unica dependency.

L'architettura della catena di approvvigionamento determina quindi molto più del normale percorso del prodotto. Determina la capacità di degradazione, i percorsi alternativi, i colli di bottiglia, la concentrazione delle dipendenze, il tempo di recupero e la velocità con cui un guasto può propagarsi.

Per questo una catena di approvvigionamento può sembrare altamente distribuita e possedere comunque pochi punti la cui interruzione produce effetti sproporzionati.

La topologia conta, ma la topologia da sola non basta. È necessario osservare capacità, dipendenze condivise, tempo di recupero e comportamento sotto guasto.

In ultima analisi, una catena di approvvigionamento resiliente non è quella in cui tutti i componenti possiedono sostituti. È quella in cui l'architettura possiede percorsi alternativi capaci di assorbire perturbazioni, entro i requisiti di capacità e tempo, senza trasformare un guasto localizzato in un'interruzione sistemica.

## Geopolitica: comando, capacità e dipendenze

Nella geopolitica, la stessa lente può essere ulteriormente ampliata. I paesi non sono componenti isolati, ma insiemi di capacità connessi a reti di dipendenza. Energia, industria, tecnologia, materie prime, infrastrutture, trasporti, mercati, alleanze e strutture di difesa formano relazioni che attraversano le frontiere.

Il sistema inizia ad assomigliare meno a una mappa e più a un grafo. Questo cambiamento di rappresentazione è importante perché la dimensione di un componente smette di essere sufficiente a determinarne l'importanza. Un paese può possedere un'enorme capacità economica e, tuttavia, dipendere da una determinata risorsa, tecnologia o rotta controllata da un componente molto più piccolo. Allo stesso modo, un'infrastruttura relativamente piccola può acquisire un'importanza sproporzionata quando molti flussi dipendono da essa.

È la stessa logica dei chokepoint osservati nelle catene di approvvigionamento, ma ora applicata a una rete molto più ampia. Il valore architetturale di un componente può risiedere meno in ciò che produce e più nella quantità di percorsi che dipendono da esso.

L'energia, per esempio, può essere modellata come una dipendenza trasversale. L'industria dipende dall'energia, i trasporti dipendono dall'energia, le infrastrutture dipendono dall'energia e, di conseguenza, diverse capacità possono condividere la stessa dependency. Quando ciò accade, un'interruzione localizzata può produrre effetti su componenti che, a prima vista, sembrano non avere una relazione diretta.

L'architettura della difesa introduce un altro aspetto del problema: il control plane. Una struttura di comando può essere rappresentata, in modo semplificato, come una gerarchia che trasforma obiettivi strategici in decisioni operative e, successivamente, in esecuzione. Il problema architetturale consiste nel determinare quali decisioni debbano rimanere al centro e quali possano essere delegate a componenti più vicini all'esecuzione.

Quanto più numerose sono le responsabilità che rimangono concentrate nel control plane, tanto maggiore tende a essere il controllo centrale. Ma aumenta anche il volume di informazioni che deve arrivare al centro e la quantità di decisioni che devono attraversare lo stesso percorso. Questo produce un problema di scala e latenza.

Una struttura che deve coordinare attività in ambienti multipli può delegare determinate responsabilità a strutture regionali. Questi hub passano a operare all'interno di un insieme definito di limiti, mentre il centro conserva capacità di coordinamento, supervisione e definizione degli obiettivi.

Architetturalmente, questo riduce la distanza tra decisione ed esecuzione e diminuisce parte del coordination overhead al centro. Ma esiste un trade-off inevitabile: delegare significa rinunciare a una parte del controllo centrale.

La centralizzazione favorisce coerenza e controllo, ma può aumentare latenza e concentrazione delle decisioni. La decentralizzazione favorisce autonomia e capacità di risposta, ma aumenta la necessità di contratti, coordinamento e meccanismi di supervisione.

Questa tensione appare in modo particolarmente chiaro nelle potenze con impegni e interessi distribuiti in diverse regioni. Quanto maggiore è il numero di ambienti che devono essere coordinati da un unico centro, tanto maggiore tende a essere la quantità di informazioni, decisioni e risorse che devono attraversare lo stesso control plane.

Una possibile risposta architetturale è distribuire parte di queste responsabilità tra hub regionali, preservando al centro ciò che richiede coordinamento globale. Questa architettura può ridurre la latenza e rendere il coordinamento più scalabile, ma crea un nuovo problema: quanto maggiore è l'autonomia concessa agli hub, tanto maggiore è la distanza tra la decisione locale e il controllo centrale.

Il problema architetturale, quindi, non consiste semplicemente nello scegliere tra centralizzazione e decentralizzazione. Consiste nel determinare quali responsabilità debbano rimanere centralizzate, quali possano essere delegate e quali interfacce debbano esistere tra questi livelli.

Su scala geopolitica, questa discussione sul comando si collega direttamente alla discussione sulle dipendenze. Un paese può cercare di ridurre la propria esposizione a un determinato componente creando fornitori alternativi, sviluppando capacità domestica o stabilendo nuove rotte e alleanze. In termini architetturali, questo significa modificare il grafo delle dipendenze.

Ma anche la capacità alternativa deve essere dimensionata. Una seconda fonte che riesce a soddisfare soltanto una piccola parte della domanda non rappresenta lo stesso livello di resilienza di una fonte capace di assumere integralmente il flusso. Allo stesso modo, una rotta alternativa che richiede mesi per essere attivata può avere poco valore di fronte a un'interruzione che richiede una risposta immediata.

La ridondanza ha un costo. Creare fornitori alternativi richiede investimenti. Costruire capacità domestica può aumentare l'autonomia, ma ridurre l'efficienza. Mantenere rotte alternative significa accettare capacità inutilizzata in determinati momenti. Sviluppare molteplici fonti di tecnologia o energia può significare duplicare infrastrutture che, in condizioni normali, sarebbero superflue. L'architettura non elimina questi trade-off. Permette di renderli espliciti.

Questo aiuta anche a spiegare perché efficienza e resilienza spesso puntino in direzioni diverse. Un'architettura ottimizzata per il percorso felice tende a eliminare capacità ridondante, concentrare le risorse e ridurre i costi. Un'architettura ottimizzata per la tolleranza ai guasti deve accettare un certo grado di ridondanza, capacità inutilizzata e percorsi alternativi.

Esiste inoltre una conseguenza importante: le dipendenze non devono essere simmetriche. Due paesi possono avere una relazione commerciale intensa senza avere lo stesso grado di dipendenza. Un componente può essere facilmente sostituibile per una parte e praticamente indispensabile per l'altra. Il grafo possiede una connessione in entrambe le direzioni, ma i suoi pesi sono differenti.

Questo modifica l'importanza architetturale di ogni relazione. Non basta chiedere se esiste una dipendenza. Dobbiamo chiederci quanto sia sostituibile, quale capacità alternativa possieda, quanto tempo occorra per attivare tale alternativa e quale sia il costo della sua rimozione.

Lo stesso ragionamento vale per alleanze e strutture di difesa. Una relazione può ridurre la dipendenza da un componente e, contemporaneamente, creare una nuova dipendenza da un altro. L'architettura raramente elimina le dipendenze; normalmente le redistribuisce.

Per questo anche un sistema geopolitico deve essere analizzato in base al comportamento sotto stress. Il percorso felice è quello in cui le rotte rimangono aperte, i fornitori continuano a operare, l'energia è disponibile, le alleanze rimangono stabili e le strutture di comando riescono a coordinare le proprie capacità.

Il problema architetturale inizia quando una di queste premesse smette di essere vera. A quel punto ricompaiono gli stessi concetti che utilizziamo per progettare sistemi distribuiti: blast radius, capacità residua, dipendenze condivise, failover, latenza decisionale, concentrazione e cascading failure. La differenza sta nella scala, nei tempi coinvolti e nel fatto che gli stessi componenti possono modificare deliberatamente la propria architettura.

Un'architettura geopolitica resiliente, quindi, non è quella che elimina le proprie dipendenze o concentra tutte le capacità in un unico centro. È quella il cui grafo possiede dipendenze critiche conosciute, alternative con capacità sufficiente, meccanismi di sostituzione e una distribuzione dell'autorità compatibile con la velocità e la scala delle decisioni che deve prendere.

La resilienza strategica, in questo senso, è meno una proprietà di ciascun paese isolatamente che una proprietà dell'architettura delle relazioni tra essi.

## La stessa lente in altri sistemi

L'utilità di questo approccio emerge anche al di fuori dei quattro domini precedenti. Quando riduciamo progressivamente la scala, le stesse proprietà architetturali continuano ad apparire, sebbene cambino i componenti, le interfacce e gli obiettivi.

I conflitti possono essere osservati come sistemi nei quali la capacità operativa dipende da una rete di capacità logistiche e industriali. Il territorio è soltanto una delle dimensioni del problema. Carburante, equipaggiamenti, manutenzione, trasporto, comunicazione, intelligence e capacità industriale sostengono la capacità operativa. Sotto questa lente, degradare una capacità non significa necessariamente attaccare direttamente il componente che esegue la funzione finale. Può essere più rilevante colpire le sue dipendenze. Il conflitto diventa quindi anche una disputa tra architetture di capacità, nella quale ciascuna parte cerca di preservare i propri flussi e degradare quelli dell'avversario.

Internet presenta un problema diverso: l'interoperabilità tra componenti autonomi. Reti distinte riescono a operare come un'infrastruttura globale perché condividono protocolli e contratti di comunicazione. L'autonomia di ciascun componente non impedisce la sua integrazione perché l'interfaccia è sufficientemente stabile da permettere la coesistenza di implementazioni differenti. Il sistema non dipende da un'unica implementazione, ma da un insieme comune di interfacce.

Le telecomunicazioni aggiungono una distinzione importante tra ridondanza logica e ridondanza fisica. Una rete può possedere molteplici percorsi e continuare a dipendere da una quantità limitata di cavi, stazioni, torri, data center o punti di interconnessione. Due percorsi apparentemente indipendenti possono condividere la stessa infrastruttura fisica. La topologia logica, quindi, può suggerire una resilienza che la topologia fisica non possiede.

Le reti elettriche rendono particolarmente visibile il problema della propagazione dei guasti. La perdita di un componente può redistribuire il carico sugli altri, modificandone le condizioni operative e creando nuovi guasti. La questione architetturale non è più soltanto se esista un percorso alternativo, ma se i componenti rimanenti possiedano capacità sufficiente per assorbire la perturbazione.

Acqua e servizi igienico-sanitari introducono un'altra proprietà: la continuità del servizio. Serbatoi, impianti di trattamento, pompaggio, distribuzione e raccolta formano una catena nella quale la capacità di una fase condiziona le altre. Un'alternativa è effettivamente ridondante soltanto se riesce a sostenere il servizio per il tempo necessario. La capacità, in questo caso, non è una caratteristica statica del componente, ma una proprietà dell'architettura nei diversi stati operativi.

Aeroporti e ospedali mostrano un problema simile nei sistemi in cui diverse organizzazioni o dipartimenti condividono lo stesso flusso. Compagnie aeree, controllo del traffico, sicurezza, immigrazione, rifornimento e manutenzione devono coordinare le operazioni in un aeroporto. In un ospedale, emergenza, diagnosi, laboratorio, farmacia, chirurgia e ricovero possiedono responsabilità distinte, ma lo stato necessario per assistere un paziente attraversa diversi di questi boundaries. In entrambi i casi, un componente può rimanere disponibile mentre limita la capacità dell'intero sistema.

I sistemi di trasporto urbano aggiungono una dimensione temporale all'analisi. Una rete non deve subire un grande guasto per perdere resilienza. L'infrastruttura invecchia, alcuni tratti vengono chiusi, le stazioni perdono capacità e il traffico viene redistribuito sui percorsi rimanenti. Una rotta che prima funzionava come ridondanza può gradualmente trasformarsi nel percorso principale per una quota crescente della domanda. La rete continua a funzionare, ma con minore capacità residua e maggiore sensibilità a nuove perturbazioni. Allo stesso tempo, la sua topologia può cambiare nella direzione opposta: nuove linee, stazioni, terminal e strade possono essere costruiti, creando nuovi percorsi e ridistribuendo la capacità, mentre le aziende possono fallire, i fornitori possono cessare le operazioni o le infrastrutture possono essere permanentemente disattivate. Il sistema, quindi, non opera soltanto su una topologia, ma modifica anche la propria topologia nel tempo, rendendo la resilienza una proprietà che può essere costruita, degradata o ricostruita man mano che i componenti entrano ed escono dalla rete.

Questi esempi sono troppo diversi per essere ridotti a un'unica spiegazione. Ciò che condividono è un'altra cosa: le stesse primitive architetturali continuano a essere utili per formulare domande. Dove sono i componenti? Quali sono le loro interfacce? Quali dipendenze sono condivise? Dove si trova la capacità? Quali componenti concentrano funzioni critiche? Cosa può essere sostituito? Cosa può essere delegato? Come degrada il sistema? E fin dove può propagarsi un guasto?

È proprio questa ricorrenza a rendere interessante la lente. Quando concetti come dipendenza, ridondanza, capacità residua, concentrazione, interoperabilità e failure propagation compaiono in sistemi così diversi, l'architettura smette di sembrare soltanto una tecnica per costruire software. Diventa un linguaggio per rappresentare sistemi complessi.

Non perché questi sistemi siano software, ma perché tutti richiedono un certo grado di composizione: dividere le responsabilità, stabilire interfacce, distribuire l'autorità, gestire le dipendenze, dimensionare la capacità e decidere cosa debba accadere quando una parte del sistema inevitabilmente fallisce.

## Ciò che l'architettura rende visibile

Dopo aver attraversato sistemi così diversi, alcune domande continuano a comparire: chi decide, chi è responsabile di una determinata capacità, chi dipende da chi, dove sono i colli di bottiglia, quanto è concentrato in un singolo componente, quali interfacce permettono il coordinamento e cosa accade quando una dipendenza fallisce?

Queste domande non spiegano banche, governi, catene di approvvigionamento o geopolitica. Fanno qualcosa di più specifico: rendono determinate proprietà di questi sistemi più facili da vedere.

Questo è il ruolo dell'astrazione architetturale. Così come nel system design, non abbiamo bisogno di rappresentare tutta la realtà per ragionare su di essa. Dobbiamo preservare le relazioni rilevanti per il problema che stiamo cercando di comprendere: responsabilità, boundaries, interfacce, dipendenze, capacità, autorità, ridondanza e guasti.

L'analogia, quindi, non pretende di trasformare i paesi in server o i mercati in sistemi distribuiti. È utile proprio perché semplifica senza pretendere di spiegare tutto. Un economista può vedere incentivi dove un architetto vede dipendenze. Uno scienziato politico può vedere istituzioni dove un architetto vede distribuzione dell'autorità. Uno specialista di logistica può vedere flussi dove un architetto vede capacità e colli di bottiglia. Sono prospettive diverse sullo stesso sistema, ciascuna delle quali preserva proprietà rilevanti per domande differenti.

La Legge di Conway aiuta a capire perché questa lente possa essere applicata a sistemi così diversi. Le strutture di autorità, comunicazione e responsabilità non scompaiono quando usciamo dal software. Trovano modi di manifestarsi nei sistemi costruiti e gestiti dalle organizzazioni.

Forse questa è la provocazione più interessante. Molti dei problemi che incontriamo quando progettiamo sistemi software ricompaiono, su scale completamente diverse, quando cerchiamo di organizzare persone, istituzioni, infrastrutture e capacità. Dividere le responsabilità, stabilire interfacce, distribuire l'autorità, gestire le dipendenze, creare ridondanza e limitare l'impatto dei guasti sono problemi di composizione prima ancora di essere problemi di tecnologia.

L'architettura non spiega completamente questi sistemi. Offre qualcosa di diverso: un modo per formularli. E forse è proprio questo il valore di una buona astrazione. Non riprodurre la complessità che cerchiamo di comprendere, ma ridurla abbastanza affinché la sua struttura, i suoi trade-off e i suoi punti di guasto diventino visibili. A volte, rendere un problema complesso sufficientemente semplice da poterlo vedere è il primo passo per iniziare a risolverlo.
