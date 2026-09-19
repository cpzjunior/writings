# PostgreSQL really is the Skyrim of databases

_A product that is complete in its own right, but with a community capable of turning it into something its own creators might never have been able to build alone._

**Summary:** I see PostgreSQL as the Skyrim of databases not because of the number of extensions, but because it is a complete product that also works as a platform open to the community. Its architecture allows third parties to add new data models, workloads, and execution approaches without abandoning the original foundation, taking PostgreSQL into territories its creators could never cover alone. This extensibility, however, also brings operational complexity as extensions accumulate. In the end, PostgreSQL's greatness lies precisely in not needing to do everything in order to allow other people to discover how far it can go.

---

Some time ago, I watched a video from The Coding Gopher YouTube channel in which a joke came up that, at first, shouldn't have deserved that much attention: PostgreSQL is the Skyrim of databases. The comparison made me laugh, but I also kept thinking about it for far too long. The more I tried to find the reasons why it didn't make sense, the more I realized that, in a strangely precise way, it did.

At first glance, the comparison seems to be nothing more than a joke about the amount of things that exist around both. Skyrim has a community that has created mods to alter, expand, and reinvent practically every aspect of the game. PostgreSQL has an equally broad ecosystem of extensions. So far, the analogy works as a good programmer joke. But the more I think about it, the more I realize that the similarity lies somewhere else.

Skyrim doesn't need mods to be Skyrim. The original game is complete, enormous, and perfectly capable of supporting hundreds of hours of gameplay on its own. There are bugs, some of them quite well known, but they don't prevent you from playing, finishing the main story, and exploring the expansion content. I myself finished the base game and its expansions without installing mods. Mods aren't what makes Skyrim a complete game. They're interesting because they allow other people to alter and expand the game in ways its creators didn't plan.

PostgreSQL seems to follow a similar logic. It is already a complete product on its own. Even so, there is an enormous amount of things built on top of it, some of them so large that they actually change the category of problems the database can solve.

And that's where the comparison starts to get interesting. What makes PostgreSQL so extensible? What has the community managed to build on top of this foundation? And how far can a database be taken when the original product leaves enough room for other people to build on top of it?

## The vanilla product is already large

One of the most curious characteristics of PostgreSQL is the number of things already inside a product that many people still simply describe as “a relational database.” JSONB is a good example. PostgreSQL isn't limited to storing a string containing JSON: it has its own data type, specific operators, functions for manipulating the structure, and indexing mechanisms such as GIN. It is possible to combine the traditional relational model with documents without having to abandon the database or introduce another datastore. Full Text Search follows a similar logic, with types, operators, linguistic configurations, and ranking mechanisms sufficient to build text search functionality directly in the database.

But the breadth of the product goes far beyond JSON and text search. PostgreSQL has a very rich type system, including arrays, ranges, enums, composite types, and user-defined types. These types can participate in SQL expressions, have their own operators, and be used in indexes. This means the data model isn't limited to the traditional combination of strings, numbers, and dates. The user can represent domain-specific concepts directly in the database and make those concepts participate in the operations the system already knows how to execute.

The same thing happens with the query language. PostgreSQL doesn't just offer SELECT, INSERT, UPDATE, and DELETE with a few variations. Window functions make it possible to perform calculations over sets of related rows without abandoning the context of the query. CTEs make it possible to structure complex queries into stages, while recursive queries allow you to traverse hierarchical structures and recursive relationships. Materialized views make it possible to persist query results for certain access patterns. Constraints allow integrity rules to be expressed directly in the model, while triggers and functions allow additional logic to be placed close to the data.

There is also a significant number of mechanisms aimed at performance and operating at scale. PostgreSQL has different indexing methods, such as B-tree, Hash, GiST, SP-GiST, GIN, and BRIN, each suited to different data structures and query patterns. Partitioning allows a logical table to be distributed across multiple partitions, while parallelism features allow certain operations to be executed using multiple processes. The query planning and execution system also has a variety of strategies for deciding how to access and combine data, rather than simply executing the query the way it was written.

