var studentsData = [
    { id: 1, name: "Sophia", email: "sophia@gmail.com", address: "USA" },
    { id: 2, name: "Ram", email: "ram@gmail.com", address: "BTK" },
    { id: 3, name: "Sita", email: "sita@gmail.com", address: "LTP" },
    { id: 4, name: "Hari", email: "hari@gmail.com", address: "KTM" },
]

function showData() {
    var outPut = "";
    studentsData.forEach(function (student, id) {
        outPut += `<tr>
        <td>${++id}</td>
        <td>${student.name}</td>
        <td>${student.email}</td>
        <td>${student.address}</td>
        <td>
        <button onclick="editRecord(${student.id})">Edit</button>
        <button onclick="deleteRecord(${student.id})">Delete</button>
        </td>
        </tr>`;
    });
    $("showRecord").innerHTML = outPut;
}

showData();



function $(id) {
    return document.getElementById(id);
}

function showMessages(message){
    $("messages").innerHTML = message;

    setTimeout(function(){
        $("messages").innerHTML = "";
    
    },3000);
}




var increment=5;
document.querySelector("#addRecord").addEventListener('click', function (e) {
    e.preventDefault();
    let name = $('name').value;
    let email = $('email').value;
    let address = $('address').value;

    if(name==""){
        $('error_name').innerHTML="Name is required";    
    }
    if(email==""){
        $('error_email').innerHTML="Email is required";
    
    }
    if(address==""){
        $('error_address').innerHTML="Address is required";
        return;
       
    }

    let criteria =$('criteria').value;
    if(criteria==""){   
        let sendData={id:increment,name:name,email:email,address:address};
        studentsData.push(sendData);
        showData();
        showMessages("Record Added Successfully");
        // clear data 
        $('name').value = "";
        $('email').value = "";
        $('address').value = "";
        increment++;
    }else{
        let id=criteria;       
        let data=getById(id);
        data.name=name
        data.email=email
        data.address=address    
        showData();
        showMessages("Record Updated Successfully");
        // clear data 
        $('name').value = "";
        $('email').value = "";
        $('address').value = "";
        $('criteria').value = "";
        $('addRecord').innerHTML = "Add Record";

    }

});


// get by id
function getById(id) {
    return studentsData.find(function (student) {
        return student.id == id;
    });
}

// delete record
function deleteRecord(id) {  
    let question = confirm(`Are you sure: ${getById(id).name} delete `);
    if(question){
        studentsData = studentsData.filter(function (student) {
            return student.id != id;
        });
        showData();
        showMessages("Record Deleted Successfully");
    }else{
        showMessages("Record Not Deleted");
    }

}

// update record
function editRecord(id) {
    let student = getById(id);
    $('name').value = student.name;
    $('email').value = student.email;
    $('address').value = student.address;
    $('criteria').value=id;
    $('addRecord').innerHTML = "Update Record";
}
