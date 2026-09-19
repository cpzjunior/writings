# What History’s Worst Types of Decisions Teach Us About Decision Architecture

_What the mistakes of empires, governments, and companies reveal about strategy, management, and decision-making_

**Summary:** I like history because it allows us to observe how decisions, resources, constraints, and incentives combine over time. In this text, I use some historical and business cases to understand why certain decisions placed organizations in positions that were difficult to reverse, whether because of an error in how the problem was viewed, the creation of dependencies, the loss of options, or the difficulty of changing direction in time. What interests me is not judging these choices based on the outcome we know today, but understanding what was behind them when they were made and what consequences were embedded in each path. This is the perspective I want to explore when thinking about decision architecture.

---

I like history. I am a fan of games such as Europa Universalis, Victoria, and Civilization, and I follow geopolitics for the same reason I like these games: the possibility of observing how decisions, resources, constraints, and incentives combine to produce outcomes over time. This perspective also lies behind a text I previously wrote, “[Solution architecture applied to financial markets, governments, supply chains, and geopolitics](https://cpzjunior.substack.com/p/arquitetura-de-solucoes-aplicada)”. In it, I used solution architecture as a lens for understanding complex systems. But I realized that one layer was missing: the decisions that build these systems. That is what I want to explore here. Not as a collection of historical failures, but as an analysis of different types of decisions that can place organizations in positions that are difficult to reverse.

And there is an important difference. Some of the companies that appear in this text went bankrupt. Others did not. Some choices produced catastrophic consequences. Others merely placed an organization in a worse position than the one it could have occupied. The final outcome, therefore, is not the only criterion. What interests me is the quality of the choice given the information, constraints, incentives, and alternatives available at that moment.

The parallel between the historical and business cases also does not lie in the events themselves. A war is not equivalent to managing a company, just as an empire is not a corporation. What we can compare is the structure of the choice: how a problem was defined, which objectives guided the action, what resources were available, and which alternatives seemed viable at that moment.

This also requires care with hindsight bias. A choice that produced a bad outcome was not necessarily a bad choice, just as a choice that worked was not necessarily a good decision. The challenge is to return to the moment of the choice and try to understand what made sense, what was ignored, and which assumptions supported that path.

The selection of cases is, naturally, subjective. It would be possible to choose dozens of other examples, perhaps more well-known or even more extreme. The seven cases in this text were chosen because they allow us to observe different mechanisms and, above all, because they help build the argument about decision architecture. The goal is not to establish a ranking of the worst decisions in history, but to use some particularly illustrative cases to understand how different types of decisions can alter an organization’s ability to respond to what comes next.

It is from this perspective that it is worth looking at some of the worst types of decisions in history.

## Crassus × New Coke: the modeling error

In 53 BC, Marcus Licinius Crassus faced the Parthians at Carrhae, in Mesopotamia. Rome possessed one of the most powerful military forces in the known world, but that did not prevent the campaign from ending in a catastrophic defeat.

It is tempting to explain the episode through Crassus’s arrogance or the superiority of Parthian cavalry. But that means looking at the decision after we already know the outcome. To understand the problem, it is more interesting to take a step back and ask how Crassus viewed the situation before the battle.

Rome had a real military advantage. Its legions were experienced, disciplined, and capable of defeating very powerful adversaries. This experience created a reasonable expectation: against a new enemy, the superiority of the legions would remain the main factor in the campaign. The problem was that this conclusion treated Roman military capability as a property almost independent of the context in which it would be employed.

At Carrhae, context was a central part of the problem. The Parthians could exploit cavalry mobility, maintain distance from Roman troops, and use mounted archers to attack without giving the Roman army an opportunity to employ its main advantages. The terrain and supply conditions also increased the weight of these differences. The question, therefore, was not simply who possessed the more powerful army, but whether the way Rome gained its military advantage remained valid in that environment.

Crassus was not making a decision with zero information. He had proven military capability and enough experience to trust it. The problem lay in the operational premise: the idea that a capability that worked extremely well in certain contexts would continue to provide an advantage when the conditions of the problem changed.

This is exactly the kind of error that makes New Coke an interesting case. Coca-Cola also did not make its decision blindly. The company conducted extensive research and used blind taste tests in which many consumers showed a preference for the new formula. There was, therefore, concrete evidence that the change could work.

But there was a difference between what the test measured and what the company needed to decide. The test essentially answered a question about taste preference in a controlled situation. Coca-Cola’s decision, however, was much larger: replacing the original product, a brand with decades of history, consumption habits, identity, and strong emotional associations.

The company turned evidence about one dimension of the product into a conclusion about the product as a whole. The implicit premise was something close to: if consumers prefer the new flavor in a test, then the new formula will be a better substitute for the original Coca-Cola. The data could be correct. The leap from the data to the decision was the problematic part.

This is where the parallel with Crassus becomes clearer. In both cases, there was legitimate evidence supporting confidence in the decision. Rome had an extremely effective military force. Coca-Cola had tests indicating a preference for the new formula. The problem was treating that evidence as sufficient to represent the system that actually needed to be understood.

Crassus needed to know whether the conditions that made the legions an advantage were still present in that theater of operations. Coca-Cola needed to know whether taste preference justified replacing a product whose value proposition included much more than taste. In both cases, one relevant variable was treated as a sufficient representation of a broader problem.

This type of error is particularly dangerous because it does not necessarily present itself as a lack of information. Often the opposite happens. There are enough data, experts, analyses, models, and precedents to give the decision an appearance of rigor. What may be wrong is the relationship between that information and the representation of the problem one intends to solve.

In solution architecture, we know this risk. A solution can be technically excellent and still solve the wrong problem. We can choose an appropriate technology, design a robust integration, and automate a process efficiently, but start from an incorrect definition of the need. In that case, improving the solution does not correct the error. It merely makes the execution of a bad premise more efficient.

Decision architecture begins before choosing between alternatives. It begins by understanding what problem we are actually trying to solve, how we are representing that problem, which assumptions support that representation, and which conditions need to remain true for the decision to continue making sense.

## Napoleon in Russia × Lehman Brothers: excessive dependency

In 1812, Napoleon invaded Russia at the head of a gigantic force. Its scale was, in itself, an extraordinary demonstration of military capability. A larger army meant more troops, more cavalry, more artillery, and greater capacity to sustain operations across different fronts.

But a capability of this size does not exist in isolation. For it to be employed, it needed a structure capable of sustaining it.

As the army advanced deeper into Russia, distances increased and, with them, the needs for supply, transportation, communication, and coordination. The force had to feed a huge contingent, move equipment, maintain supply lines, and continue operating farther and farther from its bases. Each of these functions depended on the others.

This changes the nature of the problem. It is not enough to ask how much capacity a solution has. We need to understand how many conditions that capacity depends on in order to remain available.

The Russian campaign exposed this relationship. Napoleon’s force did not cease to be powerful simply because it advanced. The problem was that its combat power depended on a logistical structure that was increasingly difficult to maintain. A failure in any part of that structure could reduce the capability of the entire system.

Lehman Brothers presented a similar mechanism in the financial system. During the years preceding the 2008 crisis, the bank had built an operation of enormous scale, with a strong presence in capital markets and significant exposure to the real estate market. Leverage amplified returns on capital, while expanding operations increased its ability to generate revenue.

None of these characteristics was necessarily problematic in isolation. Scale can generate efficiency and allow an institution to operate in markets that would be unviable at smaller dimensions. Leverage can also be rational when assets are liquid, risks are understood, and financing conditions remain favorable.

The problem arises when capacity begins to depend on an extensive chain of conditions functioning simultaneously.

An institution such as Lehman depended on financing, liquidity, counterparties, active markets, asset valuations, and confidence to keep its operations running. While these conditions remained favorable, the structure could appear efficient. When some of them began to deteriorate, the interdependencies caused problems in one part of the system to affect others.

This is where the parallel with Napoleon becomes clearer. It is not about saying that an army and a bank are the same thing. The common mechanism lies in structural dependency.

Napoleon needed more than soldiers. He needed food, transportation, communication, horses, ammunition, and supply lines to work together. Lehman needed more than capital. It needed financing, liquidity, counterparties, valuation, markets, and confidence to remain available simultaneously.

In both cases, the system’s final capacity was much greater than the capacity of any of its components in isolation. But that also meant that the disruption of a critical condition could compromise a significant portion of the result produced by the whole.

This is an important distinction in solution architecture. When we add components, integrations, suppliers, markets, or layers to a solution, we increase its capacity, but we also increase the number of relationships that need to be maintained. Each new dependency creates another condition for the system to continue functioning as designed.

Therefore, the architectural question should not be only “how much more capacity can we add?” We also need to ask “how many conditions does this capacity depend on?” and “which of them are critical for the system to continue functioning?”

A solution can be extremely powerful and still have such an extensive dependency structure that small disruptions produce disproportionate effects.

The risk lies not only in building something complex. It lies in building a capability whose operation depends on too many conditions remaining true at the same time.

## Russian Alaska × IBM: the loss of optionality

In 1867, Russia sold Alaska to the United States for US$7.2 million. In retrospect, the decision seems extraordinarily cheap given the economic and strategic value the territory would later acquire. But evaluating it solely based on what we know today would ignore the conditions under which the decision was made.

Alaska was remote, expensive to administer, and difficult to defend. After the Crimean War, there was also a concrete concern: in a potential conflict with the United Kingdom, Russia could lose the territory without being able to defend it adequately and without receiving any compensation. Under these assumptions, selling the territory and turning a difficult position to sustain into immediate cash was a defensible decision.

The problem is that a decision can be rational given the present and still reveal a cost when the future materializes. By selling Alaska, Russia resolved an immediate issue, but also eliminated a future possibility. There was no guarantee that this possibility would have great value. The territory could have remained expensive, remote, and of little relevance for decades. Keeping the position would also have had a cost. The question was not simply choosing between a right and a wrong decision, but deciding how much it was worth preserving an option whose future return was uncertain.

The value of that option only became evident later, with the discovery of natural resources and the transformation of Alaska into an economically and geopolitically relevant position. This does not make the sale irrational in 1867. It shows how decisions made to solve present problems can eliminate possibilities that only acquire value later.

IBM’s history presents a similar dynamic, although in a different type of system. When it entered the personal computer market, IBM had a concrete problem: it needed to put a competitive product on the market quickly in a market that was taking shape. To do so, it adopted a relatively open architecture and used third-party components. The decision worked. The IBM PC was an enormous success and helped establish a standard that would be widely adopted by the industry.

But some choices that made this initial success possible also altered IBM’s strategic options for the future. Hiring Microsoft to provide the operating system is a well-known example. IBM needed a fast, competitive solution, while Microsoft structured a model that allowed it to license the system to other manufacturers. At the same time, the use of third-party components and the relatively open architecture of the PC contributed to the formation of an ecosystem of compatible machines.

None of this means that IBM “lost the PC.” It had achieved exactly what it needed at that first moment: putting a competitive product on the market and turning it into a commercial success. The problem appeared later. The ecosystem that grew around the IBM PC allowed other companies to accumulate strategic positions in fundamental layers of the architecture. Microsoft gained scale in the operating system. Intel gained scale in processors. Computer manufacturers could produce compatible machines.

IBM had solved the present problem, but some of the choices made to solve it allowed other actors to capture value and build positions that would later be difficult to recover.

This is where the parallel with Alaska becomes clearer. In both cases, the decision was made in response to a concrete need and had its own logic at that moment. Russia needed to deal with the costs and risks of maintaining a remote territory. IBM needed to enter a nascent market quickly. In both, the choice produced immediate benefits.

What the future revealed was the value of some possibilities that had been sacrificed in the process. This is an important dimension of decision architecture. When choosing an alternative, we are not only choosing what we want to obtain. We are also altering the set of alternatives that will be available later.

The challenge is that preserving options also has a cost. Maintaining a territorial position, a technology, an internal capability, or control over a particular layer of an architecture requires resources. Therefore, it makes no sense to treat preserving options as an absolute objective. Some options are too expensive to maintain, and others do not have enough strategic value to justify that cost.

The question is recognizing that this trade-off exists. A decision oriented exclusively toward the current problem can appear efficient because it turns uncertainty into an immediate result. But in doing so, it may consume an option whose value we cannot yet see.

This is the question that connects Alaska to IBM: not only “what does this decision solve now?”, but also “which future possibilities does this decision make harder to recover?”

The future cannot be predicted precisely. But we can recognize that some decisions consume optionality. And perhaps we only realize the value of what we closed off when it is already impossible to reopen.

## Italy in World War II × Yahoo: the prioritization error

Italy entered World War II with ambitions greater than its ability to sustain them. Its industrial, logistical, fuel, and transportation limitations required choices. There was not enough capacity to turn all political and military objectives into simultaneous campaigns. It was necessary to identify which positions could produce the greatest strategic impact and concentrate available resources on them.

The Mediterranean was one such position. Malta, Gibraltar, and the Suez Canal affected supply routes, troop movements, and Britain’s ability to operate in the region. Controlling these points would not guarantee an Italian victory, but it could alter the conditions of several other operations. A concentration strategy could therefore seek first the positions capable of changing the regional balance.

Italy followed a different path. In 1940, it opened a campaign in North Africa and advanced from Libya toward Egypt. The offensive was eventually halted and suffered a British counterattack that destroyed much of the Italian force. To prevent the collapse of the Italian position, Germany had to send troops and equipment to the region, creating an additional dependency.

That same year, Italy opened another front by invading Greece. The campaign, which was supposed to be quick, encountered resistance and dragged on. Germany eventually intervened again in the Balkans. Resources that could have been concentrated elsewhere became necessary to sustain operations that had created their own logistical demands.

What stands out in these movements is not that Italy chose objectives with no value whatsoever. North Africa, Greece, and the Mediterranean had strategic importance. The question was the amount of capacity required to pursue each objective and what became impossible when that capacity was committed.

This is the central point of prioritization: resources employed on one front are not available for another. A military operation, like a business initiative, does not consume only the initial investment. It creates sustaining costs, requires execution capacity, and can generate new demands as it advances.

Yahoo faced a similar choice in another context. In the early 2000s, the company held one of the strongest positions on the internet. It had an audience, portal, email, advertising, distribution, and a significant presence in search. And it made decisions that could have strengthened precisely that last position. In 2002, it acquired Inktomi to strengthen its search technology. In 2003, it acquired Overture, strengthening its position in search-related advertising.

There was, therefore, a strategic position that could have been deepened. Yahoo could have concentrated capital, talent, and attention on search and advertising and attempted to turn that combination into an increasingly difficult-to-displace advantage.

But that was not the only direction it chose. Yahoo continued expanding its product portfolio and making acquisitions in different areas. It bought Flickr, a platform with enormous relevance in digital photography. It invested in content, media, communications, and mobile. In 2013, it acquired Tumblr for about US$1.1 billion, betting that its enormous audience could become a new source of growth and advertising.

These decisions were not necessarily irrational in isolation. Tumblr had a huge community. Flickr had a relevant position in photography. Content and mobile were important markets. The point is different: each of these bets competed for the same limited pool of capital, talent, and executive attention.

Meanwhile, Google concentrated its resources on a position that was becoming increasingly valuable: search and advertising. This concentration produced cumulative advantages. More users generated more queries and data; more data and scale improved advertising; more revenue allowed further investments in product and infrastructure.

Yahoo had an initial position strong enough to compete in this market. But the company did not turn that position into a comparable cumulative advantage. In 2009, it ultimately transferred its search infrastructure to Microsoft, retaining the user experience and advertiser relationships. The decision had financial and operational justifications, but it also meant reducing control over a core technological capability precisely when Google was consolidating its leadership.

The contrast is important. Yahoo was not choosing between an opportunity and no opportunity. It had too many opportunities. The challenge was deciding which one deserved enough concentration of resources to become decisive.

An acquisition can be viewed, in this sense, as a territorial conquest. The company uses capital to occupy a position, but then needs to invest in integration, technology, people, and operations to maintain it. If that position does not reinforce a broader strategic advantage, it can consume resources without proportionally improving the organization’s position.

The same applies to a new military front. Conquering territory is not the same as creating an advantage. It is necessary to assess how much it costs to reach it, how much it costs to sustain it, and whether its importance justifies taking resources away from other positions.

This is where the parallel between Italy and Yahoo becomes clearer. Both had relevant objectives and limited resources. The question was not identifying all possible opportunities, but determining which ones deserved enough concentration to alter the balance of the system.

Priority, therefore, is not a list of important things. It is a decision about where to place capacity and, consequently, where to accept not placing it.

Strategy does not consist of pursuing every opportunity. It consists of choosing the positions that deserve enough resources to become decisive.

## Japan at Pearl Harbor × Blockbuster: the cost of time

In December 1941, Japan attacked Pearl Harbor with the objective of reducing the capability of the American fleet in the Pacific and creating room for its expansion in Southeast Asia. As a military operation, the attack was significant. As a strategic decision, however, it carried a structural problem: Japan was initiating a war against a power with much greater industrial capacity.

This does not make the decision simply irrational. Japan faced important economic and strategic constraints, and the alternatives also involved risks. The question was to assess not only the immediate outcome, but the type of conflict that choice made likely.

The attack created an initial advantage that needed to be quickly converted into a new strategic reality. The longer the war continued, the greater America’s ability to mobilize resources would become. Pearl Harbor, therefore, did not solve the central problem. It created a window of opportunity that Japan would need to exploit before the balance of forces changed. The question was not only what could be destroyed at that moment, but how much time the advantage obtained would actually buy.

Blockbuster faced a different but comparable dynamic. The company held a dominant position in movie rentals, a strong brand, and a huge network of stores. Maintaining the traditional model still generated revenue and therefore was not irrational in the short term. The problem was that the market was already showing signs of structural change.

Netflix’s trajectory illustrates this change. The company began with DVD rentals by mail and a subscription model that eliminated some of the limitations of traditional video rental stores. It later moved into streaming and helped transform consumer behavior.

Blockbuster did react. It created a subscription service and later invested in digital initiatives. But the transformation competed with a physical business that was still large and profitable. The question became how much capital, talent, and attention should be shifted away from an operation that worked to finance an alternative whose return was still uncertain.

While Blockbuster protected the profitability of its existing model, Netflix accumulated experience, customers, and technological capabilities for the emerging market.

The common point between the two cases lies in the decision horizon. In Japan, the immediate military advantage received more weight than the risk of a prolonged war. At Blockbuster, the profitability of the existing business made it difficult to assign sufficient weight to the speed of market transformation.

In both cases, there were alternatives and none offered a guarantee of success. The problem lay in how they were compared. The criterion used favored what was still working, while underestimating the cost of waiting.

The problem, therefore, was not merely choosing between alternatives. It was recognizing that the value of each alternative changed over time. A position that seems sufficient today may become much harder to sustain tomorrow, while an opportunity that seems uncertain may lose value if it is not pursued while there is still room to build it.

A decision architecture needs to consider not only the return of a choice, but also the speed at which the conditions supporting that return are changing.

Time, in this sense, is also a strategic resource. A decision can consume time, buy time, or turn a window of opportunity into an obligation to act later.

Sometimes, the decision that seems safest today is precisely the one that leaves the least time to build the next position.

## Operation Barbarossa × WeWork: dependence on scale

Operation Barbarossa began with a bet on scale and speed. The German offensive against the Soviet Union assumed that a rapid campaign would allow it to destroy much of Soviet capacity before the conflict turned into a prolonged war.

The logistical problem was not unknown. Napoleon’s campaign against Russia, little more than a century earlier, had already demonstrated how distance, supply, transportation, and terrain conditions could compromise a much larger military force. German planners knew this precedent and understood that a campaign deep inside the Soviet Union would create extraordinary logistical challenges.

The response was not to eliminate this dependency, but to bet that speed and scale would overcome it. The larger the force deployed and the faster it advanced, the greater the possibility of destroying Soviet capacity before sustainment problems became decisive. The scale of the operation was therefore itself part of the bet to solve a limitation that was already known.

When that premise did not materialize, the expansion itself began to create additional problems. A force that advances needs to be supplied. The greater the distance, the greater the needs for transportation, fuel, ammunition, and maintenance. The larger the occupied territory, the greater the structure required to sustain it. An operation designed to advance rapidly faces a different logic when it needs to remain in the territory it has conquered.

The problem was not simply having advanced too far. Each stage of expansion increased the resources required to sustain the next one. The bet on scale created a growing dependency on the expansion itself continuing to work.

WeWork helps illustrate the same mechanism in a business organization. The company depended on scale to sustain an operating structure whose costs grew along with the expansion itself. More spaces meant greater presence and more potential customers, but also more contracts, fixed costs, and capital required to maintain the operation.

This created a growing dependency: raise resources to expand, expand to increase revenue, and increase revenue to sustain the structure that had been built.

The problem appears when this dynamic needs to continue indefinitely. Resources are finite. There is a limit to available capital, the market’s capacity to absorb growth, and the growth that can be converted into sufficient revenue to finance the existing structure.

When the cost of expansion grows along with expansion itself, growth ceases to be a way to capture an opportunity and becomes a condition for maintaining what has already been built.

That is where the model reveals its fragility. While available resources grow faster than the obligations created, the structure can appear sustainable. When that relationship reverses, accumulated expansion ceases to produce enough advantage to compensate for the cost it created.

The same logic appears in projects and products. An architecture can be sized for a future scale that never arrives. An operation can assume fixed costs based on demand that does not yet exist. A company can build a structure whose viability depends on a volume that needs to be reached for the structure itself to make sense.

The problem is not growth. The problem is when the next stage ceases to be an opportunity and becomes a necessity. At that point, the organization stops using growth to build capacity and starts using future resources to sustain past decisions.

The risk lies in building a structure whose sustainability depends precisely on the condition that it itself needs to keep expanding to achieve.

## Ming Dynasty × Google: lost opportunities

This case breaks the chronological order somewhat because it deals with a different type of decision. In the previous cases, we analyzed choices that placed organizations on difficult-to-reverse trajectories. Here, the problem lies in failing to develop a capability because its immediate value seems small, without considering the cost of rebuilding it if conditions change.

At the beginning of the 15th century, the maritime expeditions associated with Zheng He demonstrated extraordinary naval and logistical capabilities in Ming China. Large fleets crossed the Indian Ocean, reached distant regions, and projected diplomatic and commercial power.

These expeditions were discontinued in the 1430s amid changing priorities, political disputes, fiscal concerns, and issues related to territorial defense. The history is more complex than the narrative that China simply “stopped exploring” and therefore fell behind. Ming maritime activity continued in other forms, and there is no historical consensus that the end of the major expeditions was a single decision that determined China’s future.

Still, the episode raises an important question: what is the value of maintaining a capability when its immediate benefit appears small compared with the cost required?

This question frequently appears in technology companies. Google has built a veritable graveyard of innovations throughout its history, with products and projects that were launched, tested, and later discontinued. This is not, in itself, a sign of poor management. An organization needs to abandon initiatives that do not justify the capital, talent, and attention they consume.

Google Glass is an interesting example. The company bet early on a new category of wearable computing, but the product encountered problems involving adoption, price, privacy, and fit with consumer behavior. The enterprise-focused version continued for several more years, until Glass Enterprise Edition was also discontinued in 2023.

The end of Glass as a product does not mean that the technological bet was necessarily misguided. Years later, Ray-Ban Meta showed that consumers could adopt a different form of wearable computing based on camera, audio, and artificial intelligence, integrated into a familiar product.

The distinction is important. An initiative can fail because the market is not yet ready, because the business model is inadequate, or because the technology depends on conditions that do not yet exist. Ending the product can be rational. The risk lies in also abandoning the knowledge, capabilities, and infrastructure that would allow another attempt when those conditions are different.

The same reasoning helps us look at Ming China. It is not possible to claim that the discontinuation of the major expeditions alone determined China’s maritime future, nor that China would necessarily have dominated Indian Ocean trade had it maintained those expeditions. The point is that reducing an activity can also reduce the capacity to explore certain opportunities. Rebuilding a capability many years later can be much more expensive than maintaining it at limited scale.

This creates a difficult trade-off. People need to be allocated, infrastructure needs to be maintained, and managerial attention is limited. Trying to preserve every possibility would be unfeasible.

The architectural question, therefore, is not “should we maintain this initiative?” It is “what will we no longer be able to do if we end this initiative?” and “how much will it cost to recover this capability later?”

Current return remains important, but it is not the only criterion. We also need to consider the time required to rebuild a capability and the possibility that, when the opportunity emerges, other organizations will already have occupied that space.

We cannot know which future opportunities will actually exist. We can, however, recognize when a decision makes it much harder to take advantage of them.

Sometimes, not deciding is also a decision. And the cost may only appear when an opportunity arises and we discover that we are no longer prepared to pursue it.

## The importance of decision architecture

The seven cases show different types of decisions that can compromise the future: modeling error, excessive dependency, loss of optionality, cost of time, prioritization error, dependence on scale, and loss of opportunities. The common point is that decisions do not merely produce outcomes. They alter the conditions under which subsequent decisions will be made.

This is what brings strategy, project management, and solution architecture together. A technological choice creates dependencies. An investment commits resources. An expansion creates obligations. A supplier decision can restrict future alternatives. A divestment can eliminate an opportunity that we do not yet know whether we will need to pursue.

We do not need to predict the future to make good decisions. We need to understand the assumptions, dependencies, trade-offs, and consequences that each choice creates for subsequent decisions.

Many of the decisions analyzed here seemed reasonable when they were made. The problem is that their authors were not merely choosing a response to the present. They were defining the conditions of the next decision.

Deciding means beginning to build the next problem that the organization will have to solve.