When we get to replication and system operations, the list continues. PostgreSQL has streaming replication, logical replication, point-in-time recovery mechanisms, and tools for backup and restoration. Logical replication, in particular, allows you to select which data is replicated and build architectures that go far beyond the traditional primary and read replica. There are also monitoring and diagnostic features, as well as official extensions and internal mechanisms that allow you to observe the behavior of the database itself.

And there is one more characteristic that may be even more important to our discussion: PostgreSQL is programmable. Functions can be written in SQL and PL/pgSQL, while the system also supports other procedural languages through extensions. It is possible to create functions, operators, aggregates, casts, and custom types. Triggers can react to events involving data, and Foreign Data Wrappers allow the database to access external sources such as foreign tables. The boundary between “stored data” and “logic executed by the database” is much more flexible than the description of PostgreSQL as simply a relational database tends to suggest.

And this list is still far from exhaustive. The point isn't to turn this text into a feature catalog, but to establish the size of the foundation on which the rest of the discussion will be built. PostgreSQL brings together relational storage, different data models, sophisticated query mechanisms, programming, indexing, partitioning, replication, text search, and integration with external systems within the same product. In other contexts, parts of this set might be distributed across different products.

This also changes how we should interpret what comes next. When an extension adds a new capability to PostgreSQL, it isn't necessarily compensating for a basic deficiency in the database. It is starting from a system that already has an enormous number of abstractions ready and using those abstractions to solve an even more specific problem. The starting point is already sophisticated.

You can install PostgreSQL, start building an application, and spend years exploring its capabilities without ever needing to look for a “mod” to make it interesting. It is possible to build transactional systems, applications that work with documents, analytical workloads, text search engines, systems with hierarchical structures, and applications that require highly specific data models using only what is already part of the product.

And that's precisely what makes the analogy with Skyrim interesting. Mods aren't necessary to turn the original game into something complete. They exist because, once there is a sufficiently large and flexible game, space emerges for other people to add systems that didn't need to be part of the original experience. In PostgreSQL, the logic is similar.

The difference is that, in the case of the database, this space didn't arise merely because there were many features. It was created by an architecture that allows third parties to participate in important parts of the system itself. And that leads us to the next question: is PostgreSQL merely an extremely complete product or, in practice, does it also work as a platform?

## When a product becomes a platform

This question seems simple until we look at everything that exists around PostgreSQL. PostGIS, TimescaleDB, pgvector, and Citus are different projects, with their own communities, goals, and development models, but they all find in PostgreSQL a foundation on which they can build capabilities that aren't part of the official product. This is where the word platform starts to make sense.

A product can be evaluated primarily by what its creators deliver and maintain as part of its official experience. A platform also needs to be evaluated by what other people can build on top of it. The product remains the starting point, but the architecture it offers takes on value of its own because it creates a space of possibilities for third parties.

This is different from simply having a large ecosystem of plugins. Software can have thousands of extensions that add small features without significantly changing what can be built on top of it. In PostgreSQL's case, extensibility reaches important parts of the system itself: new types can participate in queries, operators can be integrated into SQL expressions, indexing methods can be added, external sources can appear as foreign tables, and extensions can combine different mechanisms to create abstractions that behave like natural parts of the database.

What makes PostgreSQL a platform isn't the number of available extensions, but the depth with which third parties can participate in the system's model. An extension can introduce new data types, new operations, new access mechanisms, or new ways of integrating PostgreSQL with external systems. Instead of simply adding functionality beside the database, it can participate in mechanisms that are part of the very way PostgreSQL represents, queries, and manipulates data.

This also solves a problem of scope. It wouldn't make sense to expect the official project to develop and maintain, within the core itself, a first-class geospatial solution, a platform specialized in time series, vector search mechanisms, a distributed architecture, graph support, and dozens of other specializations. Each domain has its own requirements, trade-offs, workloads, and communities. Incorporating all of them into the same product would mean making the core carry decisions and complexities that only a portion of users need, while also forcing the main project to take responsibility for maintaining technologies that could evolve independently.

