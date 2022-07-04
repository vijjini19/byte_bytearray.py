'''In bytes modifications cannot be made.
In bytearray modifications can be made'''



# a=b"program"
# print(a,type(a))  #b'program'<class 'bytes'>
# print(list(a))  #[112, 114, 111, 103, 114, 97, 109]
# print(tuple(a))  #(112,114,111,103,114,97,109)
# print(set(a))  #{97,103,109,111,112,112}

# y="python"
# for i in y:
#     print(i)  

# print(ord('A'))  #65 
# print(ord('Z'))  #90
# print(ord('a'))  #97
# print(ord('z'))  #122
# print(ord('J'))  #74
# print(ord('j'))  #106
# print(ord('t'))  #116
# print(chr(45))  #-
# print(chr(80))  #P
# print(chr(90))  #Z
# print(chr(91))  #[
# print(chr(44))  #,

# n=b"computer"
# print(n,type(n))
# n[2]='L'
# print(n)  #TypeError:'bytes' object does not support item assignment
# n[0]=90
# print(n)

# v=b'[1,2,3]'
# print(list(v))  #[91,49,44,50,44,51,93]

# print(ord('{'))  #123
# print(ord('}'))  #125
# print(ord('['))  #91
# print(ord(']'))  #93
# print(ord('"'))  #34
# print(ord(' '))  #32
# print(ord(','))  #44
# print(ord('.'))  #46

# x=bytearray(b"system")
# print(x,type(x))  #bytearray(b'system') <class 'bytearray'>
# print(x[3])
# x[3]=72
# print(x[3])
# print(x)