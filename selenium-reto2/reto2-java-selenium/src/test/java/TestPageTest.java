
// ejecutar con: mvn clean test desde la carpeta reto2-java-selenium

import org.junit.jupiter.api.*; // Importa anotaciones de JUnit 5
import org.openqa.selenium.*; // Importa WebDriver y By
import org.openqa.selenium.chrome.ChromeDriver; // Importa el driver de Chrome
import org.openqa.selenium.support.ui.WebDriverWait; // Importa WebDriverWait para esperas explícitas
import org.openqa.selenium.support.ui.ExpectedConditions; // Importa condiciones de espera
import java.time.Duration; // Importa Duration para definir tiempos de espera

/**
 * Clase de prueba con Selenium y JUnit 5.
 * Valida el login en la página de ejemplo "the-internet.herokuapp.com".
 */
public class TestPageTest {

    WebDriver driver;

    /**
     * Configuración inicial antes de cada test.
     * Se abre el navegador Chrome y se carga la URL de login.
     */
    @BeforeEach
    void setUp() {
        driver = new ChromeDriver();
        driver.get("https://the-internet.herokuapp.com/login");
    }

    /**
     * Caso de prueba: validar el formulario de login.
     * - Ingresa credenciales válidas
     * - Hace clic en el botón Login
     * - Espera explícitamente a que aparezca el mensaje de éxito
     * - Verifica que el mensaje contenga el texto esperado
     */
    @Test
    void validarFormulario() {
        // Ingresar usuario y contraseña
        driver.findElement(By.id("username")).sendKeys("tomsmith");
        //driver.findElement(By.id("password")).sendKeys("SuperSecretPassword!");
        driver.findElement(By.id("password")).sendKeys("SuperSecretPassword!");

        // Hacer clic en el botón Login
        driver.findElement(By.xpath("//button[contains(., 'Login')]")).click();

        // Espera explícita: hasta 10 segundos para que el mensaje sea visible
        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
        WebElement resultElement = wait.until(
                ExpectedConditions.visibilityOfElementLocated(By.id("flash")));

        // Obtener el texto del mensaje
        String result = resultElement.getText();

        // Validar que el mensaje contenga la cadena esperada
        Assertions.assertTrue(
                result.contains("You logged into a secure area!"),
                "El mensaje no es correcto");
       //espera implicita de 5 segundos para ver el resultado
       try {
            Thread.sleep(5000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

    }

    /**
     * Limpieza después de cada test.
     * Se cierra el navegador.
     */
    @AfterEach
    void tearDown() {
        driver.quit();
    }
}