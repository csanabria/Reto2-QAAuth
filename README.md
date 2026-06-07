# Reto 2 - QA Automation (QAAuth)

Repositorio con soluciones y pruebas automatizadas para el Reto 2 del diplomado, usando Playwright y Selenium (Python y Java).

**Estructura**
- **Playwright-reto2/**: pruebas con Playwright (Python). Ver [Playwright-reto2](Playwright-reto2/README.md).
- **selenium-reto2/reto2-python-selenium/**: pruebas con Selenium en Python. Ver [selenium-reto2/reto2-python-selenium](selenium-reto2/reto2-python-selenium/requirements.txt).
- **selenium-reto2/reto2-java-selenium/**: pruebas con Selenium en Java (Maven). Ver [selenium-reto2/reto2-java-selenium](selenium-reto2/reto2-java-selenium/pom.xml).

**Requisitos generales**
- Python 3.8+ (recomendado utilizar un entorno virtual)
- Java 11+ (para la suite Java)
- Maven (puede usarse el Maven incluido en `selenium-reto2/tools/apache-maven-3.9.12/`)

-----------------------------

## Playwright (Python)

Carpeta: [Playwright-reto2](Playwright-reto2/README.md)

Pasos rápidos:

1. Crear entorno virtual e instalar dependencias:

```bash
python -m venv .venv
source .venv/Scripts/activate  # Windows: .venv\Scripts\Activate
pip install -U pip
pip install playwright
```

2. Instalar navegadores de Playwright:

```bash
python -m playwright install
```

3. Ejecutar la prueba de ejemplo:

```bash
python Playwright-reto2/test_playwright.py
```

Revisa [Playwright-reto2/README.md](Playwright-reto2/README.md) para detalles adicionales.

-----------------------------

## Selenium (Python)

Carpeta: `selenium-reto2/reto2-python-selenium`

Pasos rápidos:

1. Crear entorno virtual e instalar dependencias:

```bash
python -m venv .venv
source .venv/Scripts/activate  # Windows: .venv\Scripts\Activate
pip install -r selenium-reto2/reto2-python-selenium/requirements.txt
```

2. Ejecutar las pruebas (usar pytest si está disponible):

```bash
cd selenium-reto2/reto2-python-selenium
pytest -q
```

O bien ejecutar un script directamente:

```bash
python selenium-reto2/reto2-python-selenium/test_page.py
```

-----------------------------

## Selenium (Java)

Carpeta: `selenium-reto2/reto2-java-selenium`

Pasos rápidos:

1. Ejecutar con Maven (si tiene `mvn` en PATH):

```bash
cd selenium-reto2/reto2-java-selenium
mvn test
```

2. Usar el Maven incluido (Windows):

```bash
selenium-reto2\tools\apache-maven-3.9.12\bin\mvn.cmd -f selenium-reto2\reto2-java-selenium\pom.xml test
```

Los reportes de Surefire se generan en `selenium-reto2/reto2-java-selenium/target/surefire-reports/`.

-----------------------------

## Notas y buenas prácticas
- Usar entornos virtuales para aislar dependencias.
- Mantener los drivers y navegadores actualizados.
- Si una suite requiere variables de entorno o credenciales, usar `.env` o variables del sistema y no versionarlas.

## Contribuir
- Abrir issues para bugs o mejoras.
- Hacer pull requests pequeñas y descriptivas.

## Licencia
Revisar el archivo `LICENSE` en el repositorio raíz.
