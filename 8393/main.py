def main():
    limit = int(input())
    ans = 0
    for i in range(1, limit + 1):
        ans += i
    print(ans)


if __name__ == '__main__':
    main()
