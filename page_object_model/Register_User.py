from modules import *

def Register_user(driver,
                  url,
                  name,
                  email,
                  title,
                  password,
                  day,
                  month,
                  year,
                  first_name,
                  last_name,
                  company,
                  address,
                  address2,
                  country,
                  state,
                  city,zipcode,
                  mobile):

    driver.get(url)
    home_page_text = driver.find_element(By.XPATH,"//div[@class='features_items']/h2").text
    assert "FEATURES ITEMS" in home_page_text

    driver.find_element(By.XPATH,"//div[@class='col-sm-8']/div/ul/li[4]/a").click()

    signup_page_text = driver.find_element(By.XPATH,"//div[@class='signup-form']/h2").text
    assert "New User Signup!" in signup_page_text

    driver.find_element(By.XPATH,"//form[@action='/signup']//input[2]").send_keys(name)
    driver.find_element(By.XPATH,"//form[@action='/signup']//input[3]").send_keys(email)
    driver.find_element(By.XPATH,"//button[text()='Signup']").click()

    signup_page2_text = driver.find_element(By.XPATH,"//b[text()='Enter Account Information']").text
    assert "ENTER ACCOUNT INFORMATION" in signup_page2_text


    driver.find_element(By.XPATH,f"//input[@value='{title}']").click()
    driver.find_element(By.ID,"password").send_keys(password)
    driver.find_element(By.ID,"days").send_keys(day)
    driver.find_element(By.ID,"months").send_keys(month)
    driver.find_element(By.ID,"years").send_keys(year)
    driver.find_element(By.ID,"newsletter").click()
    driver.find_element(By.ID,"optin").click()
    driver.find_element(By.ID,"first_name").send_keys(first_name)
    driver.find_element(By.ID,"last_name").send_keys(last_name)
    driver.find_element(By.ID,"company").send_keys(company)
    
    driver.find_element(By.ID,"address1").send_keys(address)
    driver.find_element(By.ID,"address2").send_keys(address2)

    countries = Select(driver.find_element(By.ID,"country"))
    countries.select_by_value(country)
    driver.find_element(By.ID,"state").send_keys(state)
    driver.find_element(By.ID,"city").send_keys(city)
    driver.find_element(By.ID,"zipcode").send_keys(zipcode)
    driver.find_element(By.ID,"mobile_number").send_keys(mobile)
    driver.find_element(By.XPATH,"//button[@data-qa='create-account']").click()

    wait = WebDriverWait(driver,5)
    wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//b[text()='Account Created!']")))
    account_created_text = driver.find_element(By.XPATH,"//b[text()='Account Created!']").text
    assert "ACCOUNT CREATED" in account_created_text

    driver.find_element(By.XPATH,"//a[text()='Continue']").click()

    logged_in_text = driver.find_element(By.XPATH,"//div[@class='col-sm-8']//ul//li[10]//a").text

    assert f"Logged in as {name}" in logged_in_text