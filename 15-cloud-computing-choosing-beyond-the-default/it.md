# Cloud Computing: scegliendo oltre il default

_Una mappa dei principali cloud, dei loro punti di forza, delle equivalenze e dei trade-off tra semplicità, portabilità, costo e resilienza._

**Riassunto:** Sostengo che scegliere un cloud non dovrebbe essere una decisione basata sulla familiarità o sulle dimensioni del provider, ma sulle caratteristiche concrete di ciascun workload. Le equivalenze tra piattaforme aiutano a orientare il confronto, ma non eliminano le differenze di costo, operatività, servizi, hardware, compliance e lock-in. Single-cloud e multi-cloud non sono nemmeno posizioni ideologiche: ciascuna porta con sé costi, benefici e rischi che devono essere valutati insieme alle dipendenze reali dell'architettura. Alla fine, la scelta migliore è quella che equilibra ciò che il workload richiede con il costo di implementare, gestire ed eventualmente modificare quell'architettura.

---

Storicamente, ho sempre avuto una preferenza piuttosto chiara per AWS. Non necessariamente perché considero AWS il miglior cloud in qualsiasi scenario, ma perché è stata la piattaforma con cui ho avuto maggiore contatto e familiarità. Nel corso del tempo, mi sono abituato ai suoi servizi, alla sua organizzazione, alla sua documentazione e al suo ecosistema. E c'è una conseguenza piuttosto naturale in questo: quando conosci bene una tecnologia, tende a sembrare la scelta più semplice per il problema successivo.

Negli ultimi anni, però, ho iniziato a guardare con maggiore attenzione agli altri cloud. Uno dei motivi principali è stato piuttosto pragmatico: le GPU. Man mano che i progetti di intelligenza artificiale hanno iniziato a richiedere una capacità computazionale sempre maggiore, ho iniziato a rendermi conto che la familiarità con una piattaforma non poteva più essere il criterio principale per decidere dove eseguire un workload. Prezzo, disponibilità delle GPU, localizzazione delle risorse, capacità di espansione e persino i modelli contrattuali hanno iniziato ad avere un peso molto maggiore nella decisione.

Questo mi ha portato a guardare nuovamente a un mercato che, sebbene venga spesso riassunto nella competizione tra AWS, Azure e Google Cloud, è molto più ampio. Esistono cloud specializzati, provider regionali, piattaforme con proposte deliberatamente più semplici e aziende che riescono a essere estremamente competitive in determinati tipi di workload proprio perché non cercano di offrire tutto a tutti.

L'obiettivo di questo testo non è fare un confronto esaustivo tra centinaia di servizi o dichiarare quale sia il miglior cloud. L'idea è costruire una mappa sufficientemente ampia per capire chi sono i principali player, quali sono i loro punti di forza, quali servizi hanno equivalenti tra loro e, soprattutto, in quali situazioni vale la pena uscire dal percorso più ovvio.

Scegliere un cloud per familiarità è perfettamente ragionevole. Scegliere un cloud senza conoscere le alternative, no.

## La mappa dei cloud

Quando parliamo di cloud computing, tre nomi compaiono inevitabilmente per primi: AWS, Microsoft Azure e Google Cloud. Continuano a essere le principali piattaforme generaliste del mercato del public cloud, con un'ampiezza che va ben oltre macchine virtuali e storage. Computing, database, reti, container, Kubernetes, serverless, analytics, intelligenza artificiale, sicurezza, osservabilità e una quantità sempre maggiore di servizi gestiti fanno parte di questo ecosistema.

C'è una ragione per cui queste tre dominano la conversazione. Non sono soltanto provider di infrastruttura, ma piattaforme complete. Un'applicazione può utilizzare computing, storage, database, code, identità, osservabilità, gestione dei segreti, CDN e servizi di intelligenza artificiale dello stesso provider, tutti integrati tra loro. Questa integrazione è uno dei grandi vantaggi delle hyperscaler e anche uno dei fattori che rendono più complessa un'eventuale migrazione.

Ma il mercato del cloud non è una gerarchia semplice. Esistono provider con proposte differenti e, a seconda del workload, un provider che sembra piccolo rispetto a una hyperscaler può essere un'opzione molto più interessante.

Oracle Cloud Infrastructure, IBM Cloud, Alibaba Cloud e Tencent Cloud sono esempi di provider che possiedono posizioni particolarmente forti in determinati mercati ed ecosistemi. OCI ha una relazione naturale con gli ambienti che dipendono fortemente da Oracle. IBM mantiene una presenza importante nelle grandi organizzazioni e nell'ecosistema Red Hat. Alibaba e Tencent hanno una rilevanza molto maggiore quando consideriamo la Cina e altri mercati asiatici. In questi casi, la domanda non è necessariamente quale provider offra più servizi, ma quale abbia maggiore aderenza al problema che deve essere risolto.

Esiste inoltre un gruppo di provider che adotta una proposta deliberatamente più semplice. DigitalOcean, Hetzner, OVHcloud, Scaleway e Akamai, attraverso Linode, possono essere interessanti quando l'obiettivo è ottenere computing, storage e rete senza dipendere necessariamente dall'enorme quantità di servizi gestiti offerti dalle hyperscaler. Per determinati workload, questa semplicità può significare una minore complessità operativa e costi più prevedibili.

