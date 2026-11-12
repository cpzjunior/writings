# Il dilemma architetturale dell'MCP

_Come distribuire le capacità per gestire la complessità cognitiva degli agenti IA._

**Sintesi**: Sostengo che il principale dilemma architetturale dell'MCP non riguardi la centralizzazione o la distribuzione dei server, ma la gestione del modo in cui le loro capacità vengono scoperte, selezionate e rese disponibili agli agenti. Negli ambienti aziendali, rendere disponibili tutti gli strumenti contemporaneamente aumenta la complessità cognitiva e rende più difficile la selezione contestuale. La soluzione consiste nel separare il catalogo globale delle capacità, la scoperta progressiva e l'esecuzione, combinando governance centralizzata, autonomia dei domini e routing intelligente. In questo modo, gli agenti accedono soltanto a ciò di cui hanno bisogno, quando ne hanno bisogno, senza doversi assumere la complessità di gestire l'intera infrastruttura. La sfida consiste nel trasformare la diversità delle risorse aziendali in un ecosistema selettivo, sicuro ed efficiente.

---

Nel mio ultimo articolo, "[Oltre gli Agenti Generalisti: un'Architettura di Micro-Agenti IA](https://cpzjunior.substack.com/p/alem-dos-agentes-generalistas-uma)", ho approfondito una questione che considero sempre più rilevante man mano che gli agenti IA iniziano a occupare uno spazio più significativo nelle architetture software: dobbiamo continuare a concentrare le responsabilità in agenti generalisti oppure iniziare a pensare a una distribuzione più specializzata della capacità di ragionamento?

Da quella discussione è emersa, tra le altre, la necessità di separare l'universo delle capacità possedute da un'organizzazione da ciò che ogni agente deve effettivamente conoscere durante un'esecuzione. Un catalogo globale può essere ampio, mentre il contesto di ciascun agente deve essere specifico e costruito in funzione del compito che deve svolgere.

Questa premessa, tuttavia, solleva una questione architetturale che merita di essere approfondita. Se iniziamo a distribuire l'intelligenza tra agenti diversi, come dovremmo organizzare e rendere disponibili gli strumenti e le capacità che utilizzano per interagire con il mondo?

È qui che il Model Context Protocol (MCP) introduce un nuovo dilemma. Immaginiamo una grande organizzazione, con decine di prodotti, centinaia di API e diversi domini di business. Ogni prodotto inizia a rendere disponibili le proprie funzionalità attraverso server MCP, rendendo le proprie capacità accessibili agli agenti. Inizialmente, la soluzione sembra relativamente semplice: creare un server MCP per ogni prodotto e consentire agli agenti di connettersi ai server di cui hanno bisogno.

Ma questo approccio solleva rapidamente altre questioni. E se un agente dovesse accedere a decine di prodotti? Dovremmo connetterlo a tutti questi server? Dovremmo rendere disponibili tutti gli strumenti contemporaneamente? Cosa succede quando le descrizioni, i parametri e i contratti di questi strumenti iniziano a consumare una parte significativa della finestra di contesto?

Un'alternativa sarebbe centralizzare tutto in un grande server MCP aziendale. Ma staremmo forse semplicemente ricreando, sotto una nuova interfaccia, gli stessi problemi di concentrazione e accoppiamento che storicamente abbiamo cercato di risolvere con le architetture distribuite?

Forse ci troviamo di fronte a una nuova categoria di problema. L'architettura non influisce più soltanto sull'organizzazione dei componenti software, ma anche sul modo in cui gli agenti scoprono, comprendono e selezionano le proprie capacità.

Se prima discutevamo di come distribuire l'intelligenza, ora dobbiamo discutere di come distribuire la conoscenza di ciò che l'intelligenza è in grado di fare.

## Il problema dell'abbondanza di strumenti

Una delle caratteristiche più interessanti dell'MCP è la possibilità di consentire a sistemi diversi di rendere disponibili le proprie funzionalità in modo standardizzato agli agenti IA. Invece di dipendere esclusivamente da integrazioni sviluppate appositamente per ogni applicazione, possiamo stabilire un'interfaccia comune per la scoperta e l'esecuzione degli strumenti.

