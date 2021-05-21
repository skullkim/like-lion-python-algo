import sys


def main():
    test_cases = int(sys.stdin.readline())
    while test_cases > 0:
        num1, num2 = sys.stdin.readline().rstrip().split()
        print(int(num1) + int(num2))
        test_cases -= 1


if __name__ == '__main__':
    main()
