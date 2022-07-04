#Overriding Example

class Ide:
    def functionalities(self):
        funcs=["create_file","rename","delete"]
        return funcs

class Pycharm(Ide):
    def functionalities(self):
        funcs=super().functionalities()
        funcs.append("execute")
        funcs.append("debug")
        return funcs

class Vscode(Ide):
    def functionalities(self):
        funcs=super().functionalities()
        funcs.append("vcs")
        funcs.append("formatting")
        return funcs

py=Pycharm()
print(py.functionalities())
vsc=Vscode()
print(vsc.functionalities())