import selenium.webdriver
from selenium.webdriver.chrome import options
import selenium.webdriver.chrome
from selenium.webdriver.firefox.options import Options as firefoxoptions


from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

cap_map = {
    "firefox": DesiredCapabilities.FIREFOX.copy(),
    "internet explorer": DesiredCapabilities.INTERNETEXPLORER.copy(),
    "internetexplorer": DesiredCapabilities.INTERNETEXPLORER.copy(),
    "iexplorer": DesiredCapabilities.INTERNETEXPLORER.copy(),
    "ie": DesiredCapabilities.INTERNETEXPLORER.copy(),
    "chrome": DesiredCapabilities.CHROME.copy(),
    "opera": DesiredCapabilities.OPERA.copy(),
    "phantomjs": DesiredCapabilities.PHANTOMJS.copy(),
    "htmlunitjs": DesiredCapabilities.HTMLUNITWITHJS.copy(),
    "htmlunit": DesiredCapabilities.HTMLUNIT.copy(),
    "iphone": DesiredCapabilities.IPHONE.copy(),
    "ipad": DesiredCapabilities.IPAD.copy(),
    "android": DesiredCapabilities.ANDROID.copy(),
    "edge": DesiredCapabilities.EDGE.copy(),
    "safari": DesiredCapabilities.SAFARI.copy()
}

browser_options = {
    "firefox": firefoxoptions,
}
chromeoptions = options.Options()
cr = chromeoptions.add_argument("--start-maximized")

caps = cap_map['chrome']
browser = selenium.webdriver.Chrome(chromeoptions)
#browser = selenium.webdriver.Remote(command_executor='http://10.0.0.3:5555/wd/hub', desired_capabilities=caps, browser_profile=None)

browser.get('http://hrm.seleniumminutes.com')

browser.find_element_by_id('txtUsername').send_keys('admin')
browser.find_element_by_id('txtPassword').send_keys('Password')
browser.find_element_by_id('btnLogin').click()

browser.quit()