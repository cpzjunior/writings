# How to Keep Your MVP from Becoming a Leviathan

_Between the complexity that anticipates the future and the simplicity that prevents learning._

**Summary:** An MVP is not the smallest product we can put into production, but the smallest necessary set for testing a hypothesis and learning something relevant from the outcome. The risk lies both in building too much, anticipating problems that may never exist, and in building too little and compromising the validity of the learning. Therefore, complexity needs to be proportional to what we know, the risks that actually matter, and the questions we need to answer at that moment. The MVP can grow as we learn, but this growth should be a consequence of the knowledge acquired, not an attempt to anticipate the future.

---

I have seen many people with good ideas struggle to turn them into reality. I addressed part of this problem in “[Before taking an idea off the drawing board, you need to put it on one](https://cpzjunior.substack.com/p/antes-de-tirar-uma-ideia-do-papel)“, but there is a difficulty that begins precisely when the idea stops being just an idea and starts being built: keeping the MVP small without compromising its viability.

The initial intention is usually simple. Build enough to put a hypothesis to the test and learn from the result. The problem is that, as development progresses, good reasons emerge to expand the scope. A feature seems necessary, an exception seems important, an architectural decision could be generalized, a concern about future scale seems prudent. Little by little, what should have served to test a hypothesis begins incorporating answers to problems we do not even know whether we will have.

To make user registration easier, we will implement different authentication mechanisms, such as SSO and OAuth. Since the system needs to account for different levels, profiles, and access rules, we will need a multidimensional permissions model, like those used by enterprise platforms such as Salesforce. Since we will have a subscription system, we will build a blockchain-based ledger and a geolocation system for fraud prevention. To guarantee full availability, we will adopt a multicloud architecture across multiple AZs. To anticipate a possible expansion into Latin America and Asia, we will also support multiple locales and regional configurations. Before we know it, we started out trying to validate a product hypothesis and are designing a globally distributed platform to solve hypothetical problems before even knowing whether the product solves the problem for which it was created.

This is where the comparison with Leviathan emerges. In the biblical tradition, Leviathan is a monster associated with the sea and chaos, a creature that escapes human control. The comparison is almost literal: the MVP starts as something small and manageable, but it can accumulate features, dependencies, rules, and exceptions until it becomes a monster whose complexity no longer easily responds to the intention that gave rise to the product.

But there is a trap in the opposite direction. In trying to keep the MVP under control, we may cut precisely the elements needed to test the hypothesis. The result is small, but it is no longer sufficiently viable to tell us whether we are looking at an adequate solution.

It is within this tension, between building too much and building too little, that the discussion begins about what should actually fit inside an MVP.

## The MVP Is Not a Small Product

MVP is often understood as a product with few features. It is an intuitive definition, but an insufficient one. The “minimum” is not about the amount of software we can build, but about the smallest necessary set for putting a relevant hypothesis to the test with sufficient reliability.

This distinction changes the way we decide what goes into the product. The question should not be “what is the smallest amount of code we can put into production?”, but “what is the smallest investment capable of teaching us something relevant about the product?” The second question forces us to consider not only what will be built, but also the quality of the learning that it will be capable of producing.

A feature can be simple to implement and still be indispensable for testing the hypothesis. Another may require little effort and add practically nothing to what we need to discover. Development effort, therefore, is not a good standalone indicator of relevance. What matters is that part’s contribution to the experiment.

That is why a small MVP can be inadequate. By removing an essential part of the experience, we may put something into production quickly but produce a result that does not answer the original question. In that case, we reduce the product without necessarily reducing uncertainty. We build less, but we also learn less.

The same reasoning applies to excess. A solution can be technically sophisticated and work perfectly, while incorporating capabilities that are not yet necessary to test the thesis. The problem, in this case, is not necessarily the quality of the solution, but the timing of when we choose to build it. We are investing to answer questions that the product has not yet forced us to ask.

The size of the MVP, therefore, is not an absolute measure. It needs to be proportional to what we want to discover at that moment.

### How the Leviathan Is Born

The growth of an MVP rarely happens because of a single major decision. It usually emerges from a succession of small decisions that, taken individually, seem perfectly defensible. An integration seems necessary, an exception seems simple to accommodate, a more generic structure seems to avoid rework, a concern about scale seems prudent. An additional configuration seems cheap. A feature requested by a user seems too important to leave out.

This is the context in which the familiar “since we’re doing this, we might as well do that too” appears. With each decision, the scope shifts a little. Since no individual change seems significant enough to justify stopping, their sum goes unnoticed until the product is already addressing problems that were not part of the original question.

The most treacherous point is that the cost of a decision rarely ends with its implementation. A new feature begins to require testing, monitoring, documentation, support, and maintenance. It can introduce dependencies, new states, business rules, and execution paths that did not previously exist. It can also constrain future decisions, making it more expensive to change direction when new information appears.

Therefore, the cost of a feature is not just the effort required to put it into production. It is also everything that begins to exist after it enters the system.

This is how scope can escape its original intent without there being an obvious mistake to point to. Each local decision can make sense, while the accumulated result no longer does. The Leviathan does not necessarily emerge from an absurd choice, but from the sum of reasonable choices that, together, produce a complexity that no one intended to build.

## The Problem with Trying to Solve the World

There is a particularly dangerous form of anticipation: trying to build, from the beginning, the solution to every problem the product might have in the future.

When the thesis is still uncertain, we start imagining different user profiles, business models, large data volumes, multiple integrations, internationalization needs, different permission levels, and scale scenarios. Each concern may be legitimate in isolation. The problem appears when all of them begin influencing the first version of the product.

It is understandable. Anyone who builds systems knows that some decisions are difficult to change later and that certain choices can create technical debt. They also know that correcting an inadequate architecture later can be much more expensive than making a good decision from the start. The risk is turning this legitimate concern into an attempt to predict the entire product before we even know whether it is, in fact, an adequate and viable solution.

It is like assuming the role of Atlas before knowing whether there will be a world to support: we prematurely carry the weight of every possible future, without knowing which of them will actually exist.

There is an inversion here. Instead of the solution evolving from what we learn about the problem, we begin building a solution for a hypothetical future. We start making decisions based on users who may exist, volumes that may be reached, markets that may be explored, and requirements that may never appear.

That future has a cost in the present. And, at the initial stage, we may not even know whether we will get there.

The architecture needs to deal with real risks, not every imaginable possibility. The same applies to product. A decision deserves an investment proportional to the importance and probability of the problem it intends to solve. Preparing everything for a scale that may never exist means paying in advance for a future that has not yet been validated.

## Complexity Can Also Be Necessary

This does not mean that all complexity is a sign of excess. There are products in which security, auditing, resilience, observability, access control, or operational requirements are part of the solution itself. In such cases, removing complexity does not necessarily mean simplifying the product. It may mean removing a property required for it to function correctly.

In certain contexts, oversimplifying the system may actually be the irresponsible decision. An MVP that moves money, handles sensitive data, or participates in critical processes cannot use experimentation as a justification for ignoring essential properties of the domain. The fact that we are validating a hypothesis does not suspend the risks that already exist.

There is also a difference between the complexity perceived by the user and the complexity required in the system. An experience can be simple on the surface and depend on a highly sophisticated infrastructure to function securely, resiliently, and reliably. The objective, therefore, is not to eliminate complexity, but to avoid complexity that has no concrete reason to exist at that moment.

Therefore, the question should not simply be “how can we make the system simpler?”, but “what complexity is necessary for this stage of the product?” The answer depends both on the hypothesis we want to validate and on the risks we cannot accept.

This distinction also helps avoid a false opposition between product and engineering. Product may be trying to reduce scope to validate a hypothesis, while engineering may be trying to reduce a relevant technical risk or avoid a decision that is difficult to reverse. Both concerns are legitimate. The work of architecture is precisely to evaluate these trade-offs and find a solution proportional to the product’s stage, without turning simplicity or sophistication into absolute principles.

## Building Less Can Also Be a Mistake

The reaction to excess is usually to cut. We eliminate features, simplify flows, and reduce scope until we arrive at something that seems small enough to be called an MVP. The problem is that reducing the product does not necessarily increase the quality of the experiment.

There is an important difference between reducing what will be built and reducing the ability to learn from what has been built. A hypothesis may depend on certain elements of the experience to be tested in a minimally representative way. Removing precisely those elements can produce an apparently objective result, but one that answers a different question from the one we intended to ask.

We may, for example, conclude that a solution does not work when, in fact, we tested such a simplified version that it ceased to represent the original value proposition. In that case, we built less, but we also learned less.

Therefore, the MVP is not merely intended to put something into production. It needs to produce a result that is useful for the next decision. The more the solution is simplified, the more important it becomes to understand what was preserved and what was removed. A simplification that eliminates precisely the element responsible for connecting the problem to the solution can make the experiment cheap but uninformative.

In some cases, the best MVP may not even be software. A prototype, a manual operation, or a limited pilot may answer the question with less investment and less complexity. If we can test the hypothesis without building the entire system, that may be the most appropriate way to start.

The goal is not to build as little as possible. It is to build only what is necessary for the result to tell us something worth knowing.

## The MVP Needs to Be Diagnosable

This may be one of the most important criteria for deciding what goes into a first version: when the experiment is over, we need to be able to interpret what happened.

An MVP can fail for different reasons. The hypothesis about the problem may be wrong. The solution may not be adequate. The experience may not work as expected. The price may be wrong. The acquisition channel may not work. The technology may impose some limitation. The operation may be unviable. The observed result is a consequence of a combination of these variables, and it is not always possible to determine precisely which one was responsible.

The more things we change simultaneously, the harder it becomes to interpret the result. A product may have been rejected because the value proposition did not make sense, because the experience was poor, or simply because an implementation limitation prevented the user from perceiving the solution’s value. Without some care in composing the MVP, a negative result may say very little about the hypothesis we intended to test.

This does not mean that every MVP needs to be a controlled experiment or that it is possible to isolate every variable perfectly. Real products rarely offer this level of control. It simply means that we need to preserve some ability to distinguish what we are learning. There is a difference between accepting the uncertainty inherent in the product and introducing so much complexity into the experiment that the result itself becomes difficult to interpret.

An MVP, therefore, needs to be more than executable. It needs to be diagnosable. Its result should be capable of guiding the next decision, whether to correct the solution, reformulate the hypothesis, or simply abandon a direction that did not prove promising.

## The Minimum Also Moves

There is another important aspect: the MVP is not a permanent category of the product. A product’s thesis can change as new evidence emerges. An initial hypothesis may be refined, discarded, or replaced by a more sophisticated one. The questions also change. Consequently, what was sufficient to test a hypothesis at a given moment may no longer be sufficient to answer the next question.

A simple solution may be adequate for discovering whether a particular problem actually exists. Later, it may be necessary to understand whether the proposed solution is valuable enough to be adopted. Further on, it may be necessary to evaluate retention, behavior at scale, integration with other systems, or some operational aspect that was not part of the initial question.

In this process, the concept of minimum shifts. A more sophisticated thesis may require a more sophisticated solution. This does not mean that the MVP failed and became an bloated product. It may simply mean that we learned enough to ask better questions and therefore need a solution capable of answering them.

The question is the direction of this movement. Complexity should follow the evolution of the thesis, not try to anticipate it. The product can grow as knowledge about the problem, the users, and the solution itself increases. What does not make sense is to build in advance what would only make sense after we have learned.

The problem is not that the MVP grows. The problem is that it grows before we know why it needs to grow.

## When the MVP Starts Becoming a Leviathan

The most concerning sign may not be the number of features, the size of the codebase, or the number of architectural components. It is when complexity ceases to be clearly related to the purpose of the first version.

At some point, it may become difficult to explain why certain parts of the product exist, which questions they help answer, or which concrete risks justified their inclusion. Decisions begin to be made for scenarios that do not yet exist, exceptions begin shaping the main behavior, and an increasing share of the effort is consumed by the system’s own complexity.

This is the point at which it is worth returning to the question that gave rise to the MVP: what are we trying to discover?

The answer also prevents movement in the opposite direction. Not everything that can be removed should be removed. A feature may be indispensable for testing the hypothesis validly, even if it seems to increase the size of the first version. The objective was never to build the smallest possible system, but a solution proportional to what we know, what we still need to discover, and the risks that actually matter.

That is why the Leviathan is not simply a large MVP. It is an MVP that has lost control over its own complexity.

A first version does not need to be a reduced version of everything we imagine building in the future. It needs to be a deliberately limited response to the questions we have now. As we learn, the thesis may change, new questions may emerge, and the solution may need to grow. In that case, growth stops being anticipation and becomes a consequence of the knowledge acquired.

The danger begins when we do the opposite: we build first and expect the future to give us a reason for everything we built. In that scenario, what should have helped us discover the path may end up creating a path that we will find difficult to abandon.
