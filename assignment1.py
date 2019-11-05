# a = '%s'
# b = '%s'
# c = '%s'


# for a in range (0, 9 + 1):
#     for b in range (0, 9 + 1):
#         for c in range (0, 9 + 1):
#             if (a and b and c) + (a and b and c) + (a and b and c) == (c and c and c):
#                 print (f"{a} {b} {c}")



#correction
for i in range(100, 333):
    multiple = str(i * 3)
    last_num = (str(i)[-1])*3

    # print (multiple, last_num)
    if multiple == last_num:
        print(i, i*3) 