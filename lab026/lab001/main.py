import sys


def test_for_sys(year, name, body):
    print('the year is', year)
    print('the name is', name)
    print('the body is', body)


if __name__ == '__main__':
    try:
        year, name, body = sys.argv[1:4]
        test_for_sys(year, name, body)
    except Exception as e:
        print(sys.argv)
        print(e)
