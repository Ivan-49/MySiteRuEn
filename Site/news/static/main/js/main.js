var elms = document.getElementsByClassName('header_a');
var pathname = window.location.pathname;

var lang_button = document.getElementById('lang_button');
var lang_a = document.getElementById('lang_a');

if (pathname.substring(0,4) == '/en/') {
    var lang = '/en';
    lang_button.innerHTML = 'ru';
}
else{
    lang_button.innerHTML = 'en';
}


for (var i = 0; i < elms.length; i++) {
    elm = elms[i];
    if (lang){
        elm.setAttribute('href',  lang + '/' + elm.getAttribute('id'));
    }else{
       elm.setAttribute('href', '/' + elm.getAttribute('id'));
    }
    
};



function changeLang() {

    var href = window.location.pathname;
    // console.log(href);
    if (href.substring(0,4) == '/en/') {
        lang = 'en';
    }
    else{
        lang = 'ru';
    }

    // console.log(lang);
    // console.log(href);

    if (lang == 'en') {
        
        // console.log('http://127.0.0.1:8000/' + href.substring(4));
        location.replace('http://192.168.3.18:8000/' + href.substring(4));
    }else{

        // console.log('http://127.0.0.1:8000/en' + href);
        location.replace('http://192.168.3.18:8000/en' + href);
    }
}

lang_button.addEventListener('click', function handleClick() {
    changeLang();
  });