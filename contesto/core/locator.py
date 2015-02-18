# coding: utf-8

from functools import partial

from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy


class ContestoBy(By):
    SIZZLE = "sizzle"


class Locator(dict):
    def __init__(self, by, value):
        super(Locator, self).__init__()
        self['by'] = by
        self['value'] = value


class JavaUiSelector(str):
    def __new__(cls, data=None):
        if data is None:
            data = unicode("new UiSelector()")
        return str.__new__(cls, data)

    def description(self, desc):
        return JavaUiSelector(self + '.description("%s")' % desc)

    def description_contains(self, desc):
        return JavaUiSelector(self + '.descriptionContains("%s")' % desc)


by_id = partial(Locator, By.ID)
by_xpath = partial(Locator, By.XPATH)
by_link_text = partial(Locator, By.LINK_TEXT)
by_partial_link_text = partial(Locator, By.PARTIAL_LINK_TEXT)
by_name = partial(Locator, By.NAME)
by_tag_name = partial(Locator, By.TAG_NAME)
by_class_name = partial(Locator, By.CLASS_NAME)
by_css_selector = partial(Locator, By.CSS_SELECTOR)

by_uiautomator = partial(Locator, MobileBy.ANDROID_UIAUTOMATOR)
by_uiautomation = partial(Locator, MobileBy.IOS_UIAUTOMATION)
by_accessibility_id = partial(Locator, MobileBy.ACCESSIBILITY_ID)

by_sizzle = partial(Locator, ContestoBy.SIZZLE)