Questa standardizzazione apre importanti possibilità di integrazione, ma crea anche una conseguenza che merita attenzione: più sistemi aderiscono al protocollo, più ampio diventa l'universo delle capacità potenzialmente disponibili agli agenti.

In una piccola applicazione, con pochi server e strumenti ben delimitati, questo scenario difficilmente rappresenta un problema. Tuttavia, quando trasferiamo questa architettura in un'organizzazione con decine o centinaia di prodotti, la situazione cambia considerevolmente.

Ogni server può rendere disponibili diversi strumenti, accompagnati dalle descrizioni, dai parametri e dagli schemi necessari al loro utilizzo. Quando un client aggrega strumenti provenienti da più server e presenta queste definizioni al modello, il volume delle informazioni cresce rapidamente. Una parte di esse sarà irrilevante per il compito corrente, ma continuerà a occupare spazio nel contesto e ad ampliare l'insieme delle alternative che il modello deve valutare.

È allettante trattare questo problema soltanto come un limite della finestra di contesto. Dopotutto, modelli sempre più grandi riescono a elaborare quantità crescenti di informazioni. Ma ritengo che questa interpretazione sia insufficiente.

Anche quando è disponibile spazio, presentare centinaia di strumenti non significa necessariamente migliorare la capacità decisionale dell'agente. Un catalogo esteso può aumentare l'ambiguità tra operazioni simili, rendere più difficile la selezione dello strumento appropriato e introdurre informazioni che non contribuiscono alla risoluzione del compito. La questione non riguarda soltanto la quantità di token consumati, ma anche la qualità dell'insieme di alternative presentato al modello.

Esiste quindi una distinzione importante tra tre dimensioni che spesso finiscono per essere trattate come se fossero un'unica cosa. La prima è la disponibilità: quali capacità esistono nell'organizzazione? La seconda è l'accessibilità: a quali di queste capacità un determinato agente è autorizzato e tecnicamente abilitato ad accedere? La terza è la rilevanza contestuale: quali di esse devono effettivamente essere presentate durante una specifica esecuzione?

Questi insiemi non devono necessariamente coincidere. Un'organizzazione può possedere migliaia di capacità, un agente può avere accesso autorizzato ad alcune centinaia e un determinato compito può richiedere soltanto un piccolo sottoinsieme di esse.

Questa distinzione è il punto di partenza per ripensare l'architettura MCP. La sfida non consiste semplicemente nel rendere accessibili tutti gli strumenti, ma nel gestire quali capacità devono essere scoperte, rese disponibili e utilizzate in ogni contesto.

## Il dilemma della centralizzazione e della distribuzione

La prima analogia che viene in mente è quella con una discussione ben nota nell'architettura software: centralizzare le funzionalità in un'applicazione monolitica oppure distribuirle tra servizi indipendenti.

Potremmo immaginare un grande server MCP aziendale, responsabile di concentrare gli strumenti di diversi prodotti e di offrire un unico punto di connessione agli agenti. Questo approccio semplifica l'esperienza di integrazione, facilita la gestione delle connessioni e può favorire una governance centralizzata.

D'altra parte, man mano che il catalogo cresce, il server finisce per concentrare responsabilità sempre maggiori. La manutenzione diventa più complessa, l'evoluzione può generare dipendenze tra domini e il numero di strumenti disponibili continua ad aumentare. Centralizzare la connessione non significa necessariamente risolvere il sovraccarico cognitivo. Possiamo avere un unico punto di accesso e, allo stesso tempo, rendere disponibile un universo di capacità difficile da gestire.

All'estremo opposto, potremmo adottare server MCP indipendenti per prodotto o dominio funzionale. Ogni team sarebbe responsabile dei propri strumenti, contratti e cicli di evoluzione. Avremmo maggiore autonomia, isolamento e flessibilità nella gestione delle capacità.

Tuttavia, anche questa distribuzione comporta dei costi. La moltiplicazione dei server richiede meccanismi di scoperta, gestione delle connessioni, autenticazione, osservabilità e governance. Inoltre, l'agente o l'infrastruttura responsabile della sua esecuzione dovrebbe comunque decidere quali server utilizzare e quali strumenti presentare.

