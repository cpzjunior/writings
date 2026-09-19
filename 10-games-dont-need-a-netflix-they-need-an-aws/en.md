# Games don't need a Netflix, they need an AWS

_What if the fundamental mistake of game subscription services is treating the game catalog as the product, when the real product the user wants to rent is computing capacity?_

**Summary:** I argue that cloud gaming is being approached through the wrong model: instead of turning games into a Netflix, we should separate the game from the machine that runs it. The user does not need hundreds of titles, but access to the computing capacity necessary to play what they have chosen, without having to buy hardware for several years. Just as the cloud transformed computing into elastic infrastructure, games could be run on machines rented on demand, while the purchase and distribution of games remain independent. The future, therefore, may lie less in a Netflix for games and more in an AWS for games.

---

I bought an Xbox Series S with a fairly simple idea in mind: I wanted to play my favorite games without having to build a gaming PC. Game Pass seemed like the perfect solution. One subscription, a huge library, and a relatively inexpensive console. In practice, I discovered something curious: the catalog is enormous, but very few games actually interest me. There are hundreds of titles available, but I still essentially want to play the same genres and a few specific franchises. The size of the catalog, which should be the main justification for the subscription, ends up having little meaning when the games I actually want to play represent a tiny fraction of it.

The problem became even more evident when I started thinking about the hardware. The Series S is still a capable console, but I can already see the path it is following. Recent games demand more and more from the hardware, and what is today a perfectly adequate machine gradually becomes a machine limited by the generation it was designed for. My PC does not solve the problem either. It is already a few years old and, although it remains perfectly useful for many things and runs games that are still excellent, it no longer has enough capacity to comfortably keep up with the most demanding releases. I therefore have two different problems: a game library much larger than what I actually want to play and a set of hardware that needs to be replaced periodically to keep up with the evolution of games.

That was when I started questioning whether we are looking at the problem in the right way. I do not want hundreds of games. I want to play a few specific games. I also do not necessarily want to buy a new machine every generation. I want access to the computing capacity necessary to run the game I have decided to play at that moment. These two needs seem quite different from what subscription services and the traditional hardware market are trying to sell.

The question that occurred to me was simple: what if the fundamental mistake of game subscription services is treating the game catalog as the product, when the real product the user wants to rent is computing capacity?

## The problem with turning games into Netflix

Perhaps the problem lies precisely in the attempt to turn video games into an entertainment category similar to movies and TV shows. The analogy works in some respects, but fails at one fundamental point: a game is not just content. It is also an application that needs to be executed.

When I watch a movie, the heavy computational work has already been done during production. The service needs to store and stream the video efficiently. When I play a modern title in the cloud, the situation is completely different. The server needs to run the game in real time. Every controller movement changes the state of the game, the CPU and GPU process that information, a new image is rendered, it is encoded and sent over the network to my screen, while my inputs make the journey in the opposite direction.

This completely changes the nature of the product. In traditional streaming, content is the main product and the infrastructure exists to deliver it. In cloud gaming, content is still necessary, but computing capacity becomes an essential part of what is being sold. When someone uses cloud gaming because they do not own a PC capable of running a particular game, what that person is effectively trying to buy is temporary access to a sufficiently powerful machine.

This also exposes a limitation of the catalog-based model. There is an assumption that the more games available, the greater the value of the subscription. But that relationship is not necessarily true for video games. A player may only be interested in a few specific genres and franchises. Hundreds of additional titles can represent an enormous amount of available content and, at the same time, almost no additional value for that user.

The difference compared with movies and TV shows is important. When I subscribe to a video service, I can watch a crime series today, a comedy tomorrow, a documentary on the weekend, and perhaps a science fiction movie afterward. The cost of trying something new is low. In games, the investment is much greater. Many titles require dozens of hours and an adaptation to their own mechanics, systems, controls, and progression. The player is not simply consuming content. They are learning to operate an interactive system.

