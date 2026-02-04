# Avaliação Total de Add-on para Blender (Template Executável)

> **Objetivo:** avaliar um add-on do Blender de ponta a ponta — funcionalidade, integrações, robustez, performance, segurança, UX, qualidade de código e prontidão de release — com critérios **claros**, **mensuráveis** e **auditáveis**.

---

## Modo de execução do agente (fluxo contínuo, sem interrupções)

> **Diretriz:** o agente deve **prosseguir automaticamente** por todas as seções deste template, executando o planejamento completo **sem solicitar autorização a cada etapa**. Perguntas ao usuário só devem ocorrer nos casos definidos abaixo.

### Regras de autonomia
- **Execução sequencial:** seguir as seções **0 → 18** em ordem, preenchendo o que for possível com as evidências disponíveis.
- **Sem “pedir permissão” por padrão:** não solicitar confirmação para avançar entre etapas (ex.: “posso ir para a seção 6?”).
- **Assunções explícitas:** quando um dado estiver ausente, registrar como **ASSUMIDO** ou **NÃO VERIFICADO**, com impacto e como verificar (Seção 2.2).
- **Evidência primeiro:** toda conclusão relevante deve apontar para evidências (prints, logs, arquivos, passos reproduzíveis).
- **Fechamento obrigatório:** ao final, sempre preencher o **Sumário executivo** (Seção 1), **Rubrica** (Seção 14) e gerar **Backlog executável** (Seção 16).

### Quando o agente DEVE perguntar ao usuário (gatilhos objetivos)
Perguntar apenas se faltar informação indispensável para prosseguir ou se houver risco de impacto relevante:

1) **Dados mínimos ausentes para iniciar**: link do repositório/zip, versão do Blender alvo, sistema operacional alvo, ou passos de instalação (Seções 0 e 3).  
2) **Ações potencialmente destrutivas/irreversíveis**: remover dados, sobrescrever arquivos do usuário, alterar preferências globais do Blender fora de um ambiente isolado.  
3) **Ambiguidade que altera o objetivo**: múltiplas interpretações do escopo/função do add-on, ou critérios de aceite conflitantes (Seção 4).  
4) **Risco de segurança/privacidade**: suspeita de rede/telemetria/execução de binários que exija decisão do usuário (Seção 9).  
5) **Dependências pagas/licenças**: necessidade de credenciais, chaves, ou termos que o usuário precise aceitar (Seção 9.3 / 13).

### Padrão de comunicação durante a execução
- **Atualizações por marcos (checkpoints):** reportar progresso apenas ao concluir blocos (ex.: após Seções 0–3, depois 4–6, depois 7–10, etc.).
- **Perguntas em lote:** quando necessário, consolidar dúvidas em **uma única lista**, evitando ping-pong.
- **Saídas padronizadas:** registrar achados em “Achados detalhados” (Seção 15) e ações no “Backlog executável” (Seção 16).

---

## 0) Metadados do add-on

- **Nome do add-on:**  
- **Versão do add-on:**  
- **Autor / Organização:**  
- **Repositório / Página:**  
- **Licença:**  
- **Tipo:** (Ex.: modelagem, shading, animação, pipeline, IO, utilitário, UI)  
- **Escopo declarado pelo autor:** (1–3 frases)  
- **Dependências externas:** (pip, binários, serviços, GPUs, libs)  
- **Recursos do Blender usados:** (Operators, Panels, Keymaps, Handlers, Nodes, IO, etc.)  
- **Nível de maturidade (autor):** alpha / beta / estável  
- **Data da avaliação:**  
- **Responsável pela avaliação:**  

---

## 1) Sumário executivo (preencher ao final)

- **Status geral:** ✅ Aprovado / ⚠️ Aprovado com ressalvas / ❌ Reprovado  
- **Pontuação total:** _X_/100 (ver Rubrica)  
- **Principais pontos fortes (3–5):**
  -  
- **Principais riscos/lacunas (3–7):**
  -  
- **Recomendações imediatas (Top 5):**
  1)  
- **Bloqueadores para release (se houver):**
  -  

---

## 2) Escopo, suposições e “NÃO VERIFICADO”

### 2.1 Escopo incluído nesta avaliação
Marcar o que foi efetivamente testado:

- [ ] Instalação e ativação
- [ ] Fluxos E2E críticos
- [ ] Integrações com Blender (UI, Operators, DataBlocks, handlers)
- [ ] Import/Export e I/O de arquivos (se aplicável)
- [ ] Performance (tempo, memória, UI)
- [ ] Robustez (erros, edge cases, undo/redo)
- [ ] Segurança e privacidade (se aplicável)
- [ ] Qualidade de código e manutenção
- [ ] Documentação e suporte
- [ ] Empacotamento e release

