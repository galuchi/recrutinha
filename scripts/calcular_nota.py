#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculadora de Nota Final - Processo Seletivo (Case Prático & Apresentação)
Algoritmo 100% manual via terminal para cálculo e consolidação de notas segundo criterios.md.
"""

import sys
import os

# Garante saída UTF-8 no terminal Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stdin.reconfigure(encoding="utf-8")
    except Exception:
        pass


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def ler_nota(prompt: str, detalhe: str = "") -> float:
    """Lê uma nota float entre 0.0 e 10.0 com validação e suporte a vírgula."""
    if detalhe:
        print(f"   \033[90m↳ {detalhe}\033[0m")
    while True:
        try:
            raw = input(f"   {prompt}: ").strip().lstrip('\ufeff')
            # Substitui vírgula por ponto para aceitar formato brasileiro
            raw_normalizado = raw.replace(",", ".")
            valor = float(raw_normalizado)
            if 0.0 <= valor <= 10.0:
                print()  # Respiro visual após preenchimento
                return round(valor, 2)
            print("   \033[91m[!] Erro: A nota deve estar entre 0.0 e 10.0. Tente novamente.\033[0m")
        except ValueError:
            print("   \033[91m[!] Erro: Digite um número válido (ex: 8.5 ou 8,5).\033[0m")
        except (KeyboardInterrupt, EOFError):
            print("\n")
            sys.exit(0)


def cabecalho(titulo: str):
    print("\n" + "=" * 72)
    print(f" {titulo.center(70)} ")
    print("=" * 72 + "\n")


def subcabecalho(titulo: str):
    print("\n" + "-" * 72)
    print(f" >> {titulo}")
    print("-" * 72)


def exibir_tabela_resumo(dados: dict):
    linhas = []
    linhas.append("=" * 72)
    linhas.append(f"{'QUADRO GERAL DE CONSOLIDAÇÃO DE NOTAS':^72}")
    linhas.append("=" * 72)
    linhas.append(f"{'Critério / Pilar / Subcritério':<42} | {'Nota':>6} | {'Peso':>6} | {'Pond.':>7}")
    linhas.append("-" * 72)

    # 1. Apresentação
    linhas.append(f"\033[1m1. APRESENTAÇÃO (PITCH / VÍDEO)\033[0m (Peso Final: 40%)")
    linhas.append(f"  - Manifestação                          | {dados['apr_manifestacao']:>6.2f} |  40%  | {dados['apr_manifestacao']*0.4:>7.2f}")
    linhas.append(f"  - Fluidez                               | {dados['apr_fluidez']:>6.2f} |  30%  | {dados['apr_fluidez']*0.3:>7.2f}")
    linhas.append(f"  - Convencimento                         | {dados['apr_convencimento']:>6.2f} |  20%  | {dados['apr_convencimento']*0.2:>7.2f}")
    linhas.append(f"  - Qualidade do Vídeo                    | {dados['apr_qualidade']:>6.2f} |  10%  | {dados['apr_qualidade']*0.1:>7.2f}")
    linhas.append(f"  \033[96m* NOTA DO PILAR APRESENTAÇÃO\033[0m            | \033[96m{dados['nota_apresentacao']:>6.2f}\033[0m | \033[96m 0.40 \033[0m | \033[96m{dados['pond_apresentacao']:>7.2f}\033[0m")
    linhas.append("-" * 72)

    # 2. Avaliação Técnica
    linhas.append(f"\033[1m2. AVALIAÇÃO TÉCNICA\033[0m (Peso Final: 60%)")
    
    # 2.1 Arquitetura
    linhas.append(f"  \033[93m2.1 Arquitetura e Práticas\033[0m (Peso Técnico: 20%)")
    linhas.append(f"    - Documentação (README)               | {dados['arq_doc']:>6.2f} |  30%  | {dados['arq_doc']*0.30:>7.2f}")
    linhas.append(f"    - Histórico Git                       | {dados['arq_git']:>6.2f} |  25%  | {dados['arq_git']*0.25:>7.2f}")
    linhas.append(f"    - Organização e Modularização         | {dados['arq_org']:>6.2f} |  25%  | {dados['arq_org']*0.25:>7.2f}")
    linhas.append(f"    - Clareza e Nomenclatura              | {dados['arq_clareza']:>6.2f} |  20%  | {dados['arq_clareza']*0.20:>7.2f}")
    linhas.append(f"    Subtotal Arquitetura                  | {dados['nota_arquitetura']:>6.2f} |  0.20 | {dados['nota_arquitetura']*0.2:>7.2f}")
    
    # 2.2 Frontend
    linhas.append(f"  \033[93m2.2 Frontend e UX\033[0m (Peso Técnico: 30%)")
    linhas.append(f"    - Design da Informação                | {dados['front_design']:>6.2f} |  35%  | {dados['front_design']*0.35:>7.2f}")
    linhas.append(f"    - Feedback Visual                     | {dados['front_feedback']:>6.2f} |  30%  | {dados['front_feedback']*0.30:>7.2f}")
    linhas.append(f"    - Atenção aos Detalhes                | {dados['front_detalhes']:>6.2f} |  20%  | {dados['front_detalhes']*0.20:>7.2f}")
    linhas.append(f"    - Diferenciais de Usabilidade         | {dados['front_diferenciais']:>6.2f} |  15%  | {dados['front_diferenciais']*0.15:>7.2f}")
    linhas.append(f"    Subtotal Frontend                     | {dados['nota_frontend']:>6.2f} |  0.30 | {dados['nota_frontend']*0.3:>7.2f}")

    # 2.3 Backend
    linhas.append(f"  \033[93m2.3 Backend e Resiliência\033[0m (Peso Técnico: 30%)")
    linhas.append(f"    - Integridade e Concorrência          | {dados['back_concorrencia']:>6.2f} |  40%  | {dados['back_concorrencia']*0.40:>7.2f}")
    linhas.append(f"    - Robustez e Validação                | {dados['back_validacao']:>6.2f} |  35%  | {dados['back_validacao']*0.35:>7.2f}")
    linhas.append(f"    - Tratamento de Exceções              | {dados['back_excecoes']:>6.2f} |  25%  | {dados['back_excecoes']*0.25:>7.2f}")
    linhas.append(f"    Subtotal Backend                      | {dados['nota_backend']:>6.2f} |  0.30 | {dados['nota_backend']*0.3:>7.2f}")

    # 2.4 Auditoria IA
    linhas.append(f"  \033[93m2.4 Auditoria Técnica (IA)\033[0m (Peso Técnico: 20%)")
    linhas.append(f"    - Nota Direta da Auditoria            | {dados['nota_ia']:>6.2f} |  0.20 | {dados['nota_ia']*0.2:>7.2f}")
    
    linhas.append(f"  \033[96m* NOTA DO PILAR TÉCNICO\033[0m                 | \033[96m{dados['nota_tecnica']:>6.2f}\033[0m | \033[96m 0.60 \033[0m | \033[96m{dados['pond_tecnica']:>7.2f}\033[0m")
    linhas.append("=" * 72)
    texto_final = f">>> NOTA FINAL CONSOLIDADA: {dados['nota_final']:.2f} / 10.00"
    linhas.append(f"\033[1;92m{texto_final:^72}\033[0m")
    linhas.append("=" * 72)

    print("\n".join(linhas))


def executar_calculo():
    cabecalho("CALCULADORA DE NOTA FINAL - CASE PRÁTICO")
    print("Insira as notas de 0.0 a 10.0 para cada critério e subcritério.\n")

    # ==========================================
    # 1. BLOCO DE APRESENTAÇÃO (Peso 0.4)
    # ==========================================
    subcabecalho("1. APRESENTAÇÃO (PITCH / VÍDEO) [Peso na Nota Final: 40% (0.4)]")

    apr_manifestacao = ler_nota(
        "Manifestação [Peso 40% (0.4)]",
        "Autenticidade, clareza verbal, câmera ligada e postura."
    )
    apr_fluidez = ler_nota(
        "Fluidez [Peso 30% (0.3)]",
        "Ritmo, concatenação lógica de ideias (início, meio e fim)."
    )
    apr_convencimento = ler_nota(
        "Convencimento [Peso 20% (0.2)]",
        "Defesa de escolhas, confiança e demonstração de valor da solução."
    )
    apr_qualidade = ler_nota(
        "Qualidade do Vídeo [Peso 10% (0.1)]",
        "Áudio compreensível, boa iluminação e nitidez da tela."
    )

    nota_apresentacao = (
        (apr_manifestacao * 0.4) +
        (apr_fluidez * 0.3) +
        (apr_convencimento * 0.2) +
        (apr_qualidade * 0.1)
    )
    print(f"   \033[92m=> Subtotal Apresentação: {nota_apresentacao:.2f} / 10.00\033[0m")

    # ==========================================
    # 2. BLOCO TÉCNICO (Peso 0.6)
    # ==========================================
    subcabecalho("2. AVALIAÇÃO TÉCNICA [Peso na Nota Final: 60% (0.6)]")

    # 2.1 Arquitetura e Práticas (Peso 0.2 no técnico)
    print("\n [2.1] Arquitetura, Qualidade e Boas Práticas (Peso: 20% do bloco técnico)")
    arq_doc = ler_nota(
        "Documentação README [Peso 30% (0.30)]",
        "Instruções reproduzíveis de execução e justificativas de arquitetura."
    )
    arq_git = ler_nota(
        "Histórico Git [Peso 25% (0.25)]",
        "Commits atômicos, progressivos e mensagens explicativas."
    )
    arq_org = ler_nota(
        "Organização e Modularização [Peso 25% (0.25)]",
        "Separação de pastas/responsabilidades; ausência de arquivos monolíticos."
    )
    arq_clareza = ler_nota(
        "Clareza e Nomenclatura [Peso 20% (0.20)]",
        "Nomes expressivos, legibilidade e ausência de gambiarras."
    )

    nota_arquitetura = (
        (arq_doc * 0.30) +
        (arq_git * 0.25) +
        (arq_org * 0.25) +
        (arq_clareza * 0.20)
    )
    print(f"   \033[92m=> Subtotal Arquitetura: {nota_arquitetura:.2f} / 10.00\033[0m")

    # 2.2 Frontend e UX (Peso 0.3 no técnico)
    print("\n [2.2] Frontend, UX e Design (Peso: 30% do bloco técnico)")
    front_design = ler_nota(
        "Design da Informação [Peso 35% (0.35)]",
        "Escaneabilidade de ~100 incidentes simultâneos e hierarquia por severidade."
    )
    front_feedback = ler_nota(
        "Feedback Visual [Peso 30% (0.30)]",
        "Loadings/skeletons, bloqueio contra duplo clique e mensagens de erro."
    )
    front_detalhes = ler_nota(
        "Atenção aos Detalhes [Peso 20% (0.20)]",
        "Alinhamentos, espaçamentos padronizados, tipografia e contraste."
    )
    front_diferenciais = ler_nota(
        "Diferenciais de Usabilidade [Peso 15% (0.15)]",
        "Modo escuro (Dark Mode) funcional, transições e microinterações fluidas."
    )

    nota_frontend = (
        (front_design * 0.35) +
        (front_feedback * 0.30) +
        (front_detalhes * 0.20) +
        (front_diferenciais * 0.15)
    )
    print(f"   \033[92m=> Subtotal Frontend: {nota_frontend:.2f} / 10.00\033[0m")

    # 2.3 Backend e Resiliência (Peso 0.3 no técnico)
    print("\n [2.3] Backend, Lógica e Resiliência (Peso: 30% do bloco técnico)")
    back_concorrencia = ler_nota(
        "Integridade e Concorrência [Peso 40% (0.40)]",
        "Tratamento intencional de conflito/lock na edição simultânea do mesmo recurso."
    )
    back_validacao = ler_nota(
        "Robustez e Validação [Peso 35% (0.35)]",
        "Validação de payloads na borda, erros HTTP semânticos (ex: 400 em vez de 500)."
    )
    back_excecoes = ler_nota(
        "Tratamento de Exceções [Peso 25% (0.25)]",
        "Resiliência a quedas de banco/rede, try/catch e logs defensivos."
    )

    nota_backend = (
        (back_concorrencia * 0.40) +
        (back_validacao * 0.35) +
        (back_excecoes * 0.25)
    )
    print(f"   \033[92m=> Subtotal Backend: {nota_backend:.2f} / 10.00\033[0m")

    # 2.4 Auditoria Técnica da IA (Peso 0.2 no técnico)
    print("\n [2.4] Auditoria Técnica por IA (Peso: 20% do bloco técnico)")
    nota_ia = ler_nota(
        "Nota Direta da Auditoria de IA [0.0 a 10.0]",
        "Nota atribuída para a auditoria de código / IA (conforme criterios.md)."
    )

    # Consolidação Técnica
    nota_tecnica = (
        (nota_arquitetura * 0.2) +
        (nota_frontend * 0.3) +
        (nota_backend * 0.3) +
        (nota_ia * 0.2)
    )
    print(f"   \033[92m=> Subtotal Técnico: {nota_tecnica:.2f} / 10.00\033[0m")

    # ==========================================
    # 3. NOTA FINAL CONSOLIDADA
    # ==========================================
    pond_apresentacao = nota_apresentacao * 0.4
    pond_tecnica = nota_tecnica * 0.6
    nota_final = pond_apresentacao + pond_tecnica

    dados = {
        "apr_manifestacao": apr_manifestacao,
        "apr_fluidez": apr_fluidez,
        "apr_convencimento": apr_convencimento,
        "apr_qualidade": apr_qualidade,
        "nota_apresentacao": nota_apresentacao,
        "pond_apresentacao": pond_apresentacao,
        "arq_doc": arq_doc,
        "arq_git": arq_git,
        "arq_org": arq_org,
        "arq_clareza": arq_clareza,
        "nota_arquitetura": nota_arquitetura,
        "front_design": front_design,
        "front_feedback": front_feedback,
        "front_detalhes": front_detalhes,
        "front_diferenciais": front_diferenciais,
        "nota_frontend": nota_frontend,
        "back_concorrencia": back_concorrencia,
        "back_validacao": back_validacao,
        "back_excecoes": back_excecoes,
        "nota_backend": nota_backend,
        "nota_ia": nota_ia,
        "nota_tecnica": nota_tecnica,
        "pond_tecnica": pond_tecnica,
        "nota_final": nota_final,
    }

    print("\n")
    exibir_tabela_resumo(dados)


def main():
    while True:
        try:
            executar_calculo()
        except (KeyboardInterrupt, EOFError):
            print("\n\nCálculo cancelado. Encerrando...")
            break

        try:
            repetir = input("\nDeseja realizar outro cálculo? (s/N): ").strip().lower()
        except (KeyboardInterrupt, EOFError):
            print()
            break
        if repetir not in ["s", "sim", "y", "yes"]:
            print("\nEncerrando a calculadora. Até logo!\n")
            break


if __name__ == "__main__":
    main()
