/**
*
* todo.js is part of Tackle software
* 2010 Ilshad Khabibullin <astoon@spacta.com>
*
**/

var TODO = function () {};

TODO.prototype.show_add = function (anchor) {

    var place = anchor.parentNode.parentNode.childNodes[5];
    place.setAttribute("style", "display:inline");
};

TODO.prototype.hide = function (anchor) {

    var place = anchor.parentNode;
    place.setAttribute("style", "display:none");
};

TODO.prototype.add = function (anchor, context_url) {

    var place = anchor.parentNode.parentNode.childNodes[9];
    var textarea = anchor.parentNode.childNodes[1];
    var subject = textarea.value;
    var xmlhttp = this.getXmlHttp();
    var self = this;

    xmlhttp.open('POST', context_url + '/@@todo_add', true);
    xmlhttp.setRequestHeader(
	'Content-Type',
	'application/x-www-form-urlencoded');
    xmlhttp.send('subject=' + encodeURIComponent(subject));

    xmlhttp.onreadystatechange = function () {
	if (xmlhttp.readyState == 4) {
	    if(xmlhttp.status == 200) {
		textarea.value = null;
		self.hide(anchor);
		self.load_listing(place, context_url);
            }
	}
    };
};

TODO.prototype.load_listing = function (place, context_url) {
    var xmlhttp = this.getXmlHttp();

    xmlhttp.open('GET', context_url + '/@@todo_listing', true);
    xmlhttp.send(null);

    xmlhttp.onreadystatechange = function () {
	if (xmlhttp.readyState == 4) {
	    if(xmlhttp.status == 200) {
		place.innerHTML = xmlhttp.responseText;
	    }
	}
    };
};

TODO.prototype.change = function (anchor, context_url, key) {

    var place = anchor.parentNode.parentNode.parentNode.parentNode.childNodes[7];
    var xmlhttp = this.getXmlHttp();
    var self = this;

    xmlhttp.open('GET', context_url + '/@@todo_change?item_key=' + encodeURIComponent(key), true);
    xmlhttp.send();

    xmlhttp.onreadystatechange = function () {
	if (xmlhttp.readyState == 4) {
	    if(xmlhttp.status == 200) {
		place.innerHTML = xmlhttp.responseText;
	    }
	}
    };
};

TODO.prototype.on_change = function (anchor, context_url) {

    var form = anchor.parentNode;
    var subject = form.elements.subject.value;
    var item_key = form.elements.item_key.value;
    var closed = form.elements.closed.checked;
    var xmlhttp = this.getXmlHttp();
    var place = form.parentNode.parentNode.childNodes[9];
    var self = this;

    xmlhttp.open('POST', context_url + '/@@todo_change', true);
    xmlhttp.setRequestHeader(
	'Content-Type',
	'application/x-www-form-urlencoded');
    xmlhttp.send('subject=' + encodeURIComponent(subject) +
		 '&item_key=' + encodeURIComponent(item_key) +
		 '&closed=' + closed);

    xmlhttp.onreadystatechange = function () {
	if (xmlhttp.readyState == 4) {
	    if(xmlhttp.status == 200) {
		self.hide(anchor);
		self.load_listing(place, context_url);
	    }
	}
    };
};

TODO.prototype.remove = function (anchor, context_url) {

    var form = anchor.parentNode;
    var item_key = form.elements.item_key.value;
    var xmlhttp = this.getXmlHttp();
    var place = form.parentNode.parentNode.childNodes[9];
    var self = this;

    xmlhttp.open('POST', context_url + '/@@todo_remove', true);
    xmlhttp.setRequestHeader(
	'Content-Type',
	'application/x-www-form-urlencoded');
    xmlhttp.send('item_key=' + encodeURIComponent(item_key));

    xmlhttp.onreadystatechange = function () {
	if (xmlhttp.readyState == 4) {
	    if(xmlhttp.status == 200) {
		self.hide(anchor);
		self.load_listing(place, context_url);
	    }
	}
    };
};

TODO.prototype.getXmlHttp = function () {
    var xmlhttp;
    try {
	xmlhttp = new ActiveXObject("Msxml2.XMLHTTP");
    } catch (e) {
	try {
	    xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
	} catch (E) {
	    xmlhttp = false;
	}
    }
    if (!xmlhttp && typeof XMLHttpRequest!='undefined') {
	xmlhttp = new XMLHttpRequest();
    }
    return xmlhttp;
};

todo = new TODO();
