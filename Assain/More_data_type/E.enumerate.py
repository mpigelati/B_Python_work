prog_lagn = ['Python', 'C-Lang', 'Java']
enumerateprog_lagn = enumerate(prog_lagn)
print(type(enumerateprog_lagn))
print(list(enumerateprog_lagn))


enumerateprog_lagn = enumerate(prog_lagn, 10)
print(list(enumerateprog_lagn))

print ("")
prog_lagn = ['Python', 'C-Lang', 'Java']
for item in enumerate(prog_lagn):
  print(item)

print ("")
for i, temp in enumerate(prog_lagn):
  print(i, temp)

print ("")
# changing default start value
for i, item in enumerate(prog_lagn, 100):
  print(i, item)

#print enumerateprog_lagn['Python']
