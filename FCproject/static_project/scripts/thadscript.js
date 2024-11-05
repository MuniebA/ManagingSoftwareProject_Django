const searchInput = document.getElementById('searchbar');
const divs = document.querySelectorAll('.maincon');
const priceFilter = document.getElementById('priceFilter');

searchInput?.addEventListener('input', function () {
    const searchTerm = searchInput.value.toLowerCase();

    divs.forEach(function (div) {
        const text = div.textContent.toLowerCase();
        if (text.includes(searchTerm)) {
            div.classList.remove('hide');
        } else {
            div.classList.add('hide');
        }
    });
});


priceFilter.addEventListener('change', filterProducts);

function filterProducts() {
    const selectedOption = priceFilter.value;

    divs.forEach(function (divs) {
        const price = parseFloat(divs.getAttribute('data-price'));
        const categories = divs.getAttribute('data-categories');

        if (selectedOption === 'all') {
            divs.classList.remove('hide');
        } else if (selectedOption === 'under10' && price < 10) {
            divs.classList.remove('hide');
        } else if (selectedOption === '10to20' && price >= 10 && price <= 20) {
            divs.classList.remove('hide');
        } else if (selectedOption === 'above20' && price > 20) {
            divs.classList.remove('hide');
        } else if (selectedOption === 'feature' && categories === 'featured') {
            divs.classList.remove('hide');
        } else if (selectedOption === 'budget' && categories === 'budget') {
            divs.classList.remove('hide');
        } else {
            divs.classList.add('hide');
        }
    });
}

// Darren Part
<<<<<<< HEAD:main/Scripts/cateringSystem/scripts/thadscript.js
function opencard(){
    document.querySelector('.card2').style.left = "75%";
}

function closecard(){
	document.querySelector('.card2').style.left = "100%";
}


function Addcart(picture,item_name,item_price){
    let quantity = document.querySelector('.quantity');
    quantity.innerHTML ++;
    let count=0;
    //if statement to execute the appendchild function
    count ++;//if count > 1 then appendchild function dont work just increase count
    
    
    let image = document.createElement("img");
    image.setAttribute("src",picture );
    image.setAttribute("width", "100");
    image.setAttribute("height", "100");
    image.style.borderRadius="8px";
    let name = document.createElement("p");
    name.innerHTML = item_name;
    name.style.color = "black";
    let price = document.createElement("p");
    price.innerHTML = item_price;
    price.style.color = "black";
    let div = document.createElement("div");
    div.appendChild(name);
    div.appendChild(price);
    div.style.height = "5%";
    let increase = document.createElement("button");
    increase.innerHTML = "+";
    increase.addEventListener("click",function(){
        number.innerHTML ++;
        quantity.innerHTML ++;
    })
    increase.style.width = "5%";
    let number = document.createElement("span");
    number.innerHTML = 1;
    let decrease = document.createElement("button");
    decrease.innerHTML = "-";
    decrease.addEventListener("click",function(){
        if(number.innerHTML > 1){
            number.innerHTML --;
            quantity.innerHTML -=count;
        }else{
            document.querySelector('#listcard').removeChild(list);
            quantity.innerHTML --;
        }
    })
    decrease.style.width = "5%";
    let remove = document.createElement("button");
    remove.innerHTML = "Remove";
    remove.addEventListener("click", function() {
         document.querySelector('#listcard').removeChild(list);
         quantity.innerHTML -= count;
    });
    remove.style.background= "#EEE3CB";
    remove.style.border="1px solid #EEE3CB";
=======
function opencard() {
    document.querySelector('.card2').style.left = "75%";
}

function closecard() {
    document.querySelector('.card2').style.left = "100%";
}

function Addcart1() {
    let quantity = document.querySelector('.quantity');
    quantity.innerHTML++;

    let count = 0;
    count++;

    let image = document.createElement("img");
    image.setAttribute("src", "Image/item1.jpg");
    image.setAttribute("width", "100");
    image.setAttribute("height", "100");
    let name = document.createElement("span");
    name.innerHTML = "Energized Day";
    name.style.color = "black";
    let price = document.createElement("span");
    price.innerHTML = " RM 15.50";
    price.style.color = "black";
    let remove = document.createElement("button");
    remove.innerHTML = "Remove";
    remove.addEventListener("click", function () {
        document.querySelector('#listcard').removeChild(list);
        quantity.innerHTML -= count;
    });
    remove.style.background = "#EEE3CB";
    remove.style.border = "1px solid #EEE3CB";
>>>>>>> MinKhant:FCproject/static_project/scripts/thadscript.js
    remove.style.borderRadius = "20px";

    let list = document.createElement("li");
    list.appendChild(image);
<<<<<<< HEAD:main/Scripts/cateringSystem/scripts/thadscript.js
    list.appendChild(div);
    list.appendChild(increase);
    list.appendChild(number);
    list.appendChild(decrease);
    document.querySelector('#listcard').appendChild(list);
    
}
=======
    list.appendChild(name);
    list.appendChild(price);
    list.appendChild(remove);
    document.querySelector('#listcard').appendChild(list);

}

function Addcart2() {
    let quantity = document.querySelector('.quantity');
    quantity.innerHTML++;

    let count = 0;
    count++;

    let image = document.createElement("img");
    image.setAttribute("src", "Image/item2.jpg");
    image.setAttribute("width", "100");
    image.setAttribute("height", "100");
    let name = document.createElement("span");
    name.innerHTML = "Luxury Set";
    name.style.color = "black";
    let price = document.createElement("span");
    price.innerHTML = " RM 19.90";
    price.style.color = "black";
    let remove = document.createElement("button");
    remove.innerHTML = "Remove";
    remove.addEventListener("click", function () {
        document.querySelector('#listcard').removeChild(list);
        quantity.innerHTML -= count;
    });
    remove.style.background = "#EEE3CB";
    remove.style.border = "1px solid #EEE3CB";
    remove.style.borderRadius = "20px";

    let list = document.createElement("li");
    list.appendChild(image);
    list.appendChild(name);
    list.appendChild(price);
    list.appendChild(remove);
    document.querySelector('#listcard').appendChild(list);

}
>>>>>>> MinKhant:FCproject/static_project/scripts/thadscript.js