### 2.2 Itens NÃO VERIFICADOS (e como verificar)
| Item | Motivo | Como verificar (passos objetivos) | Owner sugerido |
|---|---|---|---|
|  |  |  |  |

---

## 3) Matriz de ambientes e reprodutibilidade

### 3.1 Versões do Blender
- **Versão mínima suportada (declarada):**  
- **Versões testadas:**  
  - [ ] LTS:  
  - [ ] Última estável:  
  - [ ] Beta/Alpha (opcional):  

### 3.2 Sistemas operacionais
- [ ] Windows (versão):  
- [ ] Linux (distro/DE/Wayland/X11):  
- [ ] macOS (versão):  

### 3.3 Hardware
- **CPU:**  
- **RAM:**  
- **GPU/Driver:**  
- **Resolução/escala UI:** (100% / 125% / 150%)  

### 3.4 Como reproduzir o ambiente
- **Fonte do add-on:** (zip, git, marketplace)  
- **Procedimento de instalação reproduzível:** (passo a passo)  
- **Comandos/scripts usados:**  

---

## 4) Inventário funcional (ANTES) — o que o add-on “promete fazer”

> **Regra:** liste funcionalidades por **ações do usuário** (não por módulos internos). Cada item precisa de um **critério de aceite**.

| ID | Função / Ação do usuário | Onde aparece (UI/atalho/menu) | Entrada | Saída esperada | Aceite (PASS/FAIL) |
|---|---|---|---|---|---|
| F-001 |  |  |  |  |  |
| F-002 |  |  |  |  |  |

---

## 5) Avaliação funcional (E2E) — testes e evidências

### 5.1 Fluxos críticos (3–7)
Descrever passo a passo, com resultados e evidências (prints, arquivos, logs).

#### Fluxo E2E-01 — (nome)
- **Objetivo do usuário:**  
- **Pré-condições:**  
- **Passos:**
  1)  
- **Resultado esperado:**  
- **Resultado observado:**  
- **Evidência:** (screenshot/caminho do arquivo/log)  
- **Status:** ✅ PASS / ❌ FAIL  
- **Observações/edge cases:**  

(Replicar para E2E-02…E2E-07)

### 5.2 Regressões e compatibilidade
- **O add-on altera configurações globais do Blender?** (preferências, keymaps, tema)  
- **O add-on interfere em outros add-ons?** (conflitos de keymap, nomes, handlers)  

---

## 6) Integrações com o Blender (profundidade técnica)

### 6.1 Registro e ciclo de vida
- [ ] `register()`/`unregister()` corretos e idempotentes  
- [ ] Sem resíduos após desinstalar (classes, keymaps, handlers, timers)  
- [ ] Suporte a “Reload Scripts” / recarregar add-ons sem duplicar registro  

**Evidência:** logs/inspeção do Blender / testes repetidos de enable/disable.

### 6.2 UI (Panels, Menus, UIList, Popovers)
- **Localização e consistência:** segue padrões do Blender (N-panel, Properties, Topbar)  
- **Estados:** loading/empty/error; feedback de progresso; cancelamento  
- **Responsividade:** sem overflow/clipping com escalas 125%/150%  
- **Acessibilidade mínima:** labels claros; foco/atalhos quando aplicável  

### 6.3 Operators e UX operacional
- [ ] `bl_options` adequado (`REGISTER`, `UNDO`, `BLOCKING`, etc.)  
- [ ] Compatibilidade com Undo/Redo (quando aplicável)  
- [ ] Mensagens de erro legíveis (sem stack trace para usuário final)  
- [ ] Cancelamento funciona (Esc/Right Click, quando aplicável)  

### 6.4 Dados e DataBlocks
- [ ] Uso correto de `bpy.data` / `context`  
- [ ] Evita corromper cenas/arquivos; respeita linked data e overrides  
- [ ] Custom properties com namespace e migração/compatibilidade  
- [ ] Operações em batch: não travam UI; usam `depsgraph` quando necessário  

### 6.5 Dependência do contexto e modo
- [ ] Funciona em Object/Edit/Sculpt/etc. conforme prometido  
- [ ] Não falha em ausência de seleção, cena vazia, coleções linkadas  
- [ ] Tratamento de multi-object e multi-user data  

### 6.6 Handlers, Timers, Modal Operators
- [ ] Não cria loops infinitos/CPU alta  
- [ ] Remove handlers no `unregister()`  
- [ ] Não degrada estabilidade do Blender (crashes, freeze)  

