const apicalypse = require("apicalypse")

const requestOptions = {
    queryMethod: 'url',
    method: 'get', // The default is `get`
    baseURL: 'https://api-v3.igdb.com/',
    headers: {
        'user-key': '65870b1858a85d7e30df9a6d9c40fdd0'
    },
    responseType: 'json',
    timeout: 1000, // 1 second timeout
    // auth: { // Basic auth
    //     username: 'janedoe',
    //     password: 's00pers3cret'
    // }
};

const response = function(){
    return apicalypse(requestOptions)
    .fields('name,platforms')
    .limit(50)    
    .query('platforms = 48')
    // After setting the baseURL in the requestOptions,
    // you can just use an endpoint in the request
    .request('/games'); 

} 

console.log(JSON.stringify(response, null, 2))