The platform allows for a different division of responsibilities: PostgreSQL provides the foundation, while independent projects take responsibility for specializing in their respective domains. The main project doesn't need to anticipate every possible way the database might be used. It needs to provide sufficiently general mechanisms so that other people can explore possibilities that weren't part of the original scope.

This is precisely where the comparison with Skyrim stops being merely a joke about mods. The game didn't become a modding platform simply because there was a lot of content to modify. It provided a foundation on which other people could build experiences that no studio, no matter how large, could have produced alone at the same scale and diversity. The developers created the game, but they didn't need to anticipate every way the community might want to expand it.

In PostgreSQL, the relationship is similar. The official project doesn't need to anticipate every category of problem that will emerge in the future for the ecosystem to explore them when they appear. The value of the platform lies precisely in allowing the community to find uses that didn't need to be part of the original plan.

And now the comparison is no longer just an abstract idea. If PostgreSQL really works as a platform, we need to look at what has been built on top of it. And perhaps there is no better place to start than teaching PostgreSQL to understand the physical world.

## PostgreSQL gains a spatial model

There may be no better example to start talking about PostgreSQL mods than PostGIS. If vanilla PostgreSQL is already a complete relational database, PostGIS shows what happens when someone decides that it should also understand the physical world. The extension adds data types such as geometry and geography to the database, support for different spatial reference systems, operators and functions for working with geometry, topological relationships, and specialized indexes for spatial queries. The result isn't simply a function that calculates the distance between two points. The database begins to understand a new category of data and execute operations on it as part of its own query model.

The difference becomes clearer when we think about concrete examples. A column can represent a point, a line, or a polygon. We can store customer locations, represent streets, draw coverage areas, calculate distances, find which establishments are within a given radius, determine whether two regions overlap, or identify which geographic objects are closest to one another. All of this can be combined with the relational capabilities that already existed in PostgreSQL. A query can join customer, financial, or transactional data with spatial information and use appropriate indexes to make these operations viable at large volumes.

The most interesting point is that PostGIS didn't need to turn PostgreSQL into another database to do this. It managed to add an entire domain to the system using precisely the extensibility mechanisms PostgreSQL provides. New data types represent concepts that didn't exist in the original model, operators allow relationships between these objects to be expressed, functions implement geometric operations, and specialized indexes make it possible to query this data efficiently. The result integrates with SQL and the rest of the database rather than existing as a completely separate system.

This changes how we think about what an extension means. If someone said that PostgreSQL supports geolocation, we might imagine a few functions for calculating latitude and longitude. PostGIS is in another category. It allows you to build applications based on a complete spatial model without abandoning PostgreSQL as the data layer. Mapping systems, logistics, mobility, urban planning, and territorial analysis applications can combine spatial data with relational data, transactions, permissions, and everything else in the ecosystem within the same system.

And this is an excellent first example because PostGIS isn't a curiosity created merely to demonstrate that PostgreSQL is extensible. It is a mature project, with its own community and an extremely broad application domain. The community didn't merely add a feature to PostgreSQL. It found a new dimension in which the database could operate and built an entire infrastructure to explore it.

It's exactly the kind of transformation that makes the Skyrim analogy interesting. You start with the original game and install a mod that adds a new gameplay system. The foundation remains recognizable, but the possibilities available to the player change significantly. In PostgreSQL, you start with a relational database and install PostGIS. Suddenly, that database knows how to work with points, lines, polygons, distances, intersections, coordinates, and spatial relationships. It's not just another function in the inventory. It's an entirely new domain within the same universe.

And PostGIS is only the first example. If an extension can take a relational database into the geospatial domain, we can start asking a more interesting question: what else can be built on the same foundation?

## A time-series database inside the database

