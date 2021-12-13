#A stemming algorithm reduces the words “chocolates”, “chocolatey”, “choco” to the root word, “chocolate” 
#Stemming is desirable as it may reduce redundancy as most of the time the word stem and their inflected/derived words mean the same.
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
ps=PorterStemmer()
example_words = ["python","pythoner","pythoning","pythoned","pythonly"]
for w in example_words:
    print(ps.stem(w))
#prints pythonli for pythonly bcz of slight difference in meaning
new_text="It is very important to work diligently while you are programming with python. All pythoners have pythoned poorly at least once."       
words= word_tokenize(new_text)
for w in words:  
    print(ps.stem(w))  
