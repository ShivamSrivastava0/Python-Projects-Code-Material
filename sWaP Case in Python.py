def swap_case(s):
    a = []
    for i in s:
        if i.isupper():
            a.append(i.lower())
        elif i.islower():
            a.append(i.upper())
        else:
            a.append(i)
    return ''.join(a)
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
