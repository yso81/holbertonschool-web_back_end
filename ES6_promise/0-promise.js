export default function getResponseFromAPI() {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve("This is the API response!");
    }, 1000);
  }
);
}