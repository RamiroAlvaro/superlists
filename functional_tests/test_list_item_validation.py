from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Edith accede a la pagina inicial y accidentalmente intenta submeter
        # un item vacio en la lista. Ella apreta enter en la caja de entrada vacia

        # La pagina inicial es actualizada y hay un mensaje de error informando
        # que los items de la lista no pueden estar en blanco.

        # Ella intenta nuevamente con un texto para el item, eso ahora funciona

        # De forma perversa, ella ahora decide submeter un segundo item en
        # blanco en la lista

        # Ella recibe un aviso semejante en la pagina de la lista.

        # Y ella puede corregir eso escribiendo el item con un texto
        self.fail('write me!')
