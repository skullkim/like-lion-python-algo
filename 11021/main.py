import sys


def main():
    test_cases = int(sys.stdin.readline().strip())
    for i in range(1, test_cases + 1):
        num1, num2 = sys.stdin.readline().strip().split()
        print('Case #', i, ': ', int(num1) + int(num2), sep='')


if __name__ == '__main__':
    main()