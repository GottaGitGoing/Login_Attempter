import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def enter_site():
    password = input("Enter the password")
    user_id = input("Enter ID")
    driver.get('[A_Specific_Website_UsefForLogin');
    search_box = driver.find_element_by_name('[Div_with_ID]')
    time.sleep(0)
    search_box.send_keys(user_id)
    time.sleep(0)
    passsbox = driver.find_element_by_name('password')
    time.sleep(0)
    passsbox.send_keys(password)
    time.sleep(0)
    submiter = driver.find_element_by_name('login_button')
    time.sleep(0)
    submiter.send_keys(Keys.ENTER)


enter_site()


enter_site()
while driver.find_element_by_class_name("DivLogoutMsg"):
    enter_site()



# for quiting
# driver.f
# driver.quit()

