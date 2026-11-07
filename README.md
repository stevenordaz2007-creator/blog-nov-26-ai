# Arepas El Sabor - Sitio Web (Fase 1)

Sitio web sencillo, gratuito y listo para usar para vender arepas en **Puerto La Cruz, Venezuela**.

## ¿Qué incluye?

- 🫓 Catálogo de arepas con fotos y precios
- 🛒 Carrito de compras (funciona en el navegador, se guarda al recargar)
- 💬 Pedido por WhatsApp con resumen automático del carrito
- 📱 Sección de Pago Móvil y Transferencia Bancaria
- 🛵 Info de Delivery por zonas de Puerto La Cruz
- 📷 Galería de fotos
- 📍 Contacto, ubicación, horarios y redes sociales
- 📱 Diseño responsivo (celular y computadora)

## Cómo usar este sitio (sin saber programar)

### 1. Edita tus datos
Abre el archivo `index.html` con el Bloc de notas o cualquier editor de texto (VS Code, Sublime, Notepad++) y busca estas secciones para personalizarlas:

**WhatsApp**
```js
const WHATSAPP_NUMBER = "58XXXXXXXXX";
```
Cambia `58XXXXXXXXX` por tu número de WhatsApp con código de país (ejemplo: `584121234567`), sin espacios ni el símbolo `+`.

**Pago Móvil** (dentro del HTML, sección `#pago`)
Edita los textos dentro de los `span` con `id="pago-banco"`, `id="pago-telefono"`, `id="pago-titular"` y `id="pago-rif"` con tus datos reales.

**Productos**
En la variable `products` del JavaScript (abajo del archivo) puedes agregar, editar o eliminar arepas, cambiar precios y poner descripciones.

**Imágenes**
Las imágenes actuales son placeholders (de internet). Sustitúyelas por fotos tuyas:
1. Sube tus fotos a un sitio gratuito (Imgur, Google Fotos con enlace público, etc.)
2. Reemplaza la URL de `img` en cada producto.

### 2. Prueba en tu computadora
Haz doble clic en `index.html`. Se abrirá en tu navegador. Puedes navegar, agregar productos al carrito y probar el botón de WhatsApp.

### 3. Publica gratis en internet
Opción A - **GitHub Pages** (recomendado):
1. Crea una cuenta en github.com
2. Crea un repositorio nuevo (ejemplo: `arepas-el-sabor`)
3. Sube los archivos `index.html` y `README.md`
4. Ve a Settings > Pages y activa GitHub Pages desde la rama `main`
5. Tendrás una URL tipo: `https://tuusuario.github.io/arepas-el-sabor/`

Opción B - **Netlify Drop**:
1. Ve a netlify.com/drop
2. Arrastra la carpeta que contiene `index.html`
3. Obtendrás una URL gratuita al instante

### 4. Comparte
Envía el link de tu web por los estados de WhatsApp, Facebook e Instagram. Los clientes podrán ver el menú, armar su carrito y escribirte por WhatsApp para confirmar el pago con Pago Móvil.

## Limitaciones de la Fase 1

- El pago **no es automático** en la web. El cliente te escribe por WhatsApp y tú le das los datos de Pago Móvil/transferencia.
- El carrito se guarda en el navegador del cliente (localStorage), no en una base de datos propia.
- Cuando crezcas, puedes pasar a una tienda con carrito automático, pasarela de pagos y base de datos.

## Soporte

Si necesitas ayuda para editar los datos o subir el sitio, dime y te guío.