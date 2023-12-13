import random

# ジャンルごとの単語リスト
genres = {
    'スポーツ': ['サッカー', '野球', 'テニス', 'バスケットボール', 'ゴルフ'],
    '食べ物': ['寿司', 'ラーメン', 'ピザ', '富士山', '焼肉'],
    '動物': ['キリン', 'シマウマ', 'ライオン', '犬', '猫'],
    }

#ジャンルからランダムに単語を返す関数
def generate_random_word(genre):
    words = genres[genre]
    random_word = random.choice(words)
    return random_word

#ジャンルを選択
number=int(input("ジャンルを選んでください(1.スポーツ 2.食べ物 3.動物):"))

# ジャンルを指定
if number == 1:
    selected_genre = 'スポーツ'
elif number == 2:
    selected_genre = '食べ物'
elif number == 3:
    selected_genre = '動物'
else:
    print('正しい数字を入力してください')
 
# ランダムな単語を生成
random_word = generate_random_word(selected_genre)
    
#ジャンルから単語を生成    
if number == 1:
    print(f"{selected_genre}:{random_word}")
elif number == 2:
    print(f"{selected_genre}:{random_word}")
else:
    print(f"{selected_genre}:{random_word}")
