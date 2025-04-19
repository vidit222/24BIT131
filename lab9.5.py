def ispangram(sentence):
    alphabet_set = set("abcdefghijklmnopqrstuvwxyz")
    sentence_set = set(sentence.lower())
    return alphabet_set.issubset(sentence_set)

test_sentence1 = "The quick brown fox jumps over the lazy dog"
test_sentence2 = "Crazy Fredrick bought many very exquisite opal jewels"

print("Is the first sentence a pangram?", ispangram(test_sentence1))
print("Is the second sentence a pangram?", ispangram(test_sentence2))