//JS-Exer-25

//Start writing your code here

function find_sum(n){
    var i,sum=0;
    for(i=1;i<=n;i++){
        sum=sum+i
    }
    return sum;
}


var n=6,res=0;
res=find_sum(n);
console.log(res);

