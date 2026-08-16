const container = document.querySelector(".notes-container");
const menuBtn = document.querySelector(".three-dots");
const newCard = document.querySelector(".new-card");
const section = document.querySelector("section");
const newTitle = document.querySelector(".newTitle");
const newContent = document.querySelector(".newContent");
const saveBtn = document.querySelector(".saveBtn");
const cancelBtn = document.querySelector('.cancelBtn');

async function get_notes() {
    const response = await fetch("http://127.0.0.1:5000/notes",{
        method: "GET",
        credentials: "include"
    }
        
    )
    
    if(response.status === 200){
        const result = await response.json();
        result.forEach(note => {
            create_card(note) 
        });

        const new_container = document.querySelectorAll(".note-card");

        new_container.forEach(card=>{
            const menuBtn = card.querySelector('.three-dots');
            const idNote = card.getAttribute("data-note_id");

            menuBtn.addEventListener("click", event=>{
                console.log("clicked")

                const menuCard = card.querySelector(".menu");
                menuCard.classList.toggle("hidden")
            })
            const deleteBtn = card.querySelector(".delete")
            deleteBtn.addEventListener("click", async ()=>{
                console.log("deleted");
                
                
                const deleteResult = await delete_note(idNote);
                if(deleteResult.status === 200){
                    card.style.display = "none"
                }
                })
            const editBtn = card.querySelector(".edit");
            const menu = card.querySelector(".menu");
            const title = card.querySelector(".title");
            const content = card.querySelector(".content");

            editBtn.addEventListener("click",()=>{
                console.log(card);
                menu.classList.add("hidden")
                newCard.classList.remove("hidden");
                section.classList.add("blurred");
                newTitle.value = title.textContent;
                newContent.textContent = content.textContent;
            })
            saveBtn.addEventListener("click", ()=>{
                console.log("save");  
                let getTitle = newTitle.value;
                let getContent = newContent.value;
                title.textContent = getTitle;
                content.textContent = getContent;

                newCard.classList.add("hidden");
                section.classList.remove("blurred");
                update_note(idNote, getTitle, getContent);        
            })

            cancelBtn.addEventListener("click", ()=>{
                newCard.classList.add("hidden");
                section.classList.remove("blurred");
            })
        })
        
    }
    else{

    }
    


    
}
get_notes()

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
    console.log(JSON.stringify(data))
    const result = await fetch("http://127.0.0.1:5000/notes", {
        method: "PUT",
        headers: {
            "content-type": "application/json"
        },
        credentials: "include",
        body: JSON.stringify(data)
    })
    
}







