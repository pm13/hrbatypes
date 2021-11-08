#!/usr/bin/env python

import pathlib
import subprocess

import click


@click.command()
def generate_style():
    'Generate style for web VSK MFF UK BL'

    bootstrap_path = pathlib.Path('~/.local/lib/node_modules/bootstrap').expanduser()
    theme_path = pathlib.Path('~/src/hrbatypes/theme/static').expanduser()

    bootstrap_link_path = theme_path / 'bootstrap'
    if bootstrap_link_path.exists():
        bootstrap_link_path.unlink()
    bootstrap_link_path.symlink_to(bootstrap_path)

    subprocess.run(('sass', '--no-source-map', 'style.scss', 'style.css'), cwd=theme_path)
    subprocess.run(('sass', '--style', 'compressed', '--no-source-map', 'style.scss', 'style.min.css'), cwd=theme_path)

    bootstrap_link_path.unlink()


generate_style()
