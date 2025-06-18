s = "racecar"
t = "carrace"

shmap = {}
thmap = {}

for i in range(len(s)):
    if s[i] in shmap:
        shmap[s[i]] += 1
    else:
        shmap[s[i]] = 1


for i in range(len(t)):
    if t[i] in thmap:
        thmap[t[i]] += 1
    else:
        thmap[t[i]] = 1    

if shmap == thmap:
    print(True)