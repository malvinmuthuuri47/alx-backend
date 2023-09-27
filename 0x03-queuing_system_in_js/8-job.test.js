import kue from 'kue';
const queue = kue.createQueue();
import chai from 'chai';
const expect = chai.expect;

import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
	let queue;

	before(() => {
		queue = kue.createQueue();
		queue.testMode.enter();
	});

	after(() => {
		queue.testMode.clear();
		queue.testMode.exit();
	});

	it('should create a job and log its creation', () => {

	
		const jobs = [
			{
				phoneNumber: '123456778',
				message: 'This is the code used for testing'
			}
		];

		createPushNotificationsJobs(jobs, queue);

		const jobsInQueue = queue.testMode.jobs;

		// Assertions
		expect(jobsInQueue.length).to.equal(jobs.length);
		expect(jobsInQueue[0].type).to.equal('push_notification_3');
	});
});
