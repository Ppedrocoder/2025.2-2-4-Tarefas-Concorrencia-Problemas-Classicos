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

## 5. Comportamento observado na Execução

```bash
Filósofo 0 está pensando 🤔
Filósofo 1 está pensando 🤔
Filósofo 2 está pensando 🤔
Filósofo 3 está pensando 🤔
Filósofo 4 está pensando 🤔
Filósofo 1 tentou pegar o talher 1
Filósofo 1 pegou o talher 1
Filósofo 1 tentou pegar o talher 2
Filósofo 1 pegou o talher 2
🍝 Filósofo 1 está comendo!
Filósofo 4 tentou pegar o talher 0
Filósofo 4 pegou o talher 0
Filósofo 4 tentou pegar o talher 4
Filósofo 4 pegou o talher 4
🍝 Filósofo 4 está comendo!
Filósofo 0 tentou pegar o talher 0
Filósofo 2 tentou pegar o talher 2
Filósofo 1 devolveu o talher 2
Filósofo 2 pegou o talher 2
Filósofo 1 devolveu o talher 1
Filósofo 2 tentou pegar o talher 3
Filósofo 2 pegou o talher 3
🍝 Filósofo 2 está comendo!
----------------------------------------
Filósofo 1 está pensando 🤔
Filósofo 3 tentou pegar o talher 3
Filósofo 4 devolveu o talher 4
Filósofo 4 devolveu o talher 0
----------------------------------------
Filósofo 4 está pensando 🤔
Filósofo 0 pegou o talher 0
Filósofo 0 tentou pegar o talher 1
Filósofo 0 pegou o talher 1
🍝 Filósofo 0 está comendo!
Filósofo 2 devolveu o talher 3
Filósofo 2 devolveu o talher 2
Filósofo 3 pegou o talher 3
----------------------------------------
Filósofo 3 tentou pegar o talher 4
Filósofo 3 pegou o talher 4
Filósofo 2 está pensando 🤔
🍝 Filósofo 3 está comendo!
Filósofo 4 tentou pegar o talher 0
Filósofo 1 tentou pegar o talher 1
Filósofo 0 devolveu o talher 1
Filósofo 1 pegou o talher 1
Filósofo 1 tentou pegar o talher 2
Filósofo 0 devolveu o talher 0
----------------------------------------
Filósofo 0 está pensando 🤔
Filósofo 1 pegou o talher 2
Filósofo 4 pegou o talher 0
🍝 Filósofo 1 está comendo!
Filósofo 4 tentou pegar o talher 4
Filósofo 3 devolveu o talher 4
Filósofo 4 pegou o talher 4
Filósofo 3 devolveu o talher 3
----------------------------------------
Filósofo 3 está pensando 🤔
🍝 Filósofo 4 está comendo!
Filósofo 2 tentou pegar o talher 2
Filósofo 3 tentou pegar o talher 3
Filósofo 3 pegou o talher 3
Filósofo 3 tentou pegar o talher 4
Filósofo 1 devolveu o talher 2
Filósofo 2 pegou o talher 2
Filósofo 1 devolveu o talher 1
Filósofo 2 tentou pegar o talher 3
----------------------------------------
Filósofo 1 está pensando 🤔
Filósofo 4 devolveu o talher 4
Filósofo 3 pegou o talher 4
Filósofo 4 devolveu o talher 0
----------------------------------------
Filósofo 4 está pensando 🤔
🍝 Filósofo 3 está comendo!
Filósofo 0 tentou pegar o talher 0
Filósofo 0 pegou o talher 0
Filósofo 0 tentou pegar o talher 1
Filósofo 0 pegou o talher 1
🍝 Filósofo 0 está comendo!
Filósofo 1 tentou pegar o talher 1
Filósofo 0 devolveu o talher 1
Filósofo 0 devolveu o talher 0
----------------------------------------
Filósofo 0 está pensando 🤔
Filósofo 1 pegou o talher 1
Filósofo 1 tentou pegar o talher 2
Filósofo 3 devolveu o talher 4
Filósofo 3 devolveu o talher 3
----------------------------------------
Filósofo 2 pegou o talher 3
Filósofo 3 está pensando 🤔
🍝 Filósofo 2 está comendo!
Filósofo 4 tentou pegar o talher 0
Filósofo 4 pegou o talher 0
Filósofo 4 tentou pegar o talher 4
Filósofo 4 pegou o talher 4
🍝 Filósofo 4 está comendo!
Filósofo 4 devolveu o talher 4
Filósofo 4 devolveu o talher 0
----------------------------------------
Filósofo 4 está pensando 🤔
Filósofo 2 devolveu o talher 3
Filósofo 2 devolveu o talher 2
```

No que pode ser observado, cinco filósofos (threads) alternam entre pensar e comer, precisando de dois talheres (locks) para se alimentar. Cada filósofo pensa por um tempo aleatório, tenta adquirir dois talheres, come ao obtê-los e depois os devolve.

A execução é não determinística, pois os tempos de espera são aleatórios e as threads concorrem entre si. Isso gera interleaving nas mensagens do log, mostrando filósofos simultaneamente pensando, aguardando talheres ou comendo.

Para evitar deadlock, todos os filósofos seguem uma ordem global de aquisição: sempre pegam primeiro o talher de menor índice e depois o de maior. Assim, elimina-se a espera circular e o sistema continua progredindo.

Embora ainda possa ocorrer starvation em teoria, o trecho observado mostra que todos os filósofos conseguem comer em algum momento. A simulação, portanto, demonstra concorrência, exclusão mútua e prevenção de deadlock de forma eficaz.

## 6. Considerações Finais

Através do desenvolvimento da atividade baseada no desafio do jantar dos filósofos, foi possível compreender de forma prática o funcionamento de múltiplos processos executando de maneira concorrente, onde, em determinados momentos, diferentes threads tentam realizar a mesma ação simultaneamente, podendo ter sua execução negada ou concluída com êxito.

O uso de mecanismos de sincronização, como os Locks, mostrou-se imprescindível para o funcionamento coeso do código, garantindo a exclusão mútua no acesso aos recursos compartilhados. Nesse contexto, os talheres são bloqueados quando utilizados por um filósofo e liberados após o uso, evitando condições de corrida e assegurando a integridade da execução concorrente.
