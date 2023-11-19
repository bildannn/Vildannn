# 1
# def read_and(lines, file):
#     with open(file, encoding='utf-8') as f:
#         listF = f.readlines()
#     st = ''
#     if lines < 0:
#         return 'количество строк должно быть положительным'
#     for i in range(len(listF) - lines, len(listF)):
#         st += listF[i]
#     return st
#
#
# print(read_and(3, 'article.txt'))
# print(read_and(-4, 'article.txt'))








# 2
# import os
#
#
# def print_reps(directory):
#     all_files = os.walk(directory)
#     for catalog in all_files:
#         print(f'Папка {catalog[0]} содержит:')
#         print(f'Дериктории: {', '.join([folder for folder in catalog[1]])}')
#         print(f'Файлы: {', '.join([file for file in catalog[2]])}')
#
#
# print_reps('folder1')








# 3
# def longest_words(file):
#     with open(file, encoding='utf-8') as text:
#         words = text.read().split()
#         max_lenght = len(max(words, key=len))
#         sours_words = [word for word in words if len(word) == max_lenght]
#         if len (sours_words) == 1:
#             return sours_words[0]
#         return sours_words
#
# print(longest_words('article.txt'))







# 4
# def count_statistics(file):
#     with open(file, encoding='utf-8') as text:
#         content = text.read()
#         letter_count = sum(1 for char in content if char.isalpha() and char.isascii())
#         word_count = len(content.split())
#         line_count = len(content.split('\n'))
#
#     print(f"Количество букв латинского алфавита: {letter_count}")
#     print(f"Число слов: {word_count}")
#     print(f"Число строк: {line_count}")
#
# count_statistics('file.txt')