# Why Are Modern Systems Getting Easier to Build and Harder to Design?

_Cloud abstractions, the paradox of choice, and artificial intelligence are changing the nature of solution architecture faster than we can adapt._

**Summary:** I explore the reasons why modern systems are getting easier to build but harder to design: cloud, managed services, SaaS, and AI have reduced the cost of implementing solutions, but expanded the space of choices and made architectural judgment the main bottleneck. In this context, experience means knowing how to eliminate alternatives, evaluate trade-offs, recognize hidden dependencies, and preserve the reversibility of decisions. For this reason, I argue that solution architecture needs a more systematic body of knowledge, something close to a “PMBOK for Solution Architecture,” to organize the decision-making process without replacing the architect’s judgment.

---

I have a certain addiction to watching System Design videos. I particularly enjoy those in which someone explains how a large company solved a problem at scale: how a platform processes millions of events, how an application handles traffic spikes, how a company structured its data architecture, or how a particular service was split into dozens of components. It is interesting to observe an architecture after the main decisions have already been made. Each component seems to have a clear purpose, and, looking back, many choices seem almost obvious.

The situation is different when we need to design an architecture from scratch. I have designed dozens of architectures throughout my career. I have had to make decisions about integration, data, scalability, availability, security, cloud, and operations in very different contexts. I know that there are several reasonable ways to solve most of the problems I encounter. And yet, I often feel overwhelmed when I start a design from scratch. Not because of a lack of experience, but because of the excess of options.

The starting point should be simple: what requirements does the solution need to meet? What availability is required? What data volume do we expect? What latency is acceptable? What are the cost, security, operational, and compliance constraints? How important is the ability to evolve or migrate the solution in the future? In theory, these answers should reduce the decision space. In practice, even after establishing the constraints, we can still arrive at dozens of technically viable solutions.

And that is where I usually go back to the basics. I choose AWS services that I already know well, rely on patterns that have already worked in other projects, and avoid, when there is no strong reason to do so, introducing a completely new technology or architecture. There may be conservatism in this choice. There may also be a certain lack of experimentation. But there is something more pragmatic: I know the risks of what I have already used better.

Experimenting with a new solution in another cloud, introducing multiple clouds, or adopting a technology that I do not yet know deeply can produce a technically interesting architecture. But it can also result in a solution that does not meet the requirements as well, that the team struggles to operate, or that turns into technical debt when the reality of the project proves different from what we imagined. Responsibility for the decision does not disappear simply because the technology is new.

The problem is that the consequences do not always appear immediately. Dissatisfaction with a choice, technical debt, and even regret over having adopted a particular technology may emerge months after implementation, when the system has already accumulated data, integrations, and dependencies around it. A decision that seemed reversible can then delay a project or make its replacement so costly that it ceases to be a viable alternative.

