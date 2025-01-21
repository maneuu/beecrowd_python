S = input().strip()

bit_count = S.count('1')

B = '0' if bit_count % 2 == 0 else '1'

result = S + B

print(result)
