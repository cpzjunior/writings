# E se usassimo un'architettura modulare distribuita al posto del monolite modulare?

_Un'idea di architettura per startup in fase iniziale che devono crescere senza pagare in modo sproporzionato per l'infrastruttura o per la complessità dei microservizi._

**Sintesi:** Propongo un'architettura modulare distribuita che separa l'unità di sviluppo dall'unità di elaborazione: il modulo continua a organizzare codice, regole e test, mentre ogni use case può adottare la propria strategia di esecuzione e scalabilità quando emerge una necessità concreta. In questo modo, le startup possono iniziare con una struttura semplice, distribuendo solo i workload che richiedono realmente maggiore capacità, senza assumere anticipatamente la complessità dei microservizi. L'idea non è sostituire il monolite modulare o i microservizi, ma creare un'alternativa di partenza che permetta di rimandare le decisioni infrastrutturali e introdurre la complessità in modo graduale.

---

Quando una startup sta iniziando, l'architettura software è spesso una questione di equilibrio. Il team è piccolo, il prodotto sta ancora cercando il proprio mercato, il volume degli utenti è incerto e il budget è limitato. Allo stesso tempo, alcune decisioni prese all'inizio possono rimanere per anni e diventare difficili o costose da modificare in seguito. In questo contesto, un'architettura deve fare più che organizzare il codice: deve permettere all'azienda di rimandare le decisioni costose fino a quando non esiste una ragione concreta per prenderle.

Alcuni anni fa, sono stato presidente volontario di Se Doar, una ONG che gestiva una piattaforma per mettere in contatto organizzazioni sociali con persone e aziende interessate a fare donazioni o offrire attività di volontariato. Oltre alla presidenza, mi occupavo della piattaforma insieme ad altri volontari. Era un contesto in cui queste limitazioni diventavano particolarmente evidenti. Avevamo poche risorse, un team piccolo e poco margine per mantenere infrastruttura inutilizzata. Ogni decisione tecnica doveva essere valutata anche in base al suo impatto operativo e finanziario.

La prima versione della piattaforma utilizzava un monolite modulare. In quel momento aveva senso. L'applicazione era relativamente piccola, i moduli aiutavano a separare le responsabilità e l'infrastruttura rimaneva semplice da gestire. Con l'evoluzione del sistema, tuttavia, è diventato evidente che le diverse parti dell'applicazione non avevano necessariamente lo stesso comportamento. Alcune funzionalità ricevevano richieste costantemente, mentre altre venivano utilizzate solo occasionalmente. Alcune dovevano rimanere continuamente disponibili, mentre altre potevano essere eseguite on demand. Il codice poteva essere ben modularizzato e, tuttavia, l'applicazione continuava a essere l'unità principale di deployment e scalabilità.

È stato in questo contesto che la possibilità di utilizzare le functions è diventata interessante. Invece di mantenere capacità computazionale disponibile permanentemente per l'intera applicazione, determinate funzionalità avrebbero potuto consumare risorse solo quando venivano eseguite. Questo non significa che il serverless sia sempre più economico, né che sia la scelta migliore per qualsiasi workload. Il punto che mi ha attirato l'attenzione è stato un altro: diverse parti dello stesso prodotto possono avere profili di elaborazione molto differenti, ma normalmente siamo portati a scegliere un'unica strategia di esecuzione per l'intera applicazione.

Questa esperienza mi ha portato a una domanda che considero particolarmente rilevante per le startup in fase iniziale: perché la granularità dello sviluppo dovrebbe essere necessariamente la stessa del deployment e dell'infrastruttura? Un modulo può essere un'ottima unità per organizzare codice, test, regole di business e dipendenze senza dover essere necessariamente l'unità minima di deployment e scalabilità.

La domanda acquista ulteriore contesto quando osserviamo l'evoluzione delle architetture moderne. I microservizi offrono indipendenza di deployment, scalabilità e ownership, ma introducono la complessità intrinseca dei sistemi distribuiti. Il monolite modulare, invece, cerca di preservare la semplicità operativa di un'applicazione unica creando al contempo confini più forti all'interno del codice.

Per una startup piccola, questo può essere esattamente ciò che si cerca. Ma rimane una questione: se riusciamo a modularizzare lo sviluppo, dobbiamo necessariamente scalare e fare il provisioning di questi moduli come unità indivisibili? È questa la questione che voglio esplorare in questo articolo.

## Microservizi e monoliti modulari

