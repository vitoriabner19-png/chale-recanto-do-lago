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

## Publicar (Vercel)

```bash
cd /Users/macminim4/AI/chale-recanto-do-lago
npx vercel --prod
```

Site 100% estático — qualquer host serve (Vercel, Netlify, Cloudflare Pages, GitHub Pages).

## ⚙️ Configurar o WhatsApp

No fim do `index.html`, no `<script>`, ajuste:

```js
var WHATSAPP = "";   // ex: "5544999999999"  (DDI 55 + DDD + número, só dígitos)
```

Enquanto estiver vazio, os botões "Falar com os anfitriões" apontam para o próprio anúncio
do Airbnb. Preenchido, viram link `wa.me` com mensagem pronta.

## Conteúdo

Textos e dados vieram do anúncio do Airbnb e do Google Maps (Restaurante Recanto do Lago,
(44) 3542-3296). Avaliações citadas são reais (Giulianno, jul/2026 · Renata, jun/2026).
Para trocar fotos, substitua os arquivos em `img/` mantendo os nomes `01.jpg`…`14.jpg`
e rode `build-artifact.py` de novo.