### 6.7 Integrações específicas (marcar se aplicável)
- [ ] Geometry Nodes  
- [ ] Shader Nodes / Material Pipeline  
- [ ] Animation/Drivers/NLA  
- [ ] Render (Cycles/Eevee), Compositor  
- [ ] Grease Pencil  
- [ ] Asset Browser  
- [ ] File Browser / IO (import/export)  
- [ ] Python deps via pip / `site-packages` embutido  
- [ ] Integrações externas (APIs, DCCs, engines)  

---

## 7) Robustez e confiabilidade

### 7.1 Testes de falha (fault injection) — mínimo recomendado
- [ ] Entradas inválidas (paths vazios, objetos inexistentes, formatos errados)
- [ ] Arquivos grandes (se aplicável)
- [ ] Cena complexa (muitos objetos, modifiers, drivers)
- [ ] Execução repetida (100×) sem leak/degeneração
- [ ] Enable/disable repetido (10×) sem duplicar recursos
- [ ] Interromper operação (cancelar) sem corromper estado
- [ ] “Salvar, fechar Blender, reabrir” preserva resultados

### 7.2 Gestão de erros
- [ ] Erros tratados com `try/except` **estratégico** (sem engolir exceptions)
- [ ] Logs úteis para diagnóstico (níveis, contexto, IDs)
- [ ] Falhas não deixam cena em estado inconsistente
- [ ] Mensagens ao usuário: ação recomendada (“como resolver”)

### 7.3 Estabilidade
- **Crash/hang observado?** (detalhar)  
- **Stack trace relevante:** (anexar)  
- **Reprodutibilidade:** alta/média/baixa  

---

## 8) Performance (métrica antes/depois)

> **Regra:** medir ao menos em um cenário “pequeno” e um “grande”.

### 8.1 Métricas mínimas
- **Tempo de execução do fluxo crítico (p50/p95):**  
- **Impacto no FPS/viewport:**  
- **Uso de CPU/RAM pico e steady-state:**  
- **Tempo de startup/ativação do add-on:**  
- **I/O (tamanho de outputs/caches):**  

### 8.2 Critérios PASS/FAIL sugeridos (ajustáveis)
- Ativar add-on: **≤ 1s** em máquina alvo (ou justificar)  
- Operação principal: **≤ Xs** para cena pequena / **≤ Ys** para cena grande  
- UI responsiva (sem travar > 250 ms em interações comuns)  

### 8.3 Evidências
- Comandos/roteiro de medição:  
- Resultados (tabela):  

| Cenário | Medida | Antes | Depois | Delta | Status |
|---|---:|---:|---:|---:|---|
| Pequeno | Tempo (s) |  |  |  |  |
| Grande | Tempo (s) |  |  |  |  |

---

## 9) Segurança, privacidade e cadeia de suprimentos (quando aplicável)

### 9.1 Superfícies
- [ ] Acesso a rede (HTTP, sockets)  
- [ ] Execução de binários/`subprocess`  
- [ ] Leitura/escrita fora do projeto (paths arbitrários)  
- [ ] Download de modelos/assets/deps  
- [ ] Telemetria / envio de dados  

### 9.2 Checklist essencial
- [ ] Sem `shell=True` e sem concatenação de comandos  
- [ ] Validação de caminhos (bloquear traversal, symlinks suspeitos quando necessário)  
- [ ] Limites de tamanho e tempo para I/O e downloads  
- [ ] Dependências “pinned” (versões fixas/lockfile)  
- [ ] Arquivos temporários em diretório seguro; limpeza  
- [ ] Política de logs sem dados sensíveis  

### 9.3 Licenças e compliance
- Licença do add-on é compatível com distribuição pretendida?  
- Dependências têm licenças compatíveis?  
- Existe aviso de uso de terceiros?  

---

## 10) UX, consistência e acessibilidade (prático e objetivo)

### 10.1 Heurísticas (PASS/FAIL)
- [ ] Descoberta: usuário encontra a função em ≤ 10s sem ler manual  
- [ ] Feedback: progresso/estado sempre claro  
- [ ] Erros: texto acionável (“faça X para resolver”)  
- [ ] Consistência: nomes, ícones, agrupamento e linguagem alinhados ao Blender  
- [ ] Sem “poluição” de UI: painéis/menus só onde necessário  

### 10.2 Acessibilidade mínima (quando aplicável)
- [ ] Labels claros e não ambíguos  
- [ ] Navegação por teclado onde fizer sentido  
- [ ] Suporte a escala UI 125%/150% sem clipping  

---

## 11) Qualidade do código e manutenção

### 11.1 Estrutura e padrões
- [ ] Organização modular (evitar “arquivo monolítico”)  
- [ ] Separação UI vs lógica vs IO  
- [ ] Tipagem/documentação interna (docstrings)  
- [ ] Evita estados globais perigosos; uso cuidadoso de singletons  

