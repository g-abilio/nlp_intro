import spacy 

# There is a big amount of possible language models.
# Here, we are going to use the en_core_web LLM

nlp = spacy.load("en_core_web_lg") 

# Defining the first and second input texts:

def first_input_text():
    print("Type in the first text:")
    first_text = input()
    return nlp(first_text)

def second_input_text():
    print("Type in the second text:")
    second_text = input()
    return nlp(second_text)

# Class that will calculate the similarities based
# on the LLM selected, as well as selecting the
# verbs, nouns and adjectives from each text. It
# will also apply a test for plagiarism.

class Similarities:
    def __init__(self, text1, text2):
        self.text1 = text1
        self.text2 = text2

    def similarity(self):
        return self.text1.similarity(self.text2)
    
    def verbs_text1(self):
        text1_verbs = " ".join([token.lemma_ for token in self.text1 if token.pos_ == "VERB"])
        return text1_verbs
    
    def adjectives_text1(self):
        text1_adjectives = " ".join([token.lemma_ for token in self.text1 if token.pos_ == "ADJ"])
        return text1_adjectives

    def nouns_text1(self):
        text1_nouns = " ".join([token.lemma_ for token in self.text1 if token.pos_ == "NOUN"])
        return text1_nouns
    
    def verbs_text2(self):
        text2_verbs = " ".join([token.lemma_ for token in self.text2 if token.pos_ == "VERB"])
        return text2_verbs
    
    def adjectives_text2(self):
        text2_adjectives = " ".join([token.lemma_ for token in self.text2 if token.pos_ == "ADJ"])
        return text2_adjectives

    def nouns_text2(self):
        text2_nouns = " ".join([token.lemma_ for token in self.text2 if token.pos_ == "NOUN"])
        return text2_nouns
    
    def similarity_verbs(self):
        verbs1 = nlp(self.verbs_text1())
        verbs2 = nlp(self.verbs_text2())
        return verbs1.similarity(verbs2)
    
    def similarity_nouns(self):
        nouns1 = nlp(self.nouns_text1())
        nouns2 = nlp(self.nouns_text2())
        return nouns1.similarity(nouns2)

    def similarity_adjectives(self):
        adjectives1 = nlp(self.adjectives_text1())
        adjectives2 = nlp(self.adjectives_text2())
        return adjectives1.similarity(adjectives2)
    
    def is_plagiarism(self):
        if self.similarity() > 0.965:
            return True
        else:
            return False

if __name__ == "__main__":
    print("A module for plagiarism detection.")