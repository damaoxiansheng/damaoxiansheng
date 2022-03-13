'''
    字符串的编码：（了解）
        python的字符串都是以unicode码，一个汉字是两个字节来定义（Byte=8bit）。
        每一个汉字都要有一个整数与之对应。
        1、可以通过ord()方法获取一个字符串对应的编码（整数）
        2、通过一个整数编码获取对应的字符串，chr()
    
    编码：encode
        就是将字符串转为字节码的过程
    解码：decode
        将某个字节码（整数），转化为对应某个字符集中的字符
    乱码：
        字节码解码时候，不能正常显示字符的现象就是乱码。
        出现乱码的原因是什么？
            编码和解码使用的字符集是不一样的
        编码和解码都是用相同的字符集即可，就不会出现乱码了。

'''
print(ord("A"))   #65
print(ord("你"))  #20320

print(chr(97))
print(chr(20320))

print("A".encode("ascii")) # b'A'
# "你"--> \u4f60
# ascii-->只支持128个字符
# print("你".encode("ascii"))
print("你".encode("gb2312")) # b'\xc4\xe3'
# utf8是可变长的Unicode码，一个汉字占三个字节
print("你".encode("utf8")) # b'\xe4\xbd\xa0'

a = b'\xc4\xe3'
abc = b'\xd0\xa1'
print(abc.decode("gb2312"))
print(abc.decode("utf8")) #乱码了 C

c = b'\xe4\xbd\xa0'
print(c.decode("utf8")) 