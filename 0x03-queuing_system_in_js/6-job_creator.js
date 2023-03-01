const kue = require('kue');

const jobObject = {
  phoneNumber: '4153518780',
  message: 'This is the code to verify your account'
};
const queue = kue.createQueue();
const job = queue.create('push_notification_code', jobObject).save();

job.on('enqueue', () => {
  console.log(`Notification job created: ${job.id}`);
});
job.on('conplete', () => {
  console.log('Notification job completed');
});
job.on('failed', () => {
  console.log('Notification job failed');
});
