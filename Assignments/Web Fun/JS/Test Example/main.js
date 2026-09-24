var divs = [`<div class="card">
<img src="./static/iphone.jpg" alt="Smartphone X">
<h3>Smartphone X</h3>
<p>Latest generation smartphone with AI camera and stunning display.</p>
<div class="price">$999</div>
<button class="buy-btn">Buy Now</button>
</div>`,
    `<div class="card">
<img src="./static/laptop.jpg" alt="Laptop Pro">
<h3>Laptop Pro</h3>
<p>Powerful and lightweight laptop for professionals on the go.</p>
<div class="price">$1499</div>
<button class="buy-btn">Buy Now</button>
</div>`,
    `<div class="card">
<img src="./static/watch.jpg" alt="Smartwatch S">
<h3>Smartwatch S</h3>
<p>Track your fitness and stay connected with this sleek smartwatch.</p>
<div class="price">$299</div>
<button class="buy-btn">Buy Now</button>
</div>
`,
    `<div class="card">
<img src="./static/headphones.jpg" alt="Headphones Z">
<h3>Headphones Z</h3>
<p>Immersive sound quality with noise-cancelling technology.</p>
<div class="price">$199</div>
<button class="buy-btn">Buy Now</button>
</div>`];
var d = document.querySelector(".cards")
var i = 0;
function add() {
    if (i < divs.length) {
        d.innerHTML += divs[i]
        i++
    }
    else {
        i = 0;
    }
}
var isdown = false;
var startX;
var card;
var cards = d.children;
var index;
d.onmousedown = function (e) {
    card = e.target;
    if (card.className == "buy-btn") {
        return;
    }
    isdown = true;
    startX = e.clientX;
    if (card.className != "card") {
        card = card.parentElement;
    }
    index = Array.from(cards).indexOf(card);
}

var move = 0;
d.onmousemove = function (e) {
    if (isdown) {
        move = e.clientX - startX;
        card.style.transform = "translateX(" + move + "px)";

    }
}
d.onmouseup = function () {
    if (!card) {
        return;
    }
    var next = cards[index + 1];
    var prev = cards[index - 1];
    if (move > 100) {
        if (next) {
            d.insertBefore(next, card);
        }
    }
    if (move < -100) {
        if (prev) {
            d.insertBefore(card, prev);
        }
    }

    card.style.transform = "translateX(0px)";
    move = 0;
    isdown = false;
    card = null;
}