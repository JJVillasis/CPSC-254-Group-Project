var searchInput = window.location.search.replace(/^\?q=/, '');
let header = document.getElementById("search_Heading");
header.innerText = "Results \"" + searchInput + "\"";