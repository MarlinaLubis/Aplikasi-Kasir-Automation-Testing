from selenium.webdriver import Chrome

driver1 = Chrome()
driver2 = Chrome()
driver3 = Chrome()


driver1.get("https://www.google.com/?hl=ID")
driver2.get("https://github.com/rplulbi/sqa")
driver3.get("https://github.com/rplulbi/SQA/tree/main/Chapter3")
