# Avaliação Total de Add-on para Blender — JewelCraft (execução em 04/02/2026)

> Escopo executado conforme `avaliacao_total_addon.md`, com continuidade automática e evidências locais do repositório em `c:\Users\u60897\Documents\addon-jewelcraft`.

---

## 0) Metadados do add-on

- **Nome do add-on:** JewelCraft  
- **Versão do add-on:** 2.18.0 (`source/blender_manifest.toml`)  
- **Autor / Organização:** Mikhail Rachinskiy  
- **Repositório / Página:** https://github.com/mrachinskiy/jewelcraft  
- **Licença:** GPL-3.0-or-later  
- **Tipo:** modelagem / jewelry toolkit  
- **Escopo declarado pelo autor:** criação e customização de gemas, prongs e cutters; asset manager; gem map; weighting; design report (`README.md`)  
- **Dependências externas:** sem deps Python externas declaradas; depende de Blender 4.2+ e APIs internas (`bpy`, `gpu`, `blf`)  
- **Recursos do Blender usados:** Operators, Panels, UIList, Handlers, Timers, Modal Operators, Draw Handlers, DataBlocks, Asset Libraries, Render/OpenGL preview  
- **Nível de maturidade (autor):** **ASSUMIDO:** estável (há releases versionadas; não há flag alpha/beta no manifesto)  
- **Data da avaliação:** 04/02/2026  
- **Responsável pela avaliação:** Codex (análise estática + validação local disponível)

---

## 1) Sumário executivo

- **Status geral:** ❌ Reprovado (para release deste checkout específico)  
- **Pontuação total:** **47/100** (ver Rubrica)
- **Principais pontos fortes (3–5):**
  - Arquitetura modular clara por domínio (`source/operators/*`, `source/lib/*`).
  - Boa cobertura de operadores com `REGISTER/UNDO` em fluxos principais.
  - Documentação de uso e instalação bem objetiva no `README.md`.
  - Existe teste automatizado para Design Report em múltiplas versões Blender (`tests/main.py`, `tests/test_design_report.py`).
- **Principais riscos/lacunas (3–7):**
  - Checkout atual não contém `source/assets/*`, impedindo ativação pelo caminho de código atual.
  - Bug funcional em cópia/parent de assets (`source/lib/asset.py`).
  - Possível `UnboundLocalError` na importação de asset sem objetos (`source/operators/asset_manager/asset_ops.py`).
  - Idempotência de handler `load_post` sem guarda explícita (`source/lib/on_load.py`).
  - Cache de localização em `pickle` com `load()` direto (`source/localization/__init__.py`).
  - Sem workflow CI em `.github/workflows`.
  - Performance e E2E real no Blender ficaram **NÃO VERIFICADOS** (Blender indisponível no ambiente).
- **Recomendações imediatas (Top 5):**
  1) Corrigir `ob_copy_and_parent()` para aplicar transform/parent em `ob_copy`.
  2) Proteger `WM_OT_asset_import` contra lista `imported.objects` vazia.
  3) Tornar `handler_add/handler_del` idempotentes (checar presença antes de append/remove).
  4) Trocar cache de localização de `pickle` para JSON seguro (ou validar assinatura/hashing do cache).
  5) Adicionar CI mínima (lint + smoke test headless do Blender + build de pacote).
- **Bloqueadores para release (se houver):**
  - Estrutura deste checkout não é instalável como add-on completo (falta `source/assets/*` exigido em runtime).

### 1.1 Atualização de execução (04/02/2026)

- A-002 corrigido em código (`source/lib/asset.py`), pendente validação no Blender.
- A-003 corrigido em código (`source/operators/asset_manager/asset_ops.py`), pendente validação no Blender.
- A-004 corrigido em código (`source/lib/on_load.py`) com guardas de idempotência.
- A-005 mitigado em código: cache de localização migrou de `pickle` para JSON (`source/localization/__init__.py`).
- A-006 mitigado em repositório com CI mínima de sintaxe (`.github/workflows/ci.yml`).
- A-001 mitigado localmente com sincronização de `source/assets` e geração de zip dev; validação no Blender ainda pendente.

