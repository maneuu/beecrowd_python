conjunto = set()
while True:
    try:
        conjunto.add(input())
    except EOFError:break
    
print(len(conjunto))