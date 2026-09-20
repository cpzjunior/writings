# I giochi non hanno bisogno di una Netflix, hanno bisogno di una AWS

_Se l'errore fondamentale dei servizi di giochi in abbonamento fosse trattare il catalogo dei giochi come prodotto, quando il vero prodotto che l'utente vuole affittare è la capacità computazionale?_

**Riassunto:** Sostengo che il cloud gaming venga pensato secondo il modello sbagliato: invece di trasformare i giochi in una Netflix, dovremmo separare il gioco dalla macchina che lo esegue. L'utente non ha bisogno di centinaia di titoli, ma dell'accesso alla capacità computazionale necessaria per giocare a ciò che ha scelto, senza dover acquistare hardware per diversi anni. Così come il cloud ha trasformato la computazione in un'infrastruttura elastica, i giochi potrebbero essere eseguiti su macchine affittate on demand, mentre l'acquisto e la distribuzione dei giochi rimangono indipendenti. Il futuro, quindi, potrebbe essere meno una Netflix dei giochi e più una AWS dei giochi.

---

Ho comprato una Xbox Series S con un'idea piuttosto semplice in testa: volevo giocare ai miei giochi preferiti senza dover assemblare un PC gaming. Il Game Pass sembrava la soluzione perfetta. Un abbonamento, una biblioteca enorme e una console relativamente economica. In pratica, ho scoperto una cosa curiosa: il catalogo è gigantesco, ma pochi giochi mi interessano davvero. Ci sono centinaia di titoli disponibili, ma continuo a voler giocare essenzialmente agli stessi generi e ad alcuni franchise specifici. Le dimensioni del catalogo, che dovrebbero essere la principale giustificazione dell'abbonamento, finiscono per avere poco significato quando i giochi che voglio davvero giocare rappresentano una frazione minuscola di esso.

Il problema è diventato ancora più evidente quando ho iniziato a pensare all'hardware. La Series S continua a essere una console capace, ma riesco già a vedere il percorso che sta seguendo. I giochi più recenti richiedono sempre di più all'hardware, e quella che oggi è una macchina perfettamente adeguata si trasforma gradualmente in una macchina limitata dalla generazione per la quale è stata progettata. Anche il mio PC non risolve il problema. Ha già alcuni anni e, sebbene continui a essere perfettamente utile per molte cose e faccia girare giochi che rimangono eccellenti, non ha più la capacità di seguire comodamente le uscite più esigenti. Ho quindi due problemi diversi: una libreria di giochi molto più grande di ciò a cui effettivamente voglio giocare e un insieme di hardware che deve essere sostituito periodicamente per stare al passo con l'evoluzione dei giochi.

È stato a questo punto che ho iniziato a chiedermi se stiamo guardando al problema nel modo corretto. Non voglio centinaia di giochi. Voglio giocare ad alcuni giochi specifici. E non voglio necessariamente comprare una nuova macchina a ogni generazione. Voglio avere accesso alla capacità computazionale necessaria per eseguire il gioco che ho deciso di giocare in quel momento. Queste due esigenze sembrano piuttosto diverse da ciò che i servizi in abbonamento e il mercato tradizionale dell'hardware stanno cercando di vendere.

La domanda che mi è venuta in mente è stata semplice: e se l'errore fondamentale dei servizi di giochi in abbonamento fosse trattare il catalogo dei giochi come il prodotto, quando il vero prodotto che l'utente vuole affittare è la capacità computazionale?

## Il problema di trasformare i giochi in Netflix

Forse il problema sta proprio nel tentativo di trasformare i videogiochi in una categoria di intrattenimento simile a film e serie TV. L'analogia funziona sotto alcuni aspetti, ma fallisce su un punto fondamentale: un gioco non è soltanto contenuto. È anche un'applicazione che deve essere eseguita.

Quando guardo un film, il lavoro computazionale pesante è già stato svolto durante la produzione. Il servizio deve archiviare e trasmettere il video in modo efficiente. Quando gioco a un titolo moderno nel cloud, la situazione è completamente diversa. Il server deve eseguire il gioco in tempo reale. Ogni movimento del controller modifica lo stato del gioco, CPU e GPU elaborano queste informazioni, viene renderizzata una nuova immagine, questa viene codificata e inviata attraverso la rete fino al mio schermo, mentre i miei comandi compiono il percorso inverso.

