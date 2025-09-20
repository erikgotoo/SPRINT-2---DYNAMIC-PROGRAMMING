import bisect

class Insumo:
    def __init__(self, nome, quantidade, validade):
        self.nome = nome
        self.quantidade = quantidade
        self.validade = validade

    def __repr__(self):
        return f"{self.nome} (Qtd: {self.quantidade}, Val: {self.validade})"

class Fila:
    def __init__(self):
        self.itens = []

    def adicionar(self, item):
        self.itens.append(item)

    def remover(self):
        if not self.vazia():
            return self.itens.pop(0)
        return None

    def vazia(self):
        return len(self.itens) == 0

    def listar(self):
        return self.itens

class Pilha:
    def __init__(self):
        self.itens = []

    def adicionar(self, item):
        self.itens.append(item)

    def remover(self):
        if not self.vazia():
            return self.itens.pop()
        return None

    def vazia(self):
        return len(self.itens) == 0

    def listar(self):
        return self.itens[::-1]

def busca_sequencial(lista, nome):
    for item in lista:
        if item.nome.lower() == nome.lower():
            return item
    return None

def busca_binaria(lista, nome):
    nomes = [item.nome.lower() for item in lista]
    i = bisect.bisect_left(nomes, nome.lower())
    if i != len(lista) and nomes[i] == nome.lower():
        return lista[i]
    return None

def merge_sort(lista, chave=lambda x: x.nome):
    if len(lista) <= 1:
        return lista
    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio], chave)
    direita = merge_sort(lista[meio:], chave)
    return merge(esquerda, direita, chave)

def merge(esquerda, direita, chave):
    resultado = []
    i = j = 0
    while i < len(esquerda) and j < len(direita):
        if chave(esquerda[i]) <= chave(direita[j]):
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado

def quick_sort(lista, chave=lambda x: x.quantidade):
    if len(lista) <= 1:
        return lista
    ativo = lista[0]
    menores = [x for x in lista[1:] if chave(x) <= chave(ativo)]
    maiores = [x for x in lista[1:] if chave(x) > chave(ativo)]
    return quick_sort(menores, chave) + [ativo] + quick_sort(maiores, chave)

fila_consumo = Fila()
pilha_consumo = Pilha()

dados = [
    Insumo("Reagente A", 50, "2025-12-10"),
    Insumo("Descartável B", 120, "2026-01-05"),
    Insumo("Reagente C", 30, "2025-11-20"),
    Insumo("Descartável D", 200, "2026-02-01"),
    Insumo("Reagente E", 10, "2025-10-15"),
]

for item in dados:
    fila_consumo.adicionar(item)
    pilha_consumo.adicionar(item)

print("\n===== RELATÓRIO DE CONSUMO - ALMOXARIFADO DASA =====\n")

print("Consumo em ordem cronológica:")
print(fila_consumo.listar())

print("\nConsultas em ordem inversa:")
print(pilha_consumo.listar())

print("\nBusca Sequencial por 'Reagente C':")
print(busca_sequencial(dados, "Reagente C"))

print("\nBusca Binária por 'Descartável D':")
dados_ordenados_nome = merge_sort(dados, chave=lambda x: x.nome)
print(busca_binaria(dados_ordenados_nome, "Descartável D"))

print("\nOrdenação por Nome:")
print(merge_sort(dados, chave=lambda x: x.nome))

print("\nOrdenação por Quantidade:")
print(quick_sort(dados, chave=lambda x: x.quantidade))
