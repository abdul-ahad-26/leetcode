from collections import Counter

def selectionSort(arr):
          
    
    for i in range(len(arr)):
        smallest_index = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
                

        

        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False

        # countS, countT = {}, {}

        # for i in range(len(s)):
        #     countS[s[i]] = 1 + countS.get(s[i], 0)
        #     countT[t[i]] = 1 + countT.get(t[i], 0)

        # for c in countS:
        #     if countS[c] != countT.get(c):
        #         return False

        # return True

        # method 2
        # return Counter(s) == Counter(t)

        # method 3
        # return sorted(s) ==  sorted(t)

        # method 4

        return selectionSort(list(s)) == selectionSort(list(t))

        
s = Solution()
print(s.isAnagram("anagram", "nagaram"))
