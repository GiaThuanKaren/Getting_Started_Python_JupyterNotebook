a = 157
# Với mỗi câu lệnh if thì
# cần thêm dấu : ở cuối biểu thức điều kiện
# Khi ở else cuối cùng , nếu không có điều kiện
# thì thêm dấu : ở sau eles để kết thúc
# nếu có điều kiện ở else thì dùng elif
if(a == 5):
    print("Express 1")
elif(a == 10):
    print("Express 2")
elif(a == 15):
    print("Express 3")
else:
    print("Express 5")


# Đối với trường hợp có các if lồng nhau

num = float(input('Nhập một số'))
if(num >= 0):
    if(num == 0):
        print("Số không")
    else:
        print("Số dương")
else:
    print("Số Âm")

# Vòng lặp while
# đối với python là không có trường hợp do while
# Đối với while khi kết thúc câu lệnh

dem = 0
while(dem < 3):
    print("Dang o trong vong while")
    dem += 1
else:
    print("dang o trong while")

# For trong python
# Lặp từ A -> B dùnn hàm range (A,B)
# tương đương sẽ lặp từ A-> B-1

# hàm range hỗ trợ lên đến 3 tham số
#  A, B , C : A, B là khoảng cách , điểm đầu , điểm cuối
# C là bước nhảy , mặc định là 1

# for d in range(10, 20):
#     print(d)


x = 0
for x in range(2, 7):
    if(x == 5):
        print("break")
        break
    else:
        print(x)

