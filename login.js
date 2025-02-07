// to include packages, we store modules in these variables
var mysql = require('mysql');
var express = require('express');
var session = require('express-session');
var bodyParser = require('body-parser');
var path = require('path');
var cors = require('cors');
var fs = require('fs');
const { json } = require('express');

// creates a connection to database
var connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'palcove96',
    database: 'nodelogin'
});

// var connection = mysql.createConnection({
// 	host: 'reetu-parikh-mysqlserver.mysql.database.azure.com',
// 	user: 'reetu_root@reetu-parikh-mysqlserver',
// 	password: 'Ree_11383-',
//     database: 'nodelogin',
//     port = 3306,
//     ssl = true
// });

// checks if there is an error connecting to the database
connection.connect(function (err) {
    if (!err) {
        console.log("Database is connected");
    } else {
        console.log(err);
    }
});

// express framework
var app = express();

app.use(cors());
app.use(express.static(__dirname + '/public'))

// clients of the API/website will be assigned a unique session which allows you to store the user state 
// if a client's http request doesn't already have a session cookie, a new session is created
app.use(session({
    // secret is the only required parameter
    // password to access the session
    secret: 'secret',
    // resets the maxAge property of a cookie, which determines how long the session cookie has before it expires
    resave: true,
    // if false, the session object created by the user when they log in does not save
    // used to identify reccuring visitors
    saveUninitialized: true
}));

// bodyParser ensures that the user input is UTF-8
app.use(bodyParser.urlencoded({ extended: true }));

// bodyParser ensures that the user input returns a JSON (user input is converted to a JSON)
app.use(bodyParser.json());

// when the client goes on website, we must tell node what file to display
// 'get' gets the file login.html so it can be displayed
// the slash is the root of the website
app.get('/', function (request, response) {
    // __dirname must be there
    response.sendFile(path.join(__dirname + '/login.html'));
    // console.log(__dirname) prints the path of where the file is stored
});

app.get('/register', function (request, response) {
    response.sendFile('/register.html', { root: __dirname })
});

app.get('/home', function (request, response) {
    // check if logged in attribute for the client is true
    if (request.session.loggedin) {
        response.sendFile('/home.html', { root: __dirname })
        //response.send('Welcome back, ' + request.session.username + '!');
    }
    else {
        response.send('Please login to view this page');
    }
    //response.end();
});

app.get('/saved', function (request, response) {
    // check if logged in attribute for the client is true
    if (request.session.loggedin) {
        response.sendFile('/saved.html', { root: __dirname })
        //response.send('Welcome back, ' + request.session.username + '!');
    }
    else {
        response.send('Please login to view this page');
    }
    //response.end();
});

// app.get('/results', function(request, response) {
//     response.sendFile('public/results.html', { root: __dirname })

// });

// when /name is called, the function displayNews is called
app.get('/newsArticles', getNews);

app.get('/saved', callSaved);

// outputs from python
async function getNews(request, response) {
    //use spawn method from the child_process module to connect python
    var spawn = require('child_process').spawn;

    //spawn parameters:
    //1. type of script
    //2. list containing path and arguments of the script

    var search = request.query.search;
    var CNN = request.query.CNN;
    var MSNBC = request.query.MSNBC;
    var TheBlaze = request.query.TheBlaze;
    var TheWallStreetJournal = request.query.TheWallStreetJournal;
    var FOXNews = request.query.FOXNews;

    // var process = spawn('python', ['./news.py', search, CNN, MSNBC, TheBlaze, TheWallStreetJournal, FOXNews]);
    if (search.length == 0) {
        response.send('Please enter your search');
    }

    sources = [CNN, MSNBC, TheBlaze, TheWallStreetJournal, FOXNews];
    var numSources = 0;
    for (var i = 0; i < sources.length; i++) {
        if (sources[i] == 'on') {
            numSources++;
        }
    }
    numArticles = Math.floor(15 / numSources);

    if (numSources == 0) {
        response.send('Please check at least one news source');
    }

    if (CNN == 'on') {
        console.log('cnn1');
        process = spawn('python', ['./cnn.py', search, numArticles]);
    }

    if (MSNBC == 'on') {
        console.log('ms1');
        process = spawn('python', ['./msnbc.py', search, numArticles]);
    }

    if (TheBlaze == 'on') {
        console.log('tb');
        process = spawn('python', ['./the_blaze.py', search, numArticles]);
    }

    if (TheWallStreetJournal == 'on') {
        console.log('wsj');
        process = spawn('python', ['./wsj.py', search, numArticles]);
    }

    if (FOXNews == 'on') {
        console.log('fox');
        process = spawn('python', ['./fox_news.py', search, numArticles]);
    }

    process.stdout.on('data', function (data) {
        // response.send(data.toString());
        response.sendFile('public/results.html', { root: __dirname });
    });

    // console.log("waited");
    // response.sendFile('public/results.html', { root: __dirname });
    // setTimeout(function() {response.sendFile('public/results.html', { root: __dirname })}, 2000);

    // data contains result from python
    // process.stdout.on('data', function(data) {
    //     // response.send(data.toString());
    //     response.sendFile('public/results.html', { root: __dirname });
    // });
}

