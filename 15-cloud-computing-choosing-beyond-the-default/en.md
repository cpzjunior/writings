# Cloud Computing: choosing beyond the default

_A map of the main clouds, their strengths, equivalents, and the trade-offs between simplicity, portability, cost, and resilience._

**Summary:** I argue that choosing a cloud should not be a decision based on familiarity or the size of the provider, but on the concrete characteristics of each workload. Equivalences between platforms help guide the comparison, but they do not eliminate differences in cost, operations, services, hardware, compliance, and lock-in. Single-cloud and multi-cloud are also not ideological positions: each brings costs, benefits, and risks that need to be evaluated alongside the architecture's actual dependencies. In the end, the best choice is the one that balances what the workload requires with the cost of implementing, operating, and eventually changing that architecture.

---

Historically, I have always had a fairly clear preference for AWS. Not necessarily because I consider AWS the best cloud in every scenario, but because it was the platform I had the most exposure to and familiarity with. Over time, I became accustomed to its services, its organization, its documentation, and its ecosystem. And there is a very natural consequence to this: when you know a technology well, it tends to seem like the simplest choice for the next problem.

In recent years, however, I started looking at other clouds more closely. One of the main reasons was quite pragmatic: GPUs. As artificial intelligence projects began to require increasingly greater computing capacity, I started to realize that familiarity with a platform could no longer be the main criterion for deciding where to run a workload. Price, GPU availability, resource location, expansion capacity, and even contracting models began to carry much more weight in the decision.

This made me take another look at a market that, although it is often reduced to the competition between AWS, Azure, and Google Cloud, is much broader. There are specialized clouds, regional providers, platforms with deliberately simpler propositions, and companies that can be extremely competitive for certain types of workloads precisely because they do not try to offer everything to everyone.

The goal of this text is not to make an exhaustive comparison between hundreds of services or declare which cloud is the best. The idea is to build a map broad enough to understand who the main players are, what their strengths are, which services have equivalents across them, and, most importantly, in which situations it is worth stepping off the obvious path.

Choosing a cloud based on familiarity is perfectly reasonable. Choosing a cloud without knowing the alternatives is not.

## The cloud map

When we talk about cloud computing, three names inevitably come first: AWS, Microsoft Azure, and Google Cloud. They remain the main general-purpose platforms in the public cloud market, with a scope that goes far beyond virtual machines and storage. Compute, databases, networking, containers, Kubernetes, serverless, analytics, artificial intelligence, security, observability, and an ever-growing number of managed services are part of this ecosystem.

There is a reason these three dominate the conversation. They are not just infrastructure providers, but complete platforms. An application can use compute, storage, databases, queues, identity, observability, secrets management, CDN, and artificial intelligence services from the same provider, all integrated with one another. This integration is one of the hyperscalers' major advantages and also one of the factors that make an eventual migration more complex.

But the cloud market is not a simple hierarchy. There are providers with different propositions and, depending on the workload, a provider that looks small when compared with a hyperscaler may be a much more interesting option.

Oracle Cloud Infrastructure, IBM Cloud, Alibaba Cloud, and Tencent Cloud are examples of providers that have particularly strong positions in certain markets and ecosystems. OCI has a natural relationship with environments that depend heavily on Oracle. IBM maintains a significant presence in large organizations and the Red Hat ecosystem. Alibaba and Tencent have much greater relevance when we consider China and other Asian markets. In these cases, the question is not necessarily which provider offers more services, but which one has greater alignment with the problem that needs to be solved.

There is also a group of providers that deliberately adopts a simpler proposition. DigitalOcean, Hetzner, OVHcloud, Scaleway, and Akamai, through Linode, can be interesting when the goal is to obtain compute, storage, and networking without necessarily depending on the huge number of managed services offered by hyperscalers. For certain workloads, this simplicity can mean lower operational complexity and more predictable costs.

Artificial intelligence, however, is changing this landscape. The growth in demand for GPUs has created a market in which hardware availability and cost can be more important than the number of services offered by the platform. An AI application that needs hundreds of GPUs does not necessarily benefit from being on the provider with the largest service catalog. In this scenario, GPU price, availability, accelerator architecture, interconnection between machines, ability to scale, and resource location may be the determining factors.

