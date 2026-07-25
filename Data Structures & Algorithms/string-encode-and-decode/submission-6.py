class Solution:

    def encode(self, strs: List[str]) -> str:

        # to encode , first we print the len(str) then a delimitter # , then the str

        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res


    def decode(self, s: str) -> List[str]:

        res , i = [] , 0 # res for storing the final list of strings in a decoded way and i is the outer pointer

        while i < len(s):

            j = i # initially be i
            while s[j] != '#': #after # only the actual string starts so , increment j 
                                 

                j += 1  # incrementing j ,  funtil we find the #

                # now we want to find from which index or which indices belong to word  , we want to decode 
                 
            length = int(s[i:j]) # 0: "4" , 1 : # (str slicing happens so the res is int 4)
                
            res.append(s[j+1: j+1+length])# this line shows , starts from after the deliitter
                # and stops at j+1 + the lengthe (2+4) "4#neet" or (2+ 5) "5#hello" , so stops at 5 and 6 -> 
            i = j + 1 + length# this line is responsible for moving the i pointer to the next word
        return res



