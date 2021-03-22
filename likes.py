def likes(names):
    if not names:
        return "no one likes this"

    if len(names) == 1:
        return "{} likes this".format(names[0])
    elif len(names) == 2:
        return "{} and {} like this".format(names[0], names[1])
    elif len(names) == 3:
        return "{}, {} and {} like this".format(names[0], names[1], names[2])
    else:
        return "{}, {} and {} others like this".format(names[0], names[1], (len(names) - 2))


            


print(likes(["Peter"]))
print(likes(["Peter", "James"]))
print(likes(["Peter", "James", "Andy"]))
print(likes(["Peter", "James", "Andy", "Mark"]))
print(likes([]))
