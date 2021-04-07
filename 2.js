const shoppingDonor = document.getElementById('shoppingCartToInsert')
const catalogDonor = document.getElementById('catalogToInsert')
const products = {
  milk: 5,
  bread: 1,
  souce: 9,
  dress: 25
}

function getCatalog (items = products) {
  const listOl = document.createElement('ol')

  for (let item in items) {
    const listLi = document.createElement('li')

    listLi.innerHTML = `${item}: ${items[item]}$`
    listOl.appendChild(listLi)
  }

  document.getElementById('catalogToInsert').appendChild(listOl)
}

function calcShoppingCart () {
  const count = Math.floor(Math.random() * (Object.keys(products).length - 1 + 1)) + 0
  let result = 0
  let i = 0

  for (const product in products) {
    result += products[product]

    if (i === count) {
      if (i === 0) {
        shoppingDonor.innerHTML = 'В Вашей корзине нет товаров!'
      } else {
        shoppingDonor.innerHTML = `Количество товаров: ${i}<br />Общая сумма покупок: ${result}$`
      }

      break
    }
    
    i++
  }
}

getCatalog()
calcShoppingCart()