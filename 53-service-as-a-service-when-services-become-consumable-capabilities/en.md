# Service as a Service: When Services Become Consumable Capabilities

If we have learned to consume infrastructure, platforms, and software as a service, why do we still treat so many services as isolated deliverables?

Summary: In this article, I propose a reflection: if we have learned to consume infrastructure, platforms, and software as services, why do we still treat so many organizational capabilities as isolated deliverables? I believe we can change this perspective by thinking about services that can be continuously discovered, accessed, and consumed by different business areas, applications, and processes. This requires looking beyond project delivery and considering how these capabilities are made available, operated, governed, and evolved over time. This is not about creating yet another architectural model, but about questioning whether we are making the most of the value of what we have already built.

There has been a significant shift in how we consume technology. For a long time, to use a particular computing capability, a company had to purchase equipment, install systems, configure environments, and maintain all the infrastructure required to operate them. The evolution of service models changed this relationship. We began consuming infrastructure, platforms, and software without necessarily owning or managing the resources that support them. More than a technological change, this was a transformation in how we think about access, responsibility, and value.

This evolution led me to a reflection: if we have learned to make infrastructure, platforms, and software available as services, why do we still struggle so much to think about the services our own organizations provide in the same way?

The idea I propose calling Service as a Service starts with this question. It is not about introducing a new architectural model, methodology, or category that needs to compete for space with already established concepts. It is a way of looking at something that already exists but is not always designed to be reused, accessed, and continuously consumed. The idea is simple: what if we started treating an organization's services as capabilities available to different consumers, rather than as deliverables tied to specific projects, teams, or structures?

## From Consumed Technology to Organizational Capability

The idea of consuming software as a service is not new. For decades, companies have used applications hosted and operated by third parties without having to install, administer, or maintain all the infrastructure required to run them. The model gained scale and prominence with the expansion of the internet and, later, cloud computing, but its essence predates these developments: providing access to a technological capability without transferring to the consumer all the responsibility for building and operating it.

With the evolution of cloud computing, this logic began to extend to other layers. Infrastructure, previously acquired and managed directly by companies, became consumable as a service. Development platforms also began to be made available on demand, abstracting away some of the complexity involved in preparing and maintaining technological environments. This is how the models we know as SaaS, IaaS, and PaaS became established.

Although they address different needs, these models share an important characteristic: they change the relationship between those who provide a capability and those who use it. Consumers do not necessarily need to know or manage all the components that make the service possible. They need to understand what is available, how to access it, what results they can expect, and which responsibilities remain under their control. Complexity does not disappear, but it is managed at another layer and, often, by another party. Consumers can therefore focus their efforts on what they intend to accomplish, rather than having to build and operate everything required to achieve the desired outcome.

This logic, already well established in the technology landscape, leads me to a question: why not think the same way about the capabilities that exist within our own organizations?

It is common to find companies where certain capabilities are developed to address a specific need. A project identifies a problem, mobilizes a team, defines a scope, and delivers a solution. The result is then used by an application, a business area, or a process. In many cases, however, the capability remains closely associated with the context that motivated its creation.

The problem emerges when another business area identifies a similar need. Instead of consuming something that already exists, it may be necessary to start a new project, negotiate priorities, find those responsible for the original solution, and build specific integrations. Even when the capability could be reused, its availability is not necessarily evident, access may not be structured, and consumption may depend on informal agreements.

This happens because we often organize technology delivery around projects and systems, but do not necessarily organize the availability of the capabilities those projects produce. A project has a beginning, scope, budget, and end. A capability, on the other hand, can continue generating value for many years, serving different consumers and participating in processes that did not even exist when it was created.

It may therefore be useful to separate the delivery that gave rise to a capability from the capability itself, which remains available afterward. A service does not need to exist solely because a project requires its implementation or because a specific application depends on it. It can be designed to address a recurring need, with different consumers and usage patterns that evolve over time.

This does not mean turning everything into a shared service, nor assuming that every functionality should be exposed to the entire organization. It means recognizing that some capabilities have value beyond the context in which they were initially developed and that this value can be expanded when their availability and consumption are deliberately considered.

## A Service Is Not Just a Product

It is worth making a distinction. When I talk about a service, I am not necessarily referring to a software product or an application. A product is typically recognized by its value proposition, its users, and the experience it provides. A service can sit behind several products and processes, enabling a specific capability without needing to present itself as a complete solution to the consumer.