Man mano che sistemi e organizzazioni crescono, iniziano a emergere problemi diversi. Un'applicazione grande può diventare difficile da mantenere perché le sue responsabilità non hanno confini chiari, ma può anche diventare difficile da gestire perché parti diverse devono evolvere, essere distribuite o scalare in modi differenti. Non esiste un'unica ragione per cui un sistema grande diventa complesso, e diverse architetture sono nate per rispondere a diverse parti di questo problema.

I microservizi hanno guadagnato spazio principalmente come risposta ai problemi di scala organizzativa e operativa. Diverse parti del dominio possono evolvere a velocità differenti, i team devono lavorare con maggiore autonomia e determinati componenti possono avere requisiti di scalabilità o disponibilità molto diversi. Separando queste responsabilità in servizi indipendenti, ogni servizio può avere il proprio ciclo di sviluppo e deployment, la propria infrastruttura e la propria strategia di scalabilità.

Questa indipendenza, però, ha un prezzo. Quando due componenti si trovano nello stesso processo, una dipendenza può essere risolta tramite una chiamata a un metodo o utilizzando direttamente una libreria. Quando questi componenti diventano servizi diversi, la comunicazione attraversa una rete. Un'operazione che prima falliva con un'eccezione può iniziare a fallire con un timeout; una chiamata sincrona può richiedere retry; una transazione locale può attraversare un confine di processo; log e metriche devono essere correlati per seguire una richiesta tra componenti differenti.

I microservizi non eliminano la complessità: ne spostano una parte verso la comunicazione, l'infrastruttura e l'operatività di un sistema distribuito. Per le organizzazioni grandi, questo trade-off può essere eccellente. L'indipendenza tra servizi può avere un valore maggiore rispetto alla complessità aggiuntiva che introduce. Per una startup in fase iniziale, invece, assumere questa complessità prima che esista una necessità concreta può rappresentare un costo significativo. Con pochi sviluppatori, ogni servizio aggiuntivo significa anche più deployment, osservabilità, infrastruttura, troubleshooting e decisioni operative.

I monoliti modulari partono da una preoccupazione diversa. Anche i sistemi grandi diventano difficili da mantenere quando le loro responsabilità non hanno confini chiari, quando le dipendenze si propagano attraverso il codice e quando le modifiche a una parte del sistema producono effetti inattesi sulle altre. La modularizzazione cerca di affrontare questo problema senza necessariamente introdurre un confine di processo. Possiamo organizzare un'applicazione in moduli ben definiti, mantenendo le interazioni tra essi all'interno dello stesso processo.

Questo approccio riconosce anche una caratteristica importante dello sviluppo software: i confini del dominio cambiano. Man mano che un team comprende meglio il prodotto, emergono nuove regole, vengono scoperte nuove responsabilità e moduli che inizialmente sembravano ben definiti possono dover essere divisi, combinati o riorganizzati. Mantenere questi confini all'interno di un'unica applicazione rende questi cambiamenti più semplici rispetto al trasformarli immediatamente in decisioni di distribuzione.

Per questo motivo, monoliti modulari e microservizi non rappresentano necessariamente fasi differenti della stessa evoluzione architetturale. Sono approcci che privilegiano proprietà differenti. I microservizi privilegiano l'indipendenza operativa e organizzativa, mentre il monolite modulare cerca di preservare la semplicità operativa di un'applicazione unica creando al contempo confini chiari all'interno del software.

Il problema che mi interessa in questo articolo emerge proprio tra queste due preoccupazioni. Possiamo avere un sistema sufficientemente piccolo perché la complessità dei microservizi non sia giustificabile, ma che presenti comunque workload con esigenze di elaborazione molto differenti. Possiamo anche avere un codice perfettamente modularizzato e, tuttavia, aver bisogno di scalare l'intera applicazione perché continua a essere l'unità di deployment e di elaborazione.

È a questo punto che emerge la domanda centrale di questo articolo: e se l'unità di sviluppo potesse continuare a essere il modulo, mentre l'unità di elaborazione e scalabilità potesse essere uno use case?

## Un'architettura modulare distribuita

La proposta parte da una separazione tra due preoccupazioni che normalmente finiscono per essere accoppiate: l'unità di sviluppo e l'unità di elaborazione. Il modulo continua a essere l'unità di organizzazione del software. È al suo interno che si trovano gli use case correlati, le regole di business, la persistenza, i test e le dipendenze. Il fatto che un modulo contenga diversi use case, tuttavia, non significa che tutti debbano essere eseguiti o scalati allo stesso modo.

