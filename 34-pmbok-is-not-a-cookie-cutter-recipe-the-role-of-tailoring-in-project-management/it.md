# Il PMBOK non è una ricetta: il ruolo del tailoring nella gestione dei progetti

_Così come l’architettura software è una risposta a requisiti e vincoli, anche la gestione deve essere progettata in funzione del contesto._

**Sintesi:** Sostengo che il PMBOK non debba essere trattato come una ricetta, ma come un repertorio di pratiche che deve essere adattato al contesto di ciascun progetto. Così come nell’architettura software, prima dobbiamo comprendere requisiti, vincoli, rischi e trade-off per poi definire la soluzione gestionale adeguata. Il tailoring non significa semplicemente fare meno, ma dimensionare consapevolmente la governance necessaria, evitando sia la burocrazia sia controlli insufficienti. La maturità, quindi, risiede meno nel seguire processi e più nel saper giustificare le scelte ed evolverle man mano che il problema cambia.

---

Recentemente, durante una conversazione con un’amica che lavora come Product Manager, è emerso quasi per caso un commento che ha attirato la mia attenzione. Mi ha raccontato che l’azienda in cui lavora non utilizza il PMBOK perché considera l’approccio troppo rigido per la realtà dell’organizzazione.

La percezione non mi sembra strana. Nel settore tecnologico, vedo accadere qualcosa di simile con frequenza nelle discussioni sull’architettura delle soluzioni. Una determinata architettura viene presentata come best practice, viene poi riprodotta in altri contesti e, quando non si adatta, la conclusione è che fosse l’architettura stessa a essere inadeguata. Molte volte, il problema sta nello scegliere la soluzione prima di comprendere il problema che deve risolvere. Nel system design, sappiamo che non ha senso iniziare dall’architettura. Prima comprendiamo il problema, i suoi requisiti, i vincoli e i trade-off. Solo allora decidiamo come verrà costruito il sistema.

Quando ho sentito quel commento sul PMBOK, ho fatto la stessa associazione. Forse una parte della resistenza al framework deriva dal trattarlo come un’architettura gestionale preconfezionata, qualcosa che dovrebbe essere applicato in modo uniforme affinché un’organizzazione possa dire che “fa project management”. Se questo è il punto di partenza, è facile trasformare la conoscenza in procedura, la procedura in obbligo e l’obbligo in burocrazia.

Il problema sta proprio in questa interpretazione. Il PMBOK non deve essere necessariamente inteso come una metodologia pronta, così come un insieme di pattern architetturali non costituisce, da solo, l’architettura di un’applicazione. Offre conoscenze, pratiche e concetti che possono essere utilizzati per costruire approcci di gestione adeguati a situazioni diverse. La questione smette di essere quanto del PMBOK un’organizzazione utilizza e diventa perché determinate pratiche sono state scelte, quale problema risolvono e quale livello di formalità è necessario.

Forse è utile pensarci come a una sorta di management design. Non come una disciplina formale o un nuovo framework, ma come una lente per guardare alla gestione con la stessa logica che utilizziamo quando progettiamo sistemi: comprendere il problema prima di scegliere i componenti, esplicitare i vincoli, valutare i trade-off ed evitare sia la complessità non necessaria sia soluzioni insufficienti.

## Il problema inizia prima della metodologia

Quando parliamo di project management, spesso mettiamo sullo stesso piano cose che svolgono ruoli diversi: il corpo di conoscenze sul project management, l’approccio scelto per condurre un progetto e la metodologia utilizzata dall’organizzazione per rendere operativo tale approccio. Confondere questi livelli facilita l’idea che, per applicare determinate conoscenze, sia necessario riprodurre integralmente un processo. Ma un’organizzazione può utilizzare pratiche di gestione senza adottare una metodologia formale, così come può avere una metodologia aziendale e adattarne comunque l’applicazione a ciascun progetto.

Questa differenza diventa evidente quando osserviamo la scala e la natura del lavoro. Un piccolo team può gestire rischi, priorità, dipendenze e decisioni attraverso meccanismi informali perché la vicinanza tra le persone rende economico il coordinamento. Man mano che l’organizzazione cresce, aumentano le interfacce, le persone coinvolte, il costo dei disallineamenti e le conseguenze di determinate decisioni. Emergono quindi esigenze di governance, comunicazione e tracciabilità che prima semplicemente non esistevano. Non è che l’organizzazione sia diventata più “aderente” a una metodologia; il sistema che deve coordinare è diventato più complesso.

