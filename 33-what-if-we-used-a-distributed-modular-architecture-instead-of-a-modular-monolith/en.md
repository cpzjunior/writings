# What if we used a distributed modular architecture instead of a modular monolith?

_An architectural idea for early-stage startups that need to grow without paying disproportionately for infrastructure or the complexity of microservices._

**Summary:** I propose a distributed modular architecture that separates the development unit from the processing unit: the module continues to organize code, rules, and tests, while each use case can adopt its own execution and scaling strategy when there is a concrete need. This allows startups to begin with a simple structure, distributing only the workloads that actually require more capacity, without taking on the complexity of microservices upfront. The idea is not to replace the modular monolith or microservices, but to create a starting alternative that allows infrastructure decisions to be deferred and complexity to be introduced gradually.

---

When a startup is getting started, software architecture is often a matter of balance. The team is small, the product is still discovering its market, user volume is uncertain, and the budget is limited. At the same time, some decisions made early on can remain in place for years and become difficult or expensive to change later. In this context, an architecture needs to do more than organize code: it needs to allow the company to defer expensive decisions until there is a concrete reason to make them.

A few years ago, I was a volunteer president of Se Doar, an NGO that maintained a platform connecting social organizations with people and companies interested in making donations or offering volunteer work. In addition to being president, I took care of the platform together with other volunteers. It was a context in which these constraints became particularly evident. We had few resources, a small team, and little room to maintain idle infrastructure. Every technical decision also had to be evaluated based on its operational and financial impact.

The first version of the platform used a modular monolith. At that point, it made sense. The application was relatively small, the modules helped separate responsibilities, and the infrastructure remained simple to operate. As the system evolved, however, it became clear that the different parts of the application did not necessarily behave in the same way. Some features received requests constantly, while others were used only occasionally. Some needed to remain continuously available, while others could be executed on demand. The code could be well modularized and, even so, the application remained the main unit of deployment and scaling.

It was in this context that the possibility of using functions became interesting. Instead of keeping computational capacity permanently available for the entire application, certain features could consume resources only when they were executed. This does not mean that serverless is always cheaper, or that it is the best choice for every workload. The point that caught my attention was something else: different parts of the same product can have very different processing profiles, but we are normally led to choose a single execution strategy for the entire application.

That experience eventually led me to a question that I consider particularly relevant for early-stage startups: why does the granularity of development necessarily have to be the same as the granularity of deployment and infrastructure? A module can be an excellent unit for organizing code, tests, business rules, and dependencies without necessarily being the minimum unit of deployment and scaling.

The question gains more context when we look at the evolution of modern architectures. Microservices offer deployment, scaling, and ownership independence, but introduce the complexity inherent to distributed systems. The modular monolith, on the other hand, seeks to preserve the operational simplicity of a single application while creating stronger boundaries within the code.

For a small startup, this may be exactly what is needed. But one question remains: if we can modularize development, do we necessarily need to scale and provision those modules as indivisible units? This is the question I want to explore in this article.

## Microservices and modular monoliths

As systems and organizations grow, different problems begin to appear. A large application can become difficult to maintain because its responsibilities lack clear boundaries, but it can also become difficult to operate because different parts need to evolve, be deployed, or scale in different ways. There is no single reason why a large system becomes complex, and different architectures have emerged to address different parts of this problem.

Microservices gained traction primarily as a response to organizational and operational scaling problems. Different parts of the domain may evolve at different speeds, teams need to work with greater autonomy, and certain components may have very different scaling or availability requirements. By separating these responsibilities into independent services, each service can have its own development and deployment lifecycle, its own infrastructure, and its own scaling strategy.

This independence, however, comes at a price. When two components are in the same process, a dependency can be resolved through a method call or by directly using a library. When those components become different services, communication crosses a network. An operation that previously failed with an exception may now fail with a timeout; a synchronous call may require retries; a local transaction may cross a process boundary; logs and metrics need to be correlated to follow a request across different components.

