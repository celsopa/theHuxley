d1 = int(input())
cn, rn, dn = map(float, input().split());
d2 = int(input())
ca, ra, cca, da = map(float, input().split());

tNatal = cn + rn + dn
tAno = ca + ra + cca + da

total = 0

mes = {19: [0.00, 0.10, 0.15],
       20: [0.00, 0.00, 0.00],
       21: [0.12, 0.15, 0.20],
       22: [0.20, 0.22, 0.30],
       23: [0.25, 0.29, 0.35],
       24: [0.35, 0.35, 0.50],
       25: [0.15, 0.13, 0.00, 0.10],
       26: [0.19, 0.25, 0.05, 0.23],
       27: [0.24, 0.30, 0.12, 0.33],
       28: [0.30, 0.32, 0.20, 0.35],
       29: [0.35, 0.40, 0.33, 0.42],
       30: [0.35, 0.40, 0.33, 0.42],
       31: [0.40, 0.47, 0.45, 0.66]}

if 20 <= d1 <= 24:
    print("Compras de natal: R$ {:.2f}.".format(tNatal - ((cn * mes[d1][0]) + (rn * mes[d1][1]) + (dn * mes[d1][2]))))
    total = tNatal - ((cn * mes[d1][0]) + (rn * mes[d1][1]) + (dn * mes[d1][2]))
elif d1 < 20:
    print("Compras de natal: R$ {:.2f}.".format(tNatal - ((cn * mes[19][0]) + (rn * mes[19][1]) + (dn * mes[19][2]))))
    total = tNatal - ((cn * mes[19][0]) + (rn * mes[19][1]) + (dn * mes[19][2]))
# else:
#     print("Compras de natal: R$ {:.2f}.".format(tNatal))
#     total = tNatal

if 25 <= d2 <= 31:
    print("Compras de ano novo: R$ {:.2f}.".format(
        tAno - ((ca * mes[d2][0]) + (ra * mes[d2][1]) + (cca * mes[d2][2]) + (da * mes[d2][3]))))
    total += tAno - ((ca * mes[d2][0]) + (ra * mes[d2][1]) + (cca * mes[d2][2]) + (da * mes[d2][3]))
else:
    print("Compras de ano novo: R$ {:.2f}.".format(tAno))
    total += tAno
print("Total das compras: R$ {:.2f}.".format(total))