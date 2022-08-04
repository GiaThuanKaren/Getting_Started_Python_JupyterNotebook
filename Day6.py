# mảng 2 chiều
# a) Cấp phát tĩnh
# a=[[2,3,4],[4,3]]
# print(a)

# b) cấp phát động
# Cách 1 : Mở rộng mỗi dòng
# rows = 3
# cols = 2
# a = []
# for row in range(rows):
#     a += [[0]*cols]
# Cách 2 : Dùng list comprehension

rows = 3
cols = 2
a = [([0] * cols) for row in range(rows)]
print("This IS ok. At first:")
print(" a =", a)
a[0][0] = 42
print(" a =", a)
