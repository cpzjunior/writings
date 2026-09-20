# Come impedire che il tuo MVP diventi un Leviatano

_Tra la complessità che anticipa il futuro e la semplicità che impedisce l'apprendimento._

**Riassunto:** Un MVP non è il prodotto più piccolo che riusciamo a mettere online, ma il più piccolo insieme necessario per testare un'ipotesi e imparare qualcosa di rilevante dal risultato. Il rischio sta tanto nel costruire troppo, anticipando problemi che forse non esisteranno mai, quanto nel costruire troppo poco e compromettere la validità dell'apprendimento. Per questo, la complessità deve essere proporzionata a ciò che sappiamo, ai rischi che contano realmente e alle domande a cui dobbiamo rispondere in quel momento. L'MVP può crescere man mano che impariamo, ma questa crescita deve essere una conseguenza delle conoscenze acquisite, non del tentativo di anticipare il futuro.

---

Ho visto molte persone con buone idee incontrare difficoltà nel trasformarle in realtà. Ho affrontato parte di questo problema in “[Prima di trasformare un'idea in realtà, bisogna metterla su carta](https://cpzjunior.substack.com/p/antes-de-tirar-uma-ideia-do-papel)“, ma esiste una difficoltà che inizia proprio quando l'idea smette di essere soltanto un'idea e comincia a essere costruita: mantenere piccolo l'MVP senza comprometterne la fattibilità.

L'intenzione iniziale è solitamente semplice. Costruire quanto basta per mettere alla prova un'ipotesi e imparare dal risultato. Il problema è che, man mano che la costruzione avanza, emergono buone ragioni per ampliare l'ambito. Una funzionalità sembra necessaria, un'eccezione sembra importante, una decisione architetturale può essere generalizzata, una preoccupazione per la scalabilità futura sembra prudente. Poco a poco, ciò che avrebbe dovuto servire a testare un'ipotesi comincia a incorporare risposte a problemi che ancora non sappiamo nemmeno se avremo.

Per facilitare la registrazione degli utenti, implementeremo diversi meccanismi di autenticazione, come SSO e OAuth. Poiché il sistema deve considerare diversi livelli, profili e regole di accesso, avremo bisogno di un modello di autorizzazioni multidimensionale, nello stile di piattaforme aziendali come Salesforce. Poiché avremo un sistema di abbonamenti, costruiremo un ledger basato su blockchain e un sistema di geolocalizzazione per l'antifrode. Per garantire la disponibilità totale, adotteremo un'architettura multicloud su più AZ. Per anticipare un'eventuale espansione in America Latina e in Asia, avremo anche il supporto per più località e configurazioni regionali. Quando ce ne accorgiamo, abbiamo iniziato cercando di validare un'ipotesi di prodotto e stiamo progettando una piattaforma distribuita globalmente per risolvere problemi ipotetici prima ancora di sapere se il prodotto risolve il problema per cui è stato creato.

È qui che nasce il paragone con il Leviatano. Nella tradizione biblica, il Leviatano è un mostro associato al mare e al caos, una creatura che sfugge al dominio umano. Il paragone è quasi letterale: l'MVP inizia come qualcosa di piccolo e controllabile, ma può accumulare funzionalità, dipendenze, regole ed eccezioni fino a trasformarsi in un mostro la cui complessità non risponde più facilmente all'intenzione che ha dato origine al prodotto.

Ma esiste una trappola anche nella direzione opposta. Nel tentativo di mantenere l'MVP sotto controllo, possiamo tagliare proprio gli elementi necessari per testare l'ipotesi. Il risultato è piccolo, ma non è più sufficientemente fattibile da dirci se siamo di fronte a una soluzione adeguata.

È in questa tensione, tra costruire troppo e costruire troppo poco, che inizia la discussione su ciò che deve davvero rientrare in un MVP.

## L'MVP non è un prodotto piccolo

L'MVP viene solitamente inteso come un prodotto con poche funzionalità. È una definizione intuitiva, ma insufficiente. Il “minimo” non sta nella quantità di software che riusciamo a costruire, ma nel più piccolo insieme necessario per mettere alla prova un'ipotesi rilevante in modo sufficientemente affidabile.

Questa distinzione cambia il modo in cui decidiamo cosa entra nel prodotto. La domanda non dovrebbe essere “qual è la quantità minima di codice che riusciamo a mettere in produzione?”, ma “qual è il minimo investimento capace di insegnarci qualcosa di rilevante sul prodotto?”. La seconda domanda ci obbliga a considerare non solo ciò che verrà costruito, ma anche la qualità dell'apprendimento che sarà in grado di produrre.

Una funzionalità può essere semplice da implementare e tuttavia essere indispensabile per testare l'ipotesi. Un'altra può richiedere poco sforzo e non aggiungere praticamente nulla a ciò che dobbiamo scoprire. Lo sforzo di sviluppo, quindi, non è un buon indicatore isolato di rilevanza. Ciò che conta è il contributo di quella parte all'esperimento.

È per questo che un MVP piccolo può essere inadeguato. Rimuovendo una parte essenziale dell'esperienza, possiamo mettere qualcosa online rapidamente, ma produrre un risultato che non risponde alla domanda originale. In questo caso, riduciamo il prodotto senza necessariamente ridurre l'incertezza. Costruiamo meno, ma impariamo anche meno.

Lo stesso ragionamento vale per l'eccesso. Una soluzione può essere tecnicamente sofisticata e funzionare perfettamente, ma incorporare capacità che non sono ancora necessarie per testare la tesi. Il problema, in questo caso, non sta necessariamente nella qualità della soluzione, ma nel momento in cui scegliamo di costruirla. Stiamo investendo per rispondere a domande che il prodotto non ci ha ancora costretto a porci.

La dimensione dell'MVP, quindi, non è una misura assoluta. Deve essere proporzionata a ciò che vogliamo scoprire in quel momento.

### Come nasce il Leviatano

La crescita dell'MVP raramente avviene a causa di una grande decisione. Di solito nasce dalla successione di piccole decisioni che, prese singolarmente, sembrano perfettamente difendibili. Un'integrazione sembra necessaria, un'eccezione sembra semplice da gestire, una struttura più generica sembra evitare lavoro duplicato, una preoccupazione per la scalabilità sembra prudente. Una configurazione aggiuntiva sembra poco costosa. Una funzionalità richiesta da un utente sembra troppo importante per essere esclusa.

È in questo contesto che compare il noto “visto che stiamo facendo questo, possiamo fare anche quello”. A ogni decisione, l'ambito si sposta un po'. Poiché nessun cambiamento sembra sufficiente a giustificare un'interruzione, la somma passa inosservata finché il prodotto non sta già rispondendo a problemi che non facevano parte della domanda originale.

Il punto più insidioso è che il costo di una decisione raramente termina con la sua implementazione. Una nuova funzionalità comincia a richiedere test, monitoraggio, documentazione, supporto e manutenzione. Può introdurre dipendenze, nuovi stati, regole di business e percorsi di esecuzione che prima non esistevano. Può anche limitare le decisioni future, rendendo più costoso cambiare direzione quando emergeranno nuove informazioni.

Per questo, il costo di una funzionalità non è soltanto lo sforzo necessario per portarla in produzione. È anche tutto ciò che comincia a esistere dopo che entra nel sistema.

È così che l'ambito può sfuggire all'intenzione originale senza che ci sia un errore evidente da indicare. Ogni decisione locale può avere senso, mentre il risultato cumulativo smette di averne. Il Leviatano non nasce necessariamente da una scelta assurda, ma dalla somma di scelte ragionevoli che, insieme, producono una complessità che nessuno intendeva costruire.

## Il problema di cercare di risolvere il mondo

Esiste una forma particolarmente pericolosa di anticipazione: cercare di costruire, fin dall'inizio, la soluzione a tutti i problemi che il prodotto potrebbe avere in futuro.

Quando la tesi è ancora incerta, iniziamo a immaginare diversi profili di utenti, modelli di business, grandi volumi di dati, molteplici integrazioni, esigenze di internazionalizzazione, diversi livelli di autorizzazione e scenari di scalabilità. Ogni preoccupazione può essere legittima singolarmente. Il problema emerge quando tutte cominciano a influenzare la prima versione del prodotto.

È comprensibile. Chi costruisce sistemi sa che alcune decisioni sono difficili da modificare in seguito e che determinate scelte possono generare debito tecnico. Sa anche che correggere un'architettura inadeguata più avanti può essere molto più costoso che prendere una buona decisione fin dall'inizio. Il rischio sta nel trasformare questa preoccupazione legittima nel tentativo di prevedere l'intero prodotto prima ancora di sapere se è, di fatto, una soluzione adeguata e fattibile.

È come assumere il ruolo di Atlante prima di sapere se ci sarà un mondo da sostenere: ci facciamo carico in anticipo del peso di tutti i futuri possibili, senza sapere quali di essi esisteranno davvero.

C'è un'inversione di prospettiva. Invece di far evolvere la soluzione a partire da ciò che impariamo sul problema, iniziamo a costruire una soluzione per un futuro ipotetico. Cominciamo a prendere decisioni sulla base di utenti che forse esisteranno, volumi che forse verranno raggiunti, mercati che forse saranno esplorati e requisiti che forse non appariranno mai.

Questo futuro ha un costo nel presente. E, nella fase iniziale, potremmo non sapere nemmeno se ci arriveremo.

L'architettura deve gestire rischi reali, non tutte le possibilità immaginabili. Lo stesso vale per il prodotto. Una decisione merita un investimento proporzionato all'importanza e alla probabilità del problema che intende risolvere. Preparare tutto per una scala che forse non esisterà significa pagare in anticipo per un futuro che non è ancora stato validato.

## Anche la complessità può essere necessaria

Questo non significa che ogni complessità sia un segnale di eccesso. Esistono prodotti in cui sicurezza, audit, resilienza, osservabilità, controllo degli accessi o requisiti operativi fanno parte della soluzione stessa. In questi casi, eliminare la complessità non significa necessariamente semplificare il prodotto. Può significare eliminare una proprietà necessaria affinché funzioni correttamente.

In determinati contesti, semplificare troppo il sistema può essere proprio la decisione irresponsabile. Un MVP che movimenta denaro, tratta dati sensibili o partecipa a processi critici non può usare la sperimentazione come giustificazione per ignorare proprietà essenziali del dominio. Il fatto che stiamo validando un'ipotesi non sospende i rischi che già esistono.

Esiste anche una differenza tra la complessità percepita dall'utente e la complessità necessaria nel sistema. Un'esperienza può essere semplice in superficie e dipendere da un'infrastruttura piuttosto sofisticata per funzionare in modo sicuro, resiliente e affidabile. L'obiettivo, quindi, non è eliminare la complessità, ma evitare una complessità che non abbia una ragione concreta per esistere in quel momento.

Per questo, la domanda non dovrebbe essere semplicemente “come rendere il sistema più semplice?”, ma “quale complessità è necessaria per questa fase del prodotto?”. La risposta dipende tanto dall'ipotesi che vogliamo validare quanto dai rischi che non possiamo accettare.

Questa distinzione aiuta anche a evitare una falsa opposizione tra prodotto e ingegneria. Il prodotto può cercare di ridurre l'ambito per validare un'ipotesi, mentre l'ingegneria può cercare di ridurre un rischio tecnico rilevante o evitare una decisione difficile da invertire. Entrambe le preoccupazioni sono legittime. Il lavoro dell'architettura consiste proprio nel valutare questi trade-off e trovare una soluzione proporzionata alla fase del prodotto, senza trasformare la semplicità o la sofisticazione in principi assoluti.

## Costruire meno può essere anche un errore

La reazione all'eccesso è spesso il taglio. Eliminiamo funzionalità, semplifichiamo i flussi e riduciamo l'ambito fino ad arrivare a qualcosa che sembri abbastanza piccolo da essere chiamato MVP. Il problema è che ridurre il prodotto non significa necessariamente aumentare la qualità dell'esperimento.

Esiste un'importante differenza tra ridurre ciò che verrà costruito e ridurre la capacità di imparare da ciò che è stato costruito. Un'ipotesi può dipendere da determinati elementi dell'esperienza per essere testata in modo minimamente rappresentativo. Rimuovere proprio questi elementi può produrre un risultato apparentemente oggettivo, ma che risponde a una domanda diversa da quella che intendevamo porci.

Possiamo, per esempio, concludere che una soluzione non funziona quando, in realtà, abbiamo testato una versione così semplificata da aver smesso di rappresentare la proposta di valore originale. In questo caso, abbiamo costruito meno, ma abbiamo anche imparato meno.

Per questo, l'MVP non serve soltanto a mettere qualcosa in produzione. Deve produrre un risultato utile per la decisione successiva. Quanto più la soluzione viene semplificata, tanto più importante diventa capire cosa è stato preservato e cosa è stato rimosso. Una semplificazione che elimina proprio l'elemento responsabile del collegamento tra il problema e la soluzione può rendere l'esperimento economico, ma poco informativo.

In alcuni casi, inoltre, il miglior MVP potrebbe non essere nemmeno software. Un prototipo, un'operazione manuale o un pilota limitato possono rispondere alla domanda con meno investimento e meno complessità. Se possiamo testare l'ipotesi senza costruire l'intero sistema, forse questo è il modo più appropriato per iniziare.

L'obiettivo non è costruire il meno possibile. È costruire soltanto ciò che è necessario affinché il risultato ci dica qualcosa che valga la pena sapere.

## L'MVP deve essere diagnosticabile

Questo è forse uno dei criteri più importanti per decidere cosa entra in una prima versione: quando l'esperimento sarà terminato, dobbiamo riuscire a interpretare ciò che è successo.

Un MVP può fallire per diversi motivi. L'ipotesi sul problema può essere errata. La soluzione può non essere adeguata. L'esperienza può non funzionare come previsto. Il prezzo può essere sbagliato. Il canale di acquisizione può non funzionare. La tecnologia può imporre qualche limitazione. L'operazione può essere impraticabile. Il risultato osservato è conseguenza di una combinazione di queste variabili, e non è sempre possibile determinare con precisione quale di esse ne sia stata responsabile.

Quanto più cose cambiamo simultaneamente, tanto più difficile diventa interpretare il risultato. Un prodotto può essere stato rifiutato perché la proposta di valore non aveva senso, perché l'esperienza era scadente o semplicemente perché una limitazione dell'implementazione ha impedito all'utente di percepire il valore della soluzione. Senza una certa attenzione nella composizione dell'MVP, un risultato negativo può dire molto poco sull'ipotesi che intendevamo testare.

Questo non significa che ogni MVP debba essere un esperimento controllato o che sia possibile isolare perfettamente ogni variabile. I prodotti reali raramente offrono questo livello di controllo. Significa soltanto che dobbiamo preservare una certa capacità di distinguere ciò che stiamo imparando. Esiste una differenza tra accettare l'incertezza intrinseca del prodotto e introdurre così tanta complessità nell'esperimento che il risultato stesso diventa difficile da interpretare.

Un MVP, quindi, deve essere più che eseguibile. Deve essere diagnosticabile. Il suo risultato deve essere in grado di orientare la decisione successiva, sia per correggere la soluzione, riformulare l'ipotesi o semplicemente abbandonare una direzione che non si è dimostrata promettente.

## Anche il minimo si sposta

C'è un altro aspetto importante: l'MVP non è una categoria permanente del prodotto. La tesi di un prodotto può cambiare man mano che emergono nuove evidenze. Un'ipotesi iniziale può essere raffinata, scartata o sostituita da un'altra più sofisticata. Anche le domande cambiano. Di conseguenza, ciò che era sufficiente per testare un'ipotesi in un determinato momento può non essere più sufficiente per rispondere alla domanda successiva.

Una soluzione semplice può essere adeguata per scoprire se un determinato problema esiste realmente. Successivamente, potrebbe essere necessario capire se la soluzione proposta è sufficientemente preziosa da essere adottata. Più avanti, potrebbe essere necessario valutare la retention, il comportamento su larga scala, l'integrazione con altri sistemi o qualche aspetto operativo che non faceva parte della domanda iniziale.

In questo processo, il concetto di minimo si sposta. Una tesi più sofisticata può richiedere una soluzione più sofisticata. Questo non significa che l'MVP abbia fallito e sia diventato un prodotto gonfio. Può significare semplicemente che abbiamo imparato abbastanza per porci domande migliori e, quindi, abbiamo bisogno di una soluzione capace di rispondervi.

La questione sta nella direzione di questo movimento. La complessità deve accompagnare l'evoluzione della tesi, non cercare di anticiparla. Il prodotto può crescere man mano che aumenta la conoscenza del problema, degli utenti e della soluzione stessa. Ciò che non ha senso è costruire in anticipo ciò che avrebbe senso soltanto dopo aver imparato.

Il problema non è che l'MVP cresca. Il problema è che cresca prima di sapere perché deve crescere.

## Quando l'MVP comincia a diventare un Leviatano

Il segnale più preoccupante forse non è il numero di funzionalità, la dimensione del codice o la quantità di componenti architetturali. È quando la complessità smette di essere chiaramente correlata allo scopo della prima versione.

A un certo punto, può diventare difficile spiegare perché determinate parti del prodotto esistono, a quali domande aiutano a rispondere o quali rischi concreti ne abbiano giustificato l'inclusione. Le decisioni cominciano a essere prese per scenari che ancora non esistono, le eccezioni iniziano a plasmare il comportamento principale e una parte crescente dello sforzo viene assorbita dalla complessità stessa del sistema.

Questo è il punto in cui vale la pena tornare alla domanda che ha dato origine all'MVP: cosa stiamo cercando di scoprire?

La risposta impedisce anche il movimento contrario. Non tutto ciò che può essere rimosso dovrebbe essere rimosso. Una funzionalità può essere indispensabile affinché l'ipotesi venga testata in modo valido, anche se sembra aumentare le dimensioni della prima versione. L'obiettivo non è mai stato costruire il sistema più piccolo possibile, ma una soluzione proporzionata a ciò che sappiamo, a ciò che dobbiamo ancora scoprire e ai rischi che contano davvero.

È per questo che il Leviatano non è semplicemente un MVP grande. È l'MVP che ha perso il controllo sulla propria complessità.

Una prima versione non deve essere una versione ridotta di tutto ciò che immaginiamo di costruire in futuro. Deve essere una risposta deliberatamente limitata alle domande che abbiamo ora. Man mano che impariamo, la tesi può cambiare, possono emergere nuove domande e la soluzione può aver bisogno di crescere. In questo caso, la crescita smette di essere anticipazione e diventa conseguenza della conoscenza acquisita.

Il pericolo inizia quando facciamo il percorso inverso: costruiamo prima e aspettiamo che il futuro ci dia una ragione per tutto ciò che abbiamo costruito. In questo scenario, ciò che avrebbe dovuto aiutarci a scoprire la strada può finire per creare una strada che avremo difficoltà ad abbandonare.
