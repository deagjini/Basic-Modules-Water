# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 17:10:23 2019

@author: Dea
""" 

#property names 
rho = 1000 #density 
mu = 1 #viscosity 
Tm = 273.15 #melting point 
Tb = 373.13 #boiling point 
k = 0.58 #thermal conductivity 
cas_number = "7732-18-5" #CAS Number 

def convert_to_kelvin(temperature, units): 
    'returns the temperature in Kelvin where temperature is a numberic value and units is a string of length 1' 
    if (check_valid_temp(temperature) == False): 
       return(None)   
    else: 
        if (units == "C") and (temperature + Tm >= 0): 
            temperature = temperature + Tm
            return (temperature)
        elif (units == "F") and ((temperature - 32.0)*(5./9)+ Tm >= 0): 
            temperature = (temperature - 32.0)*(5./9) + Tm   
            return (temperature)
        elif (units == "K") and (temperature >= 0):
            return (temperature)   
        else: 
            return(None)
    
def is_gas(temperature):  
    'return true is water is a gas at the temperature (in kelvins) else return false'
    if check_valid_temp(temperature) == False: 
        return(None) 
    elif temperature >= Tb: 
        return (True) 
    elif temperature < Tb:  
        return (False) 

def is_liquid(temperature):  
    'check if water is liquid at the given temp' 
    if check_valid_temp(temperature) == False: 
        return(None) 
    elif (temperature >= Tm) and (temperature < Tb): 
        return (True) 
    elif (temperature < Tm) or (temperature > Tb): 
        return (False) 

def is_solid(temperature): 
    'check if water is solid at temperature given in Kelvins'  
    if check_valid_temp(temperature) == False: 
        return(None) 
    elif temperature < Tm: 
        return(True) 
    elif temperature >= Tm: 
        return(False)  

def check_valid_temp(temperature): 
    'check if temperature is a valid input (int or float)'
    if (type(temperature) != int) and (type(temperature) != float): 
        return(False)
    else: 
        return(True) 

def check_valid_units(units): 
    'check if units is K, C, or F'
    if (units != "C") and (units != "K") and (units != "F"): 
        return(False)
    else: 
        return(True) 
        
if __name__ == '__main__': 
    units = input("Please enter the units you will be using:  \nK for Kelvin \nC for Celsuis \nF for Fahrenheit")
    tempStr = input("Please enter the numerical value of the temperature: ")  

    if check_valid_units(units) != True: 
        print("Invalid input")        
    else: 
        try: 
            temperature = float(tempStr)   
        except: 
            print("Invalid Input")              
        else:   
            if convert_to_kelvin(temperature, units) != None:
                temperature = convert_to_kelvin(temperature, units)
                if is_solid(temperature) == True: 
                    print("Solid") 
                elif is_liquid(temperature) == True: 
                    print("Liquid") 
                elif is_gas(temperature) == True:  
                    print("Gas") 
                else: 
                    print("Invalid input")  
            else:  
                print("Invalid input")


    