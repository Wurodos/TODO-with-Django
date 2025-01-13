let remove_buttons = document.getElementsByName("remove_task")
let add_button = document.getElementById("add_task")

remove_buttons.forEach(connect_removal)

if (add_button != null)
    add_button.onclick = open_form

console.log("working...")

function connect_removal(item)
{
    item.onclick = (event) => {
        let id = item.getAttribute('task-id')
        console.log(item)
        console.log(item.parentNode)
        console.log(item.parentNode.parentNode)
        item.parentNode.remove()
        remove_task(id)
    }
}

function remove_task(id)
{
    fetch(window.location.href + "delete/" + id + "/", {
        method: 'DELETE'
      })
        .then(response => console.log(response));
    console.log("task" + id + "removed!")
}

function open_form()
{
    console.log("what")
    fetch("form/true", {
        method: 'GET'
    })
        .then(response => window.open(response.url, "_self"));
    console.log("form opened!")
}