È importante riconoscere che l'analogia con monoliti e microservizi ha i suoi limiti. Stiamo parlando di universi architetturali differenti. La distribuzione dei servizi mira a gestire principalmente responsabilità operative, dipendenze e scalabilità. Nel contesto dell'MCP esiste una dimensione aggiuntiva: il modo in cui organizziamo i server influenza la modalità con cui le loro capacità vengono scoperte e rese disponibili al modello.

Un server centralizzato può rendere disponibili gli strumenti in modo selettivo. Allo stesso modo, decine di server distribuiti possono essere gestiti attraverso un livello centrale di scoperta e routing. La topologia fisica dei server non deve necessariamente determinare l'organizzazione logica delle capacità.

Questa consapevolezza cambia la natura della discussione. Non dobbiamo necessariamente scegliere tra centralizzare o distribuire tutto. Possiamo distribuire l'esecuzione, centralizzare determinate responsabilità di governance e mantenere meccanismi condivisi di scoperta. L'importante è separare l'organizzazione dei server dal modo in cui le loro capacità raggiungono gli agenti.

## Dal catalogo dei server al catalogo delle capacità

Una possibile risposta sarebbe introdurre un livello intermedio responsabile di conoscere i server MCP disponibili e gestire l'accesso alle loro capacità.

Inizialmente, potremmo pensare a un MCP Registry, che fungerebbe da inventario dei server esistenti. Consentirebbe di individuare le integrazioni, identificare i relativi responsabili, consultare i metadati e conoscere le informazioni rilevanti su ciascun server.

Ma esiste una differenza importante tra conoscere i server di un'organizzazione e conoscere ciò che l'organizzazione è in grado di fare attraverso di essi.

Un registry risponde a domande come quali server esistono, dove sono disponibili e chi è responsabile della loro manutenzione. Un catalogo delle capacità deve andare oltre. Deve rappresentare gli strumenti messi a disposizione da questi server, le loro finalità, i loro contratti, i loro vincoli, le loro dipendenze e le condizioni necessarie per il loro utilizzo.

Immaginiamo un'organizzazione che disponga di diversi sistemi responsabili delle informazioni sui clienti. Ognuno mette a disposizione strumenti relativi a consultazioni anagrafiche, posizioni finanziarie e movimenti. Un inventario dei server consente di scoprire dove sono ospitate queste funzionalità. Un catalogo delle capacità consente di comprendere quale operazione soddisfa una determinata esigenza, quale fonte dati deve essere presa in considerazione e quali condizioni devono essere soddisfatte prima dell'esecuzione.

Questa differenza è fondamentale. La scoperta di uno strumento non dovrebbe dipendere esclusivamente dalla conoscenza preventiva del server che lo rende disponibile. Idealmente, l'agente dovrebbe poter partire da un'esigenza funzionale e trovare la capacità corrispondente, indipendentemente dalla sua posizione fisica.

In questo scenario, un MCP Hub o Gateway potrebbe assumere responsabilità complementari, come gestire le connessioni, intermediare le chiamate, applicare le policy di accesso e centralizzare gli aspetti operativi della comunicazione. Tuttavia, è importante non confondere queste responsabilità. Conoscere l'esistenza di uno strumento non significa necessariamente sapere quando utilizzarlo. Individuare un server non significa nemmeno che l'agente debba stabilire una connessione permanente con esso.

Iniziamo così a percepire la necessità di separare tre responsabilità architetturali: la registrazione delle capacità disponibili, la scoperta di quelle pertinenti a una determinata esigenza e l'esecuzione delle operazioni sui server responsabili.

Questa separazione consente all'infrastruttura di evolversi senza obbligare i prodotti a rinunciare alla propria autonomia. Ogni dominio può continuare a gestire i propri server MCP, mentre l'organizzazione mantiene una visione condivisa delle proprie capacità.

## Scoperta progressiva e selezione contestuale

Una volta definito un catalogo globale, emerge una possibilità particolarmente interessante: invece di rendere disponibili tutti gli strumenti fin dall'inizio, l'agente potrebbe partire da un insieme ridotto di capacità di scoperta.

