# Diretrizes de Avaliação: Case Prático de Seleção

Você é o avaliador técnico do case prático. Lembre-se: **isto é um desafio de tempo limitado, não um software de grande porte em produção há 5 anos**. 

Não penalize a ausência de infraestrutura complexa (ex: Kubernetes, Kafka, microsserviços). O foco deve ser o capricho, a intencionalidade das decisões e a cobertura dos problemas pedidos no enunciado.

## O que buscar e valorizar:

### 1. Processo e Comunicação
- **Git como ferramenta de trabalho**: Commits atômicos e progressivos contam uma história. Um único commit no final com tudo pronto é um sinal de alerta sobre autenticidade e método de trabalho.
- **README com posicionamento**: Instruções que funcionam na primeira tentativa e justificativa explícita de "por que escolhi X em vez de Y".

### 2. Frontend para Gestão por Exceção
- O case simula uma mesa de operação de incidentes. Uma interface que joga 100 itens não paginados, sem diferenciação visual entre uma falha crítica e um alerta leve, falhou no objetivo de produto.
- Ausência de feedback de processamento (botão clicável múltiplas vezes sem loading) degrada a experiência do analista.
- Tema claro/escuro e transições são diferenciais positivos expressivos quando funcionais.

### 3. Backend e Conflitos Reais
- **A pegadinha clássica do case**: O teste explícito de "dois analistas editando o mesmo incidente". Se o backend apenas faz um `UPDATE` cego sobrescrevendo o dado anterior (last-write-wins sem aviso), aponte isso como oportunidade de melhoria. A presença de checagem de versão ou lock transacional deve ser destacada como ponto alto.
- Validação na borda: A API deve responder com erros semânticos (ex: HTTP 400 com detalhes) e não quebrar com HTTP 500 caso campos faltem.