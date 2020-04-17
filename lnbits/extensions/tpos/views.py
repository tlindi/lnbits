from flask import g, abort, render_template

from lnbits.decorators import check_user_exists, validate_uuids
from lnbits.helpers import Status

from lnbits.extensions.tpos import tpos_ext
from .crud import get_tpos


@tpos_ext.route("/")
@validate_uuids(["usr"], required=True)
@check_user_exists()
def index():
    return render_template("tpos/index.html", user=g.user)


@tpos_ext.route("/<tpos_id>")
def tpos(tpos_id):
    tpos = get_tpos(tpos_id) or abort(Status.NOT_FOUND, "TPoS does not exist.")

    return render_template("tpos/tpos.html", tpos=tpos)
