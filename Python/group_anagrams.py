# this function holds the operation of finding the number of  group of anagrams found
def group_anagram(words):
    mp = {} # to store the anagrams with words

    for w in words:
        key = "".join(sorted(w)) # sorted so the problem is simplified 
        if key in mp:
            mp[key].append(w) # if already there add the new word with that
        else:
            mp[key] = [w] # else add the new word to list 

    return list(mp.values())
# custom input 
words = input("Enter the words : ").split()
print("Groups :",group_anagram(words))