import sys


def main():
    limit = int(sys.stdin.readline().strip())
    for i in range(limit, 0, -1):
        sys.stdout.write(str(i) + "\n")


if __name__ == '__main__':
    main()
