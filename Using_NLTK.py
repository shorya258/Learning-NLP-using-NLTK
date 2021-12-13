#this simple program shows the use of python and nltk to tokenize sentences and words
from nltk.tokenize import sent_tokenize, word_tokenize
example_text='"I am not a psychopath, Anderson. I am a high functioning sociopath, do you research": Mr. Sherlock Holmes'

print(sent_tokenize(example_text))
print(word_tokenize(example_text))
example= "There is nothing more deceptive than obvious fact."
print(sent_tokenize(example))
print(word_tokenize(example))
