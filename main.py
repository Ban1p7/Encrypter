import random

ENCRYPTION_CHARS = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
DIGITS_TO_CHARS = {
    1: "a",
    2: "b",
    3: "c",
    4: "d",
    5: "e",
    6: "f",
    7: "g",
    8: "h",
    9: "i",
    0: "j",
}
CHARS_TO_DIGITS = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 0,
}

def get_file(filename):
    file = open(filename, "r")
    return file.read()

def generate_key():
    key = []
    key.append(random.choice(ENCRYPTION_CHARS))
    key.append(random.choice(ENCRYPTION_CHARS))
    ''.join(key)
    return key

def encrypt(string, output):
    key = generate_key()

    print(f"Key: {key}")
    print(f"String: {string}")

    nums = []

    for char in string:
        nums.append(ord(char))

    for i in range(len(nums)):
        nums[i] += ord(key[0])
        nums[i] *= ord(key[1])

    for i in range(len(nums)):
        nums[i] = [int(j) for j in str(nums[i])]
        for dig in range(len(nums[i])):
            nums[i][dig] = int(nums[i][dig])
            nums[i][dig] = DIGITS_TO_CHARS[nums[i][dig]]
        ''.join(nums[i])

    for i in range(len(nums)):
        nums[i].append("k")
        nums[i] = ''.join(nums[i])

    nums = ''.join(nums)

    print(f"Nums: {nums}")

    o = open(output, "w")
    o.write(nums)
    o.close()

    return nums, key

def decrypt(code, key):
    code = code.split("k")
    code.pop()
    print(f"Code: {code}")
    for i in range(len(code)):
        code[i] = [*code[i]]
        print("-----")
        print(code[i])
        for j in range(len(code[i])):
            print(j)
            code[i][j] = str(CHARS_TO_DIGITS[code[i][j]])
        code[i] = ''.join(code[i])
        code[i] = int(code[i])

    for i in range(len(code)):
        code[i] /= ord(key[1])
        code[i] -= ord(key[0])

        code[i] = chr(int(code[i]))

    code = ''.join(code)
    print(key)
    return code

# Encode and decode
# code, key = encrypt(get_file("text.txt"), "code.txt")
# message = decrypt(code, key)
# print(f"The code is:\n{message}")

#Encode
# code, key = encrypt(get_file("text.txt"), "code.txt")

#Decode
# message = decrypt(get_file("code.txt"), "ch")
# print(f"The code is:\n{message}")
