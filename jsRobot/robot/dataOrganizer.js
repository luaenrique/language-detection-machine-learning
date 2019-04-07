const fs = require('fs')
const uniqid = require('uniqid');




function robotOrganizer(content) {
    writeNewFile(content)


    function writeNewFile(content){
        var fileName = uniqid();
        fs.appendFile("GeneratedData/"+content.language+"/"+fileName+".txt", content.sentence, function (err) {
            if (err) throw err;
            console.log('file '+fileName+'.txt saved');
        });

    }
    
  
}

module.exports = robotOrganizer