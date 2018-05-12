#python3
# -*- coding: utf-8 -*-

#Remove the start and end all spaces of the string. do not use strip() 

def trim(s):
    if len(s) == 0:
        return ''
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s
    
    
    
def trim(s):
    if len(s) == 0:
        return ''
    else:
        if s[:1] == ' ':
            return trim(s[1:])
        if s[-1:] == ' ':
            return trim(s[:-1])
    return s
    

#the test code
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
