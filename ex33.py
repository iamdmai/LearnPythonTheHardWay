# ex33: While Loops


def testNumbers(counter, step):

    i = 0
    numbers = []

    for i in range(0, counter, step):
        
        print "At the top i is %d" % i
        numbers.append(i)

        print "Numbers now:", numbers
        print "At the bottom i is %d" % i

    return numbers

numbers = testNumbers(10,2)

print "The nnumbers: "

for num in numbers:
    print num
