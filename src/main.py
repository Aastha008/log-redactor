import sys
import uvicorn
from src.cli import run_cli

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'serve':
        uvicorn.run("src.api:app", host="0.0.0.0", port=8000)
    else:
        run_cli()