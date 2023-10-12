import time
from playwright.sync_api import sync_playwright

def slice_str_before(my_string, sub):
    index = my_string.find(sub)
    return my_string[index:]

def slice_str_after(my_string, sub):
    index = my_string.find(sub)
    return my_string[:index]

cproeis_url = 'https://www.proeis.rj.gov.br'

with sync_playwright() as p:

    browser = p.chromium.launch()
    context = browser.new_context()
    page = context.new_page()
    page.goto(cproeis_url)
    page.wait_for_load_state('load')

    page.select_option("#ddlTipoAcesso", value='CPF')
    page.wait_for_load_state('load')

    '''
    captcha_image_xpath = '//*[@id="captcha"]/div'
    captcha_image_div = page.locator(captcha_image_xpath)
    captcha_image_div_style = captcha_image_div.evaluate('(element) => element.style.cssText')

    str_first_slice = slice_str_before(captcha_image_div_style, 'data')
    str_second_slice = slice_str_after(str_first_slice, '"')
    print(str_second_slice)
    '''

    captcha_image_path = '//*[@id="captcha"]/div'
    captcha_image_div = page.locator(captcha_image_path)
    path = 'captcha_screenshot.png'
    captcha_image_div.screenshot(path=path)

    browser.close()

