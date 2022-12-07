"""
Анаграмма – слово (словосочетание), образованное путём перестановки букв, составляющих другое слово (или словосочетание). Например, английские слова evil и live – это анаграммы.

На вход программе подаются два слова. Напишите программу, которая определяет, являются ли они анаграммами.

Формат входных данных
На вход программе подаются два слова, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести YES если слова являются анаграммами и NO в противном случае.
"""
def solution():
    w1 = sorted(list(input()))
    w2 = sorted(list(input()))
    res = "NO"
    if len(w1) == len(w2):
        res = "YES"
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                res = "NO"
                break
    print(res)

"""
Sample Input 1:

thing
night
Sample Output 1:

YES
Sample Input 2:

cat
rat
Sample Output 2:

NO
Sample Input 3:

tea
eat
Sample Output 3:

YES
"""