from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith escucho hablar de una nueva aplicación online interesante para
        # lista de tareas. Ella decide verificar la pagina de inicio
        self.browser.get('http://localhost:8000')

        # Ella percibe que el título de la pagina y el encabezado mencionan listas de
        # tareas (to-do)
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main()
