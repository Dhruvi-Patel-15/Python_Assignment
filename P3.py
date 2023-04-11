def group_anagrams(strs):
    anagram_dict = {}
    for s in strs:
        sorted_s = "".join(sorted(s))
        if sorted_s in anagram_dict:
            anagram_dict[sorted_s].append(s)
        else:
            anagram_dict[sorted_s] = [s]
    return list(anagram_dict.values())
    
if __name__ == "__main__":
    try:
        strs =eval(input("Enter the arrays of strings : "))
        if 1 >= len(strs)>= 104 :
            raise ValueError("Error")
        for s in strs:
            if 0 >= len(s) >= 100 :
                raise ValueError("Invalid Input:String Length out of range")
            if not s.islower() and s!="":
                raise ValueError("Invalid Input : String should be in lower case")
            
        ans  = group_anagrams(strs)
        print("An Group of Anagrams are : ",ans)
    except Exception as e:
        print("Error: {}".format(str(e)))