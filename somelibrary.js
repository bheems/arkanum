// Collects all emails in a web page, returns array with emails (in String format)

function getEmails() {

var search_in = document.body.innerHTML;
string_context = search_in.toString();

array_mails = string_context.match(/([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9._-]+)/gi);
return array_mails;

}