# Perché i sistemi moderni stanno diventando più facili da costruire e più difficili da progettare?

_Le astrazioni del cloud, il paradosso della scelta e l'intelligenza artificiale stanno cambiando la natura della solution architecture più rapidamente di quanto riusciamo ad adattarci._

**Sintesi:** Esploro i motivi per cui i sistemi moderni sono più facili da costruire, ma più difficili da progettare: cloud, servizi gestiti, SaaS e IA hanno ridotto il costo di implementazione delle soluzioni, ma hanno ampliato lo spazio delle scelte e reso il giudizio architetturale il principale collo di bottiglia. In questo scenario, l'esperienza significa saper eliminare alternative, valutare i trade-off, riconoscere le dipendenze nascoste e preservare la reversibilità delle decisioni. Per questo propongo che la solution architecture abbia bisogno di un corpo di conoscenze più sistematico, qualcosa di simile a un “PMBOK della Solution Architecture”, per organizzare il processo decisionale senza sostituire il giudizio dell'architetto.

---

Ho una certa abitudine a guardare video di System Design. Mi piacciono particolarmente quelli in cui qualcuno spiega come una grande azienda ha risolto un problema su larga scala: come una piattaforma elabora milioni di eventi, come un'applicazione gestisce picchi di traffico, come un'azienda ha strutturato la propria architettura dati o come un determinato servizio è stato suddiviso in decine di componenti. È interessante osservare un'architettura dopo che le principali decisioni sono già state prese. Ogni componente sembra avere uno scopo chiaro e, guardando indietro, molte scelte sembrano quasi ovvie.

La situazione è diversa quando dobbiamo progettare un'architettura da zero. Nel corso della mia carriera ho progettato decine di architetture. Ho dovuto prendere decisioni su integrazione, dati, scalabilità, disponibilità, sicurezza, cloud e operation in contesti molto diversi. So che esistono diversi modi ragionevoli per risolvere la maggior parte dei problemi che incontro. Eppure, spesso mi sento sopraffatto quando inizio un progetto da zero. Non per mancanza di esperienza, ma per l'eccesso di opzioni.

Il punto di partenza dovrebbe essere semplice: quali sono i requisiti che la soluzione deve soddisfare? Quale disponibilità è necessaria? Quale volume di dati ci aspettiamo? Quale latenza è accettabile? Quali sono i vincoli di costo, sicurezza, operation e compliance? Quanto è importante la capacità di evolvere o migrare la soluzione in futuro? In teoria, queste risposte dovrebbero ridurre lo spazio decisionale. Nella pratica, anche dopo aver stabilito i vincoli, possiamo comunque arrivare a decine di soluzioni tecnicamente valide.

Ed è qui che di solito torno alla mia cucina semplice. Scelgo i servizi AWS che già conosco bene, ricorro a pattern che hanno già funzionato in altri progetti ed evito, quando non esiste una ragione forte per farlo, di introdurre una tecnologia o un'architettura completamente nuova. Può esserci del conservatorismo in questa scelta. Può esserci anche una certa mancanza di sperimentazione. Ma c'è qualcosa di più pragmatico: conosco meglio i rischi di ciò che ho già utilizzato.

Sperimentare una nuova soluzione su un altro cloud, introdurre più cloud o adottare una tecnologia che non conosco ancora a fondo può produrre un'architettura tecnicamente interessante. Ma può anche portare a una soluzione che non soddisfa altrettanto bene i requisiti, che il team fatica a gestire o che si trasforma in debito tecnico quando la realtà del progetto si dimostra diversa da quella che immaginavamo. La responsabilità della decisione non scompare perché la tecnologia è nuova.

Il problema è che le conseguenze non emergono necessariamente subito. L'insoddisfazione per una scelta, il debito tecnico e persino il rimpianto di aver adottato una determinata tecnologia possono emergere mesi dopo l'implementazione, quando il sistema ha già accumulato dati, integrazioni e dipendenze intorno a sé. Una decisione che sembrava reversibile può allora rallentare un progetto o rendere la sua sostituzione così costosa da non essere più un'alternativa praticabile.

