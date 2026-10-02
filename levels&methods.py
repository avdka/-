def level_1():
    print()
    print("Уровень 1 содержит 3 метода обработки строки:")
    print(" 1 метод возвращает копию исходной строки, в которой все символы",
          "преобразованы в верхний регистр.", sep = "\n   ")
    print(" 2 метод возвращает копию исходной строки, в которой все символы",
          "преобразованы  в нижний регистр.", sep = "\n   ")
    print(" 3 метод возвращает копию исходной строки, в которой первый символ",
          "пребразован в верхний регистр, а все остальные - в нижний.", sep = "\n   ")
    print()
    
    print("Пример использования:")
    text1 = "nPuBem МИР"
    print(" Тестовая строка: ", text1)
    print(" Результат обработки строки 1 методом:", text1.upper())
    print(" Результат обработки строки 2 методом:", text1.lower())
    print(" Результат обработки строки 3 методом:", text1.capitalize())
    print()
    
    while True:
        print
        print("Введите строку:", end = " ")
        str_user = input()
        print("Выберите метод:", end = " ")
        method_num = int(input())
        if method_num == 1:
            print("Ответ: ",str_user.upper())
        elif method_num == 2:
            print("Ответ: ", str_user.lower())
        else:
            print("Ответ: ", str_user.capitalize())
        print("Хотите продолжить? [Д/н]", end = " ")
        ans = input() 
        if ans == "н":
            print()
            main()
        

def level_2():
    print()
    print("Уровень 2 содержит 3 метода обработки строки:")
    print(' 1 метод находит позицию первого вхождения слова "круто".')
    print(' 2 метод возвращает копию исходной строки где все слова "круто" ',
          'заменены на любое выбранное слово.', sep = '\n   ')
    print(' 3 метод находит кол-во букв "o".')
    
    print()
    print("Пример использования:")
    text2 = "Ботать это круто. Очень круто"
    print(" Тестовая строка: ", text2)    
    print(" Результат обработки строки 1 методом:", text2.find("круто") + 1)
    print(' Результат обработки строки 2 методом, если \n', 
          '  слово для замены "круто" - "хорошо" :', text2.replace("круто", "хорошо"))
    print(" Результат обработки строки 3 методом:", text2.count("о"))
    
    while True:
        print()
        print("Введите строку:", end = " ")
        str_user = input()
        print("Выберите метод:", end = " ")
        method_num = int(input())
        if method_num == 1:
            if str_user.find("круто") == -1:
                print("Ответ: ", 'в строке отсутствует слово "круто" ')
            else:
                print("Ответ: ",str_user.find("круто") + 1)
        elif method_num == 2:
            print('Введите слово для замены "круто":', end = " ")     
            substr_change = input()
            print("Ответ: ", str_user.replace("круто", substr_change))
        else:
            print("Ответ: ", str_user.count("о")) 
        print("Хотите продолжить? [Д/н]", end = " ")
        ans = input() 
        if ans == "н":
            print()
            main()
        

def level_3():
    print()
    print("Уровень 3 содержит 2 метода обработки строки:")
    print(" 1 метод разбивает исходную строку на подстроки по заданному",
          "разделителю и возвращает список этих подстрок", sep = "\n   ")
    print(" 2 метод возвращает строку, полученную путем объединения эл-тов",
          "строки или списка с помощию заданного разделителя, который вставляется",
          "между каждыми соседними элементами", sep = "\n   ")

    print()
    print("Пример использования:")
    text3 = "1,2,3,4"
    print(" Тестовая строка: ", text3)    
    print(' Результат обработки строки 1 методом, если ',
    'задан разделитель "," :', text3.split(","))
    print(' Результат обработки строки 2 методом, если '
    'задан разделитель "|" :', "|".join(text3))
    
    while True:
        print()
        print("Введите строку:", end = " ")
        str_user = input()
        print("Выберите метод:", end = " ")
        method_num = int(input())
        print("Введите разделитель:", end = " ")
        separator = input()
        if method_num == 1:     
            print("Ответ: ", str_user.split(separator))
        else:   
            print("Ответ: ", separator.join(str_user))
        print("Хотите продолжить? [Д/н]", end = " ")
        ans = input() 
        if ans == "н":
            print()
            main()
        
        
def level_4():
    print()
    print("Уровень 4 содержит 3 метода обработки строки:")
    print(" 1 метод возвращает True, если все символы исходной строки",
          "явл-ся цифрами, иначе - False", sep = "\n   ")
    print(" 2 метод возвращает True, если все символы исходной строки",
          "явл-ся буквами, иначе - False", sep = "\n   ")
    print(" 3 метод возвращает копию исходной строки, из которой с обоих концов",
          "удалены пробелы (по умолчанию) или заданные символы (при их указании)", 
          sep = "\n   ")
    print()
    
    print("Пример 1:")
    text4_1 = "1234*8/$"
    print(" Тестовая строка: ", text4_1)    
    print(" Результат обработки строки 1 методом:", text4_1.isdigit())
    print(" Результат обработки строки 2 методом:", text4_1.isalpha())
    print(' Результат обработки строки 3 методом, если дополнительно ',
    'для удаления задан символ "$":', text4_1.strip("$"))
    print()
    print("Пример 2:")    
    text4_2 = "   abc1234   "
    print(" Тестовая строка: ", text4_2)
    print(" Результат обработки строки 1 методом:", text4_2.isdigit())
    print(" Результат обработки строки 2 методом:", text4_2.isalpha())
    print(" Результат обработки строки 3 методом, если символы \n ",
    "для удаления заданы только по умолчанию:", text4_2.strip())    
    
    while True:
        print()
        print("Введите строку:", end = " ")
        str_user = input()
        print("Выберите метод:", end = " ")
        method_num = int(input())
        if method_num == 1:
            print("Ответ: ", str_user.isdigit())
        elif method_num == 2:
            print("Ответ: ", str_user.isalpha())
        else:
            print("Нажмите Enter, если хотите оставить символы для удаления по умолчанию.",
                  "Иначе введите требуемые символы без пробелов: ", sep = "\n", end = " ")
            characters_delete = input()
            if characters_delete == '':
                print("Ответ: ",str_user.strip())
            else:
                print("Ответ: ", str_user.strip(characters_delete))   
        print("Хотите продолжить? [Д/н]", end = " ")
        ans = input() 
        if ans == "н":
            print()
            main()
        
    
def level_5():
    text5 = "     pY+HoniisiAWESome    "
    print(text5, end = " ")
    print("===>", end = " ")
    print(" ".join(
                   text5
                   .strip()
                   .capitalize()
                   .replace("+", "t")
                   .replace("is", ".")
                   .split("i")
                   )            
              .replace(".", "is")
         ) 
    main()
    
    
def main():
    print("Выберите уровень:", end = " ")
    level = int(input())
    if level == 1:
        level_1()
    elif level == 2:
        level_2()
    elif level == 3:
        level_3()
    elif level == 4:
        level_4()
    else:
        level_5()


main()
