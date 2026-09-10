var likes = document.querySelector("div label")

function increase(){
    let int = parseInt(likes.innerText)
    var num  = int + 1
    likes.innerText = num + " like(s)"
}

