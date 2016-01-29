
from janome.tokenizer import Tokenizer
from numba.cgutils import printf
t = Tokenizer()
for token in t.tokenize(u'すもももももももものうち'):
    print (token);
