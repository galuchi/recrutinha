---
name: avaliar-repo
description: Inspeciona tecnicamente o case de estágio em ./repos/<candidato>, calcula notas de 0 a 10 por pilar (pesos 0.2, 0.4, 0.4) e gera o parecer em ./feedbacks/<candidato>.md.
---

# Skill: Avaliação de Case Prático (Estágio)

Ao receber `/avaliar-repo <nome_ou_pasta_do_candidato>`, execute:

## 1. Localização e Validação do Alvo
- Identifique a pasta em `./repos/<candidato>`.
- Caso não exista, liste as pastas disponíveis em `./repos/` e encerre.

## 2. Inspeção Técnica
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

## 3. Cálculo da Nota Final
Calcule a nota final ponderada com duas casas decimais:
$$\text{Nota Final} = (\text{Nota Arq} \times 0.2) + (\text{Nota Front} \times 0.4) + (\text{Nota Back} \times 0.4)$$

## 4. Geração do Relatório
- Preencha `templates/feedback_template.md` com as notas atribuídas, o quadro preenchido e as evidências encontradas no código.
- Salve em `./feedbacks/<candidato>.md`.

## 5. Resposta no Terminal
Exiba no chat:
1. Caminho do arquivo `./feedbacks/<candidato>.md`.
2. Tabela resumida com as 3 notas parciais e a nota final.
3. Síntese em 2 linhas: principal ponto forte e principal ponto fraco para checagem na entrevista técnica.