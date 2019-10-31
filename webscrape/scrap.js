var unirest = require("unirest");
const fastcsv = require('fast-csv');
const fs = require('fs');
const ws = fs.createWriteStream("out.csv");
// https://nodejs.org/api/fs.html#fs_fs_open_path_flags_mode_callback 
var req = unirest("GET", "https://api-v3.igdb.com/games");
//  you may need to add your own token value + key since this is Mitchell's personal key
// WHICH HAS A LIMIT TO 10K every month
req.headers({
  "cache-control": "no-cache",
  "Connection": "keep-alive",
  "Cookie": "__cfduid=d2247e241c9db5ccd0582909b012a3df21571094093",
  "Content-Length": "66",
  "Accept-Encoding": "gzip, deflate",
  "Host": "api-v3.igdb.com",
  "Postman-Token": "7c06cb27-3037-40ef-a354-0dac81858259,23ebf174-65f0-4939-be01-92427c52e3a4",
  "Cache-Control": "no-cache",
  "Accept": "*/*",
  "User-Agent": "PostmanRuntime/7.18.0",
  "Content-Type": "text/plain",
  "user-key": "65870b1858a85d7e30df9a6d9c40fdd0"
});
// platforms 48 is for the PS4 only, limit because we are limited to 50 requests

req.send("fields name,platforms;\nwhere platforms = 48;\noffset 0;\nlimit 50;\n");

req.end(function (res) {
  if (res.error) throw new Error(res.error);

  console.log(res.body);
  i= 0;

  
  data = []
  while(i<res.body.length){
    console.log(res.body[i].id + "    " + i);
    data.push(res.body[i].id)
    i++   
  } 

  console.log(data)
  fs.writeFile('out.csv', data, 'utf8', function (err) {
    flags: 'a'
    if (err) {
      console.log('Some error occured - file either not saved or corrupted file saved.');
    } else{
      console.log('It\'s saved!');
    }
  });

  fs.writeFile('out.csv', data, 'utf8', function (err) {
    flags: 'a'
    if (err) {
      console.log('Some error occured - file either not saved or corrupted file saved.');
    } else{
      console.log('It\'s saved!');
    }
  });
}

);
