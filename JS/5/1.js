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
    document.getElementById('toInsert').appendChild(tr)
  }
  for (let letter of columns) {
    const td = document.createElement('td')

    td.style.width = '50px'
    td.style.height = '50px'
    td.innerHTML = letter

    trr.appendChild(td)
  }
  document.getElementById('toInsert').appendChild(trr)
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

createChessTable();
colorifyChessTable();