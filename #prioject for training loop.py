#prioject for training loop
good = []
not_good = []
a = input("Enter your tasks for today separated by commas: ").split(", ")
for y in a:
    c = input(f"Did you finish {y} already?").lower()
    if c == 'yes':
        good.append(y)
        print("Nice job!")
    else:
        not_good.append(y)
        print("Try not to put it down")
print(f"***** Done tasks ***** {good}")