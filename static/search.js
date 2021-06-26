
/*
document.addEventListener("DOMContentLoaded", stateData);



function stateData(){
	document.getElementById('sd').innerHTML = '';
	var request = new XMLHttpRequest();
	request.onreadystatechange = function(){
		if(this.readyState == 4){
			var result = JSON.parse(request.responseText)
		}
	}
	request.open("POST", "/state");
	request.setRequestHeader("Content-Type","application/json");
	request.send(JSON.stringify(json));
}
*/

function searchSend() {
	document.getElementById('result2').innerHTML = '';
	var json = {};
	var r = document.getElementById('race').value;
	var p = document.getElementById('perc').value;
	if (p>100) {
		p = 100;
	}
	if (p<50) {
		p = 50;
	}
	json.r = r;
	json.p = p;
	var request = new XMLHttpRequest();
	request.onreadystatechange = function(){
		if(this.readyState == 4){
			var result = JSON.parse(request.responseText);
			res = ""
			if (result.a.length == 0) {
				res = "No results found."
			}
			else{
				res+= "<table><tr><th>County</th><th>Jurisdiction</th><th>Precinct</th><th>Majority Party</th></tr>"
				for (var i = result.a.length - 1; i >= 0; i--) {
					res+= "<tr>"
					res+= "<td>"+result.a[i][0]+"</td><td>"+result.a[i][1]+"</td><td>"+result.a[i][2]+"</td>"+"</td><td>"+result.a[i][3]+"</td>"
					res+= "</tr>"
				}
				res+= "</table>"
			}
			document.getElementById('result2').innerHTML = res;
		}
	}
	request.open("POST", "/search");
	request.setRequestHeader("Content-Type","application/json");
	request.send(JSON.stringify(json));
}