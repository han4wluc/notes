

Neo4j is a graph database.
Unlike traditional relational databases where the units are tables, rows, and columns, a graph database is made up of nodes and relationships.

Neo4j offial website: https://neo4j.com/
Youtube video intro to neo4j: https://www.youtube.com/watch?v=GekQqFZm7mA
Neo4j github repo: https://github.com/neo4j/neo4j
Neo4j docker: https://hub.docker.com/_/neo4j/
py2neo: Python client for node4j: http://py2neo.org/v3/index.html#

Tutorial:

The following tutorial will demonstrate how to set up a new neo4j server from scratch, and what you can do with it. It will use neo4j and python.

* first, set up a server.
* install docker
* install neo4j with the folowing docker command: 
`
docker run \
    --publish=7474:7474 --publish=7687:7687 \
    --volume=/apps/neo4j/data:/data \
    neo4j
`

* from your browser open: http://ipaddress:7687
* Login with the intial password `neo4j` and change to a new password.
* You can play around neo4j with the web interface.

* install py2neo `pip install py2neo`

* Neo4j uses a query language called Cypher to make queries.

Create a node of type Movie:
`CREATE (TheMatrix:Movie {title:'The Matrix', released:1999, tagline:'Welcome to the Real World'})`
Create a node of type Person:
`CREATE (Keanu:Person {name:'Keanu Reeves', born:1964})
As you can see, each node can also contain properties, in this case name and baord
Add a relationship between two nodes
`CREATE (Keanu)-[:ACTED_IN {roles:['Neo']}]->(TheMatrix)`

Fetch one node:
`MATCH (person {name: "Keanu Reeves"}) RETURN person`

Fetch one node of type Movie:
`MATCH (matrix:Movie {title: "The Matrix"}) return matrix`

Fetch all movies release in the nineties
`MATCH (nineties:Movie) WHERE nineties.released >= 1990 AND nineties.released < 2000 RETURN nineties`

List all movies Keanu acted in 
`MATCH (person:Person {name: "Keanu Reeves"})-[:ACTED_IN]->(keanusMovies) RETURN person,keanusMovies`

List all the names of people who directed the movie matrix:
`MATCH (movie {title: "The Matrix"})<-[:DIRECTED]-(directors) RETURN directors.name`




