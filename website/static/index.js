// creating a javascript function in order to get the messages.
// We weill recieve the messages from the chatting window
$(function() {$('#sending_button').bind('click', function() {

// Here we are creating the variable var
// This variable will recieve the message from the chatting window.
// When the user will click the the button with id=message_type then the message will come to this variable message_value.
// This .value will recieve the value of message input.

        var message_value = document.getElementById("message_type").value
// Now we are setting the value of that text box to empty string
        document.getElementById("message_type").value = ""

//Now we are sending this message value to the FLASK app in order to send it to the server an update
        var msg_vla = message_value
        $.getJSON('/sending_messages',
            {incoming_message:msg_vla},
            function(data) {
//Closing tags for all the above functions
            });
        });
    });


//this function will help in update the chatting window messages
window.onload = function (){var update_loop = setInterval(update, 100);

// this will call now update function()
    update()
};

//Update function

function update(){

// It will fetch the messages from the server.
// After fetching the messages it will update it in chatting window
    fetch('/getting_messages')
             .then(function (response)

//             Then this function(response) will return the json file in which messages are store
             {return response.json();})

//             NOw this function(text) will return the messages
             .then(function (text) {

//             Now we are setting this variable messages to empty string
              var messages = "";
//            Now we are iterating the for loop
//            Iteration is on the value of text["message_to_print"]
                 for (value of text["message_to_print"])
                    {messages = messages + "<br >" + value}

// Now we are accessing the content from index.html with button id msg_testing
                 document.getElementById("msg_testing").innerHTML = messages
                });
};
