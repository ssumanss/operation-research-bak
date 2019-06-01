try {
  navigator.serviceWorker
           .register('../../sw.js')
           .then(function() { console.log("Service Worker Registered"); });
} catch (error) {
 console.log(error.message) 
}