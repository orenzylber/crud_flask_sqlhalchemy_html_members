## This is a project that contains:
# Flask
# SQLalchemy
# Cors
# CRUD
# HTML page
# requirements.txt

# simple example

live site:
# on NETLIFY:
https://vocal-pie-b49450.netlify.app/

# Update DB Create
    with app.app_context():
        db.create_all()
        app.run(debug=True)

# prepare the invironment & requirements
    python -m virtualenv myenv
    myenv\Scripts\activate
    pip install -r .\requirements.txt




