function navbarClick() {
    document.getElementById("navbar").classList.toggle("hidden")
}

function checkAll() {
    let checked = document.getElementById("checkbox_all").checked
    let items = document.querySelectorAll("#questions-table input[type='checkbox']")
    items.forEach(item => item.checked = checked)
}
