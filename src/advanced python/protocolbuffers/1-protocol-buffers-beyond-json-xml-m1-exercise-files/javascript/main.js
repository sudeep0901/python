var http = require('http');
var fs = require('fs');
var url = require('url');
var messages = require('./public/messages_pb');

var server = http.createServer(function(req, res) {
    var path = url.parse(req.url).pathname;
    if (path.startsWith('/api')) {
        messageHandler(req, res);
    } else {
        staticFileHandler(req, res);
    }
});



function staticFileHandler(req, res) {
    var path = url.parse(req.url).pathname;
    if (path === '/') {
        path = '/index.html';
    }

    var contentType;
    if (path.endsWith('.js')) {
        contentType = 'application/json';
    } else if (path.endsWith('.html')) {
        contentType = 'text/html';
    } 
    if (contentType) {
        res.setHeader('Content-Type', contentType);
    }
    fs.readFile('public'  + path, null, function(err, data) {
        res.end(data);
    });
}

function messageHandler(req, res) { 
    var urlInfo = url.parse(req.url);
    if (urlInfo.query && urlInfo.query === 'type=json') {
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

        res.end(JSON.stringify(customer));
    } else {
        var address = new messages.Address();
        address.setAddress1('123 Main Street');
        address.setAddress2('');
        address.setCity('Heresville');
        address.setState('TX');
        address.setZipCode('99999');

        var customer = new messages.Customer();
        customer.setFirstName('Fred');
        customer.setLastName('Thompson');
        customer.setAddress(address);
        
        var bytes = customer.serializeBinary();

        res.write(new Buffer(bytes).toString('base64'));
        res.end();
    }
}

server.listen(3000);
console.log('Listening on port 3000');