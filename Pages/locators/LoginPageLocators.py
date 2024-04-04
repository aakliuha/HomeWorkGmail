class LoginPageLocators:
    email_field = '//input[@type="email"]'
    password_field = '//input[@type="password"]'
    next_btn = '//*[@id="identifierNext"]'
    greeting = '//header[@class="R3PZhd"]/h1'
    wrong_email_element = '//*[text()="Couldn’t find your Google Account"]'
    wrong_password_element = '//*[text()="Wrong password. Try again or click Forgot password to reset it."]'
    empty_email_element = '//*[text()="Enter an email or phone number"]'
    empty_password_element = '//*[text()="Enter a password"]'