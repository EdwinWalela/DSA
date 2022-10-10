function containsDuplicate(list){
    const map = new Map();

    for(let i = 0; i < list.length; i++ ){
        let currVal = map.get(list[i])
        if(typeof currVal == 'undefined'){
          map.set(list[i],1)
        }else{
         return true
        }
    }

    return false
}


const list = [1,2,4,3]

console.log(containsDuplicate(list))

