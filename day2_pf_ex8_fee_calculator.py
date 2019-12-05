//PF-Exer-8
//This verification is based on string match.

package main
import ("fmt")
func main(){
    var finalFee int=0
    //Write your program logic here
    //Populate the variable: finalFee
    var courseFee int=25000
    var marks float32=70 
    var extraFee int=1500
    var scholarship float32=float32(courseFee)*((marks/2)/100.0)
    finalFee=courseFee+extraFee-int(scholarship)
    
     //Do not modify the below print statement for verification to work
     fmt.Println(finalFee) 
}
