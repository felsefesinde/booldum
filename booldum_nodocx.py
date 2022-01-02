# -*- coding: utf-8 -*-
"""
@author: Burak Alanyalıoğlu
GitHub: @felsefesinde
Instagram: @felsefesinde
YouTube: Felsefesinde
Twitter: @felsefesinde & @binichburak

@author: Berkay Gündüz
Github: @berkaygunduzz
Instagram: berkay.gz

"""


class Booldum:
    """
    A class which represents Booldum app

    ...

    Attributes
    ----------
    __text : str
        text to be corrected
    __corrected_words_file : file
        a file that contains corrected words
    __correct_words : list
        a list that contains coreect words
    __wrong_words_file : file
        a file that contains wrong words
    __correct_words : list
        a list that contains wrong words

    Methods
    -------
    __word_in_text(word)
        Returns desired word in a part of text
    __set_words()
        Set word lists by word files
    change_wrong_words()
        Correct wrong words if user wants to change
    __write_txt()
        Create a .txt file that contains text
    write_edited_text()
        Create a folder that contains text and print the text
    get_tect()
        Returns text
    exit()
        Exits app
    """

    def __init__(self):
        self.__text = ""
        self.__corrected_words_file = open("correct_words.txt", "r")
        self.__correct_words = []
        self.__wrong_words_file = open("wrong_words.txt", "r")
        self.__wrong_words = []
        self.__set_words()

    def __word_in_text(self, word):
        """Returns desired word in a part of text

        Parameters
        ----------
        word : str
            Desired word to be return in text
        """
        length = len(word)
        position = self.__text.find(word)
        new_text = self.__text[position:position + length + 15]
        return new_text

    def __set_words(self):
        """Set word lists by word files
        """
        for corrected_word in self.__corrected_words_file:
            self.__correct_words.append(corrected_word[:-1])

        for wrong_word in self.__wrong_words_file:
            self.__wrong_words.append(wrong_word[:-1])

    def change_wrong_words(self):
        """Correct wrong words if user wants to change
        """
        print("Booldum uygulamasına hoş geldiniz!")
        self.__text = input("Lütfen metninizi giriniz: ")
        for wrong_word in self.__wrong_words:
            wrong_word_index = self.__text.find(wrong_word)
            if wrong_word_index > 0:
                change = input(f"Metninizde geçen '{wrong_word}'\n" +
                                "ifadesinin şapka ile yazılıp " +
                                "yazılmayacağını kontrol ediniz.\n" +
                                "Metindeki yeri şu şekilde:" +
                               f"'...{self.__word_in_text(wrong_word)}...'\n" +
                                "Gerekli değişiklik yapılsın mı? " +
                                "[Evet: e | Hayır: h]: ")
                try:
                    if change.upper() == "E":
                        wrong_word_index = self.__wrong_words.index(wrong_word)
                        correct_word = self.__correct_words[wrong_word_index]
                        edited = self.__text.replace(wrong_word, correct_word)
                        self.__text = edited
                    elif change.upper() == "H":
                        print(f"Kelime '{wrong_word}' aynı bırakıldı!")
                    else:
                        raise(IndexError(f"Geçersiz işlem komutu: {change}"))
                except IndexError as e:
                    print("İşlem atlandı!")
                    print(f"Kelime '{wrong_word}' aynı bırakıldı!")

    def __write_txt(self):
        """Create a .txt file that contains text
        """
        with open("Booldum_Metin.txt", "w", encoding="utf-8") as edited:
            edited.write(self.__text)

    def write_edited_text(self):
        """Create a folder that contains text and print the text
        """
        self.__write_txt()
        print(f"İşte metninizdeki şapka hatalarının Booldum tarafından " +
               "düzeltilmiş hâli:\n" +
              f"{self.__text}")

    def get_text(self):
        """Returns text
        """
        return self.__text

    def exit(self):
        """Exits app
        """
        self.__corrected_words_file.close()
        self.__wrong_words_file.close()
        input("Kapatmak için Enter tuşuna basınız...")

if __name__ == "__main__":
    booldum = Booldum()
    booldum.change_wrong_words()
    booldum.write_edited_text()
    booldum.exit()