async function getSource(search, CNN, MSNBC, TheBlaze, TheWallStreetJournal, FOXNews) {
    var spawn = require('child_process').spawn;
    // if (search.length == 0) {
    //     response.send('Please enter your search');
    // }

    // sources = [CNN, MSNBC, TheBlaze, TheWallStreetJournal, FOXNews];
    // var numSources = 0;
    // for (var i = 0; i < sources.length; i++) {
    //     if (sources[i] == 'on') {
    //         numSources++;
    //     }
    // }

    // if (numSources == 0) {
    //     response.send('Please check at least one news source');
    // }


    // if (CNN == 'on') {
    //     console.log('cnn1');
    //     process = spawn('python', ['./cnn.py', search, numArticles]); 
    // }

    // if (MSNBC == 'on') {
    //     console.log('ms1');
    //     process = spawn('python', ['./msnbc.py', search, numArticles]);
    // }

    // if (TheBlaze == 'on') {
    //     console.log('tb');
    //     process = spawn('python', ['./the_blaze.py', search, numArticles]);
    // }

    // if (TheWallStreetJournal == 'on') {
    //     console.log('wsj');
    //     process = spawn('python', ['./wsj.py', search, numArticles]);
    // }

    // if (FOXNews == 'on') {
    //     console.log('fox');
    //     process = spawn('python', ['./fox_news.py', search, numArticles]);
    // }
    // var moveOn = false;
    // var count = 0;
    // while (!moveOn) {
    //     fs.readFile('public/articles.json', (err, data) => {
    //         if (err) throw err;
    //         var article = JSON.parse(data);
    //         for (var i = 0; i < article.length; i++) {
    //             article[i].hasOwnProperty('done');
    //             count++;
    //         }
    //         count = 2;
    //         if (count == numSources) {
    //             moveOn = true;
    //         }
    //     });
    // }

}


function callSaved(request, response) {
    //use spawn method from the child_process module to connect python
    var spawn = require('child_process').spawn;

    //spawn parameters:
    //1. type of script
    //2. list containing path and arguments of the script

    // data contains result from python
    // process.stdout.on('data', function(data) { 
    //     response.send(data.toString()); 
    // } ); 
}


app.post('/auth', function (request, response) {
    // request.body.HTMLname to get the user input 
    var username = request.body.username;
    var password = request.body.password;
    // check if username and password exists
    if (username && password) {
        // first parameter: mysql query
        // second parameter: values for ? in the query
        // third parameter: function that gets called after the query
        connection.query('SELECT * FROM accounts WHERE username = ? AND password = ?', [username, password], function (error, results, fields) {
            // if username and password was found in the database
            if (results.length > 0) {
                // sets loggedin to true if the user is logged in
                // useful for if you only display certain info to users who are logged in
                request.session.loggedin = true;
                // sets username session equal to the username so you can access the username later
                request.session.username = username;
                // since the user is logged in, redirect to a different page
                response.redirect('/home');
            }
            else {
                // if client is not found in the database
                response.send('Incorrect username and/or password');
            }
            response.end();
        });
    }
    else {
        // username/password was not filled out by the client
        response.send('Please enter username and password');
        response.end();
    }
});


app.post('/addUser', function (request, response) {
    var email = request.body.email;
    var username = request.body.username;
    var password = request.body.password;

    if (email && username && password) {
        connection.query('SELECT * FROM accounts WHERE email = ? OR username= ?', [email, username], function (error, results, fields) {
            // if any error while executing above query, throw error
            if (error) throw error;
            if (results.length > 0) {
                var usedUsername = false;
                var usedEmail = false;
                // iterate for all the rows in result to check is username or email is already in the database
                for (var i = 0; i < results.length; i++) {
                    if (results[i].username == username) {
                        usedUsername = true;
                        break;
                    }
                }
                for (var i = 0; i < results.length; i++) {
                    if (results[i].email == email) {
                        usedEmail = true;
                        break;
                    }
                }
                if (usedUsername && usedEmail) {
                    response.send('A user has already registered with this username and email');
                    response.end();
                }
                else if (usedUsername) {
                    response.send('A user has already registered with this username');
                    response.end();
                }
                else {
                    response.send('A user has already registered with this email');
                    response.end();
                }
            }
            else {
                connection.query('INSERT INTO accounts(username, password, email) VALUES(?, ?, ?)', [username, password, email], function () {
                    if (error) throw error;
                });
                response.send('User has been registered');
                response.end();
            }

        });
    }
    else {
        response.send('Please enter email, username, and password');
        response.end();
    }

});

// you use '/home' because you were redirected there when the user sucessfully logged in 


// listening on a port creates a server
app.listen(5555, function () {
    console.log('Listening on port 5555');
});


// CORS Error: client can't acess the server; FIX:
// npm install cors
// var cors = requires('cors')
// app.use(cors())
// https://www.npmjs.com/package/cors

// https://codeshack.io/basic-login-system-nodejs-express-mysql/

