var sendbtn=document.getElementById("sendbtn");
sendbtn.addEventListener("click", function (e) {
    let login=document.getElementsByName("loginField")[0].value;
    localStorage.setItem('login',login);
});

