from flask import render_template

from mass_flask_core.models import Report
from mass_flask_webui.config import webui_blueprint


@webui_blueprint.route('/report/<report_id>/')
def report_detail(report_id):
    report = Report.objects(id=report_id).first()
    return render_template('report_generic.html', report=report)
