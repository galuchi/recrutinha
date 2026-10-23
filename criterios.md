# Critérios e Diretrizes de Avaliação: Case Prático e Apresentação

Este documento estabelece o modelo de cálculo, a distribuição de pesos e os critérios qualitativos para a composição da nota final dos candidatos no processo seletivo.

---

## 1. Estrutura Geral e Fórmula da Nota Final

Todas as notas parciais e subcritérios são avaliados em uma escala linear de **0,0 a 10,0**. A nota final do candidato é uma média ponderada composta por duas grandes frentes de avaliação:

| Frente de Avaliação | Peso na Nota Final | Descrição |
| :--- | :---: | :--- |
| **Apresentação (Pitch / Vídeo)** | **0,4 (40%)** | Habilidades de comunicação verbal, postura, clareza e poder de convencimento na defesa da solução. |
| **Avaliação Técnica** | **0,6 (60%)** | Qualidade do código entregue, arquitetura, design visual, robustez da lógica e parecer da IA. |

**Fórmula da nota final:**

```text
Nota Final = (Nota Apresentação * 0,4) + (Nota Técnica * 0,6)
```

## 2. Composição da Nota de Apresentação (Peso 0,4)

A nota de apresentação mede a capacidade do candidato de transmitir suas ideias, justificar escolhas e se posicionar profissionalmente através do vídeo submetido.

| Subcritério | Peso no Pilar 
| :--- | :---: | 
| Manifestação | 0,4 | 
| Fluidez | 0,3 | 
| Convencimento | 0,2 | 
| Qualidade do Vídeo | 0,1 | 
| **Total do Pilar** | **1,0** | 

```text
Nota Apresentação = (Manifestação * 0,4) + (Fluidez * 0,3) + (Convencimento * 0,2) + (Qualidade do Vídeo * 0,1)
```

## 3. Composição da Nota Técnica (Peso 0,6)

A nota técnica consolida a entrega de engenharia de software do candidato. Ela é dividida em três pilares avaliados manualmente pela banca humana (80% da nota técnica) e um pilar de auditoria automatizada via IA (20% da nota técnica).

| Pilar Técnico | Peso no Pilar | Subcritérios e Pesos Internos |
| :--- | :---: | :--- |
| **1. Arquitetura e Práticas** | 0,2 (20%) | Documentação (0,30); Histórico Git (0,25); Organização e Modularização (0,25); Clareza e Nomenclatura (0,20) |
| **2. Frontend e UX** | 0,3 (30%) | Design da Informação (0,35); Feedback Visual (0,30); Atenção aos Detalhes (0,20); Diferenciais (0,15) |
| **3. Backend e Resiliência** | 0,3 (30%) | Integridade e Concorrência (0,40); Robustez e Validação (0,35); Tratamento de Exceções (0,25) |
| **4. Auditoria Técnica (IA)** | 0,2 (20%) | Nota direta (0,0 a 10,0) atribuída pelo parecer automatizado da skill |
| **Total Técnico** | **1,0 (100%)** | Soma ponderada dos 4 pilares |

```text
Nota Técnica = (Nota Arquitetura * 0,2) + (Nota Frontend * 0,3) + (Nota Backend * 0,3) + (Nota IA * 0,2)
```

## 4. Detalhamento dos Pilares e Subcritérios

### A. Apresentação (Pitch / Vídeo)

#### 1. Manifestação (Peso 0,4)

Avalia a autenticidade, clareza verbal e segurança com que o candidato se expressa.

**O que observar:**
- O candidato está de câmera ligada? Ponto crucial para o pilar, sujeito a punição grave caso não haja vídeo.
- O candidato fala de maneira natural ou parece excessivamente mecanizado/decorado?
- Demonstra domínio do que está explicando?
- Utiliza vocabulário técnico coerente com o nível de estágio sem recorrer a rodeios ou desculpas sobre o que não conseguiu fazer?

#### 2. Fluidez (Peso 0,3)

Mede o ritmo, a concatenação de ideias e a organização lógica do discurso.

