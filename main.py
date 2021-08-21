# This is a sample Python script.
print("TESTING USING SELENIUM")
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.thesparksfoundationsingapore.org/")
driver.maximize_window()
print("******************************Testcases started******************************")

# Testcase_1#
print("***Testcase_1 started***")
if (driver.title):
    print("Title verified \n testcase 1 verified", driver.title)
else:
    print("Title not verified")

# Testcase_2#
print("***Testcase_2 started***")
logo = driver.find_element_by_xpath("//img[@src='/images/logo_small.png']")
if logo.is_displayed():
    print("logo exists")
else:
    print("logo not found")

# Testcase_3#

print("***Testcase_3 started***")
try:
    driver.find_element_by_class_name("navbar")
    time.sleep(7)
    print("Navigation bar presence is verified ")
except NoSuchElementException:
    print("Navigation bar is not present")

# Testcase_4#

print("***Testcase_4 started***")
try:
    driver.find_element_by_link_text("About Us").click()
    time.sleep(3)
    driver.find_element_by_link_text("Vision, Mission and Values").click()
    time.sleep(3)
    print(" Vision, Mission and Values page is verified")
    driver.find_element_by_link_text("Corporate Partners").click()
    time.sleep(3)
    print("Corporate Partners verified")
except NoSuchElementException:
    print("About us  page not verified")

# Testcase_5#
print("***Testcase_5 started***")
try:
    driver.find_element_by_link_text("Policies and Code").click()
    time.sleep(3)
    driver.find_element_by_link_text("Policies").click()
    time.sleep(3)
    print("policies page verified")
    driver.find_element_by_link_text("Service Quality Values").click()
    time.sleep(3)
    print("Service Quality Values page verified")
except NoSuchElementException:
    print("policies and code  page not verified")

# Testcase_6#
print("***Testcase_6 started***")
try:
    driver.find_element_by_link_text("Programs").click()
    time.sleep(3)
    driver.find_element_by_link_text("Workshops").click()
    time.sleep(3)
    driver.find_element_by_link_text("Glimpses for Kids").click()
    time.sleep(3)
    driver.find_element_by_link_text("Resume Writing")
    print("programs page verified ")
    print("workshops page found")
    print("Glimpses for kids page poster found ")
    print("resume writing poster found")
except NoSuchElementException:
    print("programs  not verified")

handles = driver.window_handles
for i in handles:
    driver.switch_to.window(i)
    if driver.title == "frames and windows":
        time.sleep(3)
        driver.quit()
time.sleep(3)

# Testcase_7#
print("***Testcase_7 started***")
try:
    driver.find_element_by_link_text("LINKS").click()
    time.sleep(3)
    driver.find_element_by_link_text("AI in Education").click()
    time.sleep(3)
    print("links page verified ")
except NoSuchElementException:
    print("links page is not verified")

# Testcase_8#
print("***Testcase_8 started***")
try:
    driver.find_element_by_link_text("LINKS App").click()
    time.sleep(3)
    print("links app  verified ")
except NoSuchElementException:
    print("links app  is not verified")

# Testcase_9#
print("***Testcase_9 started***")
try:
    driver.find_element_by_link_text("Join Us").click()
    time.sleep(3)
    driver.find_element_by_link_text("Why Join Us").click()
    time.sleep(3)
    print("Why Join Us page verified")
    driver.find_element_by_link_text("Internship Positions").click()
    time.sleep(3)
    print("Internship Positions page verified")
except NoSuchElementException:
    print("Join us   page not verified")

# Testcase_10#
print("***Testcase_10 started***")
try:
    driver.find_element_by_link_text("Contact Us").click()
    time.sleep(3)
    contact = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[3]/div[2]/p[2]")
    if contact.is_displayed():
        print("contact address found")
    else:
        print("contact address not found")
    print("contact us page is verified")
except NoSuchElementException:
    print("conatct us page is  not verified")

driver.quit()
