function createChessTable(size = 8) {
  let isBlack = true
  const trr = document.createElement('tr')
  const columns = [
    '',
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h'
  ]
  for (let i = 0; i < size; i++) {
    const tr = document.createElement('tr')
    const tdd = document.createElement('td')

    tdd.style.height = '50px'
    tdd.style.width = '50px'
    tdd.innerHTML = 8 - i
    tr.appendChild(tdd)

    for (let j = 0; j < size; j++) {
      const td = document.createElement('td')

      if (j == 0) {
        isBlack = !isBlack
      }

      td.id = `${i}-${j}`
      td.style.height = '50px'
      td.style.width = '50px'

      if (isBlack) {
        td.className = 'main__block main_black'
      } else {
        td.className = 'main__block main_white'
      }

      tr.appendChild(td)
      isBlack = !isBlack;
    }
    document.getElementById('chessToInsert').appendChild(tr)
  }
  for (let letter of columns) {
    const td = document.createElement('td')

    td.style.width = '50px'
    td.style.height = '50px'
    td.innerHTML = letter

    trr.appendChild(td)
  }
  document.getElementById('chessToInsert').appendChild(trr)
}

function colorifyChessTable() {
  const classNames = {
    main_black: 'black',
    main_white: 'white'
  };

  for (const className in classNames) {
    for (const elem of document.getElementsByClassName(className)) {
      elem.style.background = classNames[className];
    }
  }
}

function placeFiguresRandom(size = 7) {
  /*
    В задании не упомянуто, в каком количестве и на каких позициях добавлять фигуры, поэтому я сделаю произвольную расстановку
    на основе генератора псевдослучайных чисел
   */
  const figures = [
    'К',
    'Ф',
    'П',
    'Кн',
    'С'
  ]

  for (let i = 0; i < size; i++) {
    const iD = `${Math.floor(Math.random() * (7 - 1 + 1)) + 1}-${Math.floor(Math.random() * (7 - 1 + 1)) + 1}`
    const figure = figures[Math.floor(Math.random() * (figures.length - 1 + 1)) + 0]
    const donor = document.getElementById(iD)

    if (donor.className.split(' ')[1] === 'main_black') {
      donor.style.color = 'white'
    }

    document.getElementById(iD).innerHTML = figure

  }
}

createChessTable()
colorifyChessTable()
placeFiguresRandom()