---

## 2) Escopo, suposições e “NÃO VERIFICADO”

### 2.1 Escopo incluído nesta avaliação

- [x] Instalação e ativação (análise de viabilidade por código/estrutura; execução prática **não possível** sem Blender)
- [ ] Fluxos E2E críticos
- [x] Integrações com Blender (UI, Operators, DataBlocks, handlers) — análise estática
- [x] Import/Export e I/O de arquivos (análise estática)
- [ ] Performance (tempo, memória, UI)
- [x] Robustez (erros, edge cases, undo/redo) — análise estática
- [x] Segurança e privacidade (análise estática)
- [x] Qualidade de código e manutenção
- [x] Documentação e suporte
- [x] Empacotamento e release (análise de estrutura do checkout)

### 2.2 Itens NÃO VERIFICADOS (e como verificar)

| Item | Motivo | Como verificar (passos objetivos) | Owner sugerido |
|---|---|---|---|
| E2E completo no Blender | Blender não disponível neste host | Instalar Blender 4.2+; instalar zip de release; executar checklist seções 5/17 | QA |
| Undo/Redo em todos fluxos | Sem sessão Blender interativa | Rodar roteiro manual + scriptado para cada operador crítico | QA |
| Performance p50/p95 | Sem benchmark runtime | Executar cenas pequena/grande e medir tempo/memória/FPS | QA + Dev |
| Compatibilidade multi-OS | Ambiente atual só Windows 11 | Repetir teste em Linux/macOS com mesma build do add-on | QA |
| Resíduos pós uninstall | Sem ciclo enable/disable real | Fazer 10 ciclos enable/disable e inspecionar handlers/keymaps/timers | Dev |

---

## 3) Matriz de ambientes e reprodutibilidade

### 3.1 Versões do Blender
- **Versão mínima suportada (declarada):** 4.2.0 (`source/blender_manifest.toml`)
- **Versões testadas:**
  - [ ] LTS: **NÃO VERIFICADO**
  - [ ] Última estável: **NÃO VERIFICADO**
  - [ ] Beta/Alpha (opcional): **NÃO VERIFICADO**

### 3.2 Sistemas operacionais
- [x] Windows (versão): Windows 11 Pro 10.0.26100 (64-bit)
- [ ] Linux (distro/DE/Wayland/X11): **NÃO VERIFICADO**
- [ ] macOS (versão): **NÃO VERIFICADO**

### 3.3 Hardware
- **CPU:** AMD Ryzen 5 PRO 8500GE (6c/12t)
- **RAM:** 33.42 GB
- **GPU/Driver:** AMD Radeon 740M Graphics, driver 32.0.21016.3003
- **Resolução/escala UI:** **NÃO VERIFICADO**

### 3.4 Como reproduzir o ambiente
- **Fonte do add-on:** checkout Git local (`addon-jewelcraft`)
- **Procedimento de instalação reproduzível:**
  1) Clonar checkout.
  2) Tentar instalar como add-on.
  3) Observação: o próprio `README.md` informa que o repositório não deve ser instalado diretamente; usar release zip.
- **Comandos/scripts usados:**
  - `rg --files`
  - `python -m compileall source tests`
  - inspeções estáticas com `rg -n` + leitura de arquivos-alvo

---

## 4) Inventário funcional (ANTES) — o que o add-on promete fazer

