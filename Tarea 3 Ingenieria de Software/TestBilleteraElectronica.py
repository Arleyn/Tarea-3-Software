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
        
    def testUsoListaRecarga(self):
        Edwin = BilleteraElectronica.BilleteraElectronica("001","Edwin","Murillo","20132170");
        Edwin.recargar(400,'14/12/1991','05');
        Edwin.recargar(100,'27/12/1993','02');
        Edwin.recargar(250,'24/12/1995','08');
        numRecargas = Edwin._Creditos._listas_recargas[1]
        self.assertEqual((100,'27/12/1993','02'),numRecargas);
        
    def testUsoListaConsumo(self):
        Edwin = BilleteraElectronica.BilleteraElectronica("001","Edwin","Murillo","20132170");
        Edwin.recargar(400,'14/12/1991','05');
        Edwin.consumir(30,'14/12/1991','05');
        Edwin.consumir(100,'27/12/1993','02');
        Edwin.consumir(250,'24/12/1995','08');
        numConsumo = Edwin._Consumos._listas_consumos[2]
        self.assertEqual((250,'24/12/1995','08'),numConsumo);
        
    def testListaRecargasUnElemento(self):
        Edwin = BilleteraElectronica.BilleteraElectronica("001","Edwin","Murillo","20132170");
        Edwin.recargar(400,'14/12/1991','05');
        numRecargas = len(Edwin._Creditos._listas_recargas)
        self.assertEqual(1,numRecargas);
        
    def testListaConsumoUnElemento(self):
        Edwin = BilleteraElectronica.BilleteraElectronica("001","Edwin","Murillo","20132170");
        Edwin.recargar(400,'14/12/1991','05');
        Edwin.consumir(100,'27/12/1993','02');
        numConsumos = len(Edwin._Consumos._listas_consumos)
        self.assertEqual(1,numConsumos);
        
    def testListaRecargasVacia(self):
        Edwin = BilleteraElectronica.BilleteraElectronica("001","Edwin","Murillo","20132170");
        numRecargas = len(Edwin._Creditos._listas_recargas)
        self.assertEqual(0,numRecargas);