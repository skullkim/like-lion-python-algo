import sys


def main():
    nums, limit = sys.stdin.readline().strip().split()
    sequence = sys.stdin.readline().strip().split()
    for i in sequence:
        if int(i) >= int(limit) : continue
        sys.stdout.write(i + " ")


if __name__ == '__main__':
    main()