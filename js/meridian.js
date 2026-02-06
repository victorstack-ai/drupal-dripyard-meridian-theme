(function (Drupal, once) {
  Drupal.behaviors.meridianHeader = {
    attach(context) {
      once('meridian-header', '.meridian-header', context).forEach((header) => {
        const sentinel = document.createElement('div');
        sentinel.className = 'meridian-sentinel';
        header.after(sentinel);

        const observer = new IntersectionObserver(
          (entries) => {
            entries.forEach((entry) => {
              header.classList.toggle('is-anchored', !entry.isIntersecting);
            });
          },
          { threshold: 1.0 }
        );

        observer.observe(sentinel);
      });
    },
  };
})(Drupal, once);
