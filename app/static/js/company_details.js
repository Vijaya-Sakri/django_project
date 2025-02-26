$(document).ready(function(){
    $("#Submit").click(function(){
        let name = $("#name").val();
        let mobile = $("#mobile").val();
        let email = $("#email").val();
        let details = $("#details").val();
        if (name == "" ){
            alert("please enter details");
            $("#name").focus();
            return false;
        }
        else if (mobile == ""){
            alert("please enter mobile number");
            $("#mobile").focus();
            return false;
        }
        else if (email == ""){
            alert("please enter email");
            $("#email").focus();
            return false;
        }
        else if (details == ""){
            alert("please enter details");
            $("#details").focus();
            return false;
        }
        let formData = new FormData();
        formData.append("name", $("#name").val());
        formData.append("mobile", $("#mobile").val());
        formData.append("email", $("#email").val());
        formData.append("details", $("#details").val());
        formData.append("csrfmiddlewaretoken", $('input[name = csrfmiddlewaretoken]').val());
        $.ajax({
            url : "/display_details/",
            type : "POST",
            data : formData,
            processData : false,
            contentType : false,
            success : function(res){
                    alert("Details added successfully");
                
            },
            error : function(request, error){
                console.log(error);
            },
            complete : function(){
                console.log("completed function")
            },
        });
    });
});
