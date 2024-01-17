# -*- coding: utf-8 -*-
import MeCab
import correct as cr

sentence = "答えは犬ですか？"
answer = "犬"

tagger = MeCab.Tagger()
figure = tagger.parse(sentence).split("\n")
norm = []
for i in figure:
    if '名詞' in i:
        lis = i.split(" ")[0]
        norm.append(lis.split('\t')[0])

deta = []
for i in range(len(norm)):
    deta.append(cr.main(answer, norm[i]))

print(max(deta))