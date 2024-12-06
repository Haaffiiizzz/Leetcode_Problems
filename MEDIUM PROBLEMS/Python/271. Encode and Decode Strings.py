class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        encoded = ""
        for word in strs:
            new = word[::-1]
            encoded += new + "."
        return encoded

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        reversedString = s[::-1]
        decoded = reversedString[1:].split(".")
    
        return decoded[::-1]
