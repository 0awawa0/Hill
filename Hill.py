import Matrix

class Hill:

    # Алфавит
    symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\]^_`" \
              " АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя"
    # Размер алфавита
    size = len(symbols)

    # Алгоритм Евклида для поиска обратного элемента в кольце по модулю
    @staticmethod
    def gcd(a, b):
        if b == 0:
            return {"x": 1, "y": 0, "reminder": a}
        else:
            answer = Hill.gcd(b, a % b)
            x = answer["x"]
            y = answer["y"]
            d = answer["reminder"]
            ret = {"reminder": d, "x": y, "y": x - a // b * y}
            return ret
    
    # Функция для установки ключа
    def setKeyword(self, keyword):

        self.block_size = 0
        for i in range(len(keyword)):
            if i**2 == len(keyword):
                self.block_size = i
                break
        if self.block_size == 0:
            return False

        self.key = Matrix.Matrix(self.block_size, self.block_size)
        for i in range(self.block_size):
            for j in range(self.block_size):
                self.key[i][j] = Hill.symbols.find(keyword[self.block_size*i + j])
        
        obr_det = Hill.gcd(self.key.determinant(), self.size)["x"] % self.size
        self.obr_key = (self.key.algebDop().transp() * obr_det) % self.size
        return True
    
    # Функция расшифровки
    def encrypt(self, plain_text):

        while len(plain_text) % self.block_size != 0:
            plain_text += " "
        
        cipher_text = []
        for i in range(len(plain_text)//self.block_size):
            cipher_text.append(Matrix.Matrix(1, self.block_size))
            for j in range(self.block_size):
                cipher_text[i][0][j] = Hill.symbols.find(plain_text[self.block_size * i + j])
        
        for i in range(len(cipher_text)):
            cipher_text[i] = (cipher_text[i] * self.key) % self.size
        
        result = ""

        for i in range(len(cipher_text)):
            for j in range(self.block_size):
                result += Hill.symbols[cipher_text[i][0][j]]
        return result
    
    def decrypt(self, cipher_text):

        plain_text = []
        for i in range(len(cipher_text)//self.block_size):
            plain_text.append(Matrix.Matrix(1, self.block_size))
            for j in range(self.block_size):
                plain_text[i][0][j] = Hill.symbols.find(cipher_text[self.block_size * i + j])


        for i in range(len(plain_text)):
            plain_text[i] = (plain_text[i] * self.obr_key) % self.size
        
        result = ""

        for i in range(len(plain_text)):
            for j in range(self.block_size):
                result += Hill.symbols[plain_text[i][0][j]]
        return result

    @staticmethod
    def test():
        h = Hill()
        keyword = input("Введите ключ (длина равна квадрату целого числа): ")
        h.setKeyword(keyword)
        text = input("Введите текст для шифрования: ")
        text = h.encrypt(text)
        print("Шифротекст: " + text)
        text = h.decrypt(text)
        print("Открытый текст: " + text)



if __name__ == "__main__":
    Hill.test()