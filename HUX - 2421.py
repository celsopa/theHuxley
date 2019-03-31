preco = int(input())
m500 = preco//500
m100 = (preco%500)//100
m50 = ((preco%500)%100)//50
m10 = (((preco%500)%100)%50)//10
m5 = ((((preco%500)%100)%50)%10)//5
m1 = ((((preco%500)%100)%50)%10)%5
print("""{} moedas de 500.
{} moedas de 100.
{} moedas de 50.
{} moedas de 10.
{} moedas de 5.
{} moedas de 1.""".format(m500, m100, m50, m10, m5, m1))