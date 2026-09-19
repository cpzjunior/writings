# The Engineering of Organizational Communication

_How to control the flow of information, reduce knowledge asymmetries, and bring decisions closer to operational reality_

**Summary:** I argue that organizational communication is not about transmitting more information, but about designing better paths between reality, knowledge, and decision-making. As an organization grows, hierarchy, information overload, and concentration of knowledge create latency, noise, and dependencies that distance decisions from operations. Therefore, communication must be treated as an architecture: defining flows, filters, levels of abstraction, memory, and feedback that bring decisions closer to the necessary context without losing governance. Technology and AI can expand this architecture by preserving, contextualizing, and distributing knowledge, turning communication into an infrastructure for organizational learning.

---

Some time ago, I started thinking about how distance changes our perception of the environment we are in. When I lived on a lower floor, every noise from the street seemed to reach me. Cars passing by, people talking, doors opening and closing, movement on the sidewalk. The sound was constantly present and, at times, it was difficult to simply ignore it. There was too much information coming in, much of it completely irrelevant to me.

Today, living on the top floor, the experience is quite different. The silence is much greater. The distance from the street acts almost like a natural filter. Almost everything that used to catch my attention has disappeared. It is more comfortable, but there is also an interesting side effect: I have lost part of my awareness of what is happening around me. If a store closes, construction starts, there is some unusual activity on the street, or something changes in the neighborhood's routine, I will probably only notice when I go downstairs and take a walk.

This difference made me think about communication within organizations. The higher we move up the hierarchy, the greater the distance from operations tends to become. This distance is necessary. A director cannot follow every support ticket, every deployment, every vendor negotiation, or every operational incident. Their role requires abstraction, synthesis, and the ability to observe the organization at a different scale.

But there is a side effect similar to living on the top floor. Distance reduces noise, but it can also reduce signal. The more information is filtered before reaching leadership, the greater the possibility that important aspects of operational reality will fail to appear. The problem is not necessarily that someone is hiding information. Each layer of the organization naturally summarizes, selects, and interprets what it receives. When information passes through successive layers, it can arrive much cleaner than the reality that originated it.

On the other hand, simply bringing leadership closer to operations does not solve the problem either. If the director starts receiving all information directly, the result will simply be another form of communication overload. The goal should not be to eliminate the filter, but to build better filters.

Organizational communication, therefore, is not simply a matter of transmitting information. It is an engineering problem. It is necessary to determine which information should circulate, through which paths, with what level of detail, at what time, and to whom. It is necessary to reduce both silence and noise while preserving the ability to perceive what really matters. The problem, at its core, is finding the appropriate distance between those making decisions and that which those decisions concern.

## When too much communication is worse than silence

Communication is often treated as a monotonic variable. If there is too little communication, we should increase communication. If people are not informed, we create new channels, send more messages, schedule meetings, produce reports, and add dashboards. The implicit assumption is that more information necessarily produces better decisions.

It does not. Humans have an extraordinary capacity to filter stimuli. This is necessary for us to function. In a city, we do not consciously pay attention to every car that passes, every conversation on the sidewalk, every door that closes, or every noise produced around us. Our brain quickly learns to classify many of these stimuli as irrelevant and turns them into a kind of background noise. We can think of this as gray noise: information that exists, that reaches us, but that progressively stops receiving our attention.

The same mechanism appears in organizations. A professional who receives dozens of messages every day begins to develop heuristics to decide what deserves attention. Certain senders become priorities. Certain subjects are automatically associated with low relevance. Recurring meetings stop being analyzed individually. Dashboards are consulted only when some number looks exceptional. Extensive documentation is used only when there is a concrete problem.

This is a rational adaptation to an environment of excess. The problem is that the filter does not necessarily know the true importance of the information. It learns patterns.

When everything seems urgent, nothing is urgent. When all channels are important, no channel is truly important. When every message needs to be read, the human solution tends to be not to read some of them.

