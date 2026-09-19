# The Security Dilemma: Between Control and Speed

_The challenge of integrating Security into engineering without turning protection into bureaucracy._

**Summary:** I argue that the dilemma between Security and speed is not resolved by choosing one side, but by bringing Security closer to engineering and bringing security knowledge into the moment when decisions are still being shaped. Instead of relying on gates, approvals, and manual interventions, we should turn specialized knowledge into standards, automation, and risk-proportionate guardrails. This way, Security stops being a step that engineering has to wait for and becomes a capability integrated into the process. The ultimate goal is not to eliminate risks, but to allow the organization to learn, experiment, and innovate while knowing which risks it is taking.

---

For a long time, my view of Security was probably simpler than the reality of the field. As someone who works closer to architecture and engineering than to security disciplines, I tended to see Security in a relatively straightforward way: there is an area responsible for security, with policies, tools, processes, assessments, and controls that need to be considered while solutions are being built.

Look a little closer, however, and it becomes clear how limited this view is. Security is a much broader discipline than its name suggests. Identity, applications, infrastructure, cloud, data, architecture, privacy, fraud, incident response, intelligence, third parties, compliance, and several other dimensions may be directly or indirectly related to an organization's security.

This breadth also explains why it is difficult to talk about Security as though we were dealing with a single function. The pace of an incident response team is different from that of GRC. Threat Intelligence has different needs from Application Security. Identity and Access Management has different problems from Product Security. Each of these functions has its own objectives, responsibilities, and time horizons.

This text does not intend to address Security as a whole. The reflection here is more specific and arises precisely from the boundary between Security and what is closer to my reality: architecture, engineering, and software development. It is in this interaction that I began to notice a dilemma that seems increasingly relevant to me.

Security needs to be close to development to be effective. It needs to understand architectural decisions, the technologies being used, and the risks associated with each context. At the same time, the way this participation is structured can produce very different results. When it depends primarily on a sequence of gates, tickets, approvals, sign-offs, and manual controls, an additional step may emerge between engineering and decision-making, especially when similar mechanisms are applied to contexts with different levels of risk.

The challenge, therefore, is not to choose between security and speed. It is to build a model in which Security can protect the organization without reducing its ability to learn, experiment, and innovate. And when we talk about speed, we are not talking only about delivering software faster. We are talking about an organization's ability to learn quickly about new technologies, assess their risks, make decisions, and turn that learning into innovation.

## Security and the Moment of Decision

There is a common pattern in organizations. Product defines what needs to be built, architecture and engineering define how the solution will be built, and at some point, Security is brought in to assess whether it meets security requirements.

At first glance, this model seems reasonable. Each area has its responsibilities, and Security functions as a specialized assessment layer. The point of attention is when this participation happens. When Security enters the discussion after most of the decisions that influence risk have already been made, its opportunities to contribute naturally become more limited.

When a risk is identified at this stage, the architecture may already be defined, the code may already have been written, dependencies may already have been chosen, and the product may already have delivery expectations. A security decision that could have been naturally incorporated during the solution definition may, at this point, require a more significant change, alter a technology choice, or even require a substantial portion of what has already been built to be reviewed.

This is where timing becomes important. A security recommendation made at the beginning of defining a solution may represent only an architectural decision. The same recommendation made when implementation is already advanced may mean rework, component changes, integration reviews, or an impact on a schedule that is already committed to a delivery date.

Tickets enter this process as a legitimate way to record these demands, organize responsibilities, and track their resolution. The problem is not the ticket itself, but what it represents when a significant security decision is discovered only at an advanced stage of development. From that point onward, there is tension between properly addressing the risk and preserving the timeline and scope that have already been established for the delivery.

When this happens repeatedly, the interaction between Security and engineering can become concentrated on evaluating what has already been produced rather than occurring during the decisions that gave rise to the solution. The work remains important, but part of Security's potential contribution is lost because the room to change the solution at low cost has already diminished.

There is also a relevant organizational consequence. The farther Security is from the decisions that originate a solution, the greater the importance of formal mechanisms may become to ensure that security requirements are considered. Policies, approvals, evidence, gates, and processes are legitimate instruments for this purpose. At the same time, when Security participates earlier in decisions, part of this need can be addressed in other ways, such as standards, automation, reusable components, and shared knowledge.

