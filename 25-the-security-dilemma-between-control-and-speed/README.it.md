# Il dilemma della Security: tra controllo e velocità

_La sfida di integrare la Security nell'ingegneria senza trasformare la protezione in burocrazia._

**Riepilogo:** Sostengo che il dilemma tra Security e velocità non si risolva scegliendo un lato, ma avvicinando la Security all'ingegneria e portando le conoscenze di sicurezza nel momento in cui le decisioni sono ancora in fase di costruzione. Invece di dipendere da gate, approvazioni e interventi manuali, dobbiamo trasformare le conoscenze specialistiche in pattern, automazione e guardrail proporzionati al rischio. In questo modo, la Security smette di essere una fase che l'ingegneria deve aspettare e diventa una capacità integrata nel processo. L'obiettivo finale non è eliminare i rischi, ma permettere all'organizzazione di imparare, sperimentare e innovare sapendo quali rischi sta assumendo.

---

Per molto tempo, la mia visione della Security è stata probabilmente più semplice della realtà della disciplina. Essendo una persona che opera più vicino all'architettura e all'ingegneria che alle discipline di sicurezza, tendevo a vedere la Security in modo relativamente oggettivo: esiste un'area responsabile della sicurezza, con policy, strumenti, processi, valutazioni e controlli che devono essere considerati durante la costruzione delle soluzioni.

Basta però guardare un po' più da vicino per rendersi conto di quanto questa visione sia limitata. La Security è una disciplina molto più ampia di quanto suggerisca il nome. Identità, applicazioni, infrastruttura, cloud, dati, architettura, privacy, frode, risposta agli incidenti, intelligence, terze parti, compliance e molte altre dimensioni possono essere direttamente o indirettamente correlate alla sicurezza di un'organizzazione.

Questa ampiezza spiega anche perché sia difficile parlare di Security come se si trattasse di un'unica funzione. Il ritmo di un team di risposta agli incidenti è diverso da quello del GRC. La Threat Intelligence ha esigenze diverse dall'Application Security. L'Identity and Access Management affronta problemi diversi dalla Product Security. Ognuna di queste funzioni ha obiettivi, responsabilità e orizzonti temporali propri.

Questo testo non intende trattare la Security nel suo complesso. La riflessione qui è più specifica e nasce proprio dalla frontiera tra Security e ciò che è più vicino alla mia realtà: architettura, ingegneria e sviluppo software. È in questa interazione che ho iniziato a percepire un dilemma che mi sembra sempre più rilevante.

La Security deve essere vicina allo sviluppo per essere efficace. Deve comprendere le decisioni architetturali, le tecnologie utilizzate e i rischi associati a ciascun contesto. Allo stesso tempo, il modo in cui questa partecipazione viene strutturata può produrre risultati molto diversi. Quando dipende principalmente da una sequenza di gate, ticket, approvazioni, omologazioni e controlli manuali, può emergere una fase aggiuntiva tra l'ingegneria e il processo decisionale, soprattutto quando meccanismi simili vengono applicati a contesti con livelli di rischio differenti.

La sfida, quindi, non è scegliere tra sicurezza e velocità. È costruire un modello nel quale la Security riesca a proteggere l'organizzazione senza ridurne la capacità di imparare, sperimentare e innovare. E, quando parliamo di velocità, non parliamo soltanto di consegnare software più rapidamente. Parliamo della capacità di un'organizzazione di imparare rapidamente a conoscere nuove tecnologie, valutarne i rischi, prendere decisioni e trasformare questo apprendimento in innovazione.

## Security e il momento della decisione

Esiste un pattern comune nelle organizzazioni. Il prodotto definisce ciò che deve essere costruito, architettura e ingegneria definiscono come verrà costruita la soluzione e, a un certo punto, la Security viene coinvolta per valutare se quanto realizzato soddisfi i requisiti di sicurezza.

A prima vista, questo modello sembra ragionevole. Ogni area ha le proprie responsabilità e la Security funziona come livello specializzato di valutazione. Il punto di attenzione è il momento in cui questa partecipazione avviene. Quando la Security entra nella discussione dopo che gran parte delle decisioni che influenzano il rischio è già stata presa, le sue possibilità di contribuire diventano naturalmente più limitate.

