document.getElementById('addItemForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const itemName = document.getElementById('itemName').value;
    const itemQuantity = document.getElementById('itemQuantity').value;

    fetch('/add-item', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name: itemName, quantity: itemQuantity })
    })
    .then(response => response.json())
    .then(data => {
        alert('物品添加成功');
        loadInventory();
    })
    .catch(error => console.error('Error:', error));
});

document.getElementById('bookItemForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const bookItemName = document.getElementById('bookItemName').value;
    const bookItemQuantity = document.getElementById('bookItemQuantity').value;

    fetch('/book-item', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name: bookItemName, quantity: bookItemQuantity })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('物品预订成功');
        } else {
            alert('预订失败，库存不足');
        }
        loadInventory();
    })
    .catch(error => console.error('Error:', error));
});

function loadInventory() {
    fetch('/inventory')
    .then(response => response.json())
    .then(data => {
        const inventoryList = document.getElementById('inventoryList');
        inventoryList.innerHTML = '';
        data.forEach(item => {
            const li = document.createElement('li');
            li.textContent = `${item.name}: ${item.quantity}`;
            inventoryList.appendChild(li);
        });
    });
}

window.onload = function() {
    loadInventory();
};