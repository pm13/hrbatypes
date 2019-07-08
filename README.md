Web [VSK MFF UK BL](https://www.hrbatypes.cz)
=============================================

[![Netlify Status](https://api.netlify.com/api/v1/badges/2d141e12-e877-4c09-9e80-ba12c255adb2/deploy-status)](https://app.netlify.com/sites/hrbatypes/deploys)

Installation
------------

You need a reasonably new version of Python and the `pelican` library. In Linux and a properly setup virtual environment (see https://realpython.com/python-virtual-environments-a-primer/ or https://conda.io/en/latest/ for details), all your needs should be satisfied with:

```
pip install -r requirements.txt
```

**TODO:** Test on Windows.

Run
---

Although pelican is a static website generator, the following command starts a "live" version of the server.

```
pelican --listen
```

You can then see your local web at `localhost:8000`.

Editing
-------
All articles are written in markdown (see e.g. https://help.gamejolt.com/markdown to learn the syntax).


