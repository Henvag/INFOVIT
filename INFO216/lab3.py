from rdflib import Graph
from pathlib import Path

g = Graph()
g.parse(Path("INFO216/Russia_investigation_kg.ttl"), format='ttl')


# Query all distinct predicates using SPARQL
first_query = g.query("""PREFIX ex: <http://example.org/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX schema: <https://schema.org/>
PREFIX muellerkg: <http://example.org#>
SELECT DISTINCT ?p
WHERE {
    ?s ?p ?o .
}""")


"""for row in first_query:
    print(row[0])"""

second_query = g.query("""
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX schema: <https://schema.org/>
PREFIX muellerkg: <http://example.org#>
SELECT DISTINCT ?president
WHERE {
    ?s muellerkg:president ?president .
}
ORDER BY ?president""")

"""for row in second_query:
    print(row[0])
"""

third_query = g.query("""PREFIX muellerkg: <http://example.org#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX schema: <https://schema.org/>

SELECT DISTINCT ?president ?name
WHERE {
    ?s muellerkg:president ?president ;
       muellerkg:name ?name .
    FILTER (?name != "None")
}
ORDER BY ?president ?name""")

# Create dictionary using dict comprehension
pres_dict = {}
for row in third_query:
    president = str(row[0])
    indicted = str(row[1])
    if president not in pres_dict:
        pres_dict[president] = []
    if indicted != "None":
        pres_dict[president].append(indicted)

#print(pres_dict)


fourth_query = g.query("""PREFIX muellerkg: <http://example.org#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX schema: <https://schema.org/>
ASK {
    {
        SELECT (COUNT(DISTINCT ?name) AS ?count)
        WHERE {
            ?s muellerkg:president muellerkg:Donald_Trump ;
               muellerkg:name ?name ;
               muellerkg:pardoned true .
            FILTER (?name != "None")
        }
        HAVING (?count > 5)
    }
}

""")




print(fourth_query.askAnswer)








