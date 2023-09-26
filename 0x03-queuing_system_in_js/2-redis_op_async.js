import redis from 'redis';
import util from 'util';

const client = redis.createClient();
const getAsync = util.promisify(client.get).bind(client);

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.error('Redis client not connected to the server:', error);
});

// Function that sets a value for a given key in Redis
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (error, reply) => {
    if (error) {
      console.error('Error setting school value:', error);
    } else {
      console.log('Reply: OK');
    }
  });
}

// Promisify the client.get method using util.promisify
const getSchoolValue = util.promisify(client.get).bind(client);

// Modified displaySchoolValue function using async/await
async function displaySchoolValue(schoolName) {
  try {
    const value = await getSchoolValue(schoolName);
    if (value !== null) {
      console.log(`${value}`);
    } else {
      console.log(`${schoolName} not found in Redis`);
    }
    // Add any other code that needs to run after displaying the value
  } catch (error) {
    console.error('Error retrieving school value:', error);
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
