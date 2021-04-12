const shoppingDonor = document.getElementById('shoppingCartToInsert')
const catalogDonor = document.getElementById('catalogToInsert')
const colors = [
  'green',
  'lightblue',
  'pink'
]
const products = {
  milk: {
    price: 5,
    url: 'https://xn-----7kcbekeiftdh9amwkb4d2o.xn--p1ai/wp-content/uploads/2019/10/80d5dc6eac.jpg'
  },
  bread: {
    price: 1,
    url: 'https://vestirama.ru/assets/templates/images/photo/b71f9f9e9935953f16109929689476dc.jpg'
  },
  souce: {
    price: 9,
    url: 'https://i.pinimg.com/736x/a9/95/fc/a995fc566252ce3e50192562999456ac--italian-tomato-sauce-tomato-cream-sauces.jpg'
  },
  dress: {
    price: 25,
    url: 'https://avatars.mds.yandex.net/get-pdb/1723220/36e98f99-d5a9-4359-ac9c-3e59449f877e/s1200?webp=false'
  }
}
let bill = 0

function getCatalog (items = products) {
  const listOl = document.createElement('ol')

  for (let item in items) {
    const listLi = document.createElement('li')
    const liBtn = document.createElement('button')
    const liImg = document.createElement('img')

    liImg.src = items[item].url
    liImg.style.width = "5rem"
    liImg.style.transition = "all .5s"
    liImg.onmouseenter = () => {liImg.style.width = "20rem"}
    liImg.onmouseleave = () => {liImg.style.width = "5rem"}

    liBtn.innerHTML = "Добавить в корзину"
    liBtn.style.margin = "0 1rem"
    liBtn.onclick = () => {bill += items[item].price}

    listLi.innerHTML = `${item}: ${items[item].price}$`
    listLi.style.padding = '0.5rem'

    listLi.appendChild(liBtn)
    listLi.appendChild(liImg)
    listOl.appendChild(listLi)
  }

  document.getElementById('catalogToInsert').appendChild(listOl)
}

function calcPaymentBill() {
  shoppingDonor.innerHTML = `Общая сумма покупок: ${bill}$`
  shoppingDonor.style.backgroundColor = `${
    colors[Math
      .floor(Math.random() * (Object.keys(colors).length - 1 + 1)) + 0]}`
}
// function calcShoppingCart () {
//   const count = Math.floor(Math.random() * (Object.keys(products).length - 1 + 1)) + 0
//   let result = 0
//   let i = 0

//   for (const product in products) {
//     result += products[product]

//     if (i === count) {
//       if (i === 0) {
//         shoppingDonor.innerHTML = 'В Вашей корзине нет товаров!'
//       } else {
//         shoppingDonor.innerHTML = `Количество товаров: ${i}<br />Общая сумма покупок: ${result}$`
//       }

//       break
//     }
    
//     i++
//   }
// }

getCatalog()
setInterval(() => {
  calcPaymentBill()
}, 1000)