from selenium import webdriver
from selenium.webdriver.common.by import By
import sys

def test_scores_service(app_url):
    try:
        driver = webdriver.Firefox()
        driver.get(app_url)
        element = driver.find_element(By.ID, "score")
        try:
            value = int(element.text)
            if 1 <= value <= 1000:
                return True
            else:
                return False
        except ValueError:
            return False
    except:
        return False
    finally:
        driver.quit()


def main_function():
    result = test_scores_service('http://127.0.0.1:5000/')
    if result:
        return sys.exit(0)
    else:
        return sys.exit(-1)


main_function()





