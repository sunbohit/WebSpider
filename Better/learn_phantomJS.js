console.log('Hello, world!');
//phantom.exit();

var page = require('webpage').create();
page.open('http://llhelper.duapp.com/llnewcarddata', function (status) {
    console.log("Status: " + status);
    if (status === "success") {
        page.render('example.png');
    }
    phantom.exit();
});
