// Swift Data Types
// Modify the following statements
var a  = 123 //optimized signed int
var b: String = 'Hello' // String value
var c = "S" // a character
var d = 0b111100110 // optimized signed int
var e = "true" //a boolean value
var f = 3.1415 //optimize 32 bit floating point value 
var g: Float = Double.pi // correct explicit type
var h: Int = Int("123") // an optional int 
var i: Int8 = 255 // optimize unsigned int type
var j: Int = 4_294_967_295 //optimize unsigned int type


// Do not change the code beyond this line
printType(a)
printType(b)
printType(c)
printType(d)
printType(e)
printType(f)
printType(g)
printType(h)
printType(i)
printType(j)

func printType(_ value: Any) {
    let t = type(of: value)
    print("\(value) of type \(t)")
}