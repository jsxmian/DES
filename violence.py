#明文：10101010
# key：1010101010
# 密文：01101011
import time

from S_DES import generate_key, encrypt


i = 0
p10_table = (3, 5, 2, 7, 4, 10, 1, 9, 8, 6)
p8_table = (6, 3, 7, 4, 8, 5, 10, 9)
t = "10101010" #明文
m = "01101011" #目标密文
print("破解开始")
begin = time.time()




while(1):
    bit = bin(i).replace('0b', '').rjust(10,'0')
    k1, k2 = generate_key(bit, p10_table, p8_table)
    result = encrypt(t, k1, k2)
    if result == m:
        break
        # print("密匙"+ bit)
    i = i + 1
end = time.time()
print("破解结束，密钥："+ bin(i).replace('0b', '').rjust(10,'0'))
print(f'暴力破解耗时:{end - begin:.4f}s')


