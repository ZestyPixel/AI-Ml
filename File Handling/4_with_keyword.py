with open("sample.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

# with keyword: Automatically handles closing the file after the block is executed.