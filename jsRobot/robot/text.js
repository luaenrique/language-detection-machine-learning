const algorithmia = require('algorithmia')
const algorithmiaApiKey = require('../credentials/algorithmia.json').apiKey
const sentenceBoundaryDetection = require('sbd')
const robotOrganizer = require('./dataOrganizer.js')


async function robot(content) {
    await fetchTextData(content)
    sanitizeContent(content)
    breakContentIntoSentences(content)


    async function fetchTextData(content) {
        const algorithmiaAuthenticated = algorithmia(algorithmiaApiKey)
        const textAlgorithm = algorithmiaAuthenticated.algo('web/WikipediaParser/0.1.2')
        const textResponse = await textAlgorithm.pipe({
            "articleName": content.searchTerm,
            "lang": content.lang
          })
        const textContent  = textResponse.get()

        content.sourceContentOriginal = textContent.content
    }

    function sanitizeContent(content) {
        const withoutBlankLinesAndMarkdown = removeBlankLinesAndMarkdown(content.sourceContentOriginal)
        const withoutDatesInParentheses = removeDatesInParentheses(withoutBlankLinesAndMarkdown)
    
        content.sourceContentSanitized = withoutDatesInParentheses
        
        //console.log(content.sourceContentSanitized)

        function removeBlankLinesAndMarkdown(text) {
          const allLines = text.split('\n')
    
          const withoutBlankLinesAndMarkdown = allLines.filter((line) => {
            if (line.trim().length === 0 || line.trim().startsWith('=')) {
              return false
            }
    
            return true
          })
    
          return withoutBlankLinesAndMarkdown.join(' ')
        }
    }

    function removeDatesInParentheses(text) {
        return text.replace(/\((?:\([^()]*\)|[^()])*\)/gm, '').replace(/  /g,' ')
    }
    
    function breakContentIntoSentences(content) {
        var lang = content.lang
        const sentences = sentenceBoundaryDetection.sentences(content.sourceContentSanitized)
        sentences.forEach((sentence) => {
            content = {
                "sentence": sentence,
                "language": lang
            }
            robotOrganizer(content)
        })
    }

}


module.exports = robot