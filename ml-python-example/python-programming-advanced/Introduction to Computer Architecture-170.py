## 1. Introduction to Computer Components ##

print("Hello World!")

## 2. Data Storage, Memory, and RAM ##

my_int = 10
int_addr = id(my_int)
my_str = "Hello World"
str_addr = id(my_str)

## 4. Understanding How Python Stores Data ##

import sys

my_int = 200
size_of_my_int = sys.getsizeof(my_int)

int1 = 10
int2 = 100000
str1 = "Hello"
str2 = "Hi"
int_diff = sys.getsizeof(int1) - sys.getsizeof(int2)
print(int_diff)

str_diff = sys.getsizeof(str1) - sys.getsizeof(str2)
print(str_diff)