import os
import sys
import chatgpt

#ChatGPTクラスのインスタンスを作成
chatgpt_obj = chatgpt.ChatGPT()
"""
#質問リスト
question_list = ['食べられる？', 'それはイルカ？']
"""

#お題
odai = 'これから「イルカ」について答えてください。ただし、回答の際、「イルカ」という単語は出してはいけません。回答は「はい」か「いいえ」のみで答えてください。'

#質問
while True:
    question_list = []
    question = input('質問＞')
    question = odai + question
    question_list.append(question)

    #main文開始
    #ChatGPTと質疑応答
    answer_list = chatgpt_obj.ask_chatgpt(question_list)

    #回答表示
    print(answer_list[0])
