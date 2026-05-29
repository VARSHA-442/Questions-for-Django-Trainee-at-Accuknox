# Accuknox Django Trainee Assignment

## Topic: Django Signals

**Q1 — Synchronous execution** (`Answer1/`)
Proves signals block the caller. Run: `python manage.py test_sync_signal`

**Q2 — Same thread as caller** (`Answer2/`)
Proves signal runs in MainThread. Run: `python manage.py test_thread_signal`

**Q3 — Same database transaction** (`Answer3/`)
Proves signal rolls back with the caller's transaction. Run: `python manage.py test_transaction_signal`

## Topic: Custom Classes in Python

**Rectangle class** (`Class/code2.py`)
Implements `__iter__` returning `{'length': ...}` then `{'width': ...}`.