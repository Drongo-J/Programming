function Scroll(){
      // Get a reference to the target element
  const targetElement = document.getElementById('main');
  
  // Use the scrollTo() method to scroll to the target element
  targetElement.scrollIntoView({ behavior: 'smooth'});
}

function SetProgressBarsRandomly(){ 
    const progressBars = document.querySelectorAll(".progress-bar-filled");

    progressBars.forEach(function (bar) {
        bar.style.width = Math.max(50, Math.floor(Math.random() * 100)) + "%";
    });
}

SetProgressBarsRandomly();