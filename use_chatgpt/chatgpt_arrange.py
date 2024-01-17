import pyautogui as pag
from time import sleep
import subprocess
import pyperclip

class ChatGPT:
    #画像データ
    STOP_IMG = 'C:/image_list/stop-image.png'
    SAVE_IMG = 'C:/image_list/save-chatgpt-icon.png'
    CLIP_IMG = 'C:/image_list/clipboard-icon.png'
    SEND_IMG = 'C:/image_list/send-message-form-ja2.png'
    LMCSS_IMG = 'C:/image_list/launch-magic-css-icon.png'
    CSSCIOSE_IMG = 'C:/image_list/lmc-close.png'

    #定数
    CHROME_START_CMD = r'chrome.exe' #chrome起動コマンド
    CHATGPT_URL = 'https://chat.openai.com/' #ChatGPTのURL
    SAVE_CHATGPT_SEPARETOR1 = 'ChatGPT:' # Save ChatGPTで使われている区切り文字その１
    SAVE_CHATGPT_SEPARETOR2 = '------------------' # Save ChatGPTで使われている区切り文字その２
    INPUT_KEY_SLEEP_SEC = 1 # キーボード入力後の待機秒数

    #ある画像が出力されるまで待機する関数
    def wait_detecting_image(self, image_file_path, confidence_param):
        is_detected = False

        if confidence_param is None:
            confidence_param = 0.7
        
        for tryCount in range(300):
            print(tryCount)
            try:
                p = pag.locateOnScreen(image_file_path, confidence = confidence_param)
                if p:
                    is_detected = True
                    #print('detected:' + str(tryCount))
                    break
            except Exception as e:
                print(e)
                pass
            sleep(1)
        return is_detected, p

    #ChatGPTをウェブブラウザ経由で操作する関数
    def ask_chatgpt(self, question_list):

        answer_list = []

        #chrome起動
        subprocess.Popen(['start', self.CHROME_START_CMD], shell=True)
        sleep(self.INPUT_KEY_SLEEP_SEC)
        pag.hotkey('ctrl', 'l')
        sleep(self.INPUT_KEY_SLEEP_SEC)
        pag.hotkey('ctrl', 'a')
        sleep(self.INPUT_KEY_SLEEP_SEC)
        pyperclip.copy(self.CHATGPT_URL)
        pag.hotkey('ctrl', 'v')
        sleep(self.INPUT_KEY_SLEEP_SEC)
        pag.press('enter')
        sleep(self.INPUT_KEY_SLEEP_SEC)

        #対話非表示
        is_detected, p = self.wait_detecting_image(self.LMCSS_IMG, 0.8)
        x, y = pag.center(p)
        pag.click(x, y)
        sleep(self.INPUT_KEY_SLEEP_SEC)

        is_detected, p = self.wait_detecting_image(self.CSSCIOSE_IMG, 0.8)
        x, y = pag.center(p)
        pag.click(x, y)
        sleep(self.INPUT_KEY_SLEEP_SEC)

        #質問
        question_num = 0
        for que in question_list:
            #ChatGPTの質問フォームをフォーカス
            is_detected, p = self.wait_detecting_image(self.SEND_IMG, 0.8)
            x, y = pag.center(p)
            pag.click(x, y)
            sleep(self.INPUT_KEY_SLEEP_SEC)
            
            #ChatGPTにメッセージ送信
            pyperclip.copy(que)
            pag.hotkey('ctrl', 'v')
            sleep(self.INPUT_KEY_SLEEP_SEC)

            pag.press('enter')
            sleep(self.INPUT_KEY_SLEEP_SEC)

            #print("第零段階")

            #GPTの回答が終わるまで待機
            is_detected, p = self.wait_detecting_image(self.STOP_IMG, 0.8)

            #print("第一段階")

            #GPTの回答をクリップボードに格納
            is_detected, p = self.wait_detecting_image(self.SAVE_IMG, 0.8)
            x, y = pag.center(p)
            pag.click(x, y)
            sleep(self.INPUT_KEY_SLEEP_SEC)

            #print("第二段階")

            is_detected, p = self.wait_detecting_image(self.CLIP_IMG, 0.7)
            x, y = pag.center(p)
            pag.click(x, y)

            chatgpt_answer = pyperclip.waitForPaste()

            #クリップボードの回答を整形
            shaped_answer = chatgpt_answer.split(self.SAVE_CHATGPT_SEPARETOR1)[question_num + 1].strip().split(self.SAVE_CHATGPT_SEPARETOR2)[0].strip()
            answer_list.append(shaped_answer)
            question_num += 1

            #Save ChatGPTを閉じる
            pag.press('escape')
            sleep(self.INPUT_KEY_SLEEP_SEC)

            

        """
        #Chromeを閉じる
        pag.keyDown('shift')
        pag.keyDown('ctrl')
        pag.press('w')
        pag.keyUp('shift')
        pag.keyUp('ctrl')
        """
        sleep(self.INPUT_KEY_SLEEP_SEC)
        pag.hotkey('shift', 'ctrl', 'w')
        sleep(self.INPUT_KEY_SLEEP_SEC)

        print("回答ゲット")

        return answer_list