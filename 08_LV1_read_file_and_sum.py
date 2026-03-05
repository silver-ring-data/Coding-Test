result = 0
with open('numbers.txt','r') as f:
  for line in f :
    result += int(line.strip())
print(result)
  
  