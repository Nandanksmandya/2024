from Library.read_excel import ReadExcel


class Fbmsg:
    rd = ReadExcel()
    lo = rd.chage_theme_locators()

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, u_name):
        if isinstance(u_name, float):
            u_name = str(int(u_name))
        locator = self.lo["uname"]
        self.driver.find_element(*locator).send_keys(u_name)

    def enter_pswd(self, pwd):
        if isinstance(pwd, float):
            pwd = (int(pwd))

        locator = self.lo["password"]
        self.driver.find_element(*locator).send_keys(pwd)

    def click_on_longin(self):
        locator = self.lo["login"]
        self.driver.find_element(*locator).click()

    def click_on_msg_icon(self):
        locator = self.lo["msgicon"]
        self.driver.find_element(*locator).click()
        locator1 = self.lo["see_all_msg"]
        self.driver.find_element(*locator1).click()

    def click_on_anychat(self):
        locator = self.lo["anychat"]
        self.driver.find_element(*locator).click()

    def send_msg(self, msg_):
        locator = self.lo["send_msgg"]
        self.driver.find_element(*locator).send_keys(msg_)
        locator1 = self.lo["send_button"]
        self.driver.find_element(*locator1).click()

    def log_out(self):
        locator = self.lo["a/control"]
        self.driver.find_element(*locator).click()
        locator1 = self.lo["logout"]
        self.driver.find_element(*locator1).click()
