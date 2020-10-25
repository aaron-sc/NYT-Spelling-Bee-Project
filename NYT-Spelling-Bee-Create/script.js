var solveButton = document.getElementById("solveButton");
var middle = document.getElementById("middle");
var outside = document.getElementById("outside");
var statusP = document.getElementById("status");
var words = [];

var body = document.getElementById("bod");

var createG = document.getElementById("createGame");
var gameArea = document.getElementById("game");

var serverAvaliable = false;

// var hive = document.getElementById("honeycomb");

var hivecell1Text = document.getElementById("outside1");
var outsideC1 = document.getElementById("outsideCell1");

var hivecell2Text = document.getElementById("outside2");
var outsideC2 = document.getElementById("outsideCell2");

var hivecell3Text = document.getElementById("outside3");
var outsideC3 = document.getElementById("outsideCell3");

var hivecell4Text = document.getElementById("outside4");
var outsideC4 = document.getElementById("outsideCell4");

var hivecell5Text = document.getElementById("outside5");
var outsideC5 = document.getElementById("outsideCell5");

var hivecell6Text = document.getElementById("outside6");
var outsideC6 = document.getElementById("outsideCell6");

var hivecellcenterText = document.getElementById("inside");
var middleC = document.getElementById("middleCell");

var puzzleText = document.getElementById("hivePuzzleText");

var hiveActions = document.getElementById("actions");
var deleteButt = document.getElementById("deleteButton");
var enterButt = document.getElementById("enterButton");

function wait(ms){
   var start = new Date().getTime();
   var end = start;
   while(end < start + ms) {
     end = new Date().getTime();
  }
}

function updateStatus(status) {
	statusP.textContent = status;
}

function updateTextBox(toAppend){
	puzzleText.appendChild(toAppend.cloneNode(true));
}

function backspace(){
	if(puzzleText.hasChildNodes()){
		puzzleText.removeChild(puzzleText.lastChild);
	}
}

function loadPuzzle(outside1,outside2,outside3,outside4,outside5,outside6,middleLetter){
	updateStatus("Puzzle Loaded... Enjoy :)")
	wait(2000);
	actions.style.visibility = "visible";
	createG.style.visibility = "hidden";
	hivecell1Text.textContent = outside1;
	hivecell2Text.textContent = outside2;
	hivecell3Text.textContent = outside3;
	hivecell4Text.textContent = outside4;
	hivecell5Text.textContent = outside5;
	hivecell6Text.textContent = outside6;
	hivecellcenterText.textContent = middleLetter;

	// Build each letter
	var span1 = document.createElement('span');
	span1.textContent = hivecell1Text.textContent;
	outsideC1.addEventListener("click", function() {updateTextBox(span1)})

	var span2 = document.createElement('span');
	span2.textContent = hivecell2Text.textContent;
	outsideC2.addEventListener("click", function() {updateTextBox(span2)})

	var span3 = document.createElement('span');
	span3.textContent = hivecell3Text.textContent;
	outsideC3.addEventListener("click", function() {updateTextBox(span3)})

	var span4 = document.createElement('span');
	span4.textContent = hivecell4Text.textContent;
	outsideC4.addEventListener("click", function() {updateTextBox(span4)})

	var span5 = document.createElement('span');
	span5.textContent = hivecell5Text.textContent;
	outsideC5.addEventListener("click", function() {updateTextBox(span5)})

	var span6 = document.createElement('span');
	span6.textContent = hivecell6Text.textContent;
	outsideC6.addEventListener("click", function() {updateTextBox(span6)})

	var spanMiddle = document.createElement('span');
	spanMiddle.textContent = hivecellcenterText.textContent;
	spanMiddle.setAttribute("class", "sb-input-bright")
	middleC.addEventListener("click", function() {updateTextBox(spanMiddle)})
}

async function buildPuzzle(out,middle) {
	
	const response = await fetch('https://NYT-SBEE.aaronsanta.repl.co/api/create?out='+out+'&middle='+middle);
	data = await response.json();
	data = JSON.parse(JSON.stringify(data));
	words = data.words;
	updateStatus("Finished Fetching. Loading Puzzle...");
	wait(2000);
	loadPuzzle(out.charAt(0),out.charAt(1),out.charAt(2),out.charAt(3),out.charAt(4),out.charAt(5),middle.charAt(0));
}

function playGame() {
	var middleInWord = false;
	var word = "";

	var children = puzzleText.children;
	for (var i = 0; i < children.length; i++) {
		var puzzleLetter = children[i];
		if(puzzleLetter.textContent == middle.value) {
			middleInWord = true;
		}
		word += puzzleLetter.textContent;
	}

	if(puzzleText.children.length < 4) {
		alert("Length has to be at least 4!");
	}
	else if(!middleInWord){
		alert("Middle letter not in word!");
	}
	else {
		console.log(word);
		if(words.includes(word)) {
			alert("Correct!")
		}
		else {
			alert("Incorrect!")
		}
	}
}



solveButton.addEventListener("click", function() {updateStatus("Fetching Data From Server...")});
solveButton.addEventListener("click", function() {buildPuzzle(outside.value,middle.value)},false);
deleteButt.addEventListener("click", function(){backspace()})
enterButt.addEventListener("click", function(){playGame()})




