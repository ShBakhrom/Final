
let currentImageInputNumber = 0;


function validateAndUpload(input){
    if (input.files[0].type.substring(0, 5) === 'image'){
        return input.files[0].name
    }else{
        return null
    }
}
// document.getElementsByClassName('box__file').item(0).addEventListener('change', function(){
//     let imageName = validateAndUpload(this);
//     if (imageName){
//         console.log(imageName)
//     }else{
//
//         this.value=''
//         console.log('not image')
//     }
// })

function moveToTheNextImage(imageIndex){
    let input = document.getElementsByClassName('dragDropFrame').item(imageIndex);
    if (input != null){
        if (imageIndex > 0){
            //CLEAR UP
            document.getElementsByClassName('dragDropFrame').item(imageIndex-1).style.display = 'none';
        }
        input.style.display = 'block';
        input.getElementsByClassName('dragDropBox').item(0).addEventListener('change', function(){
             let imageName = validateAndUpload(this);
             if (imageName){
                 let pTag = document.createElement('p');
                 pTag.innerHTML = imageName;
                 document.getElementById('allImageInputs').insertBefore(pTag, input);
                 currentImageInputNumber++;
                 document.getElementsByClassName('dragDropFrame').item(0).style.display = 'none';
             }else{
    
                 this.value=''
                 console.log('not image')
             }
         })
    }
}
let submitButton = document.getElementById('submitForm');
if (document.getElementById("quote_form") != null){
    formLogic()
}
moveToTheNextImage(currentImageInputNumber);

function formLogic(){
    let firstName = document.getElementById('id_fistName');
    

    let lastName = document.getElementById('id_lastName');
    

  
    


    submitButton.addEventListener('click', (e)=>{
        let inputs = [firstName, lastName]
        for (i of inputs){
            if (i.value == ''){
                return;
            }
        }
        if (!submitButton.disabled){
            document.getElementById('quote_form').style.opacity = 0.2;
            document.getElementsByClassName('loading').item(0).style.display = "flex";
        }
    })
}
