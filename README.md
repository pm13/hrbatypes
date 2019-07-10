Web [VSK MFF UK BL](https://www.hrbatypes.cz)
=============================================

[![Netlify Status](https://api.netlify.com/api/v1/badges/2d141e12-e877-4c09-9e80-ba12c255adb2/deploy-status)](https://app.netlify.com/sites/hrbatypes/deploys)

Instalace
---------

V Linuxu doporučujeme použit balíček s nástrojem `pelican` (více viz https://blog.getpelican.com/) přítomný v distribuci. Pro Ubuntu je to `pelican`, pro Fedoru `python3-pelican`.


Alternativně lze nainstalovat potřebné závislosti do virtuálního prostředí Pythonu, ale kdo by se s tím dělal:

```
pip install -r requirements.txt
```

Ve Windows... **TODO!**

Spuštění
--------

Pelican je generátor statických webových stránek, takže ve výchozím adresáři spuštění `pelican` udělá právě to - vygeneruje adresář `~/tmp/hrbatypes`, který lze nahrát někam na server. Pokud chcete server rovnou pustit (doporučujeme):

```
pelican --listen
```

Oba kroky lze zkombinovat s obnovením po každé změně pomocí

```
pelican --autoreload --listen
```

Na <http://localhost:8000> potom uvidíte, jak bude vaše lokální varianta vypadat na webu.

Změna obsahu
------------

Všechny  články se píšou v **markdownu** (vysvětlení syntaxe viz třeba hhtps://commonmark.org/help nebo  https://help.gamejolt.com/markdown).