**O que observar:**
- A apresentação tem início, meio e fim claros (apresentação pessoal → problema → solução construída → aprendizados)?
- As transições entre os tópicos são naturais ou há bloqueios constantes, pausas desconfortáveis e fuga do tema central?

#### 3. Convencimento (Peso 0,2)

Capacidade de defender suas escolhas e demonstrar valor na solução entregue.

**O que observar:**
- O candidato transmite confiança nas decisões que tomou?
- Consegue defender por que escolheu determinada stack ou arquitetura?
- Se houvesse limitações no case, demonstrou clareza de como evoluiria o projeto caso tivesse mais tempo?

#### 4. Qualidade do Vídeo (Peso 0,1)

Avaliação de higiene e cuidado com os aspectos técnicos básicos da gravação.

**O que observar:**
- O áudio é compreensível e limpo, sem ruídos estáticos graves que impeçam a compreensão?
- O enquadramento, a iluminação e a captura de tela (se houver demonstração prática) estão legíveis e nítidos?

### B. Técnica: Arquitetura, Qualidade e Boas Práticas (Peso 0,2)

```text
Nota Arquitetura = (Doc * 0,30) + (Git * 0,25) + (Org * 0,25) + (Clareza * 0,20)
```

#### 1. Documentação (Peso 0,30)

**Critério:** Qualidade e utilidade do `README.md`.

**Expectativa:** Instruções reproduzíveis de execução (setup de ambiente, dependências e variáveis de ambiente). Justificativas explícitas sobre as escolhas arquiteturais, bibliotecas utilizadas e trade-offs assumidos durante o desenvolvimento.

#### 2. Histórico de Versionamento (Peso 0,25)

**Critério:** Uso do Git como ferramenta de trabalho progressiva.

**Expectativa:** Repositórios construídos com commits atômicos, progressivos e mensagens explicativas. Entregas contendo um único commit no final (`initial commit` com o projeto pronto) ou mensagens genéricas (ex.: `update`, `fix`, `wip`) devem ser penalizadas.

#### 3. Organização e Modularização (Peso 0,25)

**Critério:** Separação de pastas e responsabilidades.

**Expectativa:** Estrutura lógica de diretórios que separa regras de negócio, camada visual/componentes, utilitários e integração com dados. Ausência de arquivos monolíticos (ex.: colocar todas as regras, estilização e chamadas de API em um único arquivo de centenas de linhas).

#### 4. Clareza e Nomenclatura (Peso 0,20)

**Critério:** Legibilidade e intenção do código.

**Expectativa:** Nomes de variáveis, funções, componentes e rotas que descrevem com precisão sua função. Código legível sem abreviações arbitrárias ou funções longas e confusas.

### C. Técnica: Frontend, UX e Design (Peso 0,3)

```text
Nota Frontend = (Design da Informação * 0,35) + (Feedback Visual * 0,30) + (Detalhes UI * 0,20) + (Diferenciais * 0,15)
```

#### 1. Design da Informação (Peso 0,35)

**Critério:** Eficiência na gestão por exceção (~100 incidentes simultâneos).

**Expectativa:** O analista precisa identificar o que é crítico em poucos milissegundos. A interface utiliza densidade adequada, filtros rápidos, categorização clara por severidade (ex.: badges coloridas semânticas) e hierarquia visual que prioriza o que é grave sobre o que é informativo.

#### 2. Feedback Visual (Peso 0,30)

**Critério:** Resposta visual às ações do usuário.

**Expectativa:** O usuário nunca fica na dúvida se a aplicação travou. Presença de skeletons ou spinners de carregamento, botões desabilitados durante o envio de formulários/requisições (para evitar duplo clique acidental) e mensagens amigáveis em caso de erro.

#### 3. Atenção aos Detalhes (Peso 0,20)

**Critério:** Acabamento e consistência da interface.

**Expectativa:** Alinhamentos coerentes, espaçamentos padronizados (padding/margin), tipografia hierarquizada e contraste adequado de cores que garanta boa legibilidade.

#### 4. Diferenciais de Usabilidade (Peso 0,15)

**Critério:** Polimento adicional da experiência do usuário.

