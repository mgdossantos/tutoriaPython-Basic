import operations, inOutModules

a = inOutModules.askNumber()
b = inOutModules.askNumber()

result = operations.add(a, b)
inOutModules.output(result)