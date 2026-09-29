# genpark-ast-static-code-analyzer-linter-skill

Agent Skill implementing **Python AST Static Analysis, Complexity Calculation & Security Linting** in 100% Python standard library.

## Architectural Flow
```mermaid
flowchart TD
    Source["Python Source Code"] --> AST["ast.parse() Abstract Syntax Tree"]
    AST --> Visitor["NodeVisitor Traversal"]
    Visitor --> C1["McCabe Cyclomatic Complexity (If/For Branches)"]
    Visitor --> C2["Docstring Completeness Validator"]
    Visitor --> C3["Dangerous Calls Detector (eval / exec)"]
    C1 & C2 & C3 --> Report["Structured Lint Audit Report"]
```
