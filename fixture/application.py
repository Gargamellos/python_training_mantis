from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper
from selenium.webdriver.chrome.webdriver import WebDriver


class Application:

    def __init__(self, browser, base_url):
        if browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()


    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def open_project_page(self):
        wd = self.wd
        wd.get("http://localhost:8080/mantisbt-1.2.19/login_page.php")

    def login(self, username, password):
        wd = self.wd
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys(username)
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_css_selector("input.button").click()

    def open_project(self):
        wd = self.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def create_project(self, project):
        wd = self.wd
        # init new project
        wd.find_element_by_xpath("//table[3]/tbody/tr[1]/td/form/input[2]").click()
        # fill project firm
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.name)
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys(project.description)
        # add project
        wd.find_element_by_css_selector("input.button").click()

    def return_project_page(self):
        wd = self.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def destroy(self):
        self.wd.quit()