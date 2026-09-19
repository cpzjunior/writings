# PMBOK is not a cookie-cutter recipe: the role of tailoring in project management

_Just as software architecture is a response to requirements and constraints, management also needs to be designed for the context._

**Summary:** I argue that PMBOK should not be treated as a cookie-cutter recipe, but as a body of practices that needs to be adapted to the context of each project. Just as in software architecture, we should first understand requirements, constraints, risks, and trade-offs before defining the appropriate management solution. Tailoring does not simply mean doing less, but consciously sizing the governance required, avoiding both bureaucracy and insufficient controls. Maturity, therefore, lies less in following processes and more in knowing how to justify choices and evolve them as the problem changes.

---

Recently, in a conversation with a friend who works as a Product Manager, a comment came up almost by chance that caught my attention. She told me that the company where she works does not use PMBOK because it considers the approach too rigid for the organization’s reality.

The perception does not seem strange to me. In technology, I see something similar happening frequently in discussions about solution architecture. A particular architecture is presented as a best practice, starts being reproduced in other contexts, and, when it does not fit, the conclusion is that the architecture itself was inadequate. Often, the problem lies in choosing the solution before understanding the problem it needs to solve. In system design, we know that it makes no sense to start with the architecture. First, we understand the problem, its requirements, constraints, and trade-offs. Only then do we decide how the system will be built.

When I heard that comment about PMBOK, I made the same association. Perhaps part of the resistance to the framework comes from treating it as a ready-made management architecture, something that should be applied uniformly so that an organization can say that it “does project management.” If that is the starting point, it is easy to turn knowledge into procedure, procedure into obligation, and obligation into bureaucracy.

The problem lies precisely in this interpretation. PMBOK does not need to be understood as a ready-made methodology, just as a set of architectural patterns does not, by itself, constitute an application’s architecture. It offers knowledge, practices, and concepts that can be used to build management approaches suited to different situations. The question ceases to be how much of PMBOK an organization uses and becomes why certain practices were chosen, what problem they solve, and what level of formality is necessary.

It may be useful to think of this as a kind of management design. Not as a formal discipline or a new framework, but as a lens for looking at management with the same logic we use when designing systems: understand the problem before choosing the components, make constraints explicit, evaluate trade-offs, and avoid both unnecessary complexity and insufficient solutions.

## The problem starts before the methodology

When we talk about project management, we often put things that serve different roles on the same level: the body of knowledge about management, the approach chosen to conduct a project, and the methodology used by the organization to operationalize that approach. Confusing these layers makes it easier to assume that, in order to apply certain knowledge, it is necessary to reproduce an entire process. But an organization can use management practices without adopting a formal methodology, just as it can have a corporate methodology and still adapt its application to each project.

This difference becomes evident when we look at the scale and nature of the work. A small team can manage risks, priorities, dependencies, and decisions through informal mechanisms because proximity between people makes coordination inexpensive. As the organization grows, interfaces, stakeholders, the cost of misalignment, and the consequences of certain decisions increase. Governance, communication, and traceability needs then emerge that simply did not exist before. It is not that the organization has become more “adherent” to a methodology; the system it needs to coordinate has become more complex.

The same logic applies to the way execution takes place. A project with relatively stable requirements and a high cost of change may justify a more predictive approach. A product operating in a highly uncertain environment may benefit from short cycles of learning and adaptation. Between these extremes there is a variety of possible combinations, including within the same initiative, when different parts of the work have different levels of predictability.

Therefore, the question of which methodology to use should not be the starting point. Before that comes a more fundamental question: what do we need to manage, what risks are involved, what constraints exist, and how much coordination and governance does this context really require? It is from these answers that a management approach can be designed.

## Management design

In system design, we do not start by saying that every application needs microservices or messaging. We start by understanding requirements and constraints. Volume, availability, latency, security, cost, operational capacity, and criticality help determine which architectural decisions are justified. There is no architecture that is correct in the abstract. There is an architecture that is appropriate for a given set of requirements and constraints, considering the trade-offs involved.

The same logic can be applied to management. A critical project may require governance mechanisms that would be disproportionate for a small initiative. A project with many dependencies may need coordination mechanisms that make no sense for a team working independently. A highly uncertain initiative may derive little value from excessively detailed planning when there is not yet enough information to support it. What changes from one context to another is not the importance of management, but the problems it needs to solve and the complexity required to solve them.

Management practices can therefore be treated as components of a solution. PMBOK provides part of this repertoire, but does not determine on its own how these components should be combined. The final composition depends on the project’s context, needs, and constraints. It is in this sense that I propose thinking about management design: the deliberate construction of a management approach based on the problem that needs to be managed.

The idea is similar to assembling a system. Having more components available does not automatically make the solution better. Each component adds capabilities, but it can also introduce cost, complexity, dependencies, or new operational needs. The work of design lies precisely in deciding what needs to be part of the solution, what can be simplified, and which trade-offs are acceptable.

