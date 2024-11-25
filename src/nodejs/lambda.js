const moment = require('moment-timezone');

exports.handler = async (event) => {
    const currentTime = moment().tz('UTC').format('YYYY-MM-DD HH:mm:ss');
    return {
        statusCode: 200,
        body: JSON.stringify(`Hello from Node.js Lambda! Current time: ${currentTime}`)
    };
};