La stessa logica si applica alla modalità di esecuzione. Un progetto con requisiti relativamente stabili e alto costo del cambiamento può giustificare un approccio più predittivo. Un prodotto in un ambiente ad alta incertezza può beneficiare di cicli brevi di apprendimento e adattamento. Tra questi estremi esiste una varietà di combinazioni possibili, anche all’interno della stessa iniziativa, quando diverse parti del lavoro presentano differenti livelli di prevedibilità.

Per questo, la domanda su quale metodologia utilizzare non dovrebbe essere il punto di partenza. Prima di essa viene una questione più fondamentale: cosa dobbiamo gestire, quali sono i rischi coinvolti, quali vincoli esistono e quanta coordinazione e governance questo contesto richiede realmente? È a partire da queste risposte che può essere progettato un approccio gestionale.

## Management design

Nel system design, non iniziamo dicendo che ogni applicazione deve avere microservizi o messaging. Iniziamo comprendendo requisiti e vincoli. Volume, disponibilità, latenza, sicurezza, costo, capacità operativa e criticità aiutano a determinare quali decisioni architetturali siano giustificate. Non esiste un’architettura corretta in astratto. Esiste un’architettura adeguata a un determinato insieme di requisiti e vincoli, considerando i trade-off coinvolti.

La stessa logica può essere applicata alla gestione. Un progetto critico può richiedere meccanismi di governance che sarebbero sproporzionati in una piccola iniziativa. Un progetto con molte dipendenze può avere bisogno di meccanismi di coordinamento che non hanno senso per un team che lavora in modo indipendente. Un’iniziativa altamente incerta può ottenere poco valore da una pianificazione eccessivamente dettagliata quando non esistono ancora informazioni sufficienti per sostenerla. Ciò che cambia da un contesto all’altro non è l’importanza della gestione, ma i problemi che deve risolvere e la complessità necessaria per risolverli.

Le pratiche di gestione possono quindi essere trattate come componenti di una soluzione. Il PMBOK offre una parte di questo repertorio, ma non determina da solo come tali componenti debbano essere combinati. La composizione finale dipende dal contesto, dalle esigenze e dai vincoli del progetto. È in questo senso che propongo di pensare al management design: la costruzione deliberata di un approccio gestionale a partire dal problema che deve essere amministrato.

L’idea è simile alla costruzione di un sistema. Avere più componenti disponibili non rende automaticamente migliore la soluzione. Ogni componente aggiunge capacità, ma può anche introdurre costi, complessità, dipendenze o nuove esigenze operative. Il lavoro di design consiste proprio nel decidere cosa debba far parte della soluzione, cosa possa essere semplificato e quali trade-off siano accettabili.

Il tailoring, in questo senso, smette di essere soltanto l’atto di “adattare il PMBOK”. Diventa una conseguenza naturale dello stesso processo di design: comprendere il contesto, selezionare i componenti adeguati e comporre un approccio proporzionato al problema che deve essere risolto.

## Tailoring non significa fare meno

È facile interpretare il tailoring come una licenza per ridurre i processi. Se un’organizzazione ha molti documenti, ne elimina alcuni; se ha molte riunioni, ne cancella alcune; se una determinata fase sembra burocratica, smette di eseguirla. Il risultato può anche essere un approccio migliore, ma ridurre i processi di per sé non caratterizza il tailoring. La differenza sta nel criterio utilizzato per prendere questa decisione.

In architettura, una soluzione non è migliore semplicemente perché possiede meno componenti. Un’applicazione con pochi componenti può essere elegante o insufficiente; un’architettura più complessa può essere necessaria oppure può rappresentare overengineering. Il numero di componenti conta meno della relazione tra essi e i requisiti che devono soddisfare. La stessa logica vale per la gestione: la quantità di pratiche utilizzate non determina la qualità dell’approccio.

