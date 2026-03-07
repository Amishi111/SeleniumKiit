from selenium import webdriver
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)


#Q1. Print the categories mentioned on top of Amazon website

driver.get("https://www.amazon.in/")
sleep(3)
categories = driver.find_elements(By.CSS_SELECTOR, "#nav-xshop a")
for c in categories:
    print(c.text)


#Q2. Print top 10 movie names from IMDb

driver.get("https://www.imdb.com/chart/top/")
sleep(3)
m = driver.find_elements(By.CSS_SELECTOR, "ul.ipc-metadata-list li h3")
for i in range(10):
    print(m[i].text)


#Q3. Count all images in Amazon

driver.get("https://www.amazon.in/")
sleep(3)
img = driver.find_elements(By.TAG_NAME, "img")
print(len(img))


#Q4. Target first dropdown in that page and select first option

driver.get('https://demoqa.com/select-menu')
sleep(2)
e=driver.find_element('xpath','//input[@id="react-select-2-input"]')
e.click()
sleep(1)
driver.find_element(By.XPATH,'//div[text()="Group 1, option 1"]').click()


#Q5. Print all links in Amazon

driver.get("https://www.amazon.in/")
sleep(3)
links = driver.find_elements(By.TAG_NAME, "a")
for link in links:
    print(link.get_attribute("href"))


#Q6. Print auto suggestions of any site

driver.get("https://www.amazon.in/")
sleep(3)
driver.find_element("id",'twotabsearchtextbox').send_keys('samsung')
sleep(3)
a=driver.find_elements("xpath","//div[@class='s-suggestion-container']")
for item in a:
    print(item.text)


#Q7. From the “Accounts & Lists” section on the Amazon homepage, select the “Your Wish List” option.

driver.get("https://www.amazon.in/")
sleep(3)
a = driver.find_element("id", "nav-link-accountList")
o = ActionChains(driver)
o.move_to_element(a).perform()
sleep(2)
driver.find_element(By.LINK_TEXT, "Your Wish List").click()


#Q8. Access the content displayed inside the embedded page and print the heading text visible inside it.

driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_iframe")
driver.switch_to.frame("iframeResult")
driver.switch_to.frame(0)
a = driver.find_element(By.TAG_NAME, "h1").text
print(a)

#Q9. Search Laptop and print all product titles.

driver.get("https://www.amazon.in/")
sleep(5)
a = driver.find_element("id", "twotabsearchtextbox")
a.send_keys("Laptop")
a.send_keys(Keys.ENTER)
sleep(3)
a = driver.find_elements("xpath", "//h2//span")
for i in a:
    print(i.text)

sleep(10)
driver.quit()