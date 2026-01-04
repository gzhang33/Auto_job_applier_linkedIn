# Repository Project-Specific Rules

## Project Structure & Module Organization

### Core Files
- `app.py`: Flask UI for viewing application records
- `runAiBot.py`: Entry point for automated workflows

### Directory Layout
- `modules/`: Logic components
- `config/`: Parameter declarations, including `secrets.py` (sensitive data)
- `templates/`: UI and email templates
- `setup/`: Installation scripts
- `all resumes/`, `all excels/`: Output files
- `logs/`: Log files
- `__pycache__/`, `.venv/`: Should not be committed

### File Placement Rules
- New feature code → appropriate submodule in `modules/`
- Configuration → `config/`
- Templates → `templates/`
- Test files → should follow `test_*.py` naming

---

## Build, Run, and Development Commands

```bash
pip install -r requirements.txt    # Install dependencies
python runAiBot.py                 # Run automated job workflow
python app.py                      # Launch local service http://localhost:5000
python test.py                     # Manual check, required after modifying key logic
