function login() {
  console.log('login');
  $.ajax({
      type: 'POST',
      url: 'https://Glean-Store.marcovisaya.repl.co/verify',
      data: {
          'username': document.getElementById("floatingInput").value,
          'password': document.getElementById("floatingPassword").value
      },
      success: function (data) {
        console.log(data)
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
  console.log('signup');
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
  alert("Logged out");
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

function add_product() {
  $.ajax({
      type: 'PUT',
      url: 'https://Glean-Store.marcovisaya.repl.co/admin/add_product',
      data: {
          'name': document.getElementById('addProduct-name').value,
          'category': document.getElementById('addProduct-category').value,
          'description': document.getElementById('addProduct-description').value,
          'ingredients': document.getElementById('addProduct-ingredients').value ,
          'price': document.getElementById('addProduct-price').value,
          'stock': document.getElementById('addProduct-stock').value,
          'image': document.getElementById('addProduct-image').value
      },
      success: function (data) {
        alert('Product added!')
      }
  });
}

function deleteProduct(product_id) {
  $.ajax({
      type: 'DELETE',
      url: 'https://Glean-Store.marcovisaya.repl.co/admin/delete_product',
      data: {
          'id': product_id
      },
      success: function (data) {
        document.getElementById(product_id).remove();
        alert('Product deleted!')
      }
  });
}

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