Microservices do not eliminate complexity: they shift part of it to communication, infrastructure, and the operation of a distributed system. For large organizations, this trade-off can be excellent. Independence between services may be more valuable than the additional complexity it introduces. For an early-stage startup, however, taking on that complexity before there is a concrete need may represent a significant cost. With few developers, each additional service also means more deployments, observability, infrastructure, troubleshooting, and operational decisions.

Modular monoliths start from a different concern. Large systems also become difficult to maintain when their responsibilities lack clear boundaries, when dependencies spread throughout the code, and when changes in one part of the system produce unexpected effects in others. Modularization attempts to address this problem without necessarily introducing a process boundary. We can organize an application into well-defined modules while keeping their interactions within the same process.

This approach also recognizes an important characteristic of software development: domain boundaries change. As a team gains a better understanding of the product, new rules emerge, responsibilities are discovered, and modules that initially seemed well defined may need to be split, combined, or reorganized. Keeping these boundaries within a single application makes such changes simpler than immediately turning them into distribution decisions.

For this reason, modular monoliths and microservices do not necessarily represent different stages of the same architectural evolution. They are approaches that prioritize different properties. Microservices prioritize operational and organizational independence, while the modular monolith seeks to preserve the operational simplicity of a single application while creating clear boundaries within the software.

The problem that interests me in this article appears precisely between these two concerns. We can have a system that is small enough that the complexity of microservices is not justified, but that still has workloads with very different processing needs. We can also have perfectly modularized code and still need to scale the entire application because it remains the unit of deployment and processing.

This is where the central question of this article emerges: what if the development unit could remain the module, while the processing and scaling unit could be a use case?

## A distributed modular architecture

The proposal starts by separating two concerns that are normally coupled: the development unit and the processing unit. The module remains the unit for organizing the software. It is where related use cases, business rules, persistence, tests, and dependencies live. The fact that a module contains several use cases, however, does not mean that all of them need to be executed or scaled in the same way.

We can imagine, for example, an `Orders` module containing `CreateOrder`, `CancelOrder`, `GetOrder`, and `GenerateReport`. These use cases continue to belong to the same module and can be developed, tested, and versioned together. The difference appears at execution time: `CreateOrder` can be executed by a function, `CancelOrder` can remain in a conventional application, `GetOrder` can use another processing strategy, and `GenerateReport` can be processed asynchronously.

```
Orders
├── CreateOrder       → function
├── CancelOrder       → application
├── GetOrder          → function
└── GenerateReport    → job
```

If demand for `GetOrder` increases, for example, we can increase the capacity allocated to that use case without necessarily replicating the entire module. This is the main characteristic of the proposal: the module remains the unit of development and evolution, while the use case can, when appropriate, become an independent unit of execution and scaling.

I am not proposing that every use case needs to be executed in isolation, much less that every use case should become a service. The smaller granularity only exists when there is a reason to use it.

To make the idea concrete, throughout the article I will use some technologies that I like working with, such as .NET, PostgreSQL, Dapper, AWS, and Infrastructure as Code tools. These choices are implementation examples, not architectural requirements. In a .NET implementation, for example, each module could be a library containing its use cases, business rules, persistence, and tests. The infrastructure required to execute these use cases could be defined alongside the module, using an Infrastructure as Code tool such as AWS CDK or its equivalent on another provider.

Thus, `Orders` could declare both the resources required for its execution and how each use case is exposed. `GetOrder` could be associated with a function and an API endpoint, while `GenerateReport` could use a queue and a worker.

The idea is not to duplicate infrastructure across modules. There is a distinction between what is shared and what belongs to a specific context. What is truly used by everyone can be part of a common core. A capability used by some modules can be represented by its own module. What belongs to a single module can remain with that module.

```
Used by everyone
      ↓
    Core

Used by some
      ↓
Own module

Used by one
      ↓
Consumer module
```

This rule also helps prevent the `Core` from gradually becoming a repository for generic abstractions.

If `Orders` and `Payments` use a pricing capability, for example, that does not mean `Pricing` needs to be part of the core. It can be its own module, used by both consumers.

