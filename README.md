# csv2vcard

Se você tem uma planilha com diversos contatos (nomes, telefones) e deseja importá-los para sua lista de contatos no celular, este script feito em Python pode ajudá-lo.

O script lê um arquivo com a extensão `csv` contendo duas colunas. A primeira coluna deve conter os nomes a segunda os telefones. Você pode facilmente gerar um arquivo `csv` através do excel ou qualquer outro programa de planilha eletrônica.

# O que preciso para executar este script?

Python versão `>=3` instalado em seu computador, ou pode executar o script através do [replit.com](https://replit.com/)

# Importante:

Os números dos telefones não devem conter caracteres como, parênteses `()`, barras `\` `/`, ponto `.`, traços `-` ou qualquer outra coisa, apenas números, exemplo: `4111999998888`

# Passos

1 - Após criar o arquivo `cvs` renomeie para `contatos.cvs` e cole no mesmo local do arquivo `main.py`

2 - Execute o script: no windows execute o arquivo `main.py` dando um duplo clique. Para executar via linha de comando no Linux ou MacOS utilize `$ python3 main.py` ou `$ ./ main.py`.

3 - Se não houver nenhum erro, um arquivo com a extensão `vcf` será criado na pasta vcard_export

4 - Envie o arquivo gerado para o seu celular e clique sobre o mesmo para instalar os novos contatos
