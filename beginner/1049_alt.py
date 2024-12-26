def main():
    valor1 = input()  # vertebrado ou invertebrado
    valor2 = input()  # classificação taxonômica
    valor3 = input()  # hábitat alimentar

    animais = {
        ("vertebrado", "ave", "carnivoro"): "aguia",
        ("vertebrado", "ave", "ovivoro"): "pomba",
        
        ("vertebrado", "mamifero", "onivoro"): "homem",
        ("vertebrado", "mamifero", "herbivoro"): "vaca",

        ("invertebrado", "inseto", "hematofago"): "pulga",
        ("invertebrado", "inseto", "herbivoro"): "lagarta",

        ("invertebrado", "anelideo", "hematofago"): "sanguessuga",
        ("invertebrado", "anelideo", "onivoro"): "minhoca",
    }

    animal = animais[(valor1, valor2, valor3)]
    print(animal)

main()
