var unirest = require("unirest");

var req = unirest("GET", "https://api-v3.igdb.com/games");

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

  req.send("fields name,platforms;\nwhere platforms = 48;\noffset 49;\nlimit 50;\n");

req.end(function (res) {
  if (res.error) throw new Error(res.error);

  console.log(res.body);
});
