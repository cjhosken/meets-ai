from PyQt5.QtWidgets import QMessageBox
from selenium.webdriver.common.keys import Keys
import time
import ai.response as bot

def chat(app, driver, id, callActive, chatActive, thresh):
    window = driver.window_handles[id]
    driver.switch_to.window(window)

    try:
        chatBoxWindow = "/html/body/div[1]/c-wiz/div[1]/div/div[9]/div[3]/div[4]/div[2]/div[2]/div"
    except:
        onlineUsers = 0
        app.showErrorBox("XPath Error!", "Chatbox could not be found.")
        return False, "", "", 0.0, 0

    onlineUsers = driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div[1]/div/div[9]/div[3]/div[10]/div[3]/div[2]/div/div/div[2]/div/div").text.lower()
    onlineUsers = onlineUsers[1:][:-1]
    chatBoxEl = driver.find_element_by_xpath(f'{chatBoxWindow}/div[4]/div[1]/div[1]/div[2]/textarea')

    if chatActive:
        chatboxPath = f"{chatBoxWindow}/div[2]/div[last()]"
        chatUser = driver.find_element_by_xpath(f"{chatboxPath}/div[1]/div[1]").text.lower()
        chatText = driver.find_element_by_xpath(f"{chatboxPath}/div[last()]/div[last()]").text.lower()
        time.sleep(2)
        if chatUser != "you":
            msg, conf = bot.chatbot_response(chatText)
            if msg is not None:
                if msg != ' ' and conf >= thresh:
                    chatBoxEl.send_keys(msg, Keys.ENTER)
                    return True, chatText, str(msg), conf, onlineUsers
                else:
                    f = open("ai/data/unknowns.txt", "a")
                    for line in open("ai/data/unknowns.txt").readlines():
                        line = line.rstrip("\n")
                        if line == chatText:
                            break
                    else:
                        f.write(chatText + "\n")
                    f.close()

    if callActive:
        pass

    return False, "", "", 0.0, 0