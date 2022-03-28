def decrypt(sentences):
    plaintext = "the quick brown fox jumps over the lazy dog"
    n = len(plaintext)
    match = None
    for sentence in sentences:
        if len(sentence) == n:
            match = sentence
    mapping = {key: value for key, value in zip(match, plaintext)}
    for sentence in sentences:
        decrypted_text = ""
        for char in sentence:
            decrypted_text += mapping[char]
        print(decrypted_text)


sentence1 = "vtz ud xnm xugm itr pyy jttk gmv xt otgm xt xnm puk ti xnm fprxq"
sentence2 = "xnm ceuob lrtzv ita hegfd tsmr xnm ypwq ktj"
sentence3 = "frtjrpgguvj otvxmdxd prm iev prmvx xnmq"
sentences = [sentence1, sentence2, sentence3]
decrypt(sentences)