Quando riceve una richiesta, consultarebbe il catalogo per identificare gli strumenti potenzialmente rilevanti. Soltanto dopo questa selezione le definizioni complete, inclusi parametri e schemi, verrebbero rese disponibili per l'utilizzo.

Questo approccio, spesso chiamato Progressive Tool Discovery, cerca di separare l'universo globale degli strumenti da ciò che deve effettivamente essere presente nel contesto del modello.

L'agente non deve conoscere in anticipo tutte le capacità disponibili. Deve poter scoprire quelle che saranno necessarie.

Possiamo immaginare questo processo articolato su due livelli. Nel primo, il catalogo presenta informazioni sintetiche sulle capacità, sufficienti a consentirne l'identificazione e il confronto. Nel secondo, dopo aver selezionato le alternative più appropriate, l'agente riceve i contratti completi necessari per invocarle.

Questa separazione riduce la quantità di informazioni inizialmente presentate al modello e consente di costruire progressivamente il contesto, man mano che il compito evolve.

Tuttavia, la scoperta dinamica non è semplicemente una questione di ricerca degli strumenti in un catalogo. La ricerca deve essere sufficientemente precisa da evitare la selezione di capacità simili, ma funzionalmente inadeguate. Una ricerca che restituisce operazioni correlate all'argomento, ma che non soddisfano effettivamente l'esigenza, si limita a trasferire il problema della selezione a una fase precedente.

Per questo motivo, ritengo che la scoperta dovrebbe combinare diversi meccanismi. Informazioni strutturate su dominio, finalità, autorizzazioni e vincoli possono ridurre l'universo delle possibilità. Tecniche di ricerca lessicale e semantica possono identificare strumenti correlati all'intento espresso. Un meccanismo di ranking può quindi valutare l'adeguatezza funzionale delle alternative individuate.

È importante considerare anche le dipendenze tra capacità. Alcune operazioni possono richiedere l'esecuzione preventiva di altre, mentre determinate funzionalità possono dipendere da strumenti resi disponibili da server differenti. Il meccanismo di scoperta deve essere in grado di rappresentare queste relazioni, evitando di trattare ogni strumento come un'unità completamente isolata.

Esiste, tuttavia, una questione interessante in questo modello: per scoprire ciò che ancora non conosce, l'agente deve avere accesso a un qualche meccanismo di scoperta. Questo significa che la capacità stessa di cercare strumenti diventa una capacità fondamentale dell'architettura. Il catalogo smette di essere soltanto un repository consultivo e diventa parte integrante del meccanismo di costruzione del contesto operativo dell'agente.

## Quando la descrizione dello strumento diventa parte dell'architettura cognitiva

In un ecosistema di piccole dimensioni, le descrizioni incoerenti possono essere corrette relativamente in fretta. Quando però esistono centinaia di strumenti, la qualità dei metadati inizia ad avere un impatto diretto sull'affidabilità dell'architettura.

Immaginiamo diversi prodotti che rendono disponibili strumenti chiamati get_customer, retrieve_customer, find_client e get_customer_details. Tutti sembrano ragionevoli, ma possono rappresentare operazioni differenti, consultare fonti distinte o rispondere a esigenze specifiche.

Il modello non conosce necessariamente questi confini funzionali. Deve dedurli dalle informazioni messe a disposizione dal server: nome, descrizione, parametri, schema di input e contesto di utilizzo.

Una descrizione come "Retrieve customer information" è tecnicamente valida, ma fornisce poche informazioni per orientare la decisione. Quali informazioni verranno restituite? Qual è la fonte ufficiale? In quali situazioni deve essere utilizzato questo strumento? Esistono vincoli? Quando sarebbe più appropriato un altro strumento?

Una descrizione realmente utile deve spiegare non soltanto cosa fa l'operazione, ma anche la sua finalità, il suo ambito, i suoi limiti e le circostanze in cui dovrebbe essere scelta.

Questa differenza è rilevante perché, in un'architettura tradizionale, un'API documentata male penalizza principalmente gli sviluppatori responsabili della sua integrazione. In un'architettura agentica, uno strumento descritto male può compromettere il processo decisionale stesso dell'agente.