This has created room for specialized providers. CoreWeave is one of the best-known examples, having built its platform around GPU and artificial intelligence workloads. There are also other providers specialized in GPU and high-performance computing that can be highly competitive for this type of workload, even without offering a general-purpose platform comparable to the hyperscalers.

At the same time, the hyperscalers themselves are investing heavily in specialized hardware, foundation models, managed AI services, and integration of these resources with the rest of their platforms. This creates a different kind of competition from what existed in the traditional cloud market. The advantage can lie both in the infrastructure and in the ecosystem built around it.

In practice, this means there is no single cloud profile that is suitable for all workloads. General-purpose platforms remain extremely relevant, but specialized providers may be more competitive in certain situations. A company can be an excellent choice for traditional infrastructure and a poor choice for model training. Another may be uninteresting as a primary platform but extremely competitive for a specific GPU workload.

This is precisely one of the reasons it is worth looking beyond the default. The cloud chosen for an application does not necessarily have to be the same one chosen for every workload in the organization. A provider that historically appears small or secondary can become a relevant alternative when we change the question from “what is the best cloud?” to “what is the best infrastructure for this workload?”.

In the end, AWS, Azure, and Google Cloud remain the main general-purpose platforms, but size and number of services are not the only relevant criteria. The market is becoming more specialized, and artificial intelligence is accelerating this process. Understanding this landscape means knowing where the major platforms are strongest, where smaller providers can compete, and in which situations it makes sense to consider alternatives that would normally not even appear in the first search.

## Equivalence does not mean equality

One of the first things someone notices when studying different clouds is that the major providers have equivalents for many of the fundamental services. At the compute level, we can think of EC2 on AWS, Virtual Machines on Azure, and Compute Engine on Google Cloud. For object storage, we have S3, Blob Storage, and Cloud Storage. For virtual networks, VPC on AWS, Virtual Network on Azure, and VPC on Google Cloud. For managed Kubernetes, EKS, AKS, and GKE. For container registries, ECR, Azure Container Registry, and Artifact Registry. For load balancing, Elastic Load Balancing, Azure Load Balancer, and Cloud Load Balancing. For CDN, CloudFront, Azure Front Door, and Cloud CDN. The names change, but the fundamental concepts are quite similar.

The same happens with data services. For managed relational databases, AWS has RDS, while Azure and Google Cloud offer service families such as Azure Database for PostgreSQL and MySQL and Cloud SQL. In the NoSQL world, we have DynamoDB, Cosmos DB, and Firestore. For data warehouses, Redshift, Synapse, and BigQuery. For file storage, EFS, Azure Files, and Filestore. For messaging, we can find SQS, Azure Service Bus, and Pub/Sub. Even identity, secrets management, and observability services have clear equivalents: IAM, Entra ID, and Cloud IAM; Secrets Manager, Key Vault, and Secret Manager; CloudWatch, Azure Monitor, and Cloud Monitoring.

This correspondence also appears in more modern architectures. Lambda, Azure Functions, and Cloud Run functions address serverless execution models, while Fargate, Azure Container Apps, and Cloud Run allow containers to be run without directly managing virtual machines. For infrastructure as code, we have CloudFormation on AWS and ARM Templates and Bicep in the Microsoft ecosystem, while independent tools such as Terraform allow working with different providers using a common approach.

Even artificial intelligence already has a relatively clear set of equivalents. SageMaker, Azure Machine Learning, and Vertex AI offer platforms for developing and operating machine learning workloads. Bedrock, Azure AI Foundry, and Vertex AI offer different paths for consuming models and building artificial intelligence applications. However, this is where the differences start to become particularly important, because the available models, accelerators, APIs, training tools, managed services, and integrations with the rest of the platform vary significantly between providers.

This parallelism is useful because it allows us to build a common vocabulary for comparing platforms. Someone who knows AWS can quickly identify where to look for similar concepts in Azure or Google Cloud. This greatly reduces the initial barrier to learning a new platform and also makes it possible to carry part of the architectural knowledge from one cloud to another.

