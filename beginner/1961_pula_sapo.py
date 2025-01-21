def main():
    max_jump, total_pipes = [int(num) for num in input().split()]
    pipe_heights = [int(num) for num in input().split()]

    lose = False
    for i in range(len(pipe_heights) - 1):
        if abs(pipe_heights[i] - pipe_heights[i + 1]) > max_jump:
            lose = True
            break

    print("GAME OVER" if lose else "YOU WIN")

main()
