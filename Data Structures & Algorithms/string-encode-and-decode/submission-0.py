class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)
        # strs = ["Hello","World"]
        # "5#Hello5#World"

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = s.index("#", i) # 1
            length = int(s[i:j]) # 0:1 -> 5
            start = j + 1 # 2
            res.append(s[start:start+length]) #s[2:7] -> 2~6
            i = start + length # 7
        return res
