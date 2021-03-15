def disemvowel(string):
  a = [l for l in string if l not in "aeiou"]
  return "".join(a)

print(disemvowel("hello my name is lloyd"))