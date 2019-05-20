var char_list = ""
function getNameImgData() {
  var scrape_url = `/obtainData`
  var xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function(){
    if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
      char_list = JSON.parse(xhr.responseText)
    } 
  }; 
  xhr.open("GET", scrape_url, true); 
  xhr.send("");
};

function getData(event){
  var element = event.target;
  var input_char_name = element.getAttribute("char_name")
  for(index=0; index<=char_list.length;index++ ){
    if (char_list[index]["name"] == input_char_name) {
      var imgurl = char_list[index]["img_url"]
      document.getElementById("img").src=imgurl
      var imgid = document.getElementById("img")
      imgid.height = 325;
      imgid.width = 325;
      createGraph(char_list[index]["date"], char_list[index]["polarity"])
    }
  }
};

function createGraph(date, polarity) {
  // console.log(date)
  // console.log(polarity)
  var trace1 = {
    x: date,
    y: polarity,
    type: "scatter",
    name: "Polarity"
  }

  data = [trace1]
  layout = {
    title: "Polarity of Character",
    xaxis: {
      title: "Date"
    },
    yaxis: {
      title: "Polarity"
    }
  }
  Plotly.newPlot("graph", data, layout)
};

getNameImgData();