function concatMail(user){
    var part1 = user;
    var part2 = Math.pow(2,6);
    var part3 = String.fromCharCode(part2);
    var part4 = "pl.hanze.nl";
    var part5 = part1 + String.fromCharCode(part2) + part4;
    var resString = "<a href=" + "mai" + "lto" + ":" + part5 + ">" + part1 + part3 + part4 + "</a>";
    return resString;
}


//var name = 'j.hageman'
//res = concatMail(name);
//console.log(res);