function splitIntoObject(num) {
  const error = `Ошибка! Ваше число ${num} больше 999!`
  // let result = {}

  // if (num <= 999) {
  //   result['единицы'] = num.toString().split('')[0]
  //   result['десятки'] = num.toString().split('')[1]
  //   result['сотни'] = num.toString().split('')[2]

  //   return result
  // } else {
  //   return error
  // }

  if (num <= 999) {
    return (
      {
        'единицы': num.toString().split('')[0],
        'десятки': num.toString().split('')[1],
        'сотни': num.toString().split('')[2]
      }
    )
  } else {
    return error
  }
}

console.log(splitIntoObject(999))