The question is not to eliminate control mechanisms, but to find the most appropriate way to exercise them. In some contexts, a formal approval will be necessary. In others, the same knowledge can be embedded in the architecture, platform, or development process itself. The way control is exercised can vary according to risk, context, and, above all, the moment when the decision is made.

## The True Meaning of Speed

When we say that Security needs to keep pace with engineering, we should not be talking only about ticket response time or software delivery speed. The more important issue is the speed at which the organization can learn, make decisions, and turn that learning into innovation.

A technology organization needs to experiment. It needs to test new architectures, platforms, services, frameworks, and tools. It needs to quickly discover what works, what the risks are, what the costs are, and which technologies can generate competitive advantage. This learning process does not necessarily happen in quarterly cycles. Often, a relevant decision needs to be made within hours or days.

Imagine that a new technology emerges and a squad sees a strategic opportunity to use it. If the process required for Security to assess that technology takes weeks or months, the impact can go far beyond time to market. The organization loses its ability to experiment and, above all, to learn. While the technology evolves, the opportunity may disappear and the decision may cease to make sense.

There is also a less obvious consequence. When security processes do not keep pace with engineering needs, pressure for alternatives may increase. A team may look for another tool, use a service outside corporate standards, or build a temporary integration to keep moving forward. This does not always result from a deliberate intention to circumvent controls. Often, it is simply the result of a business or engineering need that emerged before an adequate response existed in the formal process. The effect can be reduced visibility into what is being used and less opportunity to influence how the technology is adopted.

For this reason, speed is also a dimension of security. Effective Security needs to be fast enough to participate in the experimentation process while the decision is still being shaped. It is not enough to evaluate a technology after the business has already decided to use it. It needs to be able to understand its risks, propose proportionate controls, and establish conditions under which experimentation can happen safely.

This proximity also benefits Security itself. New technologies do not represent only risks to be assessed. They also require learning. New architectural models, cloud services, development tools, and emerging technologies can introduce risks that do not fit perfectly into existing controls. Being close to engineering allows Security to understand these changes at the same time they are being explored by the organization.

The goal is not simply to reduce delivery time. It is to reduce the interval between a hypothesis, experimentation, learning about its risks, and a conscious decision about its adoption. When an organization can shorten this cycle, it not only delivers faster. It increases its ability to learn, adapt, and innovate without giving up a conscious assessment of risks.

## Security as Part of Engineering

Perhaps the most important change is to stop thinking of Security as a stage in the development process and start treating it as one of the disciplines that participate in that process. Security should not be something that is checked only at the end of a solution. It should be one of the dimensions considered while the solution is still being designed and decisions can still be changed at a lower cost.

Security should not appear only when there is something to approve. It should participate in defining the solution. A Security professional close to engineering can discuss with the architect what the solution's trust boundaries are, how authentication between services will work, what data will be handled, where the exposure points will be, what privileges will be required, how secrets will be stored, which external dependencies will be used, and which threats are actually relevant in that context. The value of this participation lies precisely in happening while these decisions are being made, rather than after the architecture has already been established.

This participation is different from placing someone inside the squad to police the work. Proximity to engineering should exist to enable more effective collaboration in building the solution, not merely to monitor what developers are doing.

In this sense, I like the idea of treating the Security professional as a partner to the solutions architect. Product, architecture, and engineering need to decide how a particular solution will be built. Security contributes to understanding which risks this architecture introduces, which threats are relevant, and how those risks can be mitigated without unnecessarily compromising the system's objective.

This proximity also changes the nature of the conversation. Instead of discussing only whether a particular technology can or cannot be used, it becomes possible to discuss under what conditions it can be used safely. Instead of discovering later that a given architecture has an undesirable exposure, it becomes possible to identify that exposure while alternatives are still being evaluated.

This does not mean transferring responsibility for the solution to Security. Product remains responsible for the product, engineering for implementation, and architectural decisions remain with the people responsible for the solution. Security adds specialized knowledge about risks and controls to this discussion.

