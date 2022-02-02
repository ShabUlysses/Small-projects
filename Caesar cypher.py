#!/usr/bin/env python
# coding: utf-8

# In[2]:


print('Привет, я помогу тебе в твоих шпионских вопросах.')

cipher = input('Мы дешифруем текст или зашифровываем? Дешифр/Шифр \n')

def define_language(text):  # Данная функция автоматически определяет язык ввода, чтобы не мучить пользователя лишний раз. 
    for letter in text:
        if 96 < ord(letter) < 122:
            return 26, 96, 122
        elif 1071 < ord(letter) < 1103:
            return 32, 1071, 1103
        else:
            continue

def deciphering(text): #  Функция для дешифрования
    max_shift, min_ord, max_ord = define_language(text)
    alpha_size = max_ord - min_ord
    for shift in range(1, max_shift):
        result = ''
        for letter in text:
            if letter.isalpha():
                a = chr(ord(letter.lower()) + shift) if (ord(letter.lower()) + shift) <= max_ord                else chr((ord(letter.lower()) + shift) - alpha_size)
                a = a.upper() if letter.isupper() else a
                result += a
            else:
                result += letter
        print(f'Дешифрование со сдвигом {shift}: {result}')
        
    
def ciphering(text, shift): #  Функция для шифрования
    max_shift, min_ord, max_ord = define_language(text)
    alpha_size = max_ord - min_ord
    result = ''
    for letter in text:
        if letter.isalpha():
            a = chr(ord(letter.lower()) + shift) if (ord(letter.lower()) + shift) <= max_ord            else chr((ord(letter.lower()) + shift) - alpha_size)
            a = a.upper() if letter.isupper() else a
            result += a
        else:
            result += letter
    print(result)
    
if cipher.lower() == 'дешифр':
    deciphering(input('Введите текст: \n'))
elif cipher.lower() == 'шифр':
    ciphering(input('Введите текст: \n'), int(input('Введите значение сдвига: \n')))
else:
    print('Не смог разобрать текст. По умолчанию выбрано дешифрование')
    deciphering(input('Введите текст: \n'))


# In[ ]:


print(ord(('q')))


# In[ ]:




