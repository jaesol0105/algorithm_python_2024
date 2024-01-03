word = input()
dic = dict()
  
for i in range(len(word)):
  if word[i].upper() in dic:
    dic[word[i].upper()] += 1
  else:
    dic[word[i].upper()] = 1

result = [k for k,v in dic.items() if max(dic.values()) == v]

if len(result) == 1:
  print(result[0])
else:
  print("?")