def solution(string,markers):
  #your code here
  # a = string.split("\n")
    new = []
    a = string.split("\n")
    for s in a:
      for i in range(len(markers)):
        if markers[i] in s:
          new.append(s[:(s.index(markers[i]))])
      else:
        new.append(s)
    ans = [s.strip() for s in new]
    return "\n".join(ans)

print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))
