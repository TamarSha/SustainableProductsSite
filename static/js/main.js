// JavaScript source code


function update_cart_value() {
    document.getElementById('cart').innerHTML = document.getElementById('inputQuantity').value;
}

function use_selected_item() {
    var selected_id = localStorage.param;
    document.getElementById('itemID').innerHTML = "Item ID#: " + selected_id;
}

function store_cart_items() {
    localStorage.setItem("CartItems", cart_items);
    // window.alert(cart_items[0]);
}

function myFunc(data) {
    // window.alert(data);
    //cart_items.push(2);
    //cart_items.push(4);
    //cart_items.push(6);
    return cart_items = localStorage.getItem("CartItems")[0]
}