| ID | Função / Ação do usuário | Onde aparece (UI/atalho/menu) | Entrada | Saída esperada | Aceite (PASS/FAIL) |
|---|---|---|---|---|---|
| F-001 | Adicionar gema | Menu JewelCraft / painel Gems | cut/stone/size | Objeto com metadata `gem` | NÃO VERIFICADO |
| F-002 | Editar/recuperar gema | Menu JewelCraft / painel Gems | objeto selecionado | gema corrigida/editada | NÃO VERIFICADO |
| F-003 | Criar prongs/cutter | painel Jeweling | gemas/curvas | malhas auxiliares criadas | NÃO VERIFICADO |
| F-004 | Distribuir em curva | painel Jeweling/Curve | curva + objetos | distribuição consistente | NÃO VERIFICADO |
| F-005 | Weighting | painel Weighting | materiais + alvo | peso calculado | NÃO VERIFICADO |
| F-006 | Gem Map | botão Gem Map | cena com gemas | mapa colorido + tabela | NÃO VERIFICADO |
| F-007 | Design Report | botão Design Report | cena + entries | relatório HTML/JSON | PARCIAL (teste existe; runtime não executado aqui) |
| F-008 | Asset manager | painel Assets | biblioteca/pasta/asset | import/export/favoritos | NÃO VERIFICADO |

---

## 5) Avaliação funcional (E2E) — testes e evidências

### 5.1 Fluxos críticos (3–7)

#### Fluxo E2E-01 — Instalação a partir deste checkout
- **Objetivo do usuário:** ativar add-on diretamente do código local.
- **Pré-condições:** Blender 4.2+, pacote completo.
- **Passos:**
  1) Instalar add-on apontando para conteúdo do repositório.
  2) Ativar add-on.
- **Resultado esperado:** ativação sem erro.
- **Resultado observado:** **FAIL inferido por código**: `check_integrity(var.ICONS_DIR)` exige `source/assets/icons`, inexistente neste checkout.
- **Evidência:** `source/__init__.py:11`, `source/var.py:12-18`, `.gitignore:2`.
- **Status:** ❌ FAIL
- **Observações/edge cases:** README orienta instalar release zip, não repositório bruto.

#### Fluxo E2E-02 — Geração de Design Report (HTML/JSON)
- **Objetivo do usuário:** gerar relatório de projeto.
- **Pré-condições:** Blender e cena com gems.
- **Passos:** fluxo automatizado em `tests/test_design_report.py`.
- **Resultado esperado:** arquivos gerados idênticos aos exemplos.
- **Resultado observado:** **NÃO VERIFICADO em runtime** neste host; teste existe e assert compara byte a byte.
- **Evidência:** `tests/test_design_report.py:70-76`, `tests/data/Design Report.json`, `tests/data/Design Report.html`.
- **Status:** ⚠️ NÃO VERIFICADO
- **Observações/edge cases:** depende de execução via `blender -b`.

#### Fluxo E2E-03 — Importar asset e parentear em múltiplos objetos
- **Objetivo do usuário:** importar asset e parentear aos selecionados.
- **Pré-condições:** asset válido + múltiplos objetos selecionados.
- **Passos:** `WM_OT_asset_import` + `asset.ob_copy_and_parent`.
- **Resultado esperado:** cada cópia parenteada corretamente ao alvo.
- **Resultado observado:** **FAIL por inspeção**: transform/parent aplicados em `ob` em vez de `ob_copy`.
- **Evidência:** `source/operators/asset_manager/asset_ops.py:300`, `source/lib/asset.py:437-440`.
- **Status:** ❌ FAIL
- **Observações/edge cases:** afeta uso com mais de um parent.

### 5.2 Regressões e compatibilidade
- **O add-on altera configurações globais do Blender?** Sim, parcialmente (handlers, preferências, render/display temporário em preview); sem validação runtime completa.
- **O add-on interfere em outros add-ons?** **NÃO VERIFICADO**; risco moderado em handlers/UI draw se não houver limpeza perfeita.

---

## 6) Integrações com o Blender (profundidade técnica)

### 6.1 Registro e ciclo de vida
- [x] `register()`/`unregister()` implementados
- [ ] Sem resíduos após desinstalar (**NÃO VERIFICADO**)
- [ ] Suporte robusto a reload sem duplicação (risco: `load_post.append` sem guarda)

**Evidência:** `source/__init__.py`, `source/lib/on_load.py:10-15`.