This distinction is important because integrating Security into engineering does not mean making Security responsible for everything involving security. It means distributing the knowledge required for decisions to be made by those who have the context, with the participation of those who have the specialization.

The question shifts from simply “Did Security approve?” to “Was the solution built considering the risks relevant to its context and the measures necessary to address them?” The change is less about removing an approval step and more about bringing security knowledge into the moment when decisions are still being shaped.

This integration creates a requirement for the Security professional as well. It is not enough to be present in squad meetings or to know the development lifecycle as a process described in documentation. To participate effectively in engineering, it is necessary to understand the process as a practice.

A concrete way to develop this understanding is to build. A proof of concept can go through the entire path of a solution, from defining the requirement and architecture to development, pull request, pipeline, security testing and controls, deployment, and observability. The goal is not to turn the Security Engineer into a developer, but to provide enough practical experience to understand the constraints, incentives, and trade-offs that are part of everyday engineering.

Practical experience also changes the way Security evaluates its own recommendations. When implementing a control in a real solution, the professional begins to see the dependencies, implementation effort, and impacts that decision produces in the pipeline and development lifecycle. This perspective is difficult to obtain solely through defining policies or reviewing documents and helps assess whether a given control is producing risk reduction proportional to the friction it introduces.

If a recommendation requires excessive manual processes, generates many exceptions, or is difficult to implement, this may be a sign that the control needs to be redesigned, automated, or incorporated into an architectural standard or platform component.

The more Security understands how software is actually built, the better it can assess not only the risks of a solution, but also the most appropriate way to address them. Likewise, the more engineering understands the reasons behind controls, the greater the possibility that security will be incorporated into the technical decisions themselves, reducing the need for later interventions.

## From Gate to Guardrail

This leads us to an important distinction between gates and guardrails. A gate conditions the continuation of the flow on meeting a condition or making a decision. A guardrail establishes the boundaries within which work can proceed and can incorporate checks and blocks directly into the engineering environment. The difference lies less in whether blocks exist and more in how they are incorporated into the process. In a gate-based model, certain decisions need to be explicitly evaluated before the flow can proceed. In a guardrail-based model, some of these conditions can be embedded into the development process itself.

Both may be necessary. A change involving highly sensitive data, elevated privileges, or critical exposure may justify human assessment. In other contexts, especially when the decision is recurring and predictable, automated controls may offer a more efficient way to address the same risk.

Not every decision has the same level of risk and, therefore, not every decision needs to require the same level of intervention. The more recurring, predictable, and low-risk the situation is, the greater the ability to address it through standards, automation, and self-service. As the criticality, exposure, or complexity of the decision increases, so does the value of specialized Security analysis.

This is the logic of a risk-based approach: the level of control should be proportional to the risk it is intended to address. The objective should not be to maximize the number of controls, but to find an efficient way to reduce relevant risks without introducing disproportionate friction into the engineering process. A control that requires recurring manual intervention from dozens of squads can consume a significant amount of specialized capacity, even when its application is justified in certain contexts.

In this context, automation stops being merely an efficiency initiative and becomes a scaling strategy. If fifty squads need to implement the same control, the knowledge used in those decisions can be transformed into a component, policy, pipeline, template, or platform capability that already incorporates that control securely. Instead of reproducing the same analysis in different contexts, part of this knowledge can be made directly available to engineering.

This transformation allows Security to concentrate its human capacity where its participation adds the most value: new, complex, high-impact decisions or decisions that depend on context. For what is recurring and predictable, knowledge can be incorporated into engineering itself.

Security does not scale sustainably by adding people in the same proportion as the number of squads grows. It scales when it transforms specialized knowledge into reusable capabilities and allows controls to be applied consistently by many teams. Whenever possible, this makes the secure path also the simplest path for engineering.

## Time and Scale: Security Beyond the Queue

There is an important operational consequence when Security becomes part of the engineering lifecycle. If engineering makes decisions in hours or days, the time required for a security assessment needs to be compatible with the time horizon of those decisions. This does not mean turning every request into an urgent one, but rather avoiding a situation in which security analysis operates at a pace completely disconnected from the engineering process.

