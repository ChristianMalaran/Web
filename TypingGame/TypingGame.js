//<p>sad</p>

var score = 0;
var random_string = Math.random(2).toString(36).substring(2, 15);
var y_axis_drop = 50;
var adjust = document.getElementById("dropname")
adjust.style.position = "absolute";

function delay(){
    setTimeout(function(){typed.call()},50)
}	

function typed(){

    if (document.getElementById("input").value == random_string){
        random_string = Math.random(2).toString(36).substring(2, 15); 
        y_axis_drop = 50
        document.getElementById("input").value = ""
        delay.call();
        score++
    }
    if (y_axis_drop>515){
        window.alert("Game Over!")
        adjust.innerHTML = ""
        
    }else{
        
    document.getElementById("scoreId").innerHTML = "SCORE: " + score
    adjust.innerHTML = random_string
    adjust.style.top = y_axis_drop + "px";
    y_axis_drop++
    delay.call()

    }
}