Ho già scritto su una parte di questo dilemma in [“Cloud Computing: scegliere oltre il default”](https://cpzjunior.substack.com/p/cloud-computing-escolhendo-alem-do), discutendo del perché non dovremmo accettare automaticamente le scelte predefinite offerte dal cloud. Il problema che mi interessa qui è un passo ulteriore: anche quando sappiamo che esistono alternative al default, come decidiamo quali meritano davvero di essere prese in considerazione?

Più tecnologie conosciamo, maggiore diventa lo spazio delle soluzioni che riusciamo a vedere. E quanto più grande è questo spazio, tanto più difficile diventa valutare ogni alternativa con la profondità necessaria per prendere una decisione realmente consapevole.

Questo accade proprio mentre costruire sistemi non è mai stato così facile. Il cloud ha trasformato gran parte dell'infrastruttura in servizi consumabili. Il SaaS ha trasformato intere capacità in API. Le piattaforme gestite hanno eliminato un'enorme quantità di lavoro operativo. E l'intelligenza artificiale sta riducendo anche il costo di implementare e sperimentare software.

Il risultato è un paradosso: stiamo diventando sempre più bravi a costruire soluzioni, ma questo non significa che stiamo diventando altrettanto bravi a decidere quali soluzioni costruire.

Non sto sostenendo che i sistemi moderni siano peggiori, né che dovremmo tornare a gestire server, configurare manualmente l'infrastruttura o evitare le nuove tecnologie. Sarebbe esattamente il contrario di ciò che rappresentano questi progressi. Il punto è che, rendendo più facili determinate parti del problema, queste tecnologie hanno anche cambiato la natura delle decisioni che rimangono.

Quando il costo di implementare alternative diminuisce drasticamente, il problema smette di essere soltanto come costruire e diventa, sempre più, come scegliere.

## La complessità non è scomparsa. Ha cambiato posto.

Una delle grandi virtù dell'astrazione è proprio quella di permetterci di smettere di preoccuparci di determinati dettagli. Non abbiamo bisogno di conoscere l'implementazione interna di un servizio per utilizzarlo. Questo è uno dei principi fondamentali alla base di gran parte dell'ingegneria del software moderna.

Il cloud ha portato questo principio a una scala enorme. Per molto tempo, costruire un sistema significava gestire direttamente una quantità considerevole di infrastruttura. Server, storage, reti, bilanciatori, capacità, replica e disaster recovery facevano parte del problema perché non c'era modo di delegarli semplicemente.

Oggi gran parte di tutto questo può essere consumata come servizio. Un database può essere provisionato in pochi minuti. Una coda può essere creata tramite configurazione. La capacità può essere adattata automaticamente. Una funzione può essere eseguita senza dover amministrare il server su cui viene eseguita.

Questo ha ridotto enormemente il costo di implementazione. Ma ridurre la complessità di un livello non significa necessariamente ridurre la complessità del sistema nel suo complesso.

La complessità può semplicemente cambiare posto. Invece di dover sapere come costruire ogni componente, dobbiamo decidere come combinarli. Un singolo servizio può essere semplice da utilizzare, mentre il sistema formato dalla composizione di decine di essi può presentare comportamenti difficili da prevedere.

Questo cambiamento modifica anche il tipo di conoscenza richiesta all'architetto. Non basta più sapere come implementare un determinato meccanismo, né è necessario conoscere tutti i dettagli della sua implementazione. È necessario comprendere le proprietà rilevanti per la decisione: le sue garanzie, i suoi limiti, i suoi modelli di failure, i suoi costi e, soprattutto, come queste proprietà interagiscono con quelle degli altri componenti.

## Il paradosso della scelta

Esiste un'idea nota come paradosso della scelta: aumentare il numero di alternative disponibili non produce necessariamente decisioni migliori. Il cosiddetto “dilemma del supermercato” lo illustra bene. Di fronte a uno scaffale con decine di opzioni apparentemente simili, scegliere può diventare più difficile, non più facile. Superato un certo punto, confrontare le alternative richiede così tanto sforzo che finiamo per preferire ciò che già conosciamo, semplicemente perché il costo della decisione è inferiore.

La solution architecture sembra aver trovato una propria versione di questo problema. Per molto tempo, molte decisioni architetturali erano limitate da ciò che era possibile costruire con le risorse disponibili. Oggi, per una quota crescente dei problemi, la situazione è quasi inversa. Abbiamo decine di servizi in grado di risolvere la stessa esigenza e innumerevoli modi di combinarli. Il problema ha smesso di essere trovare una tecnologia capace di fare qualcosa ed è diventato decidere quale delle tecnologie capaci di farlo dovrebbe essere utilizzata.

E la difficoltà non cresce soltanto con il numero di alternative. Ogni alternativa possiede proprietà diverse e crea nuove possibilità di composizione. Scegliere un database non è una decisione isolata. La scelta influenza il modello dei dati, i meccanismi di integrazione, le strategie di backup, l'osservabilità, i costi operativi e persino le tecnologie che iniziano ad avere senso nei livelli successivi. Lo spazio decisionale può crescere rapidamente man mano che queste scelte si combinano.

È qui che l'esperienza dell'architetto diventa particolarmente importante. Un architetto esperto non valuta tutte le possibilità. Utilizza conoscenze accumulate, vincoli del problema ed euristiche per eliminare rapidamente ciò che non deve essere preso in considerazione. Una parte importante dell'esperienza architetturale consiste proprio nel sapere quali opzioni possono essere scartate senza un'indagine più approfondita.

La mia “cucina semplice” AWS è, in larga misura, una conseguenza di questo. Sono tecnologie che conosco, le cui proprietà e limitazioni ho già incontrato in progetti precedenti e sui cui rischi riesco a fare stime migliori. Quando scelgo una soluzione conosciuta, non sto necessariamente cercando la tecnologia più sofisticata. Sto riducendo deliberatamente lo spazio decisionale per poter dedicare attenzione alle decisioni che contano davvero.

Il rischio emerge quando questa euristica smette di essere una scelta consapevole e diventa semplicemente un riflesso. Se scelgo sempre ciò che conosco perché ci sono troppe opzioni da valutare, potrei scambiare il sovraccarico cognitivo con debito architetturale.

L'abbondanza di alternative, quindi, non rende soltanto il problema più ampio. Aumenta l'importanza di sapere quali alternative non devono essere considerate. La sfida architetturale diventa meno conoscere tutte le possibilità e più costruire criteri sufficientemente buoni per eliminarle.

## Quando l'astrazione nasconde limitazioni e dipendenze

Esiste anche un altro effetto dell'astrazione che merita attenzione. Quando consumiamo servizi gestiti, iniziamo a vedere soltanto una parte dell'architettura da cui dipendiamo. Il nostro diagramma rappresenta ciò che abbiamo deciso di modellare, non necessariamente tutto ciò che sostiene il sistema.

Questo non è necessariamente un problema. Non abbiamo bisogno di conoscere tutti i dettagli di una piattaforma per utilizzarla correttamente. Il problema emerge quando confondiamo la semplicità dell'interfaccia con l'indipendenza tra i componenti.

Quando inseriamo un S3, una Lambda o un DynamoDB in un diagramma, che cosa stiamo esattamente rappresentando? Uno storage a oggetti, una funzione eseguibile, un database. Ma cosa esiste sotto queste astrazioni? Come vengono distribuiti e replicati i dati? Come vengono provisionate e condivise le risorse? Quali sono i limiti di queste astrazioni? Quali dipendenze esistono tra esse e l'infrastruttura che le sostiene? E, soprattutto, quali di queste proprietà possono diventare rilevanti quando qualcosa si guasta?

Non abbiamo bisogno di conoscere tutti questi meccanismi per utilizzare i servizi. Ma questo non significa che smettano di esistere o che le loro proprietà siano irrilevanti per determinate decisioni architetturali.

Un sistema può sembrare distribuito tra diversi servizi, regioni o persino diversi cloud e dipendere comunque da componenti comuni che non compaiono nel nostro diagramma. La diversità che vediamo in superficie non garantisce l'indipendenza a tutti i livelli.

Il caso di Cloudflare nel 2022 è un esempio di questo tipo di dipendenza invisibile, anche se ho già analizzato quell'incidente in un altro articolo. Per questa discussione basta l'idea: le astrazioni possono nascondere non soltanto dettagli di implementazione, ma anche dipendenze e punti comuni di failure rilevanti per la resilienza di un'architettura.

Lo stesso vale per gli stessi provider cloud. Piattaforme diverse possono offrire un'enorme varietà di servizi, ma dipendere dagli stessi fornitori o da componenti condivisi in parti della propria catena tecnologica. L'astrazione ci permette di trattare questi servizi come blocchi indipendenti perché è così che dobbiamo consumarli. Questo non significa che siano completamente indipendenti nella realtà.

Questo è uno dei limiti importanti dell'astrazione architetturale. Possiamo deliberatamente ignorare dettagli che non sono rilevanti per una determinata decisione, ma dobbiamo riconoscere quando smettono di essere irrilevanti. Una dipendenza che può essere perfettamente accettabile per un'applicazione comune può diventare critica quando stiamo progettando alta disponibilità, disaster recovery o una strategia multi-cloud.

L'architetto non deve conoscere tutto ciò che esiste sotto un'astrazione. Deve sapere abbastanza per riconoscere quando le sue limitazioni o dipendenze possono cambiare la decisione che sta prendendo.

## L'IA aggrava il problema

L'intelligenza artificiale aggiunge un'altra dimensione a questa trasformazione perché riduce ulteriormente il costo di implementazione. La discussione sull'IA nell'ingegneria del software tende a concentrarsi sulla produttività: quanto codice riusciamo a produrre, quanti test riusciamo a generare o quanto tempo possiamo risparmiare. Questi effetti sono rilevanti, ma esiste una conseguenza architetturale meno discussa.

Se diventa più economico implementare un'alternativa, diventa anche più economico sperimentare alternative. Questo è positivo. La sperimentazione è uno dei modi migliori per ridurre l'incertezza. Il problema è che la riduzione del costo della sperimentazione aumenta anche la quantità di soluzioni che possiamo mettere in pratica prima ancora di avere chiarezza su quale dovremmo scegliere.

L'IA è un'evidenza particolarmente chiara di questo fenomeno. Esiste un numero crescente di modelli disponibili, offerti da diversi provider, con differenze di capacità, costo, latenza, contesto e comportamento. Nuovi modelli emergono continuamente, le versioni vengono aggiornate e i benchmark cambiano. Per chi sta progettando una soluzione, ciò significa che persino una decisione apparentemente semplice, come scegliere un modello per una determinata attività, può coinvolgere uno spazio di alternative difficile da seguire.

E il problema non finisce con il modello. Una soluzione che utilizza l'IA può coinvolgere strategie di inferenza, meccanismi di retrieval, vector database, tecniche di prompting, tool, agenti e diverse modalità di integrazione. Ognuna di queste scelte apre nuove possibilità di composizione. La tecnologia non ha semplicemente aggiunto un altro strumento al catalogo. Ha ampliato rapidamente lo spazio delle soluzioni che un architetto può prendere in considerazione.

L'IA riduce anche drasticamente il costo di sperimentare queste alternative. Un'idea che prima avrebbe richiesto giorni di sviluppo può essere trasformata in un prototipo in poche ore. Questo è un vantaggio indiscutibile. Ma esiste un'interessante asimmetria: il costo di costruire e testare una soluzione può diminuire molto più rapidamente del costo di comprenderne le conseguenze architetturali.

Possiamo quindi arrivare all'implementazione prima di arrivare alla comprensione. Possiamo costruire un prototipo funzionante, integrarlo con altri servizi e persino portarlo in produzione prima di avere una visione sufficientemente chiara dei suoi costi, limiti, dipendenze e comportamenti in condizioni diverse.

È proprio per questo che considero l'IA un'evidenza, e non soltanto un altro esempio, del fenomeno discusso in questo articolo. Mostra in modo particolarmente evidente che stiamo riducendo il costo di trasformare le decisioni in software senza ridurre nella stessa proporzione il costo di prendere buone decisioni.

L'IA non elimina il problema dell'architettura. Rende più evidente la differenza tra riuscire a costruire qualcosa e sapere se dovremmo costruirla in quel modo.

E questa differenza conta perché il costo di una decisione architetturale raramente emerge nel momento in cui viene presa.

## Il costo di una decisione emerge dopo

Una decisione architetturale sbagliata non deve necessariamente produrre immediatamente un sistema guasto. Spesso produce un sistema che funziona perfettamente all'interno delle premesse esistenti al momento della scelta.

Il problema emerge quando queste premesse cambiano. Una decisione può introdurre un accoppiamento a un fornitore, un modello di dati difficile da migrare, una dipendenza operativa, un'architettura difficile da scalare o una tecnologia che richiede competenze molto specifiche. Mentre il sistema cresce, ciò che sembrava una scelta semplice diventa sempre più difficile da invertire.

Il technical debt trova una buona analogia nel debito della carta di credito. Il problema non è soltanto ciò che rimandiamo, ma gli interessi che iniziano a maturare mentre rimandiamo la correzione. Nell'architettura, questi interessi vengono pagati sotto forma di complessità, accoppiamento e costo del cambiamento.

Una modifica che inizialmente richiedeva soltanto un piccolo adattamento può, alcuni anni dopo, coinvolgere la migrazione dei dati, la modifica dei contratti, cambiamenti nelle integrazioni, formazione dei team, riscrittura di componenti e interruzioni operative. Il sistema cresce intorno alla scelta originale e ogni nuova dipendenza rende più costosa la sua reversibilità.

Per questo, il technical debt non è soltanto lavoro accumulato. È il costo crescente di mantenere una decisione che ha già smesso di essere adeguata.

Esiste una differenza importante tra costo di implementazione e costo di reversibilità. Un servizio gestito può risolvere un problema in poche ore. Un'architettura costruita intorno ad esso può rimanere per anni. Quanto più il sistema diventa dipendente da quella scelta, tanto maggiore tende a essere il costo per abbandonarla.

Questo cambia il modo in cui una decisione architetturale dovrebbe essere valutata. Non basta chiedersi quanto costa implementare una soluzione. Bisogna chiedersi anche quanto costa cambiarla, quali premesse sostengono quella scelta e quanto sarà facile invertirla nel caso in cui tali premesse smettano di essere vere.

Questa preoccupazione diventa ancora più importante proprio perché la tecnologia ha reso l'adozione così facile. Quanto minore è il costo per iniziare, tanto maggiore è la tentazione di rimandare la domanda su quanto costerà uscire.

## Il problema dei framework

È in questo contesto che ho iniziato a notare un'altra cosa. La mia formazione nella gestione dei progetti mi ha abituato all'idea che una disciplina possa costruire un corpo di conoscenze relativamente stabile, capace di organizzare concetti, pratiche e decisioni anche quando gli strumenti e le metodologie utilizzate cambiano.

Nella solution architecture non vedo lo stesso livello di consolidamento. Esistono framework, metodi e pratiche piuttosto utili, ma sembrano risolvere parti diverse del problema. Spesso spetta allo stesso architetto combinare questi elementi per costruire il proprio processo decisionale.

TOGAF è un buon esempio. Ha una funzione importante e non ha mai preteso di essere un manuale di System Design. È stato concepito per l'Enterprise Architecture, con una preoccupazione molto più ampia per organizzazione, capability, governance, processi e allineamento strategico. Per questo, non mi sembra corretto criticarlo per non risolvere un problema che non è esattamente il suo.

Tuttavia, esiste un disagio legittimo quando guardiamo alla velocità con cui l'ambiente tecnologico è cambiato. La struttura di conoscenze necessaria per discutere di architettura sembra cambiare più rapidamente di quanto riusciamo a consolidarla. E questo crea una tensione difficile da risolvere: se un framework incorpora continuamente nuove tecnologie e pratiche, rischia di diventare rapidamente obsoleto; se rimane stabile, rischia di allontanarsi dalla realtà nella quale gli architetti prendono le proprie decisioni.

arc42 illustra l'altro lato della questione. È molto più vicino alla pratica della software architecture e offre una struttura pragmatica per documentare contesto, requisiti di qualità, decisioni architetturali, building block, runtime e deployment. È estremamente utile per organizzare e comunicare un'architettura. Ma documentare una decisione non equivale esattamente a strutturare il processo che ha portato a quella decisione.

Lo stesso vale per altre pratiche. Un Architecture Decision Record aiuta a registrare una decisione. C4 aiuta a rappresentare l'architettura. ATAM aiuta a esplorare determinati trade-off. Ognuno di questi approcci risolve un problema reale e può essere molto utile. Ciò che mi manca è una struttura che colleghi queste pratiche in un processo completo di decisione architetturale.

Un ADR può registrare che sono state considerate tre alternative e che una di esse è stata scelta. Ma registrare una decisione non equivale a strutturare il processo che ha portato a essa. Quali criteri dovrebbero essere considerati? Come valutare i trade-off? Come ponderare costo, rischio, complessità operativa, capacità del team, reversibilità e dipendenza dai fornitori? Quando una decisione è sufficientemente importante da essere formalizzata? Quando dovrebbe essere riesaminata?

Queste domande continuano a dipendere, in larga misura, dall'esperienza e dal giudizio di chi sta progettando il sistema.

Forse è proprio per questo che, nella pratica, è così comune trovare un'architettura rappresentata direttamente dai componenti di un cloud in Draw.io, Lucidchart, Miro o uno strumento equivalente, senza che alcun framework di architettura compaia esplicitamente nel processo.

Il diagramma inizia a essere costruito a partire dai servizi disponibili. Un'API qui, una coda lì, un database gestito, qualche funzione serverless, magari un servizio di osservabilità. L'architettura emerge dalla composizione dei componenti.

Questo non significa che non esista ragionamento architetturale. Esiste. Il problema è che gran parte di esso rimane implicito. Il diagramma mostra ciò che è stato scelto, ma non necessariamente mostra perché è stato scelto, quali alternative sono state considerate, quali premesse sostengono la decisione o quanto costerebbe annullarla.

E forse è proprio questa la lacuna che mi infastidisce davvero. Non sento la mancanza di un framework che mi dica quale tecnologia devo utilizzare. Sento la mancanza di un corpo di conoscenze che aiuti a strutturare e comunicare le decisioni architetturali senza dipendere esclusivamente dall'esperienza individuale di ogni architetto.

## Un PMBOK della Solution Architecture

È stato a questo punto che ho iniziato a comprendere meglio quella sensazione iniziale che mancasse qualcosa. Non sento la mancanza di un framework che mi dica quale tecnologia utilizzare. Sarebbe impraticabile in un ambiente che cambia così rapidamente. Sento la mancanza di qualcosa di più simile a ciò che rappresenta il PMBOK per la gestione dei progetti: un corpo di conoscenze che fornisca un linguaggio, principi e strutture per organizzare il processo decisionale senza dover prescrivere la soluzione.

Quando parlo di un “PMBOK della Solution Architecture”, non immagino un manuale che dica quale database, cloud o pattern architetturale dovremmo scegliere. L'idea sarebbe avere un riferimento che aiuti l'architetto a strutturare il problema e a rendere esplicito il ragionamento alla base delle decisioni, senza trasformare l'architettura in un processo meccanico.

arc42 si avvicina molto ad alcuni di questi obiettivi. Offre una struttura pragmatica per organizzare e comunicare un'architettura ed è uno strumento molto utile. Ma evidenzia anche la distinzione che sto cercando di fare: strutturare e documentare un'architettura non equivale esattamente a strutturare il processo decisionale che l'ha prodotta.

Lo stesso vale per altre pratiche. Gli ADR aiutano a registrare le decisioni, C4 aiuta a rappresentare le architetture e ATAM aiuta a esplorare determinati trade-off. Ognuno di questi approcci risolve un problema reale. Ciò che mi manca è una struttura che colleghi queste pratiche in un processo più ampio, senza richiedere che ogni architetto costruisca da solo questo processo a partire da riferimenti diversi.

Forse esiste una ragione per questo. L'architettura è profondamente contestuale e le decisioni architetturali raramente hanno una risposta oggettivamente corretta. Una metodologia eccessivamente prescrittiva potrebbe creare una falsa sensazione di precisione o trasformare il giudizio architetturale nel semplice rispetto di una serie di fasi. Non avrebbe senso sostituire l'esperienza dell'architetto con una checklist che cercasse di determinare l'architettura corretta per ogni situazione.

Tuttavia, credo sia possibile sistematizzare parte di questa conoscenza. La gestione dei progetti offre un riferimento interessante. Il PMBOK non determina quale progetto debba essere eseguito né quale decisione debba prendere un project manager. Organizza conoscenze, processi e pratiche che aiutano a strutturare il lavoro in contesti diversi.

La solution architecture potrebbe attingere alla stessa fonte. Non per copiarne i processi, ma per adottare un approccio simile di sistematizzazione: trasformare conoscenze disperse in una disciplina che aiuti a strutturare le decisioni, rendere esplicite le premesse, comunicare il ragionamento e preservare il giudizio di chi sta progettando il sistema.

La sfida sarebbe trovare un livello di astrazione sufficientemente stabile da sopravvivere ai cambiamenti tecnologici e, allo stesso tempo, sufficientemente concreto da aiutare qualcuno a prendere una decisione reale. L'obiettivo non sarebbe seguire ogni nuova tecnologia, ma offrire una struttura che continui ad avere senso quando le tecnologie cambieranno.

Forse questa è una delle prossime frontiere della maturità della disciplina: trasformare le conoscenze che oggi sono sparse tra framework, metodi, pratiche e, soprattutto, nell'esperienza individuale degli architetti in un corpo di conoscenze più sistematico per il processo decisionale architetturale.

## Il collo di bottiglia è cambiato

Forse la questione non è se i sistemi stiano diventando più facili o più difficili. Stanno diventando più facili da costruire e, proprio per questo, più difficili da progettare.

Cloud, servizi gestiti, SaaS e IA hanno ridotto drasticamente il costo di implementare e sperimentare soluzioni. Il collo di bottiglia si è spostato dall'implementazione al giudizio: decidere cosa costruire, quali alternative scartare, quali trade-off accettare e quali conseguenze siamo disposti a portare con noi.

Questo cambia anche ciò che ci aspettiamo da un solution architect. Conoscere più tecnologie continua a essere importante, ma non è sufficiente. Man mano che lo spazio delle soluzioni cresce, diventa sempre più importante saperlo ridurre consapevolmente. Forse l'architetto più prezioso non è quello che conosce più servizi, ma quello che riesce a eliminare alternative senza eliminare quelle giuste.

È per questo che la mancanza di un “PMBOK della Solution Architecture” mi infastidisce. Non perché abbiamo bisogno di un altro framework per seguire la prossima tecnologia, ma perché forse abbiamo bisogno di una disciplina più consolidata per prendere decisioni in un ambiente che cambia continuamente.

Costruire una soluzione non è mai stato l'obiettivo dell'architettura. L'obiettivo è prendere buone decisioni su ciò che vale la pena costruire e preservare, per quanto possibile, la capacità di cambiare idea quando cambiano le premesse.
