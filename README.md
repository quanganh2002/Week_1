# **Bài 1:**

## Tìm kiếm nhị phân

Cho trước dãy số tăng dần có _n_ phần tử, tìm giá trị _target_:

- Gán _low = 0, high = n – 1_
- Ta tìm giá trị trung vị _med_ tại vị trí _mid =_ (_low + high_)/2 của dãy và so sánh với _target_
  - Nếu _med = target_: tra về _med, mid_ và kết thúc thuật toán
  - Nếu _med < target_: tiếp tục thuật toán với _low = mid +_ 1
  - Nếu _med > target_: tiếp tục thuật toán với _high = mid –_ 1
  - Nếu _low = high ≠ target_: kết thúc thuật toán

## Giải quyết bài toán



Hàm tìm kiếm nhị phân: trả về _True_ nếu tìm thấy _target_ trong mảng _arr_
```
def binary_search(arr, target):  
```

Hàm tìm giao của 2 mảng _arr1_ và _arr2:_
```
intersection(arr1, arr2)  
```

- Khởi tạo một mảng trống _itst_
- Lặp từng phần tử _i_ trong mảng _arr1_: Dùng tìm kiếm nhị phân tỉm kiếm _i_ trong _arr2_, nếu _i_ có trong _arr2_ thì thêm _i_ vào _itst_
- Trả về mảng _itst_ là giao của 2 mảng _arr1_ và _arr2_

# **Bài 2:**

## Biểu thức chính quy RegEx

Biểu thức: 
```
_^(http|https):\/\/(www\\.)?\[a-zA-Z0-9\]+(\\.\[a-z\]{2,6})\[^\\s\]\*$_
```
- ``` _^(http|https):\/\/ ``` : bắt đầu bằng _http_ hoặc _https_ và _://_
- ```_(www\\.)?_ ```: có thể chứa _www_ hoặc không
- ```_\[a-zA-Z0-9\]+(\\.\[a-z\]{2,6})_``` : Tên miền của url chỉ chứa các ký tự la tinh hoa/thường từ a-z và chữ số và theo sau là phần domain là các kí tự thường có độ dài từ 2 – 6
- ```_\[^\\s\]\*$_ ```: phần path không chứa dấu cách và kết thúc

## Giải quyết bài toán

Hàm kiếm tra xem chuỗi đầu vào có phải URL hợp lệ không
```
check_url(text)
```

Kiếm tra từng chuỗi trong danh sách xem có hợp lệ không và in ra kết quả
```
URLs = [
    'https://tiki.vn/dien-thoai-may-tinh-bang/c1789?src=mega-menu',
    'http://www.example.com',
    'ftp://invalid-url.com'
]

for i in URLs:
    if check_url(i):
        print(f"{i} hợp lệ")
    else:
        print(f"{i} không hợp lệ")
```
# **Bài 3:**

## Tìm kiếm nhị phân

Cho trước dãy số tăng dần có _n_ phần tử và giá trị _target:_

1. Tìm vị trí đầu tiên trong dãy

- Gán _low = 0, high = n – 1_, _result = - 1_
- Ta tìm giá trị trung vị _med_ tại vị trí _mid =_ (_low + high_)/2 của dãy và so sánh với _target:_
  - Nếu _med = target_: Gán ­_result = mid, high = mid – 1_ và tiếp tục thuật toán
      - Nếu _med < target_: tiếp tục thuật toán với _low = mid +_ 1
      - Nếu _med > target_: tiếp tục thuật toán với _high = mid –_ 1
      - Nếu _low = high_: kết thúc vòng lặp
- Trả về _result_

1. Tìm vị trí cuối cùng trong dãy

- Gán _low = 0, high = n – 1_, _result = - 1_
- Ta tìm giá trị trung vị _med_ tại vị trí _mid =_ (_low + high_)/2 của dãy và so sánh với _target:_
  -  Nếu _med = target_: Gán ­_result = mid, low = mid + 1_ và tiếp tục thuật toán
      - Nếu _med < target_: tiếp tục thuật toán với _low = mid +_ 1
      - Nếu _med > target_: tiếp tục thuật toán với _high = mid –_ 1
      - Nếu _low = high_: kết thúc vòng lặp
- Trả về _result_

## Giải quyết bài toán

Hàm tìm vị trí đầu tiên:

```
def binary_search_first(arr, target):
    low, high = 0, len(arr) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            high = mid - 1
            result = mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return result
```

Hàm tìm vị trí cuối cùng:
```
def binary_search_last(arr, target):
    low, high = 0, len(arr) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            low = mid + 1
            result = mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return result
```
Tìm và in ra vị trí đầu tiên và cuổi dùng của _target_ trong dãy _nums:_

```
def find_number(arr, target):
    return binary_search_first(arr, target), binary_search_last(arr, target)
```

4. nums = \[5,6,7,8,8,8,8,10,12,15\]  
5. target = 8  

7. **print**(find_number(nums, target))
