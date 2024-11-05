// // Global variable to hold orders
// let orders = [];

// // Function to fetch orders from Django and store in global variable
// function fetchOrders() {
//     fetch('/api/orders/')
//         .then(response => response.json())
//         .then(data => {
//             orders = data; // Store fetched orders in global variable
//             displayOrders(orders); // Call to display all orders initially
//         })
//         .catch(error => console.error('Error fetching orders:', error));
// }

// // Function to create and display orders
// function displayOrders(ordersToDisplay) {
//     orderContainer.innerHTML = ''; // Clear previous orders
//     ordersToDisplay.forEach(order => {
//         const orderElement = createOrderElement(order);
//         orderContainer.appendChild(orderElement);
//     });
// }

function trackOrder() {
    const orderNumber = document.getElementById('orderNumber').value.trim();
    const result = document.getElementById('result');
    result.textContent = ''; // Clear previous result

    // Check each order div for the specified order number
    const orderDivs = document.querySelectorAll('.order');
    let found = false;

    orderDivs.forEach(orderDiv => {
        const orderId = orderDiv.querySelector('h2').textContent.split(' ')[1];
        const orderStatus = orderDiv.querySelector('strong').textContent;

        if (orderId === orderNumber) {
            // Display the found order status
            result.textContent = `Order ${orderId}: ${orderStatus}`;
            found = true;
        }
    });

    if (!found) {
        result.textContent = 'Order not found. Please check the order number and try again.';
    }
    // Add any additional logic as needed
}


// // Function to create and return a DOM element for an order
// function createOrderElement(order) {
//     const orderElement = document.createElement('div');
//     orderElement.classList.add('order');
//     orderElement.id = `order-${order.id}`;
//     let itemsHtml = order.items.map(item => `
//         <li>
//             <img src="${item.fooditem.fooditemImage}" alt="${item.fooditem.name}" style="width:100px; height:auto;">
//             ${item.fooditem.name} - Quantity: ${item.quantity}
//         </li>
//     `).join('');
//     orderElement.innerHTML = `
//         <h2>Order ${order.id}</h2>
//         <p><strong>Status:</strong> ${order.status}</p>
//         <div class="order-items">
//             <h4>Items:</h4>
//             <ul>
//                 ${itemsHtml}
//             </ul>
//         </div>
//     `;
//     return orderElement;
// }

// // Initial call to fetch orders when the page loads
// document.addEventListener('DOMContentLoaded', fetchOrders);