This is where too much communication can become worse than silence. Silence is noticeable. When we do not receive information, we know there is a gap and can deliberately look for what is missing. Excess is more dangerous because it creates the feeling that we are informed. There is a huge amount of information available, but the ability to distinguish signal from noise has been degraded. An organization can therefore be extremely well communicated from a quantitative standpoint and extremely poorly communicated from an operational standpoint.

There is a point at which increasing the volume of information begins to reduce the ability to absorb the information itself. The individual starts receiving more stimuli than they can process and needs to establish mechanisms for simplification. Messages are ignored, meetings stop receiving attention, documents stop being read, and indicators are observed only superficially. The organization continues producing information, but the human capacity to transform it into knowledge does not grow at the same rate.

This is one of the most important paradoxes of organizational communication. Insufficient communication produces information asymmetry. Excessive communication produces noise. In both cases, the consequence can be the same: decisions made with an incomplete representation of reality.

Therefore, perhaps the problem of organizational communication is better described as an optimization problem. We do not want to maximize the amount of information transmitted. We want to maximize the amount of relevant information that reaches the right person, at the right time, in a form that can be understood and used. The question is not how much the organization communicates. It is how much of what it communicates remains perceived when it really matters.

## Information is not knowledge

An organization can possess an enormous amount of information and still have little ability to understand what is actually happening. Having records does not mean having knowledge. Having knowledge, in turn, does not necessarily mean having a shared view of reality.

This distinction is important because organizations do not merely need to store information. They need to establish a common basis for facts. Before discussing interpretations, responsibilities, or decisions, it is necessary to know what actually happened, what evidence exists, and which conclusions are still only hypotheses.

Documentation may exist without being used. A dashboard may contain all the necessary indicators without anyone knowing which ones actually matter. A channel may contain thousands of messages and still fail to allow someone who has just joined the team to understand how a particular system works. Likewise, different areas may have correct information about the same event and still arrive at completely different interpretations because each sees only part of the context.

Knowing that a particular service experienced an outage at 2 p.m. is information. Knowing that the outage occurred because of a particular dependency, that there were earlier signals that could have anticipated the problem, and that there is a known procedure for handling the situation is knowledge. Knowing, in addition, that the incident is actually related to that cause, rather than merely repeating the most convenient hypothesis, is a matter of evidence.

This last distinction is particularly important. An organization needs to be able to separate fact, interpretation, and hypothesis. “The service became unavailable” is an observation. “The outage was caused by component X” is an interpretation that requires evidence. “If we change X, the problem will not occur again” is already a hypothesis about the future.

When these levels become mixed, communication begins to propagate not only information, but also unverified interpretations. Over time, these interpretations can acquire the appearance of truth simply because they have been repeated many times. A hypothesis recorded as a hypothesis can be investigated. A hypothesis recorded as a fact tends to be reproduced.

Therefore, a mature organization needs to develop something close to a science of facts. Not in the sense of turning every decision into an academic or bureaucratic process, but of preserving the ability to distinguish what was observed from what was inferred, and what is known from what still needs to be validated. Logs, metrics, evidence, incident records, technical documentation, and decision history are important precisely because they make it possible to reconstruct reality when different people have different perceptions of it. Knowledge requires context, but context also needs to be anchored in evidence.

It is precisely this contextual knowledge that tends to become concentrated in individuals. The professional who participated in a decision remembers why a particular choice was made. Whoever followed an incident knows which hypotheses were discarded. Whoever spoke with a particular customer knows nuances that do not appear in the system. Whoever was present during an architecture implementation knows which constraints existed at that time. This knowledge is valuable, but when it remains exclusively in the memory of those who were present, it does not effectively belong to the organization. It belongs to the individual.

An organization begins transforming individual experience into organizational capability when it can record not only what was decided, but also the facts and evidence that led to the decision, the context in which it occurred, the alternatives considered, and what was learned afterward.

Communication, in this sense, should not merely transport information between people. It should enable the organization to build, question, and preserve a shared representation of reality.

## The organization as a communication network

Hierarchy and communication are different things. Hierarchy determines authority, responsibility, and accountability. It does not need to determine all the paths through which information can circulate. An organization can maintain a perfectly defined hierarchical structure while, at the same time, allowing information to cross its boundaries much more flexibly.

