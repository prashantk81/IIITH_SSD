// to password check it is matched or not//
function passchecker(){
    var password = document.getElementById("password")
  , confirm_password = document.getElementById("confirm_password");

  if(password.value != confirm_password.value) {
    confirm_password.setCustomValidity("Passwords Don't Match");
  } else {
    confirm_password.setCustomValidity('');
  }
}

// switch between dark mode and light mode
function dark() {
    var element = document.body;
    element.classList.toggle("dark-mode");
 }


window.addEventListener('keypress', (e) => {
    console.log(e)
    if (e.ctrlKey && e.code == 'KeyM') {
        dark();
    }
});
//drag and drop
 function dragStartHandler(event) {
    event.dataTransfer.setData('draggedElementId', event.target.id);
  }
  
  function dragOverHandler(event) {
    event.preventDefault();
  }
  
  function dropHandler(event) {
    event.preventDefault();
  
    var elementId = event.dataTransfer.getData('draggedElementId');
    event.target.appendChild(document.getElementById(elementId));
}


function submitbtn() {
    var unamename = document.getElementById("name").value;
    var mail = document.getElementById("email").value;
    var name = document.getElementById("username").value;
    var lead = document.getElementById("lead").value;
    var member = document.getElementById("tmm").value;

    alert("Name : " + unamename + " \n email:   " + mail + " \n  username: " + name + " \n teamlead: " + lead + " \n team-member:  " + member);

}