import Building from './5-building.js';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    //pass sqft to the parent class (Building)
    super(sqft);
    this._floors = floors;
  }

  //getter for floors
  get floors() {
    return this._floors;
  }

  //override method
  evacuationWarningMessage() {
    return `Evacuate slowly the ${this.floors} floors`;
  }
}
