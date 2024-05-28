PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

words = PRICE_LIST.split()

# words_dictionary = {}
# for index, word in enumerate(words):
#     if index % 2 == 0:
#         name = word.strip(",")
#         price = int(words[index + 1].strip("р,"))
#         words_dictionary[name] = price
#
# print(words_dictionary)

# Changed
names = [word for index, word in enumerate(PRICE_LIST.split()) if index % 2 == 0]
prices = [int(word[:-1]) for index, word in enumerate(PRICE_LIST.split()) if index % 2 != 0]
new_dict = dict(zip(names, prices))
print(new_dict)
