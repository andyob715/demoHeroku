function calchours()
{
    let student_class_input = document.getElementById("student_class_input").value
    let exampleDataList2 = document.getElementById("exampleDataList2").value
    let exampleDataList3 = document.getElementById("exampleDataList3").value
    let daysform = document.getElementById("daysform").value
    
    console.log("Student Input",student_class_input)
    console.log("exampleDataList2",dropdown2)
    console.log("exampleDataList3",dropdown3)
    console.log("daysform",daysform)

    fetch("/index", {
        method: "POST", 
        body: JSON.stringify(
            {
            student_class_input: student_class_input,
            input_2: exampleDataList2,
            input_3: exampleDataList3,
            input_4: daysform
            }),
        headers:
            {
            "Content-type":"application/json;charset=UTF-8"
            } 
}).then(resp=>{
    return resp.json()
    }).then(resp=>{
    console.log(resp)
    document.getElementById("prediction").innerHTML=resp.Prediction
    console.log(resp.Prediction)}
    )}