def isIsomorphic(p, s):
    mapPS, mapSP ={},{}

    for c1,c2 in zip(p,s.split()):

        if ((c1 in mapPS and mapPS[c1]!=c2)or (c2 in mapSP and mapSP[c2]!=c1)):
            return False
        
        mapPS[c1]=c2
        mapSP[c2]=c1
        
    return True

print(isIsomorphic('abba','dog cat frog dog'))


# def follows_pattern(p,s):
#     hashSP,hashPS = {},{}
#     for c1, c2 in zip(p,s.split()):
#         if ((c1 in hashSP and hashSP[c1] !=c2) or (c2 in hashPS and hashPS[c2] != c1)):
#             return False
    
#     hashSP[c1] = c2
#     hashPS[c2] = c1

#     return True

# print(follows_pattern('abba', 'dog cat cat '))