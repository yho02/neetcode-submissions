class Solution:

    def encode(self, strs: List[str]) -> str:
        return_str = ""
        for string in strs:
            length = str(len(string))
            return_str += length
            return_str += "#"
            return_str += string
        return return_str

    def decode(self, s: str) -> List[str]:
        # use index, do not manipulate s 
        # every length comes with a #
        # then when it times for slicidng, always increment + 1 account for #
        # length is a string 
        index = 0 
        length = ""
        return_strings = []
        while index < len(s):
            while s[index].isdigit():
                length += s[index]
                index += 1
                # when it hits #, while will stop here
            # once it stop
            index += 1 # to account for the #
            # string starts here
            return_strings.append(s[index:index+int(length)]) 
            index += int(length)
            length = ""
        return return_strings   


