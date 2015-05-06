'''
Created on 3/5/2015
@author: Arleyn Goncalves
         Edwin Murillo
'''
#-*- coding:UTF-8 -*-

class DatosDebitos(object):
    def __init__(self):
        self._listas_consumos = [];
    
    def Almacenar(self,cantidad,fecha,identificar):
        self._listas_consumos.append((cantidad,fecha,identificar))
        return self._listas_consumos

class BilleteraElectronica(object):
    def __init__(self,identificador,nombre,apellido,CI):
        self._identificador = identificador;
        self._nombre = nombre
        self._apellido = apellido
        self._CI = CI;
        self._saldo = 0;
        self._Consumos = DatosDebitos();
        
    def saldo(self):
        print(self._saldo);
        return self._saldo;
    
    def recargar(self,cantidad,fecha,id_estacionamiento):
        if cantidad <= 0:
            raise Exception("La cantidad a recargar tiene que se mayor a 0");
        else:
            self._saldo += cantidad;
            return self._saldo;
        
    def consumir(self,cantidad,fecha,id_estacionamiento):
        if self._saldo < cantidad:
            raise Exception("No tiene saldo suficiente");
        elif cantidad <= 0:
            raise Exception("La cantidad a consumir tiene que ser mayor a 0");
        else:
            self._saldo -= cantidad;
            self._Consumos.Almacenar(cantidad,fecha,id_estacionamiento);
            return self._saldo;