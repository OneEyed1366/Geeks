const toBuy = {
  milk: 6,
  sugar: 10,
  potato: 2,
  pineapple: 15,
  bread: 2
}

function constBeakerPrice (products) {
  let result = 0

  for (const key in products) {
    result += products[key]

    console.log(`${key} -> ok...`)
  }

  console.log(`Whew... This little trip costs my smth about ${result}$...`)
}

constBeakerPrice(toBuy)