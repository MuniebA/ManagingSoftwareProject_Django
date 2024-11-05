// Sample orders
const orders = [
    {
        id: 1,
        name: "Order 1",
        estimatedDelivery: "April 10, 2023",
        placementDate: "April 3, 2023"
    },
    {
        id: 2,
        name: "Order 2",
        estimatedDelivery: "April 15, 2023",
        placementDate: "April 5, 2023"
    },
    // Add more orders here
];

const orderContainer = document.querySelector(".order-container");

// Function to create and display orders
function displayOrders() {
    orderContainer.innerHTML = ""; // Clear previous orders
    orders.forEach(order => {
        const orderElement = document.createElement("div");
        orderElement.classList.add("order");
        orderElement.innerHTML = `
            <h2>${order.name}</h2>
            <p><strong>ID:</strong> ${order.id}</p>
            <p><strong>Estimated Delivery Date:</strong> ${order.estimatedDelivery}</p>
            <p><strong>Order Placement Date:</strong> ${order.placementDate}</p>
            <div class="order-bar">
                <div class="stage">Order Placed</div>
                <div class="stage">Order Received</div>
                <div class="stage">In Process</div>
                <div class="stage">Order Shipped</div>
                <div class="stage">Order Delivered</div>
            </div>
            <p class="order-description">Description for the current stage.</p>
        `;
        orderContainer.appendChild(orderElement);
    });
}

// Call the displayOrders function to initially display all orders
displayOrders();

// Function to track an order (search by ID)
function trackOrder() {
    const orderNumber = document.getElementById("orderNumber").value;
    const result = document.getElementById("result");
    const foundOrder = orders.find(order => order.id.toString() === orderNumber);
    if (foundOrder) {
        result.textContent = `Order ${foundOrder.id}: ${foundOrder.name} - Estimated Delivery: ${foundOrder.estimatedDelivery}`;
        // Hide all other orders
        const allOrders = document.querySelectorAll(".order");
        allOrders.forEach(order => {
            if (order.id !== `order-${foundOrder.id}`) {
                order.style.display = "none";
            }
        });
    } else {
        result.textContent = "Order not found";
    }
}
