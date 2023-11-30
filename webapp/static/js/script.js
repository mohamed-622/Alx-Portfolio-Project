// Main script wrapped in an IIFE to encapsulate variables
(function ($) {
  // Document ready function
  $(document).ready(function () {
    // Initialize Flatpickr for dateInput
    flatpickr("#reserved_date", {
      enableTime: false,
      dateFormat: "Y-m-d",
      minDate: "today",
      maxDate: new Date().fp_incr(30),
    });

    // Get references to the time slot dropdown and date input
    const timeSlotDropdown = $("#time_slot");
    const dateInput = $("#reserved_date");

    // Disable the time slot dropdown until a date is selected
    timeSlotDropdown.prop("disabled", true);

    // Event handler for date input change
    dateInput.change(function () {
      const selectedDate = dateInput.val();
      console.log("Date selected:", selectedDate);
      updateAvailableTimeSlots(selectedDate);
    });

    // Function to update available time slots based on selected date
    function updateAvailableTimeSlots(selectedDate) {
      console.log("Fetching available time slots for:", selectedDate);

      // Send an AJAX request to get the available time slots
      $.ajax({
        url: `/get_available_time_slots?date=${selectedDate}`,
        method: "GET",
        success: function (data) {
          console.log("Data:", data);
          enableTimeSlots(data);
        },
        error: function (error) {
          console.log("Error:", error);
        },
      });

      // Function to enable/disable time slots based on availability data
      function enableTimeSlots(data) {      
        // Enable the time slot dropdown
        timeSlotDropdown.prop("disabled", false);
      
        // Reset dropdown options and show all time slots
        timeSlotDropdown.find("option").show();

        // Mark booked time slots as red and disable them
        data.bookedSlots.forEach(function (bookedSlot) {
          timeSlotDropdown.find(`option[value='${bookedSlot}']`).prop("disabled", true).css("background-color", "red");
        });
      }      
    }
  });
})(jQuery);


// Function to delete a booking using AJAX
function deleteBooking(bookingId) {
  fetch(`/delete_booking/${bookingId}`, {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
    },
  })
  .then(response => response.json())
  .then(data => {
    console.log(data);
    location.reload();
  })
  .catch(error => console.error('Error:', error));
}
