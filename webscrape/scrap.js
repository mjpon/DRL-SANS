var unirest = require("unirest");

var req = unirest("GET", "https://api-v3.igdb.com/games");

req.headers({
  "Postman-Token": "4097a55e-0f58-417e-bff6-ce19f2f58e5e",
  "cache-control": "no-cache",
  "user-key": "65870b1858a85d7e30df9a6d9c40fdd0"
});

  req.send("fields name,platforms;\nwhere platforms = 48;\n");

req.end(function (res) {
  if (res.error) throw new Error(res.error);

  console.log(res.body);
});
