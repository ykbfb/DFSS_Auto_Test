
from selenium import webdriver
import time


if __name__ == '__main__':
    driver = webdriver.Chrome()

    driver.get('http://www.baidu.com')
    driver.maximize_window()
    driver.implicitly_wait(20)
    time.sleep(1)

    #元素定位
    driver.find_element_by_id('kw').clear()
    driver.find_element_by_id('kw').send_keys('sina')

    driver.find_element_by_id('su').click()
    driver.find_element_by_partial_link_text('新浪首页').click()

    cunrent_win = driver.current_window_handle
    all_handles = driver.window_handles
    for handle in all_handles:
        if handle != cunrent_win:
            driver.switch_to.window(handle)
    time.sleep(5)
    # driver.close()#关闭当前窗口
    driver.quit()#关闭所有窗口

    # driver.find_element_by_name()
    # driver.find_element_by_class_name()
    # driver.find_element_by_css_selector()
    # driver.find_elements_by_xpath()
    #
    # driver.close()
    # driver.quit()
    # driver.switch_to.frame()
    # driver.switch_to.alert()








