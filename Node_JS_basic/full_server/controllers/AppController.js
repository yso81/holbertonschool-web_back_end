class AppController {
  /**
   * Static method to handle the homepage request
   * @param {object} req request object from Express
   * @param {object} res response object from Express
   */
  static getHomepage(req, res) {
    res.status(200).send('Hello Holberton School!');
  }
}

module.exports = AppController;
