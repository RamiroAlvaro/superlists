from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith escucho hablar de una nueva aplicación online interesante para
        # lista de tareas. Ella decide verificar la pagina de inicio
        self.browser.get(self.live_server_url)

        # Ella percibe que el título de la pagina y el encabezado mencionan listas de
        # tareas (to-do)
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Ella es convidada a insertar un iten de tarea inmediatamente
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # Ella digita 'Buy peacock feathers' en una caja de texto
        inputbox.send_keys('Buy peacock feathers')

        # Cuando ella presiona Enter, la pagina se actualiza, y ahora la pagina lista
        # "1: Buy peacock feathers" como un iten de la lista de tareas
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # Todavia hay una caja de texto para acresentar otro iten. Ella inserta
        # 'Use peacock feathers to make a fly'
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # La pagina es actualizada nuevamente y ahora muestra dos itens en su lista
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # Edith se pregunta si el sitio recordara de su lista. Entonces nota
        # que el sitio genero una URL unica para ella -- hay un pequeño
        # texto explicativo para eso.
        self.fail('Finish the test!')