```
Orders ────────► Pricing
Payments ──────► Pricing
Customers
```

The same logic applies to communication, but there is an important difference between synchronous and asynchronous flows.

In a synchronous flow, a module boundary does not need to represent a network boundary. If `Orders` uses `Customers`, the application can simply depend on the corresponding library and execute the `Customers` code directly within the same process.

If `Orders.GetOrder` is running inside a function, that does not need to change. The function has the `Orders` use case as its entry point, and its dependencies can still be resolved within the same process.

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

In an asynchronous flow, on the other hand, communication can continue to use messaging or streaming. An event or command can be published to a queue, such as SQS, or to a stream, depending on the characteristics of the workload.

```
Orders
   │
   │ event
   ▼
 SQS / Stream
   │
   ▼
Payments
```

The architecture, therefore, does not attempt to eliminate distributed communication. It attempts to avoid introducing it where it is not necessary.

If tomorrow `Payments.ProcessPayment` needs to be executed separately, for example, it can already be behind an asynchronous boundary without requiring the entire `Payments` module to become an independent service.

This is an important difference from a microservices-based approach. The architecture does not automatically turn every module into a service. The system can start entirely within a single process and, as concrete needs emerge, specific use cases can receive different processing and deployment strategies.

A function can be one of these strategies, but it can also be a conventional application, a container, a worker, or any other mechanism appropriate to the workload.

```
Application
├── Orders
├── Customers
├── Payments
└── Inventory
```

can evolve into:

```
Application
├── Orders
├── Customers
└── Inventory

Functions
├── Orders.GetOrder
└── Payments.ProcessPayment
```

without `Orders`, `Customers`, or `Payments` needing to be turned into microservices.

What was distributed was not necessarily the module. It was the execution of specific use cases.

For me, this is the central distinction of the architecture: we can preserve a development unit that is large enough to keep the code organized while using an execution unit that is small enough for specific workloads to be processed and scaled independently.

## Functions as a starting point

For this proposal, I would start by using functions as the default strategy for use cases exposed through synchronous endpoints.

Not because functions are necessarily superior to containers or conventional processes, but because they offer an interesting combination for an early-stage startup: on-demand processing, independent scaling, and little idle capacity when utilization is low or variable.

The idea is to start with a simple strategy and change it only when the data shows that it is no longer appropriate. Instead of provisioning permanent capacity based on an estimate of future growth, we can let each use case consume resources as it is used.

This is particularly interesting at the beginning of a startup, when many characteristics of the workload are still unknown. Traffic may be low, irregular, or difficult to predict. A feature may remain almost unused for months and then suddenly begin receiving a significant number of requests.

If `GetOrder` has a constant and high volume, for example, it may make sense to migrate it to a provisioned container or process. If `GenerateReport` continues to run only a few times per day, it can remain a function.

```
Orders
├── GetOrder        → container
├── CreateOrder     → function
├── CancelOrder     → function
└── GenerateReport  → function
```

The change happens at the use-case level. The `Orders` module does not need to be reorganized or turned into a new service. We are simply replacing the strategy used to execute a particular part of it.

For asynchronous workloads, the strategy may be different from the beginning. A use case that consumes messages from a queue or stream can be executed by a worker, for example. A function remains a possibility, but it does not need to be the default for every type of workload.

There is, of course, the problem of cold starts. Depending on the runtime and latency requirements, the time required to initialize a function can be significant. For a workload executed a few times per day, this may be irrelevant. For a low-latency operation with constant traffic, it may be a reason to choose another execution strategy.

That is precisely the point of the proposal. Functions are a starting point, not a definitive decision. As the system reveals its real characteristics, each use case can adopt the execution strategy that best fits its workload.

The architecture, therefore, does not depend on remaining serverless. It depends on the ability to change that decision without having to change how the software is organized.

## Advantages and trade-offs

The main advantage of the proposal is separating development granularity from processing granularity. A module can remain a cohesive unit of code, tests, and evolution, while its use cases can use different execution strategies.

