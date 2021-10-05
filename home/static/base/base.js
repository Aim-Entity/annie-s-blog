function phoneNav() {
  let hamburger = document.querySelector(".hamburger")
  let dropdown = document.querySelector(".nav-dropdown")

  hamburger.addEventListener("click", (e) => {
    // dropdown.classList.toggle("nav-dropdown")
    dropdown.classList.toggle("nav-dropdown-active")
  })
}

phoneNav()