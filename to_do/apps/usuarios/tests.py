from django.test import TestCase
import string as st
import random as rd

class ClaveCorreoTests(TestCase):
    
    # Testeo para generar una contraseña aleatoria en el sistema de 75 caracteres
    def test_generar_clave(self):
        clave_aleatoria = ''.join(rd.choices(st.ascii_letters + st.digits , k=75))
        self.assertEqual(True, len(clave_aleatoria) == 75, 'La contraseña generada no tiene 75 caracteres')


