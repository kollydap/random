# import multiprocessing,threading

# result = [2,5]

# def set_result():
#     for i in range(10):
#         result.append(i)
#         print(result)
#         # return "hello"

# p1=threading.Thread(target=set_result, args=())
# p1.start()
# p1.join()

# print(result)

# def gey(li):
#     for idx, num in enumerate(li):
#         print(num)

# gey([1,2,5,6,7,8,96,3,4,5])


def get_item_by_index(i: int):
    li = [1, 2, 3, 4]
    if i > 4:
        raise IndentationError
    print(li[i])

get_item_by_index(4)