Tailoring, in this sense, stops being merely the act of “adapting PMBOK.” It becomes a natural consequence of the design process itself: understanding the context, selecting the appropriate components, and composing an approach proportional to the problem that needs to be solved.

## Tailoring is not about doing less

It is easy to interpret tailoring as a license to reduce processes. If an organization has too many documents, it eliminates some; if it has too many meetings, it cancels some; if a particular step seems bureaucratic, it stops performing it. The result may even be a better approach, but reducing processes by itself does not constitute tailoring. The difference lies in the criterion used to make that decision.

In architecture, a solution is not better simply because it has fewer components. An application with few components can be elegant or insufficient; a more complex architecture may be necessary or may represent overengineering. The number of components matters less than their relationship to the requirements they need to satisfy. The same logic applies to management: the number of practices used does not determine the quality of the approach.

Applying fewer practices can indeed be more mature than applying all of them indiscriminately, as long as the choice is deliberate. If a particular control was eliminated, it is necessary to understand what problem it solved, what risk is associated with its absence, and why that level of control is not necessary in that context. Likewise, adding a practice should require an equivalent justification: what need does it address, and what complexity does it introduce?

Tailoring is not choosing the simplest path. It is sizing management according to the problem, consciously accepting the trade-offs involved.

## The risk of management overengineering

In technology, overengineering is a well-known problem. A solution can be technically correct and still be inappropriate because it introduces complexity that the requirements do not justify. More components can mean more capacity, but also more dependencies, more operational effort, and more failure points. Complexity needs to exist for a reason.

In management, the equivalent happens when an initiative receives documents, approvals, meetings, and metrics because these mechanisms are part of the corporate methodology, rather than because the project actually needs them. Each element may seem reasonable in isolation. The problem appears when we observe the approach as a system and realize that its complexity introduces more friction than control, consuming capacity that could be used to execute the project itself.

This does not mean that documentation, governance, or controls are bad. It means they need to have a clear function. A meeting should exist because some coordination needs to happen. A record should exist because certain information needs to be preserved, shared, or used in a decision. An approval should exist because a particular decision requires that authority. A metric should exist because there is a relevant question that needs to be answered.

When this relationship is lost, the mechanism ceases to be a management tool and becomes merely a ritual. It is possible to have an organization that is extremely disciplined in executing processes and, nevertheless, not very mature in project management. Following a process demonstrates adherence to the process; it does not, by itself, demonstrate that the process was well chosen.

## The risk of undersized management also exists

Criticism of bureaucracy can lead to the opposite extreme. If too much complexity is bad, it may seem that the best management is the one with the fewest possible processes. That conclusion is just as misguided as associating maturity with the number of controls. In architecture, a minimalist solution may be exactly what the problem requires or may simply be undersized. The difference lies in the requirements and the consequences of the choices.

In management, the equivalent is eliminating controls because they are inconvenient, slow, or incompatible with the team’s culture, without assessing the risk that remains after that decision. A company may say that it does not need to document decisions because “we are Agile,” avoid a particular governance mechanism because “we are small,” or not formally track risks because “the team talks every day.” In certain contexts, these choices are perfectly reasonable. In others, they simply transfer the cost to a future problem that no one explicitly decided to accept.

This point is important because the absence of a control is also a management decision. If a mechanism was deliberately removed, it should be possible to explain what need it addressed, why that need is not relevant in that context, and what risk is being assumed by not maintaining it. Tailoring does not mean removing whatever seems bureaucratic; it means consciously deciding the level of control required.

The objective, therefore, is not to minimize processes. It is to size management according to the complexity, risks, and constraints of the context.

## A startup is not a scaled-down corporation

This is where early-stage startups become a particularly interesting case. A small organization, with few people, high uncertainty, and a product that is still evolving, operates under conditions very different from those of an established company. Communication is direct, decisions can be made with little intermediation, and much of the information remains available within the context shared by the people themselves. Reproducing a complete corporate project management structure in this environment can mean introducing complexity that the organization does not yet need.

This does not mean an absence of management. The startup still needs to define objectives, assess risks, manage dependencies, make decisions, and track results. What changes is how these activities need to be structured. When a few people need to align on a decision, a conversation may be sufficient. As the number of people involved, interfaces between teams, and cost of a poorly coordinated decision increase, mechanisms that previously seemed unnecessary may begin to have value.

The management practice can therefore remain while its form evolves. A startup does not need to import the governance structure of a large corporation to be professional, just as it does not need to turn every decision into a formal process to demonstrate maturity. But it also should not confuse informality with an absence of management. What can be resolved today through proximity and shared context may tomorrow require explicit coordination mechanisms, not because the organization has finally “adopted a methodology,” but because the problem it needs to manage has changed.

