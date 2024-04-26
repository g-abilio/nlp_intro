import lib_plagiarism as plag

text1 = plag.first_input_text()
text2 = plag.second_input_text()

obj = plag.Similarities(text1, text2)

print(f"Text similarity: {obj.similarity()}")
print(f"Adjective similarity: {obj.similarity_adjectives()}")
print(f"Noun similarity: {obj.similarity_nouns()}")
print(f"Verb similarity: {obj.similarity_verbs()}")

if obj.is_plagiarism():
    print("There is probably an occurence of plagiarism!")
else:
    print("It's probably not an occurence of plagiarism!")