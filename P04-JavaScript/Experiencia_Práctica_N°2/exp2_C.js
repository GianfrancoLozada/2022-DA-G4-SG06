console.log(x === undefined); 
    var x = 3;

    var myvar = 'my value';
    (function() { 
        var myvar = 'valor local';
        console.log(myvar)
        console.log(x)
    })();
    console.log(myvar)
    console.log(x)

    