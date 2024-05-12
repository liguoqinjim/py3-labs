import asyncio
import time

from pyppeteer import launch


async def lab001():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://httpbin.org/ip')
    await page.screenshot({'path': 'data/example.png'})
    await browser.close()


async def lab002():
    # browser = await launch(headless=False, devtools=True)
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.setViewport({'width': 2560, 'height': 1440})  # Set the viewport size
    await page.goto('https://www.csindex.com.cn/#/about/newsCenter')

    # 打开资源管理器

    # 点击selector: #app > div > div > div:nth-child(2) > div > div.main-page > div.filter-wrap.pr > div.filter-content > div > div > div:nth-child(3) > div.filter-value
    await page.click('#app > div > div > div:nth-child(2) > div > div.main-page > div.filter-wrap.pr > div.filter-content > div > div > div:nth-child(3) > div.filter-value')
    # # 点击selector: #app > div > div > div:nth-child(2) > div > div.main-page > div.filter-wrap.pr > div.filter-content > div > div > div:nth-child(3) > div.filter-value > a > div > a:nth-child(2)
    await page.click('#app > div > div > div:nth-child(2) > div > div.main-page > div.filter-wrap.pr > div.filter-content > div > div > div:nth-child(3) > div.filter-value > a > div > a:nth-child(2)')

    # 点击input: #app > div > div > div:nth-child(2) > div > div.main-page > div.filter-wrap.pr > div.search-wrapper.zh > div > input
    # await page.click('#app > div > div > div:nth-child(2) > div > div.main-page > div.filter-wrap.pr > div.search-wrapper.zh > div')
    # focus input
    # await page.focus('#app > div > div > div:nth-child(2) > div > div.main-page > div.filter-wrap.pr > div.search-wrapper.zh > div > input')
    # 输入文字： 沪深300
    # await page.keyboard.type('沪深300')
    await page.type('#app > div > div > div:nth-child(2) > div > div.main-page > div.filter-wrap.pr > div.search-wrapper.zh > div > input', '沪深300')
    # 解除焦点
    # await page.click('#app > div > div > div:nth-child(2) > div > div.main-page > div.filter-wrap.pr > div.search-wrapper.zh > div')

    # 点击button: #app > div > div > div:nth-child(2) > div > div.main-page > div.filter-wrap.pr > div.search-wrapper.zh > div > div > button
    await page.click('#app > div > div > div:nth-child(2) > div > div.main-page > div.filter-wrap.pr > div.search-wrapper.zh > div > div > button')
    # 把鼠标移动到button
    # await page.hover('#app > div > div > div:nth-child(2) > div > div.main-page > div.filter-wrap.pr > div.search-wrapper.zh > div > div > button')
    # 点击button
    # await page.mouse.down()

    # 等待5秒
    # await asyncio.sleep(5)

    # 点击第一行： #app > div > div > div:nth-child(2) > div > div.main-page > div.result-wrapper > div.ivu-table-wrapper.ivu-table-wrapper-with-border > div.ivu-table.ivu-table-default.ivu-table-border.ivu-table-stripe > div.ivu-table-body > table > tbody > tr:nth-child(1)
    # await page.click('#app > div > div > div:nth-child(2) > div > div.main-page > div.result-wrapper > div.ivu-table-wrapper.ivu-table-wrapper-with-border > div.ivu-table.ivu-table-default.ivu-table-border.ivu-table-stripe > div.ivu-table-body > table > tbody > tr:nth-child(1)')

    # 再次搜索
    # await page.click('#app > div > div > div:nth-child(2) > div > div.main-page > div.filter-wrap.pr > div.search-wrapper.zh > div')

    # 获取页面内容
    await page.screenshot({'path': 'data/example.png'})

    await browser.close()

    # time.sleep(600)


if __name__ == '__main__':
    # asyncio.get_event_loop().run_until_complete(lab001())
    asyncio.get_event_loop().run_until_complete(lab002())
