#!/usr/bin/env python3
"""Gera uma versao self-contained (imagens em base64) para publicar como Artifact."""
import base64, pathlib, re

root = pathlib.Path(__file__).parent
html = (root / "index.html").read_text()

def data_uri(p):
    b = (root / p).read_bytes()
    return "data:image/jpeg;base64," + base64.b64encode(b).decode()

# troca src="img/XX.jpg" e href/content de imagens por data URI
def repl(m):
    attr, path = m.group(1), m.group(2)
    return f'{attr}="{data_uri(path)}"'

html = re.sub(r'(src|href|content)="(img/[^"]+\.jpg)"', repl, html)

# remove wrappers que o Artifact injeta
html = re.sub(r'<!DOCTYPE html>\s*', '', html, flags=re.I)
html = re.sub(r'</?html[^>]*>\s*', '', html, flags=re.I)
html = re.sub(r'</?body[^>]*>\s*', '', html, flags=re.I)
html = html.replace('<head>', '').replace('</head>', '')
# script no-js precisa continuar logo apos abertura do body -> ja esta inline no fluxo

out = root / "dist" / "chale-recanto-do-lago.html"
out.parent.mkdir(exist_ok=True)
out.write_text(html.strip())
print("ok", out, f"{out.stat().st_size/1024/1024:.1f} MB")
