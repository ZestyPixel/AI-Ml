with open("sample.txt", "r", encoding="utf-8") as f:
    data = f.readlines()
    count = 1
    for sentence in data:
        if "fang" in sentence.lower():
            print(f"Found it at line {count}")
            break
        count = count + 1
    else: #Here else belongs to for loop not if statement. It will be executed if for loop is exhausted without break. For-else in python is similar to while-else.
        print("Not found")