let global_id = 1;

$(document).ready(function () {
    $("#add-item-btn").click(function () {
        global_id++;
        $("#add-item-btn").before(`
            <li>
                <input id='${global_id}' type="text" value="New Item" autofocus>
            </li> 
        `);
        $(`#${global_id}`).select();
    });

    $("#switch-direction-btn").click(function () {
        $("#mylist").toggleClass("col-item");
    });
});