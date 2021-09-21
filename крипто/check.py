import re
import time

file_in1 = open("in1.txt", "r")

file_in2 = open("in2.txt", "r")

alph_in = []
alph_out = []
text_in1 = file_in1.read()
text_in2 = file_in2.read()
dic = dict()
if len(text_in1) != len(text_in2):
    print("fake")
    exit(0)
else:
    for i in range(len(text_in1)):
        if (dic.get(text_in2[i]) != None):
            if text_in1[i] == text_in2[i]:
                continue
            else:
                print("fake")
                exit(0)
        else:
            dic.update({text_in2[i]: text_in1[i]})
print("ok")




file_in1.close()
file_in2.close()
