def main():
    tea_type = input()
    guesses = input().split()
    right_guesses = guesses.count(tea_type)
    print(right_guesses)
main()