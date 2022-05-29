import conf
import json
import random
from faker import Faker

from random import randint

def main():
    text = open('BOOK.txt', 'r', encoding='utf8')
    for i in text:
        print(i)
        text.close()
update_json_file = open('catalog.json', 'w')
downloads_json = json.dumps(main)



def Title():
    book = random.choice(text)
    print(book)
        # select = random.randint(text[])
    return

Title()

def year():
    print(randint(1990, 2020))
    return

year()


def pages():
    print(randint(0, 5))
pages()

def isbn13():
    fake = Faker()
    Faker.seed(0)
    for _ in range(1):
        fake.isbn13()
        print(_)
        return
isbn13()

def rating():
    #print(randint(1, 1000))
    return
rating(randint(1, 1000))


def price():
    print(randint(1, 1000))

price()

def author():
    fake = Faker()
    fake.name()
    for _ in range(10):
        print(fake.name())

if __name__ == "__main__":
    main()



