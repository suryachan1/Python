s={10,3,49,35,'iis',3,49}
print(s)

s.add(79)
s.update({1,67})
s.discard(5)
#s.remove(3)
print(s)

#frozen set is immutable
fs=frozenset(s) #convert set to frozen set
print(fs)
