const toBuy = [
  ['Milk', 200],
  ['Sugar', 150],
  ['Potato', 225],
  ['Pineapple', 445],
  ['Bread', 40]
]

function countBasketPrice (products) {
  let result = 0

  for (let i = 0; i < products.length; i++) {
    console.log(`${products[i][0]} - ok...`)
    result += products[i][1]
  }

  console.log(`Total: ${result} rub. How would you pay?`)
}

countBasketPrice(toBuy)