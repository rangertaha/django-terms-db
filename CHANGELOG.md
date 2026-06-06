# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Changed
- Target **Django 5.2 LTS** and **Django REST Framework 3.16+** (previously
  Django 1.9 / DRF 3.3).
- Set `requires-python = ">=3.10"` (supported Python window per SPEC 0).
- Migrated packaging from `setup.py`/`MANIFEST.in`/`requirements.txt` to a
  PEP 621 `pyproject.toml` with the Hatchling build backend.
- Modernized app code to the Django 5.2 baseline:
  - `ugettext_lazy` → `gettext_lazy`
  - `__unicode__` → `__str__`
  - `django.conf.urls.url`/`patterns` → `django.urls.path`/`re_path`
  - `MIDDLEWARE_CLASSES` → `MIDDLEWARE` (dropped removed
    `SessionAuthenticationMiddleware`)
  - removed the obsolete `TEMPLATE_DEBUG` setting and `null=True` on the
    `ManyToManyField`
  - template `{% load staticfiles %}` → `{% load static %}`
  - f-strings and plain `super()`
- Set `DEFAULT_AUTO_FIELD = BigAutoField` in the example project.

### Fixed
- Serializer and form referenced non-existent model fields (`title`, `code`);
  corrected to the actual fields (`short`, `long`). `CategorySerializer` now
  uses fields that exist on `Category` (`slug`, `name`, `count`).

### Added
- Initial database migration for the `terms` app (`0001_initial`).
- GitHub Actions CI (test matrix across Python 3.10–3.13) and a PyPI publish
  workflow using Trusted Publishing (OIDC).

### Removed
- Unused `django-fontawesome` dependency.