Applicare meno pratiche può, sì, essere più maturo che applicarle tutte indiscriminatamente, purché la scelta sia deliberata. Se un determinato controllo è stato eliminato, è necessario comprendere quale problema risolveva, quale rischio è associato alla sua assenza e perché quel livello di controllo non sia necessario in quel contesto. Allo stesso modo, aggiungere una pratica dovrebbe richiedere una giustificazione equivalente: quale esigenza soddisfa e quale complessità introduce?

Il tailoring non significa scegliere il percorso più semplice. Significa dimensionare la gestione in funzione del problema, accettando consapevolmente i trade-off coinvolti.

## Il rischio dell’overengineering nella gestione

Nella tecnologia, l’overengineering è un problema noto. Una soluzione può essere tecnicamente corretta e, allo stesso tempo, inadeguata perché introduce una complessità che i requisiti non giustificano. Più componenti possono significare maggiore capacità, ma anche più dipendenze, maggiore sforzo operativo e più punti di errore. La complessità deve esistere per una ragione.

Nella gestione, l’equivalente si verifica quando un’iniziativa riceve documenti, approvazioni, riunioni e indicatori perché questi meccanismi fanno parte della metodologia aziendale, e non perché il progetto ne abbia effettivamente bisogno. Ogni elemento può sembrare ragionevole isolatamente. Il problema emerge quando osserviamo l’approccio come un sistema e ci accorgiamo che la sua complessità introduce più attrito che controllo, consumando capacità che potrebbe essere utilizzata per l’esecuzione stessa del progetto.

Questo non significa che documentazione, governance o controlli siano negativi. Significa che devono avere una funzione chiara. Una riunione deve esistere perché è necessario realizzare un determinato coordinamento. Un registro deve esistere perché una determinata informazione deve essere preservata, condivisa o utilizzata in una decisione. Un’approvazione deve esistere perché una determinata decisione richiede quell’autorità. Un indicatore deve esistere perché esiste una domanda rilevante a cui occorre rispondere.

Quando questa relazione si perde, il meccanismo smette di essere uno strumento di gestione e diventa semplicemente un rituale. È possibile avere un’organizzazione estremamente disciplinata nell’esecuzione dei processi e, allo stesso tempo, poco matura nella gestione dei progetti. Rispettare un processo dimostra aderenza al processo; non dimostra, di per sé, che il processo sia stato scelto correttamente.

## Esiste anche il rischio di una gestione sottodimensionata

La critica alla burocrazia può portare all’estremo opposto. Se troppa complessità è negativa, può sembrare che la gestione migliore sia quella che possiede il minor numero possibile di processi. Questa conclusione è tanto errata quanto associare la maturità alla quantità di controlli. In architettura, una soluzione minimalista può essere esattamente ciò che il problema richiede oppure essere semplicemente sottodimensionata. La differenza sta nei requisiti e nelle conseguenze delle scelte.

Nella gestione, l’equivalente è eliminare i controlli perché sono scomodi, lenti o incompatibili con la cultura del team, senza valutare il rischio che rimane dopo questa decisione. Un’azienda può dire di non aver bisogno di documentare le decisioni perché “siamo Agile”, evitare un determinato meccanismo di governance perché “siamo piccoli” o non monitorare formalmente i rischi perché “il team parla ogni giorno”. In determinati contesti, queste scelte sono perfettamente ragionevoli. In altri, trasferiscono semplicemente il costo a un problema futuro che nessuno ha deciso esplicitamente di accettare.

Questo punto è importante perché anche l’assenza di un controllo è una decisione gestionale. Se un meccanismo è stato deliberatamente rimosso, dovrebbe essere possibile spiegare quale esigenza soddisfaceva, perché tale esigenza non sia rilevante in quel contesto e quale rischio venga assunto nel non mantenerlo. Il tailoring non significa rimuovere ciò che sembra burocratico; significa decidere consapevolmente il livello di controllo necessario.

L’obiettivo, quindi, non è minimizzare i processi. È dimensionare la gestione in funzione della complessità, dei rischi e dei vincoli del contesto.

## Una startup non è una corporation in scala ridotta

È a questo punto che le startup in fase iniziale diventano un caso particolarmente interessante. Una piccola organizzazione, con poche persone, alta incertezza e un prodotto ancora in evoluzione, opera in condizioni molto diverse da quelle di un’azienda consolidata. La comunicazione è diretta, le decisioni possono essere prese con poca intermediazione e molte informazioni rimangono disponibili nel contesto stesso delle persone. Riprodurre in questo ambiente una struttura aziendale completa di project management può significare introdurre una complessità di cui l’organizzazione non ha ancora bisogno.

