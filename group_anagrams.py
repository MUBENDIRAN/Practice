def group_anagram(words):
    mp = {}

    for w in words:
        key = "".join(sorted(w))
        if key in mp:
            mp[key].append(w)
        else:
            mp[key] = [w]

    return list(mp.values())

words = input("Enter the words : ").split()
print("Groups :",group_anagram(words))