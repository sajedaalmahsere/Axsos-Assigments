/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function(s) {
    for (var i = 0; i<s.length; i++){
        let flag = false;
        for (var j = 0; j<s.length; j++){
            if (i!=j && s[i] === s[j]){
                flag=true
                break
            }   
        }
    if (flag === false){
        return i;
            }
    }
    return -1;
};