import tkinter as tk
from tkinter import W, E


from S_DES import generate_key, encrypt


# 定义函数，接收两个参数并返回结果
def calculate(num1, num2):
    # key = "1010000010"
    p10_table = (3, 5, 2, 7, 4, 10, 1, 9, 8, 6)
    p8_table = (6, 3, 7, 4, 8, 5, 10, 9)
    # p4_table = (2, 4, 3, 1)
    # # p = "10110101"
    # # ip_table = (2, 6, 3, 1, 4, 8, 5, 7)
    # # ep_table = (4, 1, 2, 3, 2, 3, 4, 1)
    # # ip_ni_table = (4, 1, 3, 5, 7, 2, 8, 6)
    # # sbox0 = [
    # #     [1, 0, 3, 2],
    # #     [3, 2, 1, 0],
    # #     [0, 2, 1, 3],
    # #     [3, 1, 0, 2]
    # # ]
    # #
    # # sbox1 = [
    # #     [0, 1, 2, 3],
    # #     [2, 3, 1, 0],
    # #     [3, 0, 1, 2],
    # #     [2, 1, 0, 3]
    # # ]

    # 生成子密钥 K1 和 K2
    k1, k2 = generate_key(num2, p10_table, p8_table)
    result = encrypt(num1, k1, k2)
    return result


def calculate1(num1, num2):
    p10_table = (3, 5, 2, 7, 4, 10, 1, 9, 8, 6)
    p8_table = (6, 3, 7, 4, 8, 5, 10, 9)
    result = ""
    # 生成子密钥 K1 和 K2
    k1, k2 = generate_key(num2, p10_table, p8_table)
    for i in num1:
        # bit = (bin(ord(i)))
        bit = str_2_bin(i).rjust(8,'0')
        result = result + encrypt(bit, k1, k2)
    print(result)
    result = bin_2_str(result)
    return result


"""
二进制、字符串转换
"""


def str_2_bin(str):
    """
    字符串转换为二进制
    """
    return ' '.join([bin(ord(c)).replace('0b', '') for c in str])


def bin_2_str(bin):
    """
    二进制转换为字符串
    """
    return ''.join([chr(i) for i in [int(b, 2) for b in bin.split(' ')]])

# 定义按钮点击事件
def on_button_click():
    # 获取用户输入的两个数据
    num1 = str(entry1.get())
    num2 = str(entry2.get())

    # 调用函数进行计算
    result = calculate(num1, num2)

    # 显示结果
    output_label.config(text=f"结果：{result}")

def on_button1_click():
    # 获取用户输入的两个数据
    num1 = str(entry1.get())
    num2 = str(entry2.get())

    # 调用函数进行计算
    result = calculate1(num1, num2)

    # 显示结果
    output_label1.config(text=f"结果：{result}")

# 创建窗口
window = tk.Tk()
l1 = tk.Label(window, text='明文（8位）:')
l1.pack()
# 创建输入框和标签
entry1 = tk.Entry(window)
entry1.pack()

l2 = tk.Label(window, text='密钥（10位）:')
l2.pack()
entry2 = tk.Entry(window)
entry2.pack()


# 创建按钮
button = tk.Button(window, text="加密（bit）", command=on_button_click)
button.pack()

button1 = tk.Button(window, text="加密（ACII）", command=on_button1_click)
button1.pack()

# 创建输出标签
output_label = tk.Label(window, text="结果：")
output_label.pack()

output_label1 = tk.Label(window, text="结果：")
output_label1.pack()

# 运行窗口
window.mainloop()