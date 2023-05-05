var levels = ['weak', 'medium', 'strong', 'very strong'];

$(document).ready(function () {
    $("#passwordbox").keyup(function (e) {
        // Check password strength
        if ($("#passwordbox").val().length > 0)
            $("#password-strength-bg").show();
        else
            $("#password-strength-bg").hide();

        let strength = getPasswordStrength($("#passwordbox").val());


        switch (strength) {
            case 0:
                $("#password-strength").css('width', '20%');
                $("#password-strength").css('background-color', '#ff3333');
                $("#level").val(levels[0]);
                break;

            case 1:
                $("#password-strength").css('width', "40%");
                $("#password-strength").css('background-color', '#ff7f7f');
                $("#level").val(levels[1]);
                break;

            case 2:
                $("#password-strength").css('width', "60%");
                $("#password-strength").css('background-color', '#ffff7f');
                $("#level").val(levels[2]);
                break;

            case 3:
                $("#password-strength").css('width', "80%");
                $("#password-strength").css('background-color', '#7fff7f');
                $("#level").val(levels[3]);
                break;

            case 4:
                $("#password-strength").css('width', "100%");
                $("#password-strength").css('background-color', '#33ff33');
                $("#level").val(`${levels[4]}`);
                break;
        }
    });

    $('#sign-up-btn').on('click', function () {
        if ($("#input1")[0].checkValidity() === false) {
            $("#input1").css("border-color", "red");
        }
        else {
            $("#input1").css("border-color", "black");
        }
        if ($("#input2")[0].checkValidity() === false) {
            $("#input2").css("border-color", "red");
        }
        else {
            $("#input2").css("border-color", "black");
        }
        if ($("#passwordbox")[0].checkValidity() === false) {
            $("#passwordbox").css("border-color", "red");
        }
        else {
            $("#passwordbox").css("border-color", "black");
        }
        if ($("#input3")[0].checkValidity() === false) {
            $("#input3").css("border-color", "red");
        }
    });

    $("#login-btn").on("click", function () {
        if ($("#input4")[0].checkValidity() === false) {
            $("#input4").css("border-color", "red");
        }
        else {
            $("#input4").css("border-color", "black");
        }
        if ($("#input5")[0].checkValidity() === false) {
            $("#input5").css("border-color", "red");
        }
        else {
            $("#input5").css("border-color", "black");
        }
    });

});



function getPasswordStrength(password) {
    var strength = -1;
    if (password.match(/[a-z]+/)) {
        strength += 1;
    }
    if (password.match(/[A-Z]+/)) {
        strength += 1;
    }
    if (password.match(/[0-9]+/)) {
        strength += 1;
    }
    if (password.match(/[$@#&!]+/)) {
        strength += 1;
    }
    if (password.includes('a'))
        strength += 1;

    return strength;
}

