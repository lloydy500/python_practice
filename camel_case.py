
def solution(s):
    # alphabet = 'abcdefghijklmnopqrstuvwxyz'.upper()
    # a = s.split()
    # caps_tracker = [(i, j) for i, j in enumerate(a) if j in alphabet]
    return s.rpartition("C")
print(solution("thisIsCamelCase"))
