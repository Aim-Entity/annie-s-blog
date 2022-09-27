function pagination(){
  let elements = document.querySelectorAll("form")[0].children;
  let pag1 = document.querySelector(".pag1");
  let pag2 = document.querySelector(".pag2");
  let state = 0;

  let firstHalf = [];
  let secondHalf = [];
  for(let i = 0; i < 9; i++) {
    firstHalf.push(elements[i]);
  }

  for(let i = 9; i < 13; i++) {
    secondHalf.push(elements[i]);
  }

  secondHalf.push(elements[14]);

  for(let i = 0; i < secondHalf.length; i++) {
    secondHalf[i].style.display = "none";
  };


  pag2.addEventListener("click", e => {
    if(state == 1) {
      console.log("Pass")
    }
    else {
      state = 1;
      for(let i = 0; i < firstHalf.length; i++) {
        firstHalf[i].style.display = "none";
      };

      for(let i = 0; i < secondHalf.length; i++) {
        secondHalf[i].style.display = "block";
      };

      pag2.style.background = "#81b29a";
      pag1.style.background = "none";
    };
  });
  
  pag1.addEventListener("click", e => {
    if(state == 0) {
      console.log("Pass");
    }
    else {
      state = 0;
      for(let i = 0; i < secondHalf.length; i++) {
        secondHalf[i].style.display = "none";
      };

      for(let i = 0; i < firstHalf.length; i++) {
        firstHalf[i].style.display = "block";
      };

      pag1.style.background = "#81b29a";
      pag2.style.background = "none";
    }
  })
};

pagination();