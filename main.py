#!/usr/bin/env python3
import os

if __name__ == '__main__':

    # Remove o arquivo vcf
    if "contatos.vcf" in os.listdir('vcard_export'):
        os.remove("vcard_export/contatos.vcf")

    # Abre arquivo csv
    csv = open("contatos.csv", mode = "r", encoding="utf-8")

    # Cria arquivo vcf
    with open("vcard_export/contatos.vcf", mode="a", encoding="utf-8") as vcf:

        # Lê linha por linha
        for registro in csv:

            # trata a linha removendo caracteres especiais
            contato = registro.strip()

            print(contato)

            # separa o nome do contato e o número
            contato = contato.split(",")

            nome_completo = contato[0]
            telefone = contato[1]

            # substitui os espaços no nome por ponto e virgula
            nome_com_separador = nome_completo.replace(" ", ";")
            
            # Template Contato
            vcf.write("BEGIN:VCARD\n")
            vcf.write("VERSION:2.1\n")
            vcf.write("N:"+nome_com_separador+";;;\n")
            vcf.write("FN:"+nome_completo+"\n")
            vcf.write("TEL;CELL:"+telefone+"\n")
            vcf.write("END:VCARD\n")