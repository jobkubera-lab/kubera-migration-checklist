# Kubera Migration Checklist

Готовый чек-лист для клиентов **Kubera LLC Migration**: как подать на рабочую визу — шаг за шагом.

## Установка (из GitHub)
```bash
pip install git+https://github.com/<YOUR_GH_USER_OR_ORG>/kubera-migration-checklist.git
```

Установка (локально)
```
pip install -e .
```

Использование
```
kubera-checklist
kubera-checklist --output checklist.md
kubera-checklist --format txt --output checklist.txt
pip install "reportlab>=4"           # для PDF
kubera-checklist --format pdf --output checklist.pdf
```

Публикация на PyPI

Автоматически — при создании GitHub Release (см. GitHub Actions).

Ручная публикация:
```
python -m pip install --upgrade build twine
python -m build
python -m twine upload dist/*
```

**`LICENSE`**



MIT License


Copyright (c) 2025 Kubera
... (\u0441тандартный текст MIT, оставить как есть) ...