L'intelligenza artificiale, però, sta modificando questo scenario. La crescita della domanda di GPU ha creato un mercato in cui disponibilità e costo dell'hardware possono essere più importanti della quantità di servizi offerti dalla piattaforma. Un'applicazione di IA che necessita di centinaia di GPU non beneficia necessariamente del provider che offre il catalogo più ampio di servizi. In questo scenario, prezzo per GPU, disponibilità, architettura degli acceleratori, interconnessione tra macchine, capacità di scalare e localizzazione delle risorse possono essere i fattori determinanti.

Questo ha aperto spazio a provider specializzati. CoreWeave è uno degli esempi più conosciuti, avendo costruito la propria piattaforma intorno ai workload GPU e all'intelligenza artificiale. Esistono anche altri provider specializzati in GPU e high-performance computing che possono essere molto competitivi per questo tipo di carico, pur senza offrire una piattaforma generalista paragonabile alle hyperscaler.

Allo stesso tempo, le hyperscaler stanno investendo pesantemente in hardware specializzato, modelli fondazionali, servizi gestiti di IA e integrazione di queste risorse con il resto delle loro piattaforme. Questo crea una competizione diversa da quella che esisteva nel mercato tradizionale del cloud. Il vantaggio può trovarsi tanto nell'infrastruttura quanto nell'ecosistema costruito attorno a essa.

In pratica, questo significa che non esiste un unico profilo di cloud adatto a tutti i workload. Le piattaforme generaliste continuano a essere estremamente rilevanti, ma i provider specializzati possono essere più competitivi in determinate situazioni. Un'azienda può essere un'ottima scelta per l'infrastruttura tradizionale e una scelta pessima per il training di modelli. Un'altra può essere poco interessante come piattaforma principale, ma estremamente competitiva per uno specifico workload GPU.

Questo è proprio uno dei motivi per cui vale la pena guardare oltre il default. Il cloud scelto per un'applicazione non deve necessariamente essere lo stesso scelto per tutti i workload dell'organizzazione. Un provider che storicamente sembra piccolo o secondario può diventare un'alternativa rilevante quando cambiamo la domanda da “qual è il miglior cloud?” a “qual è la migliore infrastruttura per questo workload?”.

Alla fine, AWS, Azure e Google Cloud continuano a essere le principali piattaforme generaliste, ma dimensioni e quantità di servizi non sono gli unici criteri rilevanti. Il mercato sta diventando più specializzato e l'intelligenza artificiale sta accelerando questo processo. Conoscere questo scenario significa capire dove le grandi piattaforme sono più forti, dove i provider più piccoli riescono a competere e in quali situazioni ha senso considerare alternative che normalmente non comparirebbero nemmeno nella prima ricerca.

## Equivalenza non significa uguaglianza

Una delle prime cose che si nota studiando diversi cloud è che i grandi provider possiedono equivalenti per buona parte dei servizi fondamentali. A livello di computing, possiamo pensare a EC2 su AWS, Virtual Machines su Azure e Compute Engine su Google Cloud. Per l'object storage abbiamo S3, Blob Storage e Cloud Storage. Per le reti virtuali, VPC su AWS, Virtual Network su Azure e VPC su Google Cloud. Per Kubernetes gestito, EKS, AKS e GKE. Per il container registry, ECR, Azure Container Registry e Artifact Registry. Per il load balancing, Elastic Load Balancing, Azure Load Balancer e Cloud Load Balancing. Per la CDN, CloudFront, Azure Front Door e Cloud CDN. I nomi cambiano, ma i concetti fondamentali sono piuttosto simili.

Lo stesso avviene con i servizi dati. Per i database relazionali gestiti, AWS dispone di RDS, mentre Azure e Google Cloud offrono famiglie di servizi come Azure Database for PostgreSQL e MySQL e Cloud SQL. Nel mondo NoSQL abbiamo DynamoDB, Cosmos DB e Firestore. Per i data warehouse, Redshift, Synapse e BigQuery. Per il file storage, EFS, Azure Files e Filestore. Per la messaggistica, possiamo trovare SQS, Azure Service Bus e Pub/Sub. Persino i servizi di identità, gestione dei secret e osservabilità possiedono equivalenti chiari: IAM, Entra ID e Cloud IAM; Secrets Manager, Key Vault e Secret Manager; CloudWatch, Azure Monitor e Cloud Monitoring.

Questa corrispondenza compare anche nelle architetture più moderne. Lambda, Azure Functions e Cloud Run functions rispondono a modelli di esecuzione serverless, mentre Fargate, Azure Container Apps e Cloud Run permettono di eseguire container senza dover amministrare direttamente le macchine virtuali. Per l'infrastructure as code abbiamo CloudFormation su AWS e ARM Templates e Bicep nell'ecosistema Microsoft, mentre strumenti indipendenti come Terraform permettono di lavorare con diversi provider utilizzando un approccio comune.

