from src.pages.base_page import BasePage

from src.data.main_page_locators import *


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.button_section_map = {
            'about': ('#about', section_about_title),
            'services': ('#moreinfo', section_services_title),
            'projects': ('#cases', section_projects_title),
            'reviews': ('#Reviews', section_reviews_title),
            'contacts': ('#contacts', section_contacts_title),
            'choose_specialist': ('#specialists', section_specialists_title),
            'more_details': ('#moreinfo', section_services_title)
        }

    def click_menu_item(self, menu_item):
        menu_locators = {
            'about': menu_about,
            'services': menu_services,
            'projects': menu_projects,
            'reviews': menu_reviews,
            'contacts': menu_contacts,
            'choose_specialist': button_choose_specialist,
            'more_details': button_more_details
        }

        if menu_item in menu_locators:
            self.click_element(menu_locators[menu_item])
        else:
            raise ValueError(f"Неизвестный пункт меню: {menu_item}")

    def check_url_contains_anchor(self, anchor):
        current_url = self.get_current_url()
        return anchor in current_url

    def check_section_visible(self, section_locator):
        return self.is_element_visible(section_locator)

    def test_menu_navigation(self, menu_item):
        if menu_item not in self.button_section_map:
            raise ValueError(f"Неизвестный пункт меню для тестирования: {menu_item}")

        anchor, section_locator = self.button_section_map[menu_item]

        self.click_menu_item(menu_item)

        url_ok = self.check_url_contains_anchor(anchor)
        section_ok = self.check_section_visible(section_locator)

        return url_ok, section_ok