In a healthy organization, vertical communication is necessary for coordination and governance, but horizontal communication is equally important for execution. Teams need to talk to one another. Specialists need access to specialists. Operations needs to be able to transmit problems to development. Development needs to understand the operational consequences of its decisions. And leadership needs to be able to access operational reality without depending exclusively on a chain of summaries.

This distinction is important because each hierarchical layer also functions as a mechanism for compressing information. Leadership does not need to know every detail of an operation, but it does need to receive the right details to make its decisions. Likewise, an operational team does not need to know every strategic decision in the organization, but it needs to understand those that change its responsibilities and execution context.

Compression, therefore, is not necessarily a problem. It is a condition for an organization to function at scale. The problem arises when the information removed during this process was precisely what was needed to understand the context or make a decision.

The problem also arises when hierarchy stops organizing authority and starts excessively controlling the flow of information. In this scenario, information needs to pass through several levels before reaching someone who can act on it. Each passage adds latency, interpretation, and the possibility of losing context.

The hierarchical structure can remain intact while the communication topology is much more flexible. This distinction becomes especially important during crises. Under normal circumstances, there are defined processes, responsibilities, and channels. In a critical situation, however, the latency introduced by a communication chain may be more harmful than temporarily breaking that chain.

A director does not need to speak directly with every professional in the organization every day. But, in the face of a significant crisis, it may be necessary to speak directly with the people working on the problem. Not to replace those managing the operation, but to reduce the distance between information and decision.

The question, therefore, is not to eliminate hierarchy or turn all communication into direct communication. It is to allow information to find the appropriate path within the existing structure. The right question should not necessarily be “who should talk to whom?”, but “what is the shortest path between the information needed and the person capable of making the decision?”.

## The director does not need to stay on the top floor forever

The apartment metaphor returns here. The top floor is comfortable. It provides silence, perspective, and distance. But no one should confuse silence with the absence of problems. Distance reduces noise, but it also reduces awareness of what is happening in the surrounding environment.

A director does not need to be permanently immersed in operations. That would be micromanagement and would prevent them from properly fulfilling their own responsibilities. But they also should not depend exclusively on information filtered through successive hierarchical layers. Just as living on the top floor does not mean never leaving the building, holding an executive position should not mean losing contact with operations.

From time to time, it is important to go downstairs. Talk to operations. Listen to support. Identify which problems are recurring. Ask why a particular activity is still manual. Find out which systems are generating more work than they should. Understand which customers are repeatedly escalating problems. Observe which processes seem to work only because certain people possess tacit knowledge that is not documented.

These conversations can reveal information that would rarely appear in an executive report. A process may formally be within expected indicators and still consume a disproportionate amount of human effort. A system may be available and, at the same time, extremely difficult to operate. A complaint may appear isolated on a dashboard and be immediately recognized by someone who works with that customer every day. This does not mean auditing people. It means observing the system.

Operations and support are, in this sense, sensors of the organization. They are often the first places where signs appear that an architectural decision did not produce the expected result, that a process has an unforeseen exception, that a particular automation is not working as it should, or that a customer is experiencing a problem that has not yet appeared in executive indicators.

This direct observation also helps calibrate the communication mechanisms themselves. The director may discover that a particular report is providing information that nobody uses, while important information is circulating informally among a few people. They may notice that there are too many meetings to solve problems that could be resolved with proper documentation, or that a particular decision is taking too long because it has to travel through a longer hierarchical chain than necessary.

A director should have the ability to drill down. They can start with an aggregated indicator, identify an anomaly, enter an area, observe a process, reach an incident, and eventually speak with the professional who has the necessary context. Then, they should be able to return to the executive level and turn that local observation into a decision or systemic change.

This movement is important. The function of leadership is not to remain in operations, but to alternate between different levels of abstraction without losing the ability to move between them when necessary. The executive perspective makes it possible to see patterns that are not visible locally. Contact with operations makes it possible to verify whether those patterns correspond to reality.

