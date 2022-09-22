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

    def __init__(self) -> None:
        self.__text: str = ""
        self.__corrected_words_file_name: str = "correct_words.txt"
        self.__wrong_words_file_name: str = "wrong_words.txt"
        self.__correct_words: list[str] = []
        self.__wrong_words: list[str] = []
        self.__set_words()

    def __word_in_text(self, word_index: int, length: int) -> str:
        """Returns context around given index according to the length of the word.

        Parameters
        ----------
        word_index : int
            Desired word index to be returned

        length: int
            Length of the word
        """
        new_text = self.__text[word_index:word_index + length + 15]
        return new_text

    def __set_words(self) -> None:
        """Set word lists by word files
        """
        with open(self.__corrected_words_file_name, "r") as corrected_words_file:
            for corrected_word in corrected_words_file:
                self.__correct_words.append(corrected_word[:-1])

        with open(self.__wrong_words_file_name, "r") as wrong_words_file:
            for wrong_word in wrong_words_file:
                self.__wrong_words.append(wrong_word[:-1])

    def change_wrong_words(self) -> None:
        """Correct wrong words if user wants to change
        """
        print("Booldum uygulamasına hoş geldiniz!")

        # Metinde boş satır varsa çalışmıyor.
        self.__text = input("Lütfen metninizi giriniz:\n")

        # Burası bayağı değişti, pull requestte anlattığım nedenlerden ötürü.
        i = 0
        start = 0
        while i < len(self.__wrong_words):
            # Bu eklenti bugı tam düzeltmese de "Ankara" kelimesindeki "kar"ı bulmasını engelliyor.
            wrong_word = self.__wrong_words[i]
            wrong_word_index = self.__text.find(wrong_word, start)
            
            if wrong_word_index >= 0: # 1. kelime yanlış olunca oluşan bugı düzeltiyor.
                # Ankara kelimesindeki "kar" gibi kelimelerin okuyucuya sorulmadan elenmesi amaçlandı. 
                if wrong_word_index != 0 and self.__text[wrong_word_index - 1] not in [" ", "\t", "\n"]:
                    start = wrong_word_index + len(wrong_word)
                    continue
                change = input(f"Metninizde geçen '{wrong_word}'\n" +
                                "ifadesinin şapka ile yazılıp " +
                                "yazılmayacağını kontrol ediniz.\n" +
                                "Metindeki yeri şu şekilde:" +
                               f"'...{self.__word_in_text(wrong_word_index, len(wrong_word))}...'\n" +
                                "Gerekli değişiklik yapılsın mı? " +
                                "[Evet: e | Hayır: h]: ")
                try:
                    if change.upper() == "E":
                        correct_word = self.__correct_words[i]
                        self.__text = self.__text[:wrong_word_index] + correct_word + self.__text[(wrong_word_index + len(correct_word)):]
                    elif change.upper() == "H":
                        print(f"Kelime '{wrong_word}' aynı bırakıldı!")
                        start = wrong_word_index + len(wrong_word)
                    else:
                        raise(IndexError(f"Geçersiz işlem komutu: {change}"))
                except IndexError:
                    print("İşlem atlandı!")
                    print(f"Kelime '{wrong_word}' aynı bırakıldı!")
            else:
                i += 1
                start = 0

    def __write_txt(self) -> None:
        """Create a .txt file that contains text
        """
        with open("Booldum_Metin.txt", "w", encoding="utf-8") as edited:
            edited.write(self.__text)

    def write_edited_text(self) -> None:
        """Create a folder that contains text and print the text
        """
        self.__write_txt()
        # Okunabilirlik için birkaç tane newline ekledim.
        print(f"\nİşte metninizdeki şapka hatalarının Booldum tarafından " +
               "düzeltilmiş hâli:\n\n\n" +
              f"{self.__text}\n\n")

    def get_text(self) -> str:
        """Returns text
        """
        return self.__text

    def exit(self) -> None:
        """Exits app
        """
        print("Yazının düzeltilmiş haline Booldum_Metin dosyasından ulaşabilirsiniz.")
        input("Kapatmak için Enter tuşuna basınız...")

if __name__ == "__main__":
    booldum = Booldum()
    booldum.change_wrong_words()
    booldum.write_edited_text()
    booldum.exit()

