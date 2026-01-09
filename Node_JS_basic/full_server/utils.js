import fs from 'fs';

const readDatabase = (filePath) => new Promise((resolve, reject) => {
  fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
      reject(err);
      return;
    }
    const students = {};
    const lines = data.toString().trim().split('\n');
    for (const line of lines) {
      if (line) {
        const [firstname, , , field] = line.split(',');
        if (field && field !== 'field') {
          if (!students[field]) students[field] = [];
          students[field].push(firstname);
        }
      }
    }
    resolve(students);
  });
});

export default readDatabase;
