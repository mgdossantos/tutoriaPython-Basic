#🔹 1. Funções e módulos integrados (built-in)

# Esses já vêm com o Python, não precisam ser instalados.
# Para ver todos os nomes integrados disponíveis:
import builtins
print(dir(builtins))

for i, item in enumerate(dir(builtins), start=1):
    print(f"{i}. {item}")

#Para explorar funções/módulos integrados específicos:
import math, random
help(math)     # mostra tudo sobre o módulo math
help(random)   # mostra funções do random