Questo cambia completamente la natura del prodotto. Nello streaming tradizionale, il contenuto è il prodotto principale e l'infrastruttura esiste per distribuirlo. Nel cloud gaming, il contenuto rimane necessario, ma la capacità computazionale diventa una parte essenziale di ciò che viene venduto. Quando qualcuno utilizza il cloud gaming perché non possiede un PC in grado di eseguire un determinato gioco, ciò che questa persona sta effettivamente cercando di acquistare è l'accesso temporaneo a una macchina sufficientemente potente.

Questo espone anche una limitazione del modello basato sul catalogo. Esiste la premessa che, quanti più giochi sono disponibili, tanto maggiore sia il valore dell'abbonamento. Ma questa relazione non è necessariamente vera per i videogiochi. Un giocatore può essere interessato soltanto ad alcuni generi e franchise specifici. Centinaia di titoli aggiuntivi possono rappresentare un'enorme quantità di contenuti disponibili e, allo stesso tempo, quasi nessun valore aggiuntivo per quell'utente.

La differenza rispetto a film e serie TV è importante. Quando sottoscrivo un servizio video, oggi posso guardare una serie poliziesca, domani una commedia, nel fine settimana un documentario e magari un film di fantascienza in seguito. Il costo per provare qualcosa di nuovo è basso. Nei giochi, l'investimento è molto maggiore. Molti titoli richiedono decine di ore e un adattamento alle proprie meccaniche, ai sistemi, ai controlli e alla progressione. Il giocatore non sta semplicemente consumando contenuti. Sta imparando a utilizzare un sistema interattivo.

È quindi possibile avere un catalogo enorme e offrire comunque poco valore a un determinato utente. La quantità di giochi disponibili è una metrica oggettiva, ma non necessariamente una buona metrica di utilità.

E questo solleva una questione piuttosto strana sul modello attuale: se so già quale gioco voglio giocare, perché devo abbonarmi a un intero catalogo per avere accesso alla macchina che è in grado di eseguirlo?

Se ho comprato Elden Ring, per esempio, e voglio giocarci su un computer che non possiede una GPU adeguata, il problema che ho non è la mancanza di accesso ai giochi. Il gioco ce l'ho già. Il problema è la mancanza di capacità computazionale.

Forse il prodotto che il cloud gaming dovrebbe vendere è proprio questa capacità.

## AWS e GPU come servizio

Il cloud computing ha trovato una soluzione a un problema molto simile. Un'azienda che ha bisogno di capacità computazionale non deve acquistare un server per i prossimi cinque anni. Può affittare l'infrastruttura in base alle necessità. Se ha bisogno di maggiore potenza di elaborazione, effettua il provisioning di una macchina più grande. Se ha bisogno di meno, riduce la capacità. Se non ha bisogno di nulla, disattiva le risorse.

La grande innovazione non è stata semplicemente mettere dei server in un datacenter e accedervi tramite Internet. È stata trasformare la capacità computazionale in una risorsa elastica, che può essere fornita, dimensionata e consumata in base alla domanda.

Lo stesso principio potrebbe essere applicato ai giochi. Invece di comprare una GPU per i prossimi anni, il giocatore potrebbe affittare capacità computazionale quando ne ha bisogno. Invece di scegliere una macchina che deve continuare a essere sufficiente per tutta una generazione, potrebbe scegliere la configurazione necessaria per il gioco che intende eseguire in quel momento.

Un servizio di questo tipo potrebbe offrire diverse classi di macchine. Una configurazione più economica potrebbe supportare giochi meno esigenti o giocatori disposti a rinunciare alla qualità grafica. Una configurazione intermedia potrebbe offrire un'esperienza a 1080p o 1440p. Una macchina più potente potrebbe soddisfare chi desidera la grafica al massimo, alte frequenze di fotogrammi o ray tracing. L'utente sceglierebbe la capacità in base a ciò a cui intende giocare e a quanto è disposto a spendere.

Questa possibilità cambia completamente il rapporto tra giocatore e hardware. Oggi, quando compro una GPU, devo cercare di prevedere quali saranno le mie esigenze future. Se compro una scheda molto potente, pago per una capacità che forse non utilizzerò per buona parte del tempo. Se compro una scheda più economica, rischio di scoprire qualche anno dopo che non è più sufficiente per i giochi a cui voglio giocare. In entrambi i casi, sto facendo una scommessa anticipata.

