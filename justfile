# List available recipes
default:
    @just --list

# Run Pelican dev server
pelican port="8000":
    pelican --autoreload --listen --port {{ port }} -s pelicanconf.py

# Tailwind watch build
tailwind:
    tailwindcss -i assets/tailwind.css -o theme/static/site.css --watch

# Tailwind full build (regular + minified)
tailwind-build:
    tailwindcss -i assets/tailwind.css -o theme/static/site.css
    tailwindcss -i assets/tailwind.css -o theme/static/site.min.css --minify
