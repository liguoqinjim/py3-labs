import rpa as r


def lab001():
    r.init(visual_automation=True)
    print("reading...")
    print(r.read('data/01.jpg'))

    # r.init()
    # r.url('https://duckduckgo.com')
    # r.type('//*[@name="q"]', 'decentralisation[enter]')
    # r.wait()  # ensure results are fully loaded
    # r.snap('page', 'results.png')
    # r.close()


if __name__ == '__main__':
    lab001()
