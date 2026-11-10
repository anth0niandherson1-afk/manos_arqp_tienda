# ==========================================
# Generador de Archivos Web - Manos Arequipeñas
# Guardar y ejecutar en Sublime Text como 'generar_archivos.py'
# ==========================================

# 1. Contenido para 'index.html'
html_content = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Manos Arequipeñas - Textiles en Alpaca</title>
    <!-- Google Fonts & Font Awesome Icons -->
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&family=Playfair+Display:wght@600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- CSS Externo -->
    <link rel="stylesheet" href="styles.css">
</head>
<body>

    <!-- Header Navigation -->
    <header>
        <div class="navbar">
            <a href="#" class="logo">
                <i class="fa-solid fa-mountain"></i> Manos Arequipeñas
            </a>
            <div class="cart-icon" onclick="scrollToContact()">
                <i class="fa-solid fa-bag-shopping"></i>
                <span class="cart-badge" id="cart-count">0</span>
            </div>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <div class="hero-content">
            <h1>Artesanía Tradicional en Alpaca</h1>
            <p>Piezas únicas hechas a mano por Doña Elena desde la hermosa ciudad de Arequipa.</p>
            <a href="#catalogo" class="btn-primary">Ver Productos</a>
        </div>
    </section>

    <!-- Catálogo de Productos -->
    <main class="catalog-container" id="catalogo">
        <h2 class="section-title">Nuestra Colección</h2>
        <p class="section-subtitle">Tejidos 100% de fibra de alpaca de alta calidad</p>

        <!-- Grid de Productos -->
        <div class="product-grid" id="grid-productos">
            <!-- Carga dinámica vía script.js -->
        </div>
    </main>

    <!-- Sección de Contacto & WhatsApp -->
    <section class="contact-section" id="contacto">
        <div class="contact-container">
            <h2 class="section-title">Haz tu Pedido Directo</h2>
            <p>¿Tienes dudas o deseas realizar un pedido personalizado? Escríbele directamente a Doña Elena por WhatsApp.</p>
            <a href="#" id="whatsapp-link" target="_blank" class="whatsapp-btn">
                <i class="fa-brands fa-whatsapp"></i> Pedir por WhatsApp
            </a>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <p>&copy; 2026 Manos Arequipeñas - Taller Artesanal de Doña Elena, Arequipa - Perú.</p>
    </footer>

    <!-- JavaScript Externo -->
    <script src="script.js"></script>
</body>
</html>
"""

# 2. Contenido para 'styles.css'
css_content = """:root {
    --primary: #8B263E; /* Rojo Terracota / Borgoña */
    --primary-dark: #661A2D;
    --accent: #D4A373; /* Tono Cálido Fibra */
    --bg-light: #FAEDCD;
    --text-dark: #2B2D42;
    --text-muted: #6C757D;
    --white: #FFFFFF;
    --card-shadow: 0 10px 20px rgba(0, 0, 0, 0.08);
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Poppins', sans-serif;
}

body {
    background-color: #FAF9F6;
    color: var(--text-dark);
    line-height: 1.6;
}

/* Header & Navegación */
header {
    background-color: var(--white);
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    position: sticky;
    top: 0;
    z-index: 1000;
}

.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    max-width: 1200px;
    margin: 0 auto;
    padding: 1rem 2rem;
}

.logo {
    font-family: 'Playfair Display', serif;
    font-size: 1.8rem;
    font-weight: 700;
    color: var(--primary);
    text-decoration: none;
    display: flex;
    align-items: center;
    gap: 10px;
}

.cart-icon {
    position: relative;
    cursor: pointer;
    font-size: 1.4rem;
    color: var(--primary);
}

.cart-badge {
    position: absolute;
    top: -8px;
    right: -10px;
    background-color: var(--primary);
    color: white;
    font-size: 0.75rem;
    font-weight: bold;
    padding: 2px 6px;
    border-radius: 50%;
}

/* Hero / Sección de Inicio */
.hero {
    background: linear-gradient(rgba(0, 0, 0, 0.55), rgba(0, 0, 0, 0.55)), 
                url('https://images.unsplash.com/photo-1584917865442-de89df76afd3?auto=format&fit=crop&w=1200&q=80') center/cover no-repeat;
    height: 70vh;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    color: var(--white);
    padding: 0 1rem;
}

.hero-content {
    max-width: 800px;
}

.hero h1 {
    font-family: 'Playfair Display', serif;
    font-size: 3rem;
    margin-bottom: 1rem;
    letter-spacing: 1px;
}

.hero p {
    font-size: 1.2rem;
    margin-bottom: 2rem;
    font-weight: 300;
}

.btn-primary {
    background-color: var(--primary);
    color: var(--white);
    padding: 0.8rem 2rem;
    border: none;
    border-radius: 30px;
    font-size: 1rem;
    font-weight: 600;
    cursor: pointer;
    text-decoration: none;
    transition: background 0.3s ease;
    display: inline-block;
}

.btn-primary:hover {
    background-color: var(--primary-dark);
}

/* Catálogo de Productos (Grid) */
.catalog-container {
    max-width: 1200px;
    margin: 4rem auto;
    padding: 0 2rem;
}

.section-title {
    text-align: center;
    font-family: 'Playfair Display', serif;
    font-size: 2.2rem;
    color: var(--primary);
    margin-bottom: 0.5rem;
}

.section-subtitle {
    text-align: center;
    color: var(--text-muted);
    margin-bottom: 3rem;
}

/* Configuración de la Cuadrícula (Grid) */
.product-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 2rem;
}

.product-card {
    background: var(--white);
    border-radius: 12px;
    overflow: hidden;
    box-shadow: var(--card-shadow);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    display: flex;
    flex-direction: column;
}

