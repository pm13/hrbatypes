# List available recipes
default:
    @just --list

# Run Pelican dev server
pelican port="8000":
    CSS_DEBUG=1 pelican --autoreload --listen --port {{ port }} -s pelicanconf.py

# Watch Tailwind and write site.css
tailwind:
    tailwindcss -i assets/tailwind.css -o theme/static/site.css --watch

# Build Tailwind and write site.css + site.min.css
tailwind-build:
    tailwindcss -i assets/tailwind.css -o theme/static/site.css
    tailwindcss -i assets/tailwind.css -o theme/static/site.min.css --minify