Anche l'intelligenza artificiale possiede già un insieme relativamente chiaro di equivalenze. SageMaker, Azure Machine Learning e Vertex AI offrono piattaforme per lo sviluppo e l'operatività dei workload di machine learning. Bedrock, Azure AI Foundry e Vertex AI offrono percorsi differenti per consumare modelli e costruire applicazioni di intelligenza artificiale. Tuttavia, qui le differenze iniziano a diventare particolarmente importanti, perché i modelli disponibili, gli acceleratori, le API, gli strumenti di training, i servizi gestiti e le integrazioni con il resto della piattaforma variano notevolmente tra i provider.

Questo parallelismo è utile perché permette di costruire un vocabolario comune per confrontare le piattaforme. Chi conosce AWS riesce rapidamente a identificare dove cercare concetti simili in Azure o Google Cloud. Questo riduce molto la barriera iniziale per imparare una nuova piattaforma e permette anche di trasferire parte delle conoscenze architetturali da un cloud all'altro.

Ma esiste una trappola in questo confronto. Il fatto che due servizi risolvano problemi simili non significa che siano equivalenti per comportamento, architettura o esperienza operativa. Un object storage rimane un object storage, ma i meccanismi di controllo degli accessi, l'integrazione con altri servizi, la consistenza, le quote, i prezzi, la replica e le policy del ciclo di vita possono essere differenti. Lo stesso vale per database, servizi di messaggistica, Kubernetes e praticamente qualsiasi altra categoria.

Le differenze diventano ancora maggiori quando saliamo di livello di astrazione. Un database relazionale gestito può sembrare semplicemente un database relazionale gestito, ma i motori disponibili, le estensioni supportate, i meccanismi di replica, le opzioni di alta disponibilità, i backup, l'integrazione con gli analytics e gli strumenti di migrazione possono cambiare completamente la decisione. Allo stesso modo, due piattaforme possono offrire Kubernetes gestito, ma presentare differenze significative nell'integrazione con rete, identità, storage, osservabilità e servizi proprietari.

Esiste inoltre una differenza ancora più importante: ogni cloud possiede servizi che non hanno un equivalente diretto negli altri. Ed è proprio in questi servizi che spesso risiede una parte significativa del valore di una piattaforma. Se tutti i cloud offrono macchine virtuali, object storage e Kubernetes, queste risorse sono relativamente facili da confrontare. Servizi come DynamoDB, BigQuery, Cosmos DB o Cloud Run rappresentano invece decisioni architetturali più specifiche e possono creare dipendenze molto maggiori dal provider.

L'intelligenza artificiale rende questo punto ancora più evidente. I grandi cloud offrono servizi simili per training, inferenza e consumo di modelli, ma la combinazione tra modelli proprietari e di terze parti, GPU e altri acceleratori, API, strumenti di sviluppo, data pipeline, database vettoriali e servizi gestiti può essere molto diversa. Inoltre, non sempre un determinato modello o hardware è disponibile nella stessa regione, allo stesso prezzo o con la stessa capacità presso tutti i provider.

Per questo motivo, una matrice delle equivalenze è un ottimo punto di partenza per confrontare i cloud, ma non dovrebbe essere utilizzata come prova del fatto che siano intercambiabili. Aiuta a rispondere a “dove trovo qualcosa di simile a ciò che già conosco?”, ma non necessariamente a “quale piattaforma è migliore per ciò che sto cercando di costruire?”.

Conoscere le equivalenze riduce il costo di imparare un nuovo cloud. Conoscere le differenze è ciò che permette di scegliere tra loro.

## Single cloud, multi-cloud e il costo della semplicità

Esiste un argomento piuttosto forte a favore della scelta di un unico cloud: la semplicità. Gestire un'intera infrastruttura all'interno della stessa piattaforma riduce la quantità di concetti che devono essere padroneggiati, le integrazioni che devono essere mantenute e le differenze comportamentali che devono essere considerate. IAM, networking, osservabilità, billing, policy di sicurezza, deployment e troubleshooting possono seguire un insieme relativamente coerente di pattern. Il team può inoltre concentrare conoscenze, automazione e processi operativi su un'unica piattaforma.

Per un team piccolo o per un'organizzazione che non ha una necessità concreta di multi-cloud, questa semplicità ha un valore enorme. Non è soltanto una questione di produttività. Ogni tecnologia aggiuntiva richiede conoscenza, processi, monitoraggio, automazione e capacità di troubleshooting. Un secondo cloud significa imparare un secondo modo di fare molte delle stesse cose, oltre a gestire le differenze tra loro.

Strumenti come Terraform riducono molto questo problema. È possibile dichiarare infrastrutture di diversi provider utilizzando un unico linguaggio e, in molti casi, riutilizzare moduli, pipeline e pratiche operative. Questo rende una strategia multi-cloud molto più praticabile di quanto sarebbe se ogni provider richiedesse uno stack completamente indipendente. Ma Terraform non trasforma AWS, Azure e Google Cloud in piattaforme intercambiabili. Astrae il modo di dichiarare l'infrastruttura, non necessariamente l'architettura che viene dichiarata.

Una risorsa creata con Terraform continua a essere una risorsa specifica di un determinato provider. Una VPC continua ad avere le caratteristiche di AWS, una Virtual Network continua ad avere le caratteristiche di Azure e una VPC di Google Cloud possiede le proprie peculiarità. Il codice può anche apparire simile, ma il comportamento delle risorse, le loro limitazioni e le loro integrazioni continuano ad appartenere alla piattaforma.

