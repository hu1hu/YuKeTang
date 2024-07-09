import time

from selenium import webdriver  # WebDriver 是 Selenium 中的一个关键接口，用于对浏览器进行控制和执行各种操作。
from selenium.webdriver.common.keys import Keys  # 用于模拟键盘输入
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as ac

# 雨课堂自动刷课脚本


# TODO 更换为自己的url（具体课程页面）
url = "https://changjiang.yuketang.cn/v2/web/studentLog/16978956"
# 设置cookie
# TODO 更换为自己的cookie
cookie = {'name': 'sessionid', 'value': 'catf5tpoi584n5k57ipgkcswn0nty4z'}  # 设置cookie
# TODO 更换为自己的并发数
concurrent = 5  # 并发数


# 选择浏览器类型
driver = webdriver.Chrome()
# 设置等待时间为10秒
wait = WebDriverWait(driver, 10)

driver.get(url)  # 打开网页

driver.add_cookie(cookie)  # 添加cookie
driver.refresh()  # 刷新页面

# 等待直到元素出现(成绩单）
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="tab-student_school_report"]/span'))).click()

# 等待直到元素出现(视频）
videos = wait.until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="pane-student_school_report"]/div/div[2]/section[2]/div[2]/ul')))
# 获取所有视频
video_list = videos.find_elements(By.TAG_NAME, 'li')

# 获取当前窗口句柄
main_window = driver.current_window_handle

# 遍历所有视频
for video in video_list[:-1]:
    # 切换回主窗口
    driver.switch_to.window(main_window)

    # 判断是否已完成
    var = video.find_elements(By.TAG_NAME, 'div')[2]
    if var.text == '已完成 详情':
        continue

    # 获取视频名称
    text = video.find_elements(By.TAG_NAME, 'div')[0].text
    print("播放：" + text)

    current = len(driver.window_handles)
    # 点击播放
    if video.is_enabled() and videos.is_displayed():
        video.find_elements(By.TAG_NAME, 'div')[0].click()
    else:
        continue
    # 等待新窗口打开
    wait.until(EC.number_of_windows_to_be(current + 1))

    # 获取所有窗口句柄
    all_handles = driver.window_handles
    # 切换到新窗口
    driver.switch_to.window(all_handles[-1])

    # 1.等待视频加载，按静音键
    wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="video-box"]/div/xt-wrap/xt-controls/xt-inner/xt-volumebutton/xt-icon'))).click()

    # 倍速播放
    speed = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="video-box"]/div/xt-wrap/xt-controls/xt-inner/xt-speedbutton/xt-speedvalue')))
    # 播放
    play = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="video-box"]/div/xt-wrap/xt-controls/xt-inner/xt-playbutton')))
    # 点击2倍速
    acs = ac(driver)
    acs.move_to_element(speed).perform()
    # 二倍数
    acs.move_by_offset(0, -180).move_by_offset(5, 0).click().perform()
    # 点击播放
    play.click()
    # 关闭当前窗口
    # driver.close()

    while len(driver.window_handles) > concurrent:
        time.sleep(10)

while len(driver.window_handles) > 1:
    time.sleep(10)
    print("等待窗口关闭")
