from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, sys
import ai.response as bot


def main():
    f = open("data.txt")
    data = f.readlines(0)

    driver = webdriver.Remote(command_executor=data[0][:-1])
    driver.session_id = data[1]

    window = driver.window_handles[int(sys.argv[1])]
    driver.switch_to.window(window)

    chatBoxWindow = "//*[@id='ow3']/div[1]/div/div[9]/div[3]/div[4]/div/div[2]/div[2]/div[2]/span[2]/div"
    onlineUsers = driver.find_element_by_xpath("//*[@id='ow3']/div[1]/div/div[9]/div[3]/div[4]/div/div[2]/div[2]/div[1]/div[1]/span/div/span[2]").text.lower()
    onlineUsers = onlineUsers[1:][:-1]
    chatBoxEl = driver.find_element_by_xpath(f'{chatBoxWindow}/div[4]/div[1]/div[1]/div[2]/textarea')
    print("Online: " + onlineUsers)

    while True:
        chatboxPath = f"{chatBoxWindow}/div[2]/div[last()]"
        time.sleep(2)
        chatUser = driver.find_element_by_xpath(f"{chatboxPath}/div[1]/div[1]").text.lower()
        chatText = driver.find_element_by_xpath(f"{chatboxPath}/div[last()]/div[last()]").text.lower()
        time.sleep(2)
        if chatUser != "you":
            msg, tag, conf = bot.chatbot_response(chatText)
            if msg is not None:
                if msg != ' ':
                    chatBoxEl.send_keys(msg, Keys.ENTER)
            
            print("> " + chatUser + " --> " + chatText)
            print("Confidence: " + str(conf))
            print("Tag: " + str(tag))
            print("Response: " + str(msg))
            print("\n")

            if conf == 0.0:
                f = open("ai/data/unknowns.txt", "a")
                write = True
                for line in open("ai/data/unknowns.txt").readlines():
                    if line == chatText:
                        write = False
                        break

                if write:
                    f.write(chatText)

                f.close()

main()