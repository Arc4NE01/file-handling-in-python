import sys
import os

var = "hello.txt"
var2 = "myfile.txt"


# file detection
def use_try_except():
    try:
        # file = open(fr"G:\D\Codes\NewPY\{var}", "r")
        file2 = open(fr"{var}")
    except FileNotFoundError:
        print("No file")
    else:
        print(file2)
        file2.close()


def use_os_mod():
    print(os.path.isfile(fr"G:\D\Codes\NewPY\{var2}"))
    if os.path.isfile(fr"G:\D\Codes\NewPY\{var}"):
        f = open(var2)
        print(f)
        f.close()
    else:
        print("cant open file")


# whether file is readable or writable
def read_write():
    f = open(var2, "r")
    print(f.readable())
    print(f.writable())


# closing a file
def with_state():
    l = []
    with (open(var2, 'r')) as f:
        data = f.read()
        for idx, value in enumerate(data):
            if " " in value:
                l.append(idx)
        # data_mod = data.split("")
        # for i in range(len(data_mod)):
        #     if data_mod[i] == " ":
        #         l.append(i)
        print(l)
        print(data)
        # print(data_mod)


# reading using read, readline, readlines and position of the cursor
def reading():
    f = open(var2)
    # data = f.read() print(data) after the f.read() has been called the cursor moved to the last character data2 =
    # data2 = f.readline() # always remember the cursor position,
    # data3 = f.readline() # after the first readline the cursor moves to the last position of the line
    # data4 = f.readline(5)  # prints start to the given number
    # print(data2, end="")  # end is used because
    # print(data3)
    # print(data4)
    data5 = f.readlines()  # reads the full file and returns a list of lines
    for line in data5:
        print(line, end="")
    print(data5)
    f.close()


def tell_seek():
    f = open(var2)
    initial_pos = f.tell()
    print(initial_pos)
    # f.read(3)
    # print(data)
    # final_pos = f.tell()  # returns the current position of the cursor, it is like indexing of string
    # print(final_pos)
    # f.readline()
    # print(f.tell()) # readline reads all the char in a line,by using tell in this, we can verify the length of the txt
    f.readlines()  # reads all the characters including \n
    print(f.tell())
    # currently the cursor position is in the end of the file, to bring it to the top we got to use seek() method
    f.seek(0)  # this function can change the position of the cursor
    print(f.readline(), end="")
    f.seek(6)
    print(f.readline())
    f.close()


def using_sys():
    f = open(var2)
    sys.stdin = f
    s = input()
    s1 = input()
    print(s)
    print(s1)


# # print(file.read())
# file.close()
# file1 = open(r"G:\D\Codes\hello.txt", "r+")
# file1.write("hello")
# # print(file1.read())
# file1.close()
# file2 = open("G:\D\Codes\hello.txt", "r+")
# s = ["hello there", "\n", "are you alright", "\n", "hope ur good"]
# file2.writelines(s)
# #print(file2.readlines())
# file2.close()
# file3 = open("G:\D\Codes\hello.txt", "a+")
# file3.write("\noh no")
# print(file3.readlines())


# use_try_except()
# use_os_mod()
# read_write()
# with_state()
# reading()
# tell_seek()
using_sys()
