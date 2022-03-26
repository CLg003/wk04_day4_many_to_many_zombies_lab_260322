from flask import Blueprint, Flask, redirect, render_template, request

from models.biting import Biting
import repositories.biting_repository as biting_repository

bitings_blueprint = Blueprint("bitings", __name__)

# INDEX
@bitings_blueprint.route('/bitings')
def bitings():
    bitings = biting_repository.select_all()
    return render_template('bitings/index.html', bitings=bitings)

# NEW
@bitings_blueprint.route('/bitings/new')
def new():
    return render_template('bitings/new.html')

# CREATE

# EDIT

# UPDATE

# DELETE