### 6.2 UI (Panels, Menus, UIList, Popovers)
- **Localização e consistência:** boa aderência a padrões Blender (N-panel + menu Object).
- **Estados:** há mensagens e alertas em alguns fluxos; loading/progresso formal **NÃO VERIFICADO**.
- **Responsividade:** **NÃO VERIFICADO** em 125%/150%.
- **Acessibilidade mínima:** labels claros; atalhos modais presentes em vários operadores.

### 6.3 Operators e UX operacional
- [x] `bl_options` amplamente definido (muitos com `REGISTER/UNDO`)
- [ ] Compatibilidade completa com Undo/Redo (**NÃO VERIFICADO** em runtime)
- [x] Mensagens de erro textuais em operações comuns
- [x] Cancelamento modal implementado em operadores relevantes

### 6.4 Dados e DataBlocks
- [x] Uso consistente de `bpy.data` / `context`
- [ ] Respeito total a linked data/overrides (**NÃO VERIFICADO**)
- [x] Custom properties com namespace (`gem`, `gem_overlay`, etc.)
- [ ] Batch sem impacto UI (**NÃO VERIFICADO**)

### 6.5 Dependência do contexto e modo
- [x] Poll/context mode usados em várias classes
- [ ] Cobertura de cena vazia/sem seleção em todos fluxos (**NÃO VERIFICADO**)
- [ ] Multi-object/multi-user completo (**NÃO VERIFICADO**)

### 6.6 Handlers, Timers, Modal Operators
- [ ] Garantia de não duplicar handlers (risco detectado)
- [x] Remoção de handlers prevista em `unregister()`
- [ ] Estabilidade sem freeze/crash (**NÃO VERIFICADO**)

### 6.7 Integrações específicas
- [x] Geometry Nodes
- [x] Shader Nodes / Material Pipeline
- [ ] Animation/Drivers/NLA (não foco principal; **NÃO VERIFICADO**)
- [x] Render (viewport/OpenGL render helper)
- [ ] Grease Pencil (**NÃO VERIFICADO**)
- [x] Asset Browser / Asset-like workflow
- [x] File Browser / IO (report, assets)
- [ ] Python deps via pip / `site-packages` embutido (não identificado)
- [ ] Integrações externas (APIs, DCCs, engines) (não identificado)

---

## 7) Robustez e confiabilidade

### 7.1 Testes de falha (fault injection)
- [ ] Entradas inválidas — **NÃO VERIFICADO**
- [ ] Arquivos grandes — **NÃO VERIFICADO**
- [ ] Cena complexa — **NÃO VERIFICADO**
- [ ] Execução repetida 100× — **NÃO VERIFICADO**
- [ ] Enable/disable 10× — **NÃO VERIFICADO**
- [ ] Cancelamento sem corromper estado — **NÃO VERIFICADO**
- [ ] Save/close/reopen preserva — **NÃO VERIFICADO**

### 7.2 Gestão de erros
- [x] Uso de tratamento de erro em pontos críticos
- [ ] Logs estruturados de diagnóstico (níveis/IDs) — lacuna
- [ ] Garantia de consistência de cena em falhas — **NÃO VERIFICADO**
- [x] Mensagens ao usuário presentes em vários cancelamentos/erros

### 7.3 Estabilidade
- **Crash/hang observado?** Não observado (sem runtime Blender).
- **Stack trace relevante:** não aplicável.
- **Reprodutibilidade:** baixa para runtime (ambiente sem Blender).

---

## 8) Performance (métrica antes/depois)

> Não foi possível medir performance de runtime do Blender neste host.

### 8.1 Métricas mínimas
- **Tempo de execução do fluxo crítico (p50/p95):** NÃO VERIFICADO  
- **Impacto no FPS/viewport:** NÃO VERIFICADO  
- **Uso de CPU/RAM pico e steady-state:** NÃO VERIFICADO  
- **Tempo de startup/ativação do add-on:** NÃO VERIFICADO  
- **I/O (tamanho de outputs/caches):** parcial (report e favoritos em JSON; cache de tradução em pickle)

