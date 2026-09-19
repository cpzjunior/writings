# What if the future of enterprise software is not Micro-SaaS, but the Business Cloud Workspace?

_From application specialization to a platform that absorbs software, agents, knowledge, and business relationships_

**Summary:** I argue that the future of enterprise software may not lie in creating an application for every need, but in building a platform capable of bringing together different capabilities within a single environment. I call this idea the Business Cloud Workspace: a space that combines specialized software, agents, data, knowledge, and integrations under an experience oriented around work, not products. AI makes this more viable by translating how a company thinks into structures, workflows, and automations, while a plugin ecosystem allows new capabilities to be incorporated without creating new silos. The differentiator lies in generating lock-in through delivered value: the more a company builds and operates within this environment, the more it becomes part of its way of working, making continued use a consequence of value rather than dependence.

---

I have been following the Micro-SaaS community for some time, and I really like the perspective behind it: find a specific problem, build simple software that solves it very well, and from there create a business. There is something particularly appealing about the idea that a small team can identify a real pain point and turn it into an independent product.

But I increasingly have the feeling that artificial intelligence is threatening precisely this approach. Not because specific problems are disappearing or because Micro-SaaS no longer makes sense. Quite the opposite. AI is making it increasingly easy to turn a specific need into software. And when building a given capability stops being a significant barrier, the isolated functionality becomes less defensible.

This naturally leads me to a question: if specialized software is becoming increasingly abundant, where will the value be?

For a long time, the evolution of enterprise software seemed to be moving toward specialization. ERP handled operations, CRM handled customers, HR software handled people, another application handled projects, another contracts, another expenses. SaaS made it economically viable to turn practically any need into an independent product. Micro-SaaS took this logic to the extreme: if there is a specific pain point, there can be specific software to solve it.

This logic made sense. Building software was expensive, and finding a need specific enough to serve better than large vendors could be an excellent opportunity. A small team could turn a single functionality into a product and, from there, build a company.

But this equation is changing. The amount of software available has grown enormously, while artificial intelligence is reducing the cost of building new applications and functionalities. If a capability can be implemented, reproduced, and customized increasingly quickly, we will probably have more specialized software than ever before. That does not mean Micro-SaaS will disappear. Perhaps the opposite will happen. The question is where this software will live.

