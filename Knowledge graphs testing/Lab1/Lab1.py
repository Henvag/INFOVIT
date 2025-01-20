from rdflib import Graph, URIRef, Literal, Namespace

# Create a Graph.
g = Graph()

# Define a namespace
EX = Namespace("http://example.org/")

# Add triples to the graph
g.add((EX.Mueller_Investigation, EX.was_led_by, EX.Robert_Mueller))
g.add((EX.Mueller_Investigation, EX.involved, EX.Paul_Manafort))
g.add((EX.Mueller_Investigation, EX.involved, EX.Rick_Gates))
g.add((EX.Mueller_Investigation, EX.involved, EX.George_Papadopoulos))
g.add((EX.Mueller_Investigation, EX.involved, EX.Michael_Flynn))
g.add((EX.Mueller_Investigation, EX.involved, EX.Michael_Cohen))
g.add((EX.Mueller_Investigation, EX.involved, EX.Roger_Stone))
g.add((EX.Paul_Manafort, EX.was_business_partner_of, EX.Rick_Gates))
g.add((EX.Paul_Manafort, EX.was_campaign_chairman_for, EX.Donald_Trump))
g.add((EX.Michael_Cohen, EX.was_attorney, EX.Donald_Trump))
g.add((EX.Donald_Trump, EX.pleaded_guilty_to, Literal("lying to congress")))
g.add((EX.Paul_Manafort, EX.was_charged_with, Literal("money laundering")))
g.add((EX.Paul_Manafort, EX.was_charged_with, Literal("tax evasion")))
g.add((EX.Paul_Manafort, EX.was_charged_with, Literal("foreign lobbying")))
g.add((EX.Paul_Manafort, EX.was_convicted_for, Literal("bank fraud")))
g.add((EX.Paul_Manafort, EX.was_convicted_for, Literal("tax fraud")))
g.add((EX.Paul_Manafort, EX.pleaded_guilty_to, Literal("conspiracy")))
g.add((EX.Paul_Manafort, EX.was_sentenced_to, Literal("prison")))
g.add((EX.Paul_Manafort, EX.negotiated, Literal("plea agreement")))
g.add((EX.Rick_Gates, EX.was_charged_with, Literal("money laundering")))
g.add((EX.Rick_Gates, EX.was_charged_with, Literal("tax evasion")))
g.add((EX.Rick_Gates, EX.was_charged_with, Literal("foreign lobbying")))
g.add((EX.Rick_Gates, EX.pleaded_guilty_to, Literal("conspiracy")))
g.add((EX.Rick_Gates, EX.pleaded_guilty_to, Literal("lying to FBI")))

#skibidi pap pap


g.serialize("KG.xml", format="xml")
g.serialize("KG.ttl", format="turtle")
g.serialize("KG.nt", format="nt")
g.serialize("KG.json", format="json-ld")

for s, p, o in g:
    print(s, p, o)