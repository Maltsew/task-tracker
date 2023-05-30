## Poetry
```bash
poetry run
```

## Alembic
Начальная инициализация миграций

```bash
alembic init [catalog for migrations]
```
edit `alembic.ini`
```python
sqlalchemy.url = [path to db]
```
### Configure `env.py`

Add db module to `PYTHONPATH`
```python
import sys
sys.path.append('/task_manager/db/')
```

import Base model
```python
from task_manager.db import tables
target_metadata = tables.Base.metadata
```

Make migrations
```bash
poetry run alembic revision --autogenerate -m "comment"
```

Running upgrade
```bash
poetry run alembic upgrade head
```
