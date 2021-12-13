#STOP WORD FILTERATION
#'Stop words' are simply the words you don't need or their presence don't make any significant change, you can simply remove them.
#Basically fillers, they help our language make more sense to us but as far as data analysis is concerned, they're useless. e.g. the, and, a, an
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words= set(stopwords.words("english")) #we defined a set which consists all the stop words in English language

example_sentence="This is an example to show filteration of stop words."

words=word_tokenize(example_sentence)
print(words)
filtered_sentence=[]
# for w in words:
#     if w not in stop_words:
#         filtered_sentence.append(w)
#OR
filtered_sentence=[w for w in words if w not in stop_words]

print(filtered_sentence) #printing filtered sentence
