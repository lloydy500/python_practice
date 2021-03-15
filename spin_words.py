def spin_words(sentence):
  #split the sentence into seperate words
  #iterate each len each word if len is > 5 then map its reverse to new_array
  #join the array back up to string#
  if len(sentence.split()) == 1:
    return sentence[::-1] if len(sentence) > 5 else sentence
  else:
    a = sentence.split()
    new_array = [word[::-1] if len(word) >= 5 else word for word in a]
    s = " ".join(new_array)
    return s

print(spin_words("hello my name is lloyd"))


