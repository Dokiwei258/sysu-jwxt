from reconize import Pic2String
from selenium import webdriver, common
from PIL import Image
import time
if __name__ == '__main__':
    html = "https://cas-443.webvpn.sysu.edu.cn/cas/login?service=https://portal.sysu.edu.cn/management/shiro-cas"
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    browser = webdriver.Chrome(chrome_options=option)
    browser.get(html)
    print("成功打开网址")
    usn = input("请输入学号")
    psw = input("请输入密码")
    username = browser.find_element_by_name('username')
    username.send_keys(usn)
    password = browser.find_element_by_name('password')
    password.send_keys(psw)
    path = 'F:\\codelibrary\\python\\sysu-jwxt\\pic\\t01.png'
    try:
        picture_url = browser.get_screenshot_as_file(path)
    except BaseException as msg:
        print(msg)
    ran = Image.open(path)
    box=(386,401,475,431)
    ran.crop(box).save(path)
    ####
    text = input("请输入验证码")
    ####这步未来用自动化验证码得出
    captcha = browser.find_element_by_name('captcha')
    captcha.send_keys(text)
    #print(text)
    sub = browser.find_element_by_name('submit')
    sub.click()
    time.sleep(1)
    sub = browser.find_element_by_xpath('//*[@id="root"]/span/div/div[2]/div/div[1]/div[2]/div/div/div/button')
    sub.click()
    time.sleep(3)
    #browser.get_screenshot_as_file(path)






