from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


def stemming(file):
    content = file.split()
    tokenize_with_out_stopwords = []
    for word in content:
        if word not in stopwords.words('english'):
            tokenize_with_out_stopwords.append(word)
        else:
            pass
    ps = PorterStemmer()
    final_resault = []
    for word in tokenize_with_out_stopwords:
        final_resault.append(ps.stem(word))

    print('first stage (tokenize): ', content)
    print('second stage (remove stopwords): ', tokenize_with_out_stopwords)
    print('third stage (stemming): ', final_resault)


data = []
file1 = open('1.txt', 'r')
data.append(file1.read())
file1.close()

file2 = open('2.txt', 'r')
data.append(file2.read())
file2.close()

file3 = open('third.txt', 'r')
data.append(file3.read())
file3.close()

userInput = input("enter your message: ").split()
counterFile1 = counterFile2 = counterFile3 = 0

for file in data:
    for content in file.split():
        for word in userInput:
            if word in content:
                idx = data.index(file)

                if idx == 0:
                    counterFile1 += 1
                if idx == 1:
                    counterFile2 += 1
                if idx == 2:
                    counterFile3 += 1

counters = [counterFile1, counterFile2, counterFile3]
counters.sort(reverse=True)

if max(counters) == counterFile1 and max(counters)!=0:
    file = data[0]
    print('\nthe first matching \'file1\'\n')
    counters.remove(max(counters))
    if max(counters) == counterFile2 and max(counters) == counterFile3:
        print('the second \'file2\'\n')
        print('the third \'file3\'\n')

    elif max(counters) == counterFile2:
        print('the second \'file2\'\n')
        counters.remove(max(counters))

    elif max(counters) == counterFile2:
        print('the third \'file3\' \n')
        counters.remove(max(counters))
    stemming(file)

elif max(counters) == counterFile2 and max(counters)!=0:
    file = data[1]
    print('\nthe first matching \'file2\'\n')
    counters.remove(max(counters))
    if max(counters) == counterFile1 and max(counters) == counterFile3:
        print('the second \'file1\'\n')
        print('the third \'file3\'\n')

    elif max(counters) == counterFile1:
        print('the second \'file1\'\n')
        counters.remove(max(counters))

    elif max(counters) == counterFile3:
        print('the third \'file3\'\n')
        counters.remove(max(counters))

    stemming(file)

elif max(counters) == counterFile3 and max(counters)!=0:
    file = data[2]


    print('\nthe first matching \'file3\'\n')
    counters.remove(max(counters))
    if max(counters) == counterFile1 and max(counters) == counterFile2:
        print('the second \'file1\'\n')
        print('the third \'file2\'\n')

    elif max(counters) == counterFile1:
        print('the second \'file1\'\n')
        counters.remove(max(counters))

    elif max(counters) == counterFile2:
        print('the third \'file3\'\n')
        counters.remove(max(counters))
    stemming(file)
else:
    print('not found')

