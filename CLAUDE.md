# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Python Environment

- **Python version**: 3.9.13 (managed via pyenv, see `.python-version`)
- **Test framework**: unittest (built-in)
- **No external dependencies** are currently required (modules use only stdlib)

## Running Tests

### All tests
```bash
python -m unittest discover
```

### Single test file
```bash
python test_calculator.py
# or
python -m unittest test_calculator
```

### Specific test class
```bash
python -m unittest test_calculator.TestCalculator
```

### Specific test method
```bash
python -m unittest test_calculator.TestCalculator.test_add
```

### With verbose output
```bash
python -m unittest discover -v
```

## Project Structure

**Root level modules** — Simple utility classes with corresponding unit tests:
- `calculator.py` / `test_calculator.py` — Basic arithmetic operations
- `datetimehelper.py` / `test_datetimehelper.py` — Date format conversions (US ↔ Indian)
- `figura.py` / `test_figura.py` — Geometric shape class
- `cuentas.py` — Account/banking related utilities (no tests currently)

**`fakelogger/`** — Minimal logging implementation mimicking the logging.Logger interface:
- `fakelogger.py` — FakeLogger class that prints messages instead of logging
- `main.py` — Example usage of FakeLogger

**`performance/`** — Performance and algorithmic examples:
- `fractals/` — Mandelbrot set generator using PIL
- `primes/` — Prime number algorithms (threads, performance comparison)
- `joblib/` — Joblib parallelization examples
- `tpe/` — Thread pool executor patterns
- Various string and tuple performance scripts

**`sockets/`** — Network socket programming examples:
- `chatserver.py` / `chatclient.py` — Simple TCP echo server/client with threading
- `twisted/` — Async socket examples using the Twisted framework

**`data-compression/`** — Data compression examples (zlib testing)

**`docum/`** — Documentation and related files

## Development Notes

- Tests use standard unittest assertions (`assertEqual`, `assertTrue`, etc.)
- Most modules are educational examples or utilities — focus on clarity over abstraction
- Some modules import external packages (PIL for Mandelbrot, Twisted for async sockets) but are not core dependencies
- The project is multiplatform-ready but developed on Windows (PowerShell notes in README suggest pyenv-win setup)
