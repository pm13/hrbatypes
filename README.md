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

Všechny  články se píšou v **markdownu** (vysvětlení syntaxe viz třeba https://commonmark.org/help nebo  https://help.gamejolt.com/markdown).

Články jsou strukturované do podadresářů `articles` podle sezón a jmenují se podle titulku, ale obojí je jen pro pohodlnost. Kde se na webu článek objeví, záleží na metadatech v něm. Příklad (snad pochopitelný):

```
Title: 47. Karlův běh
Date: 2018-02-14 09:07
Category: Zima 2017/18
Author: Vláďa
```

Přílohy (obrázky i výsledky) mají strukturou podobnou, ovšem v `static`. Odkazuje se pak na ně takto:

```
![JF]({static}/static/zima-2017-18/vasaloppet-jf.jpg)
```

a 

```
[celkové výsledky]({static}/static/zima-2017-18/boboloppet-2018.pdf)
```
### Formátovací poznámky

* Začínejte nadpisem druhé úrovně (první úroveň se použije pro titulek).

### Vyšší (formátovací) dívčí

Jednotlivým elementům textu lze přidat CSS třídu (které rozumí [bootstrap](https://getbootstrap.com/) )

