class Test:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def testingDef(self):
        print('hello')



# test1 = Test()
# test1.test = 10
# hello = 'hello'
# test1.testingDef()
# hello = hello.replace('he', 'o')
# print('w' in hello)
#
# if hello == 'hello':
#     print("you're wrong")
# elif hello == 'ollo' and not hello == 'www':
#     print("you're right")
# else:
#     print('haha')
#
# while test1.test > 1:
#     if test1.test % 2 == 0:
#         print(test1.test)
#
#     test1.test -= 1
#
#
#
# for num in range(5, 20, 2):
#     print(num)

collection = [0,0,1,2,3,0,4,1,5,3]

def removeDup(nums):
    dup = set()
    result = []

    for num in nums:
        if not dup.__contains__(num):
            result.append(num)
            dup.add(num)

    return result

result = removeDup(collection)

print(result)

test1 = Test(10,20)
test1.x = 10
test1.hello = 10
