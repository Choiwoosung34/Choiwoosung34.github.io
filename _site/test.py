names = ["우성", "오이", "아토"]

with open("hello.txt", mode="a", encoding="utf-8") as hello:
    for index in range(4):
        try:
            hello.write("안녕: ")
            hello.write(f"{names[index]}!\n")
        except IndexError:
            pass
