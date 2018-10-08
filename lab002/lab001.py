# coding:utf8
import time
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.0.0'
desired_caps['deviceName'] = 'Genymotion'
desired_caps['appPackage'] = 'com.android.calculator2'
desired_caps['appActivity'] = '.Calculator'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.find_element_by_id("com.android.calculator2:id/digit_1").click()
driver.find_element_by_id("com.android.calculator2:id/digit_5").click()
driver.find_element_by_id("com.android.calculator2:id/digit_9").click()

driver.find_element_by_id("com.android.calculator2:id/del").click()
driver.find_element_by_id("com.android.calculator2:id/digit_9").click()
driver.find_element_by_id("com.android.calculator2:id/digit_5").click()

driver.find_element_by_id("com.android.calculator2:id/op_add").click()

driver.find_element_by_id("com.android.calculator2:id/digit_6").click()

driver.find_element_by_id("com.android.calculator2:id/eq").click()

time.sleep(1000)
driver.quit()
