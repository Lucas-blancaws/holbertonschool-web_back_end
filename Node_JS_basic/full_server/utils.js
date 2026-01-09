import fs from 'fs';

export const readDatabase = (filePath) => {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf8', (err, data) => {
      if (err) {
        reject(err);
        return;
      }

      const students = {};
      const lines = data.toString().trim().split('\n');

      for (const line of lines) {
        if (line) {
          const [firstname, lastname, age, field] = line.split(',');

          // On ignore l'en-tête ou les lignes vides si nécessaire
          if (field && field !== 'field') {
            if (!students[field]) {
              students[field] = [];
            }
            students[field].push(firstname);
          }
        }
      }
      resolve(students);
    });
  });
};