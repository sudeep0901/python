var messages = require('./public/messages_pb');

var address_pb = new messages.Address();
address_pb.setAddress1('123 Main Street');
address_pb.setAddress2('');
address_pb.setCity('Heresville');
address_pb.setState('TX');
address_pb.setZipCode('99999');

var customer_pb = new messages.Customer();
customer_pb.setFirstName('Fred');
customer_pb.setLastName('Thompson');
customer_pb.setAddress(address_pb);

var customer = {
    firstName: 'Fred',
    lastName: 'Thompson',
    address: {
        address1: '123 Main Street',
        address2: '',
        city: 'Heresville',
        state: 'TX',
        zipCode: '99999'
    }
};

var start, data, duration;

start = new Date();
for (var i = 0; i < 1000; i++) {
    
    data = JSON.stringify(customer);
    JSON.parse(data);
}
duration = new Date() - start;

console.log('JSON ' + duration + 'ms / ' + 
    data.length + ' bytes');

start = new Date();
for (var i = 0; i < 1000; i++) {
    data = customer_pb.serializeBinary();
    messages.Customer.deserializeBinary(data);
}
duration = new Date() - start;

console.log('Protobuf ' + duration + 'ms / ' + 
    data.length + ' bytes');
