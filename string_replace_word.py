def word_replace(sentence, old_word, new_word):
  words = sentence.split()
  z = [new_word if word == old_word else word for word in words]
  updated_sentence = " ".join(z)
  return updated_sentence


s = input("Enter your Sentence : ")
o = input("Enter a word to be replaced : ")
n = input("Enter a new word that will replace : ")

result = word_replace(s, o, n)
print(result)
