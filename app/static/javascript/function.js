function countCharacters(maxCharacters, source, target) {
  var count = document.getElementById("description").value.length;
  var counter = document.getElementById("counter");
  counter.innerText = count + " of" + " " +  maxCharacters + " " +  "characters used.";
}