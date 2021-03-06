import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)


    def test_negatiivinen_tilavuus_on_nolla(self):
        self.varasto = Varasto(-1)
        self.assertEqual(self.varasto.tilavuus, 0)

    def test_negatiivinen_alkusaldo_on_nolla(self):
        self.varasto = Varasto(5, -5)
        self.assertEqual(self.varasto.saldo, 0)

    def test_alkusaldo_pienempi_kuin_tilavuus(self):
        self.varasto = Varasto(1, 2)
        self.assertEqual(self.varasto.saldo, 1)

    def test_lisays_ei_ylita_tilavuutta(self):
        self.varasto.lisaa_varastoon(99999)
        self.assertEqual(self.varasto.saldo, 10)

    def test_otto_ei_ylita_nykyista_saldoa(self):
        self.varasto.lisaa_varastoon(10)
        otettu = self.varasto.ota_varastosta(100)
        self.assertEqual(otettu, 10)

    def test_negatiivine_lisays_on_nolla(self):
        self.varasto = Varasto(5, 5)
        self.varasto.lisaa_varastoon(-99999)
        self.assertEqual(self.varasto.saldo, 5)

    def test_negatiivine_otto_on_nolla(self):
        self.varasto = Varasto(5, 5)
        self.varasto.ota_varastosta(-99999)
        self.assertEqual(self.varasto.saldo, 5)
    
    def test_oikea_str(self):
        varasto_tulostus = str(self.varasto)
        oikea_tulostus = "saldo = 0, vielä tilaa 10"

        self.assertEqual(varasto_tulostus, oikea_tulostus)



    
