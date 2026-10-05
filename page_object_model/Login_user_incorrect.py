from modules import *


def Login_user_invalid(driver,url,email,password):
    driver.get(url)
    home_page_text = driver.find_element(By.XPATH,"//div[@class='features_items']/h2").text
    assert "FEATURES ITEMS" in home_page_text
    driver.find_element(By.XPATH,"//div[@class='col-sm-8']//ul//li[4]/a").click()
    
    login_page_text = driver.find_element(By.XPATH,"//div[@class='login-form']//h2").text
    assert "Login to your account" in login_page_text
    driver.find_element(By.XPATH,"//form[@action='/login']/input[2]").send_keys(email)
    driver.find_element(By.XPATH,"//form[@action='/login']/input[3]").send_keys(password)
    driver.find_element(By.XPATH,"//form[@action='/login']/button").click()

    wait = WebDriverWait(driver,5)
    wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//p[@style='color: red;']")))

    error_text = driver.find_element(By.XPATH,"//p[@style='color: red;']").text
    assert "Your email or password is incorrect!" in error_text
