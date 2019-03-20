# csv2vcard

Se você tem uma planilha com diversos contatos (nomes, telefones) e deseja importá-los para sua lista de contatos no celular, este script feito em Python é para você.

O script lê um arquivo csv com duas colunas, a primeira com os nomes e a segunda com os telefones, você pode facilmente gerar este arquivo através do excel ou qualquer outro programa de planilha eletrônica.

# O que preciso para executar este script?

Apenas o Python versão 3 instalado em seu computador

# Importante:

Os números de telefone não devem conter caracteres como parênteses, barras, ponto, traços ou qualquer outra coisa, apenas números como no exemplo abaixo.
4111999998888

# Passos

1 - Após criar seu arquivo cvs, renomeie para "contatos.cvs" e cole no mesmo local do arquivo main.py

2 - Execute o arquivo main.py

no windows, execute com duplo clique, ou via linha de comando no Linux ou MacOS:

$ python3 main.py

ou

$ ./ main.py

3 - se não houver nenhum erro um arquivo com a extesâo vcf será criado na pasta vcard_export

4 - Envie o arquivo para o seu celular e clique no mesmo para instalar os novos contatos
