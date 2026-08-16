const container = document.querySelector(".notes-container")
const menuBtn = document.querySelector(".three-dots")

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
            menuBtn.addEventListener("click", event=>{
                console.log("clicked")

                const menuCard = card.querySelector(".menu");
                menuCard.classList.toggle("hidden")
            })
        const deleteBtn = card.querySelector(".delete")
        deleteBtn.addEventListener("click", async ()=>{
            console.log("deleted");
            
            idNote = card.getAttribute("data-note_id")
            const deleteResult = await delete_note(idNote);
            if(deleteResult.status === 200){
                card.style.display = "none"
            }
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