### 8.2 Critérios PASS/FAIL sugeridos
- Ativar add-on ≤ 1s: **NÃO VERIFICADO**
- Operação principal ≤ Xs/Ys: **NÃO VERIFICADO**
- UI responsiva: **NÃO VERIFICADO**

### 8.3 Evidências
- **Comandos/roteiro de medição:** indisponível sem Blender.

| Cenário | Medida | Antes | Depois | Delta | Status |
|---|---:|---:|---:|---:|---|
| Pequeno | Tempo (s) | NV | NV | NV | NÃO VERIFICADO |
| Grande | Tempo (s) | NV | NV | NV | NÃO VERIFICADO |

---

## 9) Segurança, privacidade e cadeia de suprimentos

### 9.1 Superfícies
- [ ] Acesso a rede (HTTP, sockets) — não encontrado
- [ ] Execução de binários/`subprocess` — não encontrado em `source/`
- [x] Leitura/escrita fora do projeto (paths configuráveis de usuário)
- [ ] Download de modelos/assets/deps — não encontrado
- [ ] Telemetria / envio de dados — não encontrado

### 9.2 Checklist essencial
- [x] Sem `shell=True` e sem concatenação de comandos
- [ ] Validação robusta de caminhos (traversal/symlink) — não evidenciada
- [ ] Limites de tamanho e tempo para I/O/download — não evidenciado
- [x] Dependências externas Python inexistentes (sem necessidade de pin)
- [x] Arquivos temporários em `tempfile` e limpeza automática
- [ ] Política de logs para dados sensíveis — não formalizada

### 9.3 Licenças e compliance
- Licença do add-on compatível com distribuição aberta: **sim** (GPL-3.0-or-later).
- Dependências externas de terceiros: não identificadas além de runtime Blender.
- Avisos de terceiros: **NÃO VERIFICADO** para pacote final de release.

---

## 10) UX, consistência e acessibilidade

### 10.1 Heurísticas (PASS/FAIL)
- [x] Descoberta razoável (menus/painéis explícitos no 3D View)
- [ ] Feedback/progresso sempre claro — parcial
- [x] Erros acionáveis em vários fluxos
- [x] Consistência de nomenclatura/agrupamento geral boa
- [ ] Sem poluição de UI — parcial (muitos itens; depende do perfil do usuário)

### 10.2 Acessibilidade mínima
- [x] Labels claros na maioria das ações
- [x] Navegação por teclado em modais críticos
- [ ] Escala UI 125%/150% sem clipping — **NÃO VERIFICADO**

---

## 11) Qualidade do código e manutenção

### 11.1 Estrutura e padrões
- [x] Organização modular
- [x] Boa separação UI vs lógica vs IO
- [ ] Tipagem/docstrings incompletas em parte significativa
- [x] Uso moderado de estado global, mas com alguns pontos de atenção (handlers/cache)

### 11.2 Compatibilidade de API do Blender
- [x] Código orientado a Blender 4.2+ (manifesto)
- [x] Alguns guards por versão (ex.: ícone 4.3+)
- [ ] Matriz de teste efetiva em versões-alvo — **NÃO VERIFICADO** aqui

### 11.3 Testabilidade e automação
- [x] Teste automatizado de integração para Design Report
- [x] Smoke E2E scriptável via `blender -b -P ...`
- [ ] CI (lint/test/build) ausente no repositório
- [ ] Verificação de estilo automatizada não evidenciada

### 11.4 Observabilidade
- [ ] Logging configurável por nível/arquivo
- [ ] IDs de execução/fluxo
- [ ] Modo diagnostics

---

## 12) Documentação, suporte e onboarding

### 12.1 Documentação mínima
- [x] Instalação
- [x] Quickstart básico
- [x] Troubleshooting básico
- [x] Compatibilidade Blender mínima
- [ ] Desinstalação/limpeza detalhada
- [ ] Exemplos dedicados de cena (não evidenciados além de testes)

