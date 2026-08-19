const API_URL="http://<ALB_DNS>/api/students";

function loadStudents(){
  const container=document.getElementById("students");
  container.innerHTML="Loading...";
  fetch(API_URL)
    .then(r=>{if(!r.ok)throw new Error("API request failed");return r.json()})
    .then(data=>{
      if(!Array.isArray(data)||data.length===0){container.innerHTML="No students found.";return;}
      container.innerHTML=data.map(s=>`
        <div class="student">
          <h3>${s.name}</h3>
          <p>Roll No: ${s.roll_no}</p>
          <p>Attendance: ${s.attendance}%</p>
          <p>Result: ${s.result}</p>
        </div>`).join("");
    })
    .catch(e=>{console.error(e);container.innerHTML="Could not connect to backend. Check the ALB/API URL.";});
}
