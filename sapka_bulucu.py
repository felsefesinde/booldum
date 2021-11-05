# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 23:32:46 2021
Booldum App
@author: Burak Alanyalıoğlu
"""
wrong_list_word = []
correct_list_word = []
soru = ""

file1 = open("list_of_words.txt", "r")
file2 = open("created_text.txt", "w")
file3 = open("wrong_versions.txt", "r")

def position_of_word(text, word):
    length_of_word = len(word)
    pos_word = text.find(word)
    new_text = text[pos_word : pos_word + length_of_word + 8]
    return new_text
    
for lines in file3:
    lines1 = lines[:-1]
    wrong_list_word.append(lines1)
       
for new_lines in file1:
    new_lines1 = new_lines[:-1]
    correct_list_word.append(new_lines1) 
       
text = input("Lütfen metninizi girin: ")

for i in range (len(wrong_list_word)):
    if text.find(wrong_list_word[i]) != -1:
        soru = input(f"Metninizde geçen {wrong_list_word[i]} ifadesinin şapka ile yazılması gerekiyor: \n" + position_of_word(text, wrong_list_word[i]) + "Gerekli değişiklik yapısın mı? [Evet: e | Hayır: h]: ")
        if soru == "e":
            text = text.replace(wrong_list_word[i], correct_list_word[i])
        if soru == "h":
            text = text.replace(wrong_list_word[i], wrong_list_word[i])
        
file2.write(text)
print(text)

file1.close()
file2.close()
file3.close()