La descrizione smette di essere semplice documentazione. Diventa parte dell'interfaccia cognitiva tra il software e l'intelligenza artificiale.

Per questo motivo, ritengo che un catalogo aziendale delle capacità debba andare oltre la semplice memorizzazione di nomi, descrizioni e schemi. Dovrebbe includere informazioni sul dominio funzionale, sulla finalità, sulle precondizioni, sugli effetti collaterali, sulle dipendenze, sulle autorizzazioni, sull'origine dei dati e sulle possibili sovrapposizioni con altri strumenti.

Esiste inoltre una distinzione importante tra il contratto tecnico e il contratto semantico di uno strumento. Lo schema definisce come invocare un'operazione. Il contratto semantico spiega cosa rappresenta, in quali condizioni deve essere utilizzata e quali garanzie offre sul risultato.

Due strumenti possono presentare descrizioni molto simili e tuttavia non essere intercambiabili. Uno può consultare una fonte ufficiale, mentre l'altro utilizza informazioni derivate o aggiornate a intervalli differenti. La scelta corretta non dipende soltanto dalla similarità tra l'intento e la descrizione, ma anche dall'autorevolezza della fonte e dalle caratteristiche del risultato atteso.

In questo contesto, i modelli IA potrebbero contribuire a valutare le descrizioni, identificare ambiguità, suggerire miglioramenti e arricchire i metadati. Tuttavia, esiste un limite importante: l'inferenza di un modello non può essere confusa con la definizione ufficiale di una capacità. Le informazioni tecniche, i contratti e le regole di business devono continuare ad avere fonti verificabili e responsabili identificati.

## Il ciclo di vita delle capacità

Finora abbiamo ipotizzato l'esistenza di un catalogo in grado di rappresentare l'universo delle capacità di un'organizzazione. Ma come garantire che questo catalogo rimanga aggiornato?

In un'azienda con prodotti e team di sviluppo differenti, vengono create nuove funzionalità, gli strumenti vengono modificati, i contratti evolvono e le API vengono dismesse. Un registry che dipende esclusivamente da aggiornamenti manuali rischia di diventare un altro inventario non aggiornato.

La scoperta dinamica funziona soltanto se le informazioni utilizzate per individuare gli strumenti sono affidabili.

Questo suggerisce la necessità di gestire il ciclo di vita delle capacità. Un nuovo server MCP dovrebbe essere identificato e registrato. I nuovi strumenti dovrebbero generare aggiornamenti nel catalogo. Le modifiche ai contratti dovrebbero innescare processi di rivalidazione e versionamento. Le capacità dismesse dovrebbero smettere di essere presentate come opzioni valide.

Forse questo processo potrebbe essere basato sugli eventi, utilizzando trigger provenienti dalle pipeline CI/CD, dalle piattaforme di gestione delle API, dai registri dei servizi e dagli stessi server MCP.

In questo modello, la pubblicazione di una nuova versione potrebbe attivare automaticamente un processo di scoperta, registrazione e validazione delle capacità. Le modifiche alle autorizzazioni potrebbero aggiornare le policy associate. Le modifiche incompatibili potrebbero richiedere un'approvazione prima della pubblicazione.

Il catalogo smetterebbe di essere un documento mantenuto manualmente e diventerebbe un inventario dinamico delle capacità aziendali.

Tuttavia, automatizzare la registrazione non significa eliminare la responsabilità su ciò che viene registrato. Ogni capacità deve avere un'origine verificabile, una versione di riferimento e un responsabile identificabile. L'infrastruttura deve essere in grado di determinare chi gestisce lo strumento, quale contratto è pubblicato e quali agenti o applicazioni possono utilizzarlo.

Dobbiamo considerare anche la coerenza tra catalogo ed esecuzione. Immaginiamo che il contratto di uno strumento venga modificato mentre un agente utilizza ancora una definizione precedente. La scoperta può essere stata eseguita correttamente, ma l'esecuzione fallirà perché le informazioni utilizzate dall'agente non corrispondono più alla versione resa disponibile dal server.

