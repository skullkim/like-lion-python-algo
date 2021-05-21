import sys


def main():
    lines = int(sys.stdin.readline().strip())
    for i in range(1, lines + 1):
        for k in range(1, i + 1):
            sys.stdout.write('*')
        sys.stdout.write('\n')


if __name__ == '__main__':
    main()
