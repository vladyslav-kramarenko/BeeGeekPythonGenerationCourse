"""
Вам дан словарь, состоящий из пар слов-синонимов. Повторяющихся слов в словаре нет. Напишите программу, которая для одного данного слова определяет его синоним.

Формат входных данных
На вход программе подается количество пар синонимов nn. Далее следует nn строк, каждая строка содержит два слова-синонима. После этого следует одно слово, синоним которого надо найти.

Формат выходных данных
Программа должна вывести одно слово, синоним введенного.

Примечание 1. Гарантируется, что синоним введенного слова существует в словаре.

Примечание 2. Все слова в словаре начинаются с заглавной буквы.
"""
def solution():
    dic = {}
    for i in range(int(input())):
        s = input().split()
        dic[s[0]] = s[1]
    word = input()
    for key, val in dic.items():
        if word == key:
            print(val)
        if word == val:
            print(key)

"""
Sample Input 1:

4
Awful Terrible
Beautiful Pretty
Great Excellent
Generous Bountiful
Pretty
Sample Output 1:

Beautiful
Sample Input 2:

3
Kind Affable
Intellect Mind
Popular Celebrated
Popular
Sample Output 2:

Celebrated"""