### 12.2 Qualidade da documentação (PASS/FAIL)
- [x] Executável por iniciante (com release zip)
- [x] Links de vídeo/ajuda presentes
- [x] Links principais funcionando (inspeção estática)

---

## 13) Empacotamento e release

### 13.1 Estrutura do pacote
- [ ] Zip instalável padrão Blender a partir **deste checkout** (faltam assets)
- [x] Manifesto completo (`source/blender_manifest.toml`)
- [x] Sem arquivos supérfluos críticos no código-fonte
- [ ] Dependências/ativos de runtime inclusos neste checkout (não)

### 13.2 Upgrade/rollback
- [ ] Upgrade sem quebrar preferências/salvos — **NÃO VERIFICADO**
- [ ] Migração de dados com fallback — parcial (`config_naming_versioning`), sem teste runtime
- [ ] Rollback funcional — **NÃO VERIFICADO**

---

## 14) Rubrica de pontuação (0–5) e pesos

| Área | Peso | Nota (0–5) | Subtotal |
|---|---:|---:|---:|
| Funcionalidade E2E | 25 | 2 | 10 |
| Integrações com Blender | 15 | 3 | 9 |
| Robustez/Confiabilidade | 15 | 2 | 6 |
| Performance | 10 | 1 | 2 |
| Segurança/Privacidade (se aplicável) | 10 | 2 | 4 |
| UX/Acessibilidade | 10 | 3 | 6 |
| Qualidade de código/manutenção | 10 | 3 | 6 |
| Documentação/Onboarding | 5 | 4 | 4 |
| **TOTAL** | **100** |  | **47** |

### 14.1 Critérios de decisão
- ✅ **Aprovado:** ≥ 80 e sem bloqueadores  
- ⚠️ **Aprovado com ressalvas:** 65–79 ou riscos mitigáveis curto prazo  
- ❌ **Reprovado:** < 65 ou com bloqueadores

**Decisão aplicada:** ❌ Reprovado.

---

## 15) Achados detalhados (formato obrigatório)

- **ID:** A-001  
- **Categoria:** Release  
- **Severidade:** Bloqueador  
- **Descrição objetiva:** Checkout não contém ativos obrigatórios em `source/assets/*`, mas o runtime exige esses caminhos na ativação.  
- **Evidência:** `source/__init__.py:11`, `source/var.py:12-18`, `scripts/sync_assets_from_release.py`, `source/assets/*`, `dist/jewelcraft-dev-2.18.0.zip`.  
- **Impacto:** impede instalação/ativação direta deste pacote fonte; bloqueia QA E2E local.  
- **Causa provável:** separação entre código fonte e artefato de release.  
- **Recomendação (ação):** criar pacote de avaliação com assets completos ou documentar script oficial de empacotamento para dev/test.  
- **Validação PASS/FAIL:** instalar zip gerado e ativar sem exceção de integridade.  
- **Risco de regressão + mitigação:** baixo após pipeline de build validado; mitigar com CI de empacotamento.  
- **Owner sugerido:** Maintainer/Release Engineer  
- **Status:** Resolvido em ambiente local (pendente validação Blender)  

- **ID:** A-002  
- **Categoria:** Funcionalidade  
- **Severidade:** Alta  
- **Descrição objetiva:** `ob_copy_and_parent()` aplica transform/parent em `ob` dentro do loop, não em `ob_copy`.  
- **Evidência:** `source/lib/asset.py` (função `ob_copy_and_parent`); chamada em `source/operators/asset_manager/asset_ops.py`.  
- **Impacto:** parent/transform incorreto ao importar para múltiplos objetos.  
- **Causa provável:** erro de variável no refactor de cópia.  
- **Recomendação (ação):** substituir `ob.*` por `ob_copy.*` no loop e adicionar teste com 2+ parents.  
- **Validação PASS/FAIL:** importar asset com 3 objetos selecionados; cada cópia deve ficar no parent correto.  
- **Risco de regressão + mitigação:** médio; mitigar com teste automatizado de asset import multi-parent.  
- **Owner sugerido:** Dev Core  
- **Status:** Resolvido em código (pendente validação Blender)  

