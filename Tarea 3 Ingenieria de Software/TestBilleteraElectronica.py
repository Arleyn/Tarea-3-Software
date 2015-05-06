#-*- coding:UTF-8 -*-
import unittest
import BilleteraElectronica
from decimal import Decimal

class Test(unittest.TestCase):

    def testBilleteraExist(self):
        pass
    
    def testCrearBilletera(self):
        Arleyn = BilleteraElectronica.BilleteraElectronica("001","Arleyn","Goncalves","21467704");
        saldo = Arleyn.saldo();
        self.assertEqual(0,saldo);
        
    def testAgregarCredito(self):
        Arleyn = BilleteraElectronica.BilleteraElectronica("001","Arleyn","Goncalves","21467704");
        saldo = Arleyn.recargar(100,'27/12/1992','01');
        self.assertEqual(100,saldo);
        
    def testAgregarCredito2(self):
        Arleyn = BilleteraElectronica.BilleteraElectronica("001","Arleyn","Goncalves","21467704");
        Arleyn.recargar(100,'27/12/1992','01');
        saldo = Arleyn.recargar(550,'27/12/1992','01');
        self.assertEqual(650,saldo);
        
    def testConsumirCredito(self):
        Arleyn = BilleteraElectronica.BilleteraElectronica("001","Arleyn","Goncalves","21467704");
        Arleyn.recargar(100,'27/12/1992','01');
        saldo = Arleyn.consumir(50,'28/12/1992','02')
        self.assertEqual(50,saldo);
        
    def testConsumirCredito2(self):
        Arleyn = BilleteraElectronica.BilleteraElectronica("001","Arleyn","Goncalves","21467704");
        Arleyn.recargar(100,'27/12/1992','01')
        Arleyn.consumir(50,'28/12/1992','02')
        saldo = Arleyn.consumir(45,'28/12/1992','02')
        self.assertEqual(5,saldo);
        
    def testSinSaldo(self):
        Arleyn = BilleteraElectronica.BilleteraElectronica("001","Arleyn","Goncalves","21467704")
        self.assertRaises(Exception, lambda: Arleyn.consumir(50,'28/12/1992','02'))
        
    def testSaldoMenorConsumo(self):
        Arleyn = BilleteraElectronica.BilleteraElectronica("001","Arleyn","Goncalves","21467704")
        Arleyn.recargar(100,'27/12/1992','01')
        self.assertRaises(Exception, lambda: Arleyn.consumir(150,'28/12/1992','02'))
        
    def testSaldoConsumoNegativo(self):
        Arleyn = BilleteraElectronica.BilleteraElectronica("001","Arleyn","Goncalves","21467704")
        self.assertRaises(Exception, lambda: Arleyn.consumir(-150,'28/12/1992','02'))
        
    def testSaldoConsumoNegativo2(self):
        Arleyn = BilleteraElectronica.BilleteraElectronica("001","Arleyn","Goncalves","21467704")
        Arleyn.recargar(100,'27/12/1992','01')
        self.assertRaises(Exception, lambda: Arleyn.consumir(-50,'28/12/1992','02'))
        
    def testRecargar0(self):
        Arleyn = BilleteraElectronica.BilleteraElectronica("001","Arleyn","Goncalves","21467704");
        self.assertRaises(Exception, lambda: Arleyn.recargar(0,'28/12/1992','02'))
        
    def testConsumir0(self):
        Arleyn = BilleteraElectronica.BilleteraElectronica("001","Arleyn","Goncalves","21467704");
        self.assertRaises(Exception, lambda: Arleyn.consumir(0,'28/12/1992','02'))
        
    def testConsumir2(self):
        Arleyn = BilleteraElectronica.BilleteraElectronica("001","Arleyn","Goncalves","21467704");
        Arleyn.recargar(100,'28/12/1992','02')
        self.assertRaises(Exception, lambda: Arleyn.consumir(0,'28/12/1992','02'))
        
    def testSaldoRecargaNegativa(self):
        Arleyn = BilleteraElectronica.BilleteraElectronica("001","Arleyn","Goncalves","21467704")
        self.assertRaises(Exception, lambda: Arleyn.recargar(-150,'28/12/1992','02'))
        
    def testSaldoRecargaNegativa2(self):
        Arleyn = BilleteraElectronica.BilleteraElectronica("001","Arleyn","Goncalves","21467704")
        Arleyn.recargar(100,'27/12/1992','01')
        self.assertRaises(Exception, lambda: Arleyn.recargar(-150,'28/12/1992','02'))
        
    def testListaConsumo(self):
        Arleyn = BilleteraElectronica.BilleteraElectronica("001","Arleyn","Goncalves","21467704");
        Arleyn.recargar(400,'27/12/1992','05');
        Arleyn.consumir(100,'27/12/1993','02');
        Arleyn.consumir(250,'24/12/1995','08');
        numConsumos = len(Arleyn._Consumos._listas_consumos)
        self.assertEqual(2,numConsumos);
        
    def testListaRecargas(self):
        Arleyn = BilleteraElectronica.BilleteraElectronica("001","Arleyn","Goncalves","21467704");
        Arleyn.recargar(100,'26/12/1990','01');
        Arleyn.recargar(60,'27/12/1992','05');
        Arleyn.recargar(20,'04/08/1993','07');
        numRecargas = len(Arleyn._Creditos._listas_recargas)
        self.assertEqual(3,numRecargas);
        
    def testRecargarDecimales(self):
        Arleyn = BilleteraElectronica.BilleteraElectronica("001","Arleyn","Goncalves","21467704");
        saldo = Arleyn.recargar(10.6,'28/12/1992','02')
        self.assertEqual(10.6,saldo);
        
    def testConsumirDecimales(self):
        Arleyn = BilleteraElectronica.BilleteraElectronica("001","Arleyn","Goncalves","21467704");
        Arleyn.recargar(100,'28/12/1992','02')
        saldo = Arleyn.consumir(Decimal('99.9'),'28/12/1992','02')
        self.assertEqual(Decimal('0.1'),saldo);