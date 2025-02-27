while True:
    try:
        # X derrota Y
        regras = {"pedra": "tesoura", "papel": "pedra", "tesoura": "papel"}  

        dodo, leo, pepper = input().split()  

        if regras[dodo] == leo and regras[dodo] == pepper: # Dodo venceu
            print("Os atributos dos monstros vao ser inteligencia, sabedoria...")  
        elif regras[leo] == dodo and regras[leo] == pepper: # Leo venceu
            print("Iron Maiden's gonna get you, no matter how far!")  
        elif regras[pepper] == dodo and regras[pepper] == leo: # Pepper venceu
            print("Urano perdeu algo muito precioso...")  
        else:  # Empate 
            print("Putz vei, o Leo ta demorando muito pra jogar...")  
    except EOFError: break