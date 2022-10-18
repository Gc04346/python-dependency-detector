# Detector automático de dependências para projetos Python

O algoritmo percorre todo o código de input, mapeando métodos definidos por cada componente. Em seguida, ele percorre novamente a base de código, identificando quais métodos são usados em cada componente da aplicação, gerando assim uma tabela de dependências.

## Tutorial

1. Insira cada arquivo Python (extensão .py) do módulo da aplicação em um sub-diretório de `input_files`.
2. Execute o arquivo `detector.py`.
3. O arquivo com a tabela de dependências estará no diretório `output`