Quando un rischio viene identificato in questa fase, l'architettura può essere già definita, il codice può essere già stato scritto, le dipendenze possono essere già state scelte e il prodotto può avere già aspettative sulla consegna. Una decisione di sicurezza che avrebbe potuto essere incorporata naturalmente durante la definizione della soluzione può, a questo punto, richiedere una modifica più significativa, alterare una scelta tecnologica o persino richiedere la revisione di una parte rilevante di ciò che è già stato costruito.

È a questo punto che il timing diventa importante. Una raccomandazione di sicurezza fatta all'inizio della definizione di una soluzione può rappresentare soltanto una decisione architetturale. La stessa raccomandazione fatta quando l'implementazione è avanzata può significare rilavorazione, modifica dei componenti, revisione delle integrazioni o impatto su una pianificazione già vincolata a una data di consegna.

I ticket entrano in questo processo come un modo legittimo per registrare queste richieste, organizzare le responsabilità e monitorarne la risoluzione. Il problema non è il ticket in sé, ma ciò che rappresenta quando una decisione rilevante di sicurezza viene scoperta soltanto in una fase avanzata dello sviluppo. Da quel momento esiste una tensione tra la corretta gestione del rischio e la salvaguardia della scadenza e dell'ambito che sono già stati stabiliti per la consegna.

Quando questo accade ricorrentemente, l'interazione tra Security e ingegneria può concentrarsi sulla valutazione di ciò che è già stato prodotto, invece di avvenire durante le decisioni che hanno dato origine alla soluzione. L'intervento continua a essere importante, ma parte del potenziale contributo della Security viene perso perché lo spazio per modificare la soluzione a basso costo si è già ridotto.

Esiste anche una conseguenza organizzativa rilevante. Quanto più la Security è distante dalle decisioni che originano una soluzione, tanto maggiore può essere l'importanza di meccanismi formali per garantire che i requisiti di sicurezza vengano considerati. Policy, approvazioni, evidenze, gate e processi sono strumenti legittimi per questo scopo. Allo stesso tempo, quando la Security partecipa prima alle decisioni, parte di questa necessità può essere soddisfatta in altri modi, come pattern, automazione, componenti riutilizzabili e conoscenza condivisa.

La questione non è eliminare i meccanismi di controllo, ma trovare il modo più adeguato di esercitarli. In alcuni contesti sarà necessaria un'approvazione formale. In altri, la stessa conoscenza può essere incorporata nell'architettura, nella piattaforma o nel processo stesso di sviluppo. Il modo di esercitare questo controllo può variare in base al rischio, al contesto e, soprattutto, al momento in cui viene presa la decisione.

## Il vero significato della velocità

Quando diciamo che la Security deve tenere il passo con la velocità dell'ingegneria, non dovremmo parlare soltanto del tempo di risposta ai ticket o della velocità di consegna del software. La questione più importante è la velocità con cui l'organizzazione riesce a imparare, prendere decisioni e trasformare questo apprendimento in innovazione.

Un'organizzazione tecnologica deve sperimentare. Deve testare nuove architetture, piattaforme, servizi, framework e strumenti. Deve scoprire rapidamente cosa funziona, quali sono i rischi, quali sono i costi e quali tecnologie possono generare un vantaggio competitivo. Questo processo di apprendimento non avviene necessariamente in cicli trimestrali. Spesso una decisione rilevante deve essere presa nell'arco di ore o giorni.

Immaginiamo che compaia una nuova tecnologia e che uno squad individui un'opportunità strategica nel suo utilizzo. Se il processo necessario affinché la Security valuti questa tecnologia richiede settimane o mesi, l'impatto può andare ben oltre il time to market. L'organizzazione perde capacità di sperimentare e, soprattutto, di imparare. Mentre la tecnologia evolve, l'opportunità può scomparire e la decisione può smettere di avere senso.

Esiste inoltre una conseguenza meno ovvia. Quando i processi di sicurezza non tengono il passo con le esigenze dell'ingegneria, può aumentare la pressione verso alternative. Un team può cercare un altro strumento, utilizzare un servizio al di fuori degli standard aziendali o costruire un'integrazione provvisoria per riuscire ad andare avanti. Questo non deriva necessariamente dall'intenzione deliberata di aggirare i controlli. Spesso è semplicemente il risultato di un'esigenza di business o di ingegneria che è emersa prima che esistesse una risposta adeguata nel processo formale. L'effetto può essere una riduzione della visibilità su ciò che viene utilizzato e una minore opportunità di influenzare il modo in cui la tecnologia viene adottata.

