def convert(input_str):
    return input_str.replace(":)", "🙂").replace(":(", "🙁")

def main():
    p = input()
    x = convert(p)
    print(x)

if __name__ == "__main__":
    main()
