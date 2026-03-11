protected_files=[

"ai_runner.py",
"brain.py",
"evolution_engine.py"

]

def is_protected(file):

    if file in protected_files:

        return True

    return False
