s = input()
b = s.find('h')
f = s[b + 1: len(s)]
f = f.replace('h', 'H', f.count('h') - 1)
s = s[0:b + 1] + f
print(s)