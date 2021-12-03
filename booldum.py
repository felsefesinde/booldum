# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 23:32:46 2021

@author: Burak Alanyalıoğlu 
GitHub: @felsefesinde
Instagram: @felsefesinde
YouTube: Felsefesinde
Twitter: @felsefesinde & @binichburak

"""

import docx
from docx.shared import Pt

file_doc = docx.Document()
style = file_doc.styles["Normal"]
font = style.font
font.name = "Times New Roman"
font.size = Pt(12)

wrong_list_word = []
correct_list_word = []
question = ""

file1 = open("list_of_words.txt", "r")
file3 = open("wrong_versions.txt", "r")

def position_of_word(text, word):
    """
    

    Parameters
    ----------
    text : string
        The input string from the user.
    word : string
        The word for which a hat error is detected.

    Returns
    -------
    new_text : string
        The string in which the {word} is cropped out of text string.
    """
    
    length_of_word = len(word)
    pos_word = text.find(word)
    new_text = text[pos_word : pos_word + length_of_word + 15]
    return new_text

for lines in file3:
    lines1 = lines[:-1]
    wrong_list_word.append(lines1)
    
for new_lines in file1:
    new_lines1 = new_lines[:-1]
    correct_list_word.append(new_lines1) 
      
text = input("Booldum Uygulamasına Hoş Geldiniz! Lütfen metninizi girin: ")

for i in range (len(wrong_list_word)):
    if text.find(wrong_list_word[i]) != -1:
        question = input(f"Metninizde geçen '{wrong_list_word[i]}' \nifadesinin şapka ile yazılması gerekiyor: \nMetindeki yeri şu şekilde: '..." + position_of_word(text, wrong_list_word[i]) + "...'\n" + "Gerekli değişiklik yapılsın mı? [Evet: e | Hayır: h]: ")
        if question == "e":
            text = text.replace(wrong_list_word[i], correct_list_word[i])
        if question == "h":
            text = text.replace(wrong_list_word[i], wrong_list_word[i])

text = text.replace("Ã¢", "â", text.count("Ã¢"))
            
with open("Booldum_Oluşturulan_Metin.txt", "w", encoding="utf-8") as file2:
    file2.write(text)

file_doc.add_paragraph(text)

file_doc.save("D:/Booldum_Düzenlenmis_Metin.docx")

print(f"İşte metninizdeki şapka hatalarının Booldum tarafından düzeltilmiş hâli şu şekilde:\n{text}")

file1.close()
file2.close()
file3.close()
input("Kapatmak için Enter tuşuna basınız.")
