class Anagram:
    def __init__(self, word):
        self.word = word
        

    @property
    def word(self):
        return self._word 
    
    @word.setter 
    def word(self, word):
        self._word = word

    def match(self, list):
        word = self.word

        # is the word contained in the list
        letter_list = [letter for letter in word]
        sorted_letters = sorted(letter_list)
    
        print(sorted_letters)

        
        anagrams = []

        def matcher(word):
            tested_word = word
            words = [] 
            word_list = [letter for letter in word]
            words.append(sorted(word_list))

            for word in words:
                if sorted_letters == word:
                    anagrams.append(tested_word) 
                else:
                    pass    
                          
        
        for word in list:
            matcher(word)

        return anagrams