Possiamo immaginare, per esempio, un modulo `Orders` contenente `CreateOrder`, `CancelOrder`, `GetOrder` e `GenerateReport`. Questi use case continuano ad appartenere allo stesso modulo e possono essere sviluppati, testati e versionati insieme. La differenza appare al momento dell'esecuzione: `CreateOrder` può essere eseguito da una function, `CancelOrder` può rimanere in un'applicazione convenzionale, `GetOrder` può utilizzare un'altra strategia di elaborazione e `GenerateReport` può essere elaborato in modo asincrono.

```
Orders
├── CreateOrder       → function
├── CancelOrder       → applicazione
├── GetOrder          → function
└── GenerateReport    → job
```

Se, per esempio, la domanda per `GetOrder` aumenta, possiamo aumentare la capacità destinata a questo use case senza necessariamente replicare l'intero modulo. Questa è la caratteristica principale della proposta: il modulo continua a essere l'unità di sviluppo ed evoluzione, mentre lo use case può, quando ha senso, essere un'unità indipendente di esecuzione e scalabilità.

Non sto proponendo che ogni use case debba essere eseguito isolatamente, tanto meno che ogni use case debba diventare un servizio. La granularità minore esiste solo quando esiste una ragione per utilizzarla.

Per rendere concreta l'idea, utilizzerò nel corso dell'articolo alcune tecnologie con cui mi piace lavorare, come .NET, PostgreSQL, Dapper, AWS e strumenti di Infrastructure as Code. Queste scelte sono esempi di implementazione, non requisiti dell'architettura. In un'implementazione con .NET, per esempio, ogni modulo potrebbe essere una libreria contenente i propri use case, regole di business, persistenza e test. L'infrastruttura necessaria per eseguire questi use case potrebbe essere definita insieme al modulo, utilizzando uno strumento di Infrastructure as Code come AWS CDK o l'equivalente di un altro provider.

In questo modo, `Orders` potrebbe dichiarare sia le risorse necessarie per la sua esecuzione sia il modo in cui ogni use case viene esposto. `GetOrder` potrebbe essere associato a una function e a un endpoint API, mentre `GenerateReport` potrebbe utilizzare una coda e un worker.

L'idea non è duplicare l'infrastruttura tra i moduli. Esiste una distinzione tra ciò che è condiviso e ciò che appartiene a un contesto specifico. Ciò che viene realmente utilizzato da tutti può fare parte di un core comune. Una capacità utilizzata da alcuni moduli può essere rappresentata da un modulo proprio. Ciò che appartiene a un solo modulo può rimanere insieme a esso.

```
Usato da tutti
      ↓
    Core

Usato da alcuni
      ↓
Modulo proprio

Usato da uno
      ↓
Modulo consumatore
```

Questa regola aiuta anche a evitare che il `Core` si trasformi gradualmente in un deposito di astrazioni generiche.

Se `Orders` e `Payments` utilizzano, per esempio, una capacità di pricing, questo non significa che `Pricing` debba fare parte del core. Può essere un modulo proprio, utilizzato da entrambi i consumatori.

```
Orders ────────► Pricing
Payments ──────► Pricing
Customers
```

La stessa logica vale per la comunicazione, ma esiste una differenza importante tra flussi sincroni e asincroni.

In un flusso sincrono, un confine modulare non deve necessariamente rappresentare un confine di rete. Se `Orders` utilizza `Customers`, l'applicazione può semplicemente dipendere dalla libreria corrispondente ed eseguire il codice di `Customers` direttamente nello stesso processo.

Se `Orders.GetOrder` viene eseguito all'interno di una function, questo non deve cambiare. La function ha come punto di ingresso lo use case di `Orders`, e le sue dipendenze possono continuare a essere risolte all'interno dello stesso processo.

```
API
 │
 ▼
Orders.GetOrder
 │
 ▼
Customers.GetCustomer
 │
 ▼
Repository
 │
 ▼
Database
```

In un flusso asincrono, invece, la comunicazione può continuare a utilizzare messaggistica o streaming. Un evento o un comando può essere pubblicato in una coda, come SQS, o in uno stream, a seconda delle caratteristiche del workload.

```
Orders
   │
   │ evento
   ▼
 SQS / Stream
   │
   ▼
Payments
```

