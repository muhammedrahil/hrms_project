$(document).ready(function(){
    $("#form-submition").validate({
        rules:{
            fname:{
                required:true,
                minlength:20,
            },
            lname:{
                required:true,
                minlength:20,
            },
            email:{
                required:true,
                email:true
            },
            emp_id:{
                required:true,
                minlength:20,
            },
            uid:{
                required:true,
                minlength:20,
            },
            notification_email:{
                required:true,
                email:true
            },
            mobail_no:{
                required:true,
                minlength:15,
            }
        },
        messages:{
            fname:{
                required:"enter your first name ",
                minlength:"please enter at least 5 charector"
            },
            lname:{
                required:"enter your last name ",
                minlength:"please enter at least 5 charector"
            },
            email:{
                required:"enter your mail ",
                email:"please enter only mail",
                
            },
            emp_id:{
                required:"enter employee id ",
                minlength:"please enter at least 2 charector"
            },
            uid:{
                required:"enter uid ",
                minlength:"please enter at least 2 charector"
            },
            notification_email:{
                required:"enter your notification mail ",
                email:"please enter only mail",
                
            },
            mobail_no:{
                required:"enter your mobail number ",
            },



        }
    })
})