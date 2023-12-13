# -*- coding: utf-8 -*-
from gensim.models import KeyedVectors

# Word2Vecモデルの読み込み
model_path = 'C:\\Users\\ctwj0154\\Desktop\\entity_vector.model.bin'  # モデルのパスを指定
word2vec_model = KeyedVectors.load_word2vec_format(model_path, binary=True)

# 類似度を計算する関数
def calculate_similarity(word1, word2):
    if word1 in word2vec_model and word2 in word2vec_model:
        similarity = word2vec_model.similarity(word1, word2)
        return similarity
    else:
        return None

# 類似度を計算する(cos:-1~1)
while True:
    print("入力待ち")
    word1 = input()

    if word1 == "finish": break

    print("入力待ち")
    word2 = input()

    similarity_score = calculate_similarity(word1, word2)

    if similarity_score is not None:
        print(f"「{word1}」と「{word2}」の類似度は: {similarity_score}")
    else:
        print("単語がモデルに存在しません")

