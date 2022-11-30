import docx2txt
import nltk
# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')

SKILLS_DB = set()

def extract_text_from_docx(docx_path):
    txt = docx2txt.process(docx_path)
    # print(txt)
    if txt:
        return txt.replace('\t', ' ')
    print(txt)    
    return None

def extract_skills(input_text):
    stop_words = set(nltk.corpus.stopwords.words('english'))
    word_tokens = nltk.tokenize.word_tokenize(input_text)
 
    # remove the stop words
    filtered_tokens = [w for w in word_tokens if w not in stop_words]
 
    # remove the punctuation
    filtered_tokens = [w for w in word_tokens if w.isalpha()]
 
    # generate bigrams and trigrams (such as artificial intelligence)
    bigrams_trigrams = list(map(' '.join, nltk.everygrams(filtered_tokens, 2, 3)))
 
    # we create a set to keep the results in.
    found_skills = set()
 
    # we search for each token in our skills database
    for token in filtered_tokens:
        if token.lower() in SKILLS_DB:
            found_skills.add(token)
 
    # we search for each bigram and trigram in our skills database
    for ngram in bigrams_trigrams:
        if ngram.lower() in SKILLS_DB:
            found_skills.add(ngram)
 
    return found_skills


print("\t---- System Started ----")
n = int(input("Enter number of Required Skills "))
i=0
print("Enter Skills - ")
while(i<n):
    s = input()
    s = s.lower()
    SKILLS_DB.add(s)
    i+=1

# print(SKILLS_DB)
rpath = input("Enter path of Candidate's Resume : ")
text = extract_text_from_docx(rpath)
skills = extract_skills(text)
print("Matched Skills are - ", len(skills), " -> ",skills)

x = len(skills)/len(SKILLS_DB) * 100
print("Percent Match - ", round(x,2), "%")

if(x > 75):
    print("Recuiter should Prefer.")
else:
    print("Recuiter can wait for better candidate.")
