def longest_substring(s):
    res_set=[]
    result=0
    l=0
    for i in range(0,len(s)):
        while s[i] in res_set:
            res_set.remove(s[l])
            l+=1
        res_set.append(s[i])
        result=max(result,i-l+1)
    return result

s="abcabcabb"
print(longest_substring(s))


