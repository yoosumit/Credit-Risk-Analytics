""" | Borrower | EAD (₹ lakh) | 1-year PD | LGD |
| -------- | -----------: | --------: | --: |
| A        |          100 |        2% | 40% |
| B        |          250 |        5% | 45% |
| C        |          150 |        8% | 50% |
| D        |          500 |        1% | 35% |
 """

el_a = 100*0.02*0.4
el_b = 250*0.05*0.45
el_c = 150*0.08*0.5
el_d = 500*0.01*0.35


tpl = sum([el_a , el_b , el_c ,el_d ])

el_rate = tpl/(100+250+150+500)

high_loss = max(el_a,el_b, el_c, el_d)

print("Expected Loss:")
print("Borrower A:", el_a, "lakh")
print("Borrower B:", el_b, "lakh")
print("Borrower C:", el_c, "lakh")
print("Borrower D:", el_d, "lakh")

print("Total Expected Loss:", tpl, "lakh")
print("Portfolio EL Rate:", el_rate * 100, "%")
print("Highest Expected Loss:", high_loss, "lakh")