Per questo motivo, anche la velocità è una dimensione della sicurezza. Una Security efficiente deve essere sufficientemente rapida da partecipare al processo di sperimentazione mentre la decisione è ancora in fase di costruzione. Non basta valutare una tecnologia dopo che il business ha già deciso di utilizzarla. È necessario riuscire a comprenderne i rischi, proporre controlli proporzionati e stabilire condizioni affinché la sperimentazione possa avvenire in modo sicuro.

Questa vicinanza è vantaggiosa anche per la Security stessa. Le nuove tecnologie non rappresentano soltanto rischi da valutare. Richiedono anche apprendimento. Nuovi modelli architetturali, servizi cloud, strumenti di sviluppo e tecnologie emergenti possono introdurre rischi che non si adattano perfettamente ai controlli esistenti. Essere vicini all'ingegneria permette alla Security di comprendere questi cambiamenti nello stesso momento in cui vengono esplorati dall'organizzazione.

L'obiettivo non è semplicemente ridurre il tempo di consegna. È ridurre l'intervallo tra un'ipotesi, una sperimentazione, l'apprendimento sui suoi rischi e una decisione consapevole sulla sua adozione. Quando un'organizzazione riesce ad accorciare questo ciclo, non consegna soltanto più rapidamente. Aumenta la propria capacità di imparare, adattarsi e innovare senza rinunciare a una valutazione consapevole dei rischi.

## Security come parte dell'ingegneria

Forse il cambiamento più importante consiste nel smettere di pensare alla Security come a una fase del processo di sviluppo e iniziare a considerarla come una delle discipline che partecipano a questo processo. La sicurezza non dovrebbe essere qualcosa che si verifica soltanto alla fine di una soluzione. Dovrebbe essere una delle dimensioni considerate mentre la soluzione viene ancora progettata e le decisioni possono ancora essere modificate a un costo inferiore.

La Security non dovrebbe comparire soltanto quando c'è qualcosa da approvare. Dovrebbe partecipare alla definizione della soluzione. Un professionista della Security vicino all'ingegneria può discutere con l'architetto quali siano i confini di fiducia della soluzione, come verrà effettuata l'autenticazione tra i servizi, quali dati verranno trattati, dove si troveranno i punti di esposizione, quali privilegi saranno necessari, come verranno conservati i secret, quali dipendenze esterne verranno utilizzate e quali minacce siano realmente rilevanti in quel contesto. Il valore di questa partecipazione sta proprio nell'avvenire mentre queste decisioni vengono prese, e non dopo che l'architettura è già consolidata.

Questa partecipazione è diversa dal mettere qualcuno nello squad per controllare il lavoro. La vicinanza all'ingegneria dovrebbe esistere per consentire una collaborazione più efficace nella costruzione della soluzione, e non soltanto per seguire ciò che stanno facendo gli sviluppatori.

In questo senso, mi piace l'idea di trattare il professionista della Security come un partner dell'architetto delle soluzioni. Prodotto, architettura e ingegneria devono decidere come verrà costruita una determinata soluzione. La Security contribuisce a comprendere quali rischi questa architettura introduca, quali minacce siano rilevanti e come questi rischi possano essere mitigati senza compromettere inutilmente l'obiettivo del sistema.

Questa vicinanza cambia anche la natura della conversazione. Invece di discutere soltanto se una determinata tecnologia possa o non possa essere utilizzata, è possibile discutere a quali condizioni possa essere utilizzata in sicurezza. Invece di scoprire successivamente che una determinata architettura presenta un'esposizione indesiderata, è possibile identificare tale esposizione mentre le alternative sono ancora in fase di valutazione.

Questo non significa trasferire alla Security la responsabilità della soluzione. Il prodotto continua a essere responsabile del prodotto, l'ingegneria dell'implementazione e le decisioni architetturali delle persone responsabili della soluzione. La Security aggiunge a questa discussione conoscenze specialistiche su rischi e controlli.

