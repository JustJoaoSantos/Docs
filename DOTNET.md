# Environment
Linguagem (C#) -> Database (SQL) -> Conteiner (Docker) -> Cloud (AWS)

# Compilers
* Compilador: Converte linguagem de alto nivel para baixo nivel, e.g C# -> Binary
* Transpilador: converte linguagem de alto nivel para alto nivel, e.g typescript -> javascript

code -> Lexicon Analyzer -> Syntax Analyzer -> IL Generator -> Code Optimizer -> Binary Generator

## .netcompiler
c# Code -> C# Compiler -> IL(Intermediary Language) Code (*.exe, *.dll) -> JIT (Just in Time) Compiler -> Native Code (Binary)

* verificar .net no cmd: "dotnet --info"