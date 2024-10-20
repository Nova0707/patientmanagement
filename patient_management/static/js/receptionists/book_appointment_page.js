$(document).ready(function(){
    console.log("hello save time slot page!")
    // save_button_event_listner()
})


// Morning shift
let starts_time_morning;
let end_time_morning;

$('#start_time_morning').on('change', function() {
    var selectedTime = $(this).val();
    if (selectedTime) {
        starts_time_morning = selectedTime;
    } else {
        console.log('No start_time_morning selected.');
    }
});

$('#end_time_morning').on('change', function() {
    var selectedTime = $(this).val();
    if (selectedTime) {
        end_time_morning = selectedTime;
        if (starts_time_morning) {
            calculate_time_slots_morning();
        }
    } else {
        console.log('No end_time_morning selected.');
    }
});

function calculate_time_slots_morning() {
    if (!starts_time_morning || !end_time_morning) {
        console.log("Start or end time for morning is not set.");
        return;
    }

    let startMinutes = convertTimeToMinutes(starts_time_morning);
    let endMinutes = convertTimeToMinutes(end_time_morning);

    if (endMinutes > startMinutes) {
        let time_of_the_morning_shift = endMinutes - startMinutes;
        let average_time = 10; // 10 minutes per slot
        let number_of_slots = Math.floor(time_of_the_morning_shift / average_time);

        console.log("Number of morning slots: ", number_of_slots);
        $('#number_of_slots_morning').val(number_of_slots);
    } else {
        console.log("End time must be after start time");
        $('#number_of_slots_morning').val("End time must be after start time");
    }
}

// Evening shift
let start_time_evening;
let end_time_evening;

$('#start_time_evening').on('change', function() {
    var selectedTime = $(this).val();
    if (selectedTime) {
        start_time_evening = selectedTime;
    } else {
        console.log('No start_time_evening selected.');
    }
});

$('#end_time_evening').on('change', function() {
    var selectedTime = $(this).val();
    if (selectedTime) {
        end_time_evening = selectedTime;
        if (start_time_evening) {
            calculate_time_slots_evening();
        }
    } else {
        console.log('No end_time_evening selected.');
    }
});

function calculate_time_slots_evening() {
    if (!start_time_evening || !end_time_evening) {
        console.log("Start or end time for evening is not set.");
        return;
    }

    let startMinutes = convertTimeToMinutes(start_time_evening);
    let endMinutes = convertTimeToMinutes(end_time_evening);

    if (endMinutes > startMinutes) {
        let time_of_the_evening_shift = endMinutes - startMinutes;
        let average_time = 10; // 10 minutes per slot
        let number_of_slots = Math.floor(time_of_the_evening_shift / average_time);

        console.log("Number of evening slots: ", number_of_slots);
        $('#number_of_slots_evening').val(number_of_slots);
    } else {
        console.log("End time must be after start time");
        $('#number_of_slots_evening').val("End time must be after start time");
    }
}

// Helper function to convert time in HH:MM format to total minutes
function convertTimeToMinutes(time) {
    if (!time) {
        return 0;  // Handle the case where the time is undefined or invalid
    }
    let [hours, minutes] = time.split(':').map(Number);
    return (hours * 60) + minutes;
}


$(document).on('click','#save_time_slot',function(){
    get_form_data()
})

function get_form_data(){
    //morning shift
    let start_time_morning = $('#start_time_morning').val()
    let end_time_morning = $('#end_time_morning').val()
    let number_of_slots_morning = $('#number_of_slots_morning').val()

    // display no of slots
    // number_of_slots_morning id

    //evening shift
    let start_time_evening = $('#start_time_evening').val()
    let end_time_evening = $('#end_time_evening').val()
    let number_of_slots_evening = $('#number_of_slots_evening').val()

    //display no of slots
    // number_of_slots_evening id

    let data = {
        start_time_morning:start_time_morning,
        end_time_morning:end_time_morning,
        number_of_slots_morning:number_of_slots_morning,

        start_time_evening:start_time_evening,
        end_time_evening:end_time_evening,
        number_of_slots_evening:number_of_slots_evening
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