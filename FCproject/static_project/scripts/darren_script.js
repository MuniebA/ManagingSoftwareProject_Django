<<<<<<< HEAD:main/Scripts/cateringSystem/scripts/darren_script.js
let opencart = document.querySelector('.cart');
let closecart = document.querySelector('.closecart');
let list = document.querySelector('.list');
let listcard = document.querySelector('.listcard');
let body = document.querySelector('body');
let total = document.querySelector('.total');
let quantity = document.querySelector('.quantity');

opencart.addEventListener('click', ()=>{
    body.classList.add('active');
})

closecart.addEventListener('click', ()=>{
    body.classList.remove('active');
})

let products = [
    {
        id:1,
        name: 'PRODUCT NAME 1',
        image: 'Coffee.jpeg',
        price: 120000
    },
    {
        id:2,
        name: 'PRODUCT NAME 3',
        image: 'Tea.jpg',
        price: 240000
    },
    {
        id:3,
        name: 'PRODUCT NAME 3',
        image: 'hotChocolate.jpg',
        price: 320000
    },
    {
        id:4,
        name: 'PRODUCT NAME 4',
        image: 'matcha.jpg',
        price: 150000
    },
    {
        id:5,
        name: 'PRODUCT NAME 5',
        image: 'Croissants.jpg',
        price: 180000
    },
    {
        id:6,
        name: 'PRODUCT NAME 6',
        image: 'PancakeStack.jpg',
        price: 160000
    }
];

let listcards = [];

function intWeb(){
     products.forEach((value,key)=>{
        let newDiv = document.createElement('div');
        newDiv.classList.add('item');
        newDiv.innerHTML = `
            <img src="image/${value.image}"/>
            <div class="title">${value.name}</div>
            <div class="price">${value.price}</div>
            
            <button onclick="addToCard(${key})">Add To Card</button>
        `;list.appendChild(newDiv);
     })
}intWeb();

function addToCard(key){
    if(listcards[key] == null){
        listcards[key] = products[key];
        listcards[key].quantity = 1;
    }
    reloadCard();
}

function reloadCard(){
    listcard.innerHTML = '';
    let count = 0;
    let totalprice = 0;
    listcards.forEach((value,key) =>{
        totalprice = totalprice + value.price;
        count = count + value.quantity;

        if(value!=null){
            let newDiv = document.createElement('li');
            newDiv.innerHTML = `
                <div><img src = "image/${value.image}"/></div>
                <div>${value.name}</div>
                <div>${value.price}</div>
                <div>
                    <button onclick="removeQuantity(${key},${value.quantity - 1})">-</button>
                    <div class = "count">${value.quantity}</div>
                    <button onclick = "addQuantity(${key},${value.quantity + 1})">+</button>
                </div>
            `;
            listcard.appendChild(newDiv);
            
        }
       
    })
    total.innerHTML = totalprice.toLocaleString();
    quantity.innerHTML = count;
    
}

function addQuantity(key,quantity){
    if(quantity == 0){
        delete listcards[key];
    }else{
        listcards[key].quantity = quantity;
        listcards[key].price = quantity * products[key].price;
    }
    reloadCard();
    
}

function removeQuantity(key,quantity){
    if(quantity == 0){
        delete listcards[key];
    }else{
        listcards[key].quantity = quantity;
        listcards[key].price = quantity * products[key].price;
    }
    reloadCard();
=======
let opencart = document.querySelector('.cart');
let closecart = document.querySelector('.closecart');
let list = document.querySelector('.list');
let listcard = document.querySelector('.listcard');
let body = document.querySelector('body');
let total = document.querySelector('.total');
let quantity = document.querySelector('.quantity');

opencart.addEventListener('click', ()=>{
    body.classList.add('active');
})

closecart.addEventListener('click', ()=>{
    body.classList.remove('active');
})

let products = [
    {
        id:1,
        name: 'PRODUCT NAME 1',
        image: 'Coffee.jpeg',
        price: 120000
    },
    {
        id:2,
        name: 'PRODUCT NAME 3',
        image: 'Tea.jpg',
        price: 240000
    },
    {
        id:3,
        name: 'PRODUCT NAME 3',
        image: 'hotChocolate.jpg',
        price: 320000
    },
    {
        id:4,
        name: 'PRODUCT NAME 4',
        image: 'matcha.jpg',
        price: 150000
    },
    {
        id:5,
        name: 'PRODUCT NAME 5',
        image: 'Croissants.jpg',
        price: 180000
    },
    {
        id:6,
        name: 'PRODUCT NAME 6',
        image: 'PancakeStack.jpg',
        price: 160000
    }
];

let listcards = [];

function intWeb(){
     products.forEach((value,key)=>{
        let newDiv = document.createElement('div');
        newDiv.classList.add('item');
        newDiv.innerHTML = `
            <img src="image/${value.image}"/>
            <div class="title">${value.name}</div>
            <div class="price">${value.price}</div>
            
            <button onclick="addToCard(${key})">Add To Card</button>
        `;list.appendChild(newDiv);
     })
}intWeb();

function addToCard(key){
    if(listcards[key] == null){
        listcards[key] = products[key];
        listcards[key].quantity = 1;
    }
    reloadCard();
}

function reloadCard(){
    listcard.innerHTML = '';
    let count = 0;
    let totalprice = 0;
    listcards.forEach((value,key) =>{
        totalprice = totalprice + value.price;
        count = count + value.quantity;

        if(value!=null){
            let newDiv = document.createElement('li');
            newDiv.innerHTML = `
                <div><img src = "image/${value.image}"/></div>
                <div>${value.name}</div>
                <div>${value.price}</div>
                <div>
                    <button onclick="removeQuantity(${key},${value.quantity - 1})">-</button>
                    <div class = "count">${value.quantity}</div>
                    <button onclick = "addQuantity(${key},${value.quantity + 1})">+</button>
                </div>
            `;
            listcard.appendChild(newDiv);
            
        }
       
    })
    total.innerHTML = totalprice.toLocaleString();
    quantity.innerHTML = count;
    
}

function addQuantity(key,quantity){
    if(quantity == 0){
        delete listcards[key];
    }else{
        listcards[key].quantity = quantity;
        listcards[key].price = quantity * products[key].price;
    }
    reloadCard();
    
}

function removeQuantity(key,quantity){
    if(quantity == 0){
        delete listcards[key];
    }else{
        listcards[key].quantity = quantity;
        listcards[key].price = quantity * products[key].price;
    }
    reloadCard();
>>>>>>> MinKhant:FCproject/static_project/scripts/darren_script.js
}