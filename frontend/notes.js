const container = document.querySelector(".notes-container")

async function get_notes() {
    const response = await fetch("http://127.0.0.1:5000/notes",{
        method: "GET",
        credentials: "include"
    }
        
    )
    const result = await response.json();
    console.log(result)

    result.forEach(note => {
        create_card(note) 
    });
    
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
    menu.classList.add("inactive")

    title.textContent = note.title;
    content.textContent = note.content;
    threePoints.textContent = "⋮";
    editBtn.textContent = "Edit";
    deleteBtn.textContent = "Delete";

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