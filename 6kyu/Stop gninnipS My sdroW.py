def spin_words(sentence):
    words = sentence.split(" ")
    new_sentence = ""
    for i in range(len(words)):
        if len(words[i]) >= 5:
            new_sentence += words[i][::-1] + " "
        else:
            new_sentence += words[i] + " "

    return new_sentence.strip()
