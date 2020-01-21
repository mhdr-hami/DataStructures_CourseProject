var n = 0;
let helpText = ["Hey!",
    "I’m the Matrix.",
    "My task is analysing the dataset you gave me in 4 phases.",
    "In the first phase I read your dataset.",
    "In the second phase I check if there exists any person who’s job is at “گمرک” or “سازمان بنادر” and him o her family has bought something worthy in the past 2 years.",
    "In the third phase I check if suspected persons from phase two has a bank transaction connection with “قاچاقچی” persons! The length of this path must be shorter than 6!",
    "And in the last phase I check if phase three suspected ones has called “قاچاقچی” persons.",
    "You can ask me to show you the results of any phase you want.",
    "Hint: Show me phase 2.",
    "Click to Start:)"];
let t = "Hello kjadhbjb m, .";
let i = 0;
let j = 0;
let timer;
function printHelp(x) {
    timer = setInterval(function () {
        let lastText = document.getElementById("loader").innerHTML;
        console.log(typeof lastText);
        console.log(lastText);
        document.getElementById("loader").innerHTML = lastText.replace("_", "") + x[i][j] + "_";
        j++;
        if (j == x[i].length) {
            j = 0;
            i++;
            document.getElementById("loader").innerHTML = document.getElementById("loader").innerHTML.replace("_", "") + "<br><br>";
        }
    }, 50);

}

$(document).ready(function () {
    printHelp(helpText);
    $("#loader").click(function () {
        $("#divLoader").fadeOut();
        clearInterval(timer);
        $('input').focus();
    });
        document.body.style.visibility = "visible";

    cursor = window.setInterval(function () {
        if ($('#cursor').css('visibility') === 'visible') {
            $('#cursor').css({
                visibility: 'hidden'
            });
        } else {
            $('#cursor').css({
                visibility: 'visible'
            });
        }
    }, 460);
    cursorReady();
    $(document).keydown(function (e) {
        if (e.keyCode == 13) {
            var command = document.getElementById("s1").innerHTML;
            document.getElementById("command").value = "";
            document.getElementById("logInput").style.display = "block";

            if(n == 0){
                document.getElementById("logInput").innerHTML = document.getElementById("logInput").innerHTML + command;
                n = parseInt(n) + 1;
            }else{
                document.getElementById("logInput").innerHTML = document.getElementById("logInput").innerHTML + "<br>" + command;
                n = parseInt(n) + 1;
            }
            let faaz = whatTheFaz($("#s1").text());
            if(faaz == -1 || faaz == -3)
            {
                n = 0;
            }
            printFaz(faaz);
        }
      });
});