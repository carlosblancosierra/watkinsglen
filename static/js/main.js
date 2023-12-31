var owlProduct;

$(document).ready(function () {
      let owlProduct = $('.owl-carousel-main').owlCarousel({
        loop:true,
        margin:10,
        responsive:{
            0:{
                items:1.2
            },
            1000 :{
                items:2.2
            }
        },
        mouseDrag: true,
        nav: true, // Show navigation arrows
        dots: true,
    })

    // Initialize the miniature strip carousel
    $(".miniature-strip").owlCarousel({
        items: 3,
        center: true,
        dots: false,
        nav: true,
        margin: 10,
        responsive: {
            0: {
                items: 4,
            },

        },
        URLhashListener: true,
        startPosition: 'URLHash',
        // Connect the miniature strip to the main carousel
        onInitialized: function (event) {
            event.item.index = event.page.index - 1;
            var currentIndex = event.item.index;
            var mainCarousel = $(".owl-carousel-main").data('owl.carousel');
            mainCarousel.to(currentIndex);
        },
    });

    $(".owl-carousel-featured").each(function () {
            $(this).owlCarousel({
                items: 1,
                loop: true,
                margin: 10,
                autoplay: true,
                autoplayTimeout: 3000, // Adjust as needed
                nav: true,
                dots: false,
                navText : ['<i class="fa-solid fa-chevron-left"></i>','<i class="fa-solid fa-chevron-right"></i>']

            });
        });

    // Thumbnail Carousel
        $(".thumbnail-carousel").owlCarousel({
            items: 3, // Number of thumbnail items to display
            margin: 10, // Margin between thumbnail items
            dots: false, // Disable dots in the thumbnail carousel
            nav: false, // Disable navigation arrows for the thumbnails
            responsive: {
                0: {
                    items: 3 // Adjust the number of thumbnail items for different screen sizes if needed
                },
                768: {
                    items: 6
                }
            },
            // Use the `sync` option to connect the thumbnail carousel to the main carousel
            // This syncs the thumbnail and main carousel
            sync: ".owl-carousel-main"
        });
});