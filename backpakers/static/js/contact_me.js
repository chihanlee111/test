// Contact Form Scripts

// $(function() {

//     $("#contactForm input,#contactForm textarea").jqBootstrapValidation({
//         preventSubmit: true,
//         submitError: function($form, event, errors) {
//             // additional error messages or events
//         },
//         submitSuccess: function($form, event) {
//             event.preventDefault(); // prevent default submit behaviour
//             // get values from FORM
//             var name = $("input#name").val();
//             var email = $("input#email").val();
//             var phone = $("input#phone").val();
//             var message = $("textarea#message").val();
//             var firstName = name; // For Success/Failure Message
//             // Check for white space in name for Success/Fail message
//             if (firstName.indexOf(' ') >= 0) {
//                 firstName = name.split(' ').slice(0, -1).join(' ');
//             }
//             $.ajax({
//                 url: "/user_message",
//                 type: "POST",
//                 data: {
//                     name: name,
//                     phone: phone,
//                     email: email,
//                     message: message
//                 },
//                 cache: false,
//                 success: function() {
//                     // Success message
//                     $('#success').html("<div class='alert alert-success alert-dismissable fade show'>");
//                     $('#success > .alert-success').html("<button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;")
//                         .append("</button>");
//                     $('#success > .alert-success')
//                         .append("Your message has been sent.");
//                     $('#success > .alert-success')
//                         .append('</div>');

//                     //clear all fields
//                     $('#contactForm').trigger("reset");
//                 },
//                 error: function() {
//                     // Fail message
//                     $('#success').html("<div class='alert alert-danger alert-dismissable fade show'>");
//                     $('#success > .alert-danger').html("<button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;")
//                         .append("</button>");
//                     $('#success > .alert-danger').append("Sorry " + firstName + ", it seems that my mail server is not responding. Please try again later!");
//                     $('#success > .alert-danger').append('</div>');
//                     //clear all fields
//                     $('#contactForm').trigger("reset");
//                 },
//             });
//         },
//         filter: function() {
//             return $(this).is(":visible");
//         },
//     });

//     $("a[data-toggle=\"tab\"]").click(function(e) {
//         e.preventDefault();
//         $(this).tab("show");
//     });
// });


// /*When clicking on Full hide fail/success boxes */
// $('#name').focus(function() {
//     $('#success').html('');
// });





//name: name,
                    //phone: phone,
                    //email: email,
                   // message: message

// function sendAjaxMessage(){
//             var xhttp = new XMLHttpRequest();
//             var name = $("input#name").val();
//             var email = $("input#email").val();
//             var phone = $("input#phone").val();
//             var message = $("textarea#message").val();
//             var parm = "name="+name+"&phone="+phone+"&email="+email+"&message="+message;
//             xhttp.open("POST", "{% url 'backpakers:user_message' %}", true);
//             xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
//             xhttp.send(parm);
//             xhttp.onreadystatechange = function() {
//                 if (this.readyState == 4 && this.status == 200) {
//                     $('#success').html("<div class='alert alert-success alert-dismissable fade show'>");
//                     $('#success > .alert-success').html("<button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;")
//                         .append("</button>");
//                     $('#success > .alert-success')
//                         .append("Your message has been sent.");
//                     $('#success > .alert-success')
//                         .append('</div>');

//                     //clear all fields
//                     $('#contactForm').trigger("reset");
//                 }
//             };
// }





