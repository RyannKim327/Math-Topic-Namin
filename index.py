# ito naman kapag naka table
class logical_connectives_and_proportional_logic:
	def __init__(self, p, q):
		self.p = p
		self.q = q
	
	def get_p(self):
		return self.p

	def get_q(self):
		return self.q
	
	def negation(self, x):
		return not x
	
	def compound(self):
		return self.p and self.q
	
	def disjunction(self):
		return self.p or self.q
	
	def implication(self):
		if self.p and not self.q:
			return False
		else:
			return True
	
	def biimpication(self):
		return self.p == self.q
	
	def short(self, x):
		if x:
			return "T"
		else:
			return "F"


print(f"|	P	|	Q	|	~P	|	~Q	|	∧	|	v	|	⇒	|	↔	|")

p = [True, True, False, False]
q = [True, False, True, False]
for i in range(len(p)):

	math = logical_connectives_and_proportional_logic(p[i], q[i])
	print(f"|	{math.short(math.get_p())}	|	{math.short(math.get_q())}	|	{math.short(math.negation(math.get_p()))}	|	{math.short(math.negation(math.get_q()))}	|	{math.short(math.compound())}	|	{math.short(math.disjunction())}	|	{math.short(math.implication())}	|	{math.short(math.biimpication())}	|")
