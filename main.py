import tkinter
import Hill

class Window(tkinter.Frame):

    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.initUI()

    def btnKeyClicked(self):
        keyword = self.entryKey.get()
        self.cipher.setKeyword(keyword)
    
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
        self.buttonEncrypt = tkinter.Button(text="Зашифровать", command=self.btnEncryptClicked)
        self.buttonDecrypt = tkinter.Button(text="Расшифровать", command=self.btnDecryptClicked)
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
