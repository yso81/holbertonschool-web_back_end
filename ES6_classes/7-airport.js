export default class Airport {
  constructor(name, code) {
    this._name = name;
    this._code = code;
  }

  //modifies the string description: [object Object] -> [object CODE]
  get [Symbol.toStringTag]() {
    return this._code;
  }
}
