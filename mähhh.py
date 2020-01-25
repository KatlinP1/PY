def kitten (s):
    if s.find ("Is")==0:
        return s
    return ("Is %s" % s )

print(kitten(" vello"))
print(kitten("Is something"))