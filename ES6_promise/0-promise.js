export default function getResponseFromAPI() {
  return new Promise((resolve) => {
    // Simulate an asynchronous API call
    setTimeout(() => {
      resolve("This is the API response!");
    }, 1000);
  });
}