If PostGIS shows that PostgreSQL can learn to understand space, TimescaleDB shows that it can also be specialized to understand time. Time-series data has very particular characteristics: data usually arrives continuously, is organized chronologically, grows almost incessantly, and is frequently queried using time intervals, aggregations, windows, and different levels of granularity. Infrastructure metrics, application telemetry, sensors, financial markets, and observability data are examples of workloads in which these properties matter. Storing timestamps in a table solves only the basic representation of the data. It doesn't necessarily mean that the database is organized to exploit the characteristics of this type of workload.

This is where TimescaleDB becomes a particularly interesting example of the PostgreSQL ecosystem. The technology adds a specialized layer for working with time series, introducing its own abstractions and mechanisms for organizing, partitioning, and querying large volumes of temporal data. The concept of a hypertable is a good example of this approach: to the application, we continue working with a table and with SQL, but beneath that abstraction, the system can organize the data into a structure better suited to the growth and access patterns typical of time series. Features such as continuous aggregates and retention policies also make it possible to treat recurring operations for this type of workload as part of the platform itself.

The most interesting part, however, is what didn't have to be abandoned. PostgreSQL remains the foundation. SQL remains the central language. Transactions, data types, functions, indexes, and the entire ecosystem built around PostgreSQL remain part of the story. An application doesn't necessarily need to adopt a completely different programming model simply because its primary workload has become temporal. The specialization happens within a platform the developer already knows.

This is different from simply adding a feature. TimescaleDB takes a specific class of problem and brings PostgreSQL into territory where specialized databases exist. The point isn't that PostgreSQL stopped being relational and became a time-series database. Quite the opposite: a community found a way to specialize it for this domain without abandoning the characteristics that already made the product attractive.

And this is where the Skyrim analogy gains another dimension. The original game didn't need to be transformed into something else to be complete, but that didn't prevent someone from creating a specialized experience on top of it. TimescaleDB follows the same logic: PostgreSQL already works perfectly as a relational database, but it can receive a specialized layer when the problem requires another way of organizing and exploring data.

The pattern starts to emerge. First someone adds geospatial capabilities. Then someone specializes it for time series. And before you realize it, PostgreSQL is no longer just storing an application's data. It starts occupying territories that we would normally associate with entire categories of specialized databases.

## And then PostgreSQL gains vectors

If, a few years ago, someone had said that PostgreSQL would be an important part of the infrastructure of modern artificial intelligence applications, the statement would probably have seemed strange. PostgreSQL was born in another era, for a very different category of problems. Its fundamental model is relational, based on tables, rows, columns, keys, and SQL queries. None of this seems particularly related to embeddings, language models, or semantic search. And yet, the rise of AI applications found a particularly important extension in the PostgreSQL ecosystem: pgvector.

The fundamental idea is simple, but its consequences are significant. pgvector adds data types to PostgreSQL for representing vectors and mechanisms for performing similarity searches. Embeddings produced by machine learning models can be stored directly in the database and queried using different distance metrics. For larger workloads, the extension also provides indexing methods such as HNSW and IVFFlat, allowing vector search mechanisms to be built without necessarily introducing a database specialized exclusively for this function.

This changes the role PostgreSQL can play within an application. An architecture that has users, documents, permissions, orders, or other structured data in the relational database and embeddings in separate infrastructure can, in certain scenarios, keep this information in the same system. The document remains a relational record. Its metadata remains in PostgreSQL. Its permissions remain in PostgreSQL. The embedding can also be in PostgreSQL. And a query can combine relational filters with similarity search, rather than necessarily requiring the application to coordinate two different systems.

This doesn't mean that PostgreSQL has become the best vector database for every workload, nor that specialized databases have ceased to make sense. That isn't the point. What matters is that a technology created decades before the current AI wave managed to incorporate a new data model and a new query pattern without having to abandon its identity or turn the core into something else.

This may be one of the strongest examples of the thesis because the domain didn't exist in the way we know it today when PostgreSQL was conceived. The community wasn't simply adding a feature that was missing from an old requirements list. It was responding to a need that emerged much later, using a platform that already existed. The product didn't need to predict the future to remain relevant in the future.