Imagine an `Orders` module in which `GetOrder` receives far more requests than `CancelOrder`, while `GenerateReport` runs only a few times per day. In the modular monolith, they all remain part of the same application and share the same deployment and processing unit. In the proposed architecture, each could use a different strategy.

```
GetOrder        → function
CreateOrder    → function
CancelOrder    → application
GenerateReport → job
```

The code does not need to be reorganized for this. The module remains `Orders`, with its use cases, business rules, persistence, and tests. What changes is how each workload is executed.

This granularity can also be interesting from an economic perspective. An early-stage startup may spend a considerable amount of time with low and unpredictable demand. In this scenario, maintaining permanent capacity for the entire application may mean paying for resources that remain idle for much of the time. For certain workloads, on-demand processing may bring costs closer to actual utilization.

This does not mean that the architecture is necessarily cheaper. Constant and predictable workloads may be more economical on provisioned infrastructure. The advantage lies in not forcing the entire application to use the same strategy. One use case can use a function, another a container, another a conventional application, and another a worker.

The decision can follow the actual behavior of the workload. This may be one of the most interesting points for a startup: rather than optimizing infrastructure from day one, the proposal attempts to defer infrastructure decisions until the actual behavior of the product provides enough information to make them.

Instead of provisioning today infrastructure sized for growth that may happen two years from now, we can start with capacity compatible with current demand and change the strategy only when there is a concrete need. The architecture does not attempt to anticipate growth. It attempts to avoid the need to anticipate infrastructure.

This flexibility also changes how the application can evolve. Instead of choosing between remaining entirely monolithic or progressively migrating to microservices, we can imagine a more selective evolution:

```
Modular monolith
       ↓
Selective distribution
       ↓
More distribution when necessary
```

A system can remain mostly within a single process while only the use cases that justify a different strategy are distributed. There is no need to anticipate which parts of the application will need to be scaled, isolated, or processed differently in the future.

This can be particularly interesting when very different workloads coexist within the same product. An AI feature, for example, may have processing, latency, and cost requirements completely different from a traditional CRUD operation. There is not necessarily a reason for both to use the same execution strategy simply because they belong to the same module.

The AI feature could use specific infrastructure and scale independently, while the remaining use cases continue using conventional infrastructure.

Ultimately, the advantage is not simply being able to scale with greater granularity. It is avoiding having the needs of one workload determine the infrastructure of the others. But this flexibility does not eliminate complexity. It allows complexity to be introduced selectively.

When a use case starts running outside the main process, the known problems of distributed systems arise: latency, timeouts, retries, observability, idempotency, and partial failures. The difference is that these costs do not need to be assumed by the entire application. If ten use cases can continue running within a conventional application, there is not necessarily a reason to distribute them. If an eleventh has a different scaling or processing requirement, we can distribute only that use case. The proposal, therefore, is not to create smaller microservices. It is to allow distribution to be a local decision, made when there is a concrete benefit.

There is also a cost associated with dependencies. When a module uses another as a library, an incompatible change in that dependency requires consumers to be updated, recompiled, and tested. This reduces some of the deployment independence that would be obtained with completely separate services. On the other hand, as long as the dependency remains within the same process, we do not need to pay the cost of a remote communication for every interaction between modules. `Orders` can use `Customers` directly as a library without turning that dependency into an HTTP call simply because the modules have different boundaries.

```
Orders ───────► Customers
   │
   └──────────► Pricing
                  │
                  ▼
               Products
```

This makes the dependency graph particularly important. Dependencies between modules need to have a clear direction and avoid cycles. If `Orders` depends on `Customers` and `Customers` depends on `Orders`, distributing them separately may simply turn code coupling into network coupling.

Distributing a use case also does not imply distributing all of its dependencies. If `Orders.GetOrder` uses `Customers.GetCustomer`, for example, that call can continue to be made directly through the `Customers` library.

```
Orders.GetOrder
      │
      └──► Customers.GetCustomer
                │
                └──► Repository
```

