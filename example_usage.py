from client import ASTCodeLinter

source = """
def process(data):
    if data:
        for x in data:
            print(x)
    eval("print('danger')")
"""

report = ASTCodeLinter.analyze_source(source)
print("Complexity Score:", report["complexity"])
print("Found Issues:", report["issues"])