An application may, for example, provide a payment experience. Behind it are several capabilities: authentication, data validation, risk analysis, authorization, settlement, and notification. These capabilities may be distributed across different systems and teams, but they do not need to be consumed exclusively by the application that first brought them together.

The difference lies in the perspective. When we think only about the product or application, we tend to organize the solution around the end-user experience. When we also consider the capabilities that support it, we begin to see opportunities for reuse and composition. The same service can participate in different products, journeys, and processes, provided there is a clear way to access it and understand its usage conditions.

An analogy helps bring this idea to life. Imagine a financial institution that develops a fraud prevention capability. In a more restrictive model, this capability may originate as part of a card-related project, with rules, integrations, and infrastructure tailored to that context. If another business area wants to use it in an account-opening journey or a funds transfer, it may need to develop its own solution or negotiate a specific integration with the team responsible.

From a service perspective, the fraud prevention capability is designed to serve different business contexts. Each consumer provides the necessary information, receives a risk assessment, and uses the result within its own process. The service can evolve internally, incorporate new analytical models, and improve its detection mechanisms without requiring each consumer to rebuild that capability.

Naturally, this does not mean that all contexts should receive the same response or use exactly the same rules. A card transaction, an account opening, and a funds transfer have different characteristics and risks. The service needs to provide parameters, contracts, and configuration options that accommodate these differences. Reuse does not mean forcing all consumers to do the same thing, but rather avoiding a situation where each one has to independently build and operate a capability that could be shared.

## Consuming Does Not Simply Mean Calling an API

When we talk about making services available, it is common to immediately associate the idea with APIs. They are indeed an important mechanism for exposing capabilities in a structured way, with explicit contracts and integration between systems. But reducing service consumption to API calls would unnecessarily limit the discussion.

A capability can be consumed through different mechanisms, depending on the nature of the interaction. It may have an interface for human interaction, an API for synchronous communication between applications, events to notify consumers of state changes, queues for processing requests asynchronously, or automations to execute recurring activities. The mechanism should be a consequence of the consumption need, not a decision that predetermines what the service can be.

This distinction becomes even more relevant with the evolution of artificial intelligence. AI agents are beginning to act as consumers of organizational capabilities. Instead of simply presenting information or answering questions, they can identify a need, select a tool, request an operation, and combine different services to complete a task.

Initiatives and standards such as MCP and A2A help illustrate this movement. The former is associated with connecting models and agents to tools and context sources; the latter, with communication and collaboration between agents. We do not need to assume that these standards will become the definitive form of integration to recognize the central point: service consumers are no longer exclusively traditional applications and human users.

This increases the importance of making capabilities discoverable, understandable, and accessible through clear contracts. An agent needs to know what a service does, what information it must provide, what results it can receive, and which operations it is authorized to perform. In this scenario, a poorly documented capability or one that depends on informal knowledge becomes even harder to consume.

The question, therefore, is not simply about making more APIs available or adopting new protocols. It is about thinking through the consumption experience of a capability, regardless of who or what is consuming it.

## What Needs to Exist Behind a Service

Making a capability available to different consumers requires more than creating an integration endpoint. A set of conditions must be established to enable its use in a predictable and sustainable way.

The first aspect is the contract. Consumers need to understand what the service offers, what information is required, what results will be produced, and what limitations exist. The contract must also make usage conditions, expected behaviors, and each party's responsibilities clear. Without this, the integration may work technically, but it will continue to depend on tacit knowledge and specific negotiations.

Identity, authentication, authorization, and access segregation must also be addressed. Not every consumer can perform every operation, and different contexts may require different permission levels. Security cannot be an add-on incorporated after the service is already available. It is part of the consumption model itself.

Another consideration is operations. A service consumed by different business areas or applications potentially has a greater impact than a solution restricted to a single context. Availability, performance, capacity, observability, continuity, and failure handling are no longer internal concerns for the responsible team alone; they directly influence the consumer experience. Versioning and compatibility must also be considered, because service evolution cannot arbitrarily disrupt those who depend on it.

All of this requires a clear definition of responsibility. Who owns the service? Who decides how it evolves? Who prioritizes improvements? Who is accountable when the capability no longer meets the expected level? Who assesses the impact of a change on existing consumers?

