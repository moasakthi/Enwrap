/**
 * Created by Siva Sakthi Velan on 18/12/15.
 */
$(document).on('ready',function(){
var ctx = $("#myChart").get(0).getContext("2d");
// This will get the first returned node in the jQuery collection.
var myLineChart = new Chart(ctx).Line(data);
    var date = {{result['Date']}};
    var open = {{result['Date']}};
    var close = {{result['Date']}};
var data = {
    labels: date,
    datasets: [
        {
            label: "My First dataset",
            fillColor: "rgba(220,220,220,0.2)",
            strokeColor: "rgba(220,220,220,1)",
            pointColor: "rgba(220,220,220,1)",
            pointStrokeColor: "#fff",
            pointHighlightFill: "#fff",
            pointHighlightStroke: "rgba(220,220,220,1)",
            data: open
        },
        {
            label: "My Second dataset",
            fillColor: "rgba(151,187,205,0.2)",
            strokeColor: "rgba(151,187,205,1)",
            pointColor: "rgba(151,187,205,1)",
            pointStrokeColor: "#fff",
            pointHighlightFill: "#fff",
            pointHighlightStroke: "rgba(151,187,205,1)",
            data: close
        }
    ]
};

});