Pertanto, il ciclo di vita non termina con la registrazione. Dobbiamo gestire compatibilità, versionamento e dismissione, garantendo che le definizioni presentate agli agenti corrispondano alle capacità effettivamente disponibili.

In fondo, stiamo introducendo una nuova esigenza architetturale: non basta costruire un catalogo delle capacità. Dobbiamo costruire un'infrastruttura in grado di scoprire, registrare, validare, versionare e mantenere continuamente aggiornato questo catalogo.

## E se l'agente non dovesse mantenere tutte le connessioni?

Esiste un'altra possibilità che considero particolarmente interessante, anche sulla base di una difficoltà che riscontro nell'utilizzo quotidiano di agenti con più server MCP.

In determinate situazioni, devo attivare o disattivare manualmente le connessioni ai server che non fanno parte del contesto del compito. Il motivo è semplice: mantenere contemporaneamente disponibili molti strumenti può interferire con la selezione di quelli realmente rilevanti per l'esecuzione.

Questa esperienza suggerisce che forse non sia sufficiente controllare quali definizioni degli strumenti vengono caricate nel contesto. Potremmo aver bisogno anche di un livello responsabile della gestione dinamica delle connessioni stesse ai server.

Immaginiamo un router intelligente, un Intelligent MCP Router, che riceva la richiesta dell'agente, ne interpreti l'intento e identifichi i domini funzionali necessari. Sulla base di questa analisi, potrebbe consultare il catalogo, individuare le capacità pertinenti e rendere disponibili i relativi strumenti attraverso i server corrispondenti.

Se durante il compito emergesse la necessità di una nuova capacità, il router potrebbe effettuare un'altra ricerca, identificare il server responsabile e integrare i nuovi strumenti nell'insieme disponibile.

Allo stesso modo, i server che non fossero più rilevanti potrebbero avere i propri strumenti rimossi dall'insieme esposto all'agente. A seconda della strategia di connessione adottata, anche le relative sessioni potrebbero essere terminate.

L'infrastruttura inizierebbe così a gestire dinamicamente l'universo di possibilità presentato al modello.

Questo approccio, che potremmo chiamare Context-Aware MCP Routing, aggiunge una dimensione interessante all'architettura. Il router non sarebbe soltanto un intermediario responsabile dell'inoltro delle chiamate. Parteciperebbe alla gestione del contesto operativo dell'agente.

Tuttavia, esiste una distinzione tecnica importante. Disconnettere un server MCP non equivale semplicemente a smettere di esporre i suoi strumenti al modello. Possiamo mantenere attiva una sessione e controllare quali strumenti vengono resi disponibili. Possiamo anche mantenere il server connesso senza caricare le relative definizioni nel contesto corrente.

Ogni alternativa comporta costi differenti. Stabilire connessioni su richiesta può introdurre latenza, mentre mantenere sessioni aperte può consumare risorse. Alcuni server, inoltre, mantengono stati che non possono essere eliminati arbitrariamente.

Per questo motivo, non credo che la soluzione consista necessariamente nel connettere e disconnettere continuamente i server. Un'architettura più efficiente probabilmente combinerà strategie differenti: mantenere disponibili determinati server, caricare gli strumenti in modo selettivo e attivare nuove connessioni soltanto quando necessario.

È importante anche separare la selezione contestuale dal routing dell'esecuzione. Uno strumento può essere considerato rilevante senza essere autorizzato per un determinato agente. Allo stesso modo, una capacità può essere disponibile e autorizzata, ma non essere pertinente al compito corrente.

Il router deve rispettare questi confini. La selezione semantica non sostituisce l'autorizzazione. L'identità dell'agente, il contesto dell'utente, le autorizzazioni, le policy di dominio e l'audit devono essere considerati prima che uno strumento venga reso disponibile o eseguito.

Questa distinzione è particolarmente importante negli ambienti aziendali, nei quali determinate operazioni possono produrre effetti finanziari, modificare informazioni o accedere a dati protetti. L'infrastruttura non può delegare al modello la decisione su ciò che è autorizzato a fare.

## Un'architettura a più piani

