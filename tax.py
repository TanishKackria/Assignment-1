gross_income=input("enter the gross income")
dependents=input("enter the number of dependents")
standard_deduction=10000
dependent_deduction=3000
taxable_income=int(gross_income)-int(standard_deduction)-(int(dependent_deduction)*int(dependents))
tax_rate=0.2
tax=int(taxable_income)*int(tax_rate)
print(tax)
