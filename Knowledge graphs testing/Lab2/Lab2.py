from rdflib import Graph, Namespace, URIRef, BNode, Literal
from rdflib.namespace import RDF, FOAF, XSD
from rdflib.collection import Collection

# Create graph and bind namespace for better readability when printed
g = Graph()
EX = Namespace("http://example.org/")
g.bind("ex", EX)

# Add Mueller Investigation triples
investigation_triples = [
    (EX.Mueller_Investigation, EX.was_led_by, EX.Robert_Mueller),
    (EX.Mueller_Investigation, EX.involved, EX.Paul_Manafort),
    (EX.Mueller_Investigation, EX.involved, EX.Rick_Gates),
    (EX.Mueller_Investigation, EX.involved, EX.George_Papadopoulos),
    (EX.Mueller_Investigation, EX.involved, EX.Michael_Flynn),
    (EX.Mueller_Investigation, EX.involved, EX.Michael_Cohen),
    (EX.Mueller_Investigation, EX.involved, EX.Roger_Stone)
]
for triple in investigation_triples:
    g.add(triple)

# Add relationship triples
g.add((EX.Paul_Manafort, EX.was_business_partner_of, EX.Rick_Gates))
g.add((EX.Paul_Manafort, EX.was_campaign_chairman_for, EX.Donald_Trump))
g.add((EX.Michael_Cohen, EX.was_attorney, EX.Donald_Trump))
g.add((EX.Michael_Flynn, EX.was_adviser_to, EX.Donald_Trump))

# Create and add lying instances
lying_to_congress = BNode()
lying_to_fbi = BNode()

g.add((lying_to_congress, RDF.type, EX.Lying))
g.add((lying_to_congress, EX.detail, Literal("lying to Congress")))
g.add((lying_to_fbi, RDF.type, EX.Lying))
g.add((lying_to_fbi, EX.detail, Literal("lying to FBI")))

g.add((EX.Michael_Cohen, EX.lied_in, lying_to_congress))
g.add((EX.Michael_Flynn, EX.lied_in, lying_to_fbi))
g.add((EX.Rick_Gates, EX.lied_in, lying_to_fbi))

# Add remaining details
g.add((EX.Michael_Flynn, EX.negotiated, Literal("plea agreement")))
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

# Serialize graph
g.serialize("KG.xml", format="xml")
g.serialize("KG.ttl", format="turtle")
g.serialize("KG.nt", format="nt")
g.serialize("KG.json", format="json-ld")

# Print turtle format
print(g.serialize(format="turtle"))

