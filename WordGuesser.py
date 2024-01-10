import use_chatgpt.chatgpt as chatgpt
import correct as cr
import tkinter as tk
import tkinter.ttk as ttk
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

class Scene:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("WordGuesser")
        self.root.withdraw()
        self.ScreenSize = (self.root.winfo_screenwidth()//2,self.root.winfo_screenheight()//2)
        self.ScreenOfset = (self.root.winfo_screenwidth() // 2 - self.ScreenSize[0] // 2, self.root.winfo_screenheight() // 2 - self.ScreenSize[1] // 2)
        self.root.geometry(f"{self.ScreenSize[0]}x{self.ScreenSize[1]}+{self.ScreenOfset[0]}+{self.ScreenOfset[1]}")
    
    def next_window(self, next_scene):
        self.root.destroy()
        next_scene.root.deiconify()

class TitleScene(Scene):
    def __init__(self, next_scene):
        super().__init__()
        self.root.deiconify()
        self.FrameTitle = tk.Frame(self.root)
        self.FrameAccount = tk.Frame(self.FrameTitle)
        self.FramePassword = tk.Frame(self.FrameTitle)
        self.LabelAccount = ttk.Label(self.FrameAccount, text='アカウント名：')
        self.EntryAccount = ttk.Entry(self.FrameAccount)
        self.LabelAccount.grid(row=0, column=0)
        self.EntryAccount.grid(row=0, column=1)
        self.LabelPassword = ttk.Label(self.FramePassword, text='パスワード：')
        self.EntryPassword = ttk.Entry(self.FramePassword, show="*")
        self.LabelPassword.grid(row=0, column=0)
        self.EntryPassword.grid(row=0, column=1)
        self.ButtonNext = ttk.Button(self.FrameTitle, text='ゲームスタート!!', command=lambda: self.next_window(next_scene))
        self.ButtonQuitGame = ttk.Button(self.FrameTitle, text='終了', command=self.root.destroy)
        self.FrameAccount.pack(pady=10)
        self.FramePassword.pack(pady=10)
        self.ButtonNext.pack(pady=10)
        self.ButtonQuitGame.pack(pady=10)
        self.FrameTitle.pack(expand=True)

    def next_window(self, next_scene):
        print(f"アカウント：{self.EntryAccount.get()}")
        print(f"パスワード：{self.EntryPassword.get()}")
        super().next_window(next_scene)

class SelectScene(Scene):
    def __init__(self, next_scene):
        super().__init__()
        # 文字を大きくする
        self.Label = ttk.Label(self.root, text='ジャンルを選んでください')
        self.Label.pack(expand=True)
        self.Button_1 = ttk.Button(self.root, text='スポーツ', command=lambda: self.next_window(next_scene, genre='スポーツ'))
        self.Button_1.pack(expand=True)
        self.Button_2 = ttk.Button(self.root, text='食べ物', command=lambda: self.next_window(next_scene, genre='食べ物'))
        self.Button_2.pack(expand=True)
        self.Button_3 = ttk.Button(self.root, text='動物', command=lambda: self.next_window(next_scene, genre='動物'))
        self.Button_3.pack(expand=True)

    def next_window(self, next_scene, genre):
        next_scene.GuessWord = generate_random_word(genre)
        print(next_scene.GuessWord)
        super().next_window(next_scene)

class TalkingScene(Scene):
    def __init__(self):
        super().__init__()
        self.flag = False
        self.chatgpt_obj = chatgpt.ChatGPT()

        self.Canvas = tk.Canvas(self.root)
        self.FrameMessamge = tk.Frame(self.root)
        self.FrameTalking = tk.Frame(self.Canvas)
        
        self.Scrollbar = tk.Scrollbar(self.Canvas, orient=tk.VERTICAL, command=self.Canvas.yview)
        self.Canvas.configure(scrollregion=(0, 0, 900, 90000))
        self.Canvas.configure(yscrollcommand=self.Scrollbar.set)
        
        self.LabelMessage = ttk.Label(self.FrameMessamge, text='メッセージ')
        self.TextMessage = tk.StringVar()
        self.EntryMessage = ttk.Entry(self.FrameMessamge, textvariable=self.TextMessage)
        self.ButtonSendMessage = ttk.Button(self.FrameMessamge, text='送信', command=lambda: self.send_message())
        self.ButtonClearMessage = ttk.Button(self.FrameMessamge, text='クリア', command=lambda: self.clear_message())
        self.ButtonQuitGame = ttk.Button(self.FrameMessamge, text='終了', command=self.root.destroy)
        # Layout
        self.LabelMessage.grid(row=0, column=0)
        self.EntryMessage.grid(row=0, column=1)
        self.ButtonSendMessage.grid(row=1, column=0)
        self.ButtonClearMessage.grid(row=1, column=1)
        self.ButtonQuitGame.grid(row=1, column=2)

        self.FrameMessamge.pack()
        self.FrameTalking.pack()
        
        self.Scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.Canvas.pack(expand=True, fill=tk.BOTH)
        
        self.Canvas.create_window((0, 0), window=self.FrameTalking, anchor="nw", width=self.ScreenSize[0], height=90000)
    
    def send_message(self):
        if not self.flag:
            similarity_score = cr.calculate_similarity(self.GuessWord, self.TextMessage.get())
            if similarity_score is not None:
                similarity = round(similarity_score*100)
                if similarity == 100:
                    self.flag = True
                    
            else:
                similarity = "???"

            if not self.flag:
                # AI return()
                self.odai = f'これから「{self.GuessWord}」について答えてください。ただし、回答の際、「{self.GuessWord}」という単語は出してはいけません。回答は「はい」か「いいえ」のみで答えてください。'
                question_list = []
                question = self.odai + self.TextMessage.get()
                question_list.append(question)
                answer_list = self.chatgpt_obj.ask_chatgpt(question_list)

            ttk.Label(self.FrameTalking, text=self.TextMessage.get(), wraplength=300).pack(anchor="w")
            if not self.flag:
                ttk.Label(self.FrameTalking, text = answer_list[0], wraplength=300).pack(padx=20, anchor="e")
            else:
                ttk.Label(self.FrameTalking, text = "正解！！", wraplength=300).pack(padx=20, anchor="e")
            ttk.Label(self.FrameTalking, text =f'類似度:{similarity}%', wraplength=300).pack()


    def clear_message(self):
        self.TextMessage.set('')

talking = TalkingScene()
select = SelectScene(next_scene = talking)
title = TitleScene(next_scene = select)
title.root.mainloop()
