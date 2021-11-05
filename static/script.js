function login() {
  console.log('login');
  $.ajax({
      type: 'POST',
      url: 'https://Glean-Store.marcovisaya.repl.co/login',
      data: {
          'username': document.getElementById("username").value, //change to text field input
          'password': document.getElementById("password").value
      },
      success: function (data) {
        console.log(data)
        window.location.href = "https://Glean-Store.marcovisaya.repl.co/home?username="+data;
      },
      error: function (jqXHR, exception) {
        var msg = '';
        if (jqXHR.status === 0) {
            msg = 'Not connect.\n Verify Network.';
        } else if (jqXHR.status == 404) {
           alert('Account not retrieved');
        }
      }
  });
}

function signup() {
  console.log('signup');
  $.ajax({
      type: 'PUT',
      url: 'https://Glean-Store.marcovisaya.repl.co/login',
      data: {
          'username': document.getElementById("username").value, //change to text field input
          'password': document.getElementById("password").value
      },
      success: function (data) {
        alert('account created!')
      }
  });
}

function logout() {
  alert("Logged out");
  window.location.href = 'https://Glean-Store.marcovisaya.repl.co/logout'
}