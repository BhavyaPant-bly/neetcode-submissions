class Solution:

    def encode(self, strs: List[str]) ->str:
        if (strs == []):
            return "None"
        for i in range(len(strs)):
            new_str = ""

            for j in range(len(strs[i])):
                new_str += chr((~(ord(strs[i][j])) + 1)%256)

            strs[i] = new_str

        return '|'.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "None":
            return []
        return [
            ''.join((chr((~(ord(ch) - 1)%256))) for ch in word)
            for word in s.split('|')
        ]
