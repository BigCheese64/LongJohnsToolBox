f=open('wordList.txt','w')
initials=input('>')
for a in range(10):
  a-=1
  for b in range(10):
    b-=1
    for c in range(10):
      c-=1
      for d in range(10):
        d-=1
        f.writeline(str(a)+str(b)+str(c)+str(d)+initials)
        
