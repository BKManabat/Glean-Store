function login(e) {
  e.preventDefault();
  $.ajax({
      type: 'POST',
      url: 'https://Glean-Store.marcovisaya.repl.co/admin/verify',
      data: {
          'username': document.getElementById("loginUsername").value,
          'password': document.getElementById("loginPassword").value
      },
      success: function (data) {
        console.log("Logged In")
        window.location.href = "https://Glean-Store.marcovisaya.repl.co/admin";
      },
      error: function (jqXHR, exception) {
        var msg = '';
        if (jqXHR.status === 0) {
            alert('Not connect.\n Verify Network.');
        } else if (jqXHR.status == 401) {
           alert('Unauthorized');
        }
      }
  });
};

function logout() {
  console.log("Logged Out")
  window.location.href = 'https://Glean-Store.marcovisaya.repl.co/admin/logout';
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
        location.reload()
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
