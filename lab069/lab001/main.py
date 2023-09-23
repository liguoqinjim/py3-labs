from icecream import ic
from icecream import install

install()

ic.configureOutput(outputFunction=print)

if __name__ == '__main__':
    ic("abc")
