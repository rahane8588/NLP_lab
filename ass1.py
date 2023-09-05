import spacy
nlp = spacy.load("en_core_web_sm")

print("------------------------Sentence Detection----------------------")  
about_text = (
    "Gus Proto is a Python developer currently"
    " working for a London-based Fintech"
    " company. He is interested in learning"
    " Natural Language Processing."
    )
about_doc = nlp(about_text)
sentences = list(about_doc.sents)
len(sentences)
2
for sentence in sentences:
    print(f"{sentence[:5]}...")
    
    
    
    
print("---------------------------Tokenization -------------------------")
about_text = (
    "Gus Proto is a Python developer currently"
    " working for a London-based Fintech"
    " company. He is interested in learning"
    " Natural Language Processing."
)
about_doc = nlp(about_text)

for token in about_doc:
  print (token, token.idx)
  
  
print("----------------------------Stop words-----------------------------") 
spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS
len(spacy_stopwords)
for stop_word in list(spacy_stopwords)[:10]:
    print(stop_word)
    custom_about_text = (
    "Gus Proto is a Python developer currently"
    " working for a London-based Fintech"
    " company. He is interested in learning"
    " Natural Language Processing."
    )
about_doc = nlp(custom_about_text)
print([token for token in about_doc if not token.is_stop])