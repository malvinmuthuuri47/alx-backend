import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.error('Redis client not connected to the server:', error);
});

//Function that sets a value for a given key in Redis
function setNewSchool(schoolName, value) {
	client.set(schoolName, value, (error, reply) => {
		if (error) {
			console.error('Error setting school value:', error);
		} else {
			console.log('Reply: OK');
		}
	});
}

// Function that gets the value and logs it to the console
function displaySchoolValue(schoolName) {
	client.get(schoolName, (error, value) => {
		if (error) {
			console.error('Error retrieving school value: error');
		} else {
			console.log(`${value}`);
		}
	});
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', 100);
displaySchoolValue('HolbertonSanFrancisco');
