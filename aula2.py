# Atividade Hands-on Integrada - Gestão de Ativos
# Aluno: Antony Vasconcelos Theophilo De Azevedo

# ============================================================
# TAREFA 1
# Conjuntos A (Equipamentos) e B (Bairros)
# Produto cartesiano A x B e relação de atendimento
# ============================================================

equipamentos = {
    "EQ-001",
    "EQ-002",
    "EQ-003"
}

bairros = {
    "Centro",
    "Aldeota",
    "Meireles"
}

produto_cartesiano = {
    (equipamento, bairro)
    for equipamento in equipamentos
    for bairro in bairros
}

# Relação de atendimento:
# cada equipamento atende um determinado bairro
relacao_atendimento = {
    ("EQ-001", "Centro"),
    ("EQ-001", "Aldeota"),
    ("EQ-002", "Meireles"),
    ("EQ-003", "Centro")
}

print("=" * 60)
print("TAREFA 1 - PRODUTO CARTESIANO E RELAÇÃO")
print("=" * 60)

print("\nConjunto A - Equipamentos:")
print(sorted(equipamentos))

print("\nConjunto B - Bairros:")
print(sorted(bairros))

print("\nProduto cartesiano A x B:")
for par in sorted(produto_cartesiano):
    print(par)

print("\nRelação de atendimento:")
for par in sorted(relacao_atendimento):
    print(par)


# ============================================================
# TAREFA 2
# Função f: Ativo -> Secretaria
# Verificar se f é injetora e encontrar Im(f)
# ============================================================

ativos = {
    "ATIVO-001",
    "ATIVO-002",
    "ATIVO-003",
    "ATIVO-004"
}

secretarias = {
    "Secretaria de Educação",
    "Secretaria de Saúde",
    "Secretaria de Obras"
}

funcao_ativo_secretaria = {
    "ATIVO-001": "Secretaria de Educação",
    "ATIVO-002": "Secretaria de Saúde",
    "ATIVO-003": "Secretaria de Obras",
    "ATIVO-004": "Secretaria de Educação"
}


def verificar_funcao(dominio, funcao):
    return set(funcao.keys()) == dominio


def verificar_injetividade(funcao):
    valores = list(funcao.values())
    return len(valores) == len(set(valores))


def imagem(funcao):
    return set(funcao.values())


print("\n" + "=" * 60)
print("TAREFA 2 - FUNÇÃO ATIVO -> SECRETARIA")
print("=" * 60)

print("\nFunção f:")
for ativo, secretaria in sorted(funcao_ativo_secretaria.items()):
    print(f"{ativo} -> {secretaria}")

funcao_valida = verificar_funcao(ativos, funcao_ativo_secretaria)
e_injetora = verificar_injetividade(funcao_ativo_secretaria)
imagem_f = imagem(funcao_ativo_secretaria)

print("\nA função está definida para todos os ativos?", funcao_valida)
print("A função é injetora?", e_injetora)
print("Imagem Im(f):")
print(imagem_f)

if e_injetora:
    print("Conclusão: f é injetora.")
else:
    print("Conclusão: f NÃO é injetora, pois existem ativos associados à mesma secretaria.")


# ============================================================
# TAREFA 3
# Função inversa f^-1: Ativa -> Tombamento
# e verificação da bijetividade
# ============================================================

# Relação entre uma identificação ativa e seu tombamento
funcao_ativa_tombamento = {
    "ATIVA-001": "TOMB-901",
    "ATIVA-002": "TOMB-902",
    "ATIVA-003": "TOMB-903",
    "ATIVA-004": "TOMB-904"
}


def verificar