var count = { text: ""};
setInterval(function() {
  var xhr = new XMLHttpRequest();
  xhr.open('GET', 'text.txt', false);
  xhr.send();
  if (xhr.status != 200) {
    console.log(xhr.status)
  } else {
    count.text = xhr.responseText
    chrome.browserAction.setBadgeText(count)
  }
}, 1000); 
