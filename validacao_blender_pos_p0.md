# Validação Blender — Pós-correções P0/P1

Data: 04/02/2026

## Objetivo

Validar em Blender as correções aplicadas para:

- `A-002`: parent/transform correto no fluxo de importação com múltiplos pais.
- `A-003`: tratamento seguro quando o asset importado não contém objetos.

## Pré-requisitos

- Blender 4.2+.
- Pacote instalável do JewelCraft (release zip com `assets` incluídos).
- Add-on ativado no Blender.

### Preparação do pacote (workspace atual)

1. Rode `python scripts/sync_assets_from_release.py --force` (uma vez).
2. Rode `python scripts/build_dev_zip.py`.
3. Use o zip gerado em `dist/jewelcraft-dev-2.18.0.zip`.

## Checklist de execução

### 1) Smoke de instalação/ativação

1. Instale o add-on pelo `Preferences > Add-ons > Install...`.
2. Ative o add-on.
3. Feche e reabra o Blender.
4. Confirme se os painéis do JewelCraft continuam visíveis.

Resultado esperado:

- PASS sem erro de ativação.

---

### 2) Regressão A-002 — import com múltiplos pais

1. Crie 3 objetos mesh na cena (`P1`, `P2`, `P3`) e selecione os 3.
2. Tenha um asset `.blend` válido com apenas 1 objeto.
3. No painel de Assets do JewelCraft, importe o asset com `Alt` pressionado (modo parent).
4. Verifique no Outliner:
   - cada pai (`P1`, `P2`, `P3`) deve ter uma cópia filha;
   - transform (posição/rotação) da cópia deve acompanhar cada pai.

Resultado esperado:

- PASS: 3 cópias, cada uma parentada ao seu respectivo objeto.
- FAIL: cópias concentradas em um único pai ou transform incorreto.

---

### 3) Regressão A-003 — asset sem objetos

1. Gere/obtenha um `.blend` sem objetos importáveis no lote.
2. Tente importar pelo operador de asset.

Resultado esperado:

- PASS: operador cancela com erro amigável (`No objects found in selected asset`).
- PASS: sem traceback no console.

---

### 4) Sanidade de regressão geral

1. Rode os fluxos principais já existentes:
   - Add Gem
   - Design Report (HTML/JSON)
   - Gem Map
2. Execute o teste automatizado disponível (ambiente com Blender):
   - `python tests/main.py`

Resultado esperado:

- PASS: sem regressões visíveis.

---

### 5) Regressão A-004 — idempotência de handlers

1. Faça 10 ciclos de disable/enable do add-on.
2. No Python Console do Blender, execute:
   - `sum(1 for h in bpy.app.handlers.load_post if h.__name__ == "_execute")`
3. Desative o add-on e rode novamente o mesmo comando.

Resultado esperado:

- PASS com add-on ativo: contagem igual a `1`.
- PASS com add-on desativado: contagem igual a `0`.
- PASS: nenhum erro ao ativar/desativar.

---

### 6) Regressão A-005 — cache de localização em JSON

1. Com add-on ativo, verifique criação de `source/localization/__cache__.json`.
2. Feche o Blender.
3. Edite o arquivo de cache e deixe JSON inválido.
4. Reabra o Blender e ative o add-on.

Resultado esperado:

- PASS: add-on inicia sem crash.
- PASS: cache é reconstruído automaticamente a partir dos `.po`.
- PASS: não há uso de `pickle` no fluxo.

---

### 7) Regressão A-006 — CI mínima

1. Verifique se existe `.github/workflows/ci.yml`.
2. Em PR, confirme execução do job `syntax-check`.

Resultado esperado:

- PASS: workflow executa `python -m compileall source tests`.

---

### 8) P2 — empacotamento dev/test

1. Garanta que `source/assets` esteja presente.
2. Rode `python scripts/build_dev_zip.py`.
3. Verifique o artefato gerado em `dist/`.

Resultado esperado:

- PASS: zip criado com estrutura raiz `jewelcraft/...`.

## Registro de evidências

Para cada item acima, registrar:

- screenshot do estado final;
- trecho de console (quando aplicável);
- versão do Blender usada.