But there is a pitfall in this comparison. The fact that two services solve similar problems does not mean they are equivalent in behavior, architecture, or operational experience. Object storage is still object storage, but access control mechanisms, integration with other services, consistency, quotas, pricing, replication, and lifecycle policies can be different. The same applies to databases, messaging services, Kubernetes, and virtually any other category.

The differences become even greater when we move up the abstraction level. A managed relational database may appear to simply be a managed relational database, but the available engines, supported extensions, replication mechanisms, high-availability options, backups, analytics integration, and migration tools can completely change the decision. Likewise, two platforms may offer managed Kubernetes but have significant differences in their integration with networking, identity, storage, observability, and proprietary services.

There is another, more important difference: each cloud has services that do not have a direct equivalent in the others. And it is precisely in these services that a significant part of a platform's value often lies. If all clouds offer virtual machines, object storage, and Kubernetes, these resources are relatively easy to compare. Services such as DynamoDB, BigQuery, Cosmos DB, or Cloud Run, however, represent more specific architectural decisions and can create much greater dependencies on the provider.

Artificial intelligence makes this point even more evident. The major clouds offer similar services for training, inference, and model consumption, but the combination of proprietary and third-party models, GPUs and other accelerators, APIs, development tools, data pipelines, vector databases, and managed services can be quite different. Furthermore, a given model or piece of hardware is not always available in the same region, at the same price, or with the same capacity across all providers.

Therefore, an equivalence matrix is an excellent starting point for comparing clouds, but it should not be used as proof that they are interchangeable. It helps answer “where can I find something similar to what I already know?”, but not necessarily “which platform is better for what I am trying to build?”.

Knowing the equivalents reduces the cost of learning a new cloud. Knowing the differences is what allows you to choose between them.

## Single cloud, multi-cloud, and the cost of simplicity

There is a strong argument in favor of choosing a single cloud: simplicity. Operating an entire infrastructure within the same platform reduces the number of concepts that need to be mastered, the integrations that need to be maintained, and the behavioral differences that need to be considered. IAM, networking, observability, billing, security policies, deployment, and troubleshooting can follow a relatively consistent set of patterns. The team can also concentrate knowledge, automation, and operational processes on a single platform.

For a small team or an organization that has no concrete need for multi-cloud, this simplicity has enormous value. It is not merely a matter of productivity. Each additional technology requires knowledge, processes, monitoring, automation, and troubleshooting capabilities. A second cloud means learning a second way of doing many of the same things, in addition to dealing with the differences between them.

Tools such as Terraform significantly reduce this problem. It is possible to declare infrastructure across different providers using the same language and, in many cases, reuse modules, pipelines, and operational practices. This makes a multi-cloud strategy much more viable than it would be if each provider required a completely independent stack. But Terraform does not turn AWS, Azure, and Google Cloud into interchangeable platforms. It abstracts the way infrastructure is declared, not necessarily the architecture being declared.

A resource created with Terraform remains a resource specific to a given provider. A VPC still has AWS characteristics, a Virtual Network still has Azure characteristics, and a Google Cloud VPC has its own particularities. The code may even look similar, but the behavior of the resources, their limitations, and their integrations remain part of the platform.

This problem becomes particularly evident when new services emerge. Cloud providers constantly launch products that exploit characteristics specific to their own platforms. There is naturally a gap between the launch of a service and the availability of mature support for it in infrastructure-as-code tools. Even when support exists, not all features of the service are necessarily exposed in the same way.

There is also a subtler issue. The more an architecture tries to be portable, the greater the pressure tends to be to use only resources that have reasonably close equivalents across all providers. This can be a conscious and perfectly valid decision, but it means giving up part of the differentiation offered by each platform.

If you decide to use only services that can be found on AWS, Azure, and Google Cloud, you increase application portability. But you may also stop using services that would make that application simpler, cheaper, or more efficient within a particular cloud.

This is one of the major trade-offs of portability. It is not free. It is perfectly possible to build an application that runs on AWS, Azure, and Google Cloud. The question is how much value you are leaving on the table to make that possible.

In some cases, the answer will be “no meaningful value”. If the application uses only containers, PostgreSQL, object storage, and some relatively standardized components, portability can be a quite reasonable property. In others, the answer may be very different. An application that depends deeply on proprietary cloud services can achieve enormous gains in simplicity, performance, or cost precisely by accepting a certain level of lock-in.