These questions reveal an important organizational dimension. A service is not sustained merely because there is a technical team capable of maintaining it. There must be ownership of the capability, with responsibility for its evolution and its value over time. This does not necessarily mean creating an independent team for every service, but rather recognizing that responsibility for the capability does not end with the delivery of the project that originated it.

It is a subtle but relevant shift: success is no longer measured solely by the completion of implementation, but also by the quality and continuity of the service made available.

## Sharing Has Costs and Limits

The idea of turning capabilities into consumable services may seem inherently advantageous. Reuse avoids duplication, concentrates knowledge, and allows different business areas to benefit from the same implementation. But sharing also creates dependencies and costs that must be considered.

A service used by many consumers can become a critical point within the organization. An apparently simple change can affect different processes, each with its own rules, priorities, and change windows. The need to serve multiple contexts can increase contract complexity and make evolution more difficult. In some cases, the abstraction created to serve everyone becomes so generic that it no longer serves anyone particularly well.

There is also a risk of excessively centralizing capabilities that should remain close to the business context. Not every functionality needs to be shared. Some are highly specific, have little reuse potential, or depend on local decisions. The cost of creating and operating a common service may be greater than the benefit of reusing it.

Therefore, the question should not be whether to turn everything into a service, but rather how to identify capabilities with the potential to consistently serve different consumers. The decision needs to consider frequency of use, degree of specialization, criticality, maintenance costs, dependencies, and the autonomy required by consumers.

Standardization also has limits. A shared service should not impose artificial uniformity on processes that have legitimate, differing needs. The goal is to provide a common capability without erasing the particularities of the contexts in which it will be used. Finding this balance is part of architecture work, but also of management and governance.

## From Project Delivery to Capability Availability

Perhaps the main reflection prompted by Service as a Service is not about technology, but about how organizations structure themselves to produce and make value available.

In many companies, projects are the primary unit for mobilizing resources and executing change. This makes sense: projects help organize investments, establish objectives, control scope, and coordinate deliverables. The problem arises when this logic also determines how capabilities are maintained and consumed after delivery is complete.

An organization can successfully complete dozens of projects and still accumulate fragmented solutions, redundant integrations, and capabilities that are difficult to reuse. Each initiative solves its own problem, but the whole does not necessarily evolve as a coherent ecosystem.

Thinking of services as consumable capabilities suggests a different perspective. Projects remain important for creating or transforming solutions, but the resulting capabilities can have their own lifecycle. They need to be discovered, accessed, operated, governed, and continuously improved. Their value lies not only in what they delivered in the past, but also in what they can still enable for different consumers.

This vision also brings architecture and management closer together. Architecture no longer looks only at the components and integrations of a specific solution, but also considers how capabilities relate to one another, which can be shared, and what dependencies emerge when different parts of the organization begin consuming them. Management, in turn, needs to consider the continuity of these capabilities, their prioritization, and accountability for their evolution.

This is not about replacing a project-oriented structure with another rigid structure organized around services. It is about recognizing that delivering a solution and making a capability available are related but different problems. Confusing them can make an organization efficient at delivering projects but inefficient at making the most of what it has built.

## A Provocation, Not a New Recipe

Perhaps Service as a Service needs to be nothing more than a provocation. It is not an attempt to rename established concepts, propose a new architecture, or establish a universal model. SOA, APIs, internal platforms, event-driven architecture, and capability management already address important parts of this discussion. What interests me is the question that emerges when we bring these ideas closer to the way organizations actually work.

If we can consume infrastructure, platforms, and software as services, why are so many organizational capabilities still treated as isolated deliverables? Why do we need to rebuild solutions that already exist? Why does access to certain capabilities depend so heavily on knowing the right team, negotiating a specific integration, or finding someone who knows how a particular system works?

Perhaps part of the answer lies in how we conceive our solutions. We build projects, applications, and systems to solve concrete problems, but we do not always think of the capabilities we are creating as something that others can consume independently and continuously.

Changing this perspective does not require turning everything into a service or adopting a specific technology. It requires recognizing when a capability has value beyond its original context and considering, from the outset, how it could be made available to other consumers.

Ultimately, the question is not whether we need another architectural model. It is whether we are making the most of the capabilities we have already built. Perhaps it is time to stop thinking only about the solutions we deliver and start thinking about the services we are capable of continuously providing.
