

# 연간 매출 계산/출력
def get_yearly_revenue(monthly_revenue):
    return monthly_revenue * 12

monthly_revenue = 5500000
yearly_revenue = get_yearly_revenue(monthly_revenue)

# 연간 비용 계산/출력
def get_yearly_expenses(monthly_expenses):
    return monthly_expenses * 12

monthly_expenses = 2700000
yearly_expenses = get_yearly_expenses(monthly_expenses)

# 연간 수익 계산/출력
def get_yearly_profit(yearly_revenue, yearly_expenses):
    return yearly_revenue - yearly_expenses

yearly_revenue = get_yearly_revenue(monthly_revenue)
yearly_expenses = get_yearly_expenses(monthly_expenses)

# 세금 계산/출력
def get_tax_amount(profit):
    if profit > 100000:
        return profit * 0.25
    else: 
        return profit * 0.15

profit = get_yearly_profit(yearly_revenue, yearly_expenses)
tax_amount = get_tax_amount(profit)

# 세액 공제 적용/최종출력
def final_tax_amount(tax_amount, tax_credits):
    return tax_amount + tax_credits

tax_credits = tax_amount * 0.01
final_tax = final_tax_amount(tax_amount, tax_credits)

print(f"Your yearly_revenue is ${yearly_revenue}")
print(f"Your yearly_expenses is ${yearly_expenses}")
print(f"Your profit is ${profit}")
print(f"Your tax_amount is ${tax_amount}")
print(f"Your tax bill is ${final_tax}")
