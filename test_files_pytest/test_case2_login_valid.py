from modules import *
from page_object_model import Login_user_correct


data_file = r"C:\Users\ASUS\Downloads\python\automation_selenium\data_files_json\Login_correct_credentials.json"
with open(data_file,"r") as data_file_json:
    data_file_python = json.load(data_file_json)
    data_data = data_file_python["data"]


@pytest.mark.login_valid
@pytest.mark.parametrize("data",data_data)
def test_login_user_valid(browser_fixture,data):
    driver = browser_fixture
    test_login = Login_user_correct
    test_login.Login_user_valid(driver,data["url"],data["email"],data["password"],data["name"])


