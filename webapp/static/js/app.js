/**
 * Created by Ming on 5/10/17.
 */
var SVR_URL = "http://127.0.0.1:5000/";
$(window).on('load', function() {
    $.get(SVR_URL+"ana/hasModels", function(data, status){
        var resData = JSON.parse(data);
        console.log(resData.hasModels);
        if(resData.hasModels == false){
            console.log("true");
            $(".widget-container").not(".overview").hide();
            hideTrainBtn();
        } else {
            $("#load_btn").html("Reload Data");
            $("#train_btn").html("Re-train Models");
            loadStatistics();
            loadModelInfo();
            showTrainBtn();
        }
        showLoadBtn();

    });

    $("#page_loading_icon").hide();
});
function loadStatistics() {
    $.get(SVR_URL+"ana/getStatistics", function(data, status){
        var resData = JSON.parse(data);
            if(resData.success){
                console.log(resData);
                $(".dataset_info").html(resData.msg+" rows of data have been analyzed at "+ resData.lastOperation);
                loadGraphs();
                $("#load_btn").html("Reload Data");
            }
    });
}
function loadModelInfo() {
    $.get(SVR_URL+"ana/getModelsInfo", function(data, status){
        var resData = JSON.parse(data);
        if(resData.success){
            console.log(resData.models);
            var html = '<table class="table"><thead><tr><th>Model Name</th><th>RMSE</th></tr></thead><tbody>'+
            '<tr><td>'+resData.models[0].name+'</td><td>'+resData.models[0].rmse+'</td></tr>'+
            '<tr><td>'+resData.models[1].name+'</td><td>'+resData.models[1].rmse+'</td></tr>'+
            '</tbody></table>';
            $(".model_info").html(html);
            $(".model_info").show();
        }
    });
}
function showLoadBtn() {
    $("#load_btn").show();
    $("#load_btn").click(function(){
        $(".dataset_info").html('<img class="loading_icon" src="img/loading.gif"/>');
        $.get(SVR_URL+ "ana/generateGraphs", function(data, status){
            loadStatistics();
            showTrainBtn();
        });
    });
}

function loadGraphs() {
    $(".widget-container").fadeIn(2000);
    $(".graph_info").hide();
    $(".plot_img").each(function() {
        $(this).attr("src", $(this).attr("src"));
        /*console.log('element at index ' + index + 'is ' + (this.tagName));
        console.log('current element as dom object:' + element);
        console.log('current element as jQuery object:' + $(this));*/
    });
}
function hideTrainBtn() {
    $("#train_btn").hide();
    $("#redirect_btn").hide();
    //$(".model_info").hide();
}
function showTrainBtn() {
    $("#train_btn").show();
    $(".model_info").show();
    $("#train_btn").click(function(){
        $(".model_info").html('<img class="loading_icon" src="img/loading.gif"/>');
        $.get(SVR_URL+ "ana/trainModels", function(data, status){
            loadModelInfo();
            $("#train_btn").html("Remodeling");
            $("#redirect_btn").show();
        });
    });
}
