let display=document.getElementById("display");
function clearDisplay() {
    display.value = "";
}
function deletePrevious() {
    const expression=display.value.slice(0,-1);
    display.value = expression;
}

function appendToDisplay(value) {
    display.value += value;

}
function calculate(){
    const input=display.value;
    let result;

    if(input.includes("+")){
        const [a,b]= input.split("+");
        result= Number(a)+Number(b);
    }
    else if(input.includes("-")){
        const parts=input.split("-");
        const a=parts[0];
        const b=parts[1];
        result=a-b;//js automatically converts type for -,* and / but not + as string concatenation is a thing
    }
    else if(input.includes("*")){
        const [a,b]= input.split("*");
        result= Number(a)*Number(b);
    }
    else if(input.includes("/")){
        const [a,b]= input.split("/");
        if(Number(b)==0){
            result= "Error";
        }
        else{result= Number(a)/Number(b);}
    }
    else if(input.includes("%")){
        const [a,b]= input.split("%");
        result= Number(a)%Number(b);
    } else{
        result= "Invalid expressions";
    }
    display.value=result;
}