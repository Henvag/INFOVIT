import spacy
from spacy.symbols import nsubj, VERB
from spacy.displacy import serve
nlp = spacy.load('en_core_web_md')
nlp.add_pipe("merge_entities")
nlp.add_pipe("merge_noun_chunks")

doc1 = nlp("I like salty fries and hamburgers.")
doc2 = nlp("Fast food tastes very good.")

french_fries = doc1[2:4]
burgers = doc1[4]


print(doc1, "<-->", doc2, doc1.similarity(doc2))

print(french_fries,"<-->", burgers, french_fries.similarity(burgers))




#Work with jupyter notebook
#spacy.displacy.render(doc1, style='ent', jupyter=True)

#Work with localhost server
#serve(doc1, style='ent', auto_select_port=True)