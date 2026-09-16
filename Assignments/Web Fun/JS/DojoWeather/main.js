function show(element) {
    alert("showing weather for " + element.innerText)
}

function hide() {
    var foot = document.querySelector("footer")
    foot.remove();
}

// function convertTemp(){
//     var unit = document.querySelector("#temperature");
//     var lowtemparr = document.querySelectorAll(".low")
//     var hightemparr = document.querySelectorAll(".high")
//     if(unit.value == "Fahrenheit"){
//         //iterate all the array and send values to cl to feh function
//         console.log(lowtemparr.length)

//         for ( var i =0 ; i< lowtemparr.length ; i++){
//             var fih = fromCltoFeh(lowtemparr[i].value)
//             lowtemparr[i].innerText = fih

//             var fih = fromCltoFeh(hightemparr[i].value)
//             hightemparr[i].innerText = fih
//         }
//     }
//     else{  
//        // console.log("@@@ sajeda2")
//         for ( var i =0 ; i< lowtemparr.length ; i++){
//             var cel = fromFehtoCl(lowtemparr[i].value)
//             lowtemparr[i].innerText = cel

//             var cel = fromFehtoCl(hightemparr[i].value)
//             hightemparr[i].innerText = cel
//         }
//     }


//     // var fahrenheit = (convert.innerText * 9 / 5) + 32;
//     // convert.innerText= fahrenheit
//     // var celsius = (fahrenheit - 32) * 5 / 9;
    
//     // // if(unit === "Fahrenheit"){
//     // //     fahrenheit.convert()
//     // // }
//     // var convert = document.querySelector("h4")
//     // console.log(convert.innerHTML)
    


// }

// function fromCltoFeh (cel){
//     let mycel = parseInt (cel)
//     var fahrenheit = (mycel * 9 / 5) + 32;
//     //console.log("test123"+fahrenheit)
//     return fahrenheit ;
// }


// function fromFehtoCl (feh){
//     let myfeh = parseInt (feh)
//     var celsius = (myfeh - 32) * 5 / 9;
//     //console.log("test"+celsius)
//     return celsius;
// }



function convertTemp() {
    var unit = document.querySelector("#temperature");
    var lowtemparr = document.querySelectorAll(".low");
    var hightemparr = document.querySelectorAll(".high");

    if (unit.value == "Fahrenheit") {

        for (var i = 0; i < lowtemparr.length; i++) {
            var fih = fromCltoFeh(lowtemparr[i].innerText);
            lowtemparr[i].innerText = fih;

            var fih = fromCltoFeh(hightemparr[i].innerText);
            hightemparr[i].innerText = fih;
        }

    } else {

        for (var i = 0; i < lowtemparr.length; i++) {
            var cel = fromFehtoCl(lowtemparr[i].innerText);
            lowtemparr[i].innerText = cel;

            var cel = fromFehtoCl(hightemparr[i].innerText);
            hightemparr[i].innerText = cel;
        }
    }
}

function fromCltoFeh(cel) {
    let mycel = parseFloat(cel);
    var fahrenheit = (mycel * 9 / 5) + 32;
    return fahrenheit.toFixed(1);
}

function fromFehtoCl(feh) {
    let myfeh = parseFloat(feh);
    var celsius = (myfeh - 32) * 5 / 9;
    return celsius.toFixed(1);
}