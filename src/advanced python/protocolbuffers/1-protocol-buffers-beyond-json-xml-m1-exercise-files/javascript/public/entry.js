var messages = require('./messages_pb');

var xhr = new XMLHttpRequest();
xhr.open('GET', '/api/message');
xhr.addEventListener('load', function() {
   resp = xhr.response;
   customer_pb = messages.Customer.deserializeBinary(xhr.response); 
   console.log(customer_pb.toObject());
});
xhr.send();

xhr2 = new XMLHttpRequest();
xhr2.open('GET', '/api/message?type=json');
xhr2.addEventListener('load', function() {
   customer_json = JSON.parse(xhr2.response); 
   console.log(customer_json);
});
xhr2.send();