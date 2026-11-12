# The Architectural Dilemma of MCP

How to distribute capabilities to manage the cognitive complexity of AI agents.

**Summary**: I argue that MCP's main architectural dilemma is not whether to centralize or distribute servers, but how to manage the way their capabilities are discovered, selected, and made available to agents. In enterprise environments, exposing all tools at once increases cognitive complexity and makes contextual selection more difficult. The solution involves separating the global capability catalog, progressive discovery, and execution, combining centralized governance with domain autonomy and intelligent routing. This allows agents to access only what they need, when they need it, without taking on the complexity of managing the entire infrastructure. The challenge is to transform the diversity of enterprise resources into a selective, secure, and efficient ecosystem.

---

In my last article, "[Beyond Generalist Agents: An AI Micro-Agent Architecture](https://cpzjunior.substack.com/p/alem-dos-agentes-generalistas-uma?utm_source=chatgpt.com)", I explored a question that I believe is becoming increasingly relevant as AI agents begin to occupy a more significant place in software architectures: should we continue concentrating responsibilities in generalist agents, or should we start thinking about a more specialized distribution of reasoning capabilities?

In that discussion, one of the ideas that emerged was the need to separate the universe of capabilities an organization possesses from what each agent actually needs to know during execution. A global catalog can be extensive, while each agent's context should be specific and built according to the task it needs to perform.

This premise, however, raises an architectural question worth exploring. If we begin distributing intelligence across different agents, how should we organize and make available the tools and capabilities they use to interact with the world?

This is where the Model Context Protocol (MCP) introduces a new dilemma. Imagine a large organization with dozens of products, hundreds of APIs, and different business domains. Each product begins exposing its functionality through MCP servers, making its capabilities accessible to agents. Initially, the solution seems relatively straightforward: create an MCP server for each product and allow agents to connect to the servers they need.

But this approach quickly raises other questions. What if an agent needs to access dozens of products? Should we connect it to all those servers? Should we make all tools available at once? What happens when the descriptions, parameters, and contracts of these tools begin consuming a significant portion of the context window?

An alternative would be to centralize everything in a large enterprise MCP server. But are we simply recreating, through a new interface, the same concentration and coupling problems that we have historically sought to solve with distributed architectures?

Perhaps we are facing a new category of problem. Architecture no longer affects only the organization of software components; it also begins to influence how agents discover, understand, and select their capabilities.

If we previously discussed how to distribute intelligence, now we need to discuss how to distribute knowledge about what that intelligence can do.

## The Problem of Tool Abundance

One of MCP's most interesting characteristics is its ability to allow different systems to expose their functionality to AI agents in a standardized way. Instead of relying exclusively on integrations developed specifically for each application, we can establish a common interface for tool discovery and execution.

This standardization opens up important integration possibilities, but it also creates a consequence worth considering: the more systems adopt the protocol, the larger the universe of capabilities potentially available to agents becomes.

In a small application, with a few servers and well-defined tools, this scenario is unlikely to represent a problem. However, when we bring this architecture into an organization with dozens or hundreds of products, the situation changes considerably.

Each server can expose multiple tools, accompanied by the descriptions, parameters, and schemas required for their use. When a client aggregates tools from multiple servers and presents these definitions to the model, the volume of information grows rapidly. Some of this information will be irrelevant to the current task, but it will continue occupying context space and expanding the set of alternatives the model needs to evaluate.

It is tempting to treat this problem solely as a context window limitation. After all, increasingly larger models can process growing amounts of information. But I believe this interpretation is insufficient.

Even when space is available, presenting hundreds of tools does not necessarily improve an agent's decision-making capabilities. An extensive catalog can increase ambiguity between similar operations, make it harder to select the appropriate tool, and introduce information that does not contribute to solving the task. The issue is not just the number of tokens consumed, but also the quality of the set of alternatives presented to the model.

There is, therefore, an important distinction between three dimensions that are often treated as if they were one and the same. The first is availability: what capabilities exist within the organization? The second is accessibility: which of these capabilities is a given agent authorized and technically enabled to use? The third is contextual relevance: which of them actually need to be presented during a specific execution?

These sets do not need to be identical. An organization may have thousands of capabilities, an agent may have authorized access to several hundred, and a particular task may require only a small subset of them.

This distinction is the starting point for rethinking MCP architecture. The challenge is not simply to make all tools accessible, but to manage which capabilities should be discovered, made available, and used in each context.

## The Centralization and Distribution Dilemma

The first analogy that comes to mind is a well-known discussion in software architecture: centralizing functionality in a monolithic application or distributing it across independent services.

We could imagine a large enterprise MCP server responsible for consolidating tools from different products and providing a single connection point for agents. This approach simplifies the integration experience, facilitates connection management, and can support centralized governance.

