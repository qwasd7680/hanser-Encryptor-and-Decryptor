def to_binary_and_encrypt(text):
    binary = ''.join(format(byte, '08b') for char in text for byte in char.encode('utf-8'))
    encrypted = binary.replace('0', '憨').replace('1', '色')
    return encrypted


def decrypt_and_to_text(encrypted):
    binary = encrypted.replace('憨', '0').replace('色', '1')
    text = bytearray()
    for i in range(0, len(binary), 8):
        byte = binary[i:i + 8]
        if len(byte) == 8:
            text.append(int(byte, 2))
    return text.decode('utf-8')


RED = "\033[31m"
YELLOW = "\033[33m"
RESET = "\033[0m"

print("本代码由" + f"{YELLOW}BiliBili@毛怪的产后护理{RESET}" + "编写")
print(f"{RED}本代码仅供整活，并不能真正用于加密解密，一切不当使用所造成的后果自负{RESET}")
while True:
    mode = input("请选择模式（输入选项前的数字）：(1).加密 (2).解密 (3).退出\n")
    if mode == '1':
        original_text = input("请输入要加密的文本：")
        encrypted_text = to_binary_and_encrypt(original_text)
        print("原始文本:", original_text)
        print("加密后的文本:", encrypted_text)
    elif mode == '2':
        encrypted_text = input("请输入要解密的文本：")
        original_text = decrypt_and_to_text(encrypted_text)
        print("加密后的文本:", encrypted_text)
        print("解密后的文本:", original_text)
    elif mode == '3':
        break
    else:
        print("无效的输入，请重新输入")
