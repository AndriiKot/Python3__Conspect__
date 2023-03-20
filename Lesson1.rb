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
p    '13' + '23'         # "1323"

# p    '13' + 23           # TypeError !!!
# p     13  + '23'         # TypeError !!!

a,b,c,d = 1,'2',[],{}

p [a,b,c,d]           #  [1,"2",[],{}]

arr = a,b,c,d
p arr.class           # Array
p arr.size            # 4

p arr.map(&:class)    #[Integer,String,Array,Hash]
p arr                 #[1,"2",[],{}]

arr.map!(&:class)
p arr                 # !!! [Integer,String,Array,Hash]








   