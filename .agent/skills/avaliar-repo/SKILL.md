---
name: avaliar-repo
description: Inspeciona tecnicamente o case prático de um candidato em ./repos/<candidato> com base nos pilares de arquitetura/git, frontend/UX de incidentes e resiliência de backend, gerando o relatório em ./feedbacks/<candidato>.md.
---

# Skill: Avaliação de Case Prático

Ao receber o comando `#avaliar-repo <nome_ou_pasta_do_candidato>`, execute:

## 1. Localização e Validação do Alvo
- Identifique o diretório do candidato em `./repos/<candidato>`.
- Caso não exista, liste as pastas disponíveis em `./repos/` e encerre solicitando correção.

## 2. Inspeção Técnica Baseada nos Pilares do Case

Execute a varredura ignorando pastas de dependência (`node_modules`, `.venv`, `.git/objects`, `dist`, builds e lockfiles).

### Pilar 1: Arquitetura, Versionamento e Documentação
- **Histórico Git**: Inspecione o histórico de commits do repositório (`git log` ou árvore local de commits). Verifique se foi entregue em um único commit ("initial commit") ou se há construção progressiva com mensagens descritivas.
- **Estrutura de Pastas**: Verifique se a modularização faz sentido (separação lógica de componentes, hooks, controllers, regras de negócio).
- **Legibilidade de Código**: Observe coerência na nomenclatura de variáveis, funções e consistência de padrões.
- **README**: Verifique se há instruções claras de execução e se o candidato documentou e justificou suas decisões técnicas e trade-offs.

### Pilar 2: Frontend, UX e Design (Triagem de Incidentes)
- **Feedback Visual**: Verifique se existem estados explícitos de `loading`, desativação de botões durante requisições e tratamento de tela vazia/erro.
- **Atenção aos Detalhes**: Inspecione a consistência de estilos, tipografia e espaçamentos (uso de tokens, Tailwind ou CSS modular).
- **Diferenciais**: Cheque a presença de alternância entre Tema Claro/Escuro funcional e transições.
- **Design da Informação**: Analise como a listagem de incidentes foi construída. Há suporte visual para o analista priorizar rapidamente incidentes críticos (ex: badges de severidade, filtros rápidos, densidade adequada para ~100 itens)?

### Pilar 3: Backend, Lógica e Resiliência
- **Robustez e Validação**: Inspecione a validação de payloads nas rotas/endpoints (ex: Zod, Pydantic, class-validator) garantindo proteção contra dados inesperados.
- **Integridade e Concorrência**: Como o código trata dois analistas alterando o status do mesmo incidente simultaneamente? Há controle transacional, locking otimista (ex: campo `version`/`updatedAt`) ou lock no banco?
- **Resiliência de Rede/Banco**: Cheque o tratamento de erros em chamadas assíncronas (tratamento com `try/catch`, retentativas ou mensagens padronizadas em caso de queda de conexão).

## 3. Geração do Relatório
- Preencha o modelo em `templates/feedback_template.md` citando evidências concretas (nomes de arquivos e trechos de código).
- Salve o feedback em `./feedbacks/<candidato>.md`.

## 4. Retorno no Terminal
Exiba um resumo direto:
1. Caminho do arquivo gerado em `./feedbacks/<candidato>.md`.
2. Destaque do Histórico Git (progressivo vs. único).
3. Como o candidato abordou a concorrência no backend.
4. Nível de preparo da UI para triagem rápida de incidentes.