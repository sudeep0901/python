var message = require('./customer_pb');

var customer = new message.Customer();

customer.setFullName('Fred Flintstone');
customer.setUsername('bigman359');

console.log(customer.toObject());