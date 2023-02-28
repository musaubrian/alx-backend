const redis = require('redis');
const util = require('util');

const client = redis.createClient();
client.on('connect', () => console.log('Redis client connected to the server'));
client.on('error', err => console.log('Redis client not connected to the server:', err));

async function setNewSchool (schoolName, value) {
  const set = util.promisify(client.set).bind(client);
  redis.print(await set(schoolName, value));
}

async function displaySchoolValue (schoolName) {
  const get = util.promisify(client.get).bind(client);
  try {
    console.log(await get(schoolName));
  } catch (error) {
    console.log(error);
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