Nel cloud, questa decisione cessa di essere permanente. Immaginiamo che, invece di un abbonamento tradizionale, io possa semplicemente acquistare crediti computazionali. Metto 100 R$ sul mio conto e utilizzo quel saldo mentre gioco. Una macchina base può consumare pochi crediti all'ora, mentre una macchina dotata di una GPU di ultima generazione ne consuma molti di più. Il prezzo della sessione passa a riflettere direttamente la capacità computazionale che sto utilizzando.

Se voglio giocare a un titolo relativamente leggero per venti ore, posso scegliere una macchina più semplice e far durare a lungo i miei crediti. Se voglio trascorrere cinque ore su un gioco estremamente pesante, posso scegliere una macchina premium e accettare un consumo maggiore. Se non gioco per un intero mese, non c'è motivo di consumare crediti.

Il modello può continuare ad avere piani ricorrenti, ma l'abbonamento smetterebbe di rappresentare principalmente l'accesso a un catalogo. Potrebbe funzionare come un portafoglio di capacità computazionale, con crediti accumulati e consumati in base all'utilizzo. La differenza sembra piccola, ma economicamente è enorme: passo a pagare per ciò che utilizzo effettivamente, e non per una collezione di giochi che forse non aprirò mai.

Questo crea anche una relazione molto più trasparente tra prezzo ed esperienza. Se voglio un'immagine migliore, una risoluzione più alta o una GPU più potente, pago di più. Se sono disposto ad accettare una macchina più semplice, pago meno. Il servizio non deve decidere in anticipo quale configurazione debbano ricevere tutti gli utenti.

La differenza fondamentale è che l'unità di valore smette di essere il gioco disponibile e diventa la capacità computazionale consumata. Il gioco continua a essere necessario, ma l'infrastruttura smette di essere un dettaglio invisibile e diventa il servizio stesso.

## L'hardware smette di essere una scommessa

C'è poi una conseguenza più profonda. L'hardware locale richiede che il consumatore anticipi il futuro.

Quando compro una console o una GPU, sto acquistando una determinata quantità di capacità computazionale che spero sia sufficiente per diversi anni. Non so quali saranno i requisiti dei giochi futuri, ma devo prendere una decisione oggi.

Questo è particolarmente rilevante quando pensiamo alla velocità con cui evolve la tecnologia grafica. Una macchina che sembra potente al lancio di una generazione può continuare a funzionare perfettamente per molti anni, ma gradualmente richiede compromessi: ridurre la risoluzione, diminuire la qualità grafica, rinunciare al ray tracing o accettare frequenze di fotogrammi inferiori.

La mia Series S non smette di funzionare quando arriva una nuova generazione di giochi. Nemmeno il mio PC diventa una macchina inutile. Ciò che accade è più sottile: smettono di offrire la capacità computazionale necessaria per eseguire determinati giochi nel modo in cui vorrei.

Nel modello di cloud gaming, questa obsolescenza può essere spostata dal consumatore al provider. Quando arriva una nuova generazione di GPU, questa può essere aggiunta al datacenter. Quando un determinato hardware invecchia, può continuare a essere disponibile come opzione più economica per i giochi meno esigenti. L'utente non deve acquistare una nuova macchina per stare al passo con l'evoluzione dell'infrastruttura.

Questo non significa che l'obsolescenza scompaia. Semplicemente, smette di essere un problema che ogni consumatore deve risolvere individualmente e diventa un problema di infrastruttura che il provider gestisce su scala.

Invece di chiedermi quale hardware devo comprare oggi per continuare a giocare nei prossimi cinque anni, posso semplicemente chiedermi quale capacità mi serve per giocare al titolo a cui voglio giocare oggi.

È un cambiamento concettuale importante. Il consumatore smette di fare una scommessa sul futuro della tecnologia e inizia a consumare la capacità computazionale disponibile nel presente.

## Il gioco e la macchina non devono essere lo stesso prodotto

Il modello tradizionale ha unito due cose perché era necessario. La console o il PC forniva la capacità computazionale e il gioco veniva eseguito localmente. L'arrivo del cloud rende possibile separare questi due livelli.

Posso comprare un gioco indipendentemente dalla macchina che lo eseguirà. Posso avere la mia libreria su una piattaforma digitale e utilizzare l'hardware locale quando è sufficiente. Quando non lo è, posso utilizzare un'infrastruttura remota. Il gioco continua a essere il mio prodotto di intrattenimento, mentre la macchina diventa un servizio separato.

