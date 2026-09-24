// clicking on 'Show more' button will make it disappear
function hide(){
    let button = document.querySelector("#showMore")
    button.remove();
}

//clicking on the image with the mouse will change it
var Img = document.querySelector(".bluesuper-car")
function changeImg(){

        Img.src = "./assets/blue-super-car.png"

} 

function decrease(sajeda){
    var decrNum = document.querySelector(sajeda)
    let int = parseInt(decrNum.innerText)
    var num = int - 1;
    decrNum.innerText = num;
}




// function greet(test1, test2){
//     console.log("hello"+ test1 + "my "+ test2)
// }
//  greet("sajeda",4);

function changeText(){
    let string = document.querySelector("#text")
    string.innerHTML =  newParagraph();
}

function newParagraph(){
    const newParag = "<p> I had a great experience at the car wash. The service wos quick and efficient, and my car was cleaned thoroughly with attention to detail. The staff were professional and committed to providing the best service possible. Additionally, the prices were reasonable considering the quality of the work. I will definitely be coring back and would recommend this car wash to anyone looking for excellent service. </p>                                                                      ";
    return newParag;

}