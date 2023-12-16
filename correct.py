# -*- coding: utf-8 -*-
from gensim.models import KeyedVectors
import csv


# Word2Vecモデルの読み込み
model_path = '/data1/takabayashi/example/class/create/entity_vector.model.bin'  # モデルのパスを指定
word2vec_model = KeyedVectors.load_word2vec_format(model_path, binary=True)


# csvファイルのパス
file_path = '/data1/takabayashi/example/class/create/probability_density_function.csv' # csvファイルのパスを指定


# 確率密度関数の読み込み
def read_csv_to_list(file_path):
    data = []
    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        header_skipped = False
        for row in csv_reader:
            if not header_skipped:
                header_skipped = True
                continue  # ラベル行をスキップ

            # 各行の要素を浮動小数点数に変換して追加
            float_row = [float(value) for value in row]
            data.append(float_row)
            transposed_data = list(map(list, zip(*data)))  # 転置して新しいリストを作成
    return transposed_data


# リストの中から近い値の場所をとる
def find_closest_number_index(numbers, target):
    closest_index = None
    min_difference = float('inf')  # 初期値として無限大を設定

    for i in range(len(numbers)):
        difference = abs(numbers[i] - target)
        if difference < min_difference:
            min_difference = difference
            closest_index = i

    return closest_index


# 類似度を計算する関数
def calculate_similarity(word1, word2):

    # csvファイルから確率密度関数を得る
    csv_data = read_csv_to_list(file_path)

    if word1 in word2vec_model and word2 in word2vec_model:
        similarity = word2vec_model.similarity(word1, word2)

        # 最も近い数値の位置を探す
        closest_index = find_closest_number_index(csv_data[0][:], similarity)

        probability = sum(csv_data[1][0:closest_index+1]) 
        return probability
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
        print(f"「{word1}」と「{word2}」の類似度は: {round(similarity_score*100)}%")
    else:
        print("単語がモデルに存在しません")