### 11.2 Compatibilidade de API do Blender
- [ ] Sem uso de API depreciada sem fallback  
- [ ] Tratamento de diferenças entre versões (guards)  
- [ ] Teste em versões-alvo (matriz)  

### 11.3 Testabilidade e automação
- [ ] Testes automatizados (unit/integration)  
- [ ] Smoke E2E scriptável (ex.: `blender -b -P script.py`)  
- [ ] CI (lint, testes, build do zip)  
- [ ] Verificação de estilo (flake8/ruff/black) quando aplicável  

### 11.4 Observabilidade
- [ ] Logging configurável (nível, arquivo)  
- [ ] Identificadores por execução/fluxo  
- [ ] Modo “diagnostics” (gerar relatório) — opcional, recomendado  

---

## 12) Documentação, suporte e onboarding

### 12.1 Documentação mínima
- [ ] Instalação (zip, preferências, dependências)  
- [ ] Quickstart (3–7 passos)  
- [ ] Troubleshooting (erros comuns e correções)  
- [ ] Compatibilidade (versões do Blender, OS)  
- [ ] Desinstalação/limpeza (remover preferências/caches)  
- [ ] Exemplos (arquivos de exemplo, se aplicável)  

### 12.2 Qualidade da documentação (PASS/FAIL)
- [ ] Executável por alguém novo em ≤ 15 min  
- [ ] Prints ou GIFs para fluxo principal (quando útil)  
- [ ] Links funcionando e atualizados  

---

## 13) Empacotamento e release

### 13.1 Estrutura do pacote
- [ ] Zip instalável padrão Blender (pasta do add-on correta)  
- [ ] `bl_info` completo (nome, versão, compatibilidade, descrição)  
- [ ] Sem arquivos desnecessários (build, caches, testes pesados)  
- [ ] Dependências inclusas ou instruções claras (preferível: vendorizadas de forma segura)  

### 13.2 Upgrade/rollback
- [ ] Atualizar versão não quebra preferências/salvos  
- [ ] Migração de dados (se existir) com fallback  
- [ ] Rollback para versão anterior funciona  

---

## 14) Rubrica de pontuação (0–5) e pesos

> **Como pontuar:** 0 = inexistente/ruim; 3 = adequado; 5 = excelente e comprovado.

| Área | Peso | Nota (0–5) | Subtotal |
|---|---:|---:|---:|
| Funcionalidade E2E | 25 |  |  |
| Integrações com Blender | 15 |  |  |
| Robustez/Confiabilidade | 15 |  |  |
| Performance | 10 |  |  |
| Segurança/Privacidade (se aplicável) | 10 |  |  |
| UX/Acessibilidade | 10 |  |  |
| Qualidade de código/manutenção | 10 |  |  |
| Documentação/Onboarding | 5 |  |  |
| **TOTAL** | **100** |  |  |

### 14.1 Critérios de decisão (sugestão)
- ✅ **Aprovado:** ≥ 80 e **sem bloqueadores**  
- ⚠️ **Aprovado com ressalvas:** 65–79 ou com riscos mitigáveis em curto prazo  
- ❌ **Reprovado:** < 65 ou com bloqueadores (crash, corrupção, insegurança crítica)

---

## 15) Achados detalhados (formato obrigatório)

Para cada achado:

- **ID:** A-###  
- **Categoria:** Funcionalidade / Integração / Robustez / Performance / Segurança / UX / Código / Docs / Release  
- **Severidade:** Bloqueador / Alta / Média / Baixa  
- **Descrição objetiva:**  
- **Evidência:** (passos, log, screenshot, arquivo, vídeo)  
- **Impacto:** (usuário/produção/pipeline)  
- **Causa provável:**  
- **Recomendação (ação):**  
- **Validação PASS/FAIL:** (como testar)  
- **Risco de regressão + mitigação:**  
- **Owner sugerido:**  
- **Status:** Aberto / Em progresso / Resolvido  

---

## 16) Backlog executável (priorizado)

| Prioridade | Tarefa | Objetivo | Passos | Aceite | Esforço | Risco |
|---:|---|---|---|---|---|---|
| P0 |  |  |  |  |  |  |
| P1 |  |  |  |  |  |  |

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

### Segurança (se aplicável)
- [ ] Sem execução insegura / downloads sem validação

### Documentação
- [ ] Quickstart executável do zero

---

## 18) Registro de evidências

| Evidência | Tipo | Local (arquivo/URL/caminho) | Observação |
|---|---|---|---|
| E-001 | Screenshot |  |  |
| E-002 | Log |  |  |

