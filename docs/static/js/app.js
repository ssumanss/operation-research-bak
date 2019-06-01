try {
  navigator.serviceWorker
           .register('/complex-analysis/sw.js')
           .then(function() { console.log("Service Worker Registered"); });
} catch (error) {
 console.log(error.message) 
}