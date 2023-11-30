from . import db
from .models import Booking
from datetime import datetime
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required, current_user
from flask import jsonify
from sqlalchemy import and_


# Create a Blueprint for the views
views = Blueprint('views', __name__)


# Define the routes and their handlers

@views.route('/', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def home():
    """
    Render the home page.

    Returns:
        Rendered template with user information.
    """
    return render_template("home.html", user=current_user)


@views.route('/booking', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def booking():
    """
    Handle booking requests.

    Returns:
        Rendered template for booking or redirects to the booking page after a successful booking.
    """
    if request.method == 'POST':
        
        # Process form data for booking
        time_slot = request.form.get('time_slot')
        reserved_date = request.form.get('reserved_date')
        start_time, end_time = time_slot.split('-')
        start_time_obj = datetime.strptime(start_time, '%H:%M').time()
        end_time_obj = datetime.strptime(end_time, '%H:%M').time()
               
        try:
            reserved_date = datetime.strptime(reserved_date, '%Y-%m-%d').date()
        except ValueError:
            flash('Date format: YYYY-MM-DD', category='error')
            return render_template("booking.html", user=current_user)
        
        # Check if the booking already exists
        overlapping_booking = Booking.query.filter(
                and_(
                    Booking.user_id == current_user.id,
                    Booking.reserved_date == reserved_date,
                    Booking.start_time < end_time_obj,
                    Booking.end_time > start_time_obj
                )
            ).first()
            
        if overlapping_booking:
            flash('This time slot is already booked', category='error')
        else:
            new_booking = Booking(start_time=start_time, end_time=end_time, reserved_date=reserved_date, user_id=current_user.id)
            db.session.add(new_booking)
            db.session.commit()
            flash('Booking added!', category='success')
            # redirect to booking page
            return redirect(url_for('views.home')) 
            
    return render_template("booking.html", user=current_user)


@views.route('/delete_booking/<int:booking_id>', methods=['DELETE'])
@login_required
def delete_booking(booking_id):
    """
    Handle booking deletion.

    Args:
        booking_id (int): The ID of the booking to delete.

    Returns:
        JSON response indicating success or failure of the deletion.
    """
    
    # Get the booking from the database
    booking = Booking.query.get(booking_id)

    # Check if the booking exists and belongs to the current user
    if booking and booking.user_id == current_user.id:
        # Delete the booking from the database
        db.session.delete(booking)
        db.session.commit()
        return jsonify({'message': 'Booking deleted successfully'})

    # If the booking doesn't exist or doesn't belong to the user, return an error
    return jsonify({'error': 'Booking not found or unauthorized'}), 404


@views.route('/get_available_time_slots', methods=['GET'])
@login_required
def get_availability():
    """
    Provide availability information for a selected date.

    Returns:
        JSON response containing booked and available time slots for the selected date.
    """
    
    # Get the selected date from the request arguments
    try:
        selected_date_str = request.args.get('date')
        selected_date = datetime.strptime(selected_date_str, '%Y-%m-%d').date()
    except ValueError:
        return jsonify({'error': 'Invalid date format'}), 400

    # Get all bookings for the selected date
    bookings_for_date = Booking.query.filter_by(reserved_date=selected_date).all()

    # Extract booked time slots
    booked_slots = [
    f"{datetime.strptime(booking.start_time, '%H:%M').time().strftime('%H:%M')}-{datetime.strptime(booking.end_time, '%H:%M').time().strftime('%H:%M')}"
    if isinstance(booking.start_time, str) and isinstance(booking.end_time, str)
    else f"{booking.start_time.strftime('%H:%M')}-{booking.end_time.strftime('%H:%M')}"
    for booking in bookings_for_date
    ]

    # Define all possible time slots (adjust as needed)
    all_time_slots = [
        "08:00-09:00", "09:00-10:00", "10:00-11:00", "11:00-12:00", "12:00-13:00",
        "13:00-14:00", "14:00-15:00", "15:00-16:00", "16:00-17:00", "17:00-18:00",
        "18:00-19:00", "19:00-20:00", "20:00-21:00", "21:00-22:00", "22:00-23:00"
    ]

    # Determine available time slots
    available_slots = list(set(all_time_slots) - set(booked_slots))

    # Return the availability data as JSON
    return jsonify({'bookedSlots': booked_slots, 'availableSlots': available_slots})