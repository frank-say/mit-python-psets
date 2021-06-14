annual_salary = input('Enter the starting salary: ')
annual_salary = float(annual_salary)  # 获取输入的年薪

total_cost = 1000000  # 总房价 100w
semi_annual_raise = 0.07  # 每半年涨薪 7%
portion_down_payment = 0.25  # 首付比例 25%
r = 0.04  # 年化投资收益率 4%

if annual_salary * 3 < total_cost * portion_down_payment:
    print('It is not possible to pay the down payment in three years.')

low = 0
high = 10000
nums = 0
while low < high - 1:
    mid = (low + high) // 2
    month_salary = annual_salary / 12
    current_savings = 0
    portion_saved = mid / 10000
    nums += 1

    for i in range(1, 37):
        current_savings += current_savings * r / 12 + month_salary * portion_saved
        if i % 6 == 0:
            month_salary = month_salary * (1 + semi_annual_raise)

    if abs(total_cost * portion_down_payment - current_savings) < 100:
        break
    elif current_savings < total_cost * portion_down_payment:
        low = mid
    else:
        high = mid

if abs(total_cost * portion_down_payment - current_savings) < 100:
    print('Best savings rate:', portion_saved)
    print('Steps in bisection search:', nums)
