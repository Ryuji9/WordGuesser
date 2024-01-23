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
        similarity = cr.calculate_similarity(answer, norm[i])
        if similarity is not None:
            deta.append(similarity)

    return max(deta) if len(deta)!=0 else None

# print(PickKeyword("答えは犬ですか？", "犬"))