Questo problema diventa particolarmente evidente quando vengono introdotti nuovi servizi. I provider cloud lanciano costantemente prodotti che sfruttano caratteristiche specifiche delle proprie piattaforme. Esiste naturalmente un intervallo tra il lancio di un servizio e l'esistenza di un supporto maturo per esso negli strumenti di infrastructure as code. Anche quando il supporto esiste, non sempre tutte le funzionalità del servizio sono esposte allo stesso modo.

Esiste inoltre una questione più sottile. Quanto più un'architettura cerca di essere portabile, tanto maggiore tende a essere la pressione a utilizzare soltanto risorse che possiedano equivalenti ragionevolmente vicini in tutti i provider. Questa può essere una decisione consapevole e perfettamente valida, ma significa rinunciare a parte del differenziale offerto da ciascuna piattaforma.

Se decidi di utilizzare soltanto servizi che possono essere trovati in AWS, Azure e Google Cloud, aumenti la portabilità dell'applicazione. Ma puoi anche rinunciare a utilizzare servizi che renderebbero quell'applicazione più semplice, più economica o più efficiente all'interno di un determinato cloud.

Questo è uno dei grandi trade-off della portabilità. Non è gratuita. È perfettamente possibile costruire un'applicazione che funzioni su AWS, Azure e Google Cloud. La questione è quanto valore stai lasciando sul tavolo per riuscire a farlo.

In alcuni casi, la risposta sarà “nessun valore rilevante”. Se l'applicazione utilizza soltanto container, PostgreSQL, object storage e alcuni componenti relativamente standardizzati, la portabilità può essere una proprietà piuttosto ragionevole. In altri, la risposta può essere molto diversa. Un'applicazione che dipende profondamente da servizi proprietari di un cloud può ottenere enormi vantaggi in semplicità, performance o costo proprio accettando un determinato livello di lock-in.

La discussione sull'utilizzo di uno o più cloud viene spesso presentata come una scelta tra semplicità e resilienza. Nella pratica, è un po' più complicata. Un singolo cloud può concentrare i rischi. Se un guasto significativo colpisce il provider, una parte importante dell'infrastruttura può diventare indisponibile simultaneamente. È possibile ridurre questo rischio utilizzando più regioni, zone di disponibilità e meccanismi adeguati di disaster recovery, ma esiste un limite a quanto possiamo proteggerci da un guasto che superi il confine di una regione o persino della piattaforma stessa.

D'altra parte, distribuire i workload tra diversi provider aumenta la quantità di componenti e integrazioni che devono essere gestiti. Ci troviamo a gestire diversi modelli di rete, identità, sicurezza, osservabilità, deployment e gestione dei costi. L'architettura può guadagnare indipendenza in alcune dimensioni e perdere semplicità in altre.

Multi-cloud, quindi, non significa automaticamente maggiore disponibilità. È possibile avere un'applicazione distribuita tra AWS e Azure e avere comunque un single point of failure. Potrebbe trovarsi nel DNS, nel provider di identità, nella CDN, nella connettività, nell'osservabilità, in un SaaS utilizzato da entrambe le architetture o in qualsiasi altra dipendenza condivisa.

Questo è un punto che considero particolarmente importante: la diversità dei fornitori non equivale necessariamente alla diversità delle dipendenze. Immagina un'applicazione il cui backend è distribuito tra AWS e Azure, ma che utilizza lo stesso provider DNS, la stessa CDN e lo stesso servizio di identità. Dal punto di vista del compute, esistono due provider. Dal punto di vista del percorso critico dell'applicazione, forse non esistono. Se una di queste dipendenze condivise fallisce, avere due cloud può non fare alcuna differenza.

Il caso di Cloudflare è un buon esempio per illustrare questo problema. Nel giugno 2022, una modifica alla configurazione della rete dell'azienda provocò un'indisponibilità che colpì diversi servizi che dipendevano dalla sua infrastruttura. Il punto interessante per un'architettura multi-cloud non è semplicemente che un fornitore sia diventato indisponibile, ma che una dipendenza collocata in uno strato trasversale possa influenzare le applicazioni indipendentemente da dove sia ospitato il loro compute.

Questo tipo di dipendenza è facile da ignorare perché normalmente non compare quando guardiamo soltanto il diagramma principale dell'infrastruttura. Possiamo disegnare AWS da un lato e Azure dall'altro e concludere di avere ridondanza. Ma, se entrambi dipendono dallo stesso DNS, dalla stessa CDN, dallo stesso provider di identità o da qualsiasi altro componente critico, esiste una dipendenza comune nascosta tra loro.

Questo aiuta anche a collocare il concetto di resilienza in una prospettiva più realistica. Multi-cloud può ridurre determinati rischi, ma non elimina il rischio. In alcuni casi, si limita a spostare il punto in cui il rischio si manifesta.

La domanda, quindi, non dovrebbe essere soltanto se l'applicazione è distribuita tra più di un cloud, ma se lo sono anche le sue dipendenze critiche. Per valutare la resilienza di un'architettura, è necessario guardare all'intera catena delle dipendenze, inclusi DNS, identità, CDN, connettività, osservabilità e servizi esterni, e non soltanto a dove vengono eseguiti container o macchine virtuali.