Quando mettiamo insieme queste idee, iniziamo a comprendere che il problema non ha un'unica dimensione. L'organizzazione dei server, la registrazione delle capacità, la scoperta contestuale e l'esecuzione degli strumenti sono responsabilità correlate, ma non devono necessariamente essere concentrate nello stesso componente.

Un modo per organizzare questa architettura sarebbe suddividerla in tre piani. Il primo sarebbe il piano di controllo, responsabile del catalogo globale delle capacità, dei metadati, dei contratti, del versionamento, dell'ownership e delle policy di governance. La sua funzione sarebbe mantenere una rappresentazione affidabile di ciò che l'organizzazione rende disponibile attraverso i propri server MCP.

Il secondo sarebbe il piano di scoperta e selezione, responsabile di interpretare le esigenze presentate, consultare il catalogo, identificare le capacità pertinenti e determinare quali strumenti devono essere resi disponibili in un determinato contesto. È in questo piano che la scoperta progressiva e la selezione contestuale prenderebbero forma.

Il terzo sarebbe il piano di esecuzione, responsabile delle connessioni ai server, dell'autenticazione, dell'autorizzazione, dell'invocazione degli strumenti, della gestione dei risultati e dell'osservabilità. Qui, i server MCP continuerebbero a essere distribuiti e sotto la responsabilità dei rispettivi domini di business.

Questa separazione consente di combinare la governance aziendale con l'autonomia dei prodotti. Il catalogo può essere condiviso, mentre i server rimangono distribuiti. La scoperta può utilizzare meccanismi centralizzati, mentre l'esecuzione continua a essere responsabilità dei sistemi di origine. Il routing può essere coordinato da un livello comune senza richiedere che tutti gli strumenti risiedano in un unico server.

È importante osservare che questa suddivisione rappresenta una separazione logica delle responsabilità, non necessariamente tre piattaforme o servizi indipendenti. A seconda delle dimensioni dell'organizzazione, alcune di queste funzioni possono coesistere nello stesso componente. L'obiettivo è evitare che le decisioni relative a scoperta, governance ed esecuzione siano accoppiate soltanto perché appartengono allo stesso ecosistema MCP.

Questa architettura consente inoltre al meccanismo di selezione di evolversi indipendentemente dai server. Possiamo migliorare la ricerca semantica, modificare i criteri di ranking, integrare nuove policy o cambiare la strategia di connessione senza richiedere a ogni prodotto di ristrutturare le proprie integrazioni.

Il catalogo stesso può evolversi fino a rappresentare non soltanto singoli strumenti, ma anche capacità composte, che dipendono da operazioni rese disponibili da server differenti. In questo scenario, inizia a funzionare come una mappa delle capacità aziendali, avvicinando la visione tecnica dei servizi a ciò che l'organizzazione è effettivamente in grado di realizzare.

## La nuova sfida dell'architettura MCP

L'adozione di architetture agentiche negli ambienti aziendali amplia la portata delle decisioni di integrazione. Non basta definire come i sistemi espongono le proprie funzionalità; è necessario stabilire come queste funzionalità verranno descritte, individuate, selezionate e rese disponibili in base alle esigenze di ciascun agente.

L'MCP offre un'interfaccia standardizzata per collegare i modelli agli strumenti, ma non risolve, di per sé, l'organizzazione di questo ecosistema. Questa responsabilità spetta all'architettura che lo circonda, compresi i meccanismi di catalogazione, scoperta, governance e routing. È a questo livello che diventa possibile conciliare la distribuzione delle capacità tra domini differenti con una gestione coerente del loro utilizzo.

Le scelte relative alla granularità dei server, alla selezione contestuale e alla separazione tra scoperta, autorizzazione ed esecuzione avranno conseguenze dirette sulla scalabilità e sulla governance delle piattaforme agentiche. Più che una questione di implementazione del protocollo, si tratta di definire come l'organizzazione intende gestire le proprie capacità in uno scenario in cui gli agenti iniziano a interagire con un insieme sempre più ampio di sistemi.

La sfida architetturale consiste nel trasformare questa diversità di risorse in un ecosistema che possa essere esplorato in modo selettivo, sicuro ed efficiente, senza trasferire all'agente la complessità di gestire l'intera infrastruttura che lo supporta.
