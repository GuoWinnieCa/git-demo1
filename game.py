import random

x = random.randint(1, 50)
print(x)
for i in range(5):
    y = int(input("請猜數字(1~50):"))
    if y == x:
        print("猜對了!")
        break

    else:
        if y > x:
            print("猜低一點!!")
        else:
            print("猜高一點!")


# 1~50
# 使用者猜五次
# 猜對提前離開
# 猜錯。提示答案

# 題目
# (1~50)(1~25)....
# start = 1
# end = 50

# x = random.randint(start, end)

# print(x)
# for i in range(5):
#     y = int(input(f"請猜數字({start}~{end}):"))

#     if y == x:
#         print("猜對了!")
#         break
#     else:
#         if y > x:
#             print("猜低一點!")
#             if end > y:
#                 end = y - 1
#         else:
#             if start < y:
#                 start = y + 1
#             print("猜高一點!")

# if y != x:
#     print(f"猜錯了,答案為:{x}")
# else:
#     print(f"恭喜過關猜對了,共猜了{i+1}次")
