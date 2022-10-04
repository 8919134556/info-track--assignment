var selectedRow = null



function onSelect(td) {
    selectedRow = td.parentElement.parentElement;
    var table = document.getElementById("employeeList").getElementsByTagName('tbody')[0];
    var newRow = table.insertRow(table.length);
    cell1 = newRow.insertCell(0);
    cell1.innerHTML = selectedRow.cells[0].innerHTML;
    cell2 = newRow.insertCell(1);
    cell2.innerHTML = selectedRow.cells[1].innerHTML;
    cell3 = newRow.insertCell(2);
    cell3.innerHTML = selectedRow.cells[2].innerHTML;
    cell4 = newRow.insertCell(3);
    cell4.innerHTML = selectedRow.cells[3].innerHTML;
}

// function onDelete(id) {
//     alert(id);
//     // if (confirm('Are you sure to delete this record ?')) {
//     //     row = td.parentElement.parentElement;
//     //     document.getElementById("employeeList").deleteRow(row.rowIndex);
//     //     resetForm();
//     // }
// }

function deleteRow(td)
{
    selectedRow = td.parentElement.parentElement;
    // alert(selectedRow.cells[0].innerHTML);
    var id = selectedRow.cells[0].innerHTML;
    document.getElementById("employeeList").getElementsByTagName('tbody')[0].deleteRow(id.rowIndex);
    // var row = document.getElementById(id);
    // if (row)
    // {
    //     row.remove();
    // }
    // else{
    //     alert("there is value")
    // }
}