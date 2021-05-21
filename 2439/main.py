import sys


def main():
    lines = int(sys.stdin.readline().strip())
    for i in range(1, lines + 1):
        for k in range(i, lines):
            sys.stdout.write(' ')
        for kk in range(0, i):
            sys.stdout.write('*')
        sys.stdout.write('\n')


if __name__ == '__main__':
    main()