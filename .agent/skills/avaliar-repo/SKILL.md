---
name: avaliar-repo
description: Inspeciona tecnicamente o case de estágio em ./repos/<candidato>, calcula notas de 0 a 10 por pilar (pesos 0.2, 0.4, 0.4), audita governança de AI-Driven Development (penalidade pós-cálculo de 0 a 2 pts) e gera o parecer em ./feedbacks/<candidato>.md.
---

# Skill: Avaliação de Case Prático (Estágio)

Ao receber `/avaliar-repo <nome_ou_pasta_do_candidato>`, execute:

## 1. Localização e Validação do Alvo
- Identifique a pasta em `./repos/<candidato>`.
- Caso não exista, liste as pastas disponíveis em `./repos/` e encerre.

## 2. Inspeção Técnica dos Três Pilares
Ignore: `node_modules`, `.venv`, `dist`, builds e lockfiles.
Avalie o repositório sob o prisma de **um candidato a estágio**.

### Régua de Pontuação por Pilar (0 a 10):

#### 1. Arquitetura, Git e Documentação (Peso 0.2)
- **0 a 4:** Commit único ("initial commit"), sem README ou instruções que não funcionam, código desorganizado em um único arquivo gigante.
- **5 a 7:** README básico funcional, pastas razoavelmente separadas, commits em pequenos blocos (mesmo com mensagens curtas).
- **8 a 10:** Histórico nítido e progressivo de commits, README excelente explicando como rodar e justificando trade-offs, código legível e limpo.

#### 2. Frontend, UX e Design (Peso 0.4)
- **0 a 4:** Interface quebrada, sem qualquer loading/feedback ao clicar, listagem confusa onde é impossível distinguir incidentes críticos de leves.
- **5 a 7:** Interface funcional com listagem clara e feedbacks básicos de loading, mas sem atenção especial a espaçamento/tipografia ou diferenciais.
- **8 a 10:** Pensada para triagem rápida (badges claras de prioridade, filtros rápidos), botões desabilitados durante requisição com feedback imediato, modo dark/light ou transições fluidas.

#### 3. Backend, Lógica e Resiliência (Peso 0.4)
- **0 a 4:** Sem validação de payloads (API quebra com HTTP 500 ao receber campo inválido), sem tratamento de erros, ignora concorrência completamente.
- **5 a 7:** Validações presentes na entrada de dados, tratamento de try/catch nas rotas, endpoints REST estruturados, mas resolve concorrência com sobrescrita cega.
- **8 a 10:** Validações defensivas, tratamento de concorrência intencional (lock otimista com version/timestamp, lock no banco ou validação explícita de conflito) e retentativas ou mensagens claras em caso de lentidão/erro.

---

## 3. Cálculo da Nota Base Ponderada
Calcule a nota técnica base com duas casas decimais:
$$\text{Nota Base Ponderada} = (\text{Nota Arq} \times 0.2) + (\text{Nota Front} \times 0.4) + (\text{Nota Back} \times 0.4)$$

---

## 4. Auditoria de AI-Driven Development (Uso Consciente de IA)

O uso de IA **não é punitivo nem eliminatório**. É esperado e incentivado que o candidato saiba alavancar ferramentas modernas, desde que atue como **piloto**, mantenha discernimento técnico e gere código livre de *AI-Slop*.

### 4.1 Identificação do Uso de IA
- **Transparente / Declarado:** O candidato cita explicitamente no README, PRD, commit messages, PRs ou adiciona arquivos de configuração de agentes/ferramentas (`.cursor/`, `.cursorrules`, `CLAUDE.md`, `.agent/`, `.github/copilot-instructions.md`, etc.).
- **Inferido / Padrões Técnicos:** Padrões característicos de modelos (docstrings redundantes em estilo padronizado para funções óbvias, commits automatizados com bullets semânticos idênticos, scaffolds densos descolados da maturidade habitual sem justificativa orgânica, resíduos de prompts no código).
- *Se nenhum uso de IA for detectado:* A penalidade é **0.0** e a Nota Final é igual à Nota Base Ponderada.

### 4.2 Critérios de Avaliação do Uso de IA
Caso haja uso de IA (declarado ou inferido), avalie:
1. **Specs & Requisitos:** Há especificações prévias, PRD, diagramas ou listas de requisitos que guiaram a IA de forma intencional?
2. **Workflows & Rituais:** O trabalho foi feito de forma iterativa (etapa por etapa, commits incrementais, branches/PRs, revisão prévia) ou foi um despejo de código em bloco único?
3. **Guardrails & Regras:** Foram estabelecidas diretrizes de arquitetura, tipagem estrita, convenções de código ou regras de contexto para a IA não alucinar?
4. **Piloto vs. Passageiro & Controle de AI-Slop:** O desenvolvedor demonstra controle e influência real sobre o projeto? Os testes cobrem cenários reais e críticos (ex: testes de concorrência e resiliência) ou são testes triviais gerados em massa? O código está enxuto ou possui *AI-Slop* (código zumbi, dependências desnecessárias, abstrações ocas ou comentários redundantes de LLM)?

### 4.3 Régua de Penalidade Pós-Cálculo
- **Uso Consciente e Direcionado (Penalidade: 0.0 pts):**
  - O candidato conduziu o desenvolvimento como engenheiro-piloto.
  - Specs claras, workflow estruturado, guardrails ativos, testes intencionais e total ausência de AI-slop relevante.
  - **A nota base ponderada é mantida integralmente.**
- **Uso Parcialmente Consciente / Desalinhado (Penalidade: -0.5 a -1.0 pt):**
  - O candidato utilizou IA com controle frouxo.
  - Faltam specs consistentes ou guardrails explícitos; aceitou trechos gerados sem refinamento pleno; há resíduos leves de AI-slop ou testes genéricos; postura mais passiva que ativa, embora o projeto funcione.
  - **Perde de 0.5 a 1.0 ponto da nota total.**
- **Uso Descabido / AI-Slop Puro (Penalidade: -1.1 a -2.0 pts):**
  - O candidato terceirizou o pensamento crítico e atuou como mero passageiro.
  - Geração em bloco único sem specs nem guardrails, presença dominante de AI-slop (código inflado, arquiteturas desnecessariamente complexas mal compreendidas, dependências órfãs, comentários óbvios de IA sem limpeza).
  - Perda clara de controle técnico e discernimento.
  - **Perde de 1.1 até 2.0 pontos inteiros da nota total.**

---

## 5. Cálculo da Nota Final Sugerida
$$\text{Nota Final} = \max(0.0, \text{Nota Base Ponderada} - \text{Penalidade IA})$$

---

## 6. Geração do Relatório
- Preencha `templates/feedback_template.md` com as notas atribuídas, o quadro detalhado (Nota Base, Classificação de IA, Penalidade e Nota Final) e as evidências encontradas no código e nos rituais de desenvolvimento.
- Salve em `./feedbacks/<candidato>.md`.

---

## 7. Resposta no Terminal
Exiba no chat:
1. Caminho do arquivo `./feedbacks/<candidato>.md`.
2. Tabela consolidada com as notas parciais (0 a 10), Nota Base Ponderada, Avaliação de IA (classificação e penalidade) e Nota Final Sugerida.
3. Síntese em 3 tópicos diretos:
   - **Ponto Forte:** Principal destaque técnico.
   - **Ponto Fraco / Atenção:** Principal vulnerabilidade ou ponto cego.
   - **Sabatina Técnica (Banca):** 1 a 2 perguntas para validar o real domínio técnico do candidato sobre as soluções implementadas (especialmente em pontos sugeridos por IA).
