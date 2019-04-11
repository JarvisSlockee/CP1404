"""
Output should look like:
Text: this is a collection of words of nice words this is a fun thing it is
a : 2
collection : 1
fun : 1
is : 3
it : 1
nice : 1
of : 2
thing : 1
this : 2
words : 2
"""

word_count = {}
text = input("Enter a sentence: ")
words = text.split()
for word in words:
    occurrence = word_count.get(word, 0)
    word_count[word] = occurrence + 1

words = list(word_count.keys())
words.sort()

max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, word_count[word]))