Esiste inoltre un altro aspetto importante: il multi-cloud può essere adottato per motivi che non hanno un rapporto diretto con la disponibilità. Negoziazione commerciale, requisiti normativi, localizzazione dei dati, disponibilità di determinati servizi, capacità GPU e differenze di costo possono essere motivi sufficienti per utilizzare più di un provider.

Allo stesso modo, una strategia single-cloud può essere perfettamente difendibile quando la semplicità operativa ha più valore dell'indipendenza aggiuntiva. Un singolo cloud, distribuito adeguatamente tra regioni e zone, può offrire un livello di resilienza sufficiente per molti workload.

Single-cloud e multi-cloud non dovrebbero essere trattati come posizioni ideologiche. Sono strategie architetturali differenti, con costi, benefici e rischi differenti. La scelta dovrebbe partire dal rischio che vogliamo ridurre, dal workload che stiamo cercando di eseguire e dalla complessità che siamo disposti ad assumere per raggiungere quell'obiettivo.

## Il differenziale dei cloud più piccoli

È proprio qui che vale la pena ampliare la mappa. Le hyperscaler possiedono un vantaggio evidente quando abbiamo bisogno di una piattaforma estremamente completa, con decine o centinaia di servizi integrati. Ma questa ampiezza può essere irrilevante per determinati workload.

Un'applicazione che necessita essenzialmente di macchine virtuali, storage, rete e magari Kubernetes non ha necessariamente bisogno di tutta la complessità offerta da AWS, Azure o Google Cloud. In questo scenario, provider come Hetzner, OVHcloud, DigitalOcean, Scaleway o Akamai possono entrare nell'analisi. La proposta di queste aziende non è necessariamente competere con le hyperscaler per quantità di servizi, ma offrire determinate risorse infrastrutturali in modo più semplice e, in alcuni casi, con una struttura dei costi più competitiva.

Esiste inoltre una categoria diversa di alternativa: piattaforme che astraggono ancora di più l'infrastruttura. Heroku, Render e Railway sono esempi di piattaforme in cui lo sviluppatore può concentrarsi sull'applicazione senza dover amministrare direttamente buona parte dei componenti infrastrutturali che esisterebbero in un approccio tradizionale. Per determinati progetti, questa astrazione può valere più dell'accesso a un catalogo gigantesco di servizi.

Questa differenza può essere molto rilevante. Se un'applicazione utilizza soltanto una frazione dei servizi disponibili in una hyperscaler, esiste un punto in cui la capacità aggiuntiva smette di rappresentare valore e inizia a rappresentare soltanto complessità. Per determinati workload, avere una macchina virtuale prevedibile, una rete semplice e uno storage adeguato può essere più importante che avere centinaia di servizi gestiti disponibili. Per altri, può avere senso salire ancora di livello di astrazione e utilizzare una piattaforma che nasconda buona parte di questa infrastruttura.

Lo stesso ragionamento vale per workload specifici. Se la risorsa principale necessaria è la GPU, la domanda può smettere di essere “qual è il mio cloud standard?” e diventare “chi offre la GPU di cui ho bisogno, nella quantità di cui ho bisogno, al costo che posso sostenere?”. In questo scenario, disponibilità dell'hardware, prezzo orario, capacità di espansione, localizzazione e caratteristiche dell'infrastruttura possono essere molto più rilevanti della quantità di servizi disponibili sulla piattaforma.

È in questo tipo di situazione che una preferenza storica per un determinato cloud inizia a perdere importanza. La familiarità continua ad avere valore, ma entra in competizione con criteri oggettivi del workload. Una piattaforma che non ho mai utilizzato può essere una scelta migliore per un determinato progetto semplicemente perché offre la risorsa necessaria in condizioni significativamente migliori.

Esiste inoltre un vantaggio importante: un cloud più piccolo o una piattaforma specializzata non deve essere un sostituto completo del cloud principale. Può semplicemente essere un componente dell'architettura. Un workload specifico può avere più senso su un altro provider mentre il resto dell'organizzazione rimane su un'unica piattaforma.

Questo permette un approccio intermedio tra single-cloud e multi-cloud. Invece di cercare di costruire un'applicazione completamente portabile tra diverse piattaforme, possiamo accettare che la maggior parte dell'infrastruttura si trovi su un cloud principale e utilizzare altri provider soltanto quando esiste un vantaggio concreto.

Questo approccio cambia anche il modo in cui pensiamo al multi-cloud. Non è necessario distribuire l'intera applicazione tra diversi provider per ottenere qualche beneficio dalla diversità. Possiamo avere un cloud principale e, allo stesso tempo, scegliere deliberatamente un altro fornitore per workload in cui sia più competitivo.

Il differenziale di un cloud più piccolo non deve essere offrire più risorse di una hyperscaler. Può essere proprio offrire meno, ma offrire ciò di cui il workload ha realmente bisogno in modo più semplice, più economico o più specializzato.

## Il problema del lock-in

Ogni discussione sui cloud arriva inevitabilmente al lock-in. Esiste la percezione che utilizzare soltanto servizi di base, come macchine virtuali, container e storage, renda un'architettura più portabile. In parte è vero. Quanto più specifica è una dipendenza da un provider, tanto maggiore tende a essere il costo per sostituirla. Un'applicazione basata su container, PostgreSQL e object storage tende ad avere più opzioni di migrazione rispetto a un'altra profondamente dipendente da decine di servizi proprietari.