Questa distinzione è importante perché integrare la Security nell'ingegneria non significa rendere la Security responsabile di tutto ciò che riguarda la sicurezza. Significa distribuire meglio le conoscenze necessarie affinché le decisioni siano prese da chi possiede il contesto, con la partecipazione di chi possiede la specializzazione.

La domanda smette di essere soltanto “La Security ha approvato?” e diventa “La soluzione è stata costruita considerando i rischi rilevanti per il suo contesto e le misure necessarie per affrontarli?”. Il cambiamento riguarda meno la rimozione di una fase di approvazione e più il portare le conoscenze di sicurezza nel momento in cui le decisioni sono ancora in fase di costruzione.

Questa integrazione comporta un requisito anche per il professionista della Security. Non basta essere presenti alle riunioni dello squad o conoscere il ciclo di sviluppo come un processo descritto nella documentazione. Per partecipare effettivamente all'ingegneria, è necessario comprendere il processo come pratica.

Un modo concreto per sviluppare questa comprensione è costruire. Una proof of concept può percorrere l'intero cammino di una soluzione, dalla definizione del requisito e dell'architettura fino allo sviluppo, pull request, pipeline, test, controlli di sicurezza, deploy e osservabilità. L'obiettivo non è trasformare il Security Engineer in uno sviluppatore, ma fornire un'esperienza pratica sufficiente per comprendere i vincoli, gli incentivi e i trade-off che fanno parte della quotidianità dell'ingegneria.

L'esperienza pratica cambia anche il modo in cui la Security valuta le proprie raccomandazioni. Implementando un controllo in una soluzione reale, il professionista inizia a vedere le dipendenze, lo sforzo di implementazione e gli impatti che quella decisione produce sulla pipeline e sul ciclo di sviluppo. Questa prospettiva è difficile da ottenere soltanto attraverso la definizione di policy o la revisione di documenti e aiuta a valutare se un determinato controllo stia producendo una riduzione del rischio proporzionata alla frizione che introduce.

Se una raccomandazione richiede processi manuali eccessivi, genera molte eccezioni o è difficile da implementare, questo può essere un segnale che il controllo debba essere riprogettato, automatizzato o incorporato in un pattern architetturale o in un componente di piattaforma.

Quanto più la Security comprende come il software viene effettivamente costruito, tanto meglio riesce a valutare non soltanto i rischi di una soluzione, ma anche il modo più appropriato di trattarli. Allo stesso modo, quanto più l'ingegneria comprende le ragioni alla base dei controlli, tanto maggiore è la possibilità che la sicurezza venga incorporata nelle stesse decisioni tecniche, riducendo la necessità di interventi successivi.

## Dal gate al guardrail

Questo ci porta a una distinzione importante tra gate e guardrail. Un gate condiziona la prosecuzione del flusso al soddisfacimento di una condizione o alla presa di una decisione. Un guardrail stabilisce i limiti entro i quali il lavoro può procedere, potendo incorporare verifiche e blocchi direttamente nell'ambiente di ingegneria. La differenza riguarda meno l'esistenza o meno di blocchi e più il modo in cui questi vengono incorporati nel processo. Nel modello basato sui gate, determinate decisioni devono essere valutate esplicitamente prima che il flusso possa procedere. Nel modello basato sui guardrail, parte di queste condizioni può essere incorporata nel processo stesso di sviluppo.

Entrambi possono essere necessari. Una modifica che coinvolge dati altamente sensibili, privilegi elevati o un'esposizione critica può giustificare una valutazione umana. In altri contesti, soprattutto quando la decisione è ricorrente e prevedibile, i controlli automatizzati possono offrire un modo più efficiente di trattare lo stesso rischio.

Non tutte le decisioni hanno lo stesso livello di rischio e, per questo, non tutte le decisioni devono richiedere lo stesso livello di intervento. Quanto più ricorrente, prevedibile e basso è il rischio, tanto maggiore può essere la capacità di trattarlo attraverso pattern, automazione e self service. All'aumentare della criticità, dell'esposizione o della complessità della decisione, cresce anche il valore dell'analisi specialistica della Security.

