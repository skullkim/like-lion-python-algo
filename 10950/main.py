def main():
    test_cases = int(input())
    while test_cases > 0:
        num1, num2 = input().split()
        num1 = int(num1)
        num2 = int(num2)
        print(num1 + num2)
        test_cases -= 1


if __name__ == '__main__':
    main()

