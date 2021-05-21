def main():
    hour, minute = input().split()
    hour = int(hour)
    minute = int(minute)
    if hour == 0 and minute < 45:
        tmp_m = 45 - minute
        hour = 23
        minute = 59 - tmp_m + 1
    elif minute < 45:
        hour -= 1
        minute += 60 - 45
    else:
        minute -= 45
    print(hour, minute)


if __name__ == '__main__':
    main()