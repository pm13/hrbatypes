Web [VSK MFF UK BL](https://www.hrbatypes.cz)
=============================================

[![Netlify Status](https://api.netlify.com/api/v1/badges/2d141e12-e877-4c09-9e80-ba12c255adb2/deploy-status)](https://app.netlify.com/sites/hrbatypes/deploys)

Instalace
---------

V Linuxu doporučujeme použít balíček s nástrojem **Pelican** (více viz https://blog.getpelican.com/) přítomný v distribuci. Pro Ubuntu je to `pelican`, pro Fedoru `python3-pelican`. (V některých distribucích může chybět v povinných závislostech **Markdown** - například v Arch Linuxu je navíc potřeba balíček `python-markdown`.)


Alternativně lze nainstalovat potřebné závislosti do virtuálního prostředí Pythonu, ale kdo by se s tím dělal:

```
pip install -r requirements.txt
```

V jiných systémech si nějak opatřete rozumnou instalaci Pythonu a spusťte výše uvedený příkaz.

Spuštění
--------

Pelican je generátor statických webových stránek, takže ve výchozím adresáři příkaz `pelican` udělá právě to - vygeneruje adresář `~/hrbatypes` (který lze někam nahrát). Následně můžete spustit server (doporučujeme):

```
pelican --listen
```

Oba kroky lze zkombinovat s obnovením po každé změně pomocí

```
pelican --autoreload --listen
```

Na <http://localhost:8000> potom uvidíte, jak bude vaše lokální varianta vypadat na webu.

Ve Windows jsme s `--listen` narazili na problém a museli zvolit alternativní řešení:

1. Vygenerovat `~/hrbatypes` (viz výše)

2. Spustit ve vygenerovaném adresáři integrovaný webový server Pythonu:

```
python -m http.server
```

Změna obsahu
------------

Všechny články se píšou v **Markdownu** (vysvětlení syntaxe viz třeba https://commonmark.org/help/ nebo https://help.gamejolt.com/markdown).

Články jsou strukturované do podadresářů `articles` podle sezón a jmenují se podle titulku, ale obojí je jen pro pohodlnost. Kde se na webu článek objeví, záleží na metadatech v něm. Příklad (snad pochopitelný):

```
Title: 47. Karlův běh
Date: 2018-02-14 09:07
Category: Zima 2017/18
Author: Vláďa
```

Přílohy (obrázky i výsledky) mají strukturu podobnou, ovšem v `static`. Odkazuje se pak na ně takto:

```
![JF]({static}/static/zima-2017-18/vasaloppet-jf.jpg)
```

a

```-
[celkové výsledky]({static}/static/zima-2017-18/boboloppet-2018.pdf)
```

### Poznámky

* Začínejte nadpisem druhé úrovně (první úroveň se použije pro titulek).

* Obrázky ukládejte v přiměřené velikosti.

* Úvodní stránku nenajdete v `articles`, ale v `pages` (`vitejte.md`).

### Vyšší (formátovací) dívčí

Jednotlivým elementům textu lze přidat CSS třídu (které rozumí [Bootstrap](https://getbootstrap.com/)) a další atributy. To se může hodit třeba pro obtékání obrázku. Příklad za všechny:

```
![K30 - bedna]({static}/static/zima-2016-17/k30-bedna.jpg){: .float-left .mr-2 width="450"}
```

Zde obrázek s Ferdinandem plave vlevo, vpravo má okraj 2 jednotky a je 450 pixelů široký (pochopitelně!).

Inspirujte se existujícími články a nebojte se zeptat toho, kdo to celé zpískal.
