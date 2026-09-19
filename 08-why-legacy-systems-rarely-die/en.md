# Why Legacy Systems Rarely Die

_Legacy systems do not carry only old code. They carry decades of knowledge that companies may no longer be capable of reconstructing._

**Summary:** I argue that legacy systems rarely survive solely because of cost, risk, or technical difficulty, but because they accumulate business knowledge that the company often can no longer reconstruct. AI can accelerate this discovery by analyzing code, data, and dependencies, but it can also create a false sense of understanding by turning inferences into convincing explanations. Therefore, I advocate for modernization based on multiple sources of evidence and controlled experimentation, using AI to investigate, not simply to rewrite. Before replacing a legacy system, we need to prove that we understand everything it knows and that still matters.

---

Every experienced developer has encountered a system that seemed like it had come straight out of a museum. An application built with a technology that is no longer taught, with code that nobody would want to write today, incomplete documentation, and variable names that seem to have been chosen by someone who left the company twenty years ago. And yet, that system is in production. And not only is it in production, it is still responsible for some important part of the business.

There is a kind of involuntary respect for these systems. More experienced developers quickly learn that some parts of the architecture must be treated carefully. Not necessarily because they are technically complex, but because nobody knows exactly what will happen when someone changes them. An apparently small change can produce an effect in some process that runs overnight, break an integration that nobody remembered existed, or alter a behavior that some customer has been relying on for years.

It is common to find systems like these in COBOL, mainframes, and technologies that should have disappeared a long time ago. And when faced with them, the same question almost always arises: why doesn't anyone simply replace this?

The answer seems obvious. Because it works. Because it is expensive. Because it is critical. Because nobody wants to take responsibility for migrating a system that processes important company operations. Because, after so many years, it is connected to an unknown number of other systems, and any change can produce consequences that are difficult to predict.

All of that is true. But there is something curious about this explanation. If the problem were only cost and risk, eventually it should be possible to do the math, approve the investment, and execute the migration. In practice, there are systems that remain untouched for decades, even when the company recognizes that it would like to replace them.

## The Problem Is Not Just the Code

When a company decides to replace a relatively modern system, there is usually somewhere where the requirements are documented. There are documents, user stories, diagrams, API contracts, automated tests, records of architectural decisions, and, most importantly, people who participated in building it and can explain why certain decisions were made. Even when the documentation is not perfect, there is usually a combination of sources capable of reconstructing what the system was supposed to do. In a system that has existed for twenty or thirty years, this reality can be completely different.

Over the decades, rules were added directly to the code, exceptions were created to serve specific customers, products were launched and later discontinued, regulations changed, processes were adapted, and external systems were integrated. Developers left, teams were reorganized, vendors were replaced, and part of the context simply disappeared. The documentation aged, became incomplete, or was never updated. The code, on the other hand, kept running. And this creates a curious situation: the company may no longer know all of the requirements of its own system, but it knows that it cannot simply shut it down.

It is also important not to confuse a legacy system with old technology. A legacy system may have been running on a mainframe for forty years, but it can also be a Java, .NET, or PHP application built fifteen years ago that kept growing without a clear architecture. It can be a monolith that received dozens of features over time, a set of services created by different teams, or simply that spaghetti code written by a developer who left the company a long time ago. What characterizes a legacy system is not necessarily the language or age of the technology, but the accumulation of dependencies, decisions, and knowledge that makes it difficult to safely change or replace the system.

The hardest part emerges when we realize that some of this knowledge may no longer exist outside the system itself. Imagine a financial institution with an application responsible for calculating certain conditions of a transaction. When deciding to replace it, someone will inevitably ask the most important question: what are the rules that the new system needs to implement? In an ideal situation, the answer would be in an up-to-date specification. In many legacy systems, the answer may be much less comfortable: find it in the old code.

This may sound absurd, but it is quite plausible in systems that evolved over decades. An apparently nonsensical condition may exist to handle a contract signed twenty years ago. An apparently useless field may feed a process that runs once a month. A table may contain codes whose meaning nobody can explain anymore, but that are still consumed by other systems. An apparently redundant validation may exist because removing it already caused some problem in the past. At some point, someone made a decision, turned that decision into code, and moved on. Years later, the original decision was forgotten, but the code remained.

This is one of the most interesting aspects of legacy systems: they can preserve knowledge even when the organization that produced that knowledge has already lost it. The system continues applying a rule whose reason nobody knows how to explain, processing an exception that nobody remembers creating, and maintaining a behavior that may not appear in any documentation. The code stopped being merely an implementation of the business and became one of the few pieces of evidence of how that business actually works.

That is why there is such a huge difference between understanding the code and understanding the business. A developer may be able to perfectly explain what a particular routine does, which conditions it checks, and which data it modifies. That does not mean they know why that routine exists, whether that behavior is still necessary, or which other processes depend on it. It is possible to completely understand the implementation and still not understand the business rationale behind it.

