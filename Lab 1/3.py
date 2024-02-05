def name(first, middle, last):
    if (len(first)+len(middle)+len(last))%2==0:
        return True
    else:
        return False;

print(name("Jake", "Tyler", "Mecca"))