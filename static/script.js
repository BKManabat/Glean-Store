function login(e) {
  e.preventDefault();
  $.ajax({
      type: 'POST',
      url: 'https://Glean-Store.marcovisaya.repl.co/verify',
      data: {
          'username': document.getElementById("loginUsername").value,
          'password': document.getElementById("loginPassword").value
      },
      success: function (data) {
        console.log("Logged In")
        window.location.href = "https://Glean-Store.marcovisaya.repl.co/store";
      },
      error: function (jqXHR, exception) {
        var msg = '';
        if (jqXHR.status === 0) {
            msg = 'Not connect.\n Verify Network.';
        } else if (jqXHR.status == 401) {
           alert('Account not retrieved');
        }
      }
  });
}

function signup() {
  $.ajax({
      type: 'PUT',
      url: 'https://Glean-Store.marcovisaya.repl.co/verify',
      data: {
          'username': document.getElementById("signupUsername").value,
          'password': document.getElementById("signupPassword").value,
          'phone': document.getElementById("signupPhone").value,
          'email': document.getElementById("signupEmail").value
      },
      success: function (data) {
        alert('account created!')
      }
  });
}

function logout() {
  console.log("Logged Out")
  window.location.href = 'https://Glean-Store.marcovisaya.repl.co/logout'
}

function delete_user(uid) {
  $.ajax({
      type: 'DELETE',
      url: 'https://Glean-Store.marcovisaya.repl.co/admin/delete_user',
      data: {
          'id': uid
      },
      success: function (data) {
        document.getElementById(uid).remove();
        alert('account deleted!')
      }
  });
}

function add_order() {
  $.ajax({
      type: 'PUT',
      url: 'https://Glean-Store.marcovisaya.repl.co/add_order',
      data: {
        
      },
      success: function (data) {
        alert('Successfully ordered')
      }
  });
}

//main switcher

function swsignup(){
    var state = document.getElementById("login-screen")
    var state2 = document.getElementById("signup-screen")
    if (state.style.display !== "none" && state2.style.display === "none" ){
        state.style.display = "none"
        state2.style.display ="block"
        console.log("signup displayed, login hidden");
    }
}

function swlogin(){
    var state = document.getElementById("signup-screen")
    var state2 = document.getElementById("login-screen")
    if (state.style.display !== "none" && state2.style.display === "none" ){
        state.style.display = "none"
        state2.style.display ="block"
        console.log("login displayed, signup hidden");
    }
}

function swsubscription(){
  var state = document.getElementById("individualcards")
  var state1 = document.getElementById("subscriptioncards")
  var state2 = document.getElementById("favoritescards")
  var state3 = document.getElementById("individualhead")
  var state4 = document.getElementById("subscriptionhead")
  var state5 = document.getElementById("favoriteshead")

  if (state1.style.display === "none" && (state.style.display !== "none" || state2.style.display !== "none") ){
    state.style.display = "none"
    state1.style.display = "block"
    state2.style.display = "none"
    state3.style.display = "none"
    state4.style.display = "block"
    state5.style.display = "none"
    console.log("subscription displayed")
}
}

function swfavorites(){
  var state = document.getElementById("individualcards")
  var state1 = document.getElementById("subscriptioncards")
  var state2 = document.getElementById("favoritescards")
  var state3 = document.getElementById("individualhead")
  var state4 = document.getElementById("subscriptionhead")
  var state5 = document.getElementById("favoriteshead")

  if (state2.style.display === "none" && (state.style.display !== "none" || state1.style.display !== "none") ){
    state.style.display = "none"
    state1.style.display = "none"
    state2.style.display = "block"
    state3.style.display = "none"
    state4.style.display = "none"
    state5.style.display = "block"
    console.log("favorites displayed")
}
}

function swindividual(){
  var state = document.getElementById("individualcards")
  var state1 = document.getElementById("subscriptioncards")
  var state2 = document.getElementById("favoritescards")
  var state3 = document.getElementById("individualhead")
  var state4 = document.getElementById("subscriptionhead")
  var state5 = document.getElementById("favoriteshead")

  if (state.style.display === "none" && (state1.style.display !== "none" || state2.style.display !== "none") ){
    state.style.display = "block"
    state1.style.display = "none"
    state2.style.display = "none"
    state3.style.display = "block"
    state4.style.display = "none"
    state5.style.display = "none"
    console.log("individual displayed")
}
}