On the other hand, as the catalog grows, the server takes on increasingly greater responsibilities. Maintenance becomes more complex, evolution can introduce dependencies between domains, and the number of available tools continues to increase. Centralizing the connection does not necessarily solve cognitive overload. We can have a single access point and still expose a universe of capabilities that is difficult to manage.

At the opposite extreme, we could adopt independent MCP servers for each product or functional domain. Each team would be responsible for its own tools, contracts, and evolution cycles. This would provide greater autonomy, isolation, and flexibility in managing capabilities.

However, this distribution also comes with costs. The proliferation of servers requires mechanisms for discovery, connection management, authentication, observability, and governance. Furthermore, the agent or the infrastructure responsible for its execution would still need to decide which servers to use and which tools to expose.

It is important to recognize that the analogy with monoliths and microservices has its limitations. We are talking about different architectural domains. Service distribution primarily seeks to manage operational responsibilities, dependencies, and scalability. In the context of MCP, there is an additional dimension: how we organize servers influences how their capabilities are discovered and made available to the model.

A centralized server can expose tools selectively. Likewise, dozens of distributed servers can be managed through a centralized discovery and routing layer. The physical topology of servers does not need to determine the logical organization of capabilities.

This realization changes the nature of the discussion. We do not necessarily need to choose between centralizing or distributing everything. We can distribute execution, centralize certain governance responsibilities, and maintain shared discovery mechanisms. The important thing is to separate server organization from the way their capabilities reach agents.

## From a Server Catalog to a Capability Catalog

One possible answer would be to introduce an intermediary layer responsible for knowing which MCP servers are available and managing access to their capabilities.

Initially, we could think of an MCP Registry, functioning as an inventory of existing servers. It would make it possible to locate integrations, identify their owners, consult metadata, and access relevant information about each server.

But there is an important difference between knowing which servers an organization has and knowing what the organization can do through them.

A registry answers which servers exist, where they are available, and who is responsible for maintaining them. A capability catalog needs to go further. It must represent the tools exposed by those servers, their purposes, contracts, constraints, dependencies, and the conditions required for their use.

Imagine an organization with different systems responsible for customer information. Each one exposes tools related to customer data queries, financial positions, and transactions. A server inventory makes it possible to discover where these functionalities are hosted. A capability catalog makes it possible to understand which operation addresses a given need, which data source should be considered, and which conditions must be met before execution.

This distinction is fundamental. Discovering a tool should not depend exclusively on prior knowledge of the server that exposes it. Ideally, an agent should be able to start with a functional requirement and find the corresponding capability, regardless of its physical location.

In this scenario, an MCP Hub or Gateway could assume complementary responsibilities, such as managing connections, proxying calls, enforcing access policies, and centralizing operational aspects of communication. However, it is important not to confuse these responsibilities. Knowing that a tool exists does not necessarily mean knowing when to use it. Locating a server also does not mean that the agent needs to establish a permanent connection to it.

We are thus beginning to recognize the need to separate three architectural concerns: registering available capabilities, discovering those that make sense for a given request, and executing operations on the responsible servers.

This separation allows the infrastructure to evolve without requiring products to abandon their autonomy. Each domain can continue managing its MCP servers, while the organization maintains a shared view of its capabilities.

## Progressive Discovery and Contextual Selection

Once a global catalog has been established, a particularly interesting possibility emerges: instead of making all tools available from the outset, the agent could start with a limited set of discovery capabilities.

Upon receiving a request, it would query the catalog to identify potentially relevant tools. Only after this selection would the complete definitions, including parameters and schemas, be made available for use.

This approach, often called Progressive Tool Discovery, seeks to separate the global universe of tools from what actually needs to be present in the model's context.

The agent does not need to know all available capabilities in advance. It needs to be able to discover those that will be necessary.

We can imagine this process operating at two levels. At the first level, the catalog presents summarized information about capabilities, sufficient to identify and compare them. At the second level, after selecting the most suitable alternatives, the agent receives the complete contracts required to invoke them.

This separation reduces the amount of information initially presented to the model and allows context to be built progressively as the task evolves.

However, dynamic discovery is not simply a matter of searching for tools in a catalog. The search needs to be sufficiently precise to prevent similar but functionally unsuitable capabilities from being selected. A search that returns operations related to the subject but that do not actually address the need merely shifts the selection problem to an earlier stage.

For this reason, I believe discovery should combine different mechanisms. Structured information about domains, purposes, permissions, and constraints can narrow the universe of possibilities. Lexical and semantic search techniques can identify tools related to the stated intent. A ranking mechanism can then consider the functional suitability of the alternatives found.

