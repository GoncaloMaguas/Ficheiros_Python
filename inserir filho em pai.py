class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        novo_no = No(valor)

        if self.raiz is None:
            self.raiz = novo_no
        else:
            self._inserir_recursivo(self.raiz, novo_no)

    def _inserir_recursivo(self, no_atual, novo_no):
        if novo_no.valor < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = novo_no
            else:
                self._inserir_recursivo(no_atual.esquerda, novo_no)
        elif novo_no.valor > no_atual.valor:
            if no_atual.direita is None:
                no_atual.direita = novo_no
            else:
                self._inserir_recursivo(no_atual.direita, novo_no)

    def buscar(self, valor):
        if self.raiz is not None:
            return self._buscar_recursivo(valor, self.raiz)
        else:
            return None

    def _buscar_recursivo(self, valor, no_atual):
        if valor == no_atual.valor:
            return no_atual
        elif valor < no_atual.valor and no_atual.esquerda is not None:
            return self._buscar_recursivo(valor, no_atual.esquerda)
        elif valor > no_atual.valor and no_atual.direita is not None:
            return self._buscar_recursivo(valor, no_atual.direita)

    def imprimir_inorder(self, no_atual):
        if no_atual is not None:
            self.imprimir_inorder(no_atual.esquerda)
            print(no_atual.valor)
            self.imprimir_inorder(no_atual.direita)
            
            
    def alterar_valor(self, chave, novo_valor):
     no_para_alterar = self.buscar(chave)
     if no_para_alterar is not None:
         no_para_alterar.valor = novo_valor
         print(f"Valor do nó com chave {chave} alterado para {novo_valor}.")
     else:
             print(f"Nó com chave {chave} não encontrado na árvore.")
            
            
     def inserir_filho(self, chave_pai, chave_novo_filho):
        no_pai = self.buscar(chave_pai)

        if no_pai is None:
            print(f"Pai com chave {chave_pai} não encontrado na árvore.")
        elif no_pai.filho_esquerda is not None and no_pai.filho_direita is not None:
            print(f"Não é possível adicionar filho a pai com chave {chave_pai}, pois ele já tem dois filhos.")
        else:
            novo_filho = No(chave_novo_filho)
            if no_pai.filho_esquerda is None:
                no_pai.filho_esquerda = novo_filho
            else:
                no_pai.filho_direita = novo_filho
            print(f"Novo filho com chave {chave_novo_filho} adicionado ao pai com chave {chave_pai}.")
            
arvore = ArvoreBinaria()
arvore.inserir(10)
arvore.inserir(6)
arvore.inserir(14)
arvore.inserir(3)
arvore.inserir(8)

arvore.imprimir_inorder(arvore.raiz)

arvore.alterar_valor(arvore,3, 5)

arvore.imprimir_inorder(arvore.raiz)

arvore.inserir_filho(3, 5)



