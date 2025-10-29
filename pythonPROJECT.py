challenges = [
    "Drink a full glass of water.",
    "Organize one small area of your workspace.",
    "Reply to one pending message or email.",
    "Write down three tasks you will do today.",
    "Take a five-minute stretch break.",
    "Read five minutes of an educational article or book.",
    "Do a 60-second deep-breathing exercise.",
    "Plan tomorrow's top three priorities.",
    "Delete or archive five unnecessary files.",
    "Walk for five minutes to reset your focus."
]

levels = {}
completed = set()

print("welcome to productivity chooser!")
print(" the rules are simple you blindly choose a number 1-10, and a challenge will be given to you for it to be fun you have to do the challenge!")
print("First of all players must create their account before starting!(can be solo): ")
account_1 = input("first account: ")
levels[account_1] = 1

another_account = input("do you want to create another player?: ")
ans1 = another_account.strip().lower()
if ans1 in ("y", "yes"):
    account_2 = input("secound account: ")
    levels[account_2] = 1

    another_account2 = input("do you want to create another player?: ")
    ans2 = another_account2.strip().lower()
    if ans2 in ("y", "yes"):
        account_3 = input("third account: ")
        levels[account_3] = 1
        print("3 account created")
    else:
        print("2 account created")
else:
    print("1 account created")

while len(completed) < len(challenges):
    choosen_challenge = int(input("number 1-10: "))
    idx = choosen_challenge - 1
    if idx < 0 or idx >= len(challenges):
        continue
    if idx in completed:
        print("task already done")
        continue

    print(challenges[idx])

    who_did_it = input("which account did the challenge?: ")
    if who_did_it in levels:
        done = input("did the challenge get done? (Y/yes): ")
        if done.strip().lower() in ("y", "yes"):
            levels[who_did_it] += 1
            completed.add(idx)
            print(who_did_it, "is now level", levels[who_did_it])
    else:
        print("that account does not exist")

print("no task left")