The discussion about using one or multiple clouds is often presented as a choice between simplicity and resilience. In practice, it is a little more complicated. A single cloud can concentrate risks. If a significant failure affects the provider, a substantial portion of the infrastructure may become unavailable simultaneously. It is possible to reduce this risk by using multiple regions, availability zones, and appropriate disaster recovery mechanisms, but there is a limit to how much we can protect ourselves against a failure that crosses the boundary of a region or even the platform itself.

On the other hand, distributing workloads across different providers increases the number of components and integrations that need to be operated. We start dealing with different models for networking, identity, security, observability, deployment, and cost management. The architecture may gain independence in some dimensions and lose simplicity in others.

Multi-cloud, therefore, does not automatically mean greater availability. It is possible to have an application distributed between AWS and Azure and still have a single point of failure. It may be in DNS, the identity provider, the CDN, connectivity, observability, a SaaS used by both architectures, or any other shared dependency.

This is a point I consider particularly important: supplier diversity is not necessarily dependency diversity. Imagine an application whose backend is distributed between AWS and Azure, but which uses the same DNS provider, the same CDN, and the same identity service. From a compute perspective, there are two providers. From the application's critical path perspective, perhaps there are not. If one of those shared dependencies fails, having two clouds may make no difference at all.

Cloudflare is a good example to illustrate this problem. In June 2022, a configuration change in the company's network caused an outage that affected several services dependent on its infrastructure. The interesting point for a multi-cloud architecture is not simply that a provider became unavailable, but that a dependency located at a cross-cutting layer can affect applications regardless of where their compute is hosted.

This type of dependency is easy to overlook because it normally does not appear when we look only at the main infrastructure diagram. We can draw AWS on one side and Azure on the other and conclude that we have redundancy. But if both depend on the same DNS, the same CDN, the same identity provider, or any other critical component, there is a shared dependency hidden between them.

This also helps put the concept of resilience into a more realistic perspective. Multi-cloud can reduce certain risks, but it does not eliminate risk. In some cases, it simply shifts where the risk appears.

The question, therefore, should not be only whether the application is distributed across more than one cloud, but whether its critical dependencies are as well. To assess the resilience of an architecture, we need to look at the entire dependency chain, including DNS, identity, CDN, connectivity, observability, and external services, and not just where the containers or virtual machines are running.

There is another important aspect: multi-cloud can be adopted for reasons that have no direct relationship with availability. Commercial negotiations, regulatory requirements, data location, availability of certain services, GPU capacity, and cost differences can all be sufficient reasons to use more than one provider.

Likewise, a single-cloud strategy can be perfectly defensible when operational simplicity has more value than the additional independence. A single cloud, properly distributed across regions and zones, can provide a sufficient level of resilience for many workloads.

Single-cloud and multi-cloud should not be treated as ideological positions. They are different architectural strategies, with different costs, benefits, and risks. The choice should start from the risk we want to reduce, the workload we are trying to run, and the complexity we are willing to assume to achieve that goal.

## The differentiator of smaller clouds

This is precisely where it is worth broadening the map. Hyperscalers have an obvious advantage when we need an extremely comprehensive platform, with dozens or hundreds of integrated services. But that breadth can also be irrelevant for certain workloads.

An application that essentially needs virtual machines, storage, networking, and perhaps Kubernetes does not necessarily need all the complexity offered by AWS, Azure, or Google Cloud. In this scenario, providers such as Hetzner, OVHcloud, DigitalOcean, Scaleway, or Akamai can enter the analysis. These companies are not necessarily trying to compete with hyperscalers in the number of services, but to provide certain infrastructure resources more simply and, in some cases, with a more competitive cost structure.

There is also a different category of alternative: platforms that abstract the infrastructure even further. Heroku, Render, and Railway are examples of platforms where developers can focus on the application without directly managing much of the infrastructure components that would exist in a traditional approach. For certain projects, this abstraction may be worth more than access to a gigantic service catalog.

