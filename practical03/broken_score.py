import random


def main():
    score = get_random()
    grade_score(score)


def get_random():
    score = random.randint(0, 100)
    print(score)
    return score


def grade_score(score):
    if score < 0 or score > 100:
        print("invalid score")
    elif score < 50:
        print("bad")
    elif score < 90:
        print("pass")
    else:
        print("excellent")


if __name__ == '__main__':
    main()
