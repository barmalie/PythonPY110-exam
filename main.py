import conf
import json
import random
import Faker



# def main():
text = open('BOOK.txt', 'r', encoding='utf8')
for i in text:
    print(i)




def Title():
    book = random.choice(text)
    print(book)
    # select = random.randint(text[])
    return

Title()
    # print(select)
#
def year():
    x =[i for i in random.range(5)]
    print(x)
    return
year()



def pages():
    fake = Faker()
    Faker.seed(0)
    for _ in range(1):
        fake.isbn13()
pages()
# def isbn13():
#
# def rating():
#
#
# def price():
#
# def author():
#
# if __name__ == "__main__":
#     main()
#     downloads_json = json.loads(main)

text.close()