It is therefore possible to have an enormous catalog and still offer little value to a particular user. The number of games available is an objective metric, but not necessarily a good metric of utility.

And this raises a rather strange question about the current model: if I already know which game I want to play, why do I need to subscribe to an entire catalog to access the machine capable of running it?

If I bought Elden Ring, for example, and want to play it on a computer that does not have an adequate GPU, my problem is not a lack of access to games. I already own the game. The problem is a lack of computing capacity.

Perhaps the product cloud gaming should sell is precisely that capacity.

## AWS and GPU as a service

Cloud computing found a solution to a very similar problem. A company that needs computing capacity does not need to buy a server for the next five years. It can rent infrastructure according to its needs. If it needs more processing power, it provisions a larger machine. If it needs less, it reduces capacity. If it needs nothing, it shuts down the resources.

The major innovation was not simply putting servers in a datacenter and accessing them over the internet. It was turning computing capacity into an elastic resource that can be provisioned, scaled, and consumed according to demand.

The same principle could be applied to games. Instead of buying a GPU for the next few years, the player could rent computing capacity when needed. Instead of choosing a machine that needs to remain sufficient throughout an entire generation, they could choose the configuration required for the game they intend to run at that moment.

A service like this could offer different classes of machines. A cheaper configuration could handle less demanding games or players willing to sacrifice graphical quality. An intermediate configuration could provide a 1080p or 1440p experience. A more powerful machine could serve users who want maximum graphics, high frame rates, or ray tracing. The user would choose capacity according to what they intend to play and how much they are willing to spend.

This possibility completely changes the relationship between player and hardware. Today, when I buy a GPU, I have to try to predict what my future needs will be. If I buy a very powerful card, I pay for capacity I may not use for much of the time. If I buy a cheaper card, I risk discovering a few years later that it is no longer sufficient for the games I want to play. In both cases, I am making an upfront bet.

In the cloud, that decision is no longer permanent. Imagine that, instead of a traditional subscription, I could simply buy computing credits. I put R$ 100 into my account and use that balance as I play. A basic machine might consume a few credits per hour, while a machine equipped with a cutting-edge GPU consumes much more. The cost of the session then directly reflects the computing capacity I am using.

If I want to play a relatively lightweight title for twenty hours, I can choose a simpler machine and make my credits last a long time. If I want to spend five hours on an extremely demanding game, I can choose a premium machine and accept higher consumption. If I do not play for an entire month, there is no reason to consume credits.

The model could still have recurring plans, but the subscription would no longer primarily represent access to a catalog. It could function as a computing wallet, with credits accumulated and consumed according to usage. The difference seems small, but economically it is enormous: I start paying for what I am actually using, rather than for a collection of games I may never open.

This also creates a much more transparent relationship between price and experience. If I want a better image, higher resolution, or a more powerful GPU, I pay more. If I am willing to accept a simpler machine, I pay less. The service does not need to decide in advance which configuration all users should receive.

The fundamental difference is that the unit of value stops being the game available and becomes the computing capacity consumed. The game remains necessary, but the infrastructure stops being an invisible detail and becomes the service itself.

## Hardware stops being a bet

There is another, deeper consequence. Local hardware requires consumers to anticipate the future.

When I buy a console or GPU, I am buying a certain amount of computing capacity that I expect to be sufficient for several years. I do not know what the requirements of future games will be, but I need to make a decision today.

This is particularly relevant when we consider the speed at which graphics technology evolves. A machine that seems powerful at the launch of a generation may continue working perfectly for many years, but gradually begins to require compromises: lowering the resolution, reducing graphical quality, giving up ray tracing, or accepting lower frame rates.

My Series S does not stop working when a new generation of games appears. My PC does not suddenly become a useless machine either. What happens is more subtle: they stop providing the computing capacity necessary to run certain games the way I would like.

