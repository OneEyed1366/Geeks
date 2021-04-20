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
let proceedAdress = false
let proceedComments = false

function hideAndSeek(whos, show = none) {
  const elem = document.getElementById(whos)

  elem.style.display = show
} 

function getCatalog (items = products) {
  const listOl = document.createElement('ol')

  for (let item in items) {
    const listLi = document.createElement('li')
    const liBtnDel = document.createElement('button')
    const liImg = document.createElement('img')
    /* Предположим, что пользователь уже выбрал свои товары. В таком случае, оставим возможность лишь удалять товары */
    bill += items[item].price

    liImg.src = items[item].url
    liImg.style.width = "5rem"
    liImg.style.transition = "all .5s"
    liImg.onmouseenter = () => {liImg.style.width = "20rem"}
    liImg.onmouseleave = () => {liImg.style.width = "5rem"}

    liBtnDel.innerHTML = "Удалить из корзины"
    liBtnDel.style.margin = "0 1rem"
    liBtnDel.onclick = () => {(bill >= 0) && (
      bill - items[item].price >= 0) ? bill -= items[item].price : console.log(
        'Вы не добавили товар в корзину!')}

    listLi.innerHTML = `${item}: ${items[item].price}$`
    listLi.style.padding = '0.5rem'

    listLi.appendChild(liBtnDel)
    listLi.appendChild(liImg)
    listOl.appendChild(listLi)
  }

  document.getElementById('catalogToInsert').appendChild(listOl)
}

function calcPaymentBill() {
  if (bill == 0) {
    shoppingDonor.innerHTML = 'Ваша корзина пуста!'
  } else {
    shoppingDonor.innerHTML = `Общая сумма покупок: ${bill}$`
  }
}

getCatalog()
setInterval(() => {
  calcPaymentBill()
  hideAndSeek('shoppingAdress', proceedAdress)
}, 1000)