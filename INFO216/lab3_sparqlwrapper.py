from SPARQLWrapper import SPARQLWrapper

SERVER = 'http://localhost:7200'
REPOSITORY = 'info216_lab_hevag2184'
endpoint = f'{SERVER}/repositories/{REPOSITORY}'

query1 = """
PREFIX muellerkg: <http://example.org#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
ASK {
    ?s muellerkg:investigation_start ?start ;
       muellerkg:investigation_end ?end .
    FILTER("1990-01-01"^^xsd:date >= ?start && "1990-01-01"^^xsd:date <= ?end)
}
"""


query2 = """
PREFIX muellerkg: <http://example.org#>
SELECT DISTINCT ?president
WHERE {
    ?s muellerkg:president ?president .
}
ORDER BY ?president
"""

client = SPARQLWrapper(endpoint)
client.setQuery(query2)
client.setReturnFormat('json')
results = client.queryAndConvert()

print("Presidents in the graph:")
for result in results["results"]["bindings"]:
    president = result["president"]["value"]
    print(president.replace("http://example.org#", ""))



client = SPARQLWrapper(endpoint)
client.setQuery(query)
client.setReturnFormat('json')
result = client.queryAndConvert()
print(f"Was there an ongoing investigation on 1990-01-01? {result['boolean']}")