This also changes the discussion about scale. The challenge is not simply to make Security respond more quickly to the requests it receives, but to reduce the number of decisions that depend on a specific manual response. A common, low-risk technology can be used through predefined standards. A recurring architecture can have security mechanisms already incorporated. A simple policy can be validated automatically. A known vulnerability can, whenever possible, be detected and addressed by the pipeline.

The more predictable a decision is, the less likely it is to require a specific human intervention. When the secure path is automated, the squad does not need to wait. When an architectural standard already incorporates the necessary controls, there is no need to reproduce the same analysis for every new implementation. When Security participates in the architectural discussion, a decision can be addressed while the solution is still being built, reducing the need to subsequently send it for another assessment.

This is where tickets reveal a capacity issue. They remain useful for recording requests, responsibilities, and decisions, but they do not eliminate the structural dependency between many squads and a specialized Security capacity. If different teams need to consult Security individually to make similar decisions, the organization is repeating interactions around knowledge that could be reused.

Security that scales needs to transform specialized knowledge into capabilities that can be used by many teams simultaneously. This includes architectural standards, automation, reusable components, documentation, enablement, guardrails, and platforms that incorporate controls directly into the development process.

New technologies can help with this process. Artificial intelligence, for example, can expand the capacity of Security professionals in analysis, triage, guidance, and risk identification activities. It can make specialized knowledge more accessible and reduce the effort required for certain tasks. But this, by itself, does not change the operating model. If the process continues to depend on tickets, approvals, and individual interventions, more sophisticated tools may simply make this flow more efficient without eliminating its dependence on specific interactions.

The scaling gain happens when knowledge stops depending on an individual interaction and becomes part of the engineering process itself. A standard can be reused by dozens of squads. A control can be automated. A platform capability can eliminate the need for manual implementation. Guidance can be available at the moment the decision is made.

This also redefines the role of the central Security team. Instead of concentrating its capacity on individually reviewing everything that happens in the organization, it can direct its human effort toward new, complex, or higher-impact decisions while investing in building the capabilities that allow other teams to make recurring decisions with greater autonomy.

Scaling Security does not simply mean handling more requests or responding to more tickets. It means enabling specialized knowledge to influence a much larger number of engineering decisions without requiring human interaction proportional to the number of those decisions.

## Security as Part of the Culture

In the end, there is a dimension that no process, tool, or organizational structure can solve on its own: culture. Not in the sense of campaigns, mandatory training, or statements about “security first,” but in the way the organization makes decisions when security, speed, and innovation come into tension.

A mature organization should not depend on Security to continually remind engineering that security matters. Likewise, Security should not depend on processes to continually remind engineering that certain controls need to be followed. Knowledge about risk needs to be present where decisions are made.

This requires learning on both sides. Security needs to know engineering not only to understand how software is built, but to understand how the organization learns, experiments, and turns technology into products. Engineering needs to know security not only to comply with controls, but to incorporate risk into its own technical decisions.

This is where the dilemma changes in nature. The question stops being how much control the organization needs to exercise over engineering and becomes how much security knowledge it can distribute without turning every decision into a dependency on Security.

The goal is not to make Security chase engineering, nor to make engineering wait for Security. It is to reduce the situations in which one needs to wait for the other. To do this, Security needs to be close enough to participate in decisions and transform specialized knowledge into context, standards, and capabilities that engineering can use.

Perhaps the true balance between control and speed lies precisely there: not in eliminating controls, nor in endlessly accelerating approval processes, but in placing each mechanism where it produces the most value.

As a solutions architect, this is the perspective from which I see this dilemma. Not from the responsibility of defining how Security should operate, but from the experience of being at the point where product, architecture, engineering, and security decisions need to converge. It is at this point that it becomes clear that security and speed do not need to compete for the same space. The challenge is to create mechanisms that allow both to move forward together.

An organization capable of innovating needs to learn quickly about technology, but also about the risks that technology introduces. Not to eliminate risk, but to distinguish what needs to be mitigated, what can be accepted, and what cannot be assumed.

Security, in this context, stops being merely a function that protects what the organization has built. It begins to contribute to its ability to decide, with awareness of risk, what it can still build.
