$(document).ready(function () {

})

function add(blog_id) {
        var comment = $("#comment").val()
        data = {
            id:blog_id,
            comment:comment,
        }
        $.post("/comment/add/",data,function (ret) {
            if (ret["state"] == 1){
                 window.location.reload();
            }
            else{
                alert(ret["msg"])
            }
        })
    }