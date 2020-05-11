from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
#from models import User
#from ..app import db

## GOOD DATA ##
eventtitle = 'Test Event'
eventdesc = 'We are testing this.'
starttime = '2020-05-10 08:30:00'
endtime = '2020-05-01 09:30:00'

def test_add_event():
    from .main.main import events_post
    assert events_post == redirect(url_for('main.calendar'))
