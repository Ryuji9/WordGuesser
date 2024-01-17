# -*- coding: utf-8 -*-
import random

from gensim.models import KeyedVectors

import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KernelDensity

# Word2Vecモデルの読み込み
model_path = '/data1/takabayashi/example/class/create/entity_vector.model.bin'  # モデルのパスを指定
word2vec_model = KeyedVectors.load_word2vec_format(model_path, binary=True)

# サンプルとして使用する単語のペア数
sample_size = 10000

# 類似度を計算する関数
def calculate_similarity(word1, word2):
    if word1 in word2vec_model and word2 in word2vec_model:
        similarity = word2vec_model.similarity(word1, word2)
        return similarity
    else:
        return None

#辞書中の単語リスト
words = list(word2vec_model.index_to_key)

#類似度のサンプリング
similarities = []
for _ in range(sample_size):
    word1, word2 = np.random.choice(words, size=2, replace=False)
    similarities.append(calculate_similarity(word1, word2))

# リストに類似度が追加された後は、次のように確率密度関数を推定
similarities = np.array(similarities).reshape(-1, 1)
kde = KernelDensity(kernel='gaussian', bandwidth=0.5).fit(similarities)

# 確率密度関数の作成
x = np.linspace(-1, 1, 1000)[:, np.newaxis]
log_dens = kde.score_samples(x)
dens = np.exp(log_dens)

# 結果のプロット
plt.figure(figsize=(8, 6))
plt.plot(x, dens, label='Estimated Density')
plt.xlabel('Similarity')
plt.ylabel('Density')
plt.title('Estimated Probability Density Function')
plt.legend()
plt.show()