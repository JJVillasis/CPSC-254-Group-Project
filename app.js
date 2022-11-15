var searchInput = "";

function saveInput(){
    let input = document.getElementById('searchbar').value;
    searchInput = "Test"
}

let header = document.getElementById("search_Heading");
header.innerText = "Results \"" + searchInput + "\"";