Questo non significa assenza di gestione. La startup continua ad avere bisogno di definire obiettivi, valutare rischi, gestire dipendenze, prendere decisioni e monitorare i risultati. Ciò che cambia è il modo in cui queste attività devono essere strutturate. Quando poche persone devono allinearsi su una decisione, una conversazione può essere sufficiente. Quando aumentano le persone coinvolte, le interfacce tra i team e il costo di una decisione mal coordinata, meccanismi che prima sembravano non necessari possono acquisire valore.

La pratica gestionale può quindi rimanere mentre la sua forma evolve. Una startup non deve importare la struttura di governance di una grande corporation per essere professionale, così come non deve trasformare ogni decisione in un processo formale per dimostrare maturità. Ma non dovrebbe nemmeno confondere l’informalità con l’assenza di gestione. Ciò che oggi può essere risolto attraverso prossimità e contesto condiviso potrebbe domani richiedere meccanismi espliciti di coordinamento, non perché l’organizzazione abbia finalmente “adottato una metodologia”, ma perché il problema che deve gestire è cambiato.

Questo è uno degli esempi più chiari di management design. L’approccio adeguato non è una versione ridotta di una metodologia aziendale, ma una soluzione costruita a partire dalle caratteristiche dell’organizzazione stessa. Man mano che cresce, questa soluzione può evolversi insieme al sistema che deve coordinare.

## Anche la gestione è un’architettura evolutiva

Ciò che funziona per una piccola organizzazione può smettere di funzionare man mano che cresce, allo stesso modo in cui un’architettura adeguata per un’applicazione in una determinata fase può dover essere rivista quando cambiano i suoi requisiti. Questo non significa che la soluzione precedente fosse sbagliata. Significa che era stata progettata per condizioni che non sono più le stesse.

La crescita modifica la natura del problema. Più persone aumentano le interfacce e il costo della comunicazione. Più team creano dipendenze che prima non esistevano. Più clienti aumentano le conseguenze di determinati errori. Maggiori risorse coinvolte aumentano il costo di decisioni sbagliate. Nuovi obblighi normativi introducono ulteriori vincoli. A un certo punto, meccanismi che prima sarebbero stati burocratici diventano necessari per mantenere coordinamento e controllo.

Nell’architettura software, questo processo è noto: una soluzione evolve perché il sistema che la circonda è evoluto. L’architettura gestionale segue la stessa logica. Un’organizzazione non dovrebbe preservare una determinata struttura di governance soltanto perché ha funzionato in passato, così come non dovrebbe introdurre nuovi meccanismi soltanto perché ha raggiunto una determinata dimensione. Il fattore scatenante del cambiamento dovrebbe essere rappresentato dalle nuove esigenze, dai nuovi vincoli e dai nuovi rischi emersi.

La maturità, in questo contesto, non consiste nel raggiungere uno stato in cui tutti i progetti utilizzano la stessa quantità di processo. Consiste nello sviluppare la capacità di riconoscere quando l’architettura gestionale non è più adeguata e di evolverla prima che la complessità del sistema renda questo cambiamento necessario in modo traumatico.

## Agile cambia la forma, ma non elimina il problema

Questa prospettiva cambia anche il modo di guardare ad Agile. L’opposizione tra PMBOK e Agile spesso parte dall’idea che il primo rappresenti processi strutturati mentre il secondo rappresenti adattamento. Questa dicotomia perde di vista il punto principale: entrambi possono offrire meccanismi per affrontare problemi di gestione, ma partono da condizioni diverse riguardo a prevedibilità, incertezza e cambiamento.

Un approccio adattivo ha senso quando esiste una rilevante incertezza su cosa debba essere costruito o su quale soluzione produrrà valore. Lavorare in modo iterativo permette di apprendere e correggere il percorso man mano che emergono nuove informazioni. Ma l’iteratività non elimina rischi, dipendenze, stakeholder, vincoli di budget, requisiti di sicurezza o esigenze di governance. Cambia semplicemente il modo in cui questi elementi vengono gestiti.

