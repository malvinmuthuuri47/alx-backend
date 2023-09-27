import kue from 'kue';
const queue = kue.createQueue();

const blacklistedNumbers = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
	let progress = 0;

	const progressInterval = setInterval(() => {
		job.progress(progress, 100);
		progress += 10;

		if (progress > 100) {
			clearInterval(progressInterval);
		}
	}, 1000);

	if (blacklistedNumbers.includes(phoneNumber)) {
		const err = `Phone number ${phoneNumber} is blacklisted`;
		done(new Error(err));
	} else {
		// Simulate sending a notification
		setTimeout(() => {
			// Stop progress tracking
			clearInterval(progressInterval);
			// Update progress to 50
			job.progress(50, 100);
			// Log the notification
			console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
			done();
		}, 2000);
	}
}


// Process jobs from the queue with concurrency 2
queue.process('push_notification_code_2', 2, (job, done) => {
	const { phoneNumber, message } = job.data;
	sendNotification(phoneNumber, message, job, done);
});