This difference can be quite significant. If an application uses only a fraction of the services available from a hyperscaler, there comes a point where additional capacity stops representing value and starts representing only complexity. For certain workloads, having a predictable virtual machine, a simple network, and adequate storage can be more important than having hundreds of managed services available. For others, it may make sense to move even further up the abstraction level and use a platform that hides much of that infrastructure.

The same reasoning applies to specific workloads. If the primary resource required is GPU, the question may stop being “what is my default cloud?” and become “who offers the GPU I need, in the quantity I need, at a cost I can afford?”. In this scenario, hardware availability, hourly price, expansion capacity, location, and infrastructure characteristics may be much more relevant than the number of services available on the platform.

It is in this type of situation that a historical preference for a particular cloud begins to lose importance. Familiarity still has value, but it starts competing with objective workload criteria. A platform I have never used may be a better choice for a given project simply because it offers the required resource under significantly better conditions.

There is also an important advantage: a smaller cloud or specialized platform does not need to be a complete replacement for the primary cloud. It can simply be one piece of the architecture. A specific workload may make more sense on another provider while the rest of the organization remains on a single platform.

This enables an intermediate approach between single-cloud and multi-cloud. Instead of trying to build an application that is completely portable across several platforms, we can accept that most of the infrastructure will be on a primary cloud and use other providers only when there is a concrete advantage.

This approach also changes how we think about multi-cloud. It is not necessary to distribute the entire application across multiple providers to obtain some benefit from diversity. We can have a primary cloud and, at the same time, deliberately choose another provider for workloads where it is more competitive.

The differentiator of a smaller cloud does not need to be offering more resources than a hyperscaler. It can be precisely offering less, but offering what the workload actually needs in a simpler, cheaper, or more specialized way.

## The lock-in problem

Any discussion about clouds inevitably reaches lock-in. There is a perception that using only basic services, such as virtual machines, containers, and storage, makes an architecture more portable. This is partly true. The more specific a dependency on a provider is, the greater the cost of replacing it tends to be. An application based on containers, PostgreSQL, and object storage tends to have more migration options than one deeply dependent on dozens of proprietary services.

But lock-in is not only a technological issue. There is also operational lock-in. An organization can build processes, automations, internal knowledge, and observability tools deeply integrated with a particular platform. Even if it is technically possible to migrate an application, the cost of training teams, rebuilding pipelines, adapting processes, and operating a new infrastructure can make migration much more difficult than the architectural diagram suggests.

There is also economic lock-in. Data is a good example. Migrating virtual machines can be relatively simple, but moving large volumes of data between providers can involve transfer costs, time, and a significant operational window. An architecture can be technically portable and still be economically very expensive to move.

Therefore, avoiding any lock-in also has a cost. If a cloud offers a managed service that drastically reduces the operational complexity of an application, avoiding that service merely to preserve a future migration possibility can mean taking on a real cost today to avoid a hypothetical cost. In some cases, deliberately accepting a provider dependency is a perfectly rational architectural decision.

The goal, therefore, should not be to completely eliminate lock-in. That is probably impossible. The goal should be to understand it. Some dependencies are strategic and others are easily replaceable. Some services would have enormous migration costs, while others could be replaced in weeks. Some components justify a deep dependency on a provider, while in others the choice can simply be based on price, availability, or convenience.

It is also important to understand that not all lock-in is necessarily bad. If a proprietary service offers a significant advantage in cost, performance, availability, or productivity, the dependency may be an acceptable price for the benefit obtained. What matters is that this dependency be a conscious decision, rather than a consequence we discover only when we need to migrate.

A useful way to think about this is to ask, for each important dependency, how much effort would be required to replace it, how long it would take, how much it would cost, and which parts of the architecture would be affected. This analysis makes it possible to understand where lock-in exists, why it was accepted, and what it would cost to remove it. The goal is not to avoid lock-in at any cost, but to ensure that the architecture's dependencies are conscious decisions.

## The cost of implementation

There is another cost that tends to disappear from comparisons between clouds: the cost of implementing and operating the architecture itself. Two clouds may offer technically equivalent resources and similar prices, but require completely different levels of effort to put an application into production. One platform may have ready-made integrations for a given service, while another requires the team to build and maintain part of that integration. One may offer a managed service that eliminates dozens of components, while another requires those components to be operated directly.

