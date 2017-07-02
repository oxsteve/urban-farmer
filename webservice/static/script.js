$(function() {

  var timer;
  var counterSec = 0;

  function tictac() {
    counterSec += 0.1;
    $("#timer").text(counterSec.toFixed(1));
  };

  function startPumpClicked() {
    $.ajax({
      url: "/watering/tomato/on",
      success: function(result) {
        if (timer == null) {
          timer = setInterval(tictac, 100);
          $("#pumpStartBtn").prop('disabled', true);
          $("#pumpStopBtn").prop('disabled', false);
          $("#resetTimerBtn").prop('disabled', false);
        } else {
          console.log("Timer still running.")
        }
      }
    });
  }

  function stopPumpClicked() {
    $.ajax({
      url: "/watering/tomato/off",
      success: function(result) {
        clearInterval(timer);
        timer = null;
        $("#pumpStartBtn").prop('disabled', false);
      }
    });
  }

  function resetTimerClicked() {
    $("#timer").text("0.0");
    counterSec = 0;
    $("#resetTimerBtn").prop('disabled', true);
  }

  $("#pumpStartBtn").click(startPumpClicked);
  $("#pumpStopBtn").click(stopPumpClicked);
  $("#resetTimerBtn").click(function() {
    stopPumpClicked();
    resetTimerClicked();
  });
});
