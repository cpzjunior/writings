# Investigative Architectures: from information gathering to continuous intelligence

_An AI-oriented architecture for investigating business questions, learning from context, and continuously tracking what may change a decision._

**Summary:** I argue for an intelligence architecture that treats investigation as its primary unit: a persistent process that formulates hypotheses, connects evidence, preserves context, and resumes work when new information emerges. A scheduler decides which investigations deserve processing, how much effort is worth investing, and what the next step should be, while memory, human feedback, and governance provide continuity and reliability. Thus, AI moves beyond merely collecting, monitoring, or summarizing information and begins to sustain a continuous investigation process in which the architecture itself learns from what it has discovered and returns to the problem when the world changes.

---

While writing “[The Anti-Mage: A Literary Project](https://cpzjunior.substack.com/p/o-anti-mago-um-projeto-literario)”, I began to realize that Alden’s journey as an investigator was making me think more and more about the act of investigating itself: following clues, formulating hypotheses, connecting events, and discovering that an answer can change the next question. At some point, this idea left fiction. I started thinking that the role of an investigator could also be interesting in a product. Not as a metaphor, but as a different way of thinking about intelligence systems.

Imagine a company about to hire a strategic supplier. Before signing the contract, a simple question arises: are there public signals that this supplier may be entering a situation that could affect our business relationship?

Answering this question may involve news, public databases, complaints, corporate information, and social media. When something seems relevant, new searches are needed to understand the context.

Now imagine giving this question to an intelligence architecture. It researches the supplier, its related companies, and recent events. It finds a relevant news story, identifies a related company, and opens a new line of investigation. It then finds conflicting information and looks for sources closer to the original fact. One hypothesis gains strength, another loses relevance, and a new question emerges. At some point, the architecture may conclude that there is still insufficient evidence to recommend an action and place that investigation under monitoring.

Days later, new information emerges. The investigation returns to the queue, but it does not start from scratch. It resumes its previous state, with its hypotheses, evidence, sources, and uncertainties.

This is the behavior that interests me. The same architecture could investigate a competitor, a market opportunity, an emerging technology, a potential customer, or a strategic hypothesis. The starting point is no longer simply the entity we want to monitor, but the question we need to investigate.

## From monitoring to investigation

There is an important difference between monitoring and investigating. A monitoring system can notify us that a company was mentioned in a news story, but the mention itself does not necessarily tell us what happened, what its relevance is, or whether it should change any decision.

In information security, a SOC, Security Operations Center, exists precisely to deal with this problem. Logs, network events, endpoint alerts, and other sources continuously produce signals that, in isolation, may mean little. The SOC correlates these events, looks for patterns, investigates the context, assesses severity, and, when necessary, initiates a response. An alert is not necessarily an incident. The work lies in understanding what exists behind it.

The same logic can be applied to public information and business questions. A complaint is a signal. Ten similar complaints within a few days may indicate something else. A video may increase exposure, a post may accelerate dissemination, and a report may turn an isolated problem into an evolving incident. The task becomes understanding how these events relate to one another, which hypotheses best explain what is happening, and what still needs to be discovered.

This also changes the role of search. A traditional search ends when we find a satisfactory answer. In an investigation, the result of a search may determine what should be researched next. A news story about a technology may lead to an investigation into the company that developed it. An acquisition may generate questions about investors, technology, or other related moves. Conflicting information may require a primary source.

The investigation evolves as new evidence appears. Some lines are discarded, others gain priority, and new questions emerge. The architecture needs to follow this process, maintaining the context of what has already been discovered and deciding what the next step should be. The difference is not in making an AI search the Internet. It is in making an architecture maintain an investigation.

This also changes how we think about agents. Instead of agents permanently running searches, we can have permanently existing investigations, each with its own state and waiting for the right moment to receive processing capacity.

## A scheduler for investigations

When I began thinking about this architecture, an analogy with operating systems seemed particularly useful to me. An operating system needs to manage limited processing capacity among multiple processes. It tracks the state of each process, sets priorities, interrupts some, resumes others, and distributes CPU time according to what needs to be executed.

An investigative architecture could work in a similar way. Instead of having a set of agents continuously executing searches, we would have a set of persistent investigations, each with its own state, priority, objective, level of uncertainty, and budget. Some would be active, others waiting for new evidence, and others practically complete. The scheduler would be responsible for deciding which one receives the next unit of processing capacity.

Imagine dozens or thousands of investigations happening simultaneously. One is tracking a supplier that has shown no relevant signals for weeks. Another is investigating a competitor that recently announced an acquisition. A third is tracking an emerging technology. A fourth is trying to understand a sequence of complaints that began a few hours ago. It would not make sense to treat all of them in the same way.

The first might need only another periodic check. The second may require a deeper investigation. The third may remain low priority until a relevant signal appears. The fourth, depending on the potential impact and speed of events, may need to receive capacity immediately.

And the next processing cycle also depends on the investigation’s state. An investigation may begin by looking for recent news. After finding a related company, the next cycle may be dedicated to understanding this new entity. If conflicting information emerges, it may be necessary to look for a primary source. If a corporate change appears, it may make sense to investigate the controlling parties. If several sources are reproducing the same information, the next step may be to identify its origin.

The scheduler, therefore, is not simply asking “which search should run now?” It is asking “which investigation deserves attention now, and what is the most useful action we can perform within it?”

This brings the architecture closer to a system of concurrent processes. An investigation can be interrupted to make room for another that is more urgent. It can generate a sub-investigation that begins competing for resources. One line can be closed while another continues. An investigation can become blocked while waiting for new evidence and return to the queue when something changes.

The operating-system analogy also helps us think about a problem that tends to remain hidden when we talk about agents. We do not need a dedicated agent for every problem. Just as an operating system shares processing capacity among processes, an investigative architecture can share agentic capacity among investigations.

This significantly changes the idea of continuous automation. We are not creating thousands of robots polling the Internet at fixed intervals. We are maintaining investigations in different states and dynamically deciding which ones deserve processing, how much processing they should receive, and what the next step should be.

At the limit, the scheduler becomes a central piece of the architecture. It is not merely a resource distributor. It is the mechanism that transforms a collection of persistent investigations into a system capable of continuously working on them.

And this leads us to an inevitable question: if investigating costs resources, how do we decide when it is worth continuing to investigate?

## How much is it worth continuing to investigate?

There is another question that emerges when we take this architecture seriously: investigations have costs. There are API calls, searches, processing, storage, inference, agent time, and, in some cases, access to paid sources. If the system can deepen any investigation indefinitely, it may produce increasingly complete analyses, but it can also consume resources without necessarily generating more value.

Therefore, the architecture must not only decide what to investigate. It must decide how much effort is worth dedicating to each investigation.

Here, I like to make a pun with ROI. Traditional ROI asks whether an investment is worthwhile. In this case, we can ask whether an investigation is worthwhile. The I becomes Investigation.

It does not need to be a rigid formula. It can be a heuristic based on a few simple questions: what is the probability that new information will change our conclusion? What would be the impact of that change? How much does it cost to obtain it?

If the investigation already has consistent evidence, the remaining uncertainty is small, and another search is unlikely to change the decision, it may be better to reduce the frequency, enter monitoring mode, or simply close that line. On the other hand, if a single additional piece of information could change an important decision, the next investigation cycle may have much greater value.

This creates the idea of an investigative budget. The architecture can concentrate capacity where there is greater potential information gain and reduce effort where marginal returns have declined. The scheduler begins considering not only urgency and risk, but also the potential value of the next step.

And here an interesting characteristic of this problem appears: we probably will not know in advance what the best strategy is for every situation. Some decisions will initially be defined by heuristics and then adjusted based on observed results. The architecture can learn which paths tend to produce relevant evidence, how much they cost, and at what point continuing the investigation ceases to make sense.

In the end, intelligence is not only about discovering more. It is also about knowing when we have discovered enough.

## The investigation needs to remember and learn

An investigation should not merely accumulate documents. It needs to work with hypotheses, preserve what it has already discovered, and incorporate the context of the person or organization conducting the investigation.

Suppose a sequence of public criticisms against a company is growing. One possibility is that there is a real operational problem. Another is that the problem is isolated and being amplified. Another is that there is a coordinated campaign. Another is that different events are being grouped together because they appear similar.

The architecture should not immediately choose one narrative and search only for information that confirms it. It should maintain competing hypotheses and seek evidence that helps distinguish between them.

This also requires separating what was found from what was inferred. A source states a particular fact. That is evidence. The conclusion that this fact represents a specific risk to the organization is an inference. Likewise, a relationship between two events may be relevant without proving that one caused the other.

The investigation must also consider the independence of sources. Ten websites repeating the same news story do not necessarily represent ten pieces of evidence. It is necessary to understand the origin of the information, identify duplicates, and, whenever possible, seek the source closest to the fact.

And there is a limitation that should be present in any conclusion: failing to find information does not mean proving that something does not exist. A responsible conclusion would be: no relevant signal was found within the perimeter of sources searched. The difference between certainty and absence of evidence is small in the wording and enormous in practice.

But this rigor loses value if every investigation starts from scratch. To provide continuity, the architecture needs to preserve what was being investigated, which hypotheses were raised, what evidence was found, which sources were considered, which hypotheses were discarded, which questions remained open, and what the last conclusion was. It is not enough to store the history of conversations with a model. It is necessary to maintain the state of the investigation.

This state also needs to coexist with the organization’s specific knowledge. One company may consider a particular supplier critical while another may consider it easily replaceable. Information that represents a significant risk in one context may be irrelevant in another. The same entity may have completely different relationships with different organizations.

Therefore, the architecture needs to build a context specific to each organization, incorporating entities, relationships, definitions, policies, preferred sources, classifications, previous decisions, and, above all, corrections made by people.

This human feedback becomes part of the investigation cycle. A user can correct an association between companies, challenge an inference, confirm a relationship, discard a hypothesis, or indicate that certain evidence is more relevant than the system considered it to be. These corrections should not disappear when that investigation ends. They can alter the context used in future investigations.

This does not necessarily mean retraining the model. There is a difference between the model learning and the architecture learning. The model can remain exactly the same while the architecture accumulates knowledge about the organization, incorporates corrections, identifies which sources are most useful for particular problems, and adjusts its heuristics.

In this sense, the architecture does not learn only about the world. It learns from the organization and about how to investigate the world.

## Autonomy requires governance

It is tempting to call all of this autonomous investigation, but there is an important distinction. The autonomy that interests me lies primarily in conducting the investigation.

The system can decide which source to consult, which hypothesis to deepen, when to create a sub-investigation, when to reduce effort, when to seek additional evidence, and when to return to an investigation that had been paused.

This does not mean that it should independently make a legal decision, terminate a business relationship, or reject a supplier. The greater the impact of the decision, the greater the level of governance required.

An enterprise architecture needs to allow for different levels of autonomy, ranging from observing and alerting to recommending actions that require human approval. In some highly controlled contexts, certain actions could eventually be automated. In others, that would be inappropriate.

This autonomy also creates another requirement: the architecture needs to represent its uncertainties and be able to explain the path it followed.

The more the investigation influences a decision, the more important it becomes to reconstruct how that conclusion was reached. A technical log may say that an agent executed a search at 2:32 PM. That does not explain the investigation.

Something closer to an investigative trail would be necessary: what was the original question, which hypotheses existed, which sources were consulted, which evidence was considered or discarded, what organizational context was used, which intermediate conclusions were produced, why a particular new search was conducted, and how all of this led to the final recommendation.

If a user corrected a piece of information, that correction should also be part of the history. If a recommendation was accepted and later proved inadequate, that outcome should return to the architecture’s learning cycle.

Auditability, in this context, is not merely a compliance concern. It is part of the quality of intelligence itself. The more autonomy we give the system, the more we need to understand what it did, why it did it, and what evidence it relied upon.

An investigation that cannot explain its path is much harder to trust.

## The market already has many of these pieces

It is important to put this idea into perspective. I am not proposing a technological category that does not yet exist. The international market already has mature platforms for competitive and market intelligence, monitoring, AI-assisted research, and analysis of external sources. In 2026, for example, Gartner already treats Competitive and Market Intelligence Platforms as a distinct evaluation category, encompassing capabilities such as source aggregation, validation, AI-powered search and analysis, knowledge management, and enterprise integration.

There are also solutions that work with large volumes of sources, continuous monitoring, and insight generation about competitors, markets, and other strategic entities. In Brazil, there are companies working in competitive intelligence, monitoring, market intelligence, reputation, and information analysis. Therefore, I do not see novelty in each of these components individually.

The question that seems more interesting to me is another one: how can we reorganize these capabilities around investigation as the primary unit? Instead of starting with the entity and asking what happened to it, I propose that the architecture start with the question and, from there, discover which entities, sources, events, and relationships need to be investigated. Search stops being an isolated execution that ends in a report and becomes part of an investigation that evolves as new evidence appears. The report stops being the endpoint, and the decision becomes a state that can be revisited whenever new information may change what we know.

This composition is where I see room for a different architecture. Not to replace the capabilities that already exist, but to connect them in a persistent investigative process capable of adapting its depth, prioritizing resource usage, incorporating organizational knowledge, and learning from feedback.

I also see room to adapt this architecture to the Brazilian context, where public sources, corporate structures, the regulatory environment, market characteristics, and governance requirements may demand specific investigation strategies. In this case, adapting to the context would not simply be a localization layer, but part of the system’s intelligence itself.

## From information gathering to continuous intelligence

When these ideas come together, the architecture no longer looks like merely a sophisticated search mechanism. Information becomes the fuel for a persistent investigation capable of formulating questions, tracking hypotheses, preserving context, deciding on next steps, and returning to the problem when new evidence emerges. AI participates in this process, but the architecture provides continuity, memory, context, and governance.

This changes the central question. Instead of starting with “which model are we going to use?”, perhaps it is more interesting to ask “how are we going to organize the process through which the system investigates?” Some answers will initially be defined by heuristics and others discovered in practice. Over time, the architecture can learn which sources work best for particular problems, which paths produce relevant evidence, and when continuing to investigate stops generating value. It is not only about making the model answer better, but about making the system investigate better.

If we look at this evolution, first we built systems to collect information. Then, systems to monitor it. More recently, systems capable of summarizing and analyzing large volumes of content. The next step may be an architecture in which information stops being the final product and instead feeds a continuous investigation process.

There are still many questions to define around priority, cost, quality, heuristics, and autonomy. More than problems that need to be solved in a single way, these variables can be part of the product’s own configuration, allowing the architecture’s behavior to be adapted to the context, risk, and objectives of each organization. The difference between a research tool and continuous intelligence may lie precisely there: not in finding more information or producing better summaries, but in building a system capable of investigating questions, learning from what it has discovered, and returning to the problem when the world changes.
