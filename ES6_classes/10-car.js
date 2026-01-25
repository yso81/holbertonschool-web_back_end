export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  cloneCar() {
    const TestCar = this.constructor[Symbol.testCar] || this.constructor;
    return new TestCar(this._brand, this._motor, this._color);
  }
}
