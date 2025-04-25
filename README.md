Example error code for https://github.com/AmbitionEng/django-pgtrigger/issues/205

- Clone down repo.
- Install deps (uv sync)
- Enable virtualenv - `. .venv/bin/active`
- Make sure environmental variables from .env are loaded (direnv)
- Start example postgres server - `docker compose up`
- Sync migrations `manage.py migrate`
- Create new migration `manage.py makemigrations` -- Error will occur here

Error For Reference
-------------------

```
Traceback (most recent call last):
  File "/home/john/Code/pgtrigger-test/./manage.py", line 22, in <module>
    main()
  File "/home/john/Code/pgtrigger-test/./manage.py", line 18, in main
    execute_from_command_line(sys.argv)
  File "/home/john/Code/pgtrigger-test/.venv/lib/python3.12/site-packages/django/core/management/__init__.py", line 442, in execute_from_command_line
    utility.execute()
  File "/home/john/Code/pgtrigger-test/.venv/lib/python3.12/site-packages/django/core/management/__init__.py", line 436, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
  File "/home/john/Code/pgtrigger-test/.venv/lib/python3.12/site-packages/django/core/management/base.py", line 416, in run_from_argv
    self.execute(*args, **cmd_options)
  File "/home/john/Code/pgtrigger-test/.venv/lib/python3.12/site-packages/django/core/management/base.py", line 460, in execute
    output = self.handle(*args, **options)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/john/Code/pgtrigger-test/.venv/lib/python3.12/site-packages/django/core/management/base.py", line 107, in wrapper
    res = handle_func(*args, **kwargs)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/john/Code/pgtrigger-test/.venv/lib/python3.12/site-packages/django/core/management/commands/makemigrations.py", line 236, in handle
    changes = autodetector.changes(
              ^^^^^^^^^^^^^^^^^^^^^
  File "/home/john/Code/pgtrigger-test/.venv/lib/python3.12/site-packages/django/db/migrations/autodetector.py", line 67, in changes
    changes = self._detect_changes(convert_apps, graph)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/john/Code/pgtrigger-test/.venv/lib/python3.12/site-packages/pgtrigger/migrations.py", line 224, in _detect_changes
    return super()._detect_changes(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/john/Code/pgtrigger-test/.venv/lib/python3.12/site-packages/django/db/migrations/autodetector.py", line 189, in _detect_changes
    self.generate_created_models()
  File "/home/john/Code/pgtrigger-test/.venv/lib/python3.12/site-packages/pgtrigger/migrations.py", line 312, in generate_created_models
    self._get_add_trigger_op(model=model, trigger=trigger),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/john/Code/pgtrigger-test/.venv/lib/python3.12/site-packages/pgtrigger/migrations.py", line 228, in _get_add_trigger_op
    trigger = trigger.compile(model)
              ^^^^^^^^^^^^^^^^^^^^^^
  File "/home/john/Code/pgtrigger-test/.venv/lib/python3.12/site-packages/pgtrigger/core.py", line 831, in compile
    condition=self.render_condition(model),
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/john/Code/pgtrigger-test/.venv/lib/python3.12/site-packages/pgtrigger/core.py", line 740, in render_condition
    resolved = condition.resolve(model).strip() if condition else ""
               ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/john/Code/pgtrigger-test/.venv/lib/python3.12/site-packages/pgtrigger/core.py", line 408, in resolve
    raise ValueError(f'Field "{field}" not found on model "{model}"')
ValueError: Field "product_id" not found on model "<class '__fake__.ProductVariant'>"
```