#link  https://judge.beecrowd.com/pt/problems/view/1049
def main():
    valor1 = input() # vertebrado ou invertebrado
    valor2 = input() # classificação taxonômica do animai/insetos
    valor3 = input() # hábitat alimentar do animal/inseto

    if valor1 == "vertebrado":
        if valor2 == "ave":
            if valor3 == "carnivoro":
                animal ="aguia"

            elif valor3 == "onivoro":
                animal ="pomba"

        elif valor2 == "mamifero":
            if valor3 == "onivoro":
                animal ="homem"

            elif valor3 == "herbivoro":
                animal ="vaca"
    elif valor1 == "invertebrado":
        if valor2 == "inseto":
            if valor3 == "hematofago":
                animal ="pulga"

            elif valor3 == "herbivoro":
                animal ="lagarta"

        elif valor2 == "anelideo":
            if valor3 == "hematofago":
                animal ="sanguessuga"

            elif valor3 == "onivoro":
                animal ="minhoca"
    print(animal)
main()