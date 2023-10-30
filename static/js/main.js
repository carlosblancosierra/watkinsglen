var owlProduct;

$(document).ready(function () {
      let owlProduct = $('.owl-carousel-main').owlCarousel({
        loop:true,
        margin:10,
        responsive:{
            0:{
                items:1
            }
        },
        mouseDrag: true,
        nav: true, // Show navigation arrows
        dots: true,

    })

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