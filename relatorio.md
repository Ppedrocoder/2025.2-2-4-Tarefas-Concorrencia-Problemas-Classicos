# Jantar dos Filósofos com Threads em Python

## 1. Contexto inicial do trabalho

Este trabalho foi desenvolvido como parte da disciplina de Sistemas Operacionais, no semestre letivo 2025.2, com o objetivo de implementar uma solução para o clássico Problema do Jantar dos Filósofos, abordando conceitos fundamentais de concorrência, sincronização e prevenção de deadlock.

O problema ilustra as dificuldades enfrentadas por processos concorrentes que compartilham recursos limitados, exigindo técnicas adequadas para garantir segurança e progresso do sistema.

## 2. Descrevendo a solução em Python para o jantar dos filósofos

A solução foi implementada utilizando a linguagem Python e a biblioteca `threading`. Cada filósofo é representado por uma thread independente, e cada talher é representado por um objeto do tipo `Lock`.

Os filósofos alternam entre os estados de pensar e comer. Para comer, é necessário obter dois talheres adjacentes. Como os talheres são recursos compartilhados, foi necessário aplicar técnicas de exclusão mútua e prevenção de impasse.

## 3. Implementando o algoritmo

### 3.1 Qual o algoritmo utilizado

Foi utilizada a estratégia de **prevenção de deadlock por ordenação de recursos**. Nessa abordagem, cada filósofo sempre tenta pegar primeiro o talher de menor índice e, em seguida, o de maior índice.

Essa técnica elimina a possibilidade de espera circular, uma das condições necessárias para a ocorrência de deadlock.

### 3.2 Implementação do algoritmo em Python

Cada filósofo executa em loop infinito:

- pensa por um tempo aleatório

- tenta pegar os talheres seguindo a ordem definida
- come por um tempo aleatório
- devolve os talheres

O uso de `Lock` garante exclusão mútua no acesso aos talheres.

## 4. Tratando impasse

### 4.1 Estratégia de tratamento de impasses

A estratégia adotada foi a **prevenção**, e não a detecção ou recuperação de deadlocks. Ao impor uma ordem global para aquisição dos recursos, o sistema impede que um ciclo de espera seja formado.

### 4.2 Implementação do tratamento de impasse em Python

```python
primeiro = min(esquerdo, direito)
segundo = max(esquerdo, direito)
```

## 5. Considerações Finais

Através do desenvolvimento da atividade baseada no desafio do jantar dos filósofos, foi possível compreender de forma prática o funcionamento de múltiplos processos executando de maneira concorrente, onde, em determinados momentos, diferentes threads tentam realizar a mesma ação simultaneamente, podendo ter sua execução negada ou concluída com êxito.

O uso de mecanismos de sincronização, como os Locks, mostrou-se imprescindível para o funcionamento coeso do código, garantindo a exclusão mútua no acesso aos recursos compartilhados. Nesse contexto, os talheres são bloqueados quando utilizados por um filósofo e liberados após o uso, evitando condições de corrida e assegurando a integridade da execução concorrente.