Ma il lock-in non è soltanto una questione tecnologica. Esiste anche il lock-in operativo. Un'organizzazione può costruire processi, automazioni, conoscenze interne e strumenti di osservabilità profondamente integrati con una determinata piattaforma. Anche se tecnicamente è possibile migrare un'applicazione, il costo di formare i team, ricostruire le pipeline, adattare i processi e gestire una nuova infrastruttura può rendere la migrazione molto più difficile di quanto suggerisca il diagramma architetturale.

Esiste inoltre il lock-in economico. I dati sono un buon esempio. Migrare macchine virtuali può essere relativamente semplice, ma spostare grandi volumi di dati tra provider può comportare costi di trasferimento, tempo e una finestra operativa significativa. Un'architettura può essere tecnicamente portabile e, tuttavia, economicamente molto costosa da spostare.

Per questo motivo, evitare qualsiasi lock-in ha anch'esso un costo. Se un cloud offre un servizio gestito che riduce drasticamente la complessità operativa di un'applicazione, evitare quel servizio soltanto per mantenere una futura possibilità di migrazione può significare assumere oggi un costo reale per evitare un costo ipotetico. In alcuni casi, accettare deliberatamente una dipendenza dal provider è una decisione architetturale perfettamente razionale.

L'obiettivo, quindi, non dovrebbe essere eliminare completamente il lock-in. Probabilmente è impossibile. L'obiettivo dovrebbe essere comprenderlo. Esistono dipendenze strategiche e altre facilmente sostituibili. Esistono servizi il cui costo di migrazione sarebbe enorme e altri che potrebbero essere sostituiti in settimane. Esistono componenti che giustificano una dipendenza profonda da un provider e altri in cui la scelta può essere basata semplicemente su prezzo, disponibilità o convenienza.

È inoltre importante capire che non tutto il lock-in è necessariamente negativo. Se un servizio proprietario offre un vantaggio significativo in termini di costo, performance, disponibilità o produttività, la dipendenza può essere un prezzo accettabile per il beneficio ottenuto. L'importante è che questa dipendenza sia una decisione consapevole e non una conseguenza di cui ci accorgiamo soltanto quando dobbiamo migrare.

Un modo utile di pensarci è chiedersi, per ogni dipendenza importante, quanto sforzo sarebbe necessario per sostituirla, quanto tempo richiederebbe, quanto costerebbe e quali parti dell'architettura sarebbero interessate. Questa analisi permette di capire dove esiste lock-in, perché è stato assunto e quale sarebbe il costo per eliminarlo. L'obiettivo non è evitare il lock-in a ogni costo, ma garantire che le dipendenze dell'architettura siano decisioni consapevoli.

## Il costo di implementazione

Esiste un altro costo che spesso scompare dai confronti tra cloud: il costo di implementazione e gestione dell'architettura stessa. Due cloud possono offrire risorse tecnicamente equivalenti e prezzi simili, ma richiedere livelli completamente differenti di sforzo per portare un'applicazione in produzione. Una piattaforma può avere integrazioni pronte per un determinato servizio, mentre un'altra richiede che il team costruisca e mantenga parte di quell'integrazione. Una può offrire un servizio gestito che elimina decine di componenti, mentre un'altra richiede che questi componenti siano gestiti direttamente.

Questo costo non compare soltanto nelle architetture multi-cloud. Anche un'architettura eccessivamente sofisticata all'interno di un singolo cloud può richiedere più automazione, conoscenze e sforzo operativo di una soluzione più semplice. La differenza è che, quando aggiungiamo più provider, questa complessità tende ad aumentare perché dobbiamo gestire anche diversi modelli di rete, identità, sicurezza, osservabilità e deployment.

Quanto più numerose sono le differenze che dobbiamo nascondere dietro astrazioni, tanto maggiore tende a essere la quantità di codice, infrastruttura e automazione necessaria. Terraform aiuta molto nel livello di provisioning, ma non elimina le differenze tra le piattaforme. A un certo punto, qualcuno deve gestire queste differenze.

Lo stesso vale per osservabilità, sicurezza e operazioni. Un'architettura single-cloud può sfruttare le integrazioni native del provider per centralizzare log, metriche, identità, policy e alert. In un'architettura multi-cloud, possiamo aver bisogno di creare un ulteriore livello per unificare queste informazioni. Può essere una decisione corretta, ma anche questo livello deve essere costruito, monitorato e mantenuto.

Esiste inoltre il costo della conoscenza. Un team che gestisce AWS e Azure deve conoscere le peculiarità di entrambe le piattaforme. Questo non significa necessariamente avere il doppio del costo, ma significa aumentare la superficie di conoscenze necessaria per gestire l'infrastruttura. Lo stesso vale per i processi di troubleshooting, incident response, sicurezza e change management.

Questo costo compare anche quando arriva il momento di modificare l'architettura. Un'applicazione può essere relativamente economica da eseguire in una determinata configurazione e richiedere uno sforzo significativo per essere adattata a un'altra. La modifica può coinvolgere non soltanto macchine e container, ma anche dati, configurazioni, identità, reti, pipeline, osservabilità, integrazioni e processi operativi. In molti casi, il lavoro risiede proprio nelle dipendenze che non compaiono nel diagramma principale dell'applicazione.