Questa è la logica di un approccio basato sul rischio: il livello di controllo deve essere proporzionato al rischio che si intende trattare. L'obiettivo non dovrebbe essere massimizzare la quantità di controlli, ma trovare un modo efficiente per ridurre i rischi rilevanti senza introdurre una frizione sproporzionata nel processo di ingegneria. Un controllo che richiede un intervento manuale ricorrente da parte di decine di squad può consumare una quantità significativa di capacità specialistica, anche quando la sua applicazione è giustificata in determinati contesti.

In questo contesto, l'automazione smette di essere soltanto un'iniziativa di efficienza e diventa una strategia di scala. Se cinquanta squad devono implementare lo stesso controllo, la conoscenza utilizzata in queste decisioni può essere trasformata in un componente, una policy, una pipeline, un template o una capacità di piattaforma che incorpori già questo controllo in modo sicuro. Invece di riprodurre la stessa analisi in contesti diversi, parte di questa conoscenza può essere resa direttamente disponibile all'ingegneria.

Questa trasformazione permette alla Security di concentrare la propria capacità umana dove la sua partecipazione aggiunge più valore: decisioni nuove, complesse, ad alto impatto o che dipendono dal contesto. Per ciò che è ricorrente e prevedibile, la conoscenza può essere incorporata nell'ingegneria stessa.

La Security non scala in modo sostenibile aggiungendo persone nella stessa proporzione in cui crescono gli squad. Scala quando trasforma la conoscenza specialistica in capacità riutilizzabili e permette che i controlli vengano applicati in modo coerente da molti team. Quando possibile, questo fa sì che il percorso sicuro sia anche il percorso più semplice per l'ingegneria.

## Tempo e scala: la Security oltre la coda

Esiste una conseguenza operativa importante quando la Security diventa parte del ciclo di ingegneria. Se l'ingegneria prende decisioni in ore o giorni, il tempo necessario per una valutazione di sicurezza deve essere compatibile con l'orizzonte temporale di queste decisioni. Questo non significa trasformare ogni richiesta in un'attività urgente, ma evitare che l'analisi di sicurezza operi a un ritmo completamente disallineato rispetto al processo di ingegneria.

Questo cambia anche la discussione sulla scala. La sfida non consiste semplicemente nel fare in modo che la Security risponda più rapidamente alle richieste che riceve, ma nel ridurre il numero di decisioni che dipendono da una risposta manuale specifica. Una tecnologia comune e a basso rischio può essere utilizzata attraverso pattern precedentemente definiti. Un'architettura ricorrente può avere meccanismi di sicurezza già incorporati. Una policy semplice può essere validata automaticamente. Una vulnerabilità nota può, quando possibile, essere rilevata e trattata dalla pipeline.

Quanto più prevedibile è una decisione, tanto minore tende a essere la necessità di un intervento umano specifico. Quando il percorso sicuro è automatizzato, lo squad non deve aspettare. Quando un pattern architetturale incorpora già i controlli necessari, non è necessario ripetere la stessa analisi a ogni nuova implementazione. Quando la Security partecipa alla discussione architetturale, una decisione può essere trattata mentre la soluzione è ancora in fase di costruzione, riducendo la necessità di inoltrarla successivamente a una nuova valutazione.

È a questo punto che i ticket rivelano una questione di capacità. Continuano a essere utili per registrare richieste, responsabilità e decisioni, ma non eliminano la dipendenza strutturale tra molti squad e una capacità specialistica di Security. Se team diversi devono consultare individualmente la Security per prendere decisioni simili, l'organizzazione sta ripetendo interazioni intorno a una conoscenza che potrebbe essere riutilizzata.

Una Security che scala deve trasformare la conoscenza specialistica in capacità che possano essere utilizzate contemporaneamente da molti team. Questo include pattern architetturali, automazione, componenti riutilizzabili, documentazione, formazione, guardrail e piattaforme che incorporino i controlli direttamente nel processo di sviluppo.

Le nuove tecnologie possono aiutare in questo processo. L'intelligenza artificiale, per esempio, può ampliare la capacità dei professionisti della Security nelle attività di analisi, triage, orientamento e identificazione dei rischi. Può rendere le conoscenze specialistiche più accessibili e ridurre lo sforzo necessario per determinate attività. Ma questo, di per sé, non cambia il modello operativo. Se il processo continua a dipendere da ticket, approvazioni e interventi individuali, strumenti più sofisticati possono semplicemente rendere questo flusso più efficiente, senza eliminare la sua dipendenza da interazioni specifiche.

