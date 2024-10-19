$(document).ready(function(){
    console.log("hello save time slot page!")
    // save_button_event_listner()
})

$(document).on('click','#save_time_slot',function(){
    get_form_data()
})

function get_form_data(){
    //morning shift
    let start_time_morning = $('#start_time_morning').val()
    let end_time_morning = $('#end_time_morning').val()
    let slot_time_duration = $('#slot_time_duration').val()

    // display no of slots
    // number_of_slots_morning id

    //evening shift
    let start_time_evening = $('#start_time_evening').val()
    let end_time_evening = $('#end_time_evening').val()
    let slot_time_evening = $('#slot_time_evening').val()

    //display no of slots
    // number_of_slots_evening id

    let data = {
        start_time_morning:start_time_morning,
        end_time_morning:end_time_morning,
        slot_time_duration:slot_time_duration,

        start_time_evening:start_time_evening,
        end_time_evening:end_time_evening,
        slot_time_evening:slot_time_evening
    }
    console.log(data)
    send_data(data)
}
function send_data(data){
    console.log(data)
    fetch(
        BookAppointmentLogic,
        {
            method:'POST',
            headers:{
                'Content-Type':'application/json',
                'X-CSRFToken':getCookie("csrftoken")
            },
            body:JSON.stringify(data)
        }
    )
    .then(response=>response.json())
    .then(data=>{
        if (data.status_code==201){
            alert("slot created!")
        }
        else{
            alert(data.error)
        }
    })
}