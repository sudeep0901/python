var messages = require('./messages_pb');

var customer = new messages.Customer();

customer.setUsername('mvansickle');
customer.getEmailAddressesList().push('mike@pluralsight.com');
customer.setType(messages.Customer.Type.MEMBER);

var address = new messages.Customer.Address();
address.setAddress('123 Main St');
address.setCity('Heresville');
address.setState('OH');
address.setZipCode('44444');

customer.setAddress(address);

console.log(customer);
console.log(customer.toObject());