This distinction helps explain why systems in COBOL and on mainframes continue to exist, but also why the same phenomenon appears in much more recent technologies. The cost and risk of a migration are important, but there is a third variable that is often ignored: knowledge. An old system may carry decades of operational knowledge, handle exceptions that nobody remembers anymore, contain rules that were never documented, and be connected to other systems in ways that may not even be completely mapped. Replacing it means assuming that all of this knowledge has been recovered and that the new implementation will preserve what actually matters. And perhaps it has not.

That is why some systems remain alive long after they have ceased to be a reasonable technological choice. The problem is not necessarily writing a new system. It is discovering, with sufficient confidence, what the old system actually knows.

## What If AI Doesn't Understand the Legacy Either?

It is precisely in the face of this problem that artificial intelligence seems to offer a way out. Language models can analyze large volumes of code, explain routines, identify dependencies, relate data structures, and produce documentation from systems that, until recently, would have required months of manual work to understand. For a team trying to understand millions of lines of legacy code, having a tool capable of traversing this material, finding relationships, and turning incomprehensible sections into readable explanations seems almost obvious.

And perhaps it really is one of the most interesting applications of AI in software engineering. A team can use it to build an initial representation of the system, identify critical modules, map dependencies, find patterns, compare behaviors, and raise possible business rules. Instead of putting a developer in front of thousands or millions of lines of code and expecting them to figure out how it works on their own, AI can function as a kind of guide for the investigation.

The problem is that there is a difference between finding what is in the code and discovering what the code means.

An AI can analyze a routine and explain quite precisely what it does. It can identify that a certain field is populated under certain conditions, that one function is called after another, or that a particular combination of values produces a specific result. It can even find relationships that no developer would notice by manually looking at a gigantic codebase. But there is a question that code cannot always answer: why does this need to happen?

This may be the most dangerous aspect of using AI to modernize legacy systems. The model can produce an extremely convincing explanation for a behavior that nobody understands anymore. And a convincing explanation is not necessarily a correct explanation.

Imagine a routine that, under certain circumstances, applies an apparently strange rule to a financial transaction. AI can find the condition, explain the calculation, and identify all parts of the system that depend on that result. Technically, its analysis may be perfect. But perhaps nobody knows that the rule was created twenty years ago to address a specific contractual condition. Or perhaps it exists because another system, which is also being modernized, depends on that behavior. Or perhaps it is simply the accidental consequence of an old decision that should never have survived. The code shows what happens, but not always why it happens.

This is where the idea of using AI simply to rewrite legacy systems starts to become dangerous. It is relatively easy to imagine a model transforming an old application into a modern implementation. The problem is not necessarily its ability to generate the new code. The problem is knowing whether what was generated preserves everything that should be preserved and eliminates only what can actually be eliminated; code equivalence is not necessarily business equivalence.

An AI may conclude that two parts of the system are redundant because they produce the same result in the scenarios it was able to observe. It may identify a rule that appears obsolete. It may suggest removing a table for which it cannot find explicit references. It may reconstruct a feature based on the most frequently observed behavior in the data. All of this may seem reasonable and still be wrong.

The problem becomes even greater because legacy systems often contain exactly what AI has the most difficulty recovering: missing context. The meaning of a rule may be in a meeting that took place fifteen years ago, in a contract that is not available, in a decision made by a team that no longer exists, or in an operational dependency that does not clearly appear in the code. If that information is not among the evidence provided to the model, there is no guarantee that it will be able to recover it through inference.

And there is an even more interesting consequence. AI can reduce the cost of reverse engineering so much that it can convince us that we understand a system before we actually understand it.

Before AI, the problem of analyzing millions of lines of code was so expensive that we were forced to admit our ignorance. Now we can quickly generate documentation, diagrams, explanations, and new implementations. This is extremely useful, but it also creates the risk of confusing speed of analysis with depth of understanding.

Perhaps the greatest danger is not an AI producing incorrect code. It is producing plausible, well-structured code that appears equivalent to the old system, causing everyone to believe that the problem has been solved.

That is why reconstructing a legacy system probably needs to remain an investigation that combines different sources of evidence. The code is one of them, but historical data can reveal behaviors that are not obvious in the implementation. Logs can show paths that are actually used. Existing tests can preserve rules that were never documented. Integrations can reveal hidden dependencies. Operational processes can explain behaviors that make no sense when looking only at the software. And the few people who still know the system can provide precisely the context that disappeared from all the other sources.

AI can act as an interpretation layer over all of this. It can help organize evidence, find contradictions, raise hypotheses, and point out parts of the system that require human investigation. In this scenario, perhaps its greatest value is not in telling us what the answer is, but in helping discover which questions still need to be answered.

The question, therefore, is not simply whether artificial intelligence can understand a legacy system. It probably can understand a significant part of it, and increasingly so. The truly difficult question is whether we can distinguish what the AI actually discovered from what it merely inferred.

