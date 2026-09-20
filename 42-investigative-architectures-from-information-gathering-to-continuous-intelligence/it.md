# Architetture Investigative: dalla raccolta di informazioni all’intelligence continua

_Un’architettura orientata all’IA per indagare domande di business, apprendere dal contesto e monitorare continuamente ciò che può modificare una decisione._

**Riassunto:** Propongo un’architettura di intelligence che tratti l’indagine come propria unità principale: un processo persistente che formula ipotesi, collega evidenze, preserva il contesto e riprende il lavoro quando emergono nuove informazioni. Uno scheduler decide quali indagini meritano elaborazione, quanto sforzo valga la pena investire e quale debba essere il passo successivo, mentre memoria, feedback umano e governance danno continuità e affidabilità al processo. In questo modo, l’IA smette di limitarsi a raccogliere, monitorare o riassumere informazioni e passa a sostenere un processo continuo di indagine, nel quale l’architettura stessa apprende da ciò che ha scoperto e torna al problema quando il mondo cambia.

---

Mentre scrivevo “[L’Anti-Mago: Un Progetto Letterario](https://cpzjunior.substack.com/p/o-anti-mago-um-projeto-literario)”, mi sono reso conto che il percorso di Alden come investigatore mi stava portando a riflettere sempre di più sull’atto stesso di investigare: seguire indizi, formulare ipotesi, collegare eventi e scoprire che una risposta può modificare la domanda successiva. A un certo punto, questa idea è uscita dalla finzione. Ho iniziato a pensare che il ruolo di un investigatore potesse essere interessante anche in un prodotto. Non come metafora, ma come un modo diverso di concepire i sistemi di intelligence.

Immaginiamo un’azienda che stia per assumere un fornitore strategico. Prima di firmare il contratto, emerge una domanda semplice: esistono segnali pubblici che indichino che questo fornitore stia entrando in una situazione in grado di influenzare il nostro rapporto commerciale?

Rispondere a questa domanda può coinvolgere notizie, database pubblici, reclami, informazioni societarie e social network. Quando qualcosa sembra rilevante, sono necessarie nuove ricerche per comprenderne il contesto.

Ora immaginiamo di affidare questa domanda a un’architettura di intelligence. Essa ricerca il fornitore, le sue società collegate e gli eventi recenti. Trova una notizia rilevante, identifica una società collegata e apre una nuova linea di indagine. Poi trova informazioni contrastanti e cerca fonti più vicine al fatto originario. Un’ipotesi acquista forza, un’altra perde rilevanza e nasce una nuova domanda. A un certo punto, l’architettura può concludere che non esistono ancora evidenze sufficienti per raccomandare un’azione e mettere quella determinata indagine sotto monitoraggio.

Giorni dopo, emerge una nuova informazione. L’indagine torna in coda, ma non riparte da zero. Riprende dallo stato precedente, con le proprie ipotesi, evidenze, fonti e incertezze.

È questo comportamento che mi interessa. La stessa architettura potrebbe indagare un concorrente, un’opportunità di mercato, una tecnologia emergente, un potenziale cliente o un’ipotesi strategica. Il punto di partenza non è più soltanto l’entità che vogliamo monitorare, ma la domanda che dobbiamo investigare.

## Dal monitoraggio all’indagine

Esiste una differenza importante tra monitorare e investigare. Un sistema di monitoraggio può avvisare che un’azienda è stata menzionata in una notizia, ma la menzione, isolatamente, non dice necessariamente cosa sia successo, quale sia la sua rilevanza o se debba modificare una determinata decisione.

Nella sicurezza informatica, un SOC, Security Operations Center, esiste proprio per affrontare questo problema. Log, eventi di rete, alert degli endpoint e altre fonti producono continuamente segnali che, isolatamente, possono significare poco. Il SOC correla questi eventi, cerca pattern, analizza il contesto, valuta la gravità e, quando necessario, attiva una risposta. Un alert non è necessariamente un incidente. Il lavoro consiste nel comprendere cosa ci sia dietro.

La stessa logica può essere applicata alle informazioni pubbliche e alle domande di business. Un reclamo è un segnale. Dieci reclami simili in pochi giorni possono indicare qualcosa di diverso. Un video può ampliare l’esposizione, una pubblicazione può accelerare la diffusione e un articolo può trasformare un problema puntuale in un incidente in evoluzione. Il lavoro diventa comprendere come questi eventi siano collegati, quali ipotesi spieghino meglio ciò che sta accadendo e cosa debba ancora essere scoperto.

Questo cambia anche il ruolo della ricerca. Una ricerca tradizionale termina quando troviamo una risposta soddisfacente. In un’indagine, il risultato di una ricerca può determinare cosa debba essere cercato successivamente. Una notizia su una tecnologia può portare all’indagine sull’azienda che l’ha sviluppata. Un’acquisizione può generare domande su investitori, tecnologia o altri movimenti correlati. Un’informazione contrastante può richiedere una fonte primaria.

L’indagine evolve man mano che emergono nuove evidenze. Alcune linee vengono abbandonate, altre acquistano priorità e nascono nuove domande. L’architettura deve accompagnare questo processo, mantenendo il contesto di ciò che è già stato scoperto e decidendo quale debba essere il passo successivo. La differenza non sta nel fare in modo che un’IA ricerchi Internet. Sta nel fare in modo che un’architettura mantenga un’indagine.

Questo cambia anche il modo in cui pensiamo agli agenti. Invece di agenti permanentemente impegnati nell’esecuzione di ricerche, possiamo avere indagini permanentemente esistenti, ciascuna con il proprio stato e in attesa del momento appropriato per ricevere capacità di elaborazione.

## Uno scheduler per le indagini

Quando ho iniziato a pensare a questa architettura, un’analogia con i sistemi operativi mi è sembrata particolarmente utile. Un sistema operativo deve gestire una capacità di elaborazione limitata tra diversi processi. Tiene traccia dello stato di ciascun processo, definisce le priorità, ne interrompe alcuni, ne riprende altri e distribuisce il tempo di CPU in base a ciò che deve essere eseguito.

Un’architettura investigativa potrebbe funzionare in modo simile. Invece di avere un insieme di agenti che eseguono continuamente ricerche, avremmo un insieme di indagini persistenti, ciascuna con il proprio stato, priorità, obiettivo, livello di incertezza e budget. Alcune sarebbero attive, altre in attesa di nuove evidenze e altre praticamente concluse. Lo scheduler sarebbe responsabile di decidere quale riceva la successiva unità di capacità di elaborazione.

Immaginiamo decine o migliaia di indagini in corso simultaneamente. Una monitora un fornitore che non presenta alcun segnale rilevante da settimane. Un’altra indaga su un concorrente che ha annunciato recentemente un’acquisizione. Una terza monitora una tecnologia emergente. Una quarta cerca di comprendere una sequenza di reclami iniziata poche ore fa. Non avrebbe senso trattarle tutte allo stesso modo.

La prima potrebbe aver bisogno soltanto di una nuova verifica periodica. La seconda potrebbe richiedere un’indagine più approfondita. La terza potrebbe rimanere a bassa priorità fino alla comparsa di un segnale rilevante. La quarta, a seconda dell’impatto potenziale e della velocità degli eventi, potrebbe dover ricevere capacità immediatamente.

E anche il ciclo di elaborazione successivo dipende dallo stato dell’indagine. Un’indagine può iniziare cercando notizie recenti. Dopo aver trovato una società collegata, il ciclo successivo può essere dedicato alla comprensione di questa nuova entità. Se emerge un’informazione contrastante, potrebbe essere necessario cercare una fonte primaria. Se compare una modifica societaria, può avere senso indagare sugli azionisti di controllo. Se diverse fonti stanno riproducendo la stessa informazione, il passo successivo potrebbe essere identificarne l’origine.

Lo scheduler, quindi, non sta semplicemente chiedendo “quale ricerca eseguire adesso?”. Sta chiedendo “quale indagine merita attenzione adesso e qual è l’azione più utile che possiamo eseguire al suo interno?”.

Questo avvicina l’architettura a un sistema di processi concorrenti. Un’indagine può essere interrotta per lasciare spazio a un’altra più urgente. Può generare una sotto-indagine che inizia a competere per le risorse. Una linea può essere chiusa mentre un’altra continua. Un’indagine può rimanere bloccata in attesa di nuove evidenze e tornare in coda quando qualcosa cambia.

L’analogia con il sistema operativo aiuta anche a riflettere su un problema che spesso rimane nascosto quando parliamo di agenti. Non abbiamo bisogno di un agente dedicato per ogni problema. Così come un sistema operativo condivide la capacità di elaborazione tra i processi, un’architettura investigativa può condividere la capacità agentiva tra le indagini.

Questo modifica considerevolmente l’idea di automazione continua. Non stiamo creando migliaia di robot che fanno polling di Internet a intervalli fissi. Stiamo mantenendo indagini in stati diversi e decidendo dinamicamente quali meritino elaborazione, quanta elaborazione debbano ricevere e quale dovrebbe essere il passo successivo.

Al limite, lo scheduler diventa un elemento centrale dell’architettura. Non è soltanto un distributore di risorse. È il meccanismo che trasforma una collezione di indagini persistenti in un sistema capace di lavorare continuamente su di esse.

E questo ci porta a una domanda inevitabile: se investigare costa risorse, come decidere quando vale la pena continuare a investigare?

## Quanto vale la pena continuare a investigare?

Esiste un’altra questione che emerge quando prendiamo sul serio questa architettura: investigare ha dei costi. Ci sono chiamate alle API, ricerche, elaborazione, storage, inferenza, tempo degli agenti e, in alcuni casi, accesso a fonti a pagamento. Se il sistema potesse approfondire qualsiasi indagine indefinitamente, potrebbe produrre analisi sempre più complete, ma consumerebbe anche risorse senza che ciò generi necessariamente più valore.

Per questo, l’architettura non deve soltanto decidere cosa investigare. Deve decidere quanto sforzo valga la pena dedicare a ciascuna indagine.

Qui mi piace fare un gioco di parole con il ROI. Il ROI tradizionale chiede se valga la pena investire. In questo caso, possiamo chiederci se valga la pena investigare. La I diventa quella di Investigation.

Non deve necessariamente essere una formula rigida. Può essere un’euristica basata su alcune domande semplici: qual è la probabilità che una nuova informazione modifichi la nostra conclusione? Quale sarebbe l’impatto di questo cambiamento? Quanto costa ottenerla?

Se l’indagine possiede già evidenze consistenti, l’incertezza residua è ridotta e una nuova ricerca difficilmente modificherà la decisione, potrebbe essere meglio ridurre la frequenza, entrare in monitoraggio o semplicemente chiudere quella linea. Al contrario, se una singola informazione aggiuntiva potesse modificare una decisione importante, il ciclo successivo di indagine potrebbe avere un valore molto maggiore.

Questo crea l’idea di un budget investigativo. L’architettura può concentrare capacità dove esiste un maggiore potenziale informativo e ridurre lo sforzo dove il rendimento marginale è diminuito. Lo scheduler passa a considerare non soltanto urgenza e rischio, ma anche il valore potenziale del passo successivo.

E qui emerge una caratteristica interessante di questo problema: probabilmente non sapremo in anticipo quale sia la strategia migliore per tutte le situazioni. Alcune decisioni saranno inizialmente definite attraverso euristiche e successivamente adattate sulla base dei risultati osservati. L’architettura può imparare quali percorsi tendono a produrre evidenze rilevanti, quanto costano e in quale momento continuare a investigare smette di avere senso.

Alla fine, l’intelligenza non consiste soltanto nello scoprire di più. Consiste anche nel sapere quando abbiamo già scoperto abbastanza.

## L’indagine deve ricordare e imparare

Un’indagine non dovrebbe limitarsi ad accumulare documenti. Deve lavorare con ipotesi, preservare ciò che ha già scoperto e incorporare il contesto di chi sta investigando.

Supponiamo che una sequenza di critiche pubbliche contro un’azienda stia crescendo. Una possibilità è che esista un problema operativo reale. Un’altra è che il problema sia circoscritto e venga amplificato. Un’altra ancora è che esista una campagna coordinata. Oppure che eventi diversi vengano raggruppati perché sembrano simili.

L’architettura non dovrebbe scegliere immediatamente una narrativa e cercare soltanto informazioni che la confermino. Dovrebbe mantenere ipotesi concorrenti e cercare evidenze che aiutino a distinguerle.

Questo richiede anche di separare ciò che è stato trovato da ciò che è stato inferito. Una fonte afferma un determinato fatto. Questa è un’evidenza. La conclusione che questo fatto rappresenti uno specifico rischio per l’organizzazione è un’inferenza. Allo stesso modo, una relazione tra due eventi può essere rilevante senza dimostrare che uno abbia causato l’altro.

L’indagine deve considerare anche l’indipendenza delle fonti. Dieci siti che ripetono la stessa notizia non rappresentano necessariamente dieci evidenze. È necessario comprendere l’origine dell’informazione, identificare le duplicazioni e, quando possibile, cercare la fonte più vicina al fatto.

E c’è una limitazione che dovrebbe essere presente in qualsiasi conclusione: non trovare informazioni non significa dimostrare che qualcosa non esista. Una conclusione responsabile sarebbe: nessun segnale rilevante è stato trovato all’interno del perimetro delle fonti analizzate. La differenza tra certezza e assenza di evidenza è piccola nella frase ed enorme nella pratica.

Ma questo rigore perde valore se ogni indagine ricomincia da zero. Perché esista continuità, l’architettura deve preservare ciò che stava investigando, quali ipotesi sono state formulate, quali evidenze sono state trovate, quali fonti sono state considerate, quali ipotesi sono state scartate, quali dubbi sono rimasti aperti e quale è stata l’ultima conclusione. Non basta conservare la cronologia delle conversazioni con un modello. È necessario mantenere lo stato dell’indagine.

Questo stato deve inoltre convivere con la conoscenza specifica dell’organizzazione. Un’azienda può considerare un determinato fornitore critico mentre un’altra può considerarlo facilmente sostituibile. Un’informazione che rappresenta un rischio rilevante in un contesto può essere irrilevante in un altro. La stessa entità può avere relazioni completamente diverse con organizzazioni differenti.

Per questo, l’architettura deve costruire un contesto proprio per ciascuna organizzazione, incorporando entità, relazioni, definizioni, policy, fonti preferenziali, classificazioni, decisioni precedenti e, soprattutto, correzioni effettuate dalle persone.

Questo feedback umano entra a far parte del ciclo dell’indagine. Un utente può correggere un’associazione tra aziende, contestare un’inferenza, confermare una relazione, scartare un’ipotesi o indicare che una determinata evidenza è più rilevante di quanto il sistema abbia considerato. Queste correzioni non dovrebbero scomparire quando quell’indagine termina. Possono modificare il contesto utilizzato nelle successive.

Questo non significa necessariamente addestrare nuovamente il modello. Esiste una differenza tra il modello che apprende e l’architettura che apprende. Il modello può rimanere esattamente lo stesso mentre l’architettura accumula conoscenza sull’organizzazione, incorpora correzioni, identifica quali fonti siano più utili per determinati problemi e adatta le proprie euristiche.

In questo senso, l’architettura non impara soltanto sul mondo. Impara dall’organizzazione e su come investigare il mondo.

## L’autonomia richiede governance

È allettante chiamare tutto questo investigazione autonoma, ma esiste una distinzione importante. L’autonomia che mi interessa riguarda principalmente la conduzione dell’indagine.

Il sistema può decidere quale fonte consultare, quale ipotesi approfondire, quando creare una sotto-indagine, quando ridurre lo sforzo, quando cercare ulteriori evidenze e quando tornare a un’indagine che era ferma.

Questo non significa che debba decidere autonomamente una questione giuridica, interrompere un rapporto commerciale o rifiutare un fornitore. Quanto maggiore è l’impatto della decisione, tanto maggiore deve essere il livello di governance richiesto.

Un’architettura aziendale deve consentire diversi livelli di autonomia, dall’osservazione e dall’allerta fino alla raccomandazione di azioni che richiedano approvazione umana. In alcuni contesti altamente controllati, determinate azioni potrebbero eventualmente essere automatizzate. In altri, ciò sarebbe inappropriato.

Questa autonomia crea anche un’altra esigenza: l’architettura deve rappresentare le proprie incertezze ed essere in grado di spiegare il percorso seguito.

Quanto più l’indagine influenza una decisione, tanto più diventa importante poter ricostruire come sia stata raggiunta quella conclusione. Un log tecnico può dire che un agente ha eseguito una ricerca alle 14:32. Questo non spiega l’indagine.

Sarebbe necessario qualcosa di più vicino a una traccia investigativa: quale fosse la domanda originale, quali ipotesi esistessero, quali fonti siano state consultate, quali evidenze siano state considerate o scartate, quale contesto dell’organizzazione sia stato utilizzato, quali conclusioni intermedie siano state prodotte, perché sia stata effettuata una determinata nuova ricerca e come tutto questo abbia portato alla raccomandazione finale.

Se un utente ha corretto un’informazione, anche questa correzione dovrebbe far parte della storia. Se una raccomandazione è stata accettata e successivamente si è dimostrata inadeguata, questo risultato dovrebbe tornare nel ciclo di apprendimento dell’architettura.

L’auditabilità, in questo contesto, non è soltanto una preoccupazione di compliance. È parte della qualità stessa dell’intelligence. Quanto più autonomia diamo al sistema, tanto più dobbiamo essere in grado di comprendere cosa abbia fatto, perché lo abbia fatto e su quali evidenze si sia basato.

Un’indagine che non riesce a spiegare il proprio percorso è molto più difficile da considerare affidabile.

## Il mercato possiede già molti di questi componenti

È importante mettere questa idea in prospettiva. Il mercato internazionale possiede già piattaforme mature di competitive intelligence e market intelligence, monitoraggio, ricerca assistita dall’IA e analisi di fonti esterne. Nel 2026, per esempio, Gartner considera già le Competitive and Market Intelligence Platforms come una categoria specifica di valutazione, comprendendo capacità come aggregazione delle fonti, validazione, ricerca e analisi con IA, knowledge management e integrazione aziendale.

Esistono inoltre soluzioni che lavorano con grandi volumi di fonti, monitoraggio continuo e generazione di insight su concorrenti, mercati e altre entità strategiche. In Brasile esistono aziende che operano nell’intelligence competitiva, nel monitoraggio, nella market intelligence, nella reputazione e nell’analisi delle informazioni. Pertanto, non vedo una novità in ciascuno di questi componenti presi singolarmente.

La questione che mi sembra più interessante è un’altra: come riorganizzare queste capacità intorno all’indagine come unità principale? Invece di partire dall’entità e chiedere cosa sia successo a essa, propongo che l’architettura parta dalla domanda e, a partire da essa, scopra quali entità, fonti, eventi e relazioni debbano essere investigati. La ricerca smette di essere un’esecuzione isolata che termina in un report e diventa parte di un’indagine che evolve man mano che emergono nuove evidenze. Il report smette di essere il punto finale e la decisione diventa uno stato che può essere rivisitato ogni volta che nuove informazioni possono modificare ciò che sappiamo.

È in questa composizione che vedo spazio per un’architettura diversa. Non per sostituire le capacità che già esistono, ma per collegarle in un processo investigativo persistente, capace di adattare la propria profondità, prioritizzare l’uso delle risorse, incorporare la conoscenza organizzativa e apprendere dal feedback.

Vedo inoltre spazio per adattare questa architettura al contesto brasiliano, dove fonti pubbliche, strutture societarie, ambiente normativo, caratteristiche del mercato e necessità di governance possono richiedere strategie investigative specifiche. In questo caso, l’adattamento al contesto non sarebbe soltanto un livello di localizzazione, ma parte dell’intelligence stessa del sistema.

## Dalla raccolta di informazioni all’intelligence continua

Quando queste idee vengono riunite, l’architettura smette di sembrare soltanto un sofisticato meccanismo di ricerca. L’informazione diventa il carburante di un’indagine persistente, capace di formulare domande, seguire ipotesi, preservare il contesto, decidere i passi successivi e tornare al problema quando emergono nuove evidenze. L’IA partecipa a questo processo, ma è l’architettura a fornire continuità, memoria, contesto e governance.

Questo modifica la domanda centrale. Invece di iniziare da “quale modello useremo?”, forse è più interessante chiedere “come organizzeremo il processo attraverso il quale il sistema investiga?”. Alcune risposte saranno inizialmente definite tramite euristiche e altre scoperte nella pratica. Nel tempo, l’architettura può imparare quali fonti funzionano meglio per determinati problemi, quali percorsi producono evidenze rilevanti e quando continuare a investigare smette di generare valore. Non si tratta soltanto di fare in modo che il modello risponda meglio, ma di fare in modo che il sistema investighi meglio.

Se osserviamo questa evoluzione, prima abbiamo costruito sistemi per raccogliere informazioni. Poi sistemi per monitorarle. Più recentemente, sistemi capaci di riassumere e analizzare grandi volumi di contenuti. Il passo successivo potrebbe essere un’architettura nella quale l’informazione smette di essere il prodotto finale e passa ad alimentare un processo continuo di indagine.

Esistono ancora molte questioni da definire riguardo a priorità, costi, qualità, euristiche e autonomia. Più che problemi da risolvere in un unico modo, queste variabili possono diventare parte della configurazione stessa del prodotto, permettendo di adattare il comportamento dell’architettura al contesto, al rischio e agli obiettivi di ciascuna organizzazione. La differenza tra uno strumento di ricerca e un’intelligence continua potrebbe trovarsi proprio qui: non nel trovare più informazioni o nel produrre riassunti migliori, ma nel costruire un sistema capace di investigare domande, imparare da ciò che ha scoperto e tornare al problema quando il mondo cambia.
