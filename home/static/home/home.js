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
  let HiddenBlogs = returnHiddenBlogs();

  let loadBtn = document.querySelector(".s2-btn");

  for(let i = 0; i < HiddenBlogs.length; i++) {
    HiddenBlogs[i].classList.toggle("blog-cont-remove");
    HiddenBlogs[i].classList.toggle("blog-cont-hidden");

    HiddenBlogs[i].classList.toggle("blog-cont");

    loadBtn.innerHTML = "More Blogs";
  };

  loadBtn.addEventListener("click", e => {
    for(let i = 0; i < HiddenBlogs.length; i++) {
      HiddenBlogs[i].classList.toggle("blog-cont-remove");
      HiddenBlogs[i].classList.toggle("blog-cont-hidden");
  
      HiddenBlogs[i].classList.toggle("blog-cont");

      loadBtn.innerHTML = "Less Blogs";
    };
  });
};

loadBlogs();