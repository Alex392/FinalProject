import calendar

import flask
from flask import render_template

calendar_bp = flask.Blueprint('cal', __name__, template_folder='templates')


@calendar_bp.route('/<int:year>/<int:month>')
def random_cal(year, month):
    tc = calendar.HTMLCalendar(firstweekday=0)
    tc.cssclasses = ["mon bg-primary", "tue", "wed", "thu", "fri", "sat", "sun"]
    tc.cssclass_month = "table"
    # print(tc.formatmonth(year, month))
    return render_template("calendar.html", calendar=custformat(tc, year, month))


def custformat(c, theyear, themonth, withyear=True):
    """
    Return a formatted month as a table.
    """
    v = []
    a = v.append
    a('<table border="0" cellpadding="0" cellspacing="0" class="%s">' % (
        c.cssclass_month))
    a('\n')
    a(c.formatmonthname(theyear, themonth, withyear=withyear))
    a('\n')
    a(c.formatweekheader())
    a('\n')
    for week in c.monthdays2calendar(theyear, themonth):
        a(custformatweek(c, week))
        a('\n')
    a('</table>')
    a('\n')
    return ''.join(v)


def custformatweek(c, theweek):
    """
    Return a complete week as a table row.
    """
    s = ''.join(custformatday(c, d, wd) for (d, wd) in theweek)
    return '<tr>%s</tr>' % s


def custformatday(c, day, weekday):
    """
    Return a day as a table cell.
    """
    if day == 0:
        # day outside month
        return '<td class="%s">&nbsp;</td>' % "noday"
    else:
        return '<td class="%s">%s</td>' % (c.cssclasses[weekday], str(day) + get_event(day))

# TODO do something better than this
def get_event(day):
    # don't forget you have access to year and month
    return "<div class='bg-danger'>I'm an event</div>"
