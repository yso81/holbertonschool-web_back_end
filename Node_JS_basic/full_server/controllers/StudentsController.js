const readDatabase = require('../utils');

class StudentsController {
  /**
   * Static method to handle the request for all students
   * Displays student counts and names by field
   * @param {object} req request object from Express
   * @param {object} res response object from Express
   */
  static async getAllStudents(req, res) {
    const databasePath = process.argv[2];

    if (!databasePath) {
      return res.status(500).send('Cannot load the database');
    }

    try {
      const studentsByField = await readDatabase(databasePath);
      let responseText = 'This is the list of our students';

      let totalStudents = 0;
      for (const field in studentsByField) {
        if (Object.hasOwnProperty.call(studentsByField, field)) {
          totalStudents += studentsByField[field].length;
        }
      }

      const sortedFields = Object.keys(studentsByField).sort((a, b) =>
        a.toLowerCase().localeCompare(b.toLowerCase())
      );

      for (const field of sortedFields) {
        const studentNames = studentsByField[field];
        responseText += `\nNumber of students in ${field}: ${studentNames.length}. List: ${studentNames.join(', ')}`;
      }

      res.status(200).send(responseText);
    } catch (error) {
      res.status(500).send('Cannot load the database');
    }
  }

  /**
   * Static method to handle the request for students by major
   * @param {object} req request from Express
   * @param {object} res response from Express
   */
  static async getAllStudentsByMajor(req, res) {
    const databasePath = process.argv[2];
    const major = req.params.major;
    if (major !== 'CS' && major !== 'SWE') {
      return res.status(500).send('Major parameter must be CS or SWE');
    }

    if (!databasePath) {
      return res.status(500).send('Cannot load the database');
    }

    try {
      const studentsByField = await readDatabase(databasePath);

      if (!studentsByField[major]) {
        return res.status(200).send(`List: `);
      }

      const studentNames = studentsByField[major];
      res.status(200).send(`List: ${studentNames.join(', ')}`);
    } catch (error) {
      res.status(500).send('Cannot load the database');
    }
  }
}

module.exports = StudentsController;