.product-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 30px rgba(0,0,0,0.12);
}

.product-img {
    width: 100%;
    height: 260px;
    object-fit: cover;
}

.product-info {
    padding: 1.5rem;
    display: flex;
    flex-direction: column;
    flex-grow: 1;
}

.product-title {
    font-size: 1.2rem;
    font-weight: 600;
    margin-bottom: 0.5rem;
}

.product-price {
    font-size: 1.3rem;
    color: var(--primary);
    font-weight: 700;
    margin-bottom: 1rem;
}

.btn-add {
    margin-top: auto;
    background-color: transparent;
    border: 2px solid var(--primary);
    color: var(--primary);
    padding: 0.6rem 1rem;
    border-radius: 6px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
}

.btn-add:hover {
    background-color: var(--primary);
    color: var(--white);
}

/* Sección de Contacto y Pedidos */
.contact-section {
    background-color: #F4EAE1;
    padding: 4rem 2rem;
    margin-top: 4rem;
}

.contact-container {
    max-width: 800px;
    margin: 0 auto;
    text-align: center;
    background: var(--white);
    padding: 3rem 2rem;
    border-radius: 16px;
    box-shadow: var(--card-shadow);
}

.whatsapp-btn {
    background-color: #25D366;
    color: white;
    padding: 1rem 2.5rem;
    border-radius: 50px;
    font-size: 1.2rem;
    font-weight: 600;
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    gap: 12px;
    margin-top: 1.5rem;
    box-shadow: 0 4px 15px rgba(37, 211, 102, 0.3);
    transition: transform 0.3s ease, background-color 0.3s ease;
}

.whatsapp-btn:hover {
    background-color: #1EBE5D;
    transform: scale(1.05);
}

/* Footer */
footer {
    text-align: center;
    padding: 2rem;
    background-color: var(--text-dark);
    color: var(--white);
    font-size: 0.9rem;
}

/* Responsive Breakpoints */
@media (max-width: 768px) {
    .hero h1 {
        font-size: 2.2rem;
    }
    .product-grid {
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    }
}
"""

# 3. Contenido para 'script.js'
js_content = """// Lista de Productos de Doña Elena
const productos = [
    {
        id: 1,
        nombre: "Poncho Alpaca Tradicional",
        precio: 180,
        imagen: "https://images.unsplash.com/photo-1544441893-675973e31985?auto=format&fit=crop&w=600&q=80"
    },
    {
        id: 2,
        nombre: "Chalina Fina de Alpaca",
        precio: 75,
        imagen: "https://images.unsplash.com/photo-1608256246200-53e635b5b65f?auto=format&fit=crop&w=600&q=80"
    },
    {
        id: 3,
        nombre: "Chullo Arequipeño Tejido",
        precio: 45,
        imagen: "https://images.unsplash.com/photo-1576871337632-b9aef4c17ab9?auto=format&fit=crop&w=600&q=80"
    },
    {
        id: 4,
        nombre: "Manta Mística Cusqueña/Arequipeña",
        precio: 210,
        imagen: "https://images.unsplash.com/photo-1601924994987-69e26d50dc26?auto=format&fit=crop&w=600&q=80"
    }
];

let carritoCount = 0;

// Cargar productos en la cuadrícula (Grid)
function cargarProductos() {
    const gridContainer = document.getElementById('grid-productos');
    gridContainer.innerHTML = '';

    productos.forEach(prod => {
        const card = document.createElement('div');
        card.className = 'product-card';
        card.innerHTML = `
            <img src="${prod.imagen}" alt="${prod.nombre}" class="product-img">
            <div class="product-info">
                <h3 class="product-title">${prod.nombre}</h3>
                <div class="product-price">S/ ${prod.precio}.00</div>
                <button class="btn-add" onclick="agregarAlCarrito('${prod.nombre}')">
                    <i class="fa-solid fa-cart-plus"></i> Añadir a la selección
                </button>
            </div>
        `;
        gridContainer.appendChild(card);
    });
}

// Agregar al contador de carrito
function agregarAlCarrito(nombreProducto) {
    carritoCount++;
    document.getElementById('cart-count').innerText = carritoCount;
    actualizarEnlaceWhatsApp(nombreProducto);
    alert(`¡Añadido! Has seleccionado: ${nombreProducto}`);
}

// Actualizar enlace directo a WhatsApp con mensaje personalizado
function actualizarEnlaceWhatsApp(ultimoProducto) {
    const telefono = "51987654321"; // Reemplazar con el número real de Doña Elena
    const mensaje = encodeURIComponent(`¡Hola Doña Elena! Estoy interesado en comprar sus tejidos de alpaca. Me interesa especialmente el/la ${ultimoProducto}. ¿Podría darme más información para realizar la compra?`);
    document.getElementById('whatsapp-link').href = `https://wa.me/${telefono}?text=${mensaje}`;
}

function scrollToContact() {
    document.getElementById('contacto').scrollIntoView({ behavior: 'smooth' });
}

// Inicializar página
document.addEventListener('DOMContentLoaded', () => {
    cargarProductos();
    actualizarEnlaceWhatsApp('sus productos');
});
"""

# Generación física de los 3 archivos
archivos = {
    "index.html": html_content,
    "styles.css": css_content,
    "script.js": js_content
}

for nombre_archivo, contenido in archivos.items():
    with open(nombre_archivo, "w", encoding="utf-8") as file:
        file.write(contenido)
    print(f"✅ Archivo creado con éxito: {nombre_archivo}")

print("\n🎉 ¡Página dividida en HTML, CSS y JS con éxito!")