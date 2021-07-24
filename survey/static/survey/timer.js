function getTimeRemaining(endtime){
  const total = Date.parse(endtime) - Date.parse(new Date());
  const seconds = Math.floor( (total/1000) % 60 );
  const minutes = Math.floor( (total/1000/60) % 60 );
  const hours = Math.floor( (total/(1000*60*60)) % 24 );
  const days = Math.floor( total/(1000*60*60*24) );

  return {
    total,
    days,
    hours,
    minutes,
    seconds
  };
}

function initializeClock(id, endtime) {
  const clock = document.getElementById(id);
  const hoursSpan = clock.querySelector('.hours');
  const minutesSpan = clock.querySelector('.minutes');
  const secondsSpan = clock.querySelector('.seconds');
  function updateClock(){
      const t = getTimeRemaining(endtime);
      hoursSpan.innerHTML = ('0' + t.hours).slice(-2);
      minutesSpan.innerHTML = ('0' + t.minutes).slice(-2);
      secondsSpan.innerHTML = ('0' + t.seconds).slice(-2);

      // clock.innerHTML = 'days: ' + t.days + '<br>' +
      //                   'hours: '+ t.hours + '<br>' +
      //                   'minutes: ' + t.minutes + '<br>' +
      //                   'seconds: ' + t.seconds;
      if (t.total <= 0) {
        clearInterval(timeinterval);
        showResults();
      }
  }
  updateClock();
  var timeinterval = setInterval(updateClock,1000);
}

const timeInMinutes = parseInt(time_for_survey);
const currentTime = Date.parse(new Date());
const deadline = new Date(currentTime + timeInMinutes*60*1000);
initializeClock('clockdiv', deadline);