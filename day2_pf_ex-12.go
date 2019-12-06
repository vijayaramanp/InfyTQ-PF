//PF-Exer-12
//This verification is based on string match.

package main
import ("fmt")
func main(){
    //Write your program logic here
    var n1 int=3 
    var n2 int=4 
    var n3 int=1 
    if(n1>n2 && n1>n3){
        fmt.Println(n1)
    }else if(n2>n3){
        fmt.Println(n2)
    }else{
        fmt.Println(n3)
    }
}
