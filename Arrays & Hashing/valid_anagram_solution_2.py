class Solution :
    def isAnagram(self, string_1: str, string_2: str) -> bool :
        if (len(s) != len(t)) :
            return False
        
        string_1_Dictionnary, string_2_Dictionnary = {}, {}

        for i in range (len)(string_2):
            string_1_Dictionnary[ string_1[i] ] = string_1_Dictionnary.get(string_1[i], 0) + 1
            string_2_Dictionnary[ string_2[i] ] = string_2_Dictionnary.get(string_2[i], 0) + 1
        
        return string_1_Dictionnary == string_2_Dictionnary
    
    