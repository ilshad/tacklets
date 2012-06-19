(function($){
    window.addMarkdownFormattingToolbar = function(textarea) {

	if ((document.selection == undefined) &&
	    (textarea.setSelectionRange == undefined)
	   ) {return;}

	var toolbar = document.createElement("div");
	toolbar.className = "markdown-formatting-toolbar";

	function addButton(id, title, fn) {
	    var a = document.createElement("a");
	    a.href = "#";
	    a.id = id;
	    a.title = title;
	    a.innerHTML = "&nbsp;";
	    a.onclick = function() {
		try { fn(); }
		catch (e) { }
		return false;
	    };
	    a.tabIndex = 400;
	    toolbar.appendChild(a);
	}

	function encloseSelection(prefix, suffix) {
	    textarea.focus();
	    var start, end, sel, scrollPos, subst;
	    if (document.selection != undefined) {
		sel = document.selection.createRange().text;
	    } else if (textarea.setSelectionRange != undefined) {
		start = textarea.selectionStart;
		end = textarea.selectionEnd;
		scrollPos = textarea.scrollTop;
		sel = textarea.value.substring(start, end);
	    }
	    if (sel.match(/ $/)) { // exclude ending space char, if any
		sel = sel.substring(0, sel.length - 1);
		suffix = suffix + " ";
	    }
	    subst = prefix + sel + suffix;
	    if (document.selection != undefined) {
		var range = document.selection.createRange().text = subst;
		textarea.caretPos -= suffix.length;
	    } else if (textarea.setSelectionRange != undefined) {
		textarea.value = textarea.value.substring(0, start) +
		    subst + textarea.value.substring(end);
		if (sel) {
		    textarea.setSelectionRange(start + subst.length, start + subst.length);
		} else {
		    textarea.setSelectionRange(start + prefix.length, start + prefix.length);
		}
		textarea.scrollTop = scrollPos;
	    }
	}

	addButton(
	    "strong",
	    "Bold text: **Example**",
	    function() {
		encloseSelection("**", "**");
	    }
	);

	addButton(
	    "em",
	    "Italic text: *Example*",
	    function() {
		encloseSelection("*", "*");
	    }
	);

	addButton(
	    "heading",
	    "Heading: ## Example",
	    function() {
		encloseSelection("## ", "\n", "Heading");
	    }
	);

	/*addButton(
	    "link",
	    "Link: <http://www.example.com>",
	    function() {
		encloseSelection("<", ">");
	    }
	);*/

	$(textarea).before(toolbar);
    };

})(jQuery);

var update_markdown_input = function() {
    $('div.markdown-input > textarea').each(
	function() {
	    addMarkdownFormattingToolbar(this);
	}
    );
};

$(function($) {
      update_markdown_input();
  });

$(function() {
      $('textarea.resizable:not(.processed)').TextAreaResizer();
      $('iframe.resizable:not(.processed)').TextAreaResizer();
  });

var markdown_update = function () {
      update_markdown_input();
      $('textarea.resizable:not(.processed)').TextAreaResizer();
      $('iframe.resizable:not(.processed)').TextAreaResizer();
};