And that's exactly what makes extensible platforms so interesting. No one needed to predict that embeddings would become a central component of certain software architectures. When that need appeared, there was enough room in PostgreSQL for someone to build a solution on top of it.

In Skyrim, a mod can emerge years after release to add a mechanic that no one had imagined when the game was created. In PostgreSQL, someone can do something similar decades later and teach the database to work with vectors.

After geospatial, time series, and vectors, the question starts to become increasingly complex: what if PostgreSQL could also be a graph database?

## When PostgreSQL learns to work with graphs

After geospatial, time series, and vectors, the question starts to become even stranger: what if PostgreSQL could also work with graphs? At first glance, it seems like a contradiction. PostgreSQL is a relational database, while graph databases start from a different model, in which relationships between entities are central elements of data representation. Instead of thinking only in terms of tables related by keys, the graph model works directly with vertices, edges, and properties, allowing networks of relationships to be represented and traversed naturally.

Even so, projects such as Apache AGE add graph database capabilities to PostgreSQL. The extension makes it possible to work with graphs using concepts such as vertices and edges and introduces support for the Cypher language for querying these structures. The result is a layer that allows PostgreSQL to represent and query graphs without abandoning the relational infrastructure that continues to exist underneath it.

This doesn't mean that PostgreSQL has become a universal replacement for specialized graph databases. Graph workloads have their own requirements, and dedicated systems exist precisely because certain applications benefit from architectures built specifically for this model. The point here is different: the same foundation that already supports relationships, documents, spatial data, time series, and vectors can also serve as the basis for a graph abstraction.

This begins to reveal a pattern. PostGIS adds a spatial model. TimescaleDB specializes the database for time series. pgvector adds vectors and similarity search. Apache AGE adds graph concepts and a query language specific to them. These are problems that belong to different categories, with different data models and access patterns, but all of them can find space within the same ecosystem.

And with each new example, the question changes. We stop asking “what can PostgreSQL do?” and start asking “what hasn't someone tried to do with PostgreSQL yet?” That's the modding mindset: look at an existing platform, find a need that wasn't necessarily part of the original scope, and simply ask: “What if we did this here too?”

##

## When PostgreSQL becomes distributed

Citus takes PostgreSQL's extensibility in a different direction. PostGIS adds a data domain. TimescaleDB specializes a workload. pgvector introduces vectors and similarity search. Citus changes the execution architecture itself: it makes it possible to distribute data and processing across multiple nodes while keeping PostgreSQL and SQL at the center of the application experience. This is a change of category. The problem is no longer just “what can the database represent or query?” and becomes “where is the data and where is the query executed?”

In a distributed architecture, it is necessary to decide how to partition data, route queries, execute operations involving multiple nodes, and coordinate that processing. Citus uses PostgreSQL as the foundation for dealing with these problems, allowing an application to work with a distributed architecture without completely abandoning the model and tools it already uses with PostgreSQL.

It is perhaps the strongest example so far that extensibility doesn't simply mean adding features to the database. The same foundation can be taken into a completely different execution architecture.

And this brings the Skyrim analogy closer to a concept familiar in modding: total conversion. Instead of merely adding content to the original game, it uses its foundation to create an experience that may have its own rules, systems, and identity. In the PostgreSQL ecosystem, some projects come close to this point. They remain built on PostgreSQL, but can no longer be easily described as “PostgreSQL with an extension.” They are technologies that use the database as a foundation for solving a larger problem.

But the large projects are only one part of the ecosystem. There are extensions that solve much more specific problems. pg_stat_statements adds detailed statistics about query execution and is widely used in observability and tuning. pg_cron allows scheduled tasks to be executed directly in PostgreSQL. HypoPG allows hypothetical indexes to be tested and their potential impact on query planning to be evaluated without physically creating them. pg_repack assists in reorganizing tables and indexes with lower operational impact in certain scenarios. pg_partman automates the management of partitioned tables, especially in workloads with continuous partition creation. postgres_fdw allows data stored on other PostgreSQL servers to be queried.

