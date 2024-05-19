from selenium.webdriver.common.by import By


class FlightsWebElements():
    page_subtitle = (By.XPATH, '//h2[contains(text(), "vuelo")]')
    main_form = (By.ID, 'main-search-form')
    signin_button = (By.CSS_SELECTOR, '.J-sA-label')
    search_button = (By.CSS_SELECTOR, 'button[aria-label="Buscar"]')


class StaysWebElements():
    page_subtitle = (By.XPATH, '//h2[contains(text(), "alojamiento")]')
    main_form = (By.ID, 'main-search-form')
    signin_button = (By.CSS_SELECTOR, '.J-sA-label')
    search_button = (By.CSS_SELECTOR, 'button[aria-label="Buscar"]')


class CarsWebElements():
    page_subtitle = (By.XPATH, '//h2[contains(text(), "carro")]')
    main_form = (By.ID, 'main-search-form')
    signin_button = (By.CSS_SELECTOR, '.J-sA-label')
    search_button = (By.CSS_SELECTOR, 'button[aria-label="Haz clic para buscar carros"]')


class CitybreaksWebElements():
    page_subtitle = (By.XPATH, '//h1[contains(text(), "paquetes")]')
    main_form = (By.CSS_SELECTOR, '.form-section')
    signin_button = (By.CSS_SELECTOR, '.J-sA-label')
    search_button = (By.CSS_SELECTOR, '.EFi3-button')