In this scenario, only the execution of `Orders.GetOrder` was distributed. `Customers` remains an in-process dependency. A new distributed boundary appears only when there is an explicit decision to execute `Customers` separately.

This is an important aspect of the proposal: distribution does not need to follow module boundaries. A use case can be distributed without all the modules it depends on also being turned into services.

There is also a cost associated with the processing granularity itself. Separating use cases makes it possible to scale each workload individually, but it can also mean replicating the module's runtime and dependencies across multiple execution units. A function or container may need to load the same libraries used by other use cases, increasing memory consumption, startup time, and, depending on the workload, total processing cost. Smaller granularity, therefore, is not free. It needs to provide enough benefit to compensate for this duplication.

Another important limitation lies in shared resources. The ability to scale `GetOrder` independently does not mean that the database can keep up with that expansion. PostgreSQL, queues, caches, and external services can still be bottlenecks.

The proposal increases the granularity at which processing can be scaled, but it does not remove the limits of the components on which that processing depends. If the database is the bottleneck, simply increasing the number of functions can make the problem worse. Therefore, the idea is not that every use case can scale indefinitely and independently. It is that, when capacity is available in the resources on which it depends, there is no need to scale along with things that do not participate in that workload.

There is also an operational consequence. A system with different execution strategies will have more deployments, configurations, permissions, observability, and infrastructure resources than a conventional monolith. The proposal does not eliminate this cost. What it attempts to do is avoid introducing it before there is a concrete need. This may be the architecture's main trade-off: gaining flexibility and granularity at the cost of some additional operational complexity.

The question, therefore, should not be whether this architecture is simpler than a monolith or than microservices. It probably is not. The question is whether the additional complexity appears only where there is a need that justifies it.

## What this architecture is, and when it makes sense

I would not call this proposal microservices. Not because a distributed modular architecture is incompatible with microservices, but because the proposed architectural unit is different. In microservices, the service normally concentrates decisions about modularity, deployment, ownership, operation, and scaling. Here, those decisions are deliberately separated.

The module remains the unit of development and evolution. The use cases continue to belong to that module and can share code, business rules, dependencies, and tests. The difference is that a use case can, when necessary, have its own execution and scaling strategy.

This means that a module can remain entirely within a conventional application throughout the product's lifetime. Another may have only one use case executed as a function. A third may use asynchronous processing for a specific operation. Distribution is not the goal of the architecture; it is a possibility that can be used when there is a concrete reason.

For this reason, I prefer to call this idea a distributed modular architecture. It is not intended to be a simplified version of microservices, nor a mandatory stage between a modular monolith and a service architecture. The proposal is to explore whether we can separate two decisions that normally end up being made together: how we organize and develop the software and how we provision and scale its processing.

This also means that I do not see this architecture as suitable for every system. If an application is small, has predictable load, and conventional infrastructure handles the problem comfortably, introducing this granularity may simply add complexity without producing a proportional benefit.

Likewise, systems with very specific security, availability, governance, auditing, isolation, or consistency requirements may require other architectural decisions. The proposal in this article starts from a more specific context: early-stage startups with small teams, limited budgets, and workloads that can grow very unevenly.

Even in this scenario, there is an important limit. Distributing processing does not eliminate shared resources. If several use cases depend on the same database and the database becomes the bottleneck, increasing the number of functions does not solve the problem. It may even increase pressure on an already saturated resource. The architecture allows processing to be scaled with greater granularity, but it does not remove the limits of the components on which that processing depends.

For this reason, I see this approach primarily as a hypothesis for a specific context, rather than a universal recommendation. It seems to make more sense when there is a combination of a small team, initially low or variable demand, and an expectation that different parts of the product may grow at very different rates.

Under these conditions, the ability to choose the processing strategy per use case may allow infrastructure to follow the actual behavior of the product without requiring the startup to take on in advance all the capacity or operational complexity that may only be necessary in the future.

