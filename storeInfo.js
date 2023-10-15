function getInfo() {
    var array = [];
    array[0] = document.getElementById("major").value;
    array[1] = document.getElementById("hometown").value;
    array[2] = document.getElementById("interests").value;
    array[3] = document.getElementById("high school").value;
    array[4] = document.getElementById("housing").value;
    array[5] = document.getElementById("name").value;
    var fileName = array[5].toString() + ".txt"
}