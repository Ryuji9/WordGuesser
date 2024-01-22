# -*- coding: utf-8 -*-
import MeCab
import correct as cr

def PickKeyword(sentence, answer):
    tagger = MeCab.Tagger()
    figure = tagger.parse(sentence).split("\n")
    norm = []
    for i in figure:
        if '名詞' in i:
            lis = i.split(" ")[0]
            norm.append(lis.split('\t')[0])

    deta = []
    for i in range(len(norm)):
        deta.append(cr.calculate_similarity(answer, norm[i]))

    return max(deta)

# print(PickKeyword("答えは犬ですか？", "犬"))