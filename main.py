import tkinter
from tkinter import messagebox
import Hill

class Window(tkinter.Frame):

    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.initUI()

    def btnKeyClicked(self):
        keyword = self.entryKey.get()
        result = self.cipher.setKeyword(keyword)
        if result == True:
            self.buttonEncrypt["state"] = "active"
            self.buttonDecrypt["state"] = "active"
        else:
            tkinter.messagebox.showerror(title="Ошибка при задании ключа", message="Ключ не соответсвует требованиям.\n" +
            "1. Длина ключевого слова должна быть равна квадрату целого числа\n2. Все символы ключевого слова должны присутствовать в алфавите\n" + 
            "Алфавит: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\]^_`АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя")

    
    def btnEncryptClicked(self):
        plain_text = self.entryIn.get()
        plain_text = self.cipher.encrypt(plain_text)
        self.entryOut.delete(0, 'end')
        self.entryOut.insert(0, plain_text)
    
    def btnDecryptClicked(self):
        cipher_text = self.entryIn.get()
        cipher_text = self.cipher.decrypt(cipher_text)
        self.entryOut.delete(0, 'end')
        self.entryOut.insert(0, cipher_text)
        

    def initUI(self):
        self.cipher = Hill.Hill()
        self.parent.title("Шифр Хилла")
        self.grid(column=0, row=0)
        self.labelKey = tkinter.Label(text="Ключ")
        self.labelKey.grid(column=1, row=0)
        self.entryKey = tkinter.Entry()
        self.entryKey.grid(column=1, row=1)
        self.btnKey = tkinter.Button(text="Задать ключ", command=self.btnKeyClicked)
        self.btnKey.grid(column=1, row=2)
        self.textIn = tkinter.Label(text="Входной текст")
        self.textIn.grid(column=1, row=3)
        self.entryIn = tkinter.Entry()
        self.entryIn.grid(column=1, row=4)
        self.buttonEncrypt = tkinter.Button(text="Зашифровать", command=self.btnEncryptClicked, state='disabled')
        self.buttonDecrypt = tkinter.Button(text="Расшифровать", command=self.btnDecryptClicked, state='disabled')
        self.buttonDecrypt.grid(column=1, row=5)
        self.buttonEncrypt.grid(column=2, row=5)
        self.textOut = tkinter.Label(text="Выходной текст")
        self.textOut.grid(column=1, row=6)
        self.entryOut = tkinter.Entry()
        self.entryOut.grid(column=1, row=7)
    

if __name__ == "__main__":
    root = tkinter.Tk()
    root.geometry("300x300+300+300")
    app = Window(root)
    root.mainloop()
