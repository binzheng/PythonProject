from selenium import webdriver
import datetime
import time

def login():
    # 打开小春首页，通过扫码登录
    browser.get("https://www.incnjp.com/member.php?mod=logging&action=login")
    time.sleep(3)
    print("Login画面打开")

    if browser.find_element_by_id("logicon1"):
        browser.find_element_by_id("logicon1").click()
    
    time.sleep(5)

    print("显示登陆框")

	
    if browser.find_element_by_name("username"):
        browser.find_element_by_name("username").send_keys("yyyyyyyyy")

    print("输入用户名")

    if browser.find_element_by_name("password"):
        browser.find_element_by_name("password").send_keys("xxxxxxxxxx")

    print("输入密码")
      

    if browser.find_element_by_name("loginsubmit"):
        browser.find_element_by_name("loginsubmit").click()

    print("需要输入验证码")
    time.sleep(10)


def updatePost(times):
    while True:
        now = datetime.datetime.now().strftime('%H:%M')
        nowMintues = int(datetime.datetime.now().strftime('%M'))
        print("now:"+now)
        # print("nowMintues:"+nowMintues)
        # 指定的时间
        if now in times:
            # 发表回复
            while True:
                try:
                    browser.get("https://www.incnjp.com/forum.php?mod=viewthread&tid=4751465&page=10#pid967439521")
                    if browser.find_element_by_id("fastpostmessage"):
                        browser.find_element_by_id("fastpostmessage").send_keys("欢迎大家加入")
                        browser.find_element_by_id("fastpostsubmit").click()
                        print("发表回复成功")
                        break
                except:
                    pass
        # 5分钟进行一次页面刷新
        elif (nowMintues % 5 == 0) :
            # 更新页面
            while True:
                try:
                    browser.get("https://www.incnjp.com/forum.php?mod=viewthread&tid=4751465&page=10#pid967439521")
                    time.sleep(5)
                    print("更新页面")
                    break
                except:
                    print("再次尝试提交订单")
        # 1分钟执行一次
        time.sleep(60)


if __name__ == "__main__":

    # 请指定自动回复时间，时间格式："06:00"
    times = ["09:00","15:00","17:00","21:00"]

    # 自动打开Chrome浏览器
    browser = webdriver.Chrome("C:\seleniumDriver\chromedriver.exe")
    # 设置浏览器最大化显示
    browser.maximize_window()

    # 扫码登录淘宝
    login()
    # 回复和刷新
    updatePost(times)