In architectural terms, it is a form of observability. A director does not need to know the state of every component in the organization, just as a distributed system does not need to expose all of its internal states to those operating it. But they need to be able to drill down when an aggregated signal indicates that something deserves investigation. Hierarchical distance should not mean informational distance.

## The indispensable professional as a single point of failure

It is common to find organizations in which a particular professional has become the person who “knows everything” about a system, process, or integration. At first glance, this seems to represent an extremely valuable professional. Upon closer examination, it may represent a failure of organizational architecture.

When only one person knows how to perform a particular activity, interpret a particular system behavior, or resolve a particular incident, that person becomes a single point of failure. The organization has created a dependency whose availability is tied to the availability of an individual.

This usually happens gradually. The professional solves one problem, then another. They become a reference for a particular system. They participate in important decisions. They accumulate context. Because they know the history, they are consulted again. Over time, what began as specialization turns into concentration of knowledge.

There is also a feedback mechanism. The more a person is consulted, the more knowledge they accumulate. The more knowledge they accumulate, the more the organization depends on them. And the more it depends on them, the more opportunities there are for them to continue being consulted. What began as a natural consequence of experience can end up becoming an architecture of dependency.

The problem is not only organizational. It also harms the professional themselves. The more knowledge is concentrated in them, the harder their absence becomes. Vacations begin to require special planning. Absences become a risk. Incidents continue reaching them. Delegating responsibilities becomes difficult. And, paradoxically, what initially appeared to be a demonstration of indispensability can limit their ability to take on new responsibilities. The organization becomes dependent on the person, and the person becomes tied to the organization by the very dependency they created.

A mature organization should produce the opposite effect. The more a person masters critical knowledge, the greater the incentive should be for that knowledge to be shared, documented, and transformed into organizational knowledge. This does not mean eliminating specialization. Organizations need specialists. The goal is to prevent specialization from becoming a monopoly on knowledge.

The specialist should remain the primary reference, but should not be the only person capable of operating, explaining, or recovering a particular component of the organization. Ideally, their experience should increase the team's capability, not merely the team's dependence on them. The goal is not to make the professional less important. It is to make their knowledge create value beyond their physical presence.

## Organizations are also distributed systems

There is a particularly interesting connection between organizational communication and distributed systems architecture. Distributed systems must deal with a reality in which no component necessarily has a complete view of the system's state. Information is spread across different components, communication involves latency, states can diverge, and decisions often need to be made locally. A component needs to act based on the knowledge it possesses, even knowing that relevant information exists elsewhere in the system.

Organizations exhibit similar properties. As a company grows, it becomes impossible for a single person to possess all the context necessary to make every decision. Knowledge becomes distributed among areas, teams, and individuals. An operations professional knows certain aspects of the system that a director does not. A developer knows certain technical limitations that do not appear in an executive report. A support professional has a perception of certain customers that rarely appears in an aggregated indicator. A professional who participated in a decision years ago may know of a constraint that disappeared from the documents but remains relevant to understanding why a particular architecture exists. This distribution of knowledge is not a problem that can be eliminated. It is a natural consequence of scale and specialization.

In this sense, decentralization of decisions can be understood not only as a cultural choice, but as an architectural response to the problem of distributed information. When the knowledge required for a decision is located in a particular part of the organization, it makes sense for part of the authority needed to act to also be close to that knowledge.

The larger the organization, the greater the amount of localized knowledge tends to be. If every decision has to return to the center to be made, the organization introduces latency precisely where it should have speed. A team that needs to wait for successive approvals to solve a problem it has enough knowledge to solve locally turns an information asymmetry into a decision queue.

The solution is to bring certain decisions closer to the source of knowledge. This does not mean that every decision should be decentralized. There are decisions that need to remain centralized because they involve systemic risks, capital allocation, strategy, compliance, or consequences that exceed the capacity of a local unit. The point is to recognize that centralization and decentralization are not binary properties of an organization. Different decisions can have different levels of autonomy.

The challenge becomes determining which decisions need global context and which need only local context. Distributed authority should not mean arbitrary authority. Each unit's autonomy needs to be proportional to the context it possesses, the risks it can assume, and the contracts it maintains with the other parts of the organization.

