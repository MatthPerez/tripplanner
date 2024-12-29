const activities = document
  .getElementById('activities')
  .getElementsByTagName('li')

function hide_activities () {
  Array.from(activities).forEach(el => {
    el.classList.add('d-none')
  })
}

function show_activities (destination) {
  hide_activities()

  Array.from(activities).forEach(el => {
    let my_value = el.getElementsByTagName('label')[0].textContent
    if (my_value.includes(destination)) {
      el.classList.remove('d-none')
    }
  })
}

function trip_main () {
  Array.from(activities).forEach(el => {
    const selectElement = document.getElementById('id_place')

    // Changement de sélection
    selectElement.addEventListener('change', function () {
      const selectedValue = this.value
      // console.log('Valeur sélectionnée:', selectedValue)
      show_activities(selectedValue)
    })

    // Valeur initiale au chargement de la page
    window.addEventListener('load', function () {
      const initialValue = selectElement.value
      // console.log('Valeur sélectionnée initiale:', initialValue)
      show_activities(initialValue)
    })
  })
}

trip_main()
