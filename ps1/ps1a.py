annual_salary = input('Enter your annual salary: ')
annual_salary = float(annual_salary)  # 获取输入的年薪
portion_saved = input(
    'Enter the percent of your salary to save, as a decimal: ')
portion_saved = float(portion_saved)  # 获取输入的存钱比例
total_cost = input('Enter the cost of your dream home: ')
total_cost = float(total_cost)  # 获取房子总价

portion_down_payment = 0.25  # 首付比例 25%
r = 0.04  # 年化投资收益率 4%

i = 0  # 月份数
current_savings = 0  # 当前资金

while current_savings < total_cost * portion_down_payment:
    i += 1
    current_savings += current_savings * r / 12 + annual_salary * portion_saved / 12

print('Number of months:', i)