In the cloud gaming model, this obsolescence can be shifted from the consumer to the provider. When a new generation of GPUs arrives, it can be added to the datacenter. When certain hardware ages, it can remain available as a cheaper option for less demanding games. The user does not need to buy a new machine to keep up with the evolution of the infrastructure.

This does not mean that obsolescence disappears. It simply stops being a problem that each consumer has to solve individually and becomes an infrastructure problem that the provider manages at scale.

Instead of asking which hardware I need to buy today to keep playing for the next five years, I can simply ask what capacity I need to play the title I want to play today.

That is an important conceptual shift. The consumer stops making a bet on the future of technology and starts consuming the computing capacity available in the present.

## The game and the machine do not have to be the same product

The traditional model combined two things because that was necessary. The console or PC provided the computing capacity and the game ran locally. The arrival of the cloud makes it possible to separate these two layers.

I can buy a game independently of the machine that will run it. I can have my library on a digital platform and use local hardware when it is sufficient. When it is not, I can use remote infrastructure. The game remains my entertainment product, while the machine becomes a separate service.

This means we do not necessarily need a “Netflix of games” to make cloud gaming work. The game catalog can remain a product of the platforms themselves. Sony, Microsoft, and Nintendo can continue selling games, maintaining their libraries, offering exclusive titles, and building their own ecosystems. What changes is that the hardware required to run these games can be provided by another layer of the industry.

A company could specialize exclusively in gaming infrastructure. It would not need to own a game library or negotiate exclusives. Its role would be to provide machines capable of running games the user already owns, in the same way that a cloud provider provides servers for applications that belong to other companies.

This would allow the cloud gaming market to compete on infrastructure rather than compete exclusively on catalog. One provider could offer lower prices, another could have lower latency, another could make more modern GPUs available, and another could have datacenters better positioned geographically.

The game library would remain an independent layer. It could even be the main competitive differentiator of a platform. Users could choose where to buy their games based on price, exclusives, services, or convenience and, separately, choose where to run those games based on computing capacity, latency, and cost.

This decoupling is precisely one of the most powerful characteristics of cloud computing. The application does not need to own the server. The company does not need to buy the hardware that runs its software. Infrastructure becomes an independent layer, consumed according to need.

There is no fundamental reason why games should be different. The game can be a product. The machine can be a service. And there is no need for both to be sold by the same company.

## What are we actually renting?

Perhaps this is the question the industry should be asking. We are talking about two different products that have been put into the same package: access to games and access to the computing capacity required to run them.

A game subscription solves the first problem. The user pays to access a catalog, which may be broad, exclusive, or simply convenient. It is a software and content distribution model. Cloud gaming solves the second. The user pays to remotely use a machine capable of running the game. It is an infrastructure model.

There is no reason these two products need to be sold together.

I can buy a game from Microsoft, Sony, Nintendo, or any other store and run it on my PC. If my hardware is not sufficient, I can rent computing capacity from a specialized provider. The company selling the game does not need to be the same company providing the machine, just as the company developing an application does not need to own the server running it.

This creates two different markets. On one side, platforms compete on games, prices, exclusives, services, and libraries. On the other, infrastructure providers compete on price, performance, latency, availability, and operational efficiency.

The problem with current models is that we often treat these two markets as if they were one. The game subscription tries to sell the catalog together with the infrastructure, while the cloud gaming proposition ends up being presented as a different way to consume a subscription.

But it does not have to be that way. I may want to play only three games during a year and have no interest in hundreds of other titles. I can buy those three games and, when my hardware is not sufficient, rent a machine capable of running them. In that scenario, I do not need a game subscription. I need a game and computing capacity.

The cloud enables precisely this separation. The game can remain a product that is purchased or subscribed to, while the machine can be a utility consumed on demand.

The gaming industry has spent decades selling us increasingly powerful computers to run increasingly demanding games. The cloud offers the possibility of reversing that relationship: instead of buying a machine to keep up with games, we can rent the capacity needed to run the game we choose.

Perhaps the future of the gaming industry is not a Netflix of video games, but an AWS for games.