And the list continues in very different directions: there are extensions for auditing, authentication, queues, encryption, identifier generation, string manipulation, integration with external systems, and a series of highly specific needs.

Not all of these extensions transform PostgreSQL into a new category of database. Some solve an operational problem. Others automate a task. Others add a function or abstraction someone needed. Some are so specific that they practically disappear into the infrastructure once installed.

This is also part of the Skyrim analogy. Not every mod needs to add an entire region or transform the combat system. Some add a weapon, fix an interface, automate a task, or allow two other mods to work together. Their size and importance can vary enormously, but they all occupy the same fundamental space: what the community decided to build on top of the original product.

And perhaps that's precisely what makes the PostgreSQL ecosystem so difficult to summarize. The large projects are the easiest to see, but there is an enormous layer of smaller extensions solving problems that might never have justified a change to the core.

## When Skyrim stops looking like Skyrim

The analogy also has a less convenient side. Skyrim allows you to install mods almost indefinitely, but that doesn't mean installing more mods necessarily makes the experience better. After a certain point, the problem stops being finding new mods and becomes making all of them work together.

The same thing happens with PostgreSQL extensions. An extension can be excellent on its own and still increase the operational complexity of the system. You need to consider compatibility with the PostgreSQL version, dependencies, upgrade strategy, backup and restore, observability, support, and documentation. More importantly, someone needs to know that extension well enough to diagnose a problem when it is involved.

This means that an extension has a cost that doesn't appear in the installation command. It adds a new operational surface to the system. The problem becomes more evident when several extensions are combined. An application might depend on PostGIS, pgvector, a partitioning extension, observability tools, and other integrations. Each component may work perfectly on its own, but the architecture now has more versions to control, more dependencies to track, and more possibilities for interaction between its components.

It's the equivalent of a Skyrim modpack. A single mod can be simple to install. Hundreds of them turn the installation into a system that needs to be managed. This isn't an argument against extensions. It's precisely the other side of the same characteristic that makes the PostgreSQL ecosystem so powerful. Extensibility allows solutions to be built that the core wouldn't need to implement, but each new layer also needs to be operated, updated, and understood.

For that reason, the existence of thousands of extensions doesn't mean that an architecture should use thousands of them. The value lies in the possibility of choosing those that solve a real problem. A PostgreSQL with a few well-selected extensions can be an extremely elegant architecture. A PostgreSQL that has accumulated components over the years without anyone knowing exactly why they are there can become a corporate modpack.

## So is PostgreSQL really the Skyrim of databases?

After taking the joke seriously, the comparison seems less absurd than it did at the beginning. Vanilla PostgreSQL is complete. You can use it for years without installing a single extension and still explore only a portion of its capabilities. There is no structural dependency on an extension community for the product to be useful, sophisticated, or suitable for production systems.

But there is a second layer. Throughout this article, we've seen PostgreSQL take on roles that go far beyond the traditional relational database: geospatial, time series, vector search, graphs, integration with external sources, and distributed architectures. And these examples are far from representing everything that exists in the ecosystem.

There is also the less convenient side of the analogy. You can install too many extensions, accumulate dependencies, increase operational complexity, and end up managing a modpack that few people on the team actually understand. The existence of a thousand mods doesn't mean Skyrim became better. It means Skyrim allowed someone to get to a thousand mods.

That is, in the end, why the comparison works. Not because PostgreSQL has many extensions. Not because Skyrim has many mods. And certainly not because extensions are simply “mods for databases.”

The similarity lies in something more specific: both are complete products that also became platforms for a community to build things their original creators could never have built alone at the same scale and diversity.

Skyrim doesn't need mods to be a great game. PostgreSQL doesn't need extensions to be a great database. Mods are interesting precisely because they aren't necessarily fixing a broken product. They explore the space that a complete product left open for other people to do what its creators didn't.

PostgreSQL really is the Skyrim of databases. Not because it was built to do everything, but because it was built in a way that allows other people to discover how far it can go.