This is quite similar to defining boundaries in distributed systems. Not everything needs to be shared globally. Sharing everything can be expensive and unnecessary. What matters is establishing which information needs to cross the boundaries between components and which can remain local. Each unit can have its own operational context, provided there are sufficiently clear interfaces for the other units to know how to interact with it.

But distribution does not mean an absence of governance. Distributed systems do not work simply because each component does whatever it wants. They depend on protocols, contracts, observability, coordination mechanisms, failure handling, and well-defined interfaces. Organizations need them as well.

Policies establish boundaries. Architectural standards establish conventions. Processes establish forms of coordination. Ownership defines responsibilities. Documentation preserves knowledge. Metrics provide observability. Escalation mechanisms allow problems to cross local boundaries when necessary.

These mechanisms allow an organization to have local autonomy without losing global coherence. A distributed organization without communication and coordination mechanisms can experience problems similar to those of a poorly designed distributed system: divergent states, inconsistent decisions, hidden dependencies, fragmented knowledge, and difficulty diagnosing failures.

Likewise, an excessively centralized organization can face the opposite problem. There is a central component that theoretically has the authority to decide everything, but does not have the cognitive capacity or sufficient information to follow all the details. The result is a human architectural bottleneck: decisions accumulate at a point that has authority, but does not necessarily have the context needed to make them quickly and effectively.

Communication is the mechanism that connects these two realities. It allows the organization to preserve local autonomy without losing the ability to coordinate the system as a whole. Perhaps this is one of the main reasons why communication stops being merely an interpersonal skill as an organization grows. It becomes part of the system's architecture itself.

## When hierarchy becomes latency

A recent example from Xbox helps illustrate how organizational structure can become a communication problem. In July 2026, Asha Sharma, CEO of Xbox, announced a major restructuring of the division. When explaining the changes, she stated that, in some parts of the company, work passed through as many as 14 layers of management. According to Sharma, this complexity was making decisions slower, reducing clarity around accountability, and making delivery for players more difficult. The announced proposal was to reduce management layers to no more than five and, where possible, three.

The number 14 is striking, but the most important aspect is not the number itself. It is what happens to information when it has to cross so many organizational boundaries. An idea that originates close to the product, a problem identified by an operational team, or a technical decision made by someone with deep knowledge of a particular system should not necessarily have to pass through a long hierarchical chain to produce an effect. Each additional layer can serve a legitimate coordination function, but it also introduces another opportunity for loss of context, interpretation, delay, and shifting priorities.

Imagine information passing through fourteen layers. The first person knows the original problem. The second receives a summarized explanation. The third receives an interpretation of that explanation. The fourth receives an even more condensed version. After successive transformations, what reaches the top may remain formally correct but no longer accurately represent the situation that existed at the source.

The same happens in the opposite direction. A decision made at the top needs to be translated by different levels before reaching the person who will actually perform the work. Each translation can add context, but it can also introduce ambiguities. The result is an organization in which information travels a much greater distance than the decision actually requires.

It is possible to think of this as organizational latency. In distributed systems, an operation that depends on many calls between components can be constrained by the time required for information to traverse the system. In an organization, a decision that depends on many hierarchical levels can suffer from a similar limitation. The problem is not simply that there are many managers. The problem appears when the communication architecture requires many of them to participate in transmitting, interpreting, or validating information that could reach its destination directly.

The solution proposed by Sharma itself follows this logic. Xbox intends to adopt a flatter structure based on makers, player-coaches, and people directly responsible for decisions and outcomes. The stated intention is to reduce complexity, bring responsibility and decision-making closer together, and simplify how work is performed.

This does not mean that an organization should eliminate hierarchy. It means that hierarchy should not be confused with a mandatory chain for every decision. A hierarchical structure can continue to define who is responsible for an area, who controls the budget, who assumes a particular risk, and who is accountable for the result. But this does not mean that all information needs to pass through all those levels, nor that every decision needs to be approved by every existing layer.

