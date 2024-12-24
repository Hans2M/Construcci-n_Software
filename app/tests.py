from django.test import TestCase
from .models import Lugar

class LugarModelTest(TestCase):
    def test_crear_lugar(self):
        lugar = Lugar.objects.create(
            nombre="Parque Central",
            descripcion="Un lugar para relajarse",
            direccion="Calle 123",
            latitud="12.34",
            longitud="56.78"
        )
        self.assertEqual(lugar.nombre, "Parque Central")
        self.assertEqual(lugar.descripcion, "Un lugar para relajarse")

