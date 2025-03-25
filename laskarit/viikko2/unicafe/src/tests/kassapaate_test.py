import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_rahamaara_on_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        
    def test_myydyt_lounaat_on_aluksi_nolla(self):
        self.assertEqual(self.kassapaate.edulliset + self.kassapaate.maukkaat, 0)
        
        
    def test_kateisella_voi_ostaa_edullisen_lounaan_kun_riittavasti_rahaa(self):
        vaihtorahaa = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000+240)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(vaihtorahaa, 300-240)
        
        
    def test_kateisella_ei_voi_ostaa_edullista_lounasta_kun_ei_ole_riittavasti_rahaa(self):
        vaihtorahaa = self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(vaihtorahaa, 100)
        
        
        
        
    def test_kateisella_voi_ostaa_maukkaan_lounaan_kun_riittavasti_rahaa(self):
        vaihtorahaa = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000+400)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(vaihtorahaa, 500-400)
        
    def test_kateisella_ei_voi_ostaa_maukasta_lounasta_kun_ei_ole_riittavasti_rahaa(self):
        vaihtorahaa = self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(vaihtorahaa, 100)
        
        
        
        
    
    def test_kortilla_voi_ostaa_edullisen_lounaan_kun_riittavasti_rahaa(self):
        maksukortti = Maksukortti(500)
        
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        
        self.assertEqual(maksukortti.saldo, 500-240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        
        
    def test_kortilla_ei_voi_ostaa_edullista_lounasta_kun_ei_ole_riittavasti_rahaa(self):
        maksukortti = Maksukortti(100)
        
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        
        self.assertEqual(maksukortti.saldo, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        
        
        
        
    def test_kortilla_voi_ostaa_maukkaan_lounaan_kun_riittavasti_rahaa(self):
        maksukortti = Maksukortti(500)
        
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        
        self.assertEqual(maksukortti.saldo, 500-400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    
        
    def test_kortilla_ei_voi_ostaa_maukasta_lounasta_kun_ei_ole_riittavasti_rahaa(self):
        maksukortti = Maksukortti(100)
        
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        
        self.assertEqual(maksukortti.saldo, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        
        
        
        
        
    def test_kortille_voi_ladata_rahaa(self):
        maksukortti = Maksukortti(500)
        
        self.kassapaate.lataa_rahaa_kortille(maksukortti, 1000)
        
        self.assertEqual(maksukortti.saldo, 500+1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000+1000)
        
        
        
    def test_kortille_ei_voi_ladata_negatiivista_summaa(self):
        maksukortti = Maksukortti(500)
        
        self.kassapaate.lataa_rahaa_kortille(maksukortti, -1000)
        
        self.assertEqual(maksukortti.saldo, 500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        
        
    def test_saldo_palautuu_euroina(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.00)