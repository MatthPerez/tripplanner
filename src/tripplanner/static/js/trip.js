const activities = document
  .getElementById('activities')
  .getElementsByTagName('li')

const airbnbs = document
  .getElementById('airbnbs')
  .getElementsByTagName('li')

function hide_airbnbs () {
  Array.from(airbnbs).forEach(el => {
    el.classList.add('d-none')
  })
}

function hide_activities () {
  Array.from(activities).forEach(el => {
    el.classList.add('d-none')
  })
}

function show_airbnbs (destination) {
  hide_airbnbs()

  Array.from(airbnbs).forEach(el => {
    let my_value = el.getElementsByTagName('label')[0].textContent
    if (my_value.includes(destination)) {
      el.classList.remove('d-none')
    }
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
  Array.from(airbnbs).forEach(() => {
    const selectElement = document.getElementById('id_place')

    // Selection change
    selectElement.addEventListener('change', function () {
      const selectedValue = this.value
      show_airbnbs(selectedValue)
    })

    // Initial value while thepage is loading
    window.addEventListener('load', function () {
      const initialValue = selectElement.value
      show_airbnbs(initialValue)
    })
  })

  Array.from(activities).forEach(() => {
    const selectElement = document.getElementById('id_place')

    // Selection change
    selectElement.addEventListener('change', function () {
      const selectedValue = this.value
      show_activities(selectedValue)
    })

    // Initial value while thepage is loading
    window.addEventListener('load', function () {
      const initialValue = selectElement.value
      show_activities(initialValue)
    })
  })
}

trip_main()
