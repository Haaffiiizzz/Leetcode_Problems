def longestPalindrome(s: str) -> str:
        if len(s) == 1:
            return s
        if len(set(s)) == 1:
            return s
        
        
        
        
        def isPalindrome(word):
            reversedWord = word[::-1]
            return word == reversedWord
        
        
        def getSubstrings(word):
            longestCount = 0
            longestPalindrome = ""
            
            for i in range(0, len(word)):
                
                for j in range(1, len(word)+1):
                    if j - i < longestCount:
                        continue
                    newWord = word[i:j]
                    print("newword", newWord)
                    if isPalindrome(newWord):
                        longestCount = len(newWord)
                        if longestCount == len(word):
                            return newWord
                        print("palindrome", newWord)
                        longestPalindrome = newWord
            return longestPalindrome
                        
            
        return getSubstrings(s)
        
print("l0ngest", longestPalindrome("jaliztdispcppzgzjxnjxwbhhtbjrijyibqwrhwuscmokylygielwssuyretqnoiglvsltmhetvdoliwibrnwmdtauczcswuqxxokaykslfzgxovphdptgtrbbozdkdgawcegemkumgbyqzjrzurkdaibfwwvcxfcstvixisrcfxvnlzizlbnacxssetlsxrvcaqvzmbnzdfmtskmxmjblzgpdsjvhqhrihiajvwxbmjsncjhmilercbdbzyncrnlyrxrefaeuttkscfttqnedzvqisclbremuxmngrpgqjqkijpizkixkrgaarpknivrrirbkeddkulvlfuetbdnugzodbfufqhrpkyufhrhnnnzsenkvqsuhlbaimniusuxsnmavqbilzgsfxjykrxdkkpnneikwlucdghnikojythrpgwyzoqgraycavrivsbfuaonssmryhcykooivrxmeeowllsfeyxrznvkdpobohpzolnpbxjjxbpnlozphobopdkvnzrxyefsllwoeemxrviookychyrmssnoaufbsvirvacyargqozywgprhtyjokinhgdculwkiennpkkdxrkyjxfsgzlibqvamnsxusuinmiablhusqvknesznnnhrhfuykprhqfufbdozgundbteuflvlukddekbrirrvinkpraagrkxikzipjikqjqgprgnmxumerblcsiqvzdenqttfcskttueaferxrylnrcnyzbdbcrelimhjcnsjmbxwvjaihirhqhvjsdpgzlbjmxmkstmfdznbmzvqacvrxsltessxcanblzizlnvxfcrsixivtscfxcvwwfbiadkruzrjzqybgmukmegecwagdkdzobbrtgtpdhpvoxgzflskyakoxxquwsczcuatdmwnrbiwilodvtehmtlsvlgionqteryusswleigylykomcsuwhrwqbiyjirjbthhbwxjnxjzgzppcpsidtzilaj"))
