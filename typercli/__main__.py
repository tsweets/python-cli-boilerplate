"""Typer CLI Example entry point script."""
# typercli/__main__.py

from typercli import cli, __app_name__

def main():
    cli.app(prog_name=__app_name__)

if __name__ == "__main__":
    main()