It is also important to consider dependencies between capabilities. Some operations may require others to be executed beforehand, while certain functionalities may depend on tools exposed by different servers. Discovery needs to be able to represent these relationships, avoiding the treatment of each tool as a completely isolated unit.

There is, however, an interesting issue with this model: to discover something it does not yet know, the agent needs access to some discovery mechanism. This means that the ability to search for tools itself becomes a fundamental architectural capability. The catalog is no longer just a reference repository; it becomes part of the mechanism for building the agent's operational context.

## When Tool Descriptions Become Part of the Cognitive Architecture

In a small ecosystem, inconsistent descriptions can be corrected relatively quickly. However, when hundreds of tools are involved, metadata quality begins to have a direct impact on architectural reliability.

Imagine different products exposing tools named get_customer, retrieve_customer, find_client, and get_customer_details. All seem reasonable, but they may represent different operations, query distinct data sources, or address specific needs.

The model does not necessarily know these functional boundaries. It needs to infer them from the information provided by the server: name, description, parameters, input schema, and usage context.

A description such as "Retrieve customer information" is technically valid, but provides little information to guide the decision. What information will be returned? What is the authoritative source? In which situations should this tool be used? Are there any constraints? When would another tool be more appropriate?

A truly useful description needs to explain not only what the operation does, but also its purpose, scope, limitations, and the circumstances under which it should be selected.

This difference matters because, in a traditional architecture, a poorly documented API primarily harms the developers responsible for integrating it. In an agentic architecture, a poorly described tool can undermine the agent's own decision-making process.

The description is no longer just documentation. It becomes part of the cognitive interface between software and artificial intelligence.

For this reason, I believe an enterprise capability catalog would need to go beyond storing names, descriptions, and schemas. It should incorporate information about functional domains, purpose, preconditions, side effects, dependencies, permissions, data provenance, and potential overlaps with other tools.

There is also an important distinction between a tool's technical contract and its semantic contract. The schema defines how to invoke an operation. The semantic contract explains what it represents, under which conditions it should be used, and what guarantees it provides about the result.

Two tools may have very similar descriptions and still not be interchangeable. One may query an authoritative source, while another uses derived information or data updated at different intervals. The correct choice depends not only on the similarity between the intent and the description, but also on the authority of the source and the characteristics of the expected result.

In this context, AI models could help evaluate descriptions, identify ambiguities, suggest improvements, and enrich metadata. However, there is an important limitation: a model's inference cannot be confused with the official definition of a capability. Technical information, contracts, and business rules must continue to have verifiable sources and identifiable owners.

## The Capability Lifecycle

So far, we have assumed that a catalog exists that can represent the universe of capabilities within an organization. But how can we ensure that this catalog remains up to date?

In a company with different products and development teams, new features are created, tools are modified, contracts evolve, and APIs are decommissioned. A registry that relies exclusively on manual updates risks becoming yet another outdated inventory.

Dynamic discovery only works if the information used to find tools is reliable.

This suggests that we need to manage the capability lifecycle. A new MCP server should be identified and registered. New tools should trigger catalog updates. Contract changes should trigger revalidation and versioning. Decommissioned capabilities should no longer be presented as valid options.

Perhaps this process could be event-driven, using triggers from CI/CD pipelines, API management platforms, service registries, and the MCP servers themselves.

In this model, publishing a new version could automatically trigger a process for discovering, registering, and validating capabilities. Permission changes could update the associated policies. Breaking changes could require approval before publication.

The catalog would cease to be a manually maintained document and become a living inventory of enterprise capabilities.

However, automating registration does not mean eliminating accountability for what is being registered. Each capability needs a verifiable source, a reference version, and an identifiable owner. The infrastructure must be able to determine who maintains the tool, which contract is published, and which agents or applications can use it.

We also need to consider consistency between the catalog and execution. Imagine that a tool's contract changes while an agent is still using an earlier definition. Discovery may have been performed correctly, but execution will fail because the information used by the agent no longer matches the version exposed by the server.

Therefore, the lifecycle does not end with registration. We need to manage compatibility, versioning, and deprecation, ensuring that the definitions presented to agents correspond to the capabilities actually available.

Ultimately, we are introducing a new architectural concern: it is not enough to build a capability catalog. We need to build an infrastructure capable of continuously discovering, registering, validating, versioning, and maintaining that catalog.

## What If the Agent Didn't Need to Maintain All Connections?

There is another possibility that I find particularly interesting, including from a difficulty I encounter when using agents with multiple MCP servers in my day-to-day work.

In certain situations, I need to manually enable or disable connections to servers that are not part of the task's context. The reason is simple: keeping too many tools simultaneously available can interfere with selecting those that actually matter to the execution.

This experience suggests that controlling which tool definitions are loaded into the context may not be sufficient. We might also need a layer responsible for dynamically managing the connections to the servers themselves.

