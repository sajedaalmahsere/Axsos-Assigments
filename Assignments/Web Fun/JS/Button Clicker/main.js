function Remove(element){
    element.remove();
}


function Change(button){
    button.textContent = "Logout";
    
    if (button.textContent == "Logout"){
        button.textContent = "Login";
        console.log(button)
    }
}



function showAlert(){
    alert("ninja was liked");
}