proc1 = proc { |x| x * 2 }
proc2 = proc1 

def m1(a, &block)
  block[a]
end

def m2(a)
	yield proce1[a]
end

p m1(1, &proc1)
p m1(1, &proc1)

def m2(a)
 proc { |x| x * 2 }
end


p m2(2)