Imagine an intelligent router, an Intelligent MCP Router, that receives the agent's request, interprets its intent, and identifies which functional domains will be needed. Based on this analysis, it could query the catalog, locate relevant capabilities, and make their tools available through the corresponding servers.

If a new capability becomes necessary during the task, the router could perform another query, identify the responsible server, and incorporate the new tools into the available set.

Likewise, servers that are no longer relevant could have their tools removed from the set exposed to the agent. Depending on the connection strategy adopted, their sessions could also be terminated.

The infrastructure would begin dynamically managing the universe of possibilities presented to the model.

This approach, which we could call Context-Aware MCP Routing, adds an interesting dimension to the architecture. The router would not merely be an intermediary responsible for forwarding calls. It would participate in managing the agent's operational context.

However, there is an important technical distinction. Disconnecting an MCP server is not the same as simply ceasing to expose its tools to the model. We can maintain an active session while controlling which tools are made available. We can also keep the server connected without loading its definitions into the current context.

Each alternative has different costs. Establishing on-demand connections can introduce latency, while keeping sessions open can consume resources. Some servers also maintain state that cannot be arbitrarily discarded.

For this reason, I do not believe the solution necessarily lies in continuously connecting and disconnecting servers. A more efficient architecture will likely combine different strategies: keeping certain servers available, loading tools selectively, and activating new connections only when necessary.

It is also important to separate contextual selection from execution routing. A tool may be considered relevant without being authorized for a particular agent. Likewise, a capability may be available and authorized but still be irrelevant to the current task.

The router must respect these boundaries. Semantic selection does not replace authorization. Agent identity, user context, permissions, domain policies, and auditing must be considered before a tool is made available or executed.

This distinction is particularly important in enterprise environments, where certain operations may produce financial effects, modify information, or access protected data. The infrastructure cannot delegate to the model the decision about what it is authorized to do.

## A Multi-Plane Architecture

When we bring these ideas together, we begin to see that the problem has no single dimension. Server organization, capability registration, contextual discovery, and tool execution are related responsibilities, but they do not need to be concentrated in the same component.

One way to organize this architecture would be to separate it into three planes. The first would be the control plane, responsible for the global capability catalog, metadata, contracts, versioning, ownership, and governance policies. Its purpose would be to maintain a reliable representation of what the organization exposes through its MCP servers.

The second would be the discovery and selection plane, responsible for interpreting incoming requirements, querying the catalog, identifying relevant capabilities, and determining which tools should be made available in a given context. This is where progressive discovery and contextual selection would take shape.

The third would be the execution plane, responsible for connections to servers, authentication, authorization, tool invocation, result handling, and observability. Here, MCP servers would remain distributed and under the responsibility of their respective business domains.

This separation makes it possible to combine enterprise governance with product autonomy. The catalog can be shared while servers remain distributed. Discovery can use centralized mechanisms while execution remains the responsibility of the source systems. Routing can be coordinated by a common layer without requiring all tools to reside on a single server.

It is important to note that this division represents a logical separation of responsibilities, not necessarily three independent platforms or services. Depending on the organization's size, some of these functions may coexist within the same component. The goal is to prevent discovery, governance, and execution decisions from becoming coupled simply because they belong to the same MCP ecosystem.

This architecture also allows the selection mechanism to evolve independently of the servers. We can improve semantic search, change ranking criteria, incorporate new policies, or modify the connection strategy without requiring each product to restructure its integrations.

The catalog itself can evolve to represent not only individual tools, but also composite capabilities that depend on operations exposed by different servers. In this scenario, it begins to function as a map of enterprise capabilities, bringing the technical view of services closer to what the organization can actually accomplish.

## The New Challenge of MCP Architecture

The adoption of agentic architectures in enterprise environments expands the scope of integration decisions. It is not enough to define how systems expose their functionality; we also need to establish how that functionality will be described, located, selected, and made available according to each agent's needs.

MCP provides a standardized interface for connecting models to tools, but it does not, by itself, solve the problem of organizing this ecosystem. That responsibility belongs to the surrounding architecture, including mechanisms for cataloging, discovery, governance, and routing. This is the level at which it becomes possible to reconcile the distribution of capabilities across different domains with coherent management of their use.

Decisions about server granularity, contextual selection, and the separation of discovery, authorization, and execution will have direct consequences for the scalability and governance of agentic platforms. More than a protocol implementation issue, this is about defining how an organization intends to manage its capabilities in a scenario where agents are beginning to interact with an increasingly broad set of systems.

The architectural challenge is to transform this diversity of resources into an ecosystem that can be explored selectively, securely, and efficiently, without transferring to the agent the complexity of managing the entire infrastructure that supports it.
