const fs = require('fs').promises;

const readDatabase = (filePath) => {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, { encoding: 'utf8' })
      .then((data) => {
        const lines = data.split('\n').filter(line => line.trim() !== '');

        if (lines.length === 0) {
          resolve({});
          return;
        }

        const studentLines = lines.slice(1);

        const studentsByField = {};

        studentLines.forEach(line => {
          const student = line.split(',');
          if (student.length === 4) { // firstname, lastname, age, field
            const firstName = student[0].trim();
            const field = student[3].trim();

            if (!studentsByField[field]) {
              studentsByField[field] = [];
            }
            studentsByField[field].push(firstName);
          }
        });
        resolve(studentsByField);
      })
      .catch(() => {
        reject(new Error('Cannot load the database'));
      });
  });
};

module.exports = readDatabase;
