def firstUniqChar(s: str) -> int:
        char = set()
        index = len(s)-1
        for i in range(len(s)-1,-1,-1):
            print(s[i])
            if(s[i] not in char):
                index = i
                char.add(s[i])                
            print(char)
        return index
    
print(firstUniqChar('loveleetcode'))