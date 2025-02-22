def all_variants(text):
    n = len(text)
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            yield text[i:i + length]

def main():
    a = all_variants("abc")
    for i in a:
        print(i)

if __name__ == "__main__":
    main()