import kue from 'kue';
const queue = kue.createQueue();

function createPushNotificationsJobs(jobs, queue) {
	if (!Array.isArray(jobs)) {
		throw new Error("Jobs is not an array");
	}

	jobs.forEach((jobData) => {
		const job = queue.create('push_notification_3', jobData);

		job.save((err) => {
			if (!err) {
				console.log(`Notification job created: ${job.id}`);
			} else {
				console.error(err);
			}
		});

		job.on('complete', () => {
			console.log(`Notification job ${job.id} complete`);
		});

		job.on('failed', (err) => {
			console.log(`Notification job ${job.id} failed: ${err}`);
		});

		job.on('progress', (progress) => {
			console.log(`Notification job ${job.id} ${progress} complete`);
		});
	});
}

module.exports = createPushNotificationsJobs;
