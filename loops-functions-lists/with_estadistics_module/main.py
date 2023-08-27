from qualityAssurance import gradeAssignment #imports only the gradeAssignment operation from module QualityAssurance
from stubsA2 import *

def main() :
    #engineering the program components developed above
    grossIncomeList = buildGrossIncomeList( numberOfEmployees ) # Step 1 - function built is invoked here
    netIncomeList = computeNetIncomes( grossIncomeList ) # Step 2 - function built is invoked here
    meanOfIncome = means( netIncomeList )
    standardDeviationOfIncome = standardDeviation( netIncomeList, meanOfIncome ) 


    #-------------------------------------- Outputs ------------------------------------------------
    print("\n\n------------------------- Nova Scotia's Tax Calculator -------------------------")
    print(f"Employees' taxable incomes CAD($): {grossIncomeList}") # Step 5
    print(f"Employees' net incomes (after tax deductions) CAD($): {netIncomeList}")  # Step 5
    print(f"Mean of net incomes : CAD($) {format( meanOfIncome, '.2f' )}") # Step 3, , Step 5
    print(f"Standard deviation of net incomes : CAD($) {format( standardDeviationOfIncome, '.2f' )}") # Step 4, Step 5
    
    gradeAssignment()
    
main()