This is one of the points where organizational architecture once again approaches distributed systems architecture. A system is not more robust simply because it has more intermediary components. Likewise, an organization does not necessarily become more controlled because it has more management levels. Intermediate components exist to solve specific problems. When they exist merely because the structure has grown over time, they can become latency.

The Xbox case is interesting precisely because its leadership identified a relationship between structural complexity and decision speed. The question ceases to be “how many hierarchical levels should a company have?” and becomes “how many levels are actually necessary for information to circulate and decisions to be made with quality?”. That is an architectural question.

An efficient organization should not force information to traverse the entire hierarchy simply because the hierarchy exists. It should allow information to follow the path necessary to reach those who can understand, validate, or act on it. When hierarchy stops organizing responsibilities and begins functioning as a mandatory sequence of filters, it ceases to be merely a governance structure and becomes part of the communication problem.

## Communication as a feedback system

Organizational communication should not be understood merely as a one-way flow of information. It is also a feedback system. A decision is made, produces an effect, that effect is observed, the information returns to those who need to evaluate it, and based on it, a new decision can be made. This cycle allows an organization not only to execute plans, but also to learn from what happens after the plans are executed.

We can represent this cycle simply: reality, observation, communication, decision, execution, new reality, and new observation. The cycle does not end when a decision is executed. It is precisely from its effects that the next iteration begins.

The value of communication also lies in its ability to close this cycle. If a decision is made at the top of the organization, but its effects cannot reliably return to those who made the decision, the organization loses its ability to learn. Likewise, if operational signals arrive too late, the organization may continue correcting symptoms when the cause has already changed.

This is why communication needs to be designed not only to transmit decisions, but also to bring back the effects of those decisions. Information that circulates but cannot alter decisions is merely traffic. Feedback requires a path between observing an effect and having the ability to modify the system's behavior.

This mechanism appears continuously in operations. An architectural change is implemented, systems begin behaving in a certain way, operations identifies new patterns, support notices effects on customers, and these signals need to return to development and leadership. If this flow works, the organization can adjust its systems and processes. If it does not, each area begins operating with a partial view of reality.

The engineering of communication, therefore, is also an engineering of feedback. The lower the latency between an event and the return of information about its effects, the faster the organization can correct its trajectory. The greater the latency, the greater the chance that decisions will continue to be made based on a reality that no longer exists.

This also explains why operations and support are so important. They are not merely process executors. They are observation points in the system. When their signals are treated as noise or become trapped in certain hierarchical layers, the organization loses part of its ability to perceive how it itself operates.

Feedback also feeds back into the engineering of communication itself. If certain information never produces a decision, perhaps it does not need to continue being distributed in the same way. If a decision frequently produces problems that only appear months later, perhaps there is a deficiency in the observation mechanism. If certain incidents continue occurring because knowledge does not reach the right teams, perhaps the problem lies less in execution and more in communication architecture.

Thus, the organization can learn not only about its products, systems, and customers, but also about the way it communicates. This is where communication stops being merely a channel and becomes an adaptive system. The organization observes the effects of its decisions, identifies failures in its own information flows, and modifies those flows to improve future decisions.

When this learning is preserved, it stops depending solely on people's memories and becomes part of the organization's memory.

## Organizational memory

If knowledge needs to be distributed, the organization needs somewhere where that knowledge can exist independently of the people who possess it. It is necessary to create a memory external to individuals' minds.

This is where documentation, wikis, and knowledge bases stop being administrative tools and become organizational infrastructure. An organization that depends exclusively on the memory of its professionals is constantly subject to the loss of context. People change teams, go on vacation, leave the company, forget details, or simply cease to be available when that knowledge is needed. The problem of the indispensable professional begins precisely when what should belong to the organization exists only in one person's memory.

A well-structured Wiki makes it possible to transform tacit knowledge into accessible knowledge. A Wiki as Code adds something even more important: versioning, review, automation, and integration with the development lifecycle. Documentation stops being a collection of static pages and begins to have properties similar to those of the software it describes.

