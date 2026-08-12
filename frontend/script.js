const form = document.querySelector("#login-form")
const username_input = document.querySelector("#username")
const password_input = document.querySelector("#password")
const success_display = document.querySelector(".success-response")
const failure_display = document.querySelector(".failure-response")

let user_data = {}

form.addEventListener("submit", async (event)=>{
    event.preventDefault();
    console.log("Login form submitted");

    user_data["username"] = username_input.value;
    user_data["password"] = password_input.value;
    //console.log(user_data)
    //console.log(JSON.stringify(user_data))

    const response = await fetch("http://127.0.0.1:5000/login", {
        method: "POST",
        headers: {
            "content-type": "application/json"
        },
        body: JSON.stringify(user_data)
    }
        )

    const result = await response.json()
    console.log(result)

    success_display.style.display = "None"
    failure_display.style.display = "None"
    if(response.status === 200){
        success_display.style.display = "block";
    }
    else{
        failure_display.textContent = `${result.error}`
        failure_display.style.display = "block";
    }

    username_input.value = "";
    password_input.value = ""

})