In the end, the proposal is not to choose between a modular monolith and microservices. It is to question whether we need to choose a single execution unit for the entire system. Perhaps it is possible to preserve the simplicity of modular development while allowing only what actually needs to be distributed to be distributed.

## How would I know whether the architecture worked?

It is important to make it clear that this article presents an architectural proposal, not an empirically validated architecture. I have not had the opportunity to implement this model in a real startup and follow its evolution over several years. Therefore, I do not have data to claim that it necessarily reduces costs, simplifies system evolution, or produces a better experience for a development team.

What I do have is a previous experience that led me to see a possible space between the modular monolith and microservices: on one side, the importance of keeping development simple and modular; on the other, the possibility that different parts of a product may have very different processing and infrastructure needs.

For me, the proposal would only make sense if this separation between development and processing brought real benefits without creating greater complexity than the complexity it is intended to avoid. One of the first signs would be the ability to keep modules relatively simple even when some of their use cases start being executed in different ways. The team should be able to develop and test the module without turning every infrastructure difference into a concern in the code. At the same time, a use case should be able to gain its own execution or scaling strategy without requiring the entire module to follow that change.

Another sign would be the evolution of the system. If the application could start simply, remain mostly within a single process, and distribute only some use cases as concrete needs emerged, that would be evidence that the architecture is fulfilling one of its main purposes: allowing complexity to be introduced gradually rather than anticipated.

Dependencies would also be important. The architecture should allow modules to continue using libraries directly when appropriate, without turning every modular boundary into a network call. If distributing a single use case required a large portion of the dependencies to be turned into independent services, that would be a sign that the proposed granularity might be creating more coupling than it removes.

The economic aspect would be another point to observe. The additional granularity should, for some workloads, allow resources to follow actual utilization more closely. But this calculation could not consider only processing costs. It would need to include observability, deployments, infrastructure, maintenance, and the team's own time. If the savings from on-demand processing were smaller than the additional cost of operating the architecture, the proposal would not be achieving its objective.

Finally, I would observe what happens as the company grows. If, after reaching a larger scale, the modules needed to be rewritten, dependencies systematically replaced by APIs, or the system necessarily migrated to microservices to recover important properties, that would be a sign that the architecture merely postponed the problem. On the other hand, if the system could evolve gradually, distributing only what truly justified distribution, we would have more interesting evidence that the approach works.

Still, there is an important possibility: perhaps the result of the experiment will be discovering that this architecture does not offer enough advantage over a traditional modular monolith. That would also be a valid result.

The proposal, therefore, does not start from the certainty that it has found a better architecture. It starts from a hypothesis: perhaps there is a way to preserve the simplicity of modular development without forcing the entire system to share the same processing strategy.

## An architecture to be tested

Perhaps this approach will not work as well as I imagine. Operational complexity may appear too early. As the organization grows, certain characteristics of the system may make microservices a more appropriate choice. And, in many cases, the modular monolith itself may continue to be the best answer.

This does not contradict the proposal. The architecture was designed for a specific context: early-stage startups with small teams, limited resources, and workloads that can have significant differences in demand. Outside this context, the trade-offs may be completely different.

The idea is also not to eliminate microservices. If an organization reaches a point where isolation, ownership, independent deployment cycles, or other properties of a distributed architecture become more important than initial simplicity, microservices can be a perfectly reasonable evolution. Likewise, if the application remains small and predictable, there may be no reason whatsoever to abandon the modular monolith.

The proposal is more specific: start with a simple modular architecture and maintain the freedom to distribute only what actually needs to be distributed. If this works, a startup may defer both infrastructure decisions and some of the operational complexity until there is a concrete reason to take them on. I am not proposing a replacement for microservices. I am proposing an alternative starting point.

In the end, the distributed modular architecture is an idea that I would like to put into practice. I still do not know where its limits are, nor whether the benefits will be sufficient to offset the costs. But I believe there is a question interesting enough to justify the experiment: can we preserve the simplicity of modular development while allowing processing to be provisioned at the granularity of the use cases that actually need it?
