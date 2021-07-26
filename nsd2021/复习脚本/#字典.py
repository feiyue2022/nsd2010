#字典
adict = {'name':'tom','age':20}
bdict = {'qq':'498294810','email':'tom@tedu.cn'}
adict.update(bdict)
print(adict)

del adict['qq']
print(adict)

print(adict.pop('age'))

print(adict)
