from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys

f = open("data.txt")
data = f.readlines(0)

driver = webdriver.Remote(command_executor=data[0][:-1])
driver.session_id = data[1]

window = driver.window_handles[int(sys.argv[1])]
driver.switch_to.window(window)
chatBoxEl = driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[4]/div/div[2]/div[2]/div[2]/span[2]/div/div[4]/div[1]/div[1]/div[2]/textarea')
msg = "get SPAMMED"

while True:
    chatBoxEl.send_keys(msg, Keys.ENTER)