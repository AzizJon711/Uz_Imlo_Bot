from uzwords import words
from difflib import get_close_matches
from transliterate import to_latin, to_cyrillic

words_cr=words
words_uz=[]

for word in words_cr:
   words_uz.append(to_latin(word))

def correctWord(word):
   word=word.lower()
   words_list=[]
   for i in get_close_matches(word, words_uz, n=100):
      words_list.append(i.lower())
   if word in words_list:
      return [1,word]
   else:
      if "h" in word:
         word=word.replace("h","x")
      elif "x" in word:
         word=word.replace("x", "h")
      else:
         word=word
      return [0, get_close_matches(word, words_uz, n=5)]
