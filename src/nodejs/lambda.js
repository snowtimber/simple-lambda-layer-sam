const moment = require('moment-timezone');

exports.handler = async (event) => {
    const currentTime = moment().tz('UTC').format('YYYY-MM-DD HH:mm:ss');
    console.log(`Node.js version: ${process.version}`);
    return {
        statusCode: 200,
        body: JSON.stringify(`Hello from Node.js ${process.version} Lambda! Current time: ${currentTime}`)
    };
};