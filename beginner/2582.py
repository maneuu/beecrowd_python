nomes = [
    "PROXYCITY", "P.Y.N.G.", "DNSUEY!", "SERVERS", "HOST!", 
    "CRIPTONIZE", "OFFLINE DAY", "SALT", "ANSWER!", "RAR?", "WIFI ANTENNAS"
]

for _ in range(int(input())):
    # X, Y = [int(N) for N in input().split()]
    # print(nomes[X+Y])
    print(nomes[sum(int(N) for N in input().split())])