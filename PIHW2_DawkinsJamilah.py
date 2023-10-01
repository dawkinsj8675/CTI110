# A brief description of the project
# 09/28/2023
# CTI-110 P1HW2 - Travel Expense
# Jamilah Dawkins
#

Budget = int(input())
Destination = input()
Gas_Budget = int(input())
Accomd_Budget= int(input())
Food_Budget = int(input())
Total = ( Gas_Budget + Accomd_Budget + Food_Budget )
Balance = ( Budget - Total )


print('Enter Budget', Budget )
print('Enter your travel destination:', Destination )

print('How much do you think you will spend on gas?', Gas_Budget )
print('Approximately, how much will you need for accomodation/hotel?', Accomd_Budget )
print('Last, how much do you need for food?', Food_Budget )

print('-------------Travel Expenses-------------')

print('Location:', Destination)
print('Initial Budget:', Budget)

print('Fuel:', Gas_Budget )
print('Accommodation:', Accomd_Budget )
print('Food:', Food_Budget )

print('Remaining Balance:', Balance )

# 11 - Pseudocode #
# Balance = ( Budget - ( Gas_Budget + Accomd_Budget + Food_Budget ))
