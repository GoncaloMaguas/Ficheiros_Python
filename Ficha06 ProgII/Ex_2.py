def processar_linha(linha, dicionario_prof, dicionario_estado):
    campos = linha.strip().split()
    
    iniciais = campos[0][0] + "." + campos[1][0] + "."
    idade = campos[2]
    
    if campos[3] in dicionario_prof:
        profissao = dicionario_prof[campos[3]]
    else:
        profissao = "Desconhecido"
        
    if campos[4] in dicionario_estado:
        estado_civil = dicionario_estado[campos[4]]
    else:
        estado_civil = "Desconhecido"
    
    return f"{iniciais} {idade} {profissao} {estado_civil}"


def processar_arquivo(entrada, saida, dicionario_prof, dicionario_estado):
    with open(entrada, "r") as f_in, open(saida, "w") as f_out:
        for linha in f_in:
            linha_processada = processar_linha(linha, dicionario_prof, dicionario_estado)
            if linha_processada:
                f_out.write(linha_processada + "\n")


dicionario_prof = {"101": "Engenheiro", "102": "Professor", "103": "Médico", "104": "Advogado"}
dicionario_estado = {"1": "Casado(a)", "2": "Solteiro(a)", "3": "Divorciado(a)"}
entrada = "dados_pessoais.txt"
saida = "dados_pessoais_processados.txt"
processar_arquivo(entrada, saida, dicionario_prof, dicionario_estado)