Documentation can be treated as software. Changes can generate reviews. Changes in code can signal potentially outdated documentation. Incidents can produce new articles. Architectural changes can automatically generate tasks to update the knowledge base. Important decisions can preserve not only the final result, but also the context, facts, and evidence that led to that decision.

But organizational memory does not merely need to store knowledge. It needs to preserve the ability to evaluate that knowledge. Stored information without provenance loses part of its value. It is important to know where it came from, when it was produced, what evidence supports it, who recorded it, and in what context it was valid. An architectural decision documented five years ago may still be relevant, but it may also have been superseded by another decision. A procedure may have been correct when it was created and be completely inappropriate after an architectural change. A statement may represent a team's observation, while another may represent a formal organizational policy.

Organizational memory should therefore preserve not only content, but also its provenance, validity, and authority. Provenance answers the question “where did this information come from?”. Validity answers “is it still true or applicable?”. Authority answers “who has the legitimacy to establish or change this knowledge?”. These properties are different. A log may have high authority as a record of what happened in a particular system, but no authority to define how the system should work. Architectural documentation may have authority to establish a standard, but not necessarily to state that a particular incident was caused by a specific failure. A professional's account may contain extremely valuable context without, by itself, representing a conclusion validated by the organization.

This distinction is particularly important when different sources present conflicting information. The organization should not simply choose the most recent, most repeated, or best-written information. It should be able to identify which source has authority over a particular subject, what evidence supports each assertion, and whether the knowledge remains valid in the current context.

Artificial intelligence can act as an additional layer in this process. A change in a repository can trigger a process that identifies what changed, searches for related documents, consolidates information, and proposes updates. This information can then be structured into a knowledge base prepared to be consumed by internal tools or agents.

In this scenario, an MCP server can function as an interface between this organizational memory and systems capable of using it. An agent could, for example, query architectural standards, operational procedures, previous decisions, or documentation for a particular service without depending on someone who personally knows that information. More importantly, it could receive the context along with the information: the source, date, validity status, and, when applicable, the authority that established that knowledge.

This changes the nature of the query. Instead of simply asking “how does this system work?”, a professional or agent could obtain something closer to “how does this system currently work, which document establishes this behavior, when was it updated, and which previous decisions explain its architecture?”. Memory stops being merely a repository of answers and begins providing elements for evaluating the answers themselves.

There is also a particularly interesting application for communication: the ability to contextualize and translate knowledge between different domains of the organization. The same information may need to be presented in completely different ways depending on who receives it. A change in a messaging mechanism can be described to an architect in terms of contracts, delivery guarantees, and coupling. For operations, it may be more relevant to explain its impacts on observability, recovery procedures, and operational capacity. For a business area, the same change may need to be translated into terms of availability, customer impact, risk, and timeline. For leadership, perhaps only the effect on risk, cost, capacity, or outcome needs to be presented. The fundamental content is the same, but the context needed to understand it is not.

This ability to translate is particularly important in large organizations because different areas develop their own vocabularies. Technical terms have specific meanings for engineering. Operations uses different concepts to describe the same events. Finance, risk, legal, product, and business have their own mental models and relevance criteria. The existence of information in one domain does not mean that it is immediately understandable in another.

AI can function as a semantic layer between these domains. Instead of merely summarizing information, it can reinterpret it within the recipient's context, explaining its impacts, relating it to the concepts that area uses, and preserving the link to the original information. The goal is not to alter the fact to make it more convenient, but to alter the form of representation to reduce the cognitive distance between the information and those who need to use it.

This requires an important distinction between translation and transformation. Translation should preserve the essential meaning of the information, while transformation can produce a different interpretation. An AI that presents a technical incident to an executive should not invent an executive conclusion; it should translate the relevant technical facts into that executive's decision-making model while maintaining access to the original evidence and context.

Organizational memory can thus operate at different levels of abstraction. The original information remains available, but different consumers can access representations appropriate to their context. The same event can have a technical, operational, financial, and executive representation, all linked to the same source.

