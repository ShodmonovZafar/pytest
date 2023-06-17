
def add_length(str_: str):
    rel = str_.split()
    for i in range(len(rel)):
        rel[i] = f"{rel[i]} {len(rel[i])}"
    return rel

    

def main():
    print(add_length("you will win"))

if __name__ == "__main__":
    main()