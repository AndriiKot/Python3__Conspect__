# Ruby-lesson-1-vs-Js
Ruby Lesson 1 (vs Js)
```Ruby
=begin
JS
  console.log("Hello world!") // Hello world!
  console.log( 13 + 23)       // 36    typeof numeric
  console.log("13" + "23")    // 1323  typeof string
  console.log("13" + 23)      // 1323  typeof string
  console.log(13 + '23')      // 1323  typeof string
=end

#Ruby
puts "Hello world!"       #  Hello world!
p    'Hello world!'       # "Hello wrold!"

p     13 + 23             # 36
p    '13' + '23'          # "1323"

# p    '13' + 23          # TypeError !!!
# p     13  + '23'        # TypeError !!!

a,b,c,d = 1,'2',[],{}

p [a,b,c,d]               #  [1,"2",[],{}]

arr = a,b,c,d
p arr.class               # Array
p arr.size                # 4

p arr.map(&:class)        #[Integer,String,Array,Hash]
p arr                     #[1,"2",[],{}]

arr.map!(&:class)
p arr                     # !!! [Integer,String,Array,Hash]

=begin 
JS
let my_first_name
let my_last_name
let full_name

my_first_name = "Andrii"
my_last_name = 'Kotsiuba'
full_name = my_first_name + ' ' + my_last_name 

console.log(full_name)                          // Andrii Kotsiuba
=end

#Ruby
my_first_name,my_last_name = 'Andrii','Kotsiuba'
full_name = my_first_name + ' ' + my_last_name

p full_name        # "Andrii Kotsiuba"


=begin
JS
console.log(9/5)  // 1.8  !!!!!!!

let i = 5
let x = 8
console.log(i++)  // 5  !!!!!!!!!
console.log(i)    // 6   
console.log(++x)  // 9
console.log(x)    // 9 

let z = 6
let y = 3 
console.log(z--) // 6  !!!!!!!
console.log(z)   // 5

console.log(--y) // 2
console.log(y)   // 2

let a = 1
let b = 1
b += 1
a = a + 1
=end
```
____
```node
// JS
9 / 5   => 1.8 !!!!
```
____
```ruby
#Ruby
p  9 / 5       # !!! 1
p  9 / 5.0     # !!! 1.8
p  9.0 / 5     # !!! 1.8
p  9.0 / 5.0   # !!! 1.8

p  5 * 9       # 45
p  5.0 * 9     # 45.0
p  5 * 9.0     # 45.0
p  5.0 * 9.0   # 45.0

a,b = 1,1

a += 1
b = b + 1

p a            # 2
p b            # 2

a,b = 2,5
a,b = b,a      # !!!
p a            # 5
p b            # 2 


a = 10
#  a++    syntax error
#  a--    syntax error
p --a     # 10
p ++a     # 10
```











   
