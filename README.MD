# Recrutinha - Toolkit de Avaliação de Cases Práticos

Ambiente padronizado para avaliação técnica, auditoria assistida por IA e consolidação de notas dos candidatos a estágio.

---

## 📁 Estrutura do Repositório

| Arquivo / Pasta | Descrição |
| :--- | :--- |
| **`.agent/skills/avaliar-repo/`** | Skill do assistente para auditoria técnica automatizada e análise de AI-Driven Development. |
| **`criterios.md`** | Régua oficial com a fórmula, matriz de pesos, critérios qualitativos e política de IA. |
| **`scripts/calcular_nota.py`** | Script CLI interativo para consolidação da nota final (Apresentação + Técnica). |
| **`prompts/case_specs.md`** | Enunciado e especificações do case vigente (gerenciado pelo usuário a partir do descritivo, mutável a cada processo seletivo). |
| **`prompts/reviewer_guidelines.md`** | Diretrizes de postura, calibragem técnica e avaliação de IA para nível de estágio. |
| **`templates/feedback_template.md`** | Modelo Markdown preenchido pela skill ao gerar o parecer individual. |
| **`repos/`** | Pasta local onde os repositórios dos candidatos devem ser clonados (*vazia no GitHub*). |
| **`feedbacks/`** | Pasta local onde os relatórios de feedback gerados são salvos (*vazia no GitHub*). |

---

## ⚡ Fluxo Rápido de Avaliação

1. **Clonar o repositório do candidato:**
   Clone o projeto do candidato dentro da pasta `repos/` e **renomeie a pasta para o nome do candidato**:
   ```bash
   git clone <url-do-candidato> repos/nome-candidato
   ```
2. **Executar a auditoria com a Skill:**
   No chat do assistente/IDE, execute o comando:
   ```text
   /avaliar-repo nome-candidato
   ```
   A skill inspeciona o código, audita o uso de IA, calcula a nota técnica e gera o relatório em `feedbacks/nome-candidato.md`.
3. **Revisar o parecer gerado:**
   Abra `feedbacks/nome-candidato.md` para conferir as evidências levantadas pela IA e ajustar o que for necessário.
   Lembre-se: a skill é um **auxílio** e não substitui o julgamento humano da banca. Na consolidação da nota final, ela representa apenas 20% do peso da avaliação técnica.
4. **Calcular a nota final:**
   Após fazer a avaliação técnica e a avaliação da apresentação, rode o script calculador para compor a nota final consolidada:
   ```bash
   python scripts/calcular_nota.py
   ```

---

## 🔍 Principais Componentes

### 1. Skill de Auditoria (`.agent/skills/avaliar-repo`)
Automatiza a inspeção estática do repositório em `repos/<candidato>` sob a perspectiva de estágio:
- **Pilares avaliados (Nota Base Ponderada):**
  - **Arquitetura, Git e Documentação (peso 0.2):** histórico de commits, clareza do README, modularização e nomenclatura.
  - **Frontend, UX e Design (peso 0.4):** gestão por exceção, escaneabilidade de dados, feedback visual (loadings/erros) e acabamento.
  - **Backend, Lógica e Resiliência (peso 0.4):** validação de payloads na borda, concorrência (conflitos de edição) e tratamento de erros.
- **Auditoria de AI-Driven Development (Uso Consciente de IA):**
  - Identifica uso de IA declarado ou inferido no repositório.
  - O uso de IA **não é punitivo**: avalia se o candidato agiu como piloto (com specs/PRD, workflows iterativos, guardrails e testes intencionais) ou como mero passageiro com *AI-Slop*.
  - Aplica modulação de nota pós-cálculo: **0.0** (uso consciente, nota mantida), **-0.5 a -1.0** (uso parcialmente consciente com controle frouxo) ou **até -2.0** (uso descabido / AI-slop puro).
- **Saída:** gera automaticamente `feedbacks/<candidato>.md` estruturado com quadro de notas completo, evidências técnicas e roteiro de sabatina para a banca.
- **Filtro:** ignora ruídos como `node_modules`, `.venv`, pastas de build e lockfiles.

### 2. Script Calculador de Nota (`scripts/calcular_nota.py`)
CLI interativo em Python que guia o avaliador na consolidação das notas:
- **Entrada amigável:** aceita notas de 0.0 a 10.0 tanto com ponto quanto com vírgula (ex: `8.5` ou `8,5`).
- **Composição da nota final:**
  - **Apresentação (peso 40%):** Manifestação (40%), Fluidez (30%), Convencimento (20%) e Qualidade do Vídeo (10%).
  - **Avaliação Técnica (peso 60%):** Arquitetura (20%), Frontend (30%), Backend (30%) e Auditoria de IA (20%).
- **Resultado:** exibe no terminal uma tabela colorida com todas as notas parciais, ponderações e a média final consolidada.

### 3. Matriz de Critérios (`criterios.md`)
Documento de referência absoluto do processo seletivo:
- Define detalhadamente o que esperar de cada nota em cada pilar e a política de AI-Driven Development.
- Garante isonomia entre múltiplos avaliadores da banca.
- Estabelece que o parecer da IA serve como insumo consultivo, mantendo a banca humana com autonomia total para ajustes (*override*).

---

## 📌 Orientações e Boas Práticas

- **Pastas `repos/` e `feedbacks/` no Git:**
  Ambas as pastas estão no `.gitignore` (mantendo apenas o `.gitkeep`) e permanecem vazias no GitHub. Elas são exclusivas do ambiente local de cada avaliador para armazenar temporariamente os candidatos sob sua responsabilidade.
- **Padronização de Nomes:**
  Sempre renomeie a pasta clonada do candidato para o padrão `repos/<nome-candidato>` (sem espaços ou caracteres especiais). A skill usa esse identificador para localizar o projeto e gerar o respectivo `feedbacks/<nome-candidato>.md`.
- **Gerenciamento das Specs do Case (`prompts/case_specs.md`):**
  Assim como `repos/` e `feedbacks/`, este arquivo é gerenciado pelo próprio usuário do repositório para refletir o case do processo seletivo vigente. A cada novo ciclo, gere as especificações a partir da descrição do case (você pode colar o enunciado ou solicitar a uma IA que estruture os requisitos e critérios técnicos a partir do descritivo do desafio). O restante da estrutura do toolkit se adapta automaticamente, mantendo a consistência da régua de avaliação.
