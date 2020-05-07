const goBack = function() {
    window.history.back();
  }
  document.getElementById("backBtn").onclick = function (){
    goBack();  
  }
  
  players = document.querySelectorAll(".players")

  const change = function() {
    if (this.classList.contains("booked")) {
      alert("already booked");
      console.log("already booked");
    }
    else {
      this.src = '/static/img/user (2).png';
      this.classList.add("booked");
    }
  }

  for (i=0; i<4; i++) {
    players[i].onclick = change
  }

 

