// adding the event listener by looping
document.querySelectorAll('.episode-link').forEach(item => {
    item.addEventListener('click', event => {
        console.log(item.id)
        $.ajax({
            url:"/./ajaxhandler/switch-episode/",
            type:"get",
            data: {
                requested_episode: item.id,
                current_url      : window.location.href
            },
            success: function(response){
                document.getElementById('episode').innerHTML = response.episode;
                document.getElementById('main-frame').src = response.frame;
            }

        });
    })
  })