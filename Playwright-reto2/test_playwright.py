
# ejecutar con pytest desde la carpeta Playwright-reto2

# primer en carpeta playwright-las b ejecutar 
# python -m pip install playwright
#python -m playwright install
# para validar la instalación de playwright ejecutar el siguiente comando
#phython -m playwright --version


import asyncio

import pytest
from playwright.sync_api import sync_playwright, expect

# ---------- FIXTURES (equivalente a @BeforeAll / @AfterAll) ----------

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=False)
    yield browser
    browser.close()


# ---------- FIXTURES (equivalente a @BeforeEach / @AfterEach) ----------

@pytest.fixture
def context(browser):
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture
def page(context):
    page = context.new_page()
    page.goto("https://www.demoblaze.com/index.html")
    return page

# ---------- TEST ----------

def test_validar_formulario_login(page):
    # Abrir modal de login
    page.click("#login2")

    # Esperar que aparezca el modal
    page.wait_for_selector("#logInModal", state="visible")

    # Rellenar usuario y contraseña
    page.fill("#loginusername", "demoQA")
    page.fill("#loginpassword", "demo123")

    # Hacer clic en el botón de login
    page.click("button[onclick='logIn()']")
    
    # Esperar que aparezca el nombre de usuario en la barra superior
    page.wait_for_selector("#nameofuser")
    # Validar que el nombre de usuario es correcto
    expect(page.locator("#nameofuser")).to_have_text("Welcome demoQA")

    # Pausa de 5 segundos para ver el resultado (opcional)
    page.wait_for_timeout(1000)

# ---------- TEST ----------
# Depende del test de login, ya que para validar el logout necesitamos estar logueados
def test_validar_logout(page):
    test_validar_formulario_login(page)  # Reutiliza el test de login

    # Hacer clic en el botón de logout
    page.click("#logout2")
    # Esperar que desaparezca el nombre de usuario en la barra superior
    page.wait_for_selector("#nameofuser", state="hidden")
    # Validar que el nombre de usuario ya no está visible
    expect(page.locator("#nameofuser")).to_be_hidden()
    #validar que el link login2 es visible
    expect(page.locator("#login2")).to_be_visible()

    # Pausa de 1 segundos para ver el resultado (opcional)
    page.wait_for_timeout(1000)

# ---------- TEST ----------
# Reutiliza el test de login
def test_agregar_producto_al_carrito(page):
    test_validar_formulario_login(page)  # Reutilizamos el test de login para asegurarnos de que estamos logueados
    # Hacer clic en el producto "Sony vaio i5"
    page.click("a:has-text('Sony vaio i5')")
    # Esperar que se cargue la página del producto
    page.wait_for_selector(".name")
    # Validar que el nombre del producto es correcto
    expect(page.locator(".name")).to_have_text("Sony vaio i5")

    # Manejar el alert al hacer Add to Cart
    # async def handle_dialog(dialog):
    #     print(f"⚠️ Alert recibido: {dialog.message}")
    #     await dialog.accept()

    # page.on("dialog", handle_dialog)
    # Registrar handler ANTES de hacer clic
    page.once("dialog", lambda dialog: dialog.accept())
    # page.once("dialog", lambda dialog: asyncio.create_task(dialog.accept()))
    # Hacer clic en el botón "Add to cart"
    page.click("a:has-text('Add to cart')")
    # Esperar un poco para que se dispare el alert y se acepte
    page.wait_for_timeout(2000)

    print("Producto agregado al carrito (alert aceptado)")
    # # Validar que el mensaje de confirmación es correcto
    # expect(page.locator("#exampleModal .modal-body")).to_have_text("Product added")
    # # Cerrar el modal de confirmación
    # page.click("#exampleModal .btn-secondary")
    # # Hacer clic en el enlace "Cart" para ir al carrito de compras
    # page.click("#cartur")
    # # Esperar que se cargue la página del carrito
    # page.wait_for_selector(".table-responsive")
    # # Validar que el producto agregado está en el carrito
    # expect(page.locator(".table-responsive")).to_have_text("Sony vaio ")
    # Pausa de 1 segundos para ver el resultado (opcional)
    page.wait_for_timeout(1000)

