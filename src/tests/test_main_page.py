import pytest
from src.data.main_page_locators import *


class TestMainPageNavigation:

    def test_about_navigation(self, main_page):
        """Проверка навигации к разделу 'О нас'"""
        print("=== Тест: Навигация к разделу 'О нас' ===")

        # Кликаем на пункт меню 'О нас'
        main_page.click_menu_item('about')
        print("✓ Кликнули на 'О нас'")

        # Проверяем, что URL содержит якорь #about
        current_url = main_page.get_current_url()
        print(f"Текущий URL: {current_url}")
        assert "#about" in current_url, f"URL не содержит #about. Текущий URL: {current_url}"
        print("✓ URL содержит правильный якорь #about")

        # Проверяем видимость раздела 'О нас'
        is_visible = main_page.check_section_visible(section_about_title)
        assert is_visible, "Раздел 'О нас' не виден после навигации"
        print("✓ Раздел 'О нас' успешно отображается")

        print("✅ Тест пройден успешно!\n")

    def test_services_navigation(self, main_page):
        """Проверка навигации к разделу 'Услуги'"""
        print("=== Тест: Навигация к разделу 'Услуги' ===")

        # Кликаем на пункт меню 'Услуги'
        main_page.click_menu_item('services')
        print("✓ Кликнули на 'Услуги'")

        # Проверяем, что URL содержит якорь #moreinfo
        current_url = main_page.get_current_url()
        print(f"Текущий URL: {current_url}")
        assert "#moreinfo" in current_url, f"URL не содержит #moreinfo. Текущий URL: {current_url}"
        print("✓ URL содержит правильный якорь #moreinfo")

        # Проверяем видимость раздела 'Услуги'
        is_visible = main_page.check_section_visible(section_services_title)
        assert is_visible, "Раздел 'Услуги' не виден после навигации"
        print("✓ Раздел 'Услуги' успешно отображается")

        print("✅ Тест пройден успешно!\n")

    def test_projects_navigation(self, main_page):
        """Проверка навигации к разделу 'Проекты'"""
        print("=== Тест: Навигация к разделу 'Проекты' ===")

        # Кликаем на пункт меню 'Проекты'
        main_page.click_menu_item('projects')
        print("✓ Кликнули на 'Проекты'")

        # Проверяем, что URL содержит якорь #cases
        current_url = main_page.get_current_url()
        print(f"Текущий URL: {current_url}")
        assert "#cases" in current_url, f"URL не содержит #cases. Текущий URL: {current_url}"
        print("✓ URL содержит правильный якорь #cases")

        # Проверяем видимость раздела 'Проекты'
        is_visible = main_page.check_section_visible(section_projects_title)
        assert is_visible, "Раздел 'Проекты' не виден после навигации"
        print("✓ Раздел 'Проекты' успешно отображается")

        print("✅ Тест пройден успешно!\n")

    def test_reviews_navigation(self, main_page):
        """Проверка навигации к разделу 'Отзывы'"""
        print("=== Тест: Навигация к разделу 'Отзывы' ===")

        # Кликаем на пункт меню 'Отзывы'
        main_page.click_menu_item('reviews')
        print("✓ Кликнули на 'Отзывы'")

        # Проверяем, что URL содержит якорь #Reviews
        current_url = main_page.get_current_url()
        print(f"Текущий URL: {current_url}")
        assert "#Reviews" in current_url, f"URL не содержит #Reviews. Текущий URL: {current_url}"
        print("✓ URL содержит правильный якорь #Reviews")

        # Проверяем видимость раздела 'Отзывы'
        is_visible = main_page.check_section_visible(section_reviews_title)
        assert is_visible, "Раздел 'Отзывы' не виден после навигации"
        print("✓ Раздел 'Отзывы' успешно отображается")

        print("✅ Тест пройден успешно!\n")

    def test_contacts_navigation(self, main_page):
        """Проверка навигации к разделу 'Контакты'"""
        print("=== Тест: Навигация к разделу 'Контакты' ===")

        # Кликаем на пункт меню 'Контакты'
        main_page.click_menu_item('contacts')
        print("✓ Кликнули на 'Контакты'")

        # Проверяем, что URL содержит якорь #contacts
        current_url = main_page.get_current_url()
        print(f"Текущий URL: {current_url}")
        assert "#contacts" in current_url, f"URL не содержит #contacts. Текущий URL: {current_url}"
        print("✓ URL содержит правильный якорь #contacts")

        # Проверяем видимость раздела 'Контакты'
        is_visible = main_page.check_section_visible(section_contacts_title)
        assert is_visible, "Раздел 'Контакты' не виден после навигации"
        print("✓ Раздел 'Контакты' успешно отображается")

        print("✅ Тест пройден успешно!\n")

    def test_specialists_navigation(self, main_page):
        """Проверка навигации к разделу 'Специалисты'"""
        print("=== Тест: Навигация к разделу 'Специалисты' ===")

        # Кликаем на кнопку 'Выбрать специалиста'
        main_page.click_menu_item('choose_specialist')
        print("✓ Кликнули на 'Выбрать специалиста'")

        # Проверяем, что URL содержит якорь #specialists
        current_url = main_page.get_current_url()
        print(f"Текущий URL: {current_url}")
        assert "#specialists" in current_url, f"URL не содержит #specialists. Текущий URL: {current_url}"
        print("✓ URL содержит правильный якорь #specialists")

        # Проверяем видимость раздела 'Специалисты'
        is_visible = main_page.check_section_visible(section_specialists_title)
        assert is_visible, "Раздел 'Специалисты' не виден после навигации"
        print("✓ Раздел 'Специалисты' успешно отображается")

        print("✅ Тест пройден успешно!\n")

    def test_more_details_navigation(self, main_page):
        """Проверка навигации по кнопке 'Подробнее'"""
        print("=== Тест: Навигация по кнопке 'Подробнее' ===")

        # Кликаем на кнопку 'Подробнее'
        main_page.click_menu_item('more_details')
        print("✓ Кликнули на 'Подробнее'")

        # Проверяем, что URL содержит якорь #moreinfo
        current_url = main_page.get_current_url()
        print(f"Текущий URL: {current_url}")
        assert "#moreinfo" in current_url, f"URL не содержит #moreinfo. Текущий URL: {current_url}"
        print("✓ URL содержит правильный якорь #moreinfo")

        # Проверяем видимость раздела 'Услуги'
        is_visible = main_page.check_section_visible(section_services_title)
        assert is_visible, "Раздел 'Услуги' не виден после навигации"
        print("✓ Раздел 'Услуги' успешно отображается")

        print("✅ Тест пройден успешно!\n")


