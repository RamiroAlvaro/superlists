from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Edith accede a la pagina inicial y accidentalmente intenta submeter
        # un item vacio en la lista. Ella apreta enter en la caja de entrada vacia
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)

        # La pagina inicial es actualizada y hay un mensaje de error informando
        # que los items de la lista no pueden estar en blanco.
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element_by_css_selector('.has-error').text,
            "You can't have an empty list item"
        ))

        # Ella intenta nuevamente con un texto para el item, eso ahora funciona
        self.browser.find_element_by_id('id_new_item').send_keys('Buy milk')
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # De forma perversa, ella ahora decide submeter un segundo item en
        # blanco en la lista
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)

        # Ella recibe un aviso semejante en la pagina de la lista.
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element_by_css_selector('.has-error').text,
            "You can't have an empty list item"
        ))

        # Y ella puede corregir eso escribiendo el item con un texto
        self.browser.find_element_by_id('id_new_item').send_keys('Make tea')
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for_row_in_list_table('2: Make tea')
