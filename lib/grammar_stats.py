# user_string => "Hello! There! Friend!"
# percentage good => 100%
# check with more than one text input

# if 3 of 4 texts entered are valid => 75%
import string

class GrammarStats():
    def __init__(self):
        pass

    def check(self, text):
        self.text = text
        capital = text[0]
        last_letter = text[-1]
        punctuation = string.punctuation
        hasPunc = False
        for char in punctuation:
            if last_letter == char:
                hasPunc = True
        if (capital.isupper() and hasPunc):
            return True
        else:
            return False
        
    def percentage_good(self):
        list = []
        i = 0
        percentage = 0.0
        sentence = self.text.split(" ")
        capital = sentence[0]
        last_letter = sentence[-1]
        punctuation = string.punctuation
        for word in sentence:
            if word[0].isupper() and word[-1] == punctuation:
            #if (capital.isupper() and last_letter == punctuation):
                i += 1
                #list.append(word)
                print(len(list) + "here")                       
        percentage =  i / len(sentence) 
        print(percentage)
            

        return percentage * 100

grammar = GrammarStats()
grammar.check("Hello! There! Friend!")
grammar.percentage_good()

# vanessafcosta