def read_lines(path):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            yield line.rstrip("\n")


if __name__ == "__main__":
    for line in read_lines("practice/week1/demo.py"):
        print(line)
