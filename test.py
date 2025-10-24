
count_even = 0
count_odd = 0

print("برای خروج، عدد 0 را وارد کن.")

while True:
    number = int(input("یک عدد وارد کن: "))
    
    if number == 0:
        break

    if number % 2 == 0:
        print(f"{number} is even ✅")
        count_even += 1
    else:
        print(f"{number} is odd 🔢")
        count_odd += 1

