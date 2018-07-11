function getClickCount(e){
    $.ajax({
        method: 'GET',
        url: '/shortener/' + e.className,
        success: (data) => {
            e.parentElement.parentElement.getElementsByTagName('td')[4].innerHTML = data['clickcount'];
        },
        error: (error) => {
            console.log(error);
        }
    });
}

function changeStatus(e){
    $.ajax({
        method: 'GET',
        url: '/shortener/change/' + e.classList[0],
        success: (data) => {
            e.innerHTML = data['status'].charAt(0).toUpperCase() + data['status'].substr(1);
        },
        error: (error) => {
            console.log(error);
        }
    });
}

$(".delete").click(function(){
    var shortlink = window.location.origin + '/' + $(this).data('value')
    $('#short-url a:first-child').text(shortlink)
    $('#short-url a:first-child').attr('target', '_blank')
    $('#short-url a:first-child').prop('href', shortlink)
    $("#modalDelete").modal('show')
})

$("#btn-delete").click(function(){
    var shortlink = $('#short-url a:first-child').attr('href');
    var shortcode = shortlink.substr(shortlink.lastIndexOf('/') + 1)
    $.ajax({
        method: 'GET',
        url: '/user/delete/' + shortcode,
        success: (data) => {
            $("#modalDelete").modal('hide');
            $("tbody:first").children("#" + shortcode).remove()
        },
        error: (error) => {
            console.log(error);
        }
    });
})