In a new system, an incorrect inference can generate a bug. In a critical legacy system, an incorrect inference can erase a business rule that took decades to build and that nobody knew still existed.

Perhaps AI is precisely the technology that will finally allow us to kill some of our legacy systems. Or perhaps it will simply give us a much more efficient way to believe that we know how they work.

## What If We Break the System on Purpose?

There is another interesting possibility when the documentation is insufficient and the code can no longer explain all the rules by itself. Instead of trying to discover everything simply by reading the system, we can observe what happens when we deliberately alter its behavior. It may seem like a strange idea when we are talking about critical systems, but there is an important difference between breaking a system in production and experimenting with it in a controlled environment.

Imagine putting a copy of the system in a pre-production environment sufficiently close to reality and starting to ask questions through experiments. What happens if a certain field receives a different value? What changes if a validation is removed? Which processes stop working when a particular rule is changed? Which integrations begin to behave differently? Which results change when we modify an apparently irrelevant condition? Instead of simply asking the code what its rules are, we can observe the consequences of changing those rules.

This can reveal dependencies that do not appear clearly in the implementation. A particular validation may seem unnecessary until it is removed and causes a change in another process. A field may seem unimportant until it receives a different value and changes the behavior of a completely distant routine. An apparently isolated rule may reveal, through the effects caused by changing it, that some other process depends on it.

This approach is particularly interesting because it turns reverse engineering into an experimental process. Instead of trying to build a complete representation of the system before beginning to make changes, we can formulate hypotheses, change one variable at a time, observe the results, and update our understanding based on the evidence. The system stops being merely something we need to read and becomes something we can interrogate.

Artificial intelligence could make this process even more interesting. Instead of simply asking an AI to explain millions of lines of code, we could use it to formulate hypotheses about the system's behavior, suggest experiments, identify which components need to be observed, and compare the results obtained with the expected behavior. The model could help build a kind of causal map of the system from the evidence collected during the experiments.

This does not eliminate the knowledge problem, but it changes the nature of the investigation. If we do not know why a particular rule exists, perhaps we can discover what depends on it. If we do not know whether a particular condition is still necessary, perhaps we can remove it in a controlled environment and observe what happens. If we do not know the meaning of a particular behavior, perhaps it is possible to find a testable hypothesis.

There is, however, an important condition: experimenting does not mean simply changing the system at will. In complex systems, effects can be indirect and appear long after the original change. A pre-production environment may also fail to reproduce all the conditions that exist in production, especially when there are external integrations, large volumes of data, or behaviors that only appear under certain circumstances. Therefore, the value of these experiments depends on the quality of the environment, the data, and the ability to observe the effects produced.

Even so, there is a powerful idea behind this. Perhaps understanding a legacy system is not just a matter of reading its code or asking an AI to explain it. Perhaps it is also a matter of asking the system questions and observing its answers.

After decades of operating without anyone fully knowing how, perhaps the best way to discover what a system actually knows is, in a safe and controlled environment, to start doing what every senior developer normally avoids doing in production: break it on purpose.

## Before Replacing It, We Need to Understand It

There is a certain irony in the history of legacy systems. For decades, we have tried to replace them because they were old, expensive to maintain, and built on technologies that are no longer part of the present. Now we have tools capable of analyzing large volumes of code, reconstructing dependencies, producing documentation, and accelerating reverse engineering at a scale that would previously have been economically unfeasible. Artificial intelligence can completely change the economics of migrations, but perhaps it is only part of a larger change in the way we understand these systems.

The code can be analyzed. The data can be investigated. Behaviors can be observed. Hypotheses can be formulated and tested. Systems can be placed in controlled environments and deliberately modified to reveal dependencies that have remained hidden for decades. Artificial intelligence can help organize all of this, find patterns, suggest hypotheses, and connect pieces of evidence that would be difficult to relate manually. For the first time, perhaps we have enough tools to turn legacy modernization into a systematic discovery process.

But there is an important difference between discovering how a system works and being certain that we understand everything that matters.

A business rule may be explicit in the code, hidden in the data, preserved in an apparently strange behavior, or simply exist in the memory of someone who has worked at the company for decades. We can find dozens of pieces of evidence about how a system works and still not know whether we have found all the rules that need to be preserved. This may be the hardest limit to overcome, because there is no tool capable of proving the existence of something we can no longer observe.

Therefore, perhaps the most important question before replacing a legacy system is not how much the migration costs, which technology will be used, or how long it will take to rewrite the code. The first question should be much simpler: what exactly does this system know that we need to continue knowing?

If we can answer that question with confidence, the technology for replacing it will probably be the least of our problems. If we cannot, perhaps we are not yet looking at a system that is ready to be shut down, but at a piece of the company's knowledge that is still trapped inside it.

And perhaps that is the real reason why that system that seems to have come straight out of a museum remains in production. Not because nobody has the courage to replace it, but because, after decades, nobody has managed to prove that they know everything it knows.
