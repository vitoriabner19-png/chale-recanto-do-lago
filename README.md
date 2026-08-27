# Chalé Recanto do Lago — site

Site de divulgação do chalé (Airbnb `1652299122420318820`), em Campina da Lagoa/PR.

## Arquivos

| Caminho | O que é |
|---|---|
| `index.html` | O site. Estático, sem build. Usa as imagens de `img/`. |
| `img/` | 14 fotos (baixadas do anúncio, redimensionadas p/ web). |
| `build-artifact.py` | Gera `dist/chale-recanto-do-lago.html` com as imagens embutidas (base64), versão single-file p/ publicar como Artifact do Claude. |
| `dist/` | Saída do script acima. |

## Rodar localmente

```bash
cd /Users/macminim4/AI/chale-recanto-do-lago
python3 -m http.server 8000
# abrir http://localhost:8000
```

## 🌐 No ar

**https://chale-recanto-do-lago.vercel.app**

Hospedado na Vercel (conta `recantodolagocampina-5500`, projeto `chale-recanto-do-lago`).
Para republicar depois de editar:
```bash
cd /Users/macminim4/AI/chale-recanto-do-lago
npx vercel --prod
```

## Publicar (outras opções)

Site 100% estático — qualquer host serve.

### GitHub Pages (repo já criado e com push feito)

Repo: https://github.com/vitoriabner19-png/chale-recanto-do-lago

Falta 1 passo (precisa ser feito no navegador, logado como `vitoriabner19-png`):
**Settings → Pages → Build and deployment → Source: "Deploy from a branch" →
Branch: `main` / `/ (root)` → Save.**

Em ~1 min o site fica no ar em:
`https://vitoriabner19-png.github.io/chale-recanto-do-lago/`

Depois disso, para atualizar o site é só:
```bash
cd /Users/macminim4/AI/chale-recanto-do-lago
git add -A && git commit -m "ajustes" && git push
```

### Vercel (alternativa)

```bash
cd /Users/macminim4/AI/chale-recanto-do-lago
npx vercel login      # abre o navegador
npx vercel --prod
```

## ⚙️ Configurar o WhatsApp

Já configurado: `var WHATSAPP = "5544997108741";` — (44) 99710-8741.
Os botões "Falar com os anfitriões" abrem o WhatsApp com mensagem pronta.
Para trocar, edite essa linha no `<script>` no fim do `index.html`.

## Widget de reserva do Airbnb

A seção "Informações práticas & reserva" tem o widget oficial do Airbnb embutido
(`<div class="airbnb-embed-frame">` + `airbnb_jssdk`). Ele carrega no site publicado;
na versão Artifact do Claude aparece só o link de fallback (o CSP bloqueia scripts externos).

## Conteúdo

Textos e dados vieram do anúncio do Airbnb e do Google Maps (Restaurante Recanto do Lago,
(44) 3542-3296). Avaliações citadas são reais (Giulianno, jul/2026 · Renata, jun/2026).
Para trocar fotos, substitua os arquivos em `img/` mantendo os nomes `01.jpg`…`14.jpg`
e rode `build-artifact.py` de novo.
