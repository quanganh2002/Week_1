**Báo cáo Tuần 1**

**Nguyễn Hoàng Quang Anh**

Người hướng dẫn: **Ngô Văn Vĩ**

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


```
pip3 install torch
pip3 install transformers
pip3 install seqeval
pip3 install pytorch-crf
pip3 install tensorflow
pip3 install sentencepiece
pip3 install tensorboard
pip3 install numpy
pip3 install tqdm
pip3 install pydrive
pip3 install scikit-learn
```
Hàm tìm kiếm nhị phân: trả về _True_ nếu tìm thấy _target_ trong mảng _arr_

1. **def** intersection(arr1, arr2):  
2.     itst = \[\]  
3.     **for** i **in** arr1:  
4.         **if** binary_search(arr2, i):  
5.             itst.append(i)  
6.     **return** itst  

Hàm tìm giao của 2 mảng _arr1_ và _arr2:_

- Khởi tạo một mảng trống _itst_
- Lặp từng phần tử _i_ trong mảng _arr1_: Dùng tìm kiếm nhị phân tỉm kiếm _i_ trong _arr2_, nếu _i_ có trong _arr2_ thì thêm _i_ vào _itst_
- Trả về mảng _itst_ là giao của 2 mảng _arr1_ và _arr2_

# **Bài 2:**

## Biểu thức chính quy RegEx

Biểu thức: _^(http|https):\\/\\/(www\\.)?\[a-zA-Z0-9\]+(\\.\[a-z\]{2,6})\[^\\s\]\*$_

- _^(http|https):\\/\\/_ : bắt đầu bằng _http_ hoặc _https_ và _://_
- _(www\\.)?_ : có thể chứa _www_ hoặc không
- _\[a-zA-Z0-9\]+(\\.\[a-z\]{2,6})_ : Tên miền của url chỉ chứa các ký tự la tinh hoa/thường từ a-z và chữ số và theo sau là phần domain là các kí tự thường có độ dài từ 2 – 6
- _\[^\\s\]\*$_ : phần path không chứa dấu cách và kết thúc

## Giải quyết bài toán

1. **def** check_url(text):  
2.     patterm = '^(http|https):\\/\\/(www\\.)?\[a-zA-Z0-9\]+(\\.\[a-z\]{2,6})\[^\\s\]\*$'  
3.     **return** re.match(patterm, text)  

Hàm kiếm tra xem chuỗi đầu vào có phải URL hợp lệ không

1. URLs = \[  
2.     '<https://tiki.vn/dien-thoai-may-tinh-bang/c1789?src=mega-menu>',  
3.     '<http://www.example.com>',  
4.     'ftp://invalid-url.com'  
5. \]  

7. **for** i **in** URLs:  
8.     **if** check_url(i):  
9.         **print**(f"{i} hợp lệ")  
10.     **else**:  
11.         **print**(f"{i} không hợp lệ")  

Kiếm tra từng chuỗi trong danh sách xem có hợp lệ không và in ra kết quả

# **Bài 3:**

## Tìm kiếm nhị phân

Cho trước dãy số tăng dần có _n_ phần tử và giá trị _target:_

1. Tìm vị trí đầu tiên trong dãy

- Gán _low = 0, high = n – 1_, _result = - 1_
- Ta tìm giá trị trung vị _med_ tại vị trí _mid =_ (_low + high_)/2 của dãy và so sánh với _target:_
  - - Nếu _med = target_: Gán ­_result = mid, high = mid – 1_ và tiếp tục thuật toán
      - Nếu _med < target_: tiếp tục thuật toán với _low = mid +_ 1
      - Nếu _med > target_: tiếp tục thuật toán với _high = mid –_ 1
      - Nếu _low = high_: kết thúc vòng lặp
- Trả về _result_

1. Tìm vị trí cuối cùng trong dãy

- Gán _low = 0, high = n – 1_, _result = - 1_
- Ta tìm giá trị trung vị _med_ tại vị trí _mid =_ (_low + high_)/2 của dãy và so sánh với _target:_
  - - Nếu _med = target_: Gán ­_result = mid, low = mid + 1_ và tiếp tục thuật toán
      - Nếu _med < target_: tiếp tục thuật toán với _low = mid +_ 1
      - Nếu _med > target_: tiếp tục thuật toán với _high = mid –_ 1
      - Nếu _low = high_: kết thúc vòng lặp
- Trả về _result_

## Giải quyết bài toán

Hàm tìm vị trí đầu tiên:

1. **def** binary_search_first(arr, target):  
2.     low, high = 0, len(arr) - 1  
3.     result = -1  
4.     **while** low <= high:  
5.         mid = (low + high) // 2  
6.         **if** arr\[mid\] == target:  
7.             high = mid - 1  
8.             result = mid  
9.         **elif** arr\[mid\] < target:  
10.             low = mid + 1  
11.         **else**:  
12.             high = mid - 1  
13.     **return** result  

Hàm tìm vị trí cuối cùng:

1. **def** binary_search_last(arr, target):  
2.     low, high = 0, len(arr) - 1  
3.     result = -1  
4.     **while** low <= high:  
5.         mid = (low + high) // 2  
6.         **if** arr\[mid\] == target:  
7.             low = mid + 1  
8.             result = mid  
9.         **elif** arr\[mid\] < target:  
10.             low = mid + 1  
11.         **else**:  
12.             high = mid - 1  
13.     **return** result  

Tìm và in ra vị trí đầu tiên và cuổi dùng của _target_ trong dãy _nums:_

1. **def** find_number(arr, target):  
2.     **return** binary_search_first(arr, target), binary_search_last(arr, target)  

4. nums = \[5,6,7,8,8,8,8,10,12,15\]  
5. target = 8  

7. **print**(find_number(nums, target))
