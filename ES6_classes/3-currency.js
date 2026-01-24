export default class Currency {
  constructor (code, name) {
    this.code = code;
    this.name = name;
  }

  //code Getter & Setter
  get code() {
    return this._code
  }

  set code(value) {
    return this._code = value
  }

  //code Getter & Setter
  get name() {
    return this._name
  }

  set name(value) {
    this._name = value
  }

  //Method
  displayFullCurrency() {
    return `${this.name} (${this.code})`;
  }
}
