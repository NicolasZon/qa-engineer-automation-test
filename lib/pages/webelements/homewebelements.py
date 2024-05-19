from selenium.webdriver.common.by import By


class HomeWebElements:
    main_form = (By.ID, 'main-search-form')
    signin_button = (By.CSS_SELECTOR, '.J-sA-label')
    search_button = (By.CSS_SELECTOR, 'button[aria-label="Buscar"]')
    search_section = (By.CSS_SELECTOR, 'nav[aria-label="Buscar"]')
    plan_section = (By.CSS_SELECTOR, 'nav[aria-label="Planificación de viajes"]')
    trips_section = (By.CSS_SELECTOR, 'a[aria-label="Trips "]')
    flights_option = (By.CSS_SELECTOR, 'a[aria-label="Buscar vuelos "]')
    stays_option = (By.CSS_SELECTOR, 'a[aria-label="Buscar hoteles "]')
    cars_option = (By.CSS_SELECTOR, 'a[aria-label="Buscar autos "]')
    citybreaks_option = (By.CSS_SELECTOR, 'a[aria-label="Buscar vacaciones "]')
