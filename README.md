## Poetry
```bash
poetry run
```

Запуск приложения
```bash
poetry run uvicorn main:app --reload
```

## Alembic
1) Начальная инициализация миграций

```bash
alembic init [catalog-for-migrations]
```
2) Отредактировать `alembic.ini`
```python
sqlalchemy.url = [path-to-db]
```
Настройка конфигурации `env.py`

4) Добавить модуль `db` в окружение `PYTHONPATH`
```python
import sys
sys.path.append('/task_manager/db/')
```

5) Импортировать базовую модель
```python
from task_manager.db import tables
target_metadata = tables.Base.metadata
```

Создание миграции
```bash
poetry run alembic revision --autogenerate -m "comment"
```

Выполнить апгрейд
```bash
poetry run alembic upgrade head
```
