from selenium.webdriver.common.keys import Keys
import time
import ai.response as bot

def chat(driver, id, callActive, chatActive, thresh):
    window = driver.window_handles[id]
    driver.switch_to.window(window)
    update = False
    try:
        chatBoxWindow = "//*[@id='ow3']/div[1]/div/div[9]/div[3]/div[4]/div/div[2]/div[2]/div[2]/span[2]/div"
        onlineUsers = driver.find_element_by_xpath("//*[@id='ow3']/div[1]/div/div[9]/div[3]/div[4]/div/div[2]/div[2]/div[1]/div[1]/span/div/span[2]").text.lower()
        onlineUsers = onlineUsers[1:][:-1]
        chatBoxEl = driver.find_element_by_xpath(f'{chatBoxWindow}/div[4]/div[1]/div[1]/div[2]/textarea')

        if chatActive:
            chatboxPath = f"{chatBoxWindow}/div[2]/div[last()]"
            time.sleep(2)
            chatUser = driver.find_element_by_xpath(f"{chatboxPath}/div[1]/div[1]").text.lower()
            chatText = driver.find_element_by_xpath(f"{chatboxPath}/div[last()]/div[last()]").text.lower()
            time.sleep(2)
            if chatUser != "you":
                msg, tag, conf = bot.chatbot_response(chatText)
                if msg is not None:
                    if msg != ' ':
                        if conf >= thresh:
                            update = True
                            chatBoxEl.send_keys(msg, Keys.ENTER)
                    
                if conf < thresh or msg == " ":
                    f = open("ai/data/unknowns.txt", "a")
                    write = True
                    for line in open("ai/data/unknowns.txt").readlines():
                        line = line.rstrip("\n")
                        if line == chatText:
                            write = False
                            break

                    if write:
                        f.write(chatText + "\n")
                        

                    f.close()
    except Exception as e:
        onlineUsers = 0
        print(e)
    
    if not update:
        msg = ""
        chatText = ""
        conf = 0.0

    return update, chatText, str(msg), conf, onlineUsers

    print("> " + chatUser + " --> " + chatText)
    print("Confidence: " + str(conf))
    print("Tag: " + str(tag))
    print("Response: " + str(msg))
    print("\n")