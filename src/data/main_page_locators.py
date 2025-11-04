from selenium.webdriver.common.by import By

# Локаторы пунктов меню
menu_about = (By.CSS_SELECTOR, '.tn-elem__5730545321680606406481 a')
menu_services = (By.CSS_SELECTOR, '.tn-elem__5730545321680606406485 a')
menu_projects = (By.CSS_SELECTOR, '.tn-elem__5730545321680606406489 a')
menu_reviews = (By.CSS_SELECTOR, '.tn-elem__5730545321706704571141 a')
menu_contacts = (By.CSS_SELECTOR, '.tn-elem__5730545321680606406492 a')

# Локаторы кнопок
button_choose_specialist = (By.CSS_SELECTOR, '.tn-elem__5730545321680606406495 a')
button_more_details = (By.CSS_SELECTOR, '.tn-elem__5719935831680426641483 a')

# Локаторы заголовков разделов
section_about_title = (By.CSS_SELECTOR, '[data-elem-id="1680508197707"]')
section_services_title = (By.CSS_SELECTOR, '[data-elem-id="1680510339488"]')
section_projects_title = (By.CSS_SELECTOR, '.tn-elem__5731196821680611816671')
section_reviews_title = (By.CSS_SELECTOR, '.t730__content')
section_specialists_title = (By.CSS_SELECTOR, '.t1095')
section_contacts_title = (By.CSS_SELECTOR, '.t730__content')