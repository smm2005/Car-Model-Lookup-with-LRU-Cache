const form = document.getElementById("form")
const yearInput = document.getElementById("years")
const makeInput = document.getElementById("make")
const submitButton = document.getElementById("submit")

submitButton.addEventListener("click", ()=>{
    try{
        const yearVal = yearInput.value
        const makeVal = makeInput.value
        $.ajax({
            url: "/result",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({'yearValue': yearVal, 'makeValue': makeVal}),
            success: function(response){
                document.getElementById("carModelString").innerHTML = response;
                console.log(response);
            },
            error: function(error){
                document.getElementById("carModelString").innerHTML = error;
                console.log(error);
            }
        })
    }
    catch(err){
        console.log(err)
    }
})