L'architettura, quindi, non cerca di eliminare la comunicazione distribuita. Cerca di evitare di introdurla dove non è necessaria.

Se domani `Payments.ProcessPayment` dovesse essere eseguito separatamente, per esempio, potrebbe già trovarsi dietro un confine asincrono senza che questo richieda di trasformare l'intero modulo `Payments` in un servizio indipendente.

Questa è una differenza importante rispetto a un approccio basato sui microservizi. L'architettura non trasforma automaticamente ogni modulo in un servizio. Il sistema può iniziare interamente all'interno di un singolo processo e, man mano che emergono esigenze, determinati use case possono ricevere strategie differenti di elaborazione e deployment.

Una function può essere una di queste strategie, ma può anche essere un'applicazione convenzionale, un container, un worker o qualsiasi altro meccanismo adatto al workload.

```
Applicazione
├── Orders
├── Customers
├── Payments
└── Inventory
```

può evolvere in:

```
Applicazione
├── Orders
├── Customers
└── Inventory

Functions
├── Orders.GetOrder
└── Payments.ProcessPayment
```

senza che `Orders`, `Customers` o `Payments` debbano essere trasformati in microservizi.

Ciò che è stato distribuito non è necessariamente il modulo. È stata distribuita l'esecuzione di determinati use case.

Questa è, per me, la distinzione centrale dell'architettura: possiamo preservare un'unità di sviluppo sufficientemente grande da mantenere il codice organizzato e, allo stesso tempo, utilizzare un'unità di esecuzione sufficientemente piccola affinché determinati workload possano essere elaborati e scalati in modo indipendente.

## Le functions come punto di partenza

Per questa proposta, inizierei utilizzando le functions come strategia predefinita per gli use case esposti da endpoint sincroni.

Non perché le functions siano necessariamente superiori ai container o ai processi convenzionali, ma perché offrono una combinazione interessante per una startup in fase iniziale: elaborazione on demand, scalabilità indipendente e poca capacità inutilizzata quando l'utilizzo è basso o variabile.

L'idea è iniziare con una strategia semplice e cambiarla solo quando i dati mostrano che non è più adeguata. Invece di fare il provisioning di capacità permanente sulla base di una stima di crescita, possiamo lasciare che ogni use case consumi risorse in base al proprio utilizzo.

Questo è particolarmente interessante all'inizio di una startup, quando molte caratteristiche del workload sono ancora sconosciute. Il traffico può essere basso, irregolare o difficile da prevedere. Una funzionalità può rimanere quasi inutilizzata per mesi e, improvvisamente, iniziare a ricevere una quantità significativa di richieste.

Se `GetOrder` presenta, per esempio, un volume costante e elevato, può avere senso migrarlo verso un container o un processo provisioned. Se `GenerateReport` continua a essere eseguito poche volte al giorno, può rimanere una function.

```
Orders
├── GetOrder        → container
├── CreateOrder     → function
├── CancelOrder     → function
└── GenerateReport  → function
```

Il cambiamento avviene a livello dello use case. Il modulo `Orders` non deve essere riorganizzato né trasformato in un nuovo servizio. Stiamo semplicemente sostituendo la strategia utilizzata per eseguire una determinata parte di esso.

Per i workload asincroni, la strategia può essere diversa fin dall'inizio. Uno use case che consuma messaggi da una coda o da uno stream può essere eseguito, per esempio, da un worker. La function continua a essere una possibilità, ma non deve essere lo standard per tutti i tipi di workload.

Esiste, naturalmente, il problema del cold start. A seconda del runtime e dei requisiti di latenza, il tempo necessario per inizializzare una function può essere rilevante. Per un workload eseguito poche volte al giorno, questo può essere irrilevante. Per un'operazione a bassa latenza e traffico costante, può essere una ragione per scegliere un'altra strategia di esecuzione.

Questo è esattamente il punto della proposta. Le functions sono un punto di partenza, non una decisione definitiva. Man mano che il sistema rivela le proprie caratteristiche reali, ogni use case può adottare la strategia di esecuzione più adatta al proprio workload.

L'architettura, quindi, non dipende dal rimanere serverless. Dipende dalla possibilità di cambiare questa decisione senza dover modificare l'organizzazione del software.

## Vantaggi e trade-off

Il principale vantaggio della proposta è separare la granularità dello sviluppo da quella dell'elaborazione. Un modulo può continuare a essere un'unità coesa di codice, test ed evoluzione, mentre i suoi use case possono utilizzare strategie di esecuzione differenti.

