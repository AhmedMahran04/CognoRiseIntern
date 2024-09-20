import random

def dice_face(num):
    dice_faces = {
        1: """\
 _______
|       |
|   *   |
|_______|""",
        2: """\
 _______
|  *    |
|       |
|____*__|""",
        3: """\
 _______
| *     |
|   *   |
|_____*_|""",
        4: """\
 ________
|  *   * |
|        |
|__*___*_|""",
        5: """\
 _______
| *   * |
|   *   |
|_*___*_|""",
        6: """\
 ________
|  *   * |
|  *   * |
|__*___*_|"""
    }
    print(dice_faces[num])

while True:
    print("""Do you want to roll the dice? 
If yes, then enter "yes" to roll the dice.""")
    roll = input("Enter your answer: ").strip().lower()

    if roll in ['yes']:
        while True:
            output = random.randint(1, 6)
            dice_face(output)

            reroll = input("Do you want to reroll the dice? "
                           "(Yes/No): ").strip().lower()
            if reroll not in ['yes']:
                print("Thanks for playing!")
                break
        break
    else:
        print("Thanks for playing!")
        break