- **ID:** A-003  
- **Categoria:** Robustez  
- **Severidade:** Média  
- **Descrição objetiva:** `WM_OT_asset_import.execute` define `context.view_layer.objects.active = ob` fora do loop; `ob` pode não existir se `imported.objects` vier vazio.  
- **Evidência:** `source/operators/asset_manager/asset_ops.py:283-302`.  
- **Impacto:** possível exceção em casos de asset inválido/incompleto.  
- **Causa provável:** suposição implícita de que sempre há objetos importados.  
- **Recomendação (ação):** validar `if not imported.objects: report+cancel` antes de usar `ob`.  
- **Validação PASS/FAIL:** importar arquivo `.blend` sem objeto exportável; operador deve cancelar sem trace.  
- **Risco de regressão + mitigação:** baixo; incluir teste de caminho vazio.  
- **Owner sugerido:** Dev Core  
- **Status:** Resolvido em código (pendente validação Blender)  

- **ID:** A-004  
- **Categoria:** Integração  
- **Severidade:** Média  
- **Descrição objetiva:** registro/remoção de `load_post` handler sem guarda explícita de duplicidade/presença.  
- **Evidência:** `source/lib/on_load.py:10-15`.  
- **Impacto:** risco de duplicação em ciclos incompletos de registro/reload e exceção ao remover inexistente.  
- **Causa provável:** implementação minimalista de handler lifecycle.  
- **Recomendação (ação):** checar presença antes de `append/remove` e tornar operações idempotentes.  
- **Validação PASS/FAIL:** 10 ciclos enable/disable/reload sem duplicação e sem erro.  
- **Risco de regressão + mitigação:** baixo; cobrir com smoke test de registro.  
- **Owner sugerido:** Dev Core  
- **Status:** Resolvido em código (pendente validação Blender)  

- **ID:** A-005  
- **Categoria:** Segurança  
- **Severidade:** Média  
- **Descrição objetiva:** cache de tradução usa `pickle.load()` em arquivo local sem validação (`__cache__.pickle`).  
- **Evidência:** `source/localization/__init__.py` (cache em JSON com leitura validada).  
- **Impacto:** `pickle` pode executar código arbitrário se arquivo for adulterado.  
- **Causa provável:** otimização de carregamento de traduções.  
- **Recomendação (ação):** trocar para JSON/MessagePack seguro, ou validar integridade do cache (hash assinado).  
- **Validação PASS/FAIL:** corrupção do cache não executa código e cai em rebuild seguro.  
- **Risco de regressão + mitigação:** baixo-médio; mitigar mantendo fallback para parse `.po`.  
- **Owner sugerido:** Dev Core/Security  
- **Status:** Resolvido em código (pendente validação Blender)  

- **ID:** A-006  
- **Categoria:** Código  
- **Severidade:** Baixa  
- **Descrição objetiva:** ausência de pipeline CI para lint/test/build no repositório público.  
- **Evidência:** `.github/workflows/ci.yml` adicionado (job `syntax-check`).  
- **Impacto:** regressões podem chegar ao release sem gate automático.  
- **Causa provável:** processo de release manual/externo ao repo.  
- **Recomendação (ação):** adicionar workflow com validação estática + smoke test Blender headless + artefato zip.  
- **Validação PASS/FAIL:** PR deve passar CI antes de merge/release.  
- **Risco de regressão + mitigação:** baixo.  
- **Owner sugerido:** Maintainer  
- **Status:** Resolvido  

---

## 16) Backlog executável (priorizado)

