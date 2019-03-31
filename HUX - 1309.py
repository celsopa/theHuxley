entrada = input().upper()
print({"F":"Feminino",
       "M":"Masculino"
}[entrada] if entrada in "MF" else "Sexo nao definido")