Immaginiamo un modulo `Orders` in cui `GetOrder` riceve molte più richieste di `CancelOrder`, mentre `GenerateReport` viene eseguito solo alcune volte al giorno. Nel monolite modulare, tutti continuano a fare parte della stessa applicazione e condividono la stessa unità di deployment ed elaborazione. Nell'architettura proposta, ciascuno potrebbe utilizzare una strategia differente.

```
GetOrder        → function
CreateOrder     → function
CancelOrder     → applicazione
GenerateReport  → job
```

Il codice non deve essere riorganizzato per questo. Il modulo continua a essere `Orders`, con i suoi use case, le regole di business, la persistenza e i test. Ciò che cambia è il modo in cui ogni workload viene eseguito.

Questa granularità può essere interessante anche dal punto di vista economico. Una startup in fase iniziale può trascorrere molto tempo con una domanda bassa e imprevedibile. In questo scenario, mantenere capacità permanente per l'intera applicazione può significare pagare per risorse che rimangono inutilizzate per buona parte del tempo. Per determinati workload, l'elaborazione on demand può avvicinare il costo all'utilizzo effettivo.

Questo non significa che l'architettura sia necessariamente più economica. Workload costanti e prevedibili possono essere più economici con infrastruttura provisioned. Il vantaggio sta nella possibilità di non obbligare l'intera applicazione a utilizzare la stessa strategia. Uno use case può utilizzare una function, un altro un container, un altro un'applicazione convenzionale e un altro un worker.

La decisione può seguire il comportamento reale del workload. Questo è forse uno dei punti più interessanti per una startup: più che ottimizzare l'infrastruttura fin dal primo giorno, la proposta cerca di rimandare le decisioni infrastrutturali fino a quando il comportamento reale del prodotto non fornisce informazioni sufficienti per prenderle.

Invece di fare oggi il provisioning di un'infrastruttura dimensionata per una crescita che forse avverrà tra due anni, possiamo iniziare con una capacità compatibile con la domanda attuale e cambiare la strategia solo quando esiste una necessità concreta. L'architettura non cerca di anticipare la crescita. Cerca di evitare che sia necessario anticipare l'infrastruttura.

Questa flessibilità cambia anche il modo in cui l'applicazione può evolvere. Invece di scegliere tra rimanere interamente monolitica o migrare progressivamente verso i microservizi, possiamo immaginare un'evoluzione più selettiva:

```
Monolite modulare
       ↓
Distribuzione selettiva
       ↓
Maggiore distribuzione quando necessario
```

Un sistema può rimanere prevalentemente all'interno di un unico processo mentre solo gli use case che giustificano una strategia differente vengono distribuiti. Non è necessario anticipare quali parti dell'applicazione dovranno essere scalate, isolate o elaborate in modo diverso in futuro.

Questo può essere particolarmente interessante quando all'interno dello stesso prodotto coesistono workload molto diversi. Una funzionalità di IA, per esempio, può avere requisiti di elaborazione, latenza e costo completamente diversi rispetto a una tradizionale operazione CRUD. Non esiste necessariamente una ragione per cui entrambi debbano utilizzare la stessa strategia di esecuzione solo perché appartengono allo stesso modulo.

La funzionalità di IA potrebbe utilizzare un'infrastruttura specifica e scalare in modo indipendente, mentre gli altri use case continuerebbero a utilizzare un'infrastruttura convenzionale.

In fondo, il vantaggio non consiste semplicemente nel poter scalare con maggiore granularità. Consiste nell'evitare che le esigenze di un workload determinino l'infrastruttura degli altri. Ma questa flessibilità non elimina la complessità. Permette di introdurla in modo selettivo.

Quando uno use case viene eseguito al di fuori del processo principale, emergono i problemi noti dei sistemi distribuiti: latenza, timeout, retry, osservabilità, idempotenza e fault parziali. La differenza è che questi costi non devono essere assunti dall'intera applicazione. Se dieci use case possono continuare a essere eseguiti all'interno di un'applicazione convenzionale, non esiste necessariamente una ragione per distribuirli. Se un undicesimo presenta una necessità differente di scalabilità o elaborazione, possiamo distribuire solo quello use case. La proposta, quindi, non consiste nel creare microservizi più piccoli. Consiste nel permettere che la distribuzione sia una decisione locale, presa quando esiste un beneficio concreto.

