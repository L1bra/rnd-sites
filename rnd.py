import argparse
import requests
import random
import sys
import os
import re


def parsing(oldpath, path):
    with open('deduplicated.txt', 'r', encoding='UTF-8') as f:
        count = 0
        for line in f.readlines():
            url = line.rstrip('\n')
            try:
                response = requests.get(url).status_code
                if response == 200:
                    with open('sorted.txt', 'w', encoding='UTF-8') as s:
                        s.write(url)

            except requests.exceptions.ConnectionError:
                print("address {}: {} is not exist.".format(count + 1, url))
                count += 1

        print("{} addresses declined.\n".format(count))

    if os.path.isfile(final):
        print('File with existing addresses here: ')
        print(oldpath + '\\' + final)
        os.remove('deduplicated.txt')
    else:
        os.remove('deduplicated.txt')
        os.chdir(oldpath)
        os.rmdir(path)



def main():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-p', '--protocol', type=str, help='[http or https]', default='https')
    parser.add_argument('-l', '--letter', type=int, help='[5-7 average]', default=False)
    parser.add_argument('-d', '--domain', type=str, help='[.com or .ru]', default='.com')
    parser.add_argument('-a', '--address', type=int, 
                        help='How many addresses you need to create.', default=False)

    parse = parser.parse_args()

    magic(parse) if not len(sys.argv) < 5 else print('Not enough arguments...')


def magic(parse):
    abc = 'qwertyuiopasdfghjklzxcvbnm'
    ls = list(abc)
    random.shuffle(ls)

    dr = 'txt'
    global final
    final = 'sorted.txt'
    currdir = os.getcwd()

    if not os.path.isdir(dr):
        os.mkdir(dr)
        os.chdir(dr)
    else:
        files = os.listdir(dr)

        os.chdir(dr)
        txts = filter(lambda x: x.endswith('.txt'), files)

        for x in txts:
            txt = str(x)

            if os.path.isfile(txt):
                if not txt == final:
                    os.remove(txt)
                    print('file: {} was deleted from directory.'.format(txt))

        print()

    os.chdir(currdir)

    try:
        path = dr + '\\dump.txt'

        with open(path, 'a', encoding='UTF-8') as f:
            for _ in range(parse.address):
                result = ''.join([random.choice(ls) for _ in range(int(parse.letter) + 1)])
                f.write(parse.protocol + '://' + result + parse.domain + '\n')

        deduplicate(dr)

    except ValueError as e:
        print(e)
    except Exception:
        print('Unexpected error', sys.exc_info()[0])
        raise


def deduplicate(path):
    with open(path + '\\dump.txt') as in_f, open(path + '\\deduplicated.txt', 'w') as out_f:
        out_f.write(''.join(set(in_f)))

    oldpath = os.getcwd()

    os.chdir(path)
    os.remove('dump.txt')

    parsing(oldpath, path)








if __name__ == "__main__":
    main()