function logNewQuery(addr) {
  let ul = document.getElementById("logs");
  let li = document.createElement("li");
  li.appendChild(document.createTextNode("Querying " + addr));
  let ol = document.createElement("ol");
  li.appendChild(ol);
  ul.appendChild(li);
  return ol;
}

function logNode(olElem, node) {
  let li = document.createElement("li");
  let text = '';
  if('name' in node) {
    text = node['name'] + ' (' + node['addr'] + ')';
  } else {
    text = node['addr']
  }
  text += '  delay (ms): ';
  for(let i = 0; i < node['delays'].length; i++) {
    text += node['delays'][i] + ' ';
  }
  li.appendChild(document.createTextNode(text));
  olElem.appendChild(li);
}

function logStatus(olElem, status) {
  let li = document.createElement("li");
  li.appendChild(document.createTextNode(status));
  olElem.appendChild(li);
}

var nodeDict = {};

$(document).on('click', '#query-btn', function() {
  let target = document.getElementById('target').value;
  $.post("/api/traceroute/request", {
    target: target
  }, function (data) {
    console.log(data);
    document.getElementById('query-btn').disabled = true;
    let olElem = logNewQuery(target);
    let previousNum = 0;
    let previousNode = null;

    let refreshIntervalId = setInterval(function() {
      $.get("/api/traceroute/result?task_id="+data['task_id'], function(data2) {
        if(data2['status'] === 'timeout') {
          previousNode.data.color = 'orange';
          logStatus(olElem, 'timeout requests');
          document.getElementById('query-btn').disabled = false;
          clearInterval(refreshIntervalId);
        }

        let currNum = data2['nodes'].length;
        let newNode = null;

        if(currNum > previousNum) {
          let newNodeData = data2['nodes'][currNum-1];
          console.log(newNodeData);
          logNode(olElem, newNodeData);

          if(newNodeData['addr'] in nodeDict) { // it already exists
            newNode = nodeDict[newNodeData['addr']];

            
            if(previousNode === null) {
              newNode.data.color = "purple";
            } else {
              graph.newEdge(previousNode, newNode, {color: '#00A0B0'});
            }
          } else {
            newNode = graph.newNode({
              label: newNodeData['addr'],
              font: "10px Arial"
            });
            nodeDict[newNodeData['addr']] = newNode;

            if(previousNode === null) {
              newNode.data.color = "purple";
            } else {
              graph.newEdge(previousNode, newNode, {color: '#00A0B0'});
            }
          }

          previousNum = currNum;
          previousNode = newNode;

        }

        if(data2['status'] === 'success') {
          newNode.data.color = 'green';
          logStatus(olElem, 'destination reached');
          document.getElementById('query-btn').disabled = false;
          clearInterval(refreshIntervalId);
        }
      });
    }, 1000);

  });
});

var graph = new Springy.Graph();

jQuery(function(){
  var springy = window.springy = jQuery('#springydemo').springy({
    graph: graph,
    nodeSelected: function(node){
      console.log('Node selected: ' + JSON.stringify(node.data));
    }
  });
});