Per questo, il costo di un'architettura dovrebbe essere analizzato almeno in tre momenti: quanto costa implementarla, quanto costa gestirla e quanto costa modificarla. Il prezzo mensile dell'infrastruttura è soltanto una di queste dimensioni.

Questo aiuta anche a spiegare perché non sempre conviene scegliere l'opzione tecnicamente più economica. Se un'alternativa riduce il costo dell'infrastruttura, ma richiede molta più ingegneria per essere implementata e gestita, il risparmio può scomparire rapidamente. Allo stesso modo, pagare di più per un servizio gestito può essere razionale se il costo operativo evitato è maggiore della differenza di prezzo.

## Compliance e regolamentazione

Esiste un criterio che può eliminare un cloud dalla lista delle opzioni prima ancora di iniziare a confrontare prezzo o funzionalità: la compliance. A seconda del settore, del paese e del tipo di dati trattati, un'organizzazione può essere soggetta a requisiti specifici di sicurezza, privacy, residenza dei dati, audit e continuità operativa. Banche, assicurazioni, aziende sanitarie e enti pubblici, per esempio, normalmente hanno vincoli molto diversi rispetto a un'applicazione personale o a un prodotto SaaS senza dati regolamentati.

I grandi cloud investono molto in quest'area e possiedono un'enorme quantità di certificazioni, standard e meccanismi di controllo. Offrono inoltre regioni in diversi paesi, funzionalità di crittografia, gestione delle chiavi, audit log, controlli delle identità e strumenti rivolti a requisiti normativi specifici. Anche i provider più piccoli possono soddisfare determinati requisiti, ma non necessariamente avranno la stessa copertura geografica o lo stesso insieme di certificazioni.

Questo può cambiare completamente la scelta. Un cloud può essere tecnicamente eccellente e competitivo sul prezzo, ma smettere di essere un'opzione se non possiede una regione adeguata, una determinata certificazione o i controlli necessari per il workload.

È inoltre importante separare la certificazione del provider dalla conformità dell'applicazione. Il fatto che un cloud possieda una determinata certificazione non significa che qualsiasi applicazione eseguita su di esso sia automaticamente conforme. La responsabilità è generalmente condivisa tra provider e cliente e l'architettura deve utilizzare correttamente i meccanismi di sicurezza, controllo degli accessi, crittografia, logging e conservazione dei dati disponibili.

Anche la localizzazione merita attenzione. “Il cloud è disponibile nel paese” non significa necessariamente che tutti i dati e i servizi utilizzati dall'applicazione rimarranno in quel paese. Backup, log, servizi gestiti, supporto e integrazioni possono avere caratteristiche differenti. In ambienti regolamentati, è necessario capire dove i dati vengono realmente archiviati, elaborati e replicati.

Questo è un punto in cui anche i cloud possono avere vantaggi differenti. Una hyperscaler può offrire un'enorme quantità di regioni e controlli, mentre un provider regionale può avere un vantaggio proprio perché mantiene la propria infrastruttura concentrata in determinate giurisdizioni. Per alcuni workload, questa caratteristica può essere più importante della quantità di servizi disponibili.

Per questo motivo, la compliance non dovrebbe comparire soltanto alla fine del processo di scelta. Può funzionare come filtro iniziale. Prima di confrontare prezzo, performance o quantità di servizi, può essere necessario chiedersi quali provider siano effettivamente eleggibili per quel workload.

Negli ambienti regolamentati, la prima domanda non è quale cloud offra più risorse, ma quali cloud possano soddisfare i requisiti del workload. A partire da questo insieme di opzioni, prezzo, performance, semplicità, portabilità e gli altri criteri possono entrare nella decisione.

## Sconti, partnership e free tier

Anche confrontare il prezzo dei cloud è più complicato che guardare la tabella pubblica dei prezzi. Il valore effettivamente pagato da un'organizzazione può essere molto diverso a seconda del volume acquistato, dell'impegno assunto e dei programmi commerciali disponibili.

I grandi cloud possiedono diversi meccanismi per ridurre il costo dei workload che rimangono attivi per un determinato periodo o raggiungono un determinato volume. Reserved Instances, Savings Plans, committed use discounts e contratti enterprise sono esempi di meccanismi che possono modificare significativamente il prezzo finale. In alcuni casi, la differenza tra il prezzo di listino e quello effettivamente negoziato è abbastanza grande da cambiare completamente un confronto superficiale tra provider.

Esistono inoltre crediti e programmi specifici per startup, progetti di ricerca, formazione e aziende che stanno migrando o espandendo i propri workload. Per un'azienda nelle fasi iniziali, per esempio, i crediti possono ridurre significativamente il costo durante i primi mesi. Ma questo tipo di beneficio deve essere analizzato con attenzione. Un credito iniziale può ridurre drasticamente il costo di ingresso senza necessariamente rendere la piattaforma più economica nel lungo periodo.