This cost does not appear only in multi-cloud architectures. An excessively sophisticated architecture within a single cloud can also require more automation, knowledge, and operational effort than a simpler solution. The difference is that when we add multiple providers, this complexity tends to increase because we also need to deal with different models for networking, identity, security, observability, and deployment.

The more differences we need to hide behind abstractions, the greater the amount of code, infrastructure, and automation required tends to be. Terraform helps considerably at the provisioning layer, but it does not eliminate the differences between platforms. At some point, someone has to deal with those differences.

The same applies to observability, security, and operations. A single-cloud architecture can take advantage of the provider's native integrations to centralize logs, metrics, identity, policies, and alerts. In a multi-cloud architecture, we may need to create an additional layer to unify this information. That can be the right decision, but that layer also needs to be built, monitored, and maintained.

There is also the cost of knowledge. A team that operates AWS and Azure needs to know the particularities of both platforms. This does not necessarily mean twice the cost, but it does mean increasing the knowledge surface required to operate the infrastructure. The same applies to troubleshooting, incident response, security, and change management processes.

This cost also appears when it is time to change the architecture. An application may be relatively inexpensive to run in a particular configuration and require significant effort to be adapted to another. The change may involve not only machines and containers, but also data, configurations, identities, networks, pipelines, observability, integrations, and operational processes. In many cases, the work lies precisely in the dependencies that do not appear in the application's main diagram.

Therefore, the cost of an architecture should be analyzed at least at three moments: how much it costs to implement, how much it costs to operate, and how much it costs to change. The monthly infrastructure price is only one of these dimensions.

This also helps explain why it is not always worth choosing the technically cheapest option. If an alternative reduces infrastructure costs but requires much more engineering to implement and operate, the savings can disappear quickly. Likewise, paying more for a managed service can be rational if the avoided operational cost is greater than the price difference.

## Compliance and regulation

There is a criterion that can eliminate a cloud from the list of options before we even start comparing price or features: compliance. Depending on the industry, country, and type of data processed, an organization may be subject to specific requirements for security, privacy, data residency, auditing, and business continuity. Banks, insurers, healthcare companies, and public agencies, for example, normally have very different restrictions from a personal application or a SaaS product without regulated data.

The major clouds invest heavily in this area and have a huge number of certifications, standards, and control mechanisms. They also offer regions in different countries, encryption capabilities, key management, audit logs, identity controls, and tools aimed at specific regulatory requirements. Smaller providers may also meet certain requirements, but they will not necessarily have the same geographic coverage or the same set of certifications.

This can completely change the choice. A cloud may be technically excellent and competitive in price, but cease to be an option if it does not have an appropriate region, a particular certification, or the controls required for the workload.

It is also important to separate provider certification from application compliance. The fact that a cloud has a particular certification does not mean that every application running on it is automatically compliant. Responsibility is generally shared between the provider and the customer, and the architecture needs to correctly use the available security, access control, encryption, logging, and data retention mechanisms.

Location also deserves attention. “The cloud is available in the country” does not necessarily mean that all data and services used by the application will remain in that country. Backups, logs, managed services, support, and integrations may have different characteristics. In regulated environments, it is necessary to understand where the data is actually stored, processed, and replicated.

This is another area where clouds can have different advantages. A hyperscaler may offer a huge number of regions and controls, while a regional provider may have an advantage precisely because it keeps its infrastructure concentrated in certain jurisdictions. For some workloads, this characteristic may be more important than the number of services available.

Therefore, compliance should not appear only at the end of the selection process. It can serve as an initial filter. Before comparing price, performance, or number of services, it may be necessary to ask which providers are actually eligible for that workload.

In regulated environments, the first question is not which cloud offers the most resources, but which clouds can meet the workload's requirements. From that set of options, price, performance, simplicity, portability, and other criteria can enter the decision.

## Discounts, partnerships, and free tiers

Comparing cloud prices is also more complicated than looking at the public price list. The amount actually paid by an organization can be quite different depending on the contracted volume, the commitment made, and the commercial programs available.

