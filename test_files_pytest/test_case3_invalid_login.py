from modules import *
from page_object_model import Login_user_incorrect



data_file = r"C:\Users\ASUS\Downloads\python\automation_selenium\data_files_json\Login_incorrect_credentials.json"
with open(data_file,"r") as data_file_json:
    data_file_python = json.load(data_file_json)
    data_data = data_file_python["data"]


@pytest.mark.invalid_login
@pytest.mark.parametrize("data",data_data)
def test_logout_user(browser_fixture,data):
    driver = browser_fixture
    test_invalid_login = Login_user_incorrect
    test_invalid_login.Login_user_invalid(driver,data["url"],data["email"],data["password"])

