// function test(){
//     console.log('test was success')
// }
//
// test();

//
// function  users(name,age=20){
//     console.log(name)
//     console.log(age)
// }
//
// users('ram')

// function data(...name) {
//     console.log(name);
// }
//
// data('ram', 'sita', 2345)

// function add(x, y) {
//     return x + y;
//
// }
//
// console.log(add(10, 20))

// let name = prompt("Enter your name")
// console.log(name)



// function addData(){
//     let n1 = parseInt(document.getElementById('num1').value);
//     let n2 = parseInt(document.getElementById('num2').value);
//     let total = n1+n2;
//     document.getElementById('result').value = total;
//     document.getElementById('num1').value =''
//     document.getElementById('num2').value=''

// }


// let user = function(){
//     console.log('i am users')
// }

// user();

// let user = ()=>{
//     console.log('test');
// }

// user();


// setTimeout(function(){

// });


// setTimeout(()=>{

// })


// function* test(){
//     yield 10
//     yield 30
//     yield 40
// }

// let a = test();
// console.log(a.next())
// console.log(a.next())
// console.log(a.next())
// console.log(a.next())



// console.log(test())

// function user(){
//     return 10
//     return 30

// }



// function test(){

//     function get(){
//         return 'hello'
//     }

//     return get;
// }


// console.log(test()())

// let a ='10'
// let b =10

// if(a===b){
//     console.log('yes')
// }else{
//     console.log('no');
// }



// function demoMessage(){
//     let question = confirm("Do you love me?")
//     if(question===true){
//         let name = prompt("Enter your name")
//         alert(`Hi I am ${name}`)
//     }else{
//         alert("test");

//     }


// }


// setTimeout(function(){
//     demoMessage();
// },2000);

// setInterval(function(){
//     demoMessage()

// },2000);



// let name ='ram'
// let age =20

// console.log("my name is "+name + 'age'+age)

// console.log(`my name is ${name} age ${age}`);



// function changeColor(){
//     let colorName = prompt("Enter color name: ")
//     document.getElementById('box').style.background=colorName

// }



let items =document.getElementsByClassName('items');
for(let i=0;i<items.length;i++){
    items[i].style.display='none';
}