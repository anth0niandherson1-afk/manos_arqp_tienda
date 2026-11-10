// Lista de Productos de Doña Elena
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