I have already written about part of this dilemma in [“Cloud Computing: choosing beyond the default”](https://cpzjunior.substack.com/p/cloud-computing-escolhendo-alem-do), discussing why we should not automatically accept the default choices offered by the cloud. The problem that interests me here is one step further: even when we know that alternatives to the default exist, how do we decide which ones actually deserve to be considered?

The more technologies we know, the larger the solution space we are able to see. And the larger this space becomes, the harder it is to evaluate each alternative with the depth required to make a truly conscious decision.

This is happening precisely while building systems has never been easier. The cloud has transformed much of infrastructure into consumable services. SaaS has transformed entire capabilities into APIs. Managed platforms have eliminated an enormous amount of operational work. And artificial intelligence is also reducing the cost of implementing and experimenting with software.

The result is a paradox: we are getting increasingly better at building solutions, but that does not mean we are becoming equally better at deciding which solutions to build.

I am not arguing that modern systems are worse, nor that we should go back to managing servers, configuring infrastructure manually, or avoiding new technologies. That would be precisely the opposite of what these advances represent. The point is that, by making certain parts of the problem easier, these technologies have also changed the nature of the decisions that remain.

When the cost of implementing alternatives drops drastically, the problem becomes not just how to build, but increasingly how to choose.

## Complexity Has Not Disappeared. It Has Moved.

One of the great virtues of abstraction is precisely that it allows us to stop worrying about certain details. We do not need to know the internal implementation of a service in order to use it. This is one of the fundamental principles behind much of modern software engineering.

The cloud has taken this principle to an enormous scale. For a long time, building a system meant dealing directly with a considerable amount of infrastructure. Servers, storage, networks, load balancers, capacity, replication, and disaster recovery were part of the problem because there was no way to simply delegate them.

Today, much of this can be consumed as a service. A database can be provisioned in minutes. A queue can be created through configuration. Capacity can be adjusted automatically. A function can be executed without us having to manage the server on which it runs.

This has enormously reduced the cost of implementation. But reducing the complexity of one layer does not necessarily reduce the complexity of the system as a whole.

Complexity can simply move somewhere else. Instead of needing to know how to build each component, we need to decide how to combine them. An individual service may be simple to consume, while the system formed by the composition of dozens of them may exhibit behaviors that are difficult to predict.

This change also alters the type of knowledge required from an architect. It is no longer enough to know how to implement a particular mechanism, nor is it necessary to know all the details of its implementation. What is required is an understanding of the properties relevant to the decision: its guarantees, its limits, its failure models, its costs, and, above all, how these properties interact with those of the other components.

## The Paradox of Choice

There is a concept known as the paradox of choice: increasing the number of alternatives available does not necessarily produce better decisions. The so-called “supermarket dilemma” illustrates this well. Faced with a shelf containing dozens of seemingly similar options, choosing can become harder, not easier. After a certain point, comparing alternatives requires so much effort that we end up preferring what we already know, simply because the cost of deciding is lower.

Solution architecture seems to have developed its own version of this problem. For a long time, many architectural decisions were constrained by what was possible to build with the resources available. Today, for an increasing share of problems, the situation is almost the opposite. We have dozens of services capable of solving the same need and countless ways to combine them. The problem has shifted from finding a technology capable of doing something to deciding which of the technologies capable of doing it should be used.

And the difficulty does not grow only with the number of alternatives. Each alternative has different properties and creates new possibilities for composition. Choosing a database is not an isolated decision. The choice affects the data model, integration mechanisms, backup strategies, observability, operational costs, and even the technologies that begin to make sense in the following layers. The decision space can grow rapidly as these choices combine.

This is where the architect’s experience becomes particularly important. An experienced architect does not evaluate every possibility. They use accumulated knowledge, problem constraints, and heuristics to quickly eliminate what does not need to be considered. An important part of architectural experience is precisely knowing which options can be discarded without deeper investigation.

My AWS “basics” are, to a large extent, a consequence of this. They are technologies I know, whose properties and limitations I have already encountered in previous projects, and whose risks I can estimate more accurately. When I choose a familiar solution, I am not necessarily seeking the most sophisticated technology. I am deliberately reducing the decision space so that I can devote attention to the decisions that actually matter.

The risk appears when this heuristic stops being a conscious choice and becomes merely a reflex. If I always choose what I know because there are too many options to evaluate, I may be trading cognitive overload for architectural debt.

The abundance of alternatives, therefore, does not merely make the problem broader. It increases the importance of knowing which alternatives do not need to be considered. The architectural challenge becomes less about knowing every possibility and more about building sufficiently good criteria for eliminating them.

## When Abstraction Hides Limitations and Dependencies

There is another effect of abstraction that deserves attention. When we consume managed services, we begin to see only part of the architecture on which we depend. Our diagram represents what we decided to model, not necessarily everything that sustains the system.

This is not necessarily a problem. We do not need to know every detail of a platform to use it correctly. The problem appears when we confuse interface simplicity with independence between components.

When we put an S3, a Lambda, or a DynamoDB on a diagram, what exactly are we representing? Object storage, an executable function, a database. But what exists underneath these abstractions? How are the data distributed and replicated? How are resources provisioned and shared? What are the limits of these abstractions? What dependencies exist between them and the infrastructure that supports them? And, most importantly, which of these properties can become relevant when something fails?

We do not need to know all these mechanisms to use the services. But that does not mean they cease to exist or that their properties are irrelevant to certain architectural decisions.

A system can appear to be distributed across different services, regions, or even different clouds and still depend on common components that do not appear on our diagram. The diversity we see at the surface does not guarantee independence at every layer.

The 2022 Cloudflare incident is an example of this kind of invisible dependency, although I have already explored that incident in another article. For this discussion, the idea is enough: abstractions can hide not only implementation details, but also dependencies and common points of failure that are relevant to an architecture’s resilience.

The same applies to the cloud providers themselves. Different platforms may offer an enormous variety of services, but depend on the same suppliers or shared components in parts of their technology chains. Abstraction allows us to treat these services as independent building blocks because that is how we need to consume them. That does not mean they are completely independent in reality.

This is one of the important limits of architectural abstraction. We can deliberately ignore details that are not relevant to a particular decision, but we need to recognize when they stop being irrelevant. A dependency that may be perfectly acceptable for an ordinary application can become critical when designing for high availability, disaster recovery, or a multi-cloud strategy.

The architect does not need to know everything that exists beneath an abstraction. They need to know enough to recognize when its limitations or dependencies may change the decision they are making.

## AI Makes the Problem Worse

Artificial intelligence adds another dimension to this transformation because it further reduces the cost of implementation. Discussions about AI in software engineering tend to focus on productivity: how much code we can produce, how many tests we can generate, or how much time we can save. These effects are relevant, but there is a less discussed architectural consequence.

If it becomes cheaper to implement an alternative, it also becomes cheaper to experiment with alternatives. This is positive. Experimentation is one of the best ways to reduce uncertainty. The problem is that reducing the cost of experimentation also increases the number of solutions we can put into practice before we even have clarity about which one we should choose.

AI is a particularly clear illustration of this phenomenon. There is a growing number of models available, offered by different providers, with differences in capability, cost, latency, context, and behavior. New models appear continuously, versions are updated, and benchmarks change. For someone designing a solution, this means that even an apparently simple decision, such as choosing a model for a particular task, can involve a space of alternatives that is difficult to keep track of.

And the problem does not end with the model. A solution using AI may involve inference strategies, retrieval mechanisms, vector databases, prompting techniques, tools, agents, and different forms of integration. Each of these choices opens up new possibilities for composition. The technology has not merely added another tool to the catalog. It has rapidly expanded the space of solutions an architect can consider.

AI also drastically reduces the cost of experimenting with these alternatives. An idea that previously required days of development can be turned into a prototype in a few hours. That is an unequivocal advantage. But there is an interesting asymmetry: the cost of building and testing a solution can fall much faster than the cost of understanding its architectural consequences.

We can therefore reach implementation before reaching understanding. We can build a functional prototype, integrate it with other services, and even put it into production before having a sufficiently clear view of its costs, limitations, dependencies, and behavior under different conditions.

That is precisely why I consider AI evidence, rather than merely another example, of the phenomenon discussed in this article. It shows particularly clearly that we are reducing the cost of turning decisions into software without reducing the cost of making good decisions to the same extent.

AI does not eliminate the architecture problem. It makes the difference between being able to build something and knowing whether we should build it that way more apparent.

And that difference matters because the cost of an architectural decision rarely appears when the decision is made.

## The Cost of a Decision Appears Later

A poor architectural decision does not need to immediately produce a broken system. Often, it produces a system that works perfectly within the assumptions that existed at the time of the choice.

The problem appears when those assumptions change. A decision can introduce vendor coupling, a data model that is difficult to migrate, an operational dependency, an architecture that is difficult to scale, or a technology that requires highly specific skills. As the system grows, what seemed like a simple choice becomes increasingly difficult to reverse.

Technical debt has a good analogy in credit card debt. The problem is not only what we postpone, but the interest that begins accruing while we delay the correction. In architecture, that interest is paid in the form of complexity, coupling, and cost of change.

A change that initially required only a small adaptation may, a few years later, involve data migration, contract changes, integration changes, team training, component rewrites, and operational disruptions. The system grows around the original choice, and each new dependency makes reversing it more expensive.

For this reason, technical debt is not merely accumulated work. It is the growing cost of maintaining a decision that is no longer appropriate.

There is an important difference between implementation cost and reversibility cost. A managed service can solve a problem in hours. An architecture built around it can remain for years. The more the system comes to depend on that choice, the greater the cost of abandoning it tends to become.

This changes how an architectural decision should be evaluated. It is not enough to ask how much it costs to implement a solution. We must also ask how much it costs to change it, what assumptions support the choice, and how easy it will be to reverse if those assumptions stop being true.

This concern becomes even more important precisely because technology has made adoption so easy. The lower the cost of getting started, the greater the temptation to postpone the question of how much it will cost to leave.

## The Problem with Frameworks

It was in this context that I began to notice something else. My background in project management accustomed me to the idea that a discipline can build a relatively stable body of knowledge, capable of organizing concepts, practices, and decisions even when the tools and methodologies used change.

In solution architecture, I do not see the same level of consolidation. There are quite useful frameworks, methods, and practices, but they seem to solve different parts of the problem. Often, the architect themselves has to combine these pieces to build their decision-making process.

TOGAF is a good example. It has an important role and never intended to be a System Design manual. It was designed for Enterprise Architecture, with a much broader concern for organization, capabilities, governance, processes, and strategic alignment. Therefore, it does not seem fair to criticize it for not solving a problem that is not exactly its own.

Still, there is a legitimate discomfort when we look at the speed with which the technological environment has changed. The body of knowledge needed to discuss architecture seems to change faster than we can consolidate it. And this creates a difficult tension: if a framework continuously incorporates new technologies and practices, it risks quickly becoming obsolete; if it remains stable, it risks drifting away from the reality in which architects are making decisions.

arc42 illustrates another side of this issue. It is much closer to the practice of software architecture and provides a pragmatic structure for documenting context, quality requirements, architectural decisions, building blocks, runtime, and deployment. It is extremely useful for organizing and communicating an architecture. But documenting a decision is not exactly the same as structuring the process that led to it.

The same applies to other practices. An Architecture Decision Record helps record a decision. C4 helps represent the architecture. ATAM helps explore certain trade-offs. Each of these approaches solves a real problem and can be quite useful. What I feel is missing is a structure that connects these practices into a comprehensive architectural decision-making process.

An ADR can record that three alternatives were considered and that one of them was chosen. But recording a decision is not the same as structuring the process that led to it. What criteria should be considered? How should trade-offs be evaluated? How should cost, risk, operational complexity, team capability, reversibility, and vendor dependency be weighed? When is a decision important enough to be formalized? When should it be revisited?

These questions still depend, to a large extent, on the experience and judgment of whoever is designing the system.

Perhaps that is precisely why, in practice, it is so common to find an architecture represented directly by cloud components in Draw.io, Lucidchart, Miro, or an equivalent tool, without any architecture framework explicitly appearing in the process.

The diagram begins to be built from the available services. An API here, a queue there, a managed database, some serverless function, perhaps an observability service. The architecture emerges from the composition of the components.

This does not mean that architectural reasoning does not exist. It does. The problem is that much of it remains implicit. The diagram shows what was chosen, but does not necessarily show why it was chosen, which alternatives were considered, which assumptions support the decision, or how much it would cost to undo it.

And perhaps that is the gap that really bothers me. I do not miss a framework that tells me which technology to use. I miss a body of knowledge that helps structure and communicate architectural decisions without relying exclusively on the individual experience of each architect.

## A PMBOK for Solution Architecture

It was at this point that I began to better understand that initial feeling that something was missing. I do not miss a framework that tells me which technology to use. That would be unfeasible in an environment that changes so rapidly. I miss something closer to what PMBOK represents for project management: a body of knowledge that provides a language, principles, and structures for organizing the decision-making process without prescribing the solution.

When I talk about a “PMBOK for Solution Architecture,” I am not imagining a manual that tells us which database, cloud, or architectural pattern we should choose. The idea would be to have a reference that helps the architect structure the problem and make the reasoning behind decisions explicit, without turning architecture into a mechanical process.

arc42 comes quite close to some of these goals. It provides a pragmatic structure for organizing and communicating an architecture and is a very useful tool. But it also highlights the distinction I am trying to make: structuring and documenting an architecture is not exactly the same as structuring the decision-making process that led to it.

The same applies to other practices. ADRs help record decisions, C4 helps represent architectures, and ATAM helps explore certain trade-offs. Each of these approaches solves a real problem. What I feel is missing is a structure that connects these practices into a more comprehensive process, without requiring each architect to assemble that process alone from different references.

Perhaps there is a reason for this. Architecture is deeply contextual, and architectural decisions rarely have an objectively correct answer. An excessively prescriptive methodology could create a false sense of precision or turn architectural judgment into compliance with steps. It would make no sense to replace the architect’s experience with a checklist that attempted to determine the correct architecture for every situation.

Still, I believe it is possible to systematize part of this knowledge. Project management offers an interesting reference. PMBOK does not determine which project should be executed or which decision a project manager should make. It organizes knowledge, processes, and practices that help structure the work across different contexts.

Solution architecture could draw from the same source. Not by copying its processes, but by adopting a similar approach to systematization: transforming dispersed knowledge into a discipline that helps structure decisions, make assumptions explicit, communicate reasoning, and preserve the judgment of the person designing the system.

The challenge would be finding a level of abstraction stable enough to survive technological changes and, at the same time, concrete enough to help someone make a real decision. The goal would not be to keep up with every new technology, but to provide a structure that continues to make sense when technologies change.

Perhaps this is one of the next frontiers in the discipline’s maturity: transforming the knowledge that today is scattered across frameworks, methods, practices, and, above all, the individual experience of architects into a more systematic body of knowledge for architectural decision-making.

## The Bottleneck Has Moved

Perhaps the question is not whether systems are becoming easier or harder. They are becoming easier to build and, precisely because of that, harder to design.

Cloud, managed services, SaaS, and AI have drastically reduced the cost of implementing and experimenting with solutions. The bottleneck has shifted from implementation to judgment: deciding what to build, which alternatives to discard, which trade-offs to accept, and which consequences we are willing to carry.

This also changes what we expect from a solution architect. Knowing more technologies remains important, but it is not enough. As the solution space grows, it becomes increasingly important to know how to reduce it consciously. Perhaps the most valuable architect is not the one who knows the most services, but the one who can eliminate alternatives without eliminating the right ones.

That is why the lack of a “PMBOK for Solution Architecture” bothers me. Not because we need another framework to keep up with the next technology, but because perhaps we need a more consolidated discipline for making decisions in an environment that is constantly changing.

Building a solution has never been the goal of architecture. The goal is to make good decisions about what is worth building and to preserve, as much as possible, the ability to change our minds when the assumptions change.
