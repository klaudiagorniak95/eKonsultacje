class Locators():

    # login page locators
    login_input_xpath = "//input[@id='login'][@name='login']"
    password_input_xpath = "//input[@id='password'][@name='password']"
    submit_button_xpath = "//button[@class='ladda-button btn btn-lg btn-primary'][@type='submit']"

    # home page locators
    profile_button_xpath = '//button[@type="button"][@aria-haspopup="true"]'
    logout_button_xpath = '//button[@type="button"][text()="Wyloguj"]'

    # home page menu locators
    konsultacje_link_xpath = '//a[@class="metismenu-link"][@href="/konsultacje"][text()="Konsultacje"]'

    # konsultacje locators
    konsultacje_new_xpath = '//button[@type="button"][@class="mb-2 mr-2 btn-icon btn btn-success"]'