The major clouds have different mechanisms for reducing the cost of workloads that remain for a certain period or reach a certain volume. Reserved Instances, Savings Plans, committed use discounts, and enterprise contracts are examples of mechanisms that can significantly alter the final price. In some cases, the difference between the list price and the price actually negotiated is large enough to completely change a superficial comparison between providers.

There are also credits and specific programs for startups, research projects, education, and companies that are migrating or expanding their workloads. For a company in its early stages, for example, credits can significantly reduce costs during the first few months. But this type of benefit needs to be analyzed carefully. An initial credit can drastically reduce the entry cost without necessarily making the platform cheaper in the long term.

Partnerships can also weigh into the decision. An organization may already have contracts, expertise, specialized support, or commercial benefits associated with a particular provider. In that case, changing clouds means giving up not just infrastructure, but part of that commercial ecosystem. Likewise, a company may have a partnership with a particular provider that makes a less obvious alternative much more competitive.

Free tiers follow the same logic. They are excellent for experimenting with a platform, learning its services, or putting small projects online without significant cost. They can also be an interesting way to compare the experience across providers before making a larger commitment. But it is important to distinguish the cost of experimenting with a cloud from the cost of operating on it in production.

An application that fits comfortably within the free tier can become quite expensive as it grows. The same applies to promotional credits. They are excellent for reducing the entry cost, but they do not necessarily represent the recurring cost of the architecture.

There is also a specific pitfall when comparing clouds based only on the price of an isolated resource. A GPU may be cheaper at a given provider, but the total workload cost also depends on storage, data transfer, networking, load balancing, observability, and the other services required to put that GPU to work. The same applies to any other resource.

Therefore, when we talk about cloud costs, the most important number is not necessarily the price of an instance or a GPU. It is the total cost of running that workload.

This is especially important because commercial conditions can significantly change the analysis. A cloud may appear more expensive at list price and become competitive after discounts, credits, and enterprise contracts. Likewise, a very attractive offer during the first few months may stop making sense once the promotional benefits end.

The list price is therefore only the starting point. The actual cost depends on what will be used, how much will be used, for how long, which additional services will be required, and the commercial conditions available in that context.

## So, which path should you choose?

There is no universal answer. The choice should start with the workload and its requirements, not with the name of the cloud. Which services are actually needed? Where does the data need to be? What is the total cost, including data transfer? What level of availability is required? What skills does the team already have? How much lock-in is acceptable? Are there compliance or regulatory requirements? Is there a specific service that justifies choosing a particular provider? And, most importantly, how much does it cost to implement, operate, and eventually migrate that architecture?

This last question is particularly important because infrastructure price is only part of the cost. A cloud may offer cheaper virtual machines or GPUs and still be a more expensive option when we consider implementation effort, integrations, operations, and the need to develop components that another platform already offers as a managed service. Likewise, a more portable architecture may require more engineering to build and maintain.

The same reasoning applies to migration. A choice that seems cheap today may create a dependency whose replacement cost will be much higher in the future. On the other hand, avoiding any specific dependency to preserve a migration possibility also means paying for that portability from day one.

Therefore, comparing clouds based only on price or number of features is rarely enough. What matters is the total cost of the decision and the value each platform delivers for that workload. Discounts, credits, free tiers, and commercial contracts are also part of this calculation, but they need to be analyzed alongside recurring costs and not as substitutes for them.

The best architecture is not necessarily the one that uses more clouds, just as the best cloud is not necessarily the one that offers more services. A single cloud can be the best choice when simplicity and integration are priorities. Two or more can make sense when there is a concrete reason to distribute workloads across providers. A smaller cloud may be more suitable for a specific workload. And a solution that appears technically more sophisticated may simply be more complex without delivering a proportional benefit.

In the end, choosing a cloud means choosing a set of compromises. Simplicity, cost, portability, lock-in, availability, resilience, compliance, and operational complexity are all part of the same decision. There is no choice without trade-offs. There is only the possibility of understanding which trade-offs we are accepting and why they make sense in that context.

Knowing the alternatives does not mean using all of them. It means knowing when the default choice makes sense, when it is worth looking for another option, and what the impact of that decision will be in the present and in the future. In my case, getting to know the alternatives better did not make me stop preferring AWS. It simply made it stop being the automatic answer.