Anche le partnership possono pesare sulla decisione. Un'organizzazione può già possedere contratti, competenze, supporto specializzato o benefici commerciali associati a un determinato fornitore. In questo caso, cambiare cloud significa rinunciare non soltanto a un'infrastruttura, ma a parte di quell'ecosistema commerciale. Allo stesso modo, un'azienda può avere una partnership con un determinato provider che renda un'alternativa meno ovvia molto più competitiva.

I free tier seguono la stessa logica. Sono eccellenti per sperimentare una piattaforma, imparare a utilizzare i suoi servizi o mettere online piccoli progetti senza costi significativi. Possono anche essere un modo interessante per confrontare l'esperienza tra provider prima di assumere un impegno maggiore. Ma è importante separare il costo di sperimentare un cloud dal costo di gestirlo in produzione.

Un'applicazione che rientra comodamente nel free tier può diventare piuttosto costosa quando cresce. Lo stesso vale per i crediti promozionali. Sono eccellenti per ridurre il costo iniziale, ma non rappresentano necessariamente il costo ricorrente dell'architettura.

Esiste inoltre una trappola specifica quando confrontiamo i cloud soltanto sulla base del prezzo di una singola risorsa. Una GPU può essere più economica in un determinato provider, ma il costo totale del workload dipende anche da storage, trasferimento dati, rete, bilanciamento, osservabilità e dagli altri servizi necessari per far funzionare quella GPU. Lo stesso vale per qualsiasi altra risorsa.

Per questo, quando parliamo di costo del cloud, il numero più importante non è necessariamente il prezzo di un'istanza o di una GPU. È il costo totale per eseguire quel workload.

Questo è particolarmente importante perché le condizioni commerciali possono modificare significativamente l'analisi. Un cloud può sembrare più costoso nel prezzo di listino e diventare competitivo dopo sconti, crediti e contratti enterprise. Allo stesso modo, un'offerta molto interessante durante i primi mesi può smettere di avere senso quando terminano i benefici promozionali.

Il prezzo di listino è quindi soltanto il punto di partenza. Il costo reale dipende da ciò che verrà utilizzato, da quanto verrà utilizzato, per quanto tempo, da quali servizi aggiuntivi saranno necessari e dalle condizioni commerciali disponibili in quel contesto.

## Quindi, quale percorso scegliere?

Non esiste una risposta universale. La scelta dovrebbe iniziare dal workload e dai requisiti, non dal nome del cloud. Quali servizi sono realmente necessari? Dove devono trovarsi i dati? Qual è il costo totale, incluso il trasferimento dei dati? Qual è la disponibilità necessaria? Quali competenze possiede già il team? Quanto lock-in è accettabile? Esistono requisiti di compliance o regolamentazione? Esiste qualche servizio specifico che giustifichi la scelta di un determinato provider? E, soprattutto, quanto costa implementare, gestire ed eventualmente migrare questa architettura?

Quest'ultima domanda è particolarmente importante perché il prezzo dell'infrastruttura è soltanto una parte del costo. Un cloud può offrire macchine virtuali o GPU più economiche e continuare a essere un'opzione più costosa quando consideriamo lo sforzo di implementazione, le integrazioni, la gestione e la necessità di sviluppare componenti che un'altra piattaforma offre già come servizio gestito. Allo stesso modo, un'architettura più portabile può richiedere più ingegneria per essere costruita e mantenuta.

Lo stesso ragionamento vale per la migrazione. Una scelta che oggi sembra economica può creare una dipendenza il cui costo di sostituzione sarà molto maggiore in futuro. D'altra parte, evitare qualsiasi dipendenza specifica per preservare una possibilità di migrazione significa anche pagare per quella portabilità fin dal primo giorno.

Per questo, confrontare i cloud soltanto in base al prezzo o alla quantità di funzionalità difficilmente è sufficiente. Ciò che conta è il costo totale della decisione e il valore che ogni piattaforma offre per quel workload. Sconti, crediti, free tier e contratti commerciali entrano anch'essi nel calcolo, ma devono essere analizzati insieme al costo ricorrente e non come suoi sostituti.

La migliore architettura non è necessariamente quella che utilizza più cloud, così come il miglior cloud non è necessariamente quello che offre più servizi. Un singolo cloud può essere la scelta più adatta quando semplicità e integrazione sono prioritarie. Due o più possono avere senso quando esiste una ragione concreta per distribuire i workload tra fornitori. Un cloud più piccolo può essere più adatto a uno specifico workload. E una soluzione che sembra tecnicamente più sofisticata può essere semplicemente più complessa senza offrire un beneficio proporzionato.

Alla fine, scegliere un cloud significa scegliere un insieme di compromessi. Semplicità, costo, portabilità, lock-in, disponibilità, resilienza, compliance e complessità operativa fanno parte della stessa decisione. Non esiste una scelta senza trade-off. Esiste soltanto la possibilità di capire quali trade-off stiamo assumendo e perché abbiano senso per quel contesto.

Conoscere le alternative non significa utilizzarle tutte. Significa sapere quando la scelta predefinita ha senso, quando vale la pena cercare un'altra opzione e quale sarà l'impatto di questa decisione nel presente e nel futuro. Nel mio caso, conoscere meglio le alternative non ha fatto sì che smettessi di preferire AWS. Ha semplicemente fatto sì che smettesse di essere la risposta automatica.
