import tkinter as tk
import tkinter.ttk as ttk

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
        self.Button_1 = ttk.Button(self.root, text='ほげ', command=lambda: self.next_window(next_scene))
        self.Button_1.pack(expand=True)
        self.Button_2 = ttk.Button(self.root, text='ほが', command=lambda: self.next_window(next_scene))
        self.Button_2.pack(expand=True)
        self.Button_3 = ttk.Button(self.root, text='ほぐ', command=lambda: self.next_window(next_scene))
        self.Button_3.pack(expand=True)

class TalkingScene(Scene):
    def __init__(self):
        super().__init__()
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
        ttk.Label(self.FrameTalking, text=f'{self.TextMessage.get()}', wraplength=300).pack(anchor="w")
        # AI return()
        ttk.Label(self.FrameTalking, text='AI ターン', wraplength=300).pack(padx=20, anchor="e")
        ttk.Label(self.FrameTalking, text='類似度:???%', wraplength=300).pack()

    def clear_message(self):
        self.TextMessage.set('')

talking = TalkingScene()
select = SelectScene(next_scene = talking)
title = TitleScene(next_scene = select)
title.root.mainloop()
