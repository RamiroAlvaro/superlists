from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Edith accede a la pagina inicial y accidentalmente intenta submeter
        # un item vacio en la lista. Ella apreta enter en la caja de entrada vacia
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)

        # El navegador intercepta la requisicion y no carga la
        # pagina de la lista.
        self.wait_for(lambda: self.browser.find_element_by_css_selector(
            '#id_text:invalid'
        ))

        # Ella comienza a digitar un texto para un nuevo item y el error desaparece
        self.get_item_input_box().send_keys('Buy milk')
        self.wait_for(lambda: self.browser.find_element_by_css_selector(
            '#id_text:valid'
        ))

        # Y ella puede someter el item con exito
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # De forma perversa, ella ahora decide submeter un segundo item en
        # blanco en la lista
        self.get_item_input_box().send_keys(Keys.ENTER)

        # Nuevamente el navegador no estara de acuerdo.
        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for(lambda: self.browser.find_element_by_css_selector(
            '#id_text:invalid'
        ))

        # Y ella puede corregir eso escribiendo el item con un texto
        self.get_item_input_box().send_keys('Make tea')
        self.wait_for(lambda: self.browser.find_element_by_css_selector(
            '#id_text:valid'
        ))
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for_row_in_list_table('2: Make tea')
