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