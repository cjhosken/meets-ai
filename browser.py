  
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import sys

error = False
try:
    import config
except:
    print("No config file detected. Make sure you rename configexample.py to config.py")
    sys.exit()

opt=Options()
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.notifications": 1
})

driver = webdriver.Chrome(options=opt, executable_path='./chromedriver.exe')
url = driver.command_executor._url
id = driver.session_id

print(url)
print(id)

f = open("data.txt", "w")
f.write(f"{url}\n{id}")

def login(driver):
    driver.get('https://accounts.google.com/ServiceLogin/identifier?service=classroom&passive=1209600&continue=https%3A%2F%2Fclassroom.google.com%2F&followup=https%3A%2F%2Fclassroom.google.com%2F&emr=1&flowName=GlifWebSignIn&flowEntry=AddSession')

    username=driver.find_element_by_id('identifierId')
    username.click()
    username.send_keys(config._email)

    next=driver.find_element_by_css_selector('#identifierNext button')
    next.click()

    time.sleep(2)
    passwordEl=driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    passwordEl.click()
    passwordEl.send_keys(config._password)

    next=driver.find_element_by_css_selector('#passwordNext button')
    next.click()

    print("Google Sign-in Complete.")
    time.sleep(5)

login(driver)