/*
jQuery Words highlighter 

Highlights arbitrary terms.
case sensitive
words only

MIT license.

Ryan Wang
<http://programcreek.com>
<mailto:contact@programcreek.com>
*/

jQuery.fn.highlight = function(pat) {
	
	function innerHighlight(node, pat) {
	  var html = node.innerHTML;
	  var rexp = new RegExp( '\\b('+pat+')\\b', 'gm' );
	  html = html.replace( rexp, '<span class="highlight">$1</span>' );
	  node.innerHTML = html;
	}
 
	 return this.length && pat && pat.length ? this.each(function() {
	  innerHighlight(this, pat);
	 }) : this;
	 
};
