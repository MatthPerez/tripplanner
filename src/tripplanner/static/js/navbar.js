function main () {
  const logoBar = document.getElementById('logo')
  const logo = logoBar.getElementsByTagName('div')[1]
  const menu = document.getElementById('menu')

  logo.addEventListener('click', () => {
    menu.classList.toggle('visible')
    logoBar.classList.toggle('hamburger-active')
  })
}

main()
