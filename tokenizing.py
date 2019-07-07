from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

paragraph = "Tokenization is the act of breaking up a sequence of strings into pieces such a  words, keywords, phrases, symbols and other elements called tokens. Tokens can be individual words, phrases or even whole sentences. In the process of tokenization, some characters like punctuation marks are discarded. The tokens become the input for another proce	ss like parsing and text mining."
word = []
sentence = sent_tokenize(paragraph)
for sent in sentence:
	print(sent)
	sent = sent.replace('.','')
	word.append(word_tokenize(sent))