Un team può lavorare con cicli brevi, prioritizzazione continua e feedback frequente e, allo stesso tempo, dover gestire compliance, fornitori, budget o dipendenze tra team. Allo stesso modo, un’iniziativa può utilizzare una pianificazione predittiva in determinate dimensioni e meccanismi adattivi in altre. La scelta non deve essere ideologica. Deve rispondere alle caratteristiche del lavoro.

È per questo che gli approcci ibridi non dovrebbero essere visti come una contraddizione, ma come una possibile conseguenza dello stesso tailoring. Diverse parti di un’iniziativa possono presentare differenti livelli di prevedibilità, rischio e necessità di controllo. La domanda rilevante non è quale metodologia abbia vinto il dibattito, ma quali meccanismi di gestione siano necessari per affrontare adeguatamente il contesto.

Agile non elimina la necessità di gestione. Così come un approccio predittivo non implica, di per sé, burocrazia. Ciò che cambia è l’architettura utilizzata per organizzare e condurre il lavoro.

## L’automazione cambia i trade-off della gestione

La discussione sul management design acquisisce un’altra dimensione quando consideriamo IA e automazione. Scegliere quali pratiche applicare implica anche considerare il costo di renderle operative. Aggiornare registri, consolidare informazioni, produrre report, monitorare indicatori e identificare cambiamenti richiede impegno, e questo impegno influenza la decisione sul livello di gestione adeguato. Una pratica può essere rilevante e, allo stesso tempo, essere sproporzionata rispetto al contesto quando il suo costo di esecuzione è elevato.

L’automazione modifica questo trade-off. Un’attività che prima richiedeva ore di lavoro manuale può arrivare a richiedere soltanto una revisione umana. Informazioni disperse possono essere consolidate automaticamente, i report possono essere prodotti a partire da dati già disponibili e i sistemi possono aiutare a identificare pattern, inconsistenze e possibili rischi. Questo non significa semplicemente aggiungere più processi perché ora sono economici. Significa che pratiche prima considerate eccessivamente costose possono diventare sensate quando il costo della loro operatività diminuisce.

Il valore di una pratica non cambia necessariamente perché è diventata più economica da eseguire. Ciò che cambia è la relazione tra il suo beneficio, il suo costo e la complessità che introduce. Una soluzione che prima sarebbe stata sproporzionata può diventare adeguata al contesto, modificando le scelte possibili all’interno del management design.

Esiste, tuttavia, una frontiera importante. Automatizzare la raccolta e l’analisi delle informazioni non significa automatizzare il giudizio. Uno strumento può identificare un possibile rischio o una deviazione, ma valutarne la rilevanza, decidere se debba essere accettato e determinare una risposta continua a richiedere contesto e responsabilità. L’IA può ridurre il costo della gestione, ma non elimina la necessità di progettarla.

## Progettare la gestione, non seguire la ricetta

Il problema inizia dalla domanda stessa “quale metodologia dovremmo utilizzare?”. Nell’architettura delle soluzioni, prima comprendiamo il sistema, i suoi requisiti, vincoli, rischi e trade-off; solo allora definiamo l’architettura. Il management design segue la stessa logica: comprendere il contesto, dimensionare la governance necessaria e selezionare le pratiche che rispondono ai problemi reali del progetto. Quando i requisiti cambiano, anche l’approccio può dover evolvere.

È in questo processo che il PMBOK trova il suo posto. Non come una ricetta da applicare integralmente, ma come repertorio per orientare le decisioni. La maturità non risiede nella quantità di pratiche adottate, ma nella capacità di giustificare le scelte: quali rischi vengono gestiti, quali meccanismi sono necessari, quale complessità è accettabile e quali controlli deliberatamente non fanno parte della soluzione. Applicare meno pratiche può essere più maturo che applicarle tutte, purché la scelta sia consapevole e proporzionata al contesto.

In architettura, non consideriamo maturo l’architetto che utilizza tutti i componenti disponibili, ma colui che sa comporre una soluzione adeguata ai requisiti e ai vincoli, assumendosi consapevolmente i trade-off. La gestione dei progetti non dovrebbe essere diversa. Il PMBOK fornisce una parte del repertorio; il lavoro consiste nel saperlo trasformare in un approccio adeguato al problema che si intende risolvere.
