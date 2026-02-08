const express = require('express');
const fs = require('fs').promises;
const app = express();
const port = 1245;

async function countStudents(filePath) {
    return new Promise((resolve, reject) => {
        fs.readFile(filePath, { encoding: 'utf-8'})
            .then((data) => {
                const lines = data.split('\n').filter(line => line.trim() !== '');
                if (lines.length === 0) {
                    resolve('This is the list of our students\nNumber of students: 0');
                    return;
                }

                const students = lines.slice(1).map(line => line.split(','));
                const studentCountByField = {};
                const studentsNameByField = {};
                let totalStudents = 0;
                students.forEach(student => {
                    if (student.length === 4) {
                        const field = student[3].trim();
                        const firstName = student[0].trim();
                        if (!studentCountsByField[field]) {
                            studentCountByField[field] = 0;
                            studentsNameByField[field] = [];
                        }
                        studentCountByField[field]++;
                        studentsNameByField[field].push(firstName);
                        totalStudents++;
                    }
                });
                let result = `This is the list of our dtudents\nNumber of students: ${totalStudents}`;
                for (const field in studentCountByField) {
                    if (Object.hasOwnProperty.call(studentCountByField, field)) {
                        result += `\nNumber of students in ${field}: ${studentCountByField[field]}. List: 
${studentsNameByField[field].join(', ')}`;
                    }
                }
                resolve(result);
        })
        .catch(() => {
            reject(new Error('Cannot load the database'));
        });
    });
}

app.get('/', (req, res) => {
    res.setHeader('Content-Type', 'text/plain');
    res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
    res.setHeader('Content-Type', "text/plain");
    const databasePath = process.argv[2];
    if(!databasePath) {
        res.status(500).send(`This is the list of our students\nCannot load the database`);
        return;
    }
    try {
    const studentData = await countStudents(databasePath);
    res.status(200).send(studentData);
  } catch (error) {
    res.status(500).send(`This is the list of our students\n${error.message}`);
  }
});

if (require.main === module) {
    app.listen(port, () => {
        console.log(`server is listening on port ${port}`);
    });
}

module.exports = app;
