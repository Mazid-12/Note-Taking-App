const container = document.querySelector(".notes-container");
const newCard = document.querySelector(".new-card");
const section = document.querySelector("section");
const newTitle = document.querySelector(".newTitle");
const newContent = document.querySelector(".newContent");
const saveBtn = document.querySelector(".saveBtn");
const cancelBtn = document.querySelector('.cancelBtn');
const newNoteBtn = document.querySelector('.newNoteBtn');
const logoutBtn = document.querySelector('.logoutBtn');
let note_id;
let editState;

async function get_notes() {
    const response = await fetch("http://127.0.0.1:5000/notes",{
        method: "GET",
        credentials: "include"
    })
    
    if(response.status === 200){
        const result = await response.json();
        result.forEach(note => {
            create_card(note) 
        });     
    }
    else if(response.status ===401){
        window.location.href = "index.html";
    }
    else{
    }   
}
get_notes()

container.addEventListener("click", ()=>{
    const menuBtn = event.target.closest(".three-dots");
    const card = event.target.closest(".note-card");
    const title = container.querySelector('.title');
    const content = container.querySelector('.content')
    const deleteBtn = event.target.closest('.delete');
    note_id = card.getAttribute("data-note_id");
    const editBtn = event.target.closest('.edit')
    const menuCard = card.querySelector(".menu");
    if(menuBtn){ 
        menuCard.classList.toggle("hidden");
    } 
    if(deleteBtn){
        (async () =>{
            const deleteResult = await delete_note(note_id);
            if(deleteResult.status === 200){
            card.style.display = "none"
            }
        })() 
    }
    if(editBtn){
        menuCard.classList.add("hidden")
        newCard.classList.remove("hidden");
        section.classList.add("blurred");
        newTitle.value = title.textContent;
        newContent.textContent = content.textContent;
        editState = 'update';
    }  
});

cancelBtn.addEventListener("click", ()=>{
    newCard.classList.add("hidden");
    section.classList.remove("blurred");
})

saveBtn.addEventListener("click", ()=>{
    if(editState === "update"){
        let getTitle = newTitle.value;
        let getContent = newContent.value;
        const editedCard = container.querySelector(`[data-note_id = "${note_id}"]`)
        const editedTitle = editedCard.querySelector('.title')
        const editedContent  = editedCard.querySelector('.content')
        console.log(editedCard)
        editedTitle.textContent = getTitle;
        editedContent.textContent = getContent;
        update_note(note_id, getTitle, getContent);
        newTitle.value = "";
        newContent.value = ""; 
    } 
    else if(editState==='create'){
        let newNote = {};
        newNote.idNote = 5;
        newNote.title = newTitle.value;
        newNote.content = newContent.value;
        create_card(newNote);
        add_note(newTitle, newContent)
    }
    newCard.classList.add("hidden");
    section.classList.remove("blurred");
        
})

function create_card(note){
    const card = document.createElement('div')
    const topSection =  document.createElement('div')
    const title = document.createElement('h2')
    const threePoints =  document.createElement('button')
    const content =  document.createElement('p')
    const menu_container = document.createElement('div')
    const menu =  document.createElement('div')
    const editBtn = document.createElement('button')
    const deleteBtn = document.createElement('button')

    card.classList.add("note-card");
    topSection.classList.add("top-section");
    content.classList.add('content');
    title.classList.add("title")
    threePoints.classList.add("three-dots");
    menu.classList.add("menu");
    menu_container.classList.add("menu-container");
    menu.classList.add("hidden")
    deleteBtn.classList.add("delete");
    editBtn.classList.add("edit");
    deleteBtn.classList.add("menuBtn");
    editBtn.classList.add("menuBtn")

    title.textContent = note.title;
    content.textContent = note.content;
    threePoints.textContent = "⋮";
    editBtn.textContent = "Edit";
    deleteBtn.textContent = "Delete";
    card.dataset.note_id = note.idNote;

    menu.appendChild(editBtn)
    menu.appendChild(deleteBtn)
    menu_container.appendChild(threePoints)
    menu_container.appendChild(menu)
    topSection.appendChild(title);
    topSection.appendChild(menu_container)

    card.appendChild(topSection)
    card.appendChild(content)

    container.appendChild(card)
}

async function delete_note(id_note){
    const result = await fetch(`http://127.0.0.1:5000/notes/${id_note}`,{
        method: "DELETE",
        credentials: "include"
    })
    return result
}
async function update_note(idNote, getTitle, getContent) {
    console.log("updating...");
    let data = {}
    data.idNote = idNote
    data.newTitle = getTitle;
    data.newContent = getContent;
    const result = await fetch("http://127.0.0.1:5000/notes", {
        method: "PUT",
        headers: {
            "content-type": "application/json"
        },
        credentials: "include",
        body: JSON.stringify(data)
    })
    
}

newNoteBtn.addEventListener("click", ()=>{
    newCard.classList.remove("hidden");
    section.classList.add("blurred");
    editState = "create";
})

async function add_note(title, content){
    new_data = {};
    new_data.noteTitle = title.value;
    new_data.noteContent = content.value;
    console.log(new_data)
    const result = await fetch("http://127.0.0.1:5000/notes", {
        method: "POST",
        headers: {
            "content-type": "application/json"
        },
        credentials: "include",
        body: JSON.stringify(new_data)
    })
    console.log(await result.json())
}


logoutBtn.addEventListener("click", async ()=>{
    console.log("Logout")
    const result = await fetch("http://127.0.0.1:5000/logout",{
        method: "POST",
        credentials: "include"
    })
    console.log(result)
    if(result.ok){
        window.location.href = "index.html";
    }
    
})



