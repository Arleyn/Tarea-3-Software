'''
Created on 3/5/2015
@author: Arleyn Goncalves
         Edwin Murillo
'''
#-*- coding:UTF-8 -*-

class BilleteraElectronica(object):
    def __init__(self,identificador,nombre,apellido,CI):
        self._identificador = identificador;
        self._nombre = nombre
        self._apellido = apellido
        self._CI = CI;
        self._saldo = 0;
        
    def saldo(self):
        print(self._saldo);
        return self._saldo;
    
    def recargar(self,cantidad,fecha,id_estacionamiento):
            self._saldo += cantidad;
            return self._saldo;
        
    def consumir(self,cantidad,fecha,id_estacionamiento):
            if self._saldo < cantidad:
                raise Exception("No tiene saldo suficiente");
            self._saldo -= cantidad;
            return self._saldo;