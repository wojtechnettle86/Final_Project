var element = document.getElementById("id_username");
element.classList.add("form-control");

var element = document.getElementById("id_password1");
element.classList.add("form-control");

var element = document.getElementById("id_password2");
element.classList.add("form-control");

function checkPassword(form) {
    password1 = form.password1.value;
    password2 = form.password2.value;

    if (password1 == '')
        alert("Vyplňte prosím heslo");

    else if (password1.length < 8)
        alert("Heslo musí mít nejméně 8 znaků");

    else if (password2 == '')
        alert("Zadejte stejné heslo do druhého pole");
  
    else if (password1 != password2) {
        alert("\nHesla se neshodují, zkuste to znovu")
        return false;
    }

    else {
        alert("Registrace proběhla v pořádku")
        return true;
    }
}