This makes it possible to address both problems presented at the beginning of this article simultaneously: lack of information and information overload. The goal is not to turn the entire organization into consumers of an ever-growing knowledge base, but to make it possible for each person to access relevant knowledge, at the appropriate level of abstraction, when they need it.

The important point is not simply to put an AI in place to “read the Wiki”. It is to transform organizational knowledge into living, versioned, reviewable, contextualized infrastructure that can be consumed by humans and machines.

The flow could be described quite simply: humans produce knowledge, systems record its provenance, version and relate that knowledge, governance mechanisms establish its validity and authority, AI helps organize and contextualize the information, humans validate what is critical, and agents and professionals consume the knowledge in the form appropriate to their context.

Communication thus ceases to be exclusively a process between people. It also comes to include the mechanisms through which an organization records, preserves, validates, contextualizes, translates, updates, filters, and redistributes what it has learned.

## Onboarding as a mechanism for knowledge distribution

If the organization already has structured knowledge, onboarding is one of the first opportunities to distribute it. A professional hired for their technical competence does not need to go through a disguised examination to prove again that they know how to program. The objective of technical onboarding should be different: to enable them to quickly develop a mental model of how that organization builds systems.

An interesting approach is to start from existing knowledge. Imagine a production payments architecture. Business rules, external integrations, and accidental complexities can be simplified or removed while preserving the relevant architectural aspects. The new employee then receives an artificial problem based on that architecture and needs to implement a solution using the patterns adopted by the company.

The exercise does not measure whether they know how to develop. The hiring process has already answered that question. The exercise teaches them how that organization develops. It allows the professional to discover, in practice, how the company structures services, handles dependencies, implements observability, uses messaging, organizes configurations, handles errors, defines contracts, and establishes integration patterns. Instead of merely hearing about the company's standards, the professional needs to use them to solve a problem.

This is more efficient than a sequence of presentations about “how we do things here” because it turns organizational knowledge into practical experience. The person does not merely need to memorize an architecture or a set of patterns. They need to build something within the constraints that represent how the organization works.

There is also an additional benefit. If the onboarding exercise is derived from the production architecture, it can evolve along with it. When architectural standards change, the onboarding material can change as well. When a new approach begins to be adopted in production, it can eventually appear in the next exercise.

The company's architecture itself becomes a source of educational material. This creates an interesting cycle: production systems generate knowledge, that knowledge is documented and structured, the documentation generates onboarding exercises, and new professionals learn the patterns through practice. As the architecture evolves, the knowledge and exercises can evolve with it.

Onboarding then stops being merely a process for integrating people. It becomes a mechanism for propagating organizational architecture. More importantly, there is a direct connection between what the organization has learned and what future professionals will learn. Organizational memory stops being merely an archive of the past and begins functioning as a mechanism for transmitting knowledge into the future.

## The goal is not to communicate more, but to communicate better

There is a permanent temptation to solve communication problems by creating more communication: more meetings, more channels, more reports, more dashboards, more emails, more notifications. But an organization does not necessarily need more information. It needs better paths for relevant information to reach those who need it.

The goal of organizational communication is not to maximize the volume of information transmitted, but to reduce the distance between reality, knowledge, and decision-making. This means knowing when to communicate, whom to communicate with, at what level of detail, and through which channel.

Artificial intelligence can help in this process as a layer of contextual filtering. Instead of distributing all information to everyone, agents can analyze changes, incidents, and events and present each stakeholder with what is relevant to their context, while preserving access to the original information when necessary. AI, in this case, does not replace communication. It helps reduce noise and bring information closer to those who are able to use it.

An efficient organization is not one in which everyone knows everything. It is one in which each person receives the context necessary to make good decisions, in which important information can cross organizational boundaries, in which decisions can be made close to reality, and in which critical knowledge does not depend on a single person. The goal, therefore, is not to communicate more. It is to communicate better.

The engineering of organizational communication begins with the architecture that determines how information circulates, is filtered, contextualized, transformed into knowledge, and used to make decisions. And, when the effects of those decisions return to the organization, the communication system itself can be adjusted. This is how communication stops being merely the transmission of information and begins to function as infrastructure for organizational learning.
