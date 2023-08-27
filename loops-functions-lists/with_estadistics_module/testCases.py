from stubsA2 import *

#Testing the computeProvTaxes(...) operation
def q1() :
	
    test = []
    
    #testing the first bracket
    income = 29590
    taxes = computeProvTaxes( income )
    result = round(  abs( taxes - 2600.96 ) )
    test.append( result <= 0.01 )
    
    #testing the first bracket
    income = 39000
    taxes = computeProvTaxes( income )
    result = round( abs( taxes - 4007.75 ), 2 )
    test.append( result <= 0.01 )
    
    income = 92468.79
    taxes = computeProvTaxes( income )
    result = round( abs( taxes - 12573.91 ) )
    test.append( result <= 0.01 )
    
    income = 120000.79
    taxes = computeProvTaxes( income )
    result = round( abs( taxes - 17387.60 ) )
    test.append( result <= 0.01 )
    
    income = 200000.79
    taxes = computeProvTaxes( income )
    result = round( abs( taxes - 33137.62 ) )
    test.append( result <= 0.01 )
    
    income = 1000000.28
    taxes = computeProvTaxes( income )
    result = round( abs( taxes - 201137.52 ) )
    test.append( result <= 0.01 )
    
    return test
    
#Testing the computeFedTaxes(...) operation
def q2() :
	
    test = []
    
    #testing the first bracket
    income = 29590
    taxes = computeFedTaxes( income )
    result = round(  abs( taxes - 4438.50 ) )
    test.append( result <= 0.01 )
    
    income = 52000.98
    taxes = computeFedTaxes( income )
    result = round(  abs( taxes - 7964.10 ) )
    test.append( result <= 0.01 )
    
    income = 135000.01
    taxes = computeFedTaxes( income )
    result = round(  abs( taxes - 27011.70 ) )
    test.append( result <= 0.01 )
    
    income = 92468.79
    taxes = computeFedTaxes( income )
    result = round(  abs( taxes - 16260.00 ) )
    test.append( result <= 0.01 )
    
    income = 182456.99
    taxes = computeFedTaxes( income )
    result = round(  abs( taxes - 40264.89 ) )
    test.append( result <= 0.01 )
    
    income = 1000000
    taxes = computeFedTaxes( income )
    result = round(  abs( taxes - 308691.92 ) )
    test.append( result <= 0.01 )
    
    return test
    
#Testing the computeCPP(...) operation
def q3() :
	
    test = []
    
    #testing the first bracket
    income = 35000
    cpp = computeCPP( income )
    result = round(  abs( cpp - 1837.5 ) )
    test.append( result <= 0.01 )
    
    income = 92000
    cpp = computeCPP( income )
    result = round(  abs( cpp - 2898 ) )
    test.append( result <= 0.01 )
    
    return test    

#Testing the computeEI(...) operation
def q4() :
	
    test = []
    
    #testing the first bracket
    income = 35000
    ei = computeEI( income )
    result = round(  abs(ei - 553 ) )
    test.append( result <= 0.01 )
    
    income = 92000
    ei = computeEI( income )
    result = round(  abs( ei - 856.36 ) )
    test.append( result <= 0.01 )
    
    return test 
    
#Testing the computeHealthPremium(...) operation
def q5() :
	
    test = []
    
    #testing the first bracket
    income = 10000
    hp = computeHealthPremium( income )
    result = round(  abs(hp - 0.0 ) )
    test.append( result <= 0.01 )
    
    income = 23000
    hp = computeHealthPremium( income )
    result = round(  abs( hp - 60 ) )
    test.append( result <= 0.01 )
    
    income = 35000
    hp = computeHealthPremium( income )
    result = round(  abs( hp - 300 ) )
    test.append( result <= 0.01 )
    
    income = 38000
    hp = computeHealthPremium( income )
    result = round(  abs( hp - 300 ) )
    test.append( result <= 0.01 )
    
    income = 48500
    hp = computeHealthPremium( income )
    result = round(  abs( hp - 450 ) )
    test.append( result <= 0.01 )
    
    income = 70000
    hp = computeHealthPremium( income )
    result = round(  abs( hp - 600 ) )
    test.append( result <= 0.01 )
    
    income = 72500
    hp = computeHealthPremium( income )
    result = round(  abs( hp - 600 ) )
    test.append( result <= 0.01 )
    
    income = 200000
    hp = computeHealthPremium( income )
    result = round(  abs( hp - 750 ) )
    test.append( result <= 0.01 )
    
    income = 200500
    hp = computeHealthPremium( income )
    result = round(  abs( hp - 750 ) )
    test.append( result <= 0.01 )
    
    income = 300000
    hp = computeHealthPremium( income )
    result = round(  abs( hp - 900 ) )
    test.append( result <= 0.01 )
    
    return test 

#Testing the computeNetIncomes(...) and mean(...) operations
def q6():

    test = []
    
    incomes = [1000000, 150000, 25000, 92468.79]
    nIncomes = computeNetIncomes( incomes )
    result = round( abs( means( nIncomes ) - 163439.57 ) <= 0.01 )
    test.append( result )

    return test

#Testing the standardDeviation(...) and mean(...) operations
def q7():

    test = []
    
    incomes = [1000000, 150000, 25000, 92468.79]
    sdev = standardDeviation( incomes, means( incomes ) )
    result = round( abs( sdev - 396880.40 ) <= 0.01 )
    test.append( result )
    
    return test

#A helper operation
def evaluateQuestion( questions ) :

    answer = questions[0]
    for question in questions : 
        answer = ( answer and question )
    
    return answer