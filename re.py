# import re
#
# text = 'Beautiful is better than ugly.Explicit is better than implicit.Simple is better than complex.Complex is better than complicated.Flat is better than nested.Sparse is better than dense.Readability counts.Special cases aren\'t special enough to break the rules.Although practicality beats purity.Errors should never pass silently.Unless explicitly silenced.In the face of ambiguity, refuse the temptation to guess.There should be one-- and preferably only one --obvious way to do it.Although that way may not be obvious at first unless you\'re Dutch.Now is better than never.Although never is often better than *right* now.If the implementation is hard to explain, it\'s a bad idea.If the implementation is easy to explain, it may be a good idea.Namespaces are one honking great idea -- let\'s do more of those!'
# word = 'Beautiful'
# print(len(text))
# print(text.strip())
# print(text.lower())
# print(text.upper())
# print("Beautiful".lower().startswith("beauti"))
# print("Beautiful".startswith("Beauti"))
# print("Beautiful".endswith("ful"))
# print("Beautiful".find("Beauti"))
# print("Beautiful".find("ful"))
# print("Beautiful".replace("ful", "self"))
# print(",".join(text))
# print("ful" in "beautyful")
# string = 'Beautiful is better than ugly.Explicit is better than implicit.'
# word_2 = 'better'
# word_3 = 'than'
# word2 = re.findall(word_2, string)
# word3 = re.findall(word_3, string)
# print(word2, word3)

# print(re.findall('x{3,5}y{0,3}', 'xyyy'))
# print(re.findall('x{3,5}y', 'xxxy'))
# print(re.findall('x{3,5}y', 'xxxxy'))
# print(re.findall('x{3,5}y', 'xxxxxy'))
# print(re.findall('x{3,5}y', 'xxxxxxy'))

# inputs = ['18:29', '23:55', '123', 'ab:de', '18:299', '99:99']
# input_ok = lambda x: re.fullmatch('([01][0-9]|2[0-3]):[0-5][0-9]', x) != None
# for x in inputs:
#     print(input_ok(x))

# ord = re.findall('s...e', text)
# print(ord)
# ord_1 = re.findall('y.*y', text)
# print(ord_1)
# ord_2 = re.findall('blocks?', text)
# print(ord_2)

# txt = '<div>head</div>'
# print(re.findall('<.*?>', txt))
# print(re.findall('<.*>', txt))

# ord_3 = 'comp.*'
# print(re.match(ord_3, text))
# print(re.search(ord_3, text))
# print(re.findall(ord_3, text))

# duplicates = re.findall('([^\s]*(?P<x>[^\s])(?P=x)[^\s]*)', text)
# print(duplicates)

# update_text = re.sub('than','the', text)
# print(update_text)