Il guadagno di scala avviene quando la conoscenza smette di dipendere da un'interazione individuale e diventa parte del processo stesso di ingegneria. Un pattern può essere riutilizzato da decine di squad. Un controllo può essere automatizzato. Una capacità di piattaforma può eliminare la necessità di un'implementazione manuale. Un'indicazione può essere disponibile nel momento in cui viene presa la decisione.

Questo ridefinisce anche il ruolo del team centrale di Security. Invece di concentrare la propria capacità nella revisione individuale di tutto ciò che accade nell'organizzazione, può indirizzare il proprio intervento umano verso decisioni nuove, complesse o di maggiore impatto, investendo al contempo nella costruzione delle capacità che permettono agli altri team di prendere decisioni ricorrenti con maggiore autonomia.

Scalare la Security non significa semplicemente gestire più richieste o rispondere a più ticket. Significa fare in modo che la conoscenza specialistica riesca a influenzare un numero molto maggiore di decisioni di ingegneria senza richiedere un'interazione umana proporzionale al numero di tali decisioni.

## La sicurezza come parte della cultura

Alla fine, esiste una dimensione che nessun processo, strumento o struttura organizzativa può risolvere da solo: la cultura. Non nel senso di campagne, formazione obbligatoria o dichiarazioni sulla “security first”, ma nel modo in cui l'organizzazione prende decisioni quando sicurezza, velocità e innovazione entrano in tensione.

Un'organizzazione matura non dovrebbe dipendere dalla Security per ricordare continuamente all'ingegneria che la sicurezza è importante. Allo stesso modo, la Security non dovrebbe dipendere dai processi per ricordare continuamente all'ingegneria che determinati controlli devono essere rispettati. La conoscenza del rischio deve essere presente nel luogo in cui vengono prese le decisioni.

Questo richiede apprendimento da entrambe le parti. La Security deve conoscere l'ingegneria non soltanto per capire come viene costruito il software, ma per comprendere come l'organizzazione impara, sperimenta e trasforma la tecnologia in prodotto. L'ingegneria deve conoscere la sicurezza non soltanto per rispettare i controlli, ma per incorporare il rischio nelle proprie decisioni tecniche.

È a questo punto che il dilemma cambia natura. La domanda smette di essere quanto controllo l'organizzazione debba esercitare sull'ingegneria e diventa quanta conoscenza di sicurezza riesca a distribuire senza trasformare ogni decisione in una dipendenza dalla Security.

L'obiettivo non è fare in modo che la Security insegua l'ingegneria, né fare in modo che l'ingegneria aspetti la Security. È ridurre le situazioni in cui una deve aspettare l'altra. Per farlo, la Security deve essere sufficientemente vicina da partecipare alle decisioni e trasformare la conoscenza specialistica in contesto, pattern e capacità che possano essere utilizzati dall'ingegneria.

Forse il vero equilibrio tra controllo e velocità sta proprio qui: non nell'eliminare i controlli, né nell'accelerare indefinitamente i processi di approvazione, ma nel collocare ogni meccanismo nel punto in cui produce più valore.

Come architetto di soluzioni, è da questa prospettiva che vedo questo dilemma. Non a partire dalla responsabilità di definire come debba operare la Security, ma dall'esperienza di trovarmi nel punto in cui le decisioni di prodotto, architettura, ingegneria e sicurezza devono convergere. È in questo punto che diventa evidente che sicurezza e velocità non devono necessariamente contendersi lo stesso spazio. La sfida consiste nel creare meccanismi che permettano a entrambe di avanzare insieme.

Un'organizzazione capace di innovare deve imparare rapidamente a conoscere la tecnologia, ma anche i rischi che questa tecnologia introduce. Non per eliminare il rischio, ma per distinguere ciò che deve essere mitigato, ciò che può essere accettato e ciò che non può essere assunto.

La Security, in questo contesto, smette di essere soltanto una funzione che protegge ciò che l'organizzazione ha costruito. Contribuisce a fare in modo che essa possa decidere, con consapevolezza del rischio, ciò che può ancora costruire.
