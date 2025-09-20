



const textElement = document.querySelector(".aboutCon p.title2");
const text = textElement.textContent;
textElement.textContent = "I'm ";
let i = 0;

function typeWriter() {
  if (i < text.length) {
    textElement.textContent += text.charAt(i+3);
    i++;
    setTimeout(typeWriter, 100);
  }
}
typeWriter();