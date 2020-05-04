class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letter = {}
        flag = True
        for i in magazine:
            if(i in letter):
                letter[i] += 1
            else:
                letter[i] = 1
        print(letter)
        for i in ransomNote:
            if(i in letter and letter[i]>0):
                letter[i] -= 1
            else:
                flag = False
        return flag