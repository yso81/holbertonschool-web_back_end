process.stdin.setEncoding('utf-8');
process.stdout.write("Welcome to Holberton School, what is your name?\n");

process.stdin.on("readable", () => {
  const input = process.stdin.read();
  if (input) {
    process.stdout.write(`Your name is: ${input}`);
  }
});
/**
 * If stdout process in stream comes from the terminal, end the process
 * with a message
 */
process.stdin.on("end", () => {
  process.stdout.write("This important software is now closing\n");
});
