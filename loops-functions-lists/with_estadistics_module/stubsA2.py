#Author: Opeyemi Adesina
#Institution: University of the Fraser Valley
#Academic Session: Winter, 2021

#-------------------------------------------# Problem Analysis #-------------------------------------------#

#-----Review of the given code-----#
# The code already given for the assignment2 has defined the information that will be displayed to the user, as well as many 
# functions that will be invoked during the exercise. What is missing in this puzzle is the computation of the Employees net 
# incomes list, the mean and the standard deviation.

#-----netIncomeList creation-----#
#To create the List for Employees net income we need first to compute the Provintial tax, Federal Tax, CPP, EI and Health 
# Premium. For this is necessary using functions that can be invoked to create the list.
#Once the functions are ready, an iteration through the initial list(grossIncomeList) will be needed to go along each 
# gross income and compute all the net incomes and adding them one by one to the new netIncomeList.

#-----Mean and Standard Deviation-----#
#To compute the mean and standard deviation all is needed is to export from the statistics module the mean and pstdev,
#After that, we just need to use the matematical statistics functions inside the functions to compute the mean and St deviation.

#-------------------------------------------# End of Problem Analysis #-------------------------------------------#    

from math import sqrt #imports only the square root operation from the math module
from statistics import mean, pstdev #imports of the mean and standard deviation from the statistics module

#receiving number of employees as an input from the user 
numberOfEmployees = int(input("Enter the number of employees: "))

#operation builds gross income list from user input
def buildGrossIncomeList( numberOfEmployees ) : #Step 1

    #creating and initializing income list as empty
    grossIncomeList = list()
    i = 0
    
    print("\n\n------------------------- Enter Employees' Salaries (i.e., Gross Incomes) Below -------------------------")
    while ( i < numberOfEmployees ) :
        grossIncome = input("Enter an employee's gross income: ")
        
        #checking if the value entered is an empty string or not
        if ( grossIncome.strip() == "" ) :
            print("Gross income can't be an empty string...")
            grossIncome = input("Re-enter the employee's gross income: ")
        
        #type conversioning from string to floating point number - monies should be in float
        grossIncome = float( grossIncome )
        if ( grossIncome < 0.0 ) :
            print("Gross income can't be negative...")
            grossIncome = float( input("Re-enter non-negative value for the employee's gross income: ") )
        
        grossIncomeList.append( grossIncome )    
        i += 1
    return grossIncomeList

#operation computes provincial taxes for the input gross income...
def computeProvTaxes( grossIncome ) : 
    taxableIncome=grossIncome
    #Checking if grossincome is bigger than the last 5th bracket, starting with the greatest to facilitate computation
    if taxableIncome >= 150001.00:  
        taxableIncome-=150000.00
        ProvSection5=taxableIncome*0.21
        taxableIncome=150000.00
    else:
        ProvSection5=0.00

    if taxableIncome >=93000.01:
        taxableIncome-=93000.00
        ProvSection4=taxableIncome*.175
        taxableIncome=93000.00
    else:
        ProvSection4=0.00

    if taxableIncome >=59180.01:
        taxableIncome-=59180.00
        ProvSection3=taxableIncome*.1667
        taxableIncome=59180.00
    else:
        ProvSection3=0

    if taxableIncome >=29590.01:
        taxableIncome-=29590.00
        ProvSection2=taxableIncome*.1495
        taxableIncome=29590.00
    else:
        ProvSection2=0

    if taxableIncome >0:
        ProvSection1=taxableIncome*.0879
    
    #Adding up all provintial sections/bracket sections 
    ProvTaxes=ProvSection1+ProvSection2+ProvSection3+ProvSection4+ProvSection5
    return ProvTaxes

#operation computes federal taxes for the input gross income 
def computeFedTaxes( grossIncome ) : 
    #Checking if grossincome is bigger than the last 5th bracket, starting with the greatest to facilitate computation
    taxIncome=grossIncome
    if taxIncome >=216511.01:  
        taxIncome-=216511.00
        FedSection5=taxIncome*0.33
        taxIncome=216511.00
    else:
        FedSection5=0

    if taxIncome >=151978.01:
        taxIncome-=151978.00
        FedSection4=taxIncome*0.29
        taxIncome=151978.00
    else:
        FedSection4=0

    if taxIncome >=98040.01:
        taxIncome-=98040.00
        FedSection3=taxIncome*0.26
        taxIncome=98040.00
    else:
        FedSection3=0

    if taxIncome >=49020.01:
        taxIncome-=49020.00
        FedSection2=taxIncome*0.205
        taxIncome=49020.00
    else:
        FedSection2=0

    if taxIncome >0:
        FedSection1=taxIncome*0.15

    #Adding up all federal sections/bracket sections
    FedTaxes=FedSection1+FedSection2+FedSection3+FedSection4+FedSection5
    return FedTaxes
    
### Computing employee's CPP
def computeCPP( grossIncome ) :
    employee_cpp = grossIncome * 0.0525
    if employee_cpp > 2898.00:
        employee_cpp = 2898.00    
    return employee_cpp

### Computing employee's EI
def computeEI( grossIncome ) :
    employee_EI = grossIncome * 0.0158
    if employee_EI > 856.36:
        employee_EI = 856.36    
    return employee_EI

### Computing employee's Health Premium
def computeHealthPremium( grossIncome ) :
    #Computing Health premium for each bracket and with if conditions embeded inside an if
    if grossIncome <= 22000.00: 
            HealthPremium = 0.00
    elif grossIncome > 22000.00 and grossIncome <= 38000.00: 
        HealthPremium = (grossIncome - 22000.00)*.06
        if HealthPremium >= 300.00:
            HealthPremium = 300.00  
    elif grossIncome > 38000.00 and grossIncome <= 50000.00: 
        HealthPremium = 300.00 + ((grossIncome - 38000.00)*.06)
        if HealthPremium >= 450.00:
            HealthPremium = 450.00
    elif grossIncome > 50000.00 and grossIncome <= 74000.00: 
        HealthPremium = 450.00 + ((grossIncome - 50000.00)*.25)
        if HealthPremium >= 600.00:
            HealthPremium = 600.00
    elif grossIncome > 74000.00 and grossIncome <= 202000.00: 
        HealthPremium = 600.00 + ((grossIncome - 74000.00)*.25)
        if HealthPremium >= 750.00:
            HealthPremium = 750.00
    else:
        HealthPremium = 750.00 + ((grossIncome - 202000.00)*.25) 
        if HealthPremium >= 900.00:
            HealthPremium = 900.00
    return HealthPremium

#Function computes net incomes by invoking 
def computeNetIncomes( grossIncomeList ) : #Step 2
    
    #defining and initializating netIncomeList
    netIncomeList = list ()
    
    #Invoking grossIncomeList and generating iteration for each element in the list 
    for i in grossIncomeList: 
        taxes=computeProvTaxes(i) + computeFedTaxes(i) + computeCPP(i) + computeEI(i) + computeHealthPremium(i)
        result=i-taxes
        result=float(format(result, '.2f' ))
        
        #Generation of the new list for netIncome
        netIncomeList.append (result)
    return netIncomeList

#function computes mean or average of a set of numbers
def means( inputList ) : #Step 3
    result=mean(inputList)
    return result

def standardDeviation( inputList, means ) : #Step 4
    result=pstdev(inputList)
    return result