In a previous article, “[Why are modern systems becoming easier to build and harder to design?](https://cpzjunior.substack.com/p/por-que-sistemas-modernos-estao-ficando)“, I argued that cloud and AI are making solution implementation increasingly accessible, but that this does not necessarily mean less complexity. Complexity does not disappear; it changes location. Instead of having to build each component, we need to decide how to combine them and live with the consequences of those choices.

Enterprise software seems to be going through the same process. SaaS has made it much easier to acquire a specific capability. AI is making it easier to build new capabilities. But at the same time, a company needs to manage a growing number of applications, integrations, contracts, credentials, data, and dependencies distributed across different vendors.

Perhaps the next evolution is not to add even more applications to this ecosystem, but to create a layer capable of absorbing this abundance without transferring all of its complexity to the people who need to use it.

This is where the idea I provisionally call Business Cloud Workspace, or BCW, comes from.

## The cost of fragmentation

SaaS solved an important part of the enterprise software problem: it made acquiring a capability much simpler. Instead of buying infrastructure, hiring a team, or developing a solution internally, a company can simply subscribe to a service.

The problem is that this simplicity of acquisition does not necessarily translate into simplicity of operation. A small company may start with a few perfectly reasonable choices: a CRM for sales, a financial solution, a communication tool, another for documents, another for projects, and a few specific applications for particular needs. Individually, each decision seems simple. Complexity appears when these tools need to work together.

Each system has its own data model, authentication, permissions, interface, billing policy, and integration mechanisms. People need to know where a particular piece of information is, which system to use for each task, and how to make a process cross different applications.

There is also a financial cost that tends to be underestimated. Each application may seem inexpensive in isolation, but the sum of dozens of subscriptions represents a significant recurring expense. In addition to the subscription fee, there are costs associated with implementation, integration, training, administration, and maintenance. The ease of acquiring software can, paradoxically, make it easier to accumulate software than to evaluate the total cost of maintaining it.

Fragmentation also increases vendor dependency. Each new service introduces a relationship that needs to be managed, with its own pricing policies, security, availability, product evolution, and contractual terms. The company becomes dependent not only on its own systems, but on the continuity and decisions of a collection of external vendors.

This also creates a supply chain problem. A vulnerability, outage, or significant change at a vendor can affect processes that the company does not directly control. The greater the number of external services participating in the operation, the larger the dependency surface that needs to be monitored.

But there is an even less visible cost: cognitive cost. When moving from one application to another, a person is not simply changing windows. They need to mentally reorganize the information related to the task, recover what they were doing, and adapt their way of thinking to how that application presents the problem. Alt+Tab solves the window-switching problem, but it does not solve this cognitive effort.

When a task crosses several applications, this effort accumulates. Part of the person's attention stops being focused on the business problem and starts being used to reconstruct, with each application, the mental context necessary to continue working.

The problem, therefore, is not necessarily having too much software. Some specialized solutions are perfectly justified. Software can solve a specific need so well that it is worth incorporating into the operation. The issue arises when each new capability adds another boundary that needs to be managed financially, technically, and cognitively.

Artificial intelligence may make this scenario even more extreme. As software becomes cheaper to produce, it becomes economically viable to create tools for increasingly smaller and more specific needs. The result may be even greater abundance of specialized applications: more available capabilities, but also more decisions about where to find them, how to connect them, and who will be responsible for maintaining them.

Specialization reduces the cost of building each component, but it can transfer part of the cost to those who need to operate the whole. The cheaper it becomes to create software to solve specific problems, the greater the effort required to manage all that software as part of a coherent operation may become.

This is where an opportunity emerges. Perhaps we do not need less specialized software. We need a layer capable of absorbing it. Instead of every new need necessarily resulting in another independent application, it could be incorporated into the existing environment as a module, plugin, agent, or integration.

The value, in this scenario, would not lie only in the individual capability offered by each piece of software, but in the infrastructure that allows them to be combined coherently: context, data, identity, permissions, integration, governance, and experience.

The question stops being how to create fewer applications and becomes how to enable a company to use more software without proportionally increasing cost, dependencies, and cognitive complexity.

This is precisely where the BCW starts to make sense.

## A cloud for the business

The idea of the BCW begins with a simple inversion: instead of organizing software around the applications a company needs to purchase, organize it around the capabilities it needs to use. The platform would function like a cloud, offering these capabilities on demand and allowing each company to progressively compose its own operating environment.

On AWS, I do not need to decide my entire architecture in advance. I can start with storage, add a database, create a virtual machine, and, as the need arises, incorporate new services. I can build an extremely simple MVP or a sophisticated enterprise architecture using the same infrastructure.

What changes is not the platform, but the combination of resources I use and the level of complexity I choose to expose. The BCW would apply this logic to the business. A company could start with a few basic capabilities and, as it grows, incorporate resources for sales, finance, people, projects, payments, reconciliation, automation, or any other need that arises. These capabilities would not need to appear to the user as independent systems. They could share data, identity, permissions, workflows, and context within the same environment.

This allows a task to be treated as a task, rather than as a sequence of applications. If solving a problem requires customer data, a contract, financial approval, and a document, the user should not need to know in which systems this information is stored. The BCW should gather the necessary context and present the experience as a single operation.

The platform would also not need to build everything internally. Just as a cloud provides fundamental services on top of which other solutions can be built, the BCW could provide enterprise primitives so that third-party modules, agents, and specialized applications could be incorporated into the environment. Identity, data, permissions, billing, workflows, and governance could be the platform's responsibilities, while developers and partners would focus on the specific capabilities they want to offer.

This is an important difference from the traditional logic of enterprise suites. The goal would not be to offer a closed set of products capable of covering every area of the company, but to provide infrastructure on which the company itself can assemble its work environment.

Software would stop being organized around product boundaries and start being organized around what the company needs to accomplish. The result would be a kind of business cloud: a platform that allows a company to start small, incorporate new capabilities as they become necessary, and grow without having to rebuild its operation at every new stage.

## From MVP to operation

One of the most interesting characteristics of a cloud is its ability to allow the same infrastructure to support projects with completely different levels of sophistication. A developer can start with a simple application and, if it works, use the same foundation to build a much more complex operation.

The BCW could apply this principle to creating businesses. Today, turning an idea into a company requires building a significant amount of infrastructure that is not necessarily part of the hypothesis being tested. You need to deal with authentication, users, permissions, documents, payments, communication, internal processes, and a series of other capabilities before even knowing whether there is a business.

In “[Before taking an idea off the page, you need to put it on the page](https://cpzjunior.substack.com/p/antes-de-tirar-uma-ideia-do-papel)“, I discussed how an MVP involves much more than implementing a few functionalities. Before an idea reaches the market, decisions need to be made about product, experience, architecture, data, security, operations, and execution. Many of these are simply the price of building the infrastructure necessary for the experiment to exist.

The BCW could abstract part of this work. Someone experimenting with an idea could use the capabilities already available on the platform and focus their energy on what they actually need to discover. Authentication, users, permissions, documents, payments, communication, and workflows would not need to be built from scratch just to get the first version of the business running.

This changes the meaning of MVP. The goal stops being to build a small version of all the infrastructure required to operate a company and becomes building only what is necessary to test the hypothesis.

If the hypothesis is validated, the same solution could continue evolving within the environment. What started as a simple operation could incorporate more sophisticated processes, new users, agents, integrations, and modules without requiring a complete reconstruction of the infrastructure.

This creates a particularly interesting property: the distance between experimenting with a business and operating it can become smaller. Today, validating an idea and structuring a company are often treated as different problems. First we build the MVP; then we need to choose and deploy the systems that will support the real operation.

In a BCW, these two moments could be part of the same trajectory. The platform could be simple enough not to interfere with the experiment and deep enough to support whatever comes next.

## The experience as the product

This leads to what I consider the main differentiator of the BCW: the experience. There is a difference between having a coffee at the bar on the corner and having a coffee at Starbucks. In both cases, the fundamental need may be exactly the same: having coffee. What changes is everything around it. The environment, consistency, ordering process, payment, personalization, predictability. The product is not just the coffee. It is the way the necessary elements have been organized so that the customer does not have to think about them.

Enterprise software can follow the same logic. A traditional all-in-one tries to bring different products together under the same vendor. A product like Zoho can offer CRM, finance, projects, HR, and other applications in the same suite. This reduces the number of vendors a company needs to manage, but does not necessarily eliminate the boundaries between products. The user still needs to understand which application to use, where a given capability is available, and how a task crosses different modules.

The BCW starts from a different premise: the unit of experience should not be the product, but the work the company needs to accomplish. The user should not enter the environment thinking about which system they need to open. They should simply think about what they need to do. If they need to hire a supplier, the platform presents the process. If they need to consult a contract, they find the document and its related context. If they need to discover an internal policy, they consult the knowledge base. If they need to execute a repetitive activity, they can delegate it to an agent. A task that requires financial information, customer data, and an approval should appear as a single operation, even if different capabilities are involved behind the scenes.

This distinction is fundamental. An all-in-one organizes the experience around the products it offers. The BCW should organize it around the work that needs to be done. Therefore, CRM, finance, HR, documents, agents, workflows, and third-party modules would not need to be presented as different destinations within the platform. They would be capabilities that can be combined as the task requires. Integration, in this model, stops being an activity the user needs to understand. It becomes a property of the environment.

This also changes what it means to compete on features. The goal is not to offer an application for every need, but to allow a company to solve its problems without having to know the architecture required to do so.

The Starbucks example helps explain this difference. The value lies not only in what is offered, but in how the elements necessary for the experience have been organized in a consistent and predictable way.

In the BCW, the product would also not be the sum of the applications. It would be the experience that emerges when they stop being the center of the interaction.

## AI as an interpretation layer

Artificial intelligence can be fundamental to reducing one of the greatest barriers to adopting enterprise software: the need to translate how a company operates into the language of the system.

A company knows its own business, but that does not mean it knows the structure required to represent it within software. Traditionally, this translation requires configuration, consulting, training, and often development. The user needs to learn how the system organizes entities, relationships, workflows, and permissions before they can use it fully.

AI can function as an interpretation layer between how the company describes its business and how the platform needs to represent it. A company could import its spreadsheets and allow the platform to identify customers, suppliers, products, employees, and relationships between these entities. It could import documents, policies, and procedures. It could connect existing systems and allow the platform to help map their structures.

Likewise, the user could explain what they need in natural language and let the platform determine which data, capabilities, and workflows are necessary to execute it.

The goal would not simply be to import data or allow natural-language commands. It would be to reduce the distance between how the company thinks about its business and the structure required to represent it in software.

This is particularly important for small companies. The smaller the organization, the less likely it is that there will be someone dedicated to managing enterprise systems or translating business processes into software models. The platform needs to assume a greater share of this work precisely where technical capacity is lower.

This interpretation could also happen continuously. As the business changes, the BCW could transform new needs described by the user into structures, workflows, automations, and configurations, without requiring the company to know in advance the best way to model them.

A good enterprise platform should not require the user to learn to think like the system. It should be able to understand how the company thinks and translate that into the system.

In this sense, AI is not merely a BCW feature. It is part of the abstraction itself that makes it possible to hide the platform's complexity without eliminating the capabilities that exist behind it.

## Knowledge bases and AI agents

Once data, documents, and processes are in the same environment, organizational knowledge can stop being merely documentation and become part of the operation itself.

The company could maintain a wiki within the BCW, but a wiki connected to the rest of the platform. Policies, procedures, manuals, decisions, and lessons learned could be related to the processes that implement those rules.

This knowledge could be structured as a kind of wiki as code: versioned, organized, and governed by the company itself, while AI would use it as context to answer questions, execute processes, and guide agents.

A policy could become an execution rule. A procedure could become a workflow. A recurring guideline could give rise to an agent. In this context, agents would not simply be conversational assistants. They would be operational components of the company, capable of accessing platform resources, consulting the knowledge base, executing workflows, and operating within the permissions defined for them.

The company could customize not only what an agent knows, but also how it works. A process could have its own agent, with objectives, permissions, tools, and decision criteria defined by the organization.

Even the strategy used to solve a problem could be part of this configuration. An agent could be instructed to work according to PDCA, while another could use OODA or a specific methodology defined internally. The methodology would stop being merely a documented guideline and become part of the agent's execution logic.

The same principle would apply to workflows. Instead of simply choosing between predefined processes, the company could adapt stages, approval rules, conditions, and responsibilities according to its way of operating.

The result would be a different layer of customization. The company would not merely be storing its knowledge within the BCW. It would be transforming that knowledge into operational behavior.

And all of this could happen within the platform itself. It would not be necessary to develop an agent from scratch, create an MCP server, build specific integrations, or maintain a parallel architecture just to connect AI to the company's systems. The necessary primitives would already be available in the environment.

The BCW would therefore stop being merely the place where the company stores information and executes processes. It would also become the place where it defines how those processes should work and how agents can execute them.

## Micro-SaaS as plugins

This is where Micro-SaaS can find a new role. Instead of disappearing, it can stop necessarily being an island.

A platform of this kind could have a Marketplace where developers create modules for needs that the main vendor could never anticipate. An extremely specific product for a particular industry, an integration with a legacy system, a specialized workflow, or a new AI capability could be installed directly into the BCW.

The best analogy might be Skyrim mods. Bethesda did not need to imagine every functionality, story, map, and experience that players might want. It created a game extensible enough for an entire community to build upon.

A BCW could work similarly. The vendor would build the common infrastructure, while a developer community could create capabilities that the central company would never have the capacity or incentive to anticipate. The difference is that, in this case, mods would not merely add content. They could add real capabilities to the business.

The developer would not need to rebuild all the enterprise infrastructure required to deliver their functionality. Identity, permissions, data, billing, workflows, and other primitives could be provided by the platform. They would focus on the specific capability they want to offer.

This changes the nature of Micro-SaaS. Instead of each product needing to acquire customers individually, deploy its own infrastructure, and create another data island, it could be distributed as an extension of the environment the customer already uses. The developer gains access to an existing customer base. The customer gains a new capability without having to adopt another system.

This dynamic also reduces the cost of experimentation. A developer can create a module for a very specific niche without having to build all the enterprise infrastructure around it. If there is demand, the module grows within the ecosystem. If there is not, the cost of failure is lower.

But this openness brings an inevitable consequence: the more things that can be built on the BCW, the greater the need for governance. Allowing third parties to create modules, agents, and workflows means dealing with identity, permissions, isolation, security, auditing, versioning, observability, billing, and policies. The platform would need to provide components running on it with governance infrastructure similar to what a cloud provides to workloads. Freedom would lie in what can be built. Control would lie in the infrastructure that enables those things to be built safely.

The BCW, therefore, should not be an attempt to centralize all enterprise software under a single vendor. Its function would be to centralize the experience and common primitives while keeping open the possibility of incorporating specialized software.

If the best payroll system remains external, it can be integrated. If a better legal solution emerges, it can participate in the environment. If a developer creates a specialized tool superior to the native module, it can be installed.

The BCW vendor does not need to anticipate every need or build the best solution for each one. The more extensible the platform, the less necessary it becomes to anticipate the future. The vendor builds the substrate; the ecosystem discovers what should exist on top of it.

In this scenario, the Marketplace would not merely be a distribution channel. It would be part of the mechanism through which the BCW evolves faster than the company that built it.

The BCW does not need to replace all software. It needs to make leaving it unnecessary in order to use that software.

## Lock-in through value

This architecture also creates a different kind of lock-in. There is lock-in based on restriction, in which the customer stays because leaving is difficult. There is another, more interesting kind, based on value: the customer stays because the platform has become the natural environment in which they solve their problems.

This is how I think about a platform like AWS. When a platform becomes familiar enough, when facing a new problem the question stops being “which vendor should I hire?” and becomes “how do I solve this within the platform I already use?”

The BCW should seek something similar in the enterprise context. Over time, a company would not merely use the platform. It would build on it. Its processes, workflows, agents, integrations, and knowledge would be shaped according to its own way of operating.

At that point, the BCW would stop being merely the software the company uses. It would become the environment the company itself built for itself.

Skyrim also offers an interesting analogy here. After hundreds of hours and dozens of installed mods, the player is not simply playing the product Bethesda delivered. They are playing a version of the game shaped by their own choices.

The same could happen to a company. After years, the BCW would no longer be a generic tool. It would be a version of the platform shaped by the organization itself: with its processes, knowledge, agents, and particular way of working.

This is where lock-in through value becomes interesting. The real lock-in would not be preventing exit. It would be making exit a regression. The company would continue using the BCW not because it was trapped in it, but because it had built a way of working there that it would not find ready-made anywhere else.

## From Workspace to Business Network

When the BCW begins to concentrate a company's operations, connecting different companies becomes a natural evolution. If the platform knows an organization's processes, people, documents, suppliers, and needs, it also possesses part of the context necessary to facilitate that organization's relationships with others.

VTEX offers an interesting reference. Instead of treating e-commerce merely as an isolated application, its platform participates in an operation that connects companies, consumers, sellers, payments, orders, and other elements of the transaction. The BCW could take a similar logic beyond e-commerce, turning the business work environment itself into a layer for relationships between organizations.

This could begin with a public services catalog. A supplier could register its company, products, services, capabilities, service regions, and commercial terms. This catalog would be accessible even to companies that do not yet use the BCW, creating a public discovery layer over the Business Network.

From there, discovery and operation could be part of the same flow. A company could search for a service provider, compare alternatives, request a quote, negotiate, contract, issue an order, and make payment without having to reconstruct the context across different systems. The supplier, in turn, could respond to the demand, manage the relationship, and operate its own processes within the same environment.

The difference from a traditional marketplace would lie precisely in the context. The platform already knows the buyer's users, policies, approval limits, and processes. At the same time, it can incorporate the supplier's data, services, documents, and history.

A purchase request could begin as an internal need and end as an external transaction, without requiring someone to copy information from one system to another.

This is where the Business Network differs from the Marketplace discussed earlier. The Marketplace connects a company to software capabilities. The Business Network connects a company to other companies. In the first case, the ecosystem expands what can be built within the platform. In the second, it expands what can be accomplished through it. The BCW would then stop being merely an individual workspace and also become infrastructure for relationships between companies.

This dynamic would introduce a network effect. The more companies are present, the more suppliers and services can be found. The more suppliers are present, the more useful the platform becomes for companies. And the larger this base becomes, the larger the market also becomes for modules, agents, and solutions developed by third parties.

At this point, the boundary between enterprise software and business infrastructure begins to disappear. The platform not only helps a company operate. It also facilitates the discovery, contracting, and operation of the relationships that allow a company to function.

The ecosystem begins to reinforce the platform itself.

## The risk of creating new complexity

There is, however, a paradox in the proposal itself. A platform capable of doing many things can also become a platform that is difficult to use.

Salesforce is a good example of this challenge. Its platform proposition is powerful precisely because it allows processes, objects, permissions, automations, and integrations to be modeled in depth. But this flexibility also creates an administrative layer that can require specialized knowledge.

It would be entirely possible to turn the BCW into something similar: an extremely powerful platform, with hundreds of features, configurations, permissions, and possibilities, but one that required specialized knowledge to use.

In that case, the platform would merely have shifted the problem. Instead of managing dozens of independent systems, the company would manage a single, excessively complex system.

Abstraction, therefore, cannot merely be a characteristic of the interface. It needs to be part of the product's architecture itself. Complexity must continue to exist for those who need it, but it cannot be a requirement for those who do not.

A small business should be able to operate the BCW without knowing its internal structure. A more advanced professional should be able to access deeper configurations when necessary. An administrator could define sophisticated policies and workflows without forcing every employee to understand them. An enterprise architect could access APIs, integrations, and advanced configurations without turning that same experience into the default interface for every user.

The experience of an entrepreneur and the experience of an enterprise architect can be radically different without them using different products.

This is where AWS offers an important reference. The same infrastructure can serve everyone from those who need only a simple abstraction to those who need to control much deeper details. The platform does not need to choose between simplicity and sophistication. It can offer both, provided it can expose complexity progressively.

The BCW would need to do the same. Its advantage would not lie in eliminating complexity, something that is probably impossible on a platform of this kind, but in ensuring that each person interacts only with the complexity necessary to perform their work.

The platform needs to offer depth without imposing depth. Perhaps this is the fundamental condition for a platform of this kind to remain simple even when what exists behind it becomes extremely sophisticated.

## An idea that is already taking shape

The idea of a BCW may seem like an extrapolation, but its components are already being built separately by different companies.

Salesforce transformed enterprise software into an extensible platform of applications, automations, and data. Microsoft has been bringing productivity, data, development, and agents closer together within the same ecosystem. Shopify and VTEX show how a platform can connect a company's operations to a third-party ecosystem. AWS demonstrated, at another layer, how infrastructure can provide very different capabilities without requiring all users to understand its internal complexity. What has not yet been completely solved is the combination of these ideas into a coherent experience. Perhaps the BCW is not a disruption that is still to come, but the result of movements that have already begun.

AI is making software cheaper to create. Platforms are becoming more extensible. Agents are beginning to participate in operations. Marketplaces are connecting companies to new capabilities. And at the same time, the amount of software a company needs to manage continues to grow.

The question, therefore, may not be whether we will have more software, but where that software will live. Applications grouped into suites, each preserving its own boundary? Or an environment in which applications, agents, data, knowledge, external services, and specialized modules are simply different ways of expanding what a company can do?

The cloud transformed infrastructure into on-demand capability. The BCW could apply a similar logic to enterprise software: not delivering a fixed collection of applications, but an environment capable of incorporating new capabilities as they become necessary.

In this model, the company would not need to choose all the software it will use in advance. It could start small, incorporate new capabilities, connect existing systems, add agents, and install extensions as its operation evolves.

This changes the unit of value. Software stops being merely the application that solves a specific problem and becomes the environment that allows a company to solve different problems without rebuilding its way of working for every new need.

Perhaps this is the most important change. The future of enterprise software may not be an application for every thing, nor necessarily a suite that tries to do everything. It may be a platform on which each company progressively builds its own way of working.