Esiste anche un costo legato alle dipendenze. Quando un modulo utilizza un altro come libreria, una modifica incompatibile a questa dipendenza richiede che i consumatori vengano aggiornati, ricompilati e testati. Questo riduce parte dell'indipendenza di deployment che si otterrebbe con servizi completamente separati. D'altra parte, finché la dipendenza rimane all'interno dello stesso processo, non dobbiamo pagare il costo di una comunicazione remota per ogni interazione tra moduli. `Orders` può utilizzare direttamente `Customers` come libreria, senza trasformare questa dipendenza in una chiamata HTTP solo perché i moduli hanno confini differenti.

```
Orders ───────► Customers
   │
   └──────────► Pricing
                  │
                  ▼
               Products
```

Questo punto rende particolarmente importante il grafo delle dipendenze. Le dipendenze tra moduli devono avere una direzione chiara ed evitare cicli. Se `Orders` dipende da `Customers` e `Customers` dipende da `Orders`, distribuirli separatamente potrebbe semplicemente trasformare un accoppiamento di codice in un accoppiamento di rete.

La distribuzione di uno use case non implica nemmeno la distribuzione di tutte le sue dipendenze. Se `Orders.GetOrder` utilizza, per esempio, `Customers.GetCustomer`, questa chiamata può continuare a essere effettuata direttamente dalla libreria di `Customers`.

```
Orders.GetOrder
      │
      └──► Customers.GetCustomer
                │
                └──► Repository
```

In questo scenario, è stata distribuita solo l'esecuzione di `Orders.GetOrder`. `Customers` continua a essere una dipendenza in-process. Un nuovo confine distribuito appare solo quando esiste una decisione esplicita di eseguire `Customers` separatamente.

Questo è un aspetto importante della proposta: la distribuzione non deve necessariamente seguire i confini dei moduli. Uno use case può essere distribuito senza che tutti i moduli da cui dipende vengano anch'essi trasformati in servizi.

Esiste anche un costo legato alla granularità stessa dell'elaborazione. Separare gli use case permette di scalare ogni workload individualmente, ma può anche significare replicare il runtime e le dipendenze del modulo in diverse unità di esecuzione. Una function o un container può dover caricare le stesse librerie utilizzate da altri use case, aumentando il consumo di memoria, il tempo di inizializzazione e, a seconda del workload, il costo totale di elaborazione. La granularità minore, quindi, non è gratuita. Deve portare un beneficio sufficiente a compensare questa duplicazione.

Un altro limite importante riguarda le risorse condivise. La possibilità di scalare `GetOrder` indipendentemente non significa che il database sia in grado di accompagnare questa espansione. PostgreSQL, code, cache e servizi esterni possono continuare a rappresentare dei colli di bottiglia.

La proposta aumenta la granularità con cui possiamo scalare l'elaborazione, ma non rimuove i limiti dei componenti da cui questa elaborazione dipende. Se il database è il collo di bottiglia, aumentare semplicemente il numero di functions può peggiorare il problema. Per questo motivo, l'idea non è che ogni use case possa scalare indefinitamente in modo indipendente. È che, quando esiste capacità disponibile nelle risorse da cui dipende, non sia necessario scalare insieme ciò che non partecipa a quel workload.

Esiste anche una conseguenza operativa. Un sistema con diverse strategie di esecuzione avrà più deployment, configurazioni, permessi, osservabilità e risorse infrastrutturali rispetto a un monolite convenzionale. La proposta non elimina questo costo. Cerca di evitare che venga introdotto prima che esista una necessità concreta. Questo è forse il principale trade-off dell'architettura: ottenere flessibilità e granularità al costo di una certa complessità operativa aggiuntiva.

La domanda, quindi, non dovrebbe essere se questa architettura sia più semplice di un monolite o dei microservizi. Probabilmente non lo è. La domanda è se la complessità aggiuntiva emerga solo dove esiste una necessità che la giustifica.

## Cosa è questa architettura e quando ha senso

Non chiamerei questa proposta microservizi. Non perché un'architettura modulare distribuita sia incompatibile con i microservizi, ma perché l'unità architetturale proposta è diversa. Nei microservizi, il servizio concentra normalmente decisioni di modularità, deployment, ownership, operatività e scalabilità. Qui queste decisioni sono deliberatamente separate.

Il modulo continua a essere l'unità di sviluppo ed evoluzione. Gli use case continuano ad appartenere a quel modulo e possono condividere codice, regole di business, dipendenze e test. La differenza è che uno use case può, quando necessario, avere una propria strategia di esecuzione e scalabilità.