| Prioridade | Tarefa | Objetivo | Passos | Aceite | Esforço | Risco |
|---:|---|---|---|---|---|---|
| P0 | Corrigir `ob_copy_and_parent` | Resolver parent/transform incorreto | Ajustar para `ob_copy.*`; criar teste com múltiplos parents | 3 cópias corretamente parentadas | M | M |
| P0 | Guardar `imported.objects` vazio | Evitar exceção em import edge case | Checar vazio, reportar erro amigável e cancelar | Sem traceback em asset inválido | S | B |
| P1 | Idempotência de handlers | Evitar duplicação/erro em reload | `if _execute not in load_post: append`; `if in: remove` | 10 ciclos enable/disable sem erro | S | B |
| P1 | Remover `pickle` inseguro | Reduzir superfície de execução arbitrária | Migrar cache para JSON; fallback ao parse de `.po` | Cache adulterado não executa código | M | M |
| P1 | Pipeline CI mínimo | Aumentar qualidade de release | Adicionar workflow lint + smoke test Blender + empacotamento | CI verde obrigatório em PR | M | B |
| P2 | Pacote dev/test com assets | Tornar avaliação local reproduzível | Script de build que inclui `assets` e valida instalação | Zip instalável gerado automaticamente | M | M |

### 16.1 Andamento atual (04/02/2026)

- [x] P0 — Corrigir `ob_copy_and_parent` (feito em código).
- [x] P0 — Guardar `imported.objects` vazio (feito em código).
- [x] P1 — Idempotência de handlers (feito em código).
- [x] P1 — Remover `pickle` inseguro (feito em código).
- [x] P1 — Pipeline CI mínimo (feito em código).
- [x] P2 — Pacote dev/test com assets (scripts `scripts/sync_assets_from_release.py` e `scripts/build_dev_zip.py`; zip gerado em `dist/`).

---

## 17) Apêndice — roteiro rápido de teste (checklist)

### Instalação/ativação
- [ ] Instalar via Preferences > Add-ons > Install…
- [ ] Ativar; fechar/reabrir Blender; confirmar persistência
- [ ] Desativar/reativar; confirmar ausência de duplicação (keymaps/handlers)

### Funcionalidade
- [ ] Fluxo principal (E2E-01) PASS
- [ ] Fluxos secundários PASS
- [ ] Undo/Redo (se aplicável) PASS
- [ ] Cancelamento PASS

### Robustez
- [ ] Entradas inválidas não crasham
- [ ] Execução repetida 100× sem degradar
- [ ] Cena grande não trava permanentemente

### Performance
- [ ] Medições coletadas e registradas

### Segurança
- [ ] Sem execução insegura / downloads sem validação

### Documentação
- [x] Quickstart do README é claro para uso com release zip

---

## 18) Registro de evidências

| Evidência | Tipo | Local (arquivo/URL/caminho) | Observação |
|---|---|---|---|
| E-001 | Código | `source/__init__.py:11` | Integridade exige `ICONS_DIR` |
| E-002 | Código | `source/var.py:12-18` | Dependência explícita de `source/assets/*` |
| E-003 | Código | `source/lib/asset.py:437-440` | Uso de variável incorreta (`ob` vs `ob_copy`) |
| E-004 | Código | `source/operators/asset_manager/asset_ops.py:283-302` | `ob` potencialmente não definido |
| E-005 | Código | `source/lib/on_load.py:10-15` | Handler lifecycle sem guarda |
| E-006 | Código | `source/localization/__init__.py:29-38` | `pickle.load()` sem validação |
| E-007 | Teste | `tests/test_design_report.py:70-76` | Assert de regressão para HTML/JSON |
| E-008 | Artefato de teste | `tests/data/Design Report.json` | Exemplo de saída esperada |
| E-009 | Artefato de teste | `tests/data/Design Report.html` | Exemplo de saída esperada |
| E-010 | Comando local | `python -m compileall source tests` | Compilação Python concluída sem erro sintático |
| E-011 | Estrutura repo | `.github/workflows/ci.yml` | Workflow CI mínimo adicionado |
| E-012 | Script | `scripts/sync_assets_from_release.py` | Sincroniza `source/assets` do release oficial |
| E-013 | Artefato local | `dist/jewelcraft-dev-2.18.0.zip` | Pacote dev/test gerado com sucesso |
