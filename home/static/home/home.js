function returnHiddenBlogs(){
  let HiddenBlogs = []
  let blogs = document.querySelectorAll(".blogs")[0].children;
  var HiddenBlogsCount = blogs.length - 3;

  if(HiddenBlogsCount < 1) {
    null
  } else {
    for(let i = 3; i < HiddenBlogsCount + 3; i++) {
      HiddenBlogs.push(blogs[i]);
    };
  };

  return HiddenBlogs;
}

function loadBlogs() {
  let HiddenBlogs = document.querySelector(".hidden-blogs");

  let loadBtn = document.querySelector(".s2-btn");

  // for(let i = 0; i < HiddenBlogs.length; i++) {
  //   HiddenBlogs[i].classList.toggle("blog-cont-remove");
  //   HiddenBlogs[i].classList.toggle("blog-cont-hidden");

  //   HiddenBlogs[i].classList.toggle("blog-cont");

  //   loadBtn.innerHTML = "More Blogs";
  // };

  loadBtn.addEventListener("click", e => {
    HiddenBlogs.classList.toggle("hidden-blogs");

    if(loadBtn.innerHTML == "More Blogs") {
      loadBtn.innerHTML = "Less Blogs";
    }
    else{
      loadBtn.innerHTML = "More Blogs";
    };
  });
};

function animateBlogs() {
  let blogs = document.querySelectorAll(".blog-cont");
  
  if(window.innerWidth > 900) {
    for(let i = 0; i < blogs.length; i++) {
      blogs[i].style.opacity = 0
      blogs[i].style.position = "relative";
      blogs[i].style.top = "75px";
    };
  
    let state = 0;
  
    document.addEventListener("scroll", e => {
      let scrollNumber = window.scrollY;
  
      if(scrollNumber >= 400 && state == 0){
        state = 1;
        
        gsap.to(blogs, {duration: 0.90, y: "-75px", opacity: 1, ease: "Back.easeOut", stagger: 0.25});
      };
    })
  };
};

function btnAppear() {
  let btns = document.querySelectorAll(".affiliate-btn-container");
  let state = 0;

  if(window.innerWidth > 900) {
    for(let i = 0; i < btns.length; i++) {
      btns[i].style.opacity = 0;

      btns[i].parentNode.parentNode.addEventListener("mouseenter", e => {
        if(state == 0) {
          gsap.to(e.target.children[0].children[1], {duration: 0.90, opacity: 1, ease: "Back.easeOut"});
          state = 1;
        }
      });

      btns[i].parentNode.parentNode.addEventListener("mouseout", e => {
        console.log(e.target.children[1].className)
        if(e.target.children[1].className == "affiliate-btn-container" || e.target.children[1].className == "") {
          console.log("hover")
        }
        else{
          gsap.to(e.target.children[1], {duration: 0.90, opacity: 0, ease: "Back.easeOut"});
          state = 0
        }
      });
    };
  };
};

// btnAppear();
loadBlogs();
animateBlogs();