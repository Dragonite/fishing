// This function is for counting the amount of characters left to use in a TextField. It uses DOM to modify an
// existing target's innerHTML, so that on every new input, the value is dynamically rendered onto the screen.
// inputs: maxCharacters, source, target.
// - maxCharacters: the maximum amount of characters you want the textArea to have.
// - source: The textArea element of which you are analysing the length of.
// - target: The target text tag that displays the text.
function countCharacters(maxCharacters, source, target) {
  var count = document.getElementById(source).value.length;
  var counter = document.getElementById(target);
  counter.innerText = count + " of" + " " +  maxCharacters + " " +  "characters used.";
}

function handleClick() {
  alert("clicked!")
}