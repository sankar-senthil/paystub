function emptyp() {
    var select = document.getElementById('ET');
    var value = select.options[select.selectedIndex].value;
    if (value == 'Contractor') {
        var output = 0
        alert("All Deductions Will Become Zero...!");
    } else {
        var output = null
    }

    // if (document.getElementById("FtT").value)
    document.getElementById("FMT").value = output;
    document.getElementById("FMY").value = output;
    document.getElementById("FSST").value = output;
    document.getElementById("FSSY").value = output;
    document.getElementById("FtT").value = output;
    document.getElementById("FtY").value = output;
    document.getElementById("StT").value = output;
    document.getElementById("StY").value = output;

}

function lasthide() {
    var x = document.getElementById("ALYTD").checked;

    if (x == true) {
        output = "block";

    } else {
        output = "none";
    }
    console.log(output)
    document.getElementById("Last").style.display = output
    document.getElementById("Last1").style.display = output
        // document.getElementById("Last2").style.display = output
        // document.getElementById("Last3").style.display = output
        // // document.getElementById("Last4").style.display = output
}