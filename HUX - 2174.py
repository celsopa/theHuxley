m3Agua = float(input())
custoAgua = float(input())
totalAgua = m3Agua*1000*custoAgua
print("{:.2f}".format(custoAgua))
print("{:.2f}".format(custoAgua*80/100))
print("{:.2f}".format((custoAgua*80/100)+custoAgua))