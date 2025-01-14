const select = document.getElementById('destinations')
const elements = document
  .getElementsByClassName('act_el')

function act_main () {
  hide_elements()
  select_element()
}

function hide_elements () {
  Array.from(elements).forEach(el => {
    el.classList.add('d-none')
  })
}

function show_elements (reference) {
  Array.from(elements).forEach(el => {
    if (el.id.includes(reference)) {
      el.classList.remove('d-none')
    }
  })
}

function select_element () {
  hide_elements()

  select.addEventListener('change', () => {
    hide_elements()
    const selectedValue = select.options[select.selectedIndex]
    // console.log(`Activité sélectionnée : ${selectedValue.value}`)

    show_elements(selectedValue.value)
  })
}

act_main()
