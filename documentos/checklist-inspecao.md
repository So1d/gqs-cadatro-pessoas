# CHECKLIST DE INSPEÇÃO
## A. Clareza e legibilidade

- [x] A1 — Os nomes das variáveis deixam claro o seu significado?
- [x] A2 — É possível compreender o que cada trecho faz sem executar o programa?
- [x] A3 — Textos e valores literais aparecem repetidos ao longo do código?

## B. Duplicação

- [x] B1 — Existe código repetido em pontos diferentes do programa?
- [x] B2 — A mesma regra está implementada em mais de um lugar?
- [x] B3 — A busca de uma pessoa aparece repetida?
- [x] B4 — A impressão dos dados de uma pessoa aparece repetida?

## C. Estrutura e complexidade

- [x] C1 — Há blocos muito extensos ou difíceis de acompanhar?
- [ ] C2 — É possível identificar rapidamente onde começa e termina cada responsabilidade?
- [x] C3 — Menu, leitura de dados, regras e exibição estão misturados no mesmo trecho?

## D. Entrada e validação de dados

- [x] D1 — Entradas inválidas podem causar comportamento inesperado?
- [ ] D2 — Existe verificação de faixa ou de plausibilidade para a idade?
- [x] D3 — Campos obrigatórios podem ser gravados vazios?

## E. Consistência dos dados

- [x] E1 — Os dados de uma mesma pessoa estão espalhados em variáveis que podem se desencontrar?
- [ ] E2 — Existe regra clara para identificar unicamente uma pessoa?
- [ ] E3 — Há política definida para nomes duplicados?

## F. Manutenibilidade e evolução

- [x] F1 — Acrescentar um novo atributo à pessoa exigiria alterar muitos pontos do código?
- [x] F2 — Uma nova operação faria o bloco principal crescer significativamente?
- [x] F3 — Alterar a interface com o usuário exigiria alterar a lógica do sistema?

## G. Comportamento e possíveis defeitos

- [ ] G1 — O comportamento para uma pessoa inexistente é adequado e informativo?
- [ ] G2 — Operações equivalentes tratam os mesmos dados de maneira coerente entre si?

---
