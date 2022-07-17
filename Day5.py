# List, Tuple , Dictionary

# Khởi tạo mảng

a = []
b = list()

# Khởi tạo mảng có một phần tử

a = ["Hello"]
b = [42]


# List

a = [2, 3, 5, 7]
b = list(range(5))
c = ["mixed type", True, 42]

# các toán tử thông dụng trên list


# len() , min(), max(),sum()

# len dùng để xác định độ dài
# min dùng để tìm phần tử nhỏ nhất
# max dùng để tìm phần tử lớn nhất
# sum dùng để tìm tổng của tất cả các phần tử có trong mảng

# in vs not in
# in dùng để kiểm tra coi phần tử đó có trong mảng hay chứa
# not in dùng để kiểm tra coi nếu phần tử đó không có trong mảng

# index( value , start)
# trả ra index của phần tử trong mảng

# start là vị trí bắt đầu tìm kiếm


# Thêm 1 phần từ vào list
# arr.append(item)

# thêm 1 list vào 1 list

# arr1 += arr2

# thêm 1 list dùng list.extend(list2)


# thêm một phần tử tại vị trí cho trước
# dùng insert()

# Thêm phần tử hoặc list bằng cách
# tạo 1 list mới

# a =[2,3]
# b=a+[13,17]


# Destructive
# a=[2,3]
# b=a
# a+= [4]

#Non - Destructive

# a=[2,3]
# b=a
# a=a+[4]


# muốn thay đổi hàng loạt các giá trị trong mảng

# letter[a:b]=[]

# hoán đổi giá trị giữa 2 biến
# swap parallel assignment
# a=[2,3,5,7]
# a[0],a[1]=a[1],a[0]