**Expectativa:** Implementação funcional de alternância entre Modo Claro/Escuro (Dark Mode) sem quebrar contrastes, transições suaves de estado e microinterações fluidas.

### D. Técnica: Backend, Lógica e Resiliência (Peso 0,3)

```text
Nota Backend = (Concorrência * 0,40) + (Validação * 0,35) + (Exceções * 0,25)
```

#### 1. Integridade e Concorrência (Peso 0,40)

**Critério:** Tratamento de alterações simultâneas no mesmo recurso.

**Expectativa:** Demonstração de intencionalidade para tratar conflito quando dois analistas alteram o mesmo incidente ao mesmo tempo. Abordagens aceitáveis variam desde lock otimista (controle por campo de versão/data de atualização), validação de status prévio ou bloqueio explícito, evitando sobrescrita cega de dados (*last-write-wins* silencioso).

#### 2. Robustez e Validação de Entradas (Peso 0,35)

**Critério:** Resguardo da aplicação contra dados inesperados.

**Expectativa:** Validação estruturada de payloads nas bordas das rotas (ex.: tipos incorretos, campos ausentes, textos maiores que o limite). A aplicação deve retornar códigos HTTP semânticos (ex.: `400 Bad Request` com corpo explicativo) e nunca estourar erros 500 não tratados para entradas inválidas.

#### 3. Tratamento de Exceções de Rede e Banco (Peso 0,25)

**Critério:** Resiliência a lentidões e falhas temporárias.

**Expectativa:** O código sabe lidar de forma defensiva com quedas de conexão do banco de dados ou APIs externas. Presença de blocos `try/catch` estruturados, logs de erro informativos e retorno amigável para a camada consumidora sem derrubar o processo da aplicação.

### E. Técnica: Auditoria Automatizada por IA (Peso 0,2)

A nota de Auditoria por IA (0,0 a 10,0) é gerada pela skill técnica do assistente de terminal/IDE ao analisar o repositório clonado em `./repos/<candidato>`.

**Função no processo:** Atua como um olhar analítico padronizado que busca evidências de higiene de código, varre arquivos em busca de segredos expostos (`.env`), checa a consistência de tipagem e confere se os critérios mandatórios descritos no case foram atendidos.

**Composição da Nota da Skill:**
1. **Nota Base Ponderada:** Calculada sobre a inspeção técnica dos três pilares fundamentais do repositório:
   $$\text{Nota Base Ponderada} = (\text{Arquitetura} \times 0.2) + (\text{Frontend} \times 0.4) + (\text{Backend} \times 0.4)$$
2. **Auditoria de AI-Driven Development (Uso Consciente de IA):**
   O uso de ferramentas de IA (declarado ou inferido) **não é punitivo nem eliminatório**, desde que o candidato atue como engenheiro-piloto e demonstre influência e domínio sobre o resultado:
   - **Uso Consciente e Direcionado (Penalidade: 0,0):** O candidato define specs/PRDs, opera em workflows estruturados, adota guardrails/regras, realiza testes intencionais e não gera *AI-Slop*. A nota base é mantida integralmente.
   - **Uso Parcialmente Consciente / Desalinhado (Penalidade: -0,5 a -1,0):** Uso de IA com controle frouxo, carência de specs ou guardrails explícitos, postura mais passiva ou resíduos leves de código morto/AI-slop.
   - **Uso Descabido / AI-Slop Puro (Penalidade: -1,1 a -2,0):** Terceirização total do pensamento crítico; ausência de controle sobre o código gerado; presença marcante de *AI-slop* (código inchado, alucinações, dependências desnecessárias ou perda de discernimento).
3. **Nota Final Sugerida pela Skill:**
   $$\text{Nota Final IA} = \max(0.0, \text{Nota Base Ponderada} - \text{Penalidade IA})$$

**Direito a override:** O parecer técnico emitido pela IA é um insumo de apoio para os avaliadores humanos. A banca tem autonomia total para ajustar a nota no cálculo final caso constate particularidades ou soluções criativas não capturadas pelo modelo.
