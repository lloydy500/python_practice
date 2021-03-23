def wave(people):
    if not people:
        return []
    a = []
    
    for i in range(len(people)):
        if people[i] == " ":
            continue
        mexican_letter = people[i].upper()
        word_part_one = people[:i]
        word_part_two = people[i+1:]
        mexican_word = word_part_one + mexican_letter + word_part_two
        a.append(mexican_word)
    return a

print(wave("hello"))
print(wave(" gap "))