Questo significa che non abbiamo necessariamente bisogno di una “Netflix dei giochi” per far funzionare il cloud gaming. Il catalogo dei giochi può continuare a essere un prodotto delle piattaforme stesse. Sony, Microsoft e Nintendo possono continuare a vendere giochi, mantenere le proprie librerie, offrire titoli esclusivi e costruire i propri ecosistemi. Ciò che cambia è che l'hardware necessario per eseguire questi giochi può essere fornito da un altro livello dell'industria.

Un'azienda potrebbe specializzarsi esclusivamente nell'infrastruttura per i giochi. Non avrebbe bisogno di possedere una libreria di titoli né di negoziare esclusive. La sua funzione sarebbe mettere a disposizione macchine in grado di eseguire i giochi che l'utente già possiede, proprio come un provider cloud fornisce server per applicazioni appartenenti ad altre aziende.

Questo permetterebbe al mercato del cloud gaming di competere sull'infrastruttura invece di competere esclusivamente sul catalogo. Un provider potrebbe offrire prezzi più bassi, un altro potrebbe avere una latenza inferiore, un altro potrebbe mettere a disposizione GPU più moderne e un altro potrebbe avere datacenter posizionati geograficamente in modo migliore.

La libreria dei giochi continuerebbe a essere un livello indipendente. Potrebbe persino essere il principale differenziale competitivo di una piattaforma. L'utente potrebbe scegliere dove acquistare i propri giochi in base a prezzo, esclusive, servizi o comodità e, separatamente, scegliere dove eseguire quei giochi in base a capacità computazionale, latenza e costo.

Questo disaccoppiamento è proprio una delle caratteristiche più potenti del cloud computing. L'applicazione non deve essere proprietaria del server. L'azienda non deve acquistare l'hardware che esegue il suo software. L'infrastruttura diventa un livello indipendente, consumato in base alle necessità.

Non esiste una ragione fondamentale per cui i giochi debbano essere diversi. Il gioco può essere un prodotto. La macchina può essere un servizio. E non è necessario che i due siano venduti dalla stessa azienda.

## Che cosa stiamo realmente affittando?

Questa è forse la domanda che l'industria dovrebbe porsi. Stiamo parlando di due prodotti diversi che sono stati messi nello stesso pacchetto: accesso ai giochi e accesso alla capacità computazionale necessaria per eseguirli.

Un abbonamento ai giochi risolve il primo problema. L'utente paga per accedere a un catalogo, che può essere ampio, esclusivo o semplicemente conveniente. È un modello di distribuzione di software e contenuti. Il cloud gaming risolve il secondo. L'utente paga per utilizzare da remoto una macchina in grado di eseguire il gioco. È un modello di infrastruttura.

Non c'è motivo per cui questi due prodotti debbano essere venduti insieme.

Posso comprare un gioco da Microsoft, Sony, Nintendo o da qualsiasi altro store ed eseguirlo sul mio PC. Se il mio hardware non è sufficiente, posso affittare capacità computazionale da un provider specializzato. L'azienda che vende il gioco non deve essere la stessa che fornisce la macchina, così come l'azienda che sviluppa un'applicazione non deve essere proprietaria del server che la esegue.

Questo crea due mercati diversi. Da un lato, le piattaforme competono per giochi, prezzi, esclusive, servizi e librerie. Dall'altro, i provider di infrastruttura competono per prezzo, prestazioni, latenza, disponibilità ed efficienza operativa.

Il problema dei modelli attuali è che spesso trattiamo questi due mercati come se fossero uno solo. L'abbonamento ai giochi cerca di vendere il catalogo insieme all'infrastruttura, mentre la proposta di cloud gaming finisce per essere presentata come un modo diverso di consumare un abbonamento.

Ma non deve essere così. Posso voler giocare soltanto a tre giochi durante un anno e non avere alcun interesse per centinaia di altri titoli. Posso comprare questi tre giochi e, quando il mio hardware non è sufficiente, affittare una macchina in grado di eseguirli. In questo scenario, non ho bisogno di un abbonamento ai giochi. Ho bisogno di un gioco e di capacità computazionale.

Il cloud permette proprio questa separazione. Il gioco può continuare a essere un prodotto acquistato o sottoscritto, mentre la macchina può essere una utility consumata on demand.

L'industria ci ha venduto per decenni computer sempre più potenti per eseguire giochi sempre più esigenti. Il cloud offre la possibilità di invertire questa relazione: invece di comprare una macchina per stare al passo con i giochi, possiamo affittare la capacità necessaria per eseguire il gioco che scegliamo.

Forse il futuro dell'industria dei giochi non è una Netflix dei videogiochi, ma una AWS dei giochi.
