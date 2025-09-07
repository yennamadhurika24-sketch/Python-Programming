#calculate total number notes in a given amount

def Notes(amount):
    total_notes = 0
    if amount >= 2000:
        total_notes += amount // 2000
        print("2000 x", amount // 2000)
        amount = amount % 2000

    if amount >= 500:
        total_notes += amount // 500
        print("500 x", amount // 500)
        amount = amount % 500

    if amount >= 200:
        total_notes += amount // 200
        print("200 x", amount // 200)
        amount = amount % 200

    if amount >= 100:
        total_notes += amount // 100
        print("100 x", amount // 100)
        amount = amount % 100

    if amount >= 50:
        total_notes += amount // 50
        print("50 x", amount // 50)
        amount = amount % 50

    if amount >= 20:
        total_notes += amount // 20
        print("20 x", amount // 20)
        amount = amount % 20

    if amount >= 10:
        total_notes += amount // 10
        print("10 x", amount // 10)
        amount = amount % 10

    if amount >= 5:
        total_notes += amount // 5
        print("5 x", amount // 5)
        amount = amount % 5

    if amount >= 2:
        total_notes += amount // 2
        print("2 x", amount // 2)
        amount = amount % 2

    if amount >= 1:
        total_notes += amount // 1
        print("1 x", amount // 1)
        amount = amount % 1
    return total_notes
amount = int(input("Enter amount: "))
print("Total number of notes =",Notes(amount))
