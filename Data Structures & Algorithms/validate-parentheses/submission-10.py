class Solution:
    def isValid(self, s: str) -> bool:  #s = "([{}])"

        
        dicti = {'}':'{', 
                ']':'[', 
                ')':'('}
        
        store = []

        for c in s:
            if c in dicti:  # '}' in dic ?
                if store and store[-1] == dicti[c]:  # '}' == '}'
                    store.pop()

                else: # '}' not equal to the dict[c] , so paranthesis is not is order
                    return False
            # c is not in the dicti

            else:
                store.append(c)  # --> '(' appended to the store , '[' , then 
                # '{'--> store = ['(' , '[' , '{']
            

        return True if not store else False
                