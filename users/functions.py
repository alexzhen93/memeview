from django.db.models.expressions import Func
from django.db.models.lookups import Transform

# accepts a single text field or expression and returns the lowercase representation
class Lower(Transform):
	function = 'LOWER'
	lookup_name = 'lower'

# replaces all occurences of text with replacement in expression
class Replace(Func):
	function = 'REPLACE'

	def __init__(self, expression, text, replacement=Value(''), **extra):
		super().__init__(expression, text, replacement, **extra)

# accepts a single text field or expression and returns the uppercase representation
class Upper(Transform):
	function = 'UPPER'
	lookup_name = 'upper'