Questo significa che un modulo può rimanere interamente all'interno di un'applicazione convenzionale per tutta la vita del prodotto. Un altro può avere un solo use case eseguito come function. Un terzo può utilizzare l'elaborazione asincrona per un'operazione specifica. La distribuzione non è l'obiettivo dell'architettura; è una possibilità che può essere utilizzata quando esiste una ragione concreta.

Per questo preferisco chiamare questa idea architettura modulare distribuita. Non vuole essere una versione semplificata dei microservizi, né una fase obbligatoria tra il monolite modulare e un'architettura a servizi. La proposta consiste nell'esplorare se possiamo separare due decisioni che normalmente finiscono per essere prese insieme: come organizziamo e sviluppiamo il software e come facciamo il provisioning e la scalabilità della sua elaborazione.

Questo significa anche che non considero questa architettura adatta a qualsiasi sistema. Se un'applicazione è piccola, ha un carico prevedibile e un'infrastruttura convenzionale risolve il problema con ampio margine, introdurre questa granularità può semplicemente aggiungere complessità senza produrre un beneficio proporzionale.

Allo stesso modo, sistemi con requisiti molto specifici di sicurezza, disponibilità, governance, audit, isolamento o consistenza possono richiedere altre decisioni architetturali. La proposta di questo articolo parte da un contesto più specifico: startup in fase iniziale, con team piccoli, budget limitato e workload che possono crescere in modo molto disomogeneo.

Anche in questo scenario esiste un limite importante. Distribuire l'elaborazione non elimina le risorse condivise. Se diversi use case dipendono dallo stesso database e il database diventa il collo di bottiglia, aumentare il numero di functions non risolve il problema. Può persino aumentare la pressione sulla risorsa già satura. L'architettura permette di scalare l'elaborazione con maggiore granularità, ma non elimina i limiti dei componenti da cui tale elaborazione dipende.

Per questo vedo questo approccio principalmente come un'ipotesi per un determinato contesto, e non come una raccomandazione universale. Sembra avere più senso quando esiste una combinazione di team piccolo, domanda inizialmente bassa o variabile e aspettativa che diverse parti del prodotto possano crescere a velocità molto differenti.

In queste condizioni, la possibilità di scegliere la strategia di elaborazione per use case può permettere all'infrastruttura di seguire il comportamento reale del prodotto, senza richiedere alla startup di assumere anticipatamente tutta la capacità o la complessità operativa che potrebbe essere necessaria solo in futuro.

Alla fine, la proposta non consiste nello scegliere tra monolite modulare e microservizi. Consiste nel mettere in discussione se abbiamo bisogno di scegliere un'unica unità di esecuzione per l'intero sistema. Forse è possibile mantenere la semplicità dello sviluppo modulare e, allo stesso tempo, distribuire solo ciò che ha realmente bisogno di essere distribuito.

## Come saprei se l'architettura ha funzionato?

È importante chiarire che questo articolo presenta una proposta architetturale, non un'architettura validata empiricamente. Non ho avuto l'opportunità di implementare questo modello in una startup reale e seguirne l'evoluzione nel corso degli anni. Pertanto, non ho dati per affermare che riduca necessariamente i costi, semplifichi l'evoluzione del sistema o produca un'esperienza migliore per un team di sviluppo.

Ciò che ho è un'esperienza precedente che mi ha portato a vedere un possibile spazio tra il monolite modulare e i microservizi: da un lato, l'importanza di mantenere lo sviluppo semplice e modulare; dall'altro, la possibilità che diverse parti di un prodotto abbiano esigenze molto differenti di elaborazione e infrastruttura.

Per me, la proposta avrebbe senso solo se questa separazione tra sviluppo ed elaborazione portasse benefici reali senza creare una complessità maggiore di quella che intende evitare. Uno dei primi segnali sarebbe la capacità di mantenere i moduli relativamente semplici anche quando alcuni dei loro use case iniziassero a essere eseguiti in modi differenti. Il team dovrebbe riuscire a sviluppare e testare il modulo senza dover trasformare ogni differenza infrastrutturale in una preoccupazione del codice. Allo stesso tempo, uno use case dovrebbe poter acquisire una propria strategia di esecuzione o scalabilità senza richiedere che l'intero modulo segua il cambiamento.

