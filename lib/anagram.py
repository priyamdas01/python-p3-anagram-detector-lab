class Anagram:

    def __init__(self, word):
        self.word = word

    def match(self, anagram_list):
        l = []
        for each_anagram in anagram_list:
            ll = sorted(list(each_anagram))
            llword = sorted(list(self.word))
            if (llword == ll):
                l.append(each_anagram)
            
        return l
            

