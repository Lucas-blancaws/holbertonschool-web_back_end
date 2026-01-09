import { readDatabase } from '../utils';

class StudentsController {
  static getAllStudents(request, response) {
    const databaseFile = process.argv[2];

    readDatabase(databaseFile)
      .then((fields) => {
        let output = 'This is the list of our students';
        
        // Tri des clés (filières) par ordre alphabétique insensible à la casse
        const sortedFields = Object.keys(fields).sort((a, b) => 
          a.toLowerCase().localeCompare(b.toLowerCase())
        );

        sortedFields.forEach((field) => {
          const list = fields[field];
          output += `\nNumber of students in ${field}: ${list.length}. List: ${list.join(', ')}`;
        });

        response.status(200).send(output);
      })
      .catch(() => {
        response.status(500).send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(request, response) {
    const databaseFile = process.argv[2];
    const { major } = request.params;

    if (major !== 'CS' && major !== 'SWE') {
      response.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    readDatabase(databaseFile)
      .then((fields) => {
        const students = fields[major] || [];
        response.status(200).send(`List: ${students.join(', ')}`);
      })
      .catch(() => {
        response.status(500).send('Cannot load the database');
      });
  }
}

export default StudentsController;
