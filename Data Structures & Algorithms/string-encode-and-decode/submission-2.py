class Solution:

    def encode(self, strs: List[str]) -> str:
        # encode by adding len and #
        encoded = ""
        for w in strs:
            encoded += str(len(w)) + "#" + w
        
        return encoded

    def decode(self, s: str) -> List[str]:

        #  4#Alok6#Shukla
        # take a decode list
        # while i is less that len s
        # j = i
        # while s[j] ! = # j++
        # length = s[i:j] because length can be 2, 3 digit as well, covert to int
        # append s[j+1:j+1+length]
        # i = j + 1 + length
        decoded = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            decoded.append(s[j+1:j+1+length])
            i = j + 1 + length
            
        return decoded