def caesar(text):
    lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    a = [i for i in text.split()]   # Список слов из исходного текста
    b = []   # Список слов из исходного текста без небуквенных символов
    for i in a:
        c = ''
        for k in range(len(i)):
            if i[k].isalpha():
                c += i[k]
        b.append(c)

    for i in range(len(a)):
        for m in range(len(a[i])):
            if a[i][m].isalpha():   # Является ли символ буквой
                if a[i][m] == a[i][m].lower():
                    ind = lower_alphabet.index(a[i][m])   # Индекс строчной буквы в алфавите
                    index = (ind + len(b[i])) % 26    # Индекс буквы при шифровании с шагом равным слову
                    print(lower_alphabet[index], end='')   # Вывод строчной буквы в итоговый текст
                if a[i][m] == a[i][m].upper():
                    ind = upper_alphabet.index(a[i][m])   # Индекс заглавной буквы в алфавите
                    index = (ind + len(b[i])) % 26    # Индекс буквы при шифровании с шагом равным слову
                    print(upper_alphabet[index], end='')   # Вывод заглавной буквы в итоговый текст
            else:
                print(a[i][m], end='')   # Вывод не буквенных символов в итоговый текст
        print(' ', end='')   # Вывод пробела между словами

if __name__ == '__main__':
    text = input()
    caesar(text)