Un altro segnale sarebbe l'evoluzione del sistema. Se l'applicazione potesse iniziare in modo semplice, rimanere prevalentemente all'interno di un unico processo e distribuire solo alcuni use case man mano che emergono esigenze concrete, questo sarebbe un'evidenza del fatto che l'architettura sta realizzando una delle sue principali proposte: permettere che la complessità venga introdotta gradualmente, invece di essere anticipata.

Anche le dipendenze sarebbero importanti. L'architettura dovrebbe permettere ai moduli di continuare a utilizzare direttamente le librerie quando questo è appropriato, senza trasformare ogni confine modulare in una chiamata di rete. Se, per distribuire un singolo use case, fosse necessario trasformare gran parte delle dipendenze in servizi indipendenti, questo sarebbe un segnale che la granularità proposta potrebbe creare più accoppiamento di quanto ne rimuova.

L'aspetto economico sarebbe un altro punto da osservare. La granularità aggiuntiva dovrebbe, per alcuni workload, permettere alle risorse di seguire meglio l'utilizzo reale. Ma questo calcolo non potrebbe considerare soltanto il costo di elaborazione. Sarebbe necessario includere osservabilità, deployment, infrastruttura, manutenzione e il tempo del team stesso. Se il risparmio ottenuto dall'elaborazione on demand fosse inferiore al costo aggiuntivo di gestione dell'architettura, la proposta non starebbe raggiungendo il proprio obiettivo.

Infine, osserverei cosa accade man mano che l'azienda cresce. Se, dopo aver raggiunto una scala maggiore, fosse necessario riscrivere i moduli, sostituire sistematicamente le dipendenze con API o migrare obbligatoriamente verso i microservizi per recuperare proprietà importanti, questo sarebbe un segnale che l'architettura ha semplicemente rimandato il problema. D'altra parte, se il sistema potesse evolvere gradualmente, distribuendo solo ciò che giustifica realmente la distribuzione, avremmo un'evidenza più interessante del fatto che l'approccio funziona.

Esiste comunque una possibilità importante: forse il risultato dell'esperimento sarà scoprire che questa architettura non offre un vantaggio sufficiente rispetto a un monolite modulare tradizionale. E anche questo sarebbe un risultato valido.

La proposta, quindi, non parte dalla certezza di aver trovato un'architettura migliore. Parte da un'ipotesi: forse esiste un modo per preservare la semplicità dello sviluppo modulare senza obbligare l'intero sistema a condividere la stessa strategia di elaborazione.

## Un'architettura da testare

Forse questo approccio non funziona così bene come immagino. La complessità operativa potrebbe emergere troppo presto. Man mano che l'organizzazione cresce, determinate caratteristiche del sistema potrebbero rendere i microservizi una scelta più adatta. E, in molti casi, lo stesso monolite modulare potrebbe continuare a essere la risposta migliore.

Questo non contraddice la proposta. L'architettura è stata pensata per un contesto specifico: startup in fase iniziale, con team piccoli, risorse limitate e workload che possono presentare differenze significative di domanda. Al di fuori di questo contesto, i trade-off possono essere completamente diversi.

L'idea non è nemmeno eliminare i microservizi. Se un'organizzazione arrivasse a un punto in cui isolamento, ownership, cicli di deployment indipendenti o altre proprietà di un'architettura distribuita diventassero più importanti della semplicità iniziale, i microservizi potrebbero rappresentare un'evoluzione perfettamente ragionevole. Allo stesso modo, se l'applicazione rimanesse piccola e prevedibile, potrebbe non esserci alcuna ragione per abbandonare il monolite modulare.

La proposta è più specifica: iniziare con un'architettura modulare semplice e mantenere la libertà di distribuire solo ciò che ha realmente bisogno di essere distribuito. Se questo funziona, una startup potrà rimandare sia le decisioni infrastrutturali sia parte della complessità operativa fino a quando non esisterà una ragione concreta per assumerle. Non sto proponendo un sostituto dei microservizi. Sto proponendo un'alternativa come punto di partenza.

L'architettura modulare distribuita è, alla fine, un'idea che mi piacerebbe mettere in pratica. Non so ancora dove siano i suoi limiti, né se i benefici saranno sufficienti a compensare i costi. Ma credo che esista una domanda abbastanza interessante da giustificare l'esperimento: possiamo mantenere la semplicità dello sviluppo modulare e, allo stesso tempo, permettere che l'elaborazione venga sottoposta a provisioning alla granularità degli use case che ne hanno realmente bisogno?