class TestMainPageSmoke:

    def test_page_load(self, main_page):
        """Проверка загрузки главной страницы"""
        print("=== Smoke тест: Загрузка главной страницы ===")

        # Проверяем, что страница загружена
        current_url = main_page.get_current_url()
        print(f"Текущий URL: {current_url}")
        assert "effective-mobile" in current_url, f"Страница не загружена. URL: {current_url}"
        print("✓ Страница успешно загружена")

        # Проверяем заголовок страницы
        page_title = main_page.get_page_title()
        assert page_title, "Заголовок страницы пустой"
        print(f"✓ Заголовок страницы: {page_title}")

        print("✅ Smoke тест пройден успешно!\n")

    def test_main_elements_present(self, main_page):
        """Проверка наличия основных элементов на странице"""
        print("=== Smoke тест: Наличие основных элементов ===")

        # Проверяем наличие логотипа
        assert main_page.is_element_visible(menu_about), "Логотип не отображается"
        print("✓ Логотип отображается")

        # Проверяем наличие основных пунктов меню
        menu_items = [menu_services, menu_projects, menu_reviews, menu_contacts]
        for i, menu_item in enumerate(menu_items, 1):
            assert main_page.is_element_visible(menu_item), f"Пункт меню {i} не отображается"
        print("✓ Все пункты меню отображаются")

        # Проверяем наличие кнопок
        assert main_page.is_element_visible(button_choose_specialist), "Кнопка 'Выбрать специалиста' не отображается"
        assert main_page.is_element_visible(button_more_details), "Кнопка 'Подробнее' не отображается"
        print("✓ Основные кнопки отображаются")

        print("✅ Smoke тест пройден успешно!\n")