def main():
    j_inicio = 7
    j_final = 4

    for i in range(1,10,2):
        
        for j in range(j_inicio,j_final,-1):
            print(f"I={i} J={j}")
            
        j_inicio += 2
        j_final += 2
main()