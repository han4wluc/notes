
from py2neo import Graph
graph = Graph(bolt=True, host="localhost", user='neo4j' , password="neo4j")
import json


# helpder function to run a query and print out the result as a json
def run_query_and_print_json(query):
  data = graph.data(query)
  print(json.dumps(data,indent=2))

def caption_print(content):
  print("#####\n" + content + "\n#####")


query = """
CREATE (TheMatrix:Movie {title:'The Matrix', released:1999, tagline:'Welcome to the Real World'})
CREATE (Keanu:Person {name:'Keanu Reeves', born:1964})
CREATE (Carrie:Person {name:'Carrie-Anne Moss', born:1967})
CREATE (Laurence:Person {name:'Laurence Fishburne', born:1961})
CREATE (Hugo:Person {name:'Hugo Weaving', born:1960})
CREATE (LillyW:Person {name:'Lilly Wachowski', born:1967})
CREATE (LanaW:Person {name:'Lana Wachowski', born:1965})
CREATE (JoelS:Person {name:'Joel Silver', born:1952})
CREATE
  (Keanu)-[:ACTED_IN {roles:['Neo']}]->(TheMatrix),
  (Carrie)-[:ACTED_IN {roles:['Trinity']}]->(TheMatrix),
  (Laurence)-[:ACTED_IN {roles:['Morpheus']}]->(TheMatrix),
  (Hugo)-[:ACTED_IN {roles:['Agent Smith']}]->(TheMatrix),
  (LillyW)-[:DIRECTED]->(TheMatrix),
  (LanaW)-[:DIRECTED]->(TheMatrix),
  (JoelS)-[:PRODUCED]->(TheMatrix)

CREATE (Emil:Person {name:"Emil Eifrem", born:1978})
CREATE (Emil)-[:ACTED_IN {roles:["Emil"]}]->(TheMatrix)

CREATE (TheMatrixReloaded:Movie {title:'The Matrix Reloaded', released:2003, tagline:'Free your mind'})
CREATE
  (Keanu)-[:ACTED_IN {roles:['Neo']}]->(TheMatrixReloaded),
  (Carrie)-[:ACTED_IN {roles:['Trinity']}]->(TheMatrixReloaded),
  (Laurence)-[:ACTED_IN {roles:['Morpheus']}]->(TheMatrixReloaded),
  (Hugo)-[:ACTED_IN {roles:['Agent Smith']}]->(TheMatrixReloaded),
  (LillyW)-[:DIRECTED]->(TheMatrixReloaded),
  (LanaW)-[:DIRECTED]->(TheMatrixReloaded),
  (JoelS)-[:PRODUCED]->(TheMatrixReloaded)
"""

graph.run(query)

caption_print('movie data created')


# return all nodes
caption_print('All Data:')
query = """
MATCH (n) RETURN n
"""
run_query_and_print_json(query)

caption_print('Fetch one node')
query = """ MATCH (person {name: "Keanu Reeves"}) RETURN person """
run_query_and_print_json(query)

caption_print('Fetch one node of type Movie:')
query = """ MATCH (matrix:Movie {title: "The Matrix"}) return matrix """
run_query_and_print_json(query)

caption_print('Fetch all movies release in the nineties')
query = """ MATCH (nineties:Movie) WHERE nineties.released >= 1990 AND nineties.released < 2000 RETURN nineties """
run_query_and_print_json(query)

caption_print('List all movies Keanu acted in ')
query = """
MATCH (person:Person {name: "Keanu Reeves"})-[:ACTED_IN]->(keanusMovies) RETURN person,keanusMovies
"""
run_query_and_print_json(query)

caption_print('List all the names of people who directed the movie matrix:')
query = """
MATCH (movie {title: "The Matrix"})<-[:DIRECTED]-(directors) RETURN directors.name
"""
run_query_and_print_json(query)

# delete all data
query = """
MATCH (n) DETACH DELETE n
"""
graph.run(query)
caption_print('all data in database has been deleted')



