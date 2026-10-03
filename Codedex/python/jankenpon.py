import random

print("=" * 19)
print("Rock Paper Scissors")
print("=" * 19)

decision = {"1": "Rock", "2": "Paper", "3": "Scissors"}

print("1) ✊")
print("2) ✋")
print("3) ✌️")


while True:
    bot = random.randint(1, 3)
    user = input(
        "Pick a number, (1) Rock, (2) Paper, (3) Scissors, or q to quit: ")

    if user == "q":
        break

    if user not in decision:
        print("Please choose the correct option!")
        continue

    print(f"User choice: {decision[user]} | bot choice: {decision[str(bot)]}")

    if int(user) == bot:
        print("Tied!")
        break
    elif (int(user) - bot) % 3 == 1:
        print("User Win")
        break
    else:
        print("Bot Win")
        break
