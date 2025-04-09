document.addEventListener("DOMContentLoaded", function() {
    const excludeElements = document.getElementsByClassName("exclude");
    const toExclude = Array.from(excludeElements).map(element => element.id);

    const tocLinks = document.querySelectorAll(`[data-md-component="toc"] a`);

    console.log(Array.from(excludeElements).map(element => element.innerText))

    tocLinks.forEach(link => {
      toExclude.forEach(id => {
        if (link.href.includes(id)) {
          link.classList.add('hidden');
        }
      });
    });
});