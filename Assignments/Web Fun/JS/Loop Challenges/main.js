function getOddNumbers() {
    var oddNum = [];

    for (var i = 1; i < 20; i++) {
        if (i % 2 !== 0) {
            oddNum.push(i);
        }
    }

    return oddNum;
}

console.log(getOddNumbers());

function getMultpliesOf3(){
    var multpliesOf3 =[];
    for(var i=100; i>0; i--){
        if(i%3 == 0){
        multpliesOf3.push(i);
    }
} return  multpliesOf3;
}

console.log (getMultpliesOf3());

function sequence(){
    var seq =[];
    for(var i =4; i>= -3.5; i-=1.5){
        seq.push(i);
    } return seq;
} 

console.log (sequence());

function sigma(){
    var sum = 0;
    for(var i=1; i<=100; i++){
        sum = sum + i;
    } return sum;
}
console.log (sigma());

function factorai(){
    var result = 1;
    for(var i = 1; i<=12; i++){
        result = result * i;
    } return result;
} console.log(factorai());