This is one of the clearest examples of management design. The appropriate approach is not a reduced version of a corporate methodology, but a solution built from the characteristics of the organization itself. As it grows, this solution can evolve alongside the system it needs to coordinate.

## Management is also an evolving architecture

What works for a small organization may stop working as it grows, in the same way that an architecture suitable for an application at a particular stage may need to be revisited when its requirements change. This does not mean the previous solution was wrong. It means it was designed for conditions that are no longer the same.

Growth changes the nature of the problem. More people increase interfaces and the cost of communication. More teams create dependencies that did not exist before. More customers increase the consequences of certain failures. More resources involved raise the cost of poor decisions. New regulatory obligations introduce additional constraints. At some point, mechanisms that previously would have been bureaucratic become necessary to maintain coordination and control.

In software architecture, this process is familiar: a solution evolves because the system around it has evolved. Management architecture follows the same logic. An organization should not preserve a particular governance structure merely because it worked in the past, just as it should not introduce new mechanisms simply because it has reached a certain size. The trigger for change should be the new needs, constraints, and risks that have emerged.

Maturity, in this context, is not reaching a state in which all projects use the same amount of process. It is developing the ability to recognize when the management architecture is no longer adequate and evolve it before the system’s complexity makes that change necessary in a traumatic way.

## Agile changes the form, but does not eliminate the problem

This perspective also changes how we look at Agile. The opposition between PMBOK and Agile often starts from the idea that one represents structured processes while the other represents adaptation. This dichotomy overlooks the main point: both can provide mechanisms for dealing with management problems, but they start from different assumptions about predictability, uncertainty, and change.

An adaptive approach makes sense when there is significant uncertainty about what should be built or about which solution will produce value. Working iteratively allows learning and adjusting the path as new information emerges. But iterativity does not eliminate risks, dependencies, stakeholders, budget constraints, security requirements, or governance needs. It simply changes how these elements are handled.

A team can work with short cycles, continuous prioritization, and frequent feedback while also needing to deal with compliance, suppliers, budget, or dependencies between teams. Likewise, an initiative can use predictive planning in certain dimensions and adaptive mechanisms in others. The choice does not need to be ideological. It needs to respond to the characteristics of the work.

That is why hybrid approaches should not be seen as a contradiction, but as a possible consequence of tailoring itself. Different parts of an initiative may have different levels of predictability, risk, and need for control. The relevant question is not which methodology won the debate, but which management mechanisms are necessary to deal appropriately with the context.

Agile does not eliminate the need for management. Just as a predictive approach does not, by itself, imply bureaucracy. What changes is the architecture used to organize and conduct the work.

## Automation changes management trade-offs

The discussion about management design gains another dimension when we consider AI and automation. Choosing which practices to apply also involves considering the cost of operationalizing them. Updating records, consolidating information, producing reports, tracking metrics, and identifying changes requires effort, and that effort influences the decision about the appropriate level of management. A practice may be relevant and, nevertheless, be disproportionate to the context when its execution cost is high.

Automation changes this trade-off. An activity that previously required hours of manual work may come to require only human review. Scattered information can be consolidated automatically, reports can be produced from already available data, and systems can assist in identifying patterns, inconsistencies, and potential risks. This does not simply mean adding more processes because they are now cheap. It means that practices previously considered excessively costly may become sensible when the cost of operationalizing them decreases.

The value of a practice does not necessarily change because it has become cheaper to execute. What changes is the relationship between its benefit, its cost, and the complexity it introduces. A solution that was previously disproportionate may become appropriate to the context, changing the choices available within management design.

There is, however, an important boundary. Automating the collection and analysis of information does not mean automating judgment. A tool can identify a potential risk or deviation, but assessing its relevance, deciding whether it should be accepted, and determining a response still requires context and accountability. AI can reduce the cost of management, but it does not eliminate the need to design it.

## Design management, don't follow the recipe

The problem begins with the question itself: “which methodology should we use?” In solution architecture, we first understand the system, its requirements, constraints, risks, and trade-offs; only then do we define the architecture. Management design follows the same logic: understand the context, size the governance required, and select the practices that address the project’s real problems. When requirements change, the approach may also need to evolve.

This is where PMBOK finds its place. Not as a recipe to be applied in its entirety, but as a repertoire to guide decisions. Maturity does not lie in the number of practices adopted, but in the ability to justify choices: which risks are being addressed, which mechanisms are necessary, what complexity is acceptable, and which controls deliberately do not form part of the solution. Applying fewer practices can be more mature than applying all of them, provided that the choice is conscious and proportional to the context.

In architecture, we do not consider an architect mature because they use every available component, but because they know how to compose a solution suited to the requirements and constraints, consciously assuming the trade-offs. Project management should be no different. PMBOK provides part of the repertoire; the work lies in knowing how to turn it into an approach suited to the problem one intends to solve.
