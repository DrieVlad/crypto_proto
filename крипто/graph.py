import re
import time

file_in = open("in.txt", "r")

file_out = open("2.txt", "w")

alph_in = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
        "v", "w", "x", "y", "z", ".", ",", "!", "?"]
alph_out = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т",
            "у", "ф", "х", "ц", "ч", "ш", "щ", "э", "ю", "ъ", "ь", "я"]

text_in = file_in.read()
text_in = text_in.lower()
for i in range(30):

    text_in = text_in.replace(alph_in[i], alph_out[i])

file_out.write(text_in)

file_in.close()
file_out.close()
