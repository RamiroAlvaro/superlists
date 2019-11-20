from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import WebDriverException

MAX_WAIT = 10


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_list_for_one_user(self):
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
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # Todavia hay una caja de texto para acresentar otro iten. Ella inserta
        # 'Use peacock feathers to make a fly'
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # La pagina es actualizada nuevamente y ahora muestra dos itens en su lista
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # Satisfecha, ella vuelve a dormir

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Edith inicia una nueva lista de tareas
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # Ella percibe que su lista tiene un URL unico
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')

        # Agora un nuevo usuario, Francis, llega al sitio

        ## Usamos una nueva sesion del navegador para garantizar que ninguna informacion
        ## de Edith esta viniendo de cookies, etc
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Francis accede a la pagina inicial. No hay ninguna señal de la lista de Edith
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # Francis inicia una nueva lista, insertando un iten nuevo
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # Francis obtiene su propio URL exclusivo
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        # Nuevamente, no hay ninguna señal de la lista de Edith
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

        # Satisfechos ambos vuelven a dormir

        # Edith se pregunta si el sitio recordara de su lista. Entonces nota
        # que el sitio genero una URL unica para ella -- hay un pequeño
        # texto explicativo para eso.
        # self.fail('Finish the test!')
