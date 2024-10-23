import os


counter = 0
def get_id(number):
    a = len(str(number))
    di = []
    for i in range(4 - a):
        di.append("0")
    di.append(str(number))
    return "".join(di)

main_dir = os.getcwd()
print(main_dir)
for i in range(100):
    os.mkdir(f"./items/{get_id(counter)}")
    os.chdir(f"./items/{get_id(counter)}")
    with open("index.html", "x") as f:
        f.write("")
    os.chdir(main_dir)
    counter += 1