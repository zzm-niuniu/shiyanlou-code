# 逢7就跳过，程序编写。打印1-100直接，不是7的倍数,包含7也不行
for i in range(1,101):
    if i % 7 == 0 or i % 10 ==7 or i // 10 ==7:
      continue
    else:
       print(i)
