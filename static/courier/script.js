function login(e) {
  e.preventDefault();
  $.ajax({
      type: 'POST',
      url: 'https://Glean-Store.marcovisaya.repl.co/courier/verify',
      data: {
          'username': document.getElementById("loginUsername").value,
          'password': document.getElementById("loginPassword").value
      },
      success: function (data) {
        console.log("Logged In")
        window.location.href = "https://Glean-Store.marcovisaya.repl.co/courier";
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

function logout() {
  console.log("Logged Out")
  window.location.href = 'https://Glean-Store.marcovisaya.repl.co/courier/logout'
}
