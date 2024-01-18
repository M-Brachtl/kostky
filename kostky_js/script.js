const dices = document.getElementsByClassName('playingDice'); // playing dice
const throwDice = document.getElementById('throw') // throw the dice button
const media = ['kostka_1.png','kostka_2.png','kostka_3.png','kostka_4.png','kostka_5.png','kostka_6.png']
const pointsShow = document.getElementById('points-show') // line with points number of current choice
const newTurn = document.getElementById('new-turn') // button for new turn
const pointsTurn = document.getElementById('points-turn') // line with points number of current turn
const pointsTotal = document.getElementById('points-total') // line with points number in total
let kostky = 6
let points
let selectedDice = Array(); // selected dice
const limitPoints = document.getElementById('limit')

function countPoints(countedDice=[]){
    let body_vyberu = 0;
    if (countedDice.toString() === "1,2,3,4,5,6") {
        body_vyberu = 1500;
        countedDice = [];
    } else {
        for (let i = 1; i <= 6; i++) {
            if (countedDice.filter(x => x === i).length >= 3) {
                body_vyberu += (countedDice.filter(x => x === i).length - 2) * [1000, 200, 300, 400, 500, 600][i - 1];
                countedDice = countedDice.filter(x => x !== i);
            }
        }
        // stovky
        body_vyberu += 100*countedDice.filter(x => x === 1).length;
        countedDice = countedDice.filter(x => x !== 1);
    
        // padesatky
        body_vyberu += 50*countedDice.filter(x => x === 5).length;
        countedDice = countedDice.filter(x => x !== 5);
        
    }
    if (countedDice.length === 0){
        return body_vyberu
    }else{
        return 0
    }
    
}
function endTurn(addedPoints){
    if(addedPoints === -1 || !parseInt(pointsShow.innerHTML) || parseInt(pointsShow.innerHTML)+addedPoints < parseInt(limitPoints.value)){ addedPoints = 0; }else{
        addedPoints += countPoints(selectedDice);
    };
    pointsTotal.innerHTML = parseInt(pointsTotal.innerHTML) + addedPoints;
    selectedDice.splice(0,selectedDice.length)
    pointsShow.innerText = 0
    pointsTurn.innerText = 0
    for (let index = 0; index < dices.length; index++) {
            
        dices[index].hidden = false
        dices[index].id = "non-selected"
        dices[index].src = "media/" + media[Math.floor(Math.random()*6)]
        
    }
    kostky = 6;
}

for (let index = 0; index < dices.length; index++) {
    dices[index].id = "non-selected";
    dices[index].addEventListener('click',()=>{
        if(dices[index].id !== "selected"){
            dices[index].id = "selected";
            selectedDice.push(media.indexOf(dices[index].src.slice(-12)) + 1)
        }else{
            dices[index].id = "non-selected";
            selectedDice.splice(selectedDice.indexOf(media.indexOf(dices[index].src.slice(-12)) + 1),1)
        };
        //console.log(selectedDice) // debugging
        pointsShow.innerText = countPoints(selectedDice)
    });
    dices[index].src = "media/" + media[Math.floor(Math.random()*6)]
    
};

throwDice.addEventListener('click',()=>{
    if(parseInt(pointsShow.innerHTML) === 0){
        endTurn(-1);
    }else{
        pointsTurn.innerHTML = parseInt(pointsTurn.innerHTML) + parseInt(pointsShow.innerHTML)
        pointsShow.innerText = 0
        selectedDice.splice(0,selectedDice.length)
        toSix = false;
        for (let index = 0; index < dices.length; index++) {
            
            if(dices[index].id === "selected"){
                dices[index].hidden = true
                kostky --;
            }
            dices[index].id = "non-selected"
            dices[index].src = "media/" + media[Math.floor(Math.random()*6)]
            
        }
        if (kostky === 0){
            for (let index = 0; index < dices.length; index++) {
                dices[index].hidden = false
            }
            kostky = 6;
        }
    }
})



