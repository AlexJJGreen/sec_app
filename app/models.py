from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#sec data tables

class num(db.Model):
    adsh = db.Column(db.String(20))
    tag = db.Column(db.String(200))
    version = db.Column(db.String(20))
    coreg = db.Column(db.Float())
    ddate = db.Column(db.Integer)
    qtrs = db.Column(db.Integer)
    uom = db.Column(db.String(20))
    value = db.Column(db.Float())
    footnote = db.Column(db.Float())

class pre(db.Model):
    adsh = db.Column(db.String(20))
    report = db.Column(db.Integer)
    line = db.Column(db.Integer)
    stmt = db.Column(db.String(2))
    inpth = db.Column(db.Integer)
    rfile = db.Column(db.String(1))
    tag = db.Column(db.String(198))
    version = db.Column(db.String(20))
    plabel = db.Column(db.Text(264207))
    negating = db.Column(db.Integer)

class sub(db.Model):
    adsh = db.Column(db.String(20))
    cik = db.Column(db.Integer)
    name = db.Column(db.String(100))
    sic = db.Column(db.Float())
    countryba = db.Column(db.String(3))
    stprba = db.Column(db.String(3))
    cityba = db.Column(db.String(30))
    zipba
    bas1 = db.Column(db.String(40))
    bas2 = db.Column(db.String(40))
    baph = db.Column(db.String(20))
    countryma = db.Column(db.String(3))
    stprma = db.Column(db.String(3))
    cityma = db.Column(db.String(30))
    zipma = db.Column(db.String(10))
    mas1 = db.Column(db.String(40))
    mas2 = db.Column(db.String(40))
    countryinc = db.Column(db.String(3))
    stprinc = db.Column(db.String(3))
    ein = db.Column(db.String(11))
    former = db.Column(db.String(100))
    changed = db.Column(db.Float())
    afs = db.Column(db.Float())
    wksi = db.Column(db.Integer)
    fye = db.Column(db.Float())
    form = db.Column(db.String())
    period = db.Column(db.Integer)
    fy = db.Column(db.Float())
    fp = db.Column(db.Float())
    filed = db.Column(db.Integer)
    accepted = db.Column(db.String(21))
    prevrpt = db.Column(db.Float())
    detail = db.Column(db.Integer)
    instance = db.Column(db.String(32))
    nciks = db.Column(db.Integer)
    aciks = db.Column(db.Float())

            tag